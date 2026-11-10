/**
 * CodeQuest 3D - Reactive Action Queue Interpreter
 * Executes student code in Python, JavaScript, and C-syntax in-browser
 * Generates an atomic Action Queue with 2000-tick loop guard.
 */

class ActionInterpreter {
    constructor(gridConfig = {}) {
        this.cols = gridConfig.cols || 8;
        this.rows = gridConfig.rows || 8;
        this.startPos = gridConfig.start || { x: 0, z: 0, dir: 'east' };
        this.portalPos = gridConfig.portal || { x: this.cols - 1, z: this.rows - 1 };
        this.obstacles = gridConfig.obstacles || [];
        this.gems = gridConfig.gems || [];
        this.maxTicks = 2000;
    }

    /**
     * Executes code and returns an Action Queue
     */
    execute(language, code) {
        const lang = (language || 'javascript').toLowerCase();

        // 1. Convert Python or C code to executable JS Sandbox script
        let jsScript = code;
        try {
            if (lang === 'python') {
                jsScript = this.transpilePythonToJS(code);
            } else if (lang === 'c' || lang === 'cpp') {
                jsScript = this.transpileCToJS(code);
            }
        } catch (transpileErr) {
            return {
                success: false,
                error: `Syntax Parsing Error: ${transpileErr.message}`
            };
        }

        // 2. Setup Virtual Rover Environment & Action Queue
        const actions = [];
        let tickCount = 0;
        let isHalted = false;
        let haltReason = '';

        const simRover = {
            x: this.startPos.x,
            z: this.startPos.z,
            dir: this.startPos.dir,
            energy: 100
        };

        const activeGems = new Set(this.gems.map(g => `${g.x},${g.z}`));
        const obstacleSet = new Set(this.obstacles.map(o => `${o.x},${o.z}`));

        const recordTick = () => {
            tickCount++;
            if (tickCount > this.maxTicks) {
                isHalted = true;
                haltReason = `Execution safety limit exceeded (${this.maxTicks} steps). Check for infinite loops!`;
                throw new Error(haltReason);
            }
        };

        const getFrontCoord = () => {
            let dx = 0;
            let dz = 0;
            if (simRover.dir === 'east') dx = 1;
            else if (simRover.dir === 'west') dx = -1;
            else if (simRover.dir === 'south') dz = 1;
            else if (simRover.dir === 'north') dz = -1;
            return { x: simRover.x + dx, z: simRover.z + dz };
        };

        // Create Virtual Rover API
        const roverAPI = {
            moveForward: (line = 0) => {
                recordTick();
                if (isHalted) return;

                const front = getFrontCoord();
                const fromPos = { x: simRover.x, z: simRover.z };

                // Collision checks
                if (front.x < 0 || front.x >= this.cols || front.z < 0 || front.z >= this.rows) {
                    isHalted = true;
                    actions.push({
                        type: 'COLLISION',
                        from: fromPos,
                        to: front,
                        reason: 'Out of Grid Bounds',
                        line: line
                    });
                    return;
                }

                if (obstacleSet.has(`${front.x},${front.z}`)) {
                    isHalted = true;
                    actions.push({
                        type: 'COLLISION',
                        from: fromPos,
                        to: front,
                        reason: 'Laser Barrier Impact',
                        line: line
                    });
                    return;
                }

                simRover.x = front.x;
                simRover.z = front.z;
                simRover.energy -= 2;

                actions.push({
                    type: 'MOVE',
                    from: fromPos,
                    to: { x: simRover.x, z: simRover.z },
                    dir: simRover.dir,
                    line: line
                });

                // Auto-detect crystal
                if (activeGems.has(`${simRover.x},${simRover.z}`)) {
                    actions.push({
                        type: 'AUTO_DETECT_GEM',
                        x: simRover.x,
                        z: simRover.z
                    });
                }
            },

            turnLeft: (line = 0) => {
                recordTick();
                if (isHalted) return;
                const dirs = ['north', 'west', 'south', 'east'];
                const curIdx = dirs.indexOf(simRover.dir);
                const fromDir = simRover.dir;
                simRover.dir = dirs[(curIdx + 1) % 4];

                actions.push({
                    type: 'TURN_LEFT',
                    fromDir: fromDir,
                    toDir: simRover.dir,
                    line: line
                });
            },

            turnRight: (line = 0) => {
                recordTick();
                if (isHalted) return;
                const dirs = ['north', 'east', 'south', 'west'];
                const curIdx = dirs.indexOf(simRover.dir);
                const fromDir = simRover.dir;
                simRover.dir = dirs[(curIdx + 1) % 4];

                actions.push({
                    type: 'TURN_RIGHT',
                    fromDir: fromDir,
                    toDir: simRover.dir,
                    line: line
                });
            },

            collect: (line = 0) => {
                recordTick();
                if (isHalted) return;
                const key = `${simRover.x},${simRover.z}`;
                const hasGem = activeGems.has(key);
                if (hasGem) {
                    activeGems.delete(key);
                    actions.push({
                        type: 'COLLECT',
                        x: simRover.x,
                        z: simRover.z,
                        success: true,
                        line: line
                    });
                } else {
                    actions.push({
                        type: 'COLLECT',
                        x: simRover.x,
                        z: simRover.z,
                        success: false,
                        line: line
                    });
                }
            },

            sensorFront: () => {
                recordTick();
                const front = getFrontCoord();
                if (front.x < 0 || front.x >= this.cols || front.z < 0 || front.z >= this.rows) {
                    return 'wall';
                }
                const key = `${front.x},${front.z}`;
                if (obstacleSet.has(key)) return 'laser';
                if (activeGems.has(key)) return 'gem';
                if (front.x === this.portalPos.x && front.z === this.portalPos.z) return 'portal';
                return 'clear';
            },

            hasGemAhead: () => {
                return roverAPI.sensorFront() === 'gem';
            },

            hasObstacleAhead: () => {
                const s = roverAPI.sensorFront();
                return s === 'laser' || s === 'wall';
            },

            isAtPortal: () => {
                return (simRover.x === this.portalPos.x && simRover.z === this.portalPos.z);
            },

            getEnergy: () => simRover.energy,
        };

        // Aliases for Python & C-style functions
        roverAPI.move_forward = roverAPI.moveForward;
        roverAPI.turn_left = roverAPI.turnLeft;
        roverAPI.turn_right = roverAPI.turnRight;
        roverAPI.sensor_front = roverAPI.sensorFront;
        roverAPI.has_gem_ahead = roverAPI.hasGemAhead;
        roverAPI.has_obstacle_ahead = roverAPI.hasObstacleAhead;
        roverAPI.detect_gem = roverAPI.hasGemAhead;
        roverAPI.is_at_portal = roverAPI.isAtPortal;

        // 3. Sandbox Run
        try {
            const sandboxFn = new Function(
                'rover',
                'move_forward', 'turn_left', 'turn_right', 'collect',
                'sensor_front', 'detect_gem', 'is_at_portal',
                `"use strict";\n${jsScript}`
            );

            sandboxFn(
                roverAPI,
                roverAPI.moveForward,
                roverAPI.turnLeft,
                roverAPI.turnRight,
                roverAPI.collect,
                roverAPI.sensorFront,
                roverAPI.hasGemAhead,
                roverAPI.isAtPortal
            );

            const reachedPortal = (simRover.x === this.portalPos.x && simRover.z === this.portalPos.z);
            const collectedCount = this.gems.length - activeGems.size;

            return {
                success: true,
                actions: actions,
                totalTicks: tickCount,
                reachedPortal: reachedPortal,
                collectedGems: collectedCount,
                totalGems: this.gems.length,
                finalPos: { x: simRover.x, z: simRover.z, dir: simRover.dir },
                isHalted: isHalted,
                haltReason: haltReason
            };

        } catch (err) {
            return {
                success: false,
                error: err.message,
                partialActions: actions
            };
        }
    }

