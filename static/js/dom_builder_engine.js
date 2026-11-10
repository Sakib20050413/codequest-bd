/**
 * CodeQuest BD - Mode 2: Visual CSS & DOM Builder Game Engine
 * Inspired by Flexbox Froggy & CSS Diner with real-time DOM stage rendering.
 */

class DomBuilderEngine {
    constructor(stageId, config = {}) {
        this.stage = document.getElementById(stageId);
        this.config = config;
        this.targetStyles = config.target_styles || {};
        this.requiredSelectors = config.required_selectors || [];
        this.itemCount = config.item_count || 3;
        this.mode = config.type || 'FLEXBOX'; // 'FLEXBOX' or 'JS_DOM'
        
        this.init();
    }

    init() {
        if (!this.stage) return;
        this.renderStage();
    }

    renderStage() {
        this.stage.innerHTML = '';

        // Container wrapper
        const sandbox = document.createElement('div');
        sandbox.id = 'dom-sandbox-container';
        sandbox.className = 'w-full h-72 rounded-xl relative p-4 flex overflow-hidden border border-slate-700 bg-slate-950 transition-all duration-300';

        // Target Landing Pads (Background Overlay)
        const padsOverlay = document.createElement('div');
        padsOverlay.id = 'pads-overlay';
        padsOverlay.className = 'absolute inset-0 p-4 flex pointer-events-none';
        
        // Apply target flex styles to pads
        if (this.config.target_css) {
            padsOverlay.style.cssText = this.config.target_css;
        } else {
            padsOverlay.style.justifyContent = this.targetStyles.justifyContent || 'space-between';
            padsOverlay.style.alignItems = this.targetStyles.alignItems || 'center';
            padsOverlay.style.flexDirection = this.targetStyles.flexDirection || 'row';
        }

        for (let i = 0; i < this.itemCount; i++) {
            const pad = document.createElement('div');
            pad.className = 'w-16 h-16 rounded-2xl border-2 border-dashed border-emerald-500/60 bg-emerald-500/10 flex items-center justify-center font-mono text-xs text-emerald-400';
            pad.innerHTML = `<span>PAD ${i+1}</span>`;
            padsOverlay.appendChild(pad);
        }

        // Live Drone Characters (Foreground elements that move with student CSS)
        const dronesContainer = document.createElement('div');
        dronesContainer.id = 'drones-container';
        dronesContainer.className = 'absolute inset-0 p-4 flex transition-all duration-300';
        dronesContainer.style.display = 'flex';

        for (let i = 0; i < this.itemCount; i++) {
            const drone = document.createElement('div');
            drone.id = `cyber-drone-${i+1}`;
            drone.className = 'cyber-drone w-16 h-16 rounded-2xl bg-gradient-to-tr from-indigo-600 to-cyan-500 flex items-center justify-center text-2xl shadow-lg shadow-cyan-500/20 transform transition-all duration-300';
            drone.innerHTML = '🛸';
            dronesContainer.appendChild(drone);
        }

        sandbox.appendChild(padsOverlay);
        sandbox.appendChild(dronesContainer);
        this.stage.appendChild(sandbox);
    }

    applyLiveCSS(cssString) {
        const dronesContainer = document.getElementById('drones-container');
        if (!dronesContainer) return;

        // Reset and apply rules
        dronesContainer.style.cssText = 'position: absolute; inset: 0; padding: 1rem; display: flex; transition: all 0.3s ease; ' + cssString;

        // Check if drones overlap target pads
        this.checkAlignment();
    }

    checkAlignment() {
        const drones = document.querySelectorAll('.cyber-drone');
        const pads = document.querySelectorAll('#pads-overlay > div');

        if (drones.length !== pads.length) return false;

        let allAligned = true;
        const tolerance = 18; // px tolerance

        for (let i = 0; i < drones.length; i++) {
            const dRect = drones[i].getBoundingClientRect();
            const pRect = pads[i].getBoundingClientRect();

            const xDiff = Math.abs(dRect.left - pRect.left);
            const yDiff = Math.abs(dRect.top - pRect.top);

            if (xDiff > tolerance || yDiff > tolerance) {
                allAligned = false;
                drones[i].classList.remove('ring-4', 'ring-emerald-400');
            } else {
                drones[i].classList.add('ring-4', 'ring-emerald-400');
            }
        }

        const statusEl = document.getElementById('dom-status-badge');
        if (statusEl) {
            if (allAligned) {
                statusEl.textContent = 'Aligned with Target Pads! 🛸✨';
                statusEl.className = 'text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30';
                if (window.soundEngine) window.soundEngine.playCombo();
            } else {
                statusEl.textContent = 'Drones not aligned to target pads yet.';
                statusEl.className = 'text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800 text-slate-400 border border-slate-700';
            }
        }

        return allAligned;
    }

    runDomScript(scriptCode) {
        try {
            const sandbox = document.getElementById('dom-sandbox-container');
            if (!sandbox) return { success: false, error: 'Sandbox missing' };

            // Wrap execution with scoped functions
            const runFn = new Function('document', 'sandbox', scriptCode);
            runFn(document, sandbox);

            // Verify condition
            const checkFn = this.config.validator_fn;
            let success = false;
            if (checkFn) {
                const evalFn = new Function('document', 'return (' + checkFn + ')');
                success = evalFn(document);
            } else {
                success = this.checkAlignment();
            }

            if (success && window.soundEngine) {
                window.soundEngine.playSuccess();
            }

            return { success: success };
        } catch (err) {
            if (window.soundEngine) window.soundEngine.playError();
            return { success: false, error: err.message };
        }
    }
}

window.DomBuilderEngine = DomBuilderEngine;
