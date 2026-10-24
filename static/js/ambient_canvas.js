/**
 * CodeQuest BD — Living Ambient 60fps Dual-Engine Canvas
 * Features:
 * 1. 4 Harmonic Volumetric Aurora Orbs (Smooth Lissajous harmonic drift)
 * 2. Precision Architectural Cyber-Dot Matrix with Mouse Proximity Lighting
 * 3. Interactive Constellation Nodes with Elastic Cursor Physics
 * 4. Dual-Mode Studio Palette: Deep Cosmic Obsidian (Dark) vs. Architectural Slate Aura (Light)
 * 5. High-DPI (Retina) Hardware-Accelerated Rendering & Power-Saving Visibility Engine
 */
(function () {
  'use strict';

  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return;
  }

  const canvas = document.createElement('canvas');
  canvas.id = 'ambientLiveCanvas';
  canvas.style.position = 'fixed';
  canvas.style.top = '0';
  canvas.style.left = '0';
  canvas.style.width = '100vw';
  canvas.style.height = '100vh';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '0';
  canvas.style.opacity = '1';
  canvas.style.transition = 'opacity 0.4s ease';

  document.body.prepend(canvas);

  const ctx = canvas.getContext('2d', { alpha: true });
  if (!ctx) return;

  let width = 0;
  let height = 0;
  let dpr = 1;
  let particles = [];
  const particleCount = Math.min(50, Math.max(25, Math.floor(window.innerWidth / 32)));
  let mouse = { x: -2000, y: -2000, radius: 150 };

  function isDarkTheme() {
    return document.documentElement.getAttribute('data-theme') !== 'light';
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = Math.floor(width * dpr);
    canvas.height = Math.floor(height * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function initParticles() {
    particles = [];
    for (let i = 0; i < particleCount; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.42,
        vy: (Math.random() - 0.5) * 0.42,
        radius: Math.random() * 1.6 + 0.8,
        baseAlpha: Math.random() * 0.4 + 0.25
      });
    }
  }

  window.addEventListener('resize', () => {
    resize();
    initParticles();
  });

  window.addEventListener('mousemove', (e) => {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  window.addEventListener('mouseleave', () => {
    mouse.x = -2000;
    mouse.y = -2000;
  });

  // Dual-mode Palettes
  const palettes = {
    dark: {
      orbs: [
        { color: '6, 182, 212', alpha: 0.18 },   // Cyber Cyan
        { color: '99, 102, 241', alpha: 0.20 },  // Electric Indigo
        { color: '16, 185, 129', alpha: 0.12 },  // Emerald Glow
        { color: '168, 85, 247', alpha: 0.13 }   // Royal Violet
      ],
      dotBase: 'rgba(255, 255, 255, 0.035)',
      dotActive: 'rgba(99, 102, 241, 0.32)',
      node: '99, 102, 241',
      line: '6, 182, 212'
    },
    light: {
      orbs: [
        { color: '14, 165, 233', alpha: 0.12 },  // Sky 500
        { color: '79, 70, 229', alpha: 0.11 },   // Indigo 600
        { color: '13, 148, 136', alpha: 0.08 },  // Teal 600
        { color: '245, 158, 11', alpha: 0.07 }   // Amber 500
      ],
      dotBase: 'rgba(15, 23, 42, 0.05)',
      dotActive: 'rgba(79, 70, 229, 0.25)',
      node: '79, 70, 229',
      line: '2, 132, 199'
    }
  };

  resize();
  initParticles();

  let isRunning = true;
  document.addEventListener('visibilitychange', () => {
    isRunning = !document.hidden;
    if (isRunning) requestAnimationFrame(loop);
  });

  // Watch for theme changes dynamically
  window.addEventListener('cq:theme-changed', () => {});
  const themeObserver = new MutationObserver(() => {});
  themeObserver.observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });

  function drawAuroraOrbs(t, pal) {
    const orbList = pal.orbs;
    const time = t * 0.0004;

    // Orb 1 - Top Left / Center drift
    const x1 = width * 0.3 + Math.sin(time * 0.9) * (width * 0.25);
    const y1 = height * 0.25 + Math.cos(time * 0.7) * (height * 0.18);
    const r1 = Math.max(340, width * 0.35);
    drawRadialOrb(x1, y1, r1, orbList[0].color, orbList[0].alpha);

    // Orb 2 - Top Right / Center drift
    const x2 = width * 0.7 + Math.cos(time * 0.8) * (width * 0.22);
    const y2 = height * 0.35 + Math.sin(time * 0.6) * (height * 0.2);
    const r2 = Math.max(360, width * 0.38);
    drawRadialOrb(x2, y2, r2, orbList[1].color, orbList[1].alpha);

    // Orb 3 - Lower Left drift
    const x3 = width * 0.25 + Math.cos(time * 0.65) * (width * 0.18);
    const y3 = height * 0.75 + Math.sin(time * 0.85) * (height * 0.18);
    const r3 = Math.max(300, width * 0.3);
    drawRadialOrb(x3, y3, r3, orbList[2].color, orbList[2].alpha);

    // Orb 4 - Lower Right drift
    const x4 = width * 0.78 + Math.sin(time * 0.75) * (width * 0.16);
    const y4 = height * 0.7 + Math.cos(time * 0.9) * (height * 0.22);
    const r4 = Math.max(320, width * 0.32);
    drawRadialOrb(x4, y4, r4, orbList[3].color, orbList[3].alpha);
  }

  function drawRadialOrb(x, y, r, rgb, maxAlpha) {
    const grad = ctx.createRadialGradient(x, y, 0, x, y, r);
    grad.addColorStop(0, `rgba(${rgb}, ${maxAlpha})`);
    grad.addColorStop(0.5, `rgba(${rgb}, ${maxAlpha * 0.45})`);
    grad.addColorStop(1, `rgba(${rgb}, 0)`);
    ctx.fillStyle = grad;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
  }

  function drawDotMatrix(pal) {
    const step = 44;
    const startX = (width % step) / 2;
    const startY = (height % step) / 2;
    const mouseRadSq = 140 * 140;

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
            proximityAlpha = (1 - Math.sqrt(distSq) / 140);
          }
        }

        ctx.beginPath();
        ctx.arc(x, y, 1.1, 0, Math.PI * 2);

        if (isNearMouse) {
          ctx.fillStyle = pal.dotActive.replace('0.32', (0.12 + proximityAlpha * 0.28).toFixed(3));
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

      // Mouse interactive push
      const dx = mouse.x - p.x;
      const dy = mouse.y - p.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < mouse.radius) {
        const force = (mouse.radius - dist) / mouse.radius;
        p.x -= (dx / dist) * force * 1.6;
        p.y -= (dy / dist) * force * 1.6;
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
        if (dist2 < 125) {
          const alpha = (1 - dist2 / 125) * 0.18;
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(p2.x, p2.y);
          ctx.strokeStyle = `rgba(${lineColor}, ${alpha})`;
          ctx.lineWidth = 0.75;
          ctx.stroke();
        }
      }
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

    requestAnimationFrame(loop);
  }

  requestAnimationFrame(loop);
})();
