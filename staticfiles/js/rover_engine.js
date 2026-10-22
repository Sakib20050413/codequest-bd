/**
 * CodeQuest BD - Mode 1: 2D Grid Rover Maze Engine
 * Animates rover logic, detects obstacles, gems, and portal goals.
 */

class RoverMazeEngine {
    constructor(containerId, config = {}) {
        this.container = document.getElementById(containerId);
        this.rows = config.rows || 8;
        this.cols = config.cols || 8;
        this.start = config.start || { x: 0, y: 0, dir: 'east' };
        this.portal = config.portal || { x: 7, y: 7 };
        this.obstacles = config.obstacles || []; // [{x, y}]
        this.gems = config.gems || []; // [{x, y}]
        
        this.rover = { ...this.start };
        this.collectedGems = 0;
        this.totalGems = this.gems.length;
        this.isRunning = false;
        this.stepDelay = 220; // ms per step

        this.init();
    }

    init() {
        if (!this.container) return;
        this.renderGrid();
        this.updateStatusText("Ready. Write your logic and click 'Run Rover'!");
    }

    reset() {
        this.rover = { ...this.start };
        this.collectedGems = 0;
        this.isRunning = false;
        this.renderGrid();
        this.updateStatusText("Maze reset to initial state.");
    }

    renderGrid() {
        this.container.innerHTML = '';
        this.container.style.gridTemplateColumns = `repeat(${this.cols}, minmax(0, 1fr))`;

        for (let r = 0; r < this.rows; r++) {
            for (let c = 0; c < this.cols; c++) {
                const cell = document.createElement('div');
                cell.className = 'aspect-square border border-slate-800/80 rounded-lg flex items-center justify-center relative font-mono text-base transition-all duration-200 bg-slate-900/60';
                cell.dataset.row = r;
                cell.dataset.col = c;

                // Target Portal
                if (r === this.portal.y && c === this.portal.x) {
                    cell.innerHTML = '<span class="text-xl animate-pulse" title="Portal">🏁</span>';
                    cell.classList.add('bg-emerald-950/40', 'border-emerald-500/40');
                }

                // Laser Obstacle
                const isObstacle = this.obstacles.some(o => o.x === c && o.y === r);
                if (isObstacle) {
                    cell.innerHTML = '<span class="text-xl text-amber-400 animate-bounce" title="Laser Barrier">⚡</span>';
                    cell.classList.add('bg-amber-950/30', 'border-amber-500/40');
                }

                // Energy Gem
                const isGem = this.gems.some(g => g.x === c && g.y === r);
                if (isGem) {
                    cell.innerHTML = '<span class="text-lg text-cyan-300 drop-shadow" title="Energy Gem">💎</span>';
                    cell.classList.add('bg-cyan-950/20');
                }

                // Cyber Rover
                if (r === this.rover.y && c === this.rover.x) {
                    cell.innerHTML = this.getRoverIcon(this.rover.dir);
                    cell.classList.add('bg-indigo-600/30', 'border-indigo-400', 'shadow-inner');
                }

                this.container.appendChild(cell);
            }
        }
    }

    getRoverIcon(dir) {
        let rotation = '0deg';
        if (dir === 'east') rotation = '0deg';
        if (dir === 'south') rotation = '90deg';
        if (dir === 'west') rotation = '180deg';
        if (dir === 'north') rotation = '270deg';

        return `<div class="rover-sprite text-2xl transition-transform duration-200" style="transform: rotate(${rotation})">🤖</div>`;
    }

    updateStatusText(msg) {
        const statusEl = document.getElementById('rover-status-text');
        if (statusEl) {
            statusEl.textContent = msg;
        }
        const gemEl = document.getElementById('rover-gem-count');
        if (gemEl) {
            gemEl.textContent = `${this.collectedGems} / ${this.totalGems}`;
        }
    }