    /**
     * Lightweight Python-to-JS Transpiler for Loop & Sensor Structures
     */
    transpilePythonToJS(pyCode) {
        const lines = pyCode.split('\n');
        const jsLines = [];
        const indentStack = [0];

        for (let i = 0; i < lines.length; i++) {
            let line = lines[i];
            const trimmed = line.trim();

            if (!trimmed || trimmed.startsWith('#')) {
                continue;
            }

            // Calculate indentation
            const currentIndent = line.search(/\S/);

            while (currentIndent < indentStack[indentStack.length - 1]) {
                indentStack.pop();
                jsLines.push(' '.repeat(indentStack[indentStack.length - 1]) + '}');
            }

            let jsLine = trimmed;

            // Transpile for loop: for i in range(N):
            const forRangeMatch = trimmed.match(/^for\s+(\w+)\s+in\s+range\s*\((.*?)\)\s*:/);
            if (forRangeMatch) {
                const varName = forRangeMatch[1];
                const args = forRangeMatch[2].split(',').map(a => a.trim());
                let start = '0';
                let end = args[0];
                let step = '1';

                if (args.length === 2) {
                    start = args[0];
                    end = args[1];
                } else if (args.length === 3) {
                    start = args[0];
                    end = args[1];
                    step = args[2];
                }

                jsLine = `for (let ${varName} = ${start}; ${varName} < ${end}; ${varName} += ${step}) {`;
                indentStack.push(currentIndent + 4);
                jsLines.push(' '.repeat(currentIndent) + jsLine);
                continue;
            }

            // Transpile while loop: while condition:
            const whileMatch = trimmed.match(/^while\s+(.*?)\s*:/);
            if (whileMatch) {
                const cond = whileMatch[1].replace(/==/g, '===').replace(/!=/g, '!==');
                jsLine = `while (${cond}) {`;
                indentStack.push(currentIndent + 4);
                jsLines.push(' '.repeat(currentIndent) + jsLine);
                continue;
            }

            // Transpile if: if cond:
            const ifMatch = trimmed.match(/^if\s+(.*?)\s*:/);
            if (ifMatch) {
                const cond = ifMatch[1].replace(/==/g, '===').replace(/!=/g, '!==');
                jsLine = `if (${cond}) {`;
                indentStack.push(currentIndent + 4);
                jsLines.push(' '.repeat(currentIndent) + jsLine);
                continue;
            }

            // Transpile elif: elif cond:
            const elifMatch = trimmed.match(/^elif\s+(.*?)\s*:/);
            if (elifMatch) {
                const cond = elifMatch[1].replace(/==/g, '===').replace(/!=/g, '!==');
                jsLine = `} else if (${cond}) {`;
                jsLines.push(' '.repeat(currentIndent) + jsLine);
                continue;
            }

            // Transpile else:
            if (trimmed === 'else:') {
                jsLines.push(' '.repeat(currentIndent) + '} else {');
                continue;
            }

            // Python functions / methods to JS
            jsLine = jsLine
                .replace(/\.move_forward\(\)/g, '.moveForward(' + (i + 1) + ')')
                .replace(/\.turn_left\(\)/g, '.turnLeft(' + (i + 1) + ')')
                .replace(/\.turn_right\(\)/g, '.turnRight(' + (i + 1) + ')')
                .replace(/\.collect\(\)/g, '.collect(' + (i + 1) + ')')
                .replace(/^move_forward\(\)/g, 'move_forward(' + (i + 1) + ')')
                .replace(/^turn_left\(\)/g, 'turn_left(' + (i + 1) + ')')
                .replace(/^turn_right\(\)/g, 'turn_right(' + (i + 1) + ')')
                .replace(/^collect\(\)/g, 'collect(' + (i + 1) + ')')
                .replace(/\.sensor_front\(\)/g, '.sensorFront()')
                .replace(/\.has_gem_ahead\(\)/g, '.hasGemAhead()')
                .replace(/\.has_obstacle_ahead\(\)/g, '.hasObstacleAhead()')
                .replace(/\.is_at_portal\(\)/g, '.isAtPortal()');

            if (!jsLine.endsWith(';') && !jsLine.endsWith('{') && !jsLine.endsWith('}')) {
                jsLine += ';';
            }

            jsLines.push(' '.repeat(currentIndent) + jsLine);
        }

        while (indentStack.length > 1) {
            indentStack.pop();
            jsLines.push('}');
        }

        return jsLines.join('\n');
    }

    /**
     * Lightweight C-to-JS Transpiler
     */
    transpileCToJS(cCode) {
        let js = cCode
            .replace(/#include\s+<.*?>/g, '')
            .replace(/int\s+main\s*\([^)]*\)\s*\{/g, '')
            .replace(/return\s+0\s*;/g, '')
            .replace(/\bint\s+(\w+)\s*=/g, 'let $1 =')
            .replace(/\bint\s+(\w+);/g, 'let $1 = 0;')
            .replace(/printf\s*\([^)]*\);/g, '')
            .replace(/cout\s*<<[^;]*;/g, '');

        // Remove trailing closing brace for main
        const lastBrace = js.lastIndexOf('}');
        if (lastBrace !== -1) {
            js = js.slice(0, lastBrace) + js.slice(lastBrace + 1);
        }

        return js;
    }
}

window.ActionInterpreter = ActionInterpreter;
