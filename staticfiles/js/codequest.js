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
        window.dispatchEvent(new CustomEvent('cq:theme-changed', { detail: { theme: next } }));
      };
    }
  }


  // 1b. Dynamic Fluid / Full-Width Layout Engine (Eliminates side blank margins)
  function initFluidLayout() {
    const saved = localStorage.getItem('cq_fluid_layout');
    // Default to true (fluid edge-to-edge view)
    const isFluid = saved === null ? true : saved === 'true';
    if (isFluid) {
      document.body.classList.add('is-fluid-layout');
    } else {
      document.body.classList.remove('is-fluid-layout');
    }

    const btn = document.getElementById('fluidToggleBtn');
    if (btn) {
      updateFluidBtn(btn, isFluid);
      btn.onclick = function () {
        const active = document.body.classList.toggle('is-fluid-layout');
        localStorage.setItem('cq_fluid_layout', active ? 'true' : 'false');
        updateFluidBtn(btn, active);
        if (global.CodeQuest && global.CodeQuest.playMechanicalClick) {
          global.CodeQuest.playMechanicalClick();
        }
      };
    }
  }

  function updateFluidBtn(btn, isFluid) {
    btn.innerHTML = isFluid ? '⛶' : '🗖';
    btn.setAttribute('title', isFluid ? 'Switch to Contained Width' : 'Switch to Dynamic Full-Width Layout');
    btn.setAttribute('aria-label', isFluid ? 'Contained Width' : 'Fluid Full-Width Layout');
    if (isFluid) {
      btn.classList.add('is-active-fluid');
    } else {
      btn.classList.remove('is-active-fluid');
    }
  }

  // 2. Mobile Navigation Drawer
  function initMobileMenu() {
    const btn = document.getElementById('mobileMenuBtn');
    const drawer = document.getElementById('mobileNavDrawer');
    const closeBtn = document.getElementById('mobileDrawerCloseBtn');
    if (!drawer) return;

    function openDrawer() {
      drawer.classList.add('open');
      if (btn) btn.setAttribute('aria-expanded', 'true');
      document.body.style.overflow = 'hidden'; // Prevent background scrolling
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
      closeBtn.onclick = function () {
        closeDrawer();
      };
    }

    // Close on navigation link click
    drawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', closeDrawer);
    });

    // Close on Escape key
    window.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('open')) {
        closeDrawer();
      }
    });

    // Close drawer when resizing to desktop
    window.addEventListener('resize', function () {
      if (window.innerWidth > 860 && drawer.classList.contains('open')) {
        closeDrawer();
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
      if (audioCtx.state === 'suspended') audioCtx.resume().catch(() => {});
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
    const desktopBtn = document.getElementById('soundToggleBtn');
    const mobileBtn = document.getElementById('mobileSoundToggleBtn');

    function syncButtons() {
      const enabled = isSoundEnabled();
      if (desktopBtn) {
        desktopBtn.textContent = enabled ? '🔊' : '🔇';
      }
      if (mobileBtn) {
        mobileBtn.textContent = enabled ? '🔊 Sound: ON' : '🔇 Sound: OFF';
        mobileBtn.style.color = enabled ? 'var(--accent)' : 'var(--text-muted)';
      }
    }

    syncButtons();

    function toggle() {
      const next = !isSoundEnabled();
      localStorage.setItem('cq_sound', next ? 'true' : 'false');
      syncButtons();
      if (next) playTone('click');
    }

    if (desktopBtn) desktopBtn.onclick = toggle;
    if (mobileBtn) mobileBtn.onclick = toggle;
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
      if (audioCtx.state === 'suspended') audioCtx.resume().catch(() => {});
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

  // 6. Card Spotlight & 3D Tilt Engine (Linear / Apple / Vercel Proximity Interaction)
  function initCardSpotlightAndTilt() {
    if (window.matchMedia('(pointer: coarse)').matches) return; // Touch devices use native tap gestures

    let activeCard = null;
    let rafId = null;
    let mouseX = 0;
    let mouseY = 0;
    let rect = null;

    document.addEventListener('mouseover', function (e) {
      const card = e.target.closest('.cq-card, .catalogue-course-card, .arcade-game-card, .arena-level-card, .arena-task-card, .hero-stat-card, .bento-tile, .featured-course-card, .lms-resume-card, .lms-habit-card, .cq-spotlight');
      if (card) {
        activeCard = card;
        rect = card.getBoundingClientRect();
      }
    }, { passive: true });

    document.addEventListener('mouseout', function (e) {
      if (activeCard && (!e.relatedTarget || !activeCard.contains(e.relatedTarget))) {
        activeCard.style.setProperty('--rot-x', '0deg');
        activeCard.style.setProperty('--rot-y', '0deg');
        activeCard = null;
      }
    }, { passive: true });

    document.addEventListener('mousemove', function (e) {
      if (!activeCard) return;
      mouseX = e.clientX;
      mouseY = e.clientY;

      if (!rafId) {
        rafId = requestAnimationFrame(function () {
          if (activeCard) {
            if (!rect) rect = activeCard.getBoundingClientRect();
            const x = mouseX - rect.left;
            const y = mouseY - rect.top;
            activeCard.style.setProperty('--mouse-x', x + 'px');
            activeCard.style.setProperty('--mouse-y', y + 'px');

            // Subtle 3D tilt calculation (clamped to max ±3.5deg for tactile luxury feel)
            if (activeCard.classList.contains('cq-card-interactive') ||
                activeCard.classList.contains('arcade-game-card') ||
                activeCard.classList.contains('arena-level-card') ||
                activeCard.classList.contains('catalogue-course-card') ||
                activeCard.classList.contains('hero-stat-card')) {
              const cx = rect.width / 2;
              const cy = rect.height / 2;
              const rotX = ((y - cy) / cy) * -3.5;
              const rotY = ((x - cx) / cx) * 3.5;
              activeCard.style.setProperty('--rot-x', rotX.toFixed(2) + 'deg');
              activeCard.style.setProperty('--rot-y', rotY.toFixed(2) + 'deg');
            }
          }
          rafId = null;
        });
      }
    }, { passive: true });

    window.addEventListener('scroll', function () {
      if (activeCard) rect = activeCard.getBoundingClientRect();
    }, { passive: true });
  }

  // 7. Scroll-Driven Staggered Entrance Reveal Engine
  function initScrollReveal() {
    if (typeof IntersectionObserver === 'undefined') {
      document.querySelectorAll('.cq-reveal').forEach(el => el.classList.add('cq-revealed'));
      return;
    }

    const observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('cq-revealed');
          obs.unobserve(entry.target);
        }
      });
    }, {
      threshold: 0.08,
      rootMargin: '0px 0px -30px 0px'
    });

    const targets = document.querySelectorAll(
      '.cq-card, .catalogue-course-card, .arcade-game-card, .arena-level-card, .arena-task-card, .hero-stat-card, .bento-tile, .featured-course-card, .lms-resume-card, .lms-habit-card, .cq-reveal'
    );

    targets.forEach(function (el) {
      if (!el.classList.contains('cq-reveal')) {
        el.classList.add('cq-reveal');
      }
      if (el.parentElement) {
        const siblings = Array.from(el.parentElement.children);
        const idx = siblings.indexOf(el);
        if (idx > 0 && idx < 8 && !el.style.transitionDelay) {
          el.style.transitionDelay = (idx * 50) + 'ms';
        }
      }
      observer.observe(el);
    });
  }

  // 8. Number Counter Rollup Engine (Quartic Ease-Out)
  function initNumberCounters() {
    const counterElements = document.querySelectorAll('[data-counter-val]');
    if (!counterElements.length) return;

    if (typeof IntersectionObserver === 'undefined') {
      counterElements.forEach(el => {
        el.textContent = (el.getAttribute('data-counter-prefix') || '') + 
                         parseFloat(el.getAttribute('data-counter-val')).toLocaleString() + 
                         (el.getAttribute('data-counter-suffix') || '');
      });
      return;
    }

    const observer = new IntersectionObserver(function (entries, obs) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          obs.unobserve(entry.target);
          animateCounter(entry.target);
        }
      });
    }, { threshold: 0.2 });

    counterElements.forEach(function (el) {
      observer.observe(el);
    });

    function animateCounter(el) {
      const targetVal = parseFloat(el.getAttribute('data-counter-val'));
      if (isNaN(targetVal)) return;
      const prefix = el.getAttribute('data-counter-prefix') || '';
      const suffix = el.getAttribute('data-counter-suffix') || '';
      const duration = 1400; // ms
      const startTime = performance.now();

      function step(now) {
        const elapsed = now - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 4);
        const currentVal = Math.round(ease * targetVal);
        el.textContent = prefix + currentVal.toLocaleString() + suffix;
        if (progress < 1) {
          requestAnimationFrame(step);
        } else {
          el.textContent = prefix + targetVal.toLocaleString() + suffix;
        }
      }
      requestAnimationFrame(step);
    }
  }

  // 9. Tactile Mechanical Click Sound Engine
  function initTactileClickSounds() {
    document.addEventListener('click', function (e) {
      const target = e.target.closest('.btn, .filter-pill, .ide-tab, .tab-btn, .hero-lang-tab, .nav-link-item, .game-filter-btn, .task-filter-pill, .arena-mode-pill');
      if (target && playMechanicalClick) {
        playMechanicalClick();
      }
    });
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
    initFluidLayout();
    initMobileMenu();
    initSoundToggle();
    initDailyQuests();
    initCardSpotlightAndTilt();
    initScrollReveal();
    initNumberCounters();
    initTactileClickSounds();
  });
})(typeof window !== 'undefined' ? window : this);
