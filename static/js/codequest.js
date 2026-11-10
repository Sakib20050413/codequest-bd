/**
 * CodeQuest Core UI Script
 * Handles theme switching (default: light), mobile menu drawer, and guest progress sync.
 */
(function (global) {
  'use strict';

  function initTheme() {
    const saved = localStorage.getItem('cq_theme_v7') || 'light';
    document.documentElement.setAttribute('data-theme', saved);
    const btn = document.getElementById('themeToggleBtn');
    if (btn) {
      btn.textContent = saved === 'light' ? 'Dark Mode' : 'Light Mode';
      btn.onclick = function () {
        const curr = document.documentElement.getAttribute('data-theme') || 'light';
        const next = curr === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('cq_theme_v7', next);
        btn.textContent = next === 'light' ? 'Dark Mode' : 'Light Mode';
        window.dispatchEvent(new CustomEvent('cq:theme-changed', { detail: { theme: next } }));
      };
    }
  }

  function initMobileMenu() {
    const btn = document.getElementById('mobileMenuBtn');
    const drawer = document.getElementById('mobileNavDrawer');
    const closeBtn = document.getElementById('mobileDrawerCloseBtn');
    if (!drawer) return;

    function openDrawer() {
      drawer.classList.add('open');
      if (btn) btn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden';
    }

    function closeDrawer() {
      drawer.classList.remove('open');
      if (btn) btn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    if (btn) {
      btn.onclick = function (e) {
        e.stopPropagation();
        if (drawer.classList.contains('open')) {
          closeDrawer();
        } else {
          openDrawer();
        }
      };
    }

    if (closeBtn) {
      closeBtn.onclick = closeDrawer;
    }

    drawer.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', closeDrawer);
    });

    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) {
        closeDrawer();
      }
    });

    window.addEventListener('resize', function () {
      if (window.innerWidth > 860 && drawer.classList.contains('open')) {
        closeDrawer();
      }
    });
  }

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

  // Keep no-op helpers so existing lesson/game scripts calling CodeQuest.playTone don't error
  function playTone() {}
  function playMechanicalClick() {}
  function fireConfetti() {}

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
  });
})(typeof window !== 'undefined' ? window : this);
