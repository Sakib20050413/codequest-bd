/**
 * CodeQuest BD - Code Runner & Challenge Submission Controller
 * Bridges Code Editor, Rover Maze, DOM Builder, and Piston Cloud API.
 */

class CodeQuestRunner {
    constructor(options = {}) {
        this.levelId = options.levelId;
        this.engineType = options.engineType || 'CODE_JUDGE';
        this.csrfToken = options.csrfToken || '';
        this.mazeEngine = options.mazeEngine || null;
        this.domEngine = options.domEngine || null;

        this.codeEditor = document.getElementById('code-editor');
        this.langSelect = document.getElementById('language-select');
        this.consoleOutput = document.getElementById('console-output-text');
        this.runBtn = document.getElementById('btn-run-code');
        this.submitBtn = document.getElementById('btn-submit-code');
        this.testResultsContainer = document.getElementById('test-results-container');

        this.initEvents();
    }

    initEvents() {
        if (this.runBtn) {
            this.runBtn.addEventListener('click', () => this.handleRun());
        }
        if (this.submitBtn) {
            this.submitBtn.addEventListener('click', () => this.handleSubmit());
        }

        // Live input typing for DOM builder
        if (this.engineType === 'DOM_BUILDER' && this.codeEditor) {
            this.codeEditor.addEventListener('input', (e) => {
                if (this.domEngine) {
                    this.domEngine.applyLiveCSS(e.target.value);
                }
            });
        }
    }

    getEditorContent() {
        return this.codeEditor ? this.codeEditor.value : '';
    }

    getLanguage() {
        return this.langSelect ? this.langSelect.value : 'c';
    }

    setConsoleOutput(text, isError = false) {
        if (this.consoleOutput) {
            this.consoleOutput.textContent = text;
            this.consoleOutput.className = isError 
                ? 'font-mono text-xs text-rose-400 p-3 whitespace-pre-wrap' 
                : 'font-mono text-xs text-emerald-400 p-3 whitespace-pre-wrap';
        }
    }

    async handleRun() {
        const code = this.getEditorContent();
        const lang = this.getLanguage();

        this.setConsoleOutput("Compiling and executing code...");

        // 1. If ROVER_MAZE engine
        if (this.engineType === 'ROVER_MAZE' && this.mazeEngine) {
            // First run on backend or parse commands
            try {
                const res = await fetch('/api/run-code/', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': this.csrfToken },
                    body: JSON.stringify({ language: lang, code: code, stdin: '' })
                });
                const data = await res.json();
                const stdout = data.execution?.stdout || '';
                this.setConsoleOutput(`[Execution Output]\n${stdout}\n\nRunning Rover Animation...`);

                // Convert output lines or keywords to rover commands
                const lines = stdout.split('\n').filter(l => l.trim().length > 0);
                const commands = lines.length > 0 ? lines : code.split('\n');

                this.mazeEngine.executeCommands(commands, (result) => {
                    if (result.success) {
                        this.setConsoleOutput("Rover completed journey successfully! Click 'Submit Solution' to earn your XP.");
                    } else {
                        this.setConsoleOutput(`Rover failed: ${result.reason}`, true);
                    }
                });
            } catch (err) {
                this.setConsoleOutput(`Execution Error: ${err.message}`, true);
            }
            return;
        }

        // 2. If DOM_BUILDER engine
        if (this.engineType === 'DOM_BUILDER' && this.domEngine) {
            const isAligned = this.domEngine.checkAlignment();
            if (isAligned) {
                this.setConsoleOutput("DOM Visual Stage verified: All Cyber Drones correctly aligned! 🛸");
            } else {
                this.setConsoleOutput("DOM Visual Stage: Alignment condition not fully met.", true);
            }
            return;
        }

        // 3. CODE_JUDGE (Standard)
        try {
            const res = await fetch('/api/run-code/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'X-CSRFToken': this.csrfToken },
                body: JSON.stringify({ language: lang, code: code, stdin: '' })
            });
            const data = await res.json();
            const exec = data.execution;

