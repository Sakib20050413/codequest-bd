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

  global.CodeQuest = {
    playTone: playTone,
    fireConfetti: function () {}, // Safe no-op per restrained visual guidelines
    recordGuestCompleted: recordGuestCompleted,
    getGuestCompletedIds: getGuestCompletedIds,
    syncGuestProgress: syncGuestProgress,
  };

  window.addEventListener('DOMContentLoaded', function () {
    initTheme();
    initMobileMenu();
    initSoundToggle();
  });
})(typeof window !== 'undefined' ? window : this);
