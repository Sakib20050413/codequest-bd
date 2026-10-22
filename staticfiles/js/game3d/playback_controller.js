/**
 * CodeQuest 3D - Reactive Playback Controller
 * Interpolates Action Queue steps on RoverWorld3D with speed scaling,
 * step-by-step debug stepping, and active code line highlighting.
 */

class PlaybackController {
    constructor(world3D, options = {}) {
        this.world = world3D;
        this.interpreter = new ActionInterpreter({
            cols: world3D.cols,
            rows: world3D.rows,
            start: world3D.startPos,
            portal: world3D.portalPos,
            obstacles: world3D.obstacles,
            gems: world3D.gems,
        });

        this.levelId = options.levelId;
        this.csrfToken = options.csrfToken || '';
        this.onCompleteCallback = options.onComplete || null;

        // Playback state
        this.actionQueue = [];
        this.currentIndex = 0;
        this.isPlaying = false;
        this.speed = 1.0; // 1x, 2x, 4x
        this.stepDuration = 400; // ms per step at 1x
        this.animFrameId = null;

        // Interpolation
        this.isInterpolating = false;
        this.interpStartTime = 0;
        this.currentAction = null;
        this.fromPos = null;
        this.toPos = null;
        this.fromAngle = 0;
        this.toAngle = 0;

        this.initDOM();
    }

    initDOM() {
        this.btnPlay = document.getElementById('btn-play-run');
        this.btnPause = document.getElementById('btn-pause');
        this.btnStep = document.getElementById('btn-step');
        this.btnReset = document.getElementById('btn-reset');
        this.speedSelector = document.getElementById('speed-selector');
        this.statusText = document.getElementById('playback-status-text');
        this.codeEditor = document.getElementById('code-editor');

        if (this.btnPlay) this.btnPlay.addEventListener('click', () => this.handlePlay());
        if (this.btnPause) this.btnPause.addEventListener('click', () => this.pause());
        if (this.btnStep) this.btnStep.addEventListener('click', () => this.stepForward());
        if (this.btnReset) this.btnReset.addEventListener('click', () => this.reset());

        const speedBtns = document.querySelectorAll('.speed-btn');
        speedBtns.forEach(btn => {
            btn.addEventListener('click', (e) => {
                const spd = parseFloat(e.target.dataset.speed || '1');
                this.setSpeed(spd);
                speedBtns.forEach(b => b.classList.remove('bg-emerald-500', 'text-slate-950', 'font-bold'));
                e.target.classList.add('bg-emerald-500', 'text-slate-950', 'font-bold');
            });
        });
    }

    setSpeed(speedMultiplier) {
        this.speed = speedMultiplier;
        this.stepDuration = 400 / this.speed;
    }

    setStatus(text, isError = false) {
        if (this.statusText) {
            this.statusText.textContent = text;
            this.statusText.className = isError 
                ? 'text-xs font-mono text-rose-400 font-semibold' 
                : 'text-xs font-mono text-emerald-400 font-semibold';
        }
    }

    handlePlay() {
        if (!this.isPlaying) {
            // If at the beginning or complete, re-parse code
            if (this.actionQueue.length === 0 || this.currentIndex >= this.actionQueue.length) {
                const langSelect = document.getElementById('language-select');
                const lang = langSelect ? langSelect.value : 'python';
                const code = this.codeEditor ? this.codeEditor.value : '';

                this.world.reset();
                this.setStatus("Compiling and generating 3D action queue...");

                const result = this.interpreter.execute(lang, code);
                if (!result.success) {
                    this.setStatus(`Error: ${result.error}`, true);
                    if (window.soundEngine) window.soundEngine.playError();
                    return;
                }

                if (result.actions.length === 0) {
                    this.setStatus("Code executed but rover took no actions.", true);
                    return;
                }

                this.actionQueue = result.actions;
                this.currentIndex = 0;
                this.execSummary = result;
            }

            this.isPlaying = true;
            this.updateButtonStates();
            this.runNextAction();
        }
    }

    pause() {
        this.isPlaying = false;
        this.updateButtonStates();
        this.setStatus(`Paused at action ${this.currentIndex} of ${this.actionQueue.length}`);
    }

    stepForward() {
        if (this.isInterpolating) return;

        if (this.actionQueue.length === 0 || this.currentIndex >= this.actionQueue.length) {
            const langSelect = document.getElementById('language-select');
            const lang = langSelect ? langSelect.value : 'python';
            const code = this.codeEditor ? this.codeEditor.value : '';

            this.world.reset();
            const result = this.interpreter.execute(lang, code);
            if (!result.success) {
                this.setStatus(`Error: ${result.error}`, true);
                return;
            }
            this.actionQueue = result.actions;
            this.currentIndex = 0;
            this.execSummary = result;
        }

        this.isPlaying = false;
        this.updateButtonStates();
        this.executeSingleStep();
    }

    reset() {
        this.isPlaying = false;
        this.isInterpolating = false;
        this.actionQueue = [];
        this.currentIndex = 0;
        this.world.reset();
        this.updateButtonStates();
        this.setStatus("3D Stage Reset. Ready to execute.");
        this.clearLineHighlight();
    }

