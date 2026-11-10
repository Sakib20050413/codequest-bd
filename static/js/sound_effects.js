/**
 * CodeQuest BD - Web Audio API Sound Synthesizer
 * Generates arcade audio effects with zero external audio files.
 */

class SoundEngine {
    constructor() {
        this.ctx = null;
        this.enabled = true;
    }

    init() {
        if (!this.ctx) {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            if (AudioCtx) {
                this.ctx = new AudioCtx();
            }
        }
    }

    playTone(freq, type = 'sine', duration = 0.15, gainVal = 0.1) {
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        try {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();

            osc.type = type;
            osc.frequency.setValueAtTime(freq, this.ctx.currentTime);

            gain.gain.setValueAtTime(gainVal, this.ctx.currentTime);
            gain.gain.exponentialRampToValueAtTime(0.001, this.ctx.currentTime + duration);

            osc.connect(gain);
            gain.connect(this.ctx.destination);

            osc.start();
            osc.stop(this.ctx.currentTime + duration);
        } catch (e) {
            console.warn('Audio play error', e);
        }
    }

    playMove() {
        this.playTone(320, 'triangle', 0.08, 0.08);
    }

    playGem() {
        this.playTone(880, 'sine', 0.1, 0.12);
        setTimeout(() => this.playTone(1320, 'sine', 0.18, 0.15), 60);
    }

    playLaser() {
        this.playTone(180, 'sawtooth', 0.25, 0.15);
    }

    playSuccess() {
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C E G C
        notes.forEach((freq, idx) => {
            setTimeout(() => {
                this.playTone(freq, 'sine', 0.2, 0.15);
            }, idx * 100);
        });
    }

    playError() {
        this.playTone(150, 'square', 0.2, 0.15);
        setTimeout(() => this.playTone(110, 'square', 0.3, 0.15), 120);
    }

    playCombo() {
        this.playTone(660, 'sine', 0.1, 0.1);
        setTimeout(() => this.playTone(990, 'sine', 0.12, 0.12), 70);
        setTimeout(() => this.playTone(1320, 'sine', 0.2, 0.15), 140);
    }
}

window.soundEngine = new SoundEngine();
document.addEventListener('click', () => {
    if (window.soundEngine && !window.soundEngine.ctx) {
        window.soundEngine.init();
    }
}, { once: true });