    async executeCommands(commandList, onComplete) {
        if (this.isRunning) return;
        this.isRunning = true;
        this.reset();

        for (let i = 0; i < commandList.length; i++) {
            const cmd = commandList[i].trim().toLowerCase();
            if (!cmd) continue;

            const success = await this.step(cmd);
            if (!success) {
                this.isRunning = false;
                if (window.soundEngine) window.soundEngine.playLaser();
                this.updateStatusText("Mission Failed! Rover hit an obstacle or left the grid.");
                if (onComplete) onComplete({ success: false, reason: 'Collision or Out of Bounds' });
                return;
            }
            await new Promise(res => setTimeout(res, this.stepDelay));
        }

        this.isRunning = false;

        // Check if reached portal and collected required gems
        const atPortal = (this.rover.x === this.portal.x && this.rover.y === this.portal.y);
        const gemsComplete = (this.collectedGems >= this.totalGems);

        if (atPortal && gemsComplete) {
            if (window.soundEngine) window.soundEngine.playSuccess();
            this.updateStatusText("Target Portal Reached! All Gems Secured! 🏁💎");
            if (onComplete) onComplete({ success: true });
        } else if (atPortal && !gemsComplete) {
            this.updateStatusText(`Reached portal, but missed gems! (${this.collectedGems}/${this.totalGems})`);
            if (onComplete) onComplete({ success: false, reason: 'Missed Gems' });
        } else {
            this.updateStatusText("Rover stopped before reaching the portal.");
            if (onComplete) onComplete({ success: false, reason: 'Did not reach portal' });
        }
    }

    async step(cmd) {
        let dx = 0;
        let dy = 0;

        if (cmd === 'forward' || cmd === 'move_forward' || cmd === 'move') {
            if (this.rover.dir === 'east') dx = 1;
            else if (this.rover.dir === 'west') dx = -1;
            else if (this.rover.dir === 'south') dy = 1;
            else if (this.rover.dir === 'north') dy = -1;
        } else if (cmd === 'left' || cmd === 'turn_left') {
            const dirs = ['north', 'west', 'south', 'east'];
            const curIdx = dirs.indexOf(this.rover.dir);
            this.rover.dir = dirs[(curIdx + 1) % 4];
            if (window.soundEngine) window.soundEngine.playMove();
            this.renderGrid();
            return true;
        } else if (cmd === 'right' || cmd === 'turn_right') {
            const dirs = ['north', 'east', 'south', 'west'];
            const curIdx = dirs.indexOf(this.rover.dir);
            this.rover.dir = dirs[(curIdx + 1) % 4];
            if (window.soundEngine) window.soundEngine.playMove();
            this.renderGrid();
            return true;
        } else if (cmd === 'collect' || cmd === 'collect_gem') {
            // Check if current cell has a gem
            const gemIdx = this.gems.findIndex(g => g.x === this.rover.x && g.y === this.rover.y);
            if (gemIdx !== -1) {
                this.gems.splice(gemIdx, 1);
                this.collectedGems++;
                if (window.soundEngine) window.soundEngine.playGem();
                this.updateStatusText(`Collected Energy Gem! 💎 (${this.collectedGems}/${this.totalGems})`);
                this.renderGrid();
            }
            return true;
        } else {
            return true; // ignore unknown comment
        }

        const newX = this.rover.x + dx;
        const newY = this.rover.y + dy;

        // Boundary check
        if (newX < 0 || newX >= this.cols || newY < 0 || newY >= this.rows) {
            return false;
        }

        // Obstacle check
        const hitObstacle = this.obstacles.some(o => o.x === newX && o.y === newY);
        if (hitObstacle) {
            return false;
        }

        // Leave trail on previous cell
        const oldCell = this.container.querySelector(`[data-row="${this.rover.y}"][data-col="${this.rover.x}"]`);
        if (oldCell) {
            oldCell.classList.add('bg-indigo-950/20');
        }

        this.rover.x = newX;
        this.rover.y = newY;

        // Auto collect gem on step if present
        const gemIdx = this.gems.findIndex(g => g.x === newX && g.y === newY);
        if (gemIdx !== -1) {
            this.gems.splice(gemIdx, 1);
            this.collectedGems++;
            if (window.soundEngine) window.soundEngine.playGem();
        } else {
            if (window.soundEngine) window.soundEngine.playMove();
        }

        this.renderGrid();
        return true;
    }
}

window.RoverMazeEngine = RoverMazeEngine;