    updateButtonStates() {
        if (this.btnPlay) {
            if (this.isPlaying) {
                this.btnPlay.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Running...';
                this.btnPlay.disabled = true;
            } else {
                this.btnPlay.innerHTML = '<i class="fa-solid fa-play"></i> Run 3D Rover';
                this.btnPlay.disabled = false;
            }
        }
    }

    runNextAction() {
        if (!this.isPlaying) return;

        if (this.currentIndex >= this.actionQueue.length) {
            this.finishExecution();
            return;
        }

        this.executeSingleStep(() => {
            if (this.isPlaying) {
                this.runNextAction();
            }
        });
    }

    executeSingleStep(onStepDone) {
        if (this.currentIndex >= this.actionQueue.length) {
            this.finishExecution();
            return;
        }

        const action = this.actionQueue[this.currentIndex];
        this.currentAction = action;
        this.highlightCodeLine(action.line);

        if (action.type === 'MOVE') {
            this.isInterpolating = true;
            this.interpStartTime = performance.now();
            this.fromPos = this.world.gridToWorld(action.from.x, action.from.z);
            this.toPos = this.world.gridToWorld(action.to.x, action.to.z);

            if (window.soundEngine) window.soundEngine.playMove();

            const animateMove = (now) => {
                const elapsed = now - this.interpStartTime;
                const progress = Math.min(1.0, elapsed / this.stepDuration);

                // Ease out cubic
                const t = 1 - Math.pow(1 - progress, 3);
                this.world.roverMesh.position.x = this.fromPos.x + (this.toPos.x - this.fromPos.x) * t;
                this.world.roverMesh.position.z = this.fromPos.z + (this.toPos.z - this.fromPos.z) * t;

                if (progress < 1.0) {
                    requestAnimationFrame(animateMove);
                } else {
                    this.world.roverState.x = action.to.x;
                    this.world.roverState.z = action.to.z;
                    this.world.updateHUD();
                    this.isInterpolating = false;
                    this.currentIndex++;
                    if (onStepDone) onStepDone();
                }
            };
            requestAnimationFrame(animateMove);

        } else if (action.type === 'TURN_LEFT' || action.type === 'TURN_RIGHT') {
            this.isInterpolating = true;
            this.interpStartTime = performance.now();
            this.fromAngle = this.world.roverMesh.rotation.y;
            const deltaAngle = (action.type === 'TURN_LEFT') ? -Math.PI / 2 : Math.PI / 2;
            this.toAngle = this.fromAngle + deltaAngle;

            if (window.soundEngine) window.soundEngine.playMove();

            const animateTurn = (now) => {
                const elapsed = now - this.interpStartTime;
                const progress = Math.min(1.0, elapsed / (this.stepDuration * 0.7));
                const t = 1 - Math.pow(1 - progress, 3);

                this.world.roverMesh.rotation.y = this.fromAngle + (this.toAngle - this.fromAngle) * t;

                if (progress < 1.0) {
                    requestAnimationFrame(animateTurn);
                } else {
                    this.world.setRoverDirection(action.toDir);
                    this.isInterpolating = false;
                    this.currentIndex++;
                    if (onStepDone) onStepDone();
                }
            };
            requestAnimationFrame(animateTurn);

        } else if (action.type === 'COLLECT' || action.type === 'AUTO_DETECT_GEM') {
            this.world.collectCrystalAt(action.x, action.z);
            this.currentIndex++;
            setTimeout(() => { if (onStepDone) onStepDone(); }, this.stepDuration * 0.5);

        } else if (action.type === 'COLLISION') {
            this.isPlaying = false;
            if (window.soundEngine) window.soundEngine.playLaser();
            this.setStatus(`MISSION FAILED: ${action.reason}!`, true);
            this.updateButtonStates();

        } else {
            this.currentIndex++;
            if (onStepDone) onStepDone();
        }
    }

    finishExecution() {
        this.isPlaying = false;
        this.updateButtonStates();
        this.clearLineHighlight();

        const summary = this.execSummary;
        if (!summary) return;

        if (summary.reachedPortal && summary.collectedGems >= summary.totalGems) {
            if (window.soundEngine) window.soundEngine.playSuccess();
            this.setStatus("MISSION ACCOMPLISHED! Portal reached and all crystals collected! 🏁💎");

            if (this.onCompleteCallback) {
                this.onCompleteCallback(summary);
            }
        } else if (summary.reachedPortal && summary.collectedGems < summary.totalGems) {
            this.setStatus(`Reached portal but missed crystals! (${summary.collectedGems}/${summary.totalGems})`, true);
        } else {
            this.setStatus("Rover stopped without reaching the destination portal.", true);
        }
    }

    highlightCodeLine(lineNum) {
        const lineIndicator = document.getElementById('active-line-indicator');
        if (lineIndicator && lineNum > 0) {
            lineIndicator.textContent = `Executing Line: ${lineNum}`;
            lineIndicator.classList.remove('hidden');
        }
    }

    clearLineHighlight() {
        const lineIndicator = document.getElementById('active-line-indicator');
        if (lineIndicator) lineIndicator.classList.add('hidden');
    }
}

window.PlaybackController = PlaybackController;
