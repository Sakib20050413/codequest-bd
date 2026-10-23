/**
 * CodeQuest Core Platform Engine
 * Theme switching, Web Audio synth, single confetti burst, guest progress sync.
 */
(function (global) {
  'use strict';

  // 1. Theme Management
  function initTheme() {
    const saved = localStorage.getItem('cq_theme') || 'dark';
    document.documentElement.setAttribute('data-theme', saved);
    const btn = document.getElementById('themeToggleBtn');
    if (btn) {
      btn.textContent = saved === 'light' ? '☾' : '☀';
      btn.setAttribute('aria-label', 'Switch to ' + (saved === 'light' ? 'Dark' : 'Light') + ' mode');
      btn.onclick = function () {
        const curr = document.documentElement.getAttribute('data-theme') || 'dark';
        const next = curr === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('cq_theme', next);
        btn.textContent = next === 'light' ? '☾' : '☀';
        btn.setAttribute('aria-label', 'Switch to ' + (next === 'light' ? 'Dark' : 'Light') + ' mode');
      };
    }
  }

  // 2. Web Audio API Chimes (Tone Synthesizer)
  let audioCtx = null;
  function isSoundEnabled() {
    return localStorage.getItem('cq_sound') !== 'false';
  }

  function playTone(type) {
    if (!isSoundEnabled()) return;
    try {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      const now = audioCtx.currentTime;

      if (type === 'success' || type === 'win') {
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(587.33, now); // D5
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.18); // A5
        gain.gain.setValueAtTime(0.08, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.22);
        osc.start(now);
        osc.stop(now + 0.22);
      } else if (type === 'error') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.setValueAtTime(180, now + 0.08);
        gain.gain.setValueAtTime(0.06, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
        osc.start(now);
        osc.stop(now + 0.2);
      } else {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        gain.gain.setValueAtTime(0.04, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
        osc.start(now);
        osc.stop(now + 0.08);
      }
    } catch (e) {}
  }

  function initSoundToggle() {
    const btn = document.getElementById('soundToggleBtn');
    if (!btn) return;
    btn.textContent = isSoundEnabled() ? '🔊' : '🔇';
    btn.onclick = function () {
      const next = !isSoundEnabled();
      localStorage.setItem('cq_sound', next ? 'true' : 'false');
      btn.textContent = next ? '🔊' : '🔇';
      if (next) playTone('click');
    };
  }

  // 3. Single Lightweight Confetti Particle Burst
  function fireConfetti() {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.inset = '0';
    canvas.style.width = '100vw';
    canvas.style.height = '100vh';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '99999';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    const dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width = window.innerWidth * dpr;
    canvas.height = window.innerHeight * dpr;
    ctx.scale(dpr, dpr);

    const colors = ['#10b981', '#34d399', '#6ee7b7', '#f59e0b', '#38bdf8'];
    const particles = [];
    const count = 45;
    const originX = window.innerWidth / 2;
    const originY = window.innerHeight * 0.45;

    for (let i = 0; i < count; i++) {
      const angle = (Math.PI * 2 * i) / count + (Math.random() - 0.5) * 0.5;
      const speed = 4 + Math.random() * 7;
      particles.push({
        x: originX,
        y: originY,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed - 2.5,
        size: 5 + Math.random() * 4,
        color: colors[Math.floor(Math.random() * colors.length)],
        alpha: 1,
        rotation: Math.random() * 360,
        vr: (Math.random() - 0.5) * 12,
      });
    }

    let start = null;
    function render(time) {
      if (!start) start = time;
      const elapsed = time - start;
      ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);

      let alive = false;
      for (let p of particles) {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.22; // gravity
        p.vx *= 0.98;
        p.rotation += p.vr;
        p.alpha = Math.max(0, 1 - elapsed / 1100);

        if (p.alpha > 0.01) {
          alive = true;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rotation * Math.PI) / 180);
          ctx.globalAlpha = p.alpha;
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
          ctx.restore();
        }
      }

      if (alive && elapsed < 1200) {
        requestAnimationFrame(render);
      } else {
        if (canvas.parentNode) canvas.parentNode.removeChild(canvas);
      }
    }
    requestAnimationFrame(render);
  }

  // 4. Guest LocalStorage Progress Sync
  function recordGuestCompleted(lessonId, xp) {
    let ids = JSON.parse(localStorage.getItem('cq_guest_lessons') || '[]');
    if (ids.indexOf(lessonId) === -1) {
      ids.push(lessonId);
      localStorage.setItem('cq_guest_lessons', JSON.stringify(ids));
    }
    let totalXp = parseInt(localStorage.getItem('cq_guest_xp') || '0', 10) + xp;
    localStorage.setItem('cq_guest_xp', totalXp.toString());
  }

  function getGuestCompletedIds() {
    return JSON.parse(localStorage.getItem('cq_guest_lessons') || '[]');
  }

  global.CodeQuest = {
    playTone: playTone,
    fireConfetti: fireConfetti,
    recordGuestCompleted: recordGuestCompleted,
    getGuestCompletedIds: getGuestCompletedIds,
  };

  window.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initSoundToggle();
  });
})(typeof window !== 'undefined' ? window : this);