            if (exec.status === 'SYNTAX_ERROR') {
                this.setConsoleOutput(`[Syntax/Compilation Error]\n${exec.stderr}`, true);
            } else if (exec.status === 'RUNTIME_ERROR') {
                this.setConsoleOutput(`[Runtime Error]\n${exec.stderr}`, true);
            } else {
                this.setConsoleOutput(`[Status: ${exec.status}] (${exec.execution_time_ms} ms via ${exec.engine})\n\n${exec.stdout}`);
            }
        } catch (err) {
            this.setConsoleOutput(`Network or Server Error: ${err.message}`, true);
        }
    }

    async handleSubmit() {
        const code = this.getEditorContent();
        const lang = this.getLanguage();

        this.setConsoleOutput("Evaluating solution against all test cases...");

        try {
            const res = await fetch('/api/submit-level/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'X-CSRFToken': this.csrfToken },
                body: JSON.stringify({
                    level_id: this.levelId,
                    language: lang,
                    code: code
                })
            });
            const data = await res.json();
            const evalRes = data.evaluation;

            this.renderTestCases(evalRes.results || []);

            if (evalRes.all_passed) {
                if (window.soundEngine) window.soundEngine.playSuccess();
                this.setConsoleOutput(`[VERIFIED ACCEPTED ✅]\nAll test cases passed! +${data.earned_xp} XP Awarded.\nUser Total XP: ${data.user_total_xp} (${data.user_rank})`);

                // Show celebration modal
                this.showCelebrationModal(data.earned_xp, data.user_total_xp, data.user_rank);
            } else {
                if (window.soundEngine) window.soundEngine.playError();
                this.setConsoleOutput(`[FAILED ❌]\nSome test cases failed. Inspect the Test Cases tab for details.`, true);
            }
        } catch (err) {
            this.setConsoleOutput(`Submission error: ${err.message}`, true);
        }
    }

    renderTestCases(results) {
        if (!this.testResultsContainer) return;
        this.testResultsContainer.innerHTML = '';

        results.forEach(r => {
            const item = document.createElement('div');
            item.className = r.passed 
                ? 'p-3 rounded-lg border border-emerald-500/30 bg-emerald-950/20 text-xs font-mono space-y-1'
                : 'p-3 rounded-lg border border-rose-500/30 bg-rose-950/20 text-xs font-mono space-y-1';

            item.innerHTML = `
                <div class="flex justify-between items-center font-bold">
                    <span class="${r.passed ? 'text-emerald-400' : 'text-rose-400'}">
                        ${r.passed ? '✅ Passed' : '❌ Failed'} — Test Case #${r.test_num}
                    </span>
                    <span class="text-slate-500 text-[10px]">${r.engine || 'Evaluator'}</span>
                </div>
                <div class="text-slate-400"><span class="text-slate-500">Expected:</span> ${r.expected}</div>
                <div class="${r.passed ? 'text-slate-300' : 'text-rose-300'}"><span class="text-slate-500">Actual:</span> ${r.actual || r.stderr || '(empty)'}</div>
            `;
            this.testResultsContainer.appendChild(item);
        });
    }

    showCelebrationModal(earnedXP, totalXP, rank) {
        const modal = document.getElementById('celebration-modal');
        if (!modal) return;

        const xpEl = document.getElementById('modal-earned-xp');
        const rankEl = document.getElementById('modal-user-rank');
        if (xpEl) xpEl.textContent = `+${earnedXP} XP`;
        if (rankEl) rankEl.textContent = rank;

        modal.classList.remove('hidden');

        // Update top navbar XP badge live without reloading
        const navXp = document.getElementById('nav-user-xp');
        if (navXp) navXp.textContent = `${totalXP} XP`;
    }
}

window.CodeQuestRunner = CodeQuestRunner;
