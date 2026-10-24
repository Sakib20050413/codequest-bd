/**
 * CodeQuest BD — Ultra-Resilient Living Ambient Dual-Engine Canvas (v5.0)
 * 
 * Features:
 * 1. 4 Harmonic Volumetric Aurora Orbs (Smooth Lissajous harmonic drift)
 * 2. Precision Architectural Cyber-Dot Matrix with Mouse Proximity Lighting
 * 3. Interactive Constellation Nodes with Elastic Cursor Physics
 * 4. Dual-Mode Studio Palette: Deep Cosmic Obsidian (Dark) vs. Architectural Slate Aura (Light)
 * 5. Universal Viewport Coverage: Full-screen, Split-screen, Tiled, Dual-Monitor & Multi-DPI
 * 6. Zero Black-Void Guarantee: Handles prefers-reduced-motion gracefully with static architectural framing
 * 7. Active Multi-Window & Tab Auto-Recovery (Focus, Visibility & Hover Wakeup)
 */
(function () {
  'use strict';

  // Ensure DOM is ready before mounting
  function onReady(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  onReady(function initAmbientEngine() {
    // Avoid double mounting
    if (document.getElementById('ambientLiveCanvas')) {
      return;
    }

    const canvas = document.createElement('canvas');
    canvas.id = 'ambientLiveCanvas';
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '0';
    canvas.style.opacity = '1';
    canvas.style.transition = 'opacity 0.4s ease';

    // Mount at beginning of body
    if (document.body.firstChild) {
      document.body.insertBefore(canvas, document.body.firstChild);
    } else {
      document.body.appendChild(canvas);
    }

    const ctx = canvas.getContext('2d', { alpha: true });
    if (!ctx) return;

    let width = 0;
    let height = 0;
    let dpr = 1;
    let particles = [];
    let particleCount = 40;
    let mouse = { x: -2000, y: -2000, radius: 160 };
    let isRunning = true;
    let animationFrameId = null;

    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function isDarkTheme() {
      return document.documentElement.getAttribute('data-theme') !== 'light';
    }

    // Dual-mode Palettes with high-fidelity contrast
    const palettes = {
      dark: {
        orbs: [
          { color: '6, 182, 212', alpha: 0.22 },   // Cyber Cyan
          { color: '99, 102, 241', alpha: 0.24 },  // Electric Indigo
          { color: '16, 185, 129', alpha: 0.16 },  // Emerald Glow
          { color: '168, 85, 247', alpha: 0.18 }   // Royal Violet
        ],
        dotBase: 'rgba(255, 255, 255, 0.055)',
        dotActive: 'rgba(99, 102, 241, 0.38)',
        node: '99, 102, 241',
        line: '6, 182, 212'
      },
      light: {
        orbs: [
          { color: '14, 165, 233', alpha: 0.14 },  // Sky 500
          { color: '79, 70, 229', alpha: 0.13 },   // Indigo 600
          { color: '13, 148, 136', alpha: 0.10 },  // Teal 600
          { color: '245, 158, 11', alpha: 0.09 }   // Amber 500
        ],
        dotBase: 'rgba(15, 23, 42, 0.065)',
        dotActive: 'rgba(79, 70, 229, 0.30)',
        node: '79, 70, 229',
        line: '2, 132, 199'
      }
    };

    function calculateDimensions() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      width = Math.max(window.innerWidth || 0, document.documentElement.clientWidth || 0, document.body.clientWidth || 0);
      height = Math.max(window.innerHeight || 0, document.documentElement.clientHeight || 0);

      // Fallback for edge cases
      if (width < 320) width = window.screen.availWidth || 1280;
      if (height < 240) height = window.screen.availHeight || 800;

      canvas.width = Math.floor(width * dpr);
      canvas.height = Math.floor(height * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      particleCount = Math.min(65, Math.max(26, Math.floor(width / 32)));
    }

    function initParticles() {
      particles = [];
      for (let i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.45,
          vy: (Math.random() - 0.5) * 0.45,
          radius: Math.random() * 1.8 + 0.9,
          baseAlpha: Math.random() * 0.45 + 0.3
        });
      }
    }

    function onResize() {
      calculateDimensions();
      initParticles();
      if (prefersReducedMotion || !isRunning) {
        renderStaticPass();
      }
    }

    // Multi-viewport & Resize Observers
    window.addEventListener('resize', onResize, { passive: true });
    window.addEventListener('orientationchange', onResize, { passive: true });

    if (window.ResizeObserver) {
      const ro = new ResizeObserver(() => {
        calculateDimensions();
      });
      ro.observe(document.documentElement);
    }

    // Cursor tracking
    window.addEventListener('mousemove', (e) => {
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      // Hover wakeup
      if (!isRunning) {
        resumeLoop();
      }
    }, { passive: true });

    window.addEventListener('mouseleave', () => {
      mouse.x = -2000;
      mouse.y = -2000;
    }, { passive: true });

    // Multi-Window & Tab Visibility Management
    function resumeLoop() {
      if (!isRunning) {
        isRunning = true;
        if (!prefersReducedMotion) {
          if (animationFrameId) cancelAnimationFrame(animationFrameId);
          animationFrameId = requestAnimationFrame(loop);
        } else {
          renderStaticPass();
        }
      }
    }

    document.addEventListener('visibilitychange', () => {
      if (!document.hidden) {
        resumeLoop();
      }
    });

    window.addEventListener('focus', resumeLoop);
    window.addEventListener('pageshow', resumeLoop);

    // Dynamic Theme Observer
    const themeObserver = new MutationObserver(() => {
      if (prefersReducedMotion || !isRunning) {
        renderStaticPass();
      }
    });
    themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    window.addEventListener('cq:theme-changed', () => {
      if (prefersReducedMotion || !isRunning) renderStaticPass();
    });

    function drawRadialOrb(x, y, r, rgb, maxAlpha) {
      if (r <= 0) return;
      const grad = ctx.createRadialGradient(x, y, 0, x, y, r);
      grad.addColorStop(0, `rgba(${rgb}, ${maxAlpha})`);
      grad.addColorStop(0.45, `rgba(${rgb}, ${maxAlpha * 0.5})`);
      grad.addColorStop(1, `rgba(${rgb}, 0)`);
      ctx.fillStyle = grad;
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fill();
    }

    function drawAuroraOrbs(t, pal) {
      const orbList = pal.orbs;
      const time = t * 0.00045;

      // Orb 1 - Top Left / Center harmonic drift
      const x1 = width * 0.28 + Math.sin(time * 0.9) * (width * 0.22);
      const y1 = height * 0.22 + Math.cos(time * 0.7) * (height * 0.16);
      const r1 = Math.max(360, width * 0.36);
      drawRadialOrb(x1, y1, r1, orbList[0].color, orbList[0].alpha);

      // Orb 2 - Top Right harmonic drift
      const x2 = width * 0.72 + Math.cos(time * 0.8) * (width * 0.22);
      const y2 = height * 0.32 + Math.sin(time * 0.6) * (height * 0.18);
      const r2 = Math.max(380, width * 0.38);
      drawRadialOrb(x2, y2, r2, orbList[1].color, orbList[1].alpha);

      // Orb 3 - Lower Left harmonic drift
      const x3 = width * 0.24 + Math.cos(time * 0.65) * (width * 0.18);
      const y3 = height * 0.76 + Math.sin(time * 0.85) * (height * 0.18);
      const r3 = Math.max(320, width * 0.32);
      drawRadialOrb(x3, y3, r3, orbList[2].color, orbList[2].alpha);

      // Orb 4 - Lower Right harmonic drift
      const x4 = width * 0.76 + Math.sin(time * 0.75) * (width * 0.16);
      const y4 = height * 0.72 + Math.cos(time * 0.9) * (height * 0.22);
      const r4 = Math.max(340, width * 0.34);
      drawRadialOrb(x4, y4, r4, orbList[3].color, orbList[3].alpha);
    }

    function drawDotMatrix(pal) {
      const step = 44;
      const startX = (width % step) / 2;
      const startY = (height % step) / 2;
      const mouseRadSq = 150 * 150;

      for (let x = startX; x < width; x += step) {
        for (let y = startY; y < height; y += step) {
          let isNearMouse = false;
          let proximityAlpha = 0;

          if (mouse.x > 0) {
            const dx = mouse.x - x;
            const dy = mouse.y - y;
            const distSq = dx * dx + dy * dy;
            if (distSq < mouseRadSq) {
              isNearMouse = true;
              proximityAlpha = (1 - Math.sqrt(distSq) / 150);
            }
          }

          ctx.beginPath();
          ctx.arc(x, y, 1.25, 0, Math.PI * 2);

          if (isNearMouse) {
            ctx.fillStyle = pal.dotActive.replace('0.38', (0.15 + proximityAlpha * 0.32).toFixed(3));
          } else {
            ctx.fillStyle = pal.dotBase;
          }
          ctx.fill();
        }
      }
    }

    function drawParticlesAndFilaments(pal) {
      const nodeColor = pal.node;
      const lineColor = pal.line;

      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;

        // Interactive mouse physics
        const dx = mouse.x - p.x;
        const dy = mouse.y - p.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < mouse.radius) {
          const force = (mouse.radius - dist) / mouse.radius;
          p.x -= (dx / dist) * force * 1.8;
          p.y -= (dy / dist) * force * 1.8;
        }

        // Draw particle node
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${nodeColor}, ${p.baseAlpha})`;
        ctx.fill();

        // Connect filaments
        for (let j = i + 1; j < particles.length; j++) {
          const p2 = particles[j];
          const dist2 = Math.hypot(p.x - p2.x, p.y - p2.y);
          if (dist2 < 130) {
            const alpha = (1 - dist2 / 130) * 0.22;
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = `rgba(${lineColor}, ${alpha})`;
            ctx.lineWidth = 0.85;
            ctx.stroke();
          }
        }
      }
    }

    // Static pass for reduced motion or paused state (guarantees beauty without animation)
    function renderStaticPass() {
      ctx.clearRect(0, 0, width, height);
      const dark = isDarkTheme();
      const pal = dark ? palettes.dark : palettes.light;
      drawAuroraOrbs(12000, pal);
      drawDotMatrix(pal);
      // Static particle points
      for (let i = 0; i < particles.length; i++) {
        const p = particles[i];
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(${pal.node}, ${p.baseAlpha})`;
        ctx.fill();
      }
    }

    function loop(now) {
      if (!isRunning) return;

      ctx.clearRect(0, 0, width, height);
      const dark = isDarkTheme();
      const pal = dark ? palettes.dark : palettes.light;

      // Layer 1: Volumetric Aurora Orbs
      drawAuroraOrbs(now || performance.now(), pal);

      // Layer 2: Architectural Precision Dot Matrix
      drawDotMatrix(pal);

      // Layer 3: Interactive Constellation Nodes & Filaments
      drawParticlesAndFilaments(pal);

      animationFrameId = requestAnimationFrame(loop);
    }

    // Initialize and start
    calculateDimensions();
    initParticles();

    if (prefersReducedMotion) {
      renderStaticPass();
    } else {
      animationFrameId = requestAnimationFrame(loop);
    }
  });
})();
