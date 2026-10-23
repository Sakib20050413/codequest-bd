/**
 * CodeQuest Core Platform Engine
 * Theme management, mobile drawer toggle, Web Audio synthesizer, and guest progress sync.
 */
(function (global) {
  'use strict';

  // 1. Theme Management (Light / Dark)
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

  // 2. Mobile Navigation Drawer
  function initMobileMenu() {
    const btn = document.getElementById('mobileMenuBtn');
    const drawer = document.getElementById('mobileNavDrawer');
    if (!btn || !drawer) return;

    btn.onclick = function () {
      const isOpen = drawer.classList.contains('open');
      if (isOpen) {
        drawer.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      } else {
        drawer.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    };

    // Close drawer when clicking outside or resizing
    window.addEventListener('resize', function () {
      if (window.innerWidth > 860 && drawer.classList.contains('open')) {
        drawer.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  // 3. Web Audio API Chimes (Tone Synthesizer)
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
        osc.frequency.exponentialRampToValueAtTime(880, now + 0.16); // A5
        gain.gain.setValueAtTime(0.06, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
        osc.start(now);
        osc.stop(now + 0.2);
      } else if (type === 'error') {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.setValueAtTime(180, now + 0.08);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.18);
        osc.start(now);
        osc.stop(now + 0.18);
      } else {
        osc.type = 'sine';
        osc.frequency.setValueAtTime(440, now);
        gain.gain.setValueAtTime(0.03, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
        osc.start(now);
        osc.stop(now + 0.06);
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

  function syncGuestProgress() {
    const completedIds = getGuestCompletedIds();
    const token = (document.cookie.match(/csrftoken=([^;]+)/) || [])[1] || '';
    return fetch('/api/progress/sync/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': token,
      },
      body: JSON.stringify({ completed_ids: completedIds }),
    }).then(function (res) {
      return res.json();
    });
  }

  // Mechanical Keyboard Switch Audio Synthesizer
  function playMechanicalClick() {
    if (!isSoundEnabled()) return;
    try {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') audioCtx.resume();
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      const now = audioCtx.currentTime;
      // High-frequency tactile crisp click
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(1400 + Math.random() * 200, now);
      osc.frequency.exponentialRampToValueAtTime(300, now + 0.025);
      gain.gain.setValueAtTime(0.04, now);
      gain.gain.exponentialRampToValueAtTime(0.001, now + 0.025);
      osc.start(now);
      osc.stop(now + 0.025);
    } catch (e) {}
  }

  // Lightweight Pure Canvas Confetti Micro-Celebration
  function fireConfetti(originX, originY) {
    try {
      let canvas = document.getElementById('cqConfettiCanvas');
      if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.id = 'cqConfettiCanvas';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '99999';
        document.body.appendChild(canvas);
      }
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      const particles = [];
      const colors = ['#6366f1', '#38bdf8', '#34d399', '#facc15', '#f472b6', '#a855f7'];
      const count = 48;
      const startX = originX || canvas.width / 2;
      const startY = originY || canvas.height / 3;

      for (let i = 0; i < count; i++) {
        const angle = Math.random() * Math.PI * 2;
        const speed = 4 + Math.random() * 7;
        particles.push({
          x: startX,
          y: startY,
          vx: Math.cos(angle) * speed,
          vy: Math.sin(angle) * speed - 3,
          size: 5 + Math.random() * 5,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          vRot: (Math.random() - 0.5) * 12,
          alpha: 1,
          decay: 0.015 + Math.random() * 0.015
        });
      }

      function renderFrame() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let alive = false;
        particles.forEach(function (p) {
          if (p.alpha > 0) {
            alive = true;
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.22; // gravity
            p.alpha -= p.decay;
            p.rotation += p.vRot;

            ctx.save();
            ctx.globalAlpha = Math.max(0, p.alpha);
            ctx.translate(p.x, p.y);
            ctx.rotate((p.rotation * Math.PI) / 180);
            ctx.fillStyle = p.color;
            ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
            ctx.restore();
          }
        });
        if (alive) {
          requestAnimationFrame(renderFrame);
        } else {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
      }
      renderFrame();
    } catch (e) {}
  }

  // 5. Daily Retention & Quests Engine (Point 21)
  function initDailyQuests() {
    const today = new Date().toISOString().slice(0, 10);
    const savedDate = localStorage.getItem('cq_quest_date');
    if (savedDate !== today) {
      localStorage.setItem('cq_quest_date', today);
      localStorage.setItem('cq_quests_state', JSON.stringify({ q1: false, q2: false, q3: true }));
    }
    const qState = JSON.parse(localStorage.getItem('cq_quests_state') || '{"q1":false,"q2":false,"q3":true}');
    const q2 = document.getElementById('quest2');
    if (q2) {
      q2.checked = !!qState.q2;
      q2.addEventListener('change', function () {
        qState.q2 = q2.checked;
        localStorage.setItem('cq_quests_state', JSON.stringify(qState));
        if (q2.checked) {
          playTone('win');
          fireConfetti();
        }
      });
    }
  }

  global.CodeQuest = {
    playTone: playTone,
    playMechanicalClick: playMechanicalClick,
    fireConfetti: fireConfetti,
    recordGuestCompleted: recordGuestCompleted,
    getGuestCompletedIds: getGuestCompletedIds,
    syncGuestProgress: syncGuestProgress,
  };

  window.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initMobileMenu();
    initSoundToggle();
    initDailyQuests();
  });
})(typeof window !== 'undefined' ? window : this);
