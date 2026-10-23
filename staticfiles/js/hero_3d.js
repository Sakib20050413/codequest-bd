/**
 * CodeQuest Tasteful 3D Wireframe Landing Hero
 * Lightweight, lazy-loaded Three.js cluster reacting smoothly to cursor coordinates.
 * Respects prefers-reduced-motion with static SVG fallback.
 */
(function () {
  'use strict';

  function initHero3D() {
    const container = document.getElementById('hero3dContainer');
    if (!container) return;

    // Check prefers-reduced-motion
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      container.innerHTML = `
        <div style="display:flex;align-items:center;justify-content:center;height:100%;">
          <svg viewBox="0 0 160 160" width="140" height="140" style="opacity:0.35;">
            <polygon points="80,15 145,52 145,127 80,165 15,127 15,52" fill="none" stroke="#10b981" stroke-width="2"/>
            <text x="80" y="90" font-family="monospace" font-size="28" font-weight="bold" fill="#10b981" text-anchor="middle">&lt;/&gt;</text>
          </svg>
        </div>`;
      return;
    }

    // Lazy load Three.js if not already present
    function mountScene() {
      if (typeof THREE === 'undefined') {
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
        script.onload = runThree;
        document.head.appendChild(script);
      } else {
        runThree();
      }
    }

    function runThree() {
      const w = container.clientWidth || 320;
      const h = container.clientHeight || 320;

      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(45, w / h, 0.1, 100);
      camera.position.z = 4.8;

      const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
      renderer.setSize(w, h);
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      container.innerHTML = '';
      container.appendChild(renderer.domElement);

      const group = new THREE.Group();
      scene.add(group);

      // Inner Wireframe Cube
      const cubeGeo = new THREE.BoxGeometry(1.6, 1.6, 1.6);
      const cubeEdges = new THREE.EdgesGeometry(cubeGeo);
      const cubeLine = new THREE.LineSegments(
        cubeEdges,
        new THREE.LineBasicMaterial({ color: 0x10b981, transparent: true, opacity: 0.85 })
      );
      group.add(cubeLine);

      // Outer Octahedron Halo Ring
      const octGeo = new THREE.OctahedronGeometry(1.2, 0);
      const octEdges = new THREE.EdgesGeometry(octGeo);
      const octLine = new THREE.LineSegments(
        octEdges,
        new THREE.LineBasicMaterial({ color: 0x34d399, transparent: true, opacity: 0.45 })
      );
      group.add(octLine);

      // Subtle Center Code Core
      const core = new THREE.Mesh(
        new THREE.IcosahedronGeometry(0.5, 0),
        new THREE.MeshBasicMaterial({ color: 0x10b981, wireframe: true, transparent: true, opacity: 0.6 })
      );
      group.add(core);

      let targetRotX = 0;
      let targetRotY = 0;

      window.addEventListener('mousemove', function (e) {
        const rect = container.getBoundingClientRect();
        const cx = rect.left + rect.width / 2;
        const cy = rect.top + rect.height / 2;
        const dx = (e.clientX - cx) / (window.innerWidth / 2);
        const dy = (e.clientY - cy) / (window.innerHeight / 2);
        targetRotY = dx * 0.45;
        targetRotX = dy * 0.45;
      });

      window.addEventListener('resize', function () {
        const nw = container.clientWidth;
        const nh = container.clientHeight;
        if (nw && nh) {
          camera.aspect = nw / nh;
          camera.updateProjectionMatrix();
          renderer.setSize(nw, nh);
        }
      });

      let animId;
      function animate() {
        animId = requestAnimationFrame(animate);
        group.rotation.y += 0.008;
        group.rotation.x += 0.004;
        group.rotation.x += (targetRotX - group.rotation.x) * 0.04;
        group.rotation.y += (targetRotY - group.rotation.y) * 0.04;
        core.rotation.y -= 0.012;
        renderer.render(scene, camera);
      }
      animate();
    }

    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver((entries) => {
        if (entries[0].isIntersecting) {
          mountScene();
          observer.disconnect();
        }
      });
      observer.observe(container);
    } else {
      setTimeout(mountScene, 400);
    }
  }

  window.addEventListener('DOMContentLoaded', initHero3D);
})();
