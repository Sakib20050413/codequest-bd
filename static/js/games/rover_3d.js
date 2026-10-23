/**
 * CodeQuest BD — Cyber Rover 3D WebGL Simulation Engine
 * Uses Three.js for interactive 3D spatial programming
 */
(function () {
  'use strict';

  let scene, camera, renderer, controls;
  let roverGroup, gridHelper;
  let gems = [];
  let currentCameraMode = 'isometric';
  let collectedCount = 0;
  const TOTAL_GEMS = 3;

  // Rover Grid State (Grid size 7x7: from -3 to +3)
  const GRID_SIZE = 7;
  const TILE_SIZE = 4;
  let roverState = {
    x: 0,
    z: 0,
    angle: 0 // 0 = pointing North (-Z), 90 = East (+X), 180 = South (+Z), 270 = West (-X)
  };

  const GEM_POSITIONS = [
    { x: 1, z: -2 },
    { x: -2, z: 1 },
    { x: 2, z: 2 }
  ];

  function init3DWorld() {
    const container = document.getElementById('rover3dCanvas');
    if (!container || !window.THREE) return;

    const width = container.clientWidth || 600;
    const height = container.clientHeight || 480;

    // 1. Scene Setup
    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070913);
    scene.fog = new THREE.FogExp2(0x070913, 0.025);

    // 2. Camera Setup
    camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    setCameraPerspective('isometric');

    // 3. Renderer Setup
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // 4. OrbitControls
    if (window.THREE.OrbitControls) {
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.05;
      controls.maxPolarAngle = Math.PI / 2 - 0.05; // Don't clip below ground
    }

    // 5. Ambient & Directional Lighting
    const ambientLight = new THREE.AmbientLight(0x404868, 1.2);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xffffff, 1.5);
    dirLight.position.set(15, 25, 20);
    dirLight.castShadow = true;
    dirLight.shadow.mapSize.width = 1024;
    dirLight.shadow.mapSize.height = 1024;
    scene.add(dirLight);

    const blueRimLight = new THREE.DirectionalLight(0x38bdf8, 0.8);
    blueRimLight.position.set(-20, 10, -15);
    scene.add(blueRimLight);

    // 6. Terrain Ground & Grid
    createTerrain();

    // 7. Create 3D Rover
    createRover();

    // 8. Create Gems / Energy Cores
    spawnGems();

    // 9. Resize Listener
    window.addEventListener('resize', onWindowResize);

    // 10. Animation Loop
    animate();

    // 11. Bind UI Controls
    bindControls();
    updateHUD();
  }

  function createTerrain() {
    // Ground Plane with Cyber Martian Texture
    const planeGeo = new THREE.PlaneGeometry(GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE);
    const planeMat = new THREE.MeshStandardMaterial({
      color: 0x111625,
      roughness: 0.85,
      metalness: 0.15
    });
    const ground = new THREE.Mesh(planeGeo, planeMat);
    ground.rotation.x = -Math.PI / 2;
    ground.receiveShadow = true;
    scene.add(ground);

    // Grid lines
    gridHelper = new THREE.GridHelper(GRID_SIZE * TILE_SIZE, GRID_SIZE, 0x6366f1, 0x1e293b);
    gridHelper.position.y = 0.02;
    scene.add(gridHelper);

    // Outer Boundary Glow Fence
    const borderGeo = new THREE.BoxGeometry(GRID_SIZE * TILE_SIZE + 0.4, 0.4, GRID_SIZE * TILE_SIZE + 0.4);
    const borderMat = new THREE.MeshBasicMaterial({ color: 0x6366f1, wireframe: true });
    const border = new THREE.Mesh(borderGeo, borderMat);
    border.position.y = 0.2;
    scene.add(border);
  }

  function createRover() {
    roverGroup = new THREE.Group();

    // Rover Chassis (Body)
    const bodyGeo = new THREE.BoxGeometry(2, 0.8, 2.6);
    const bodyMat = new THREE.MeshStandardMaterial({
      color: 0x1e293b,
      metalness: 0.6,
      roughness: 0.3
    });
    const body = new THREE.Mesh(bodyGeo, bodyMat);
    body.position.y = 0.9;
    body.castShadow = true;
    roverGroup.add(body);

    // Cyan Top Plate
    const plateGeo = new THREE.BoxGeometry(1.6, 0.1, 2.2);
    const plateMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, metalness: 0.8, roughness: 0.2 });
    const plate = new THREE.Mesh(plateGeo, plateMat);
    plate.position.y = 1.35;
    roverGroup.add(plate);

    // 4 Wheels
    const wheelGeo = new THREE.CylinderGeometry(0.5, 0.5, 0.4, 16);
    const wheelMat = new THREE.MeshStandardMaterial({ color: 0x090b10, roughness: 0.9 });

    const wheelPositions = [
      [-1.15, 0.5, -0.9],
      [1.15, 0.5, -0.9],
      [-1.15, 0.5, 0.9],
      [1.15, 0.5, 0.9]
    ];

    wheelPositions.forEach(pos => {
      const wheel = new THREE.Mesh(wheelGeo, wheelMat);
      wheel.rotation.z = Math.PI / 2;
      wheel.position.set(pos[0], pos[1], pos[2]);
      wheel.castShadow = true;
      roverGroup.add(wheel);
    });

    // Headlight (Pointing forward / -Z)
    const headlight = new THREE.SpotLight(0x38bdf8, 3, 15, Math.PI / 4, 0.3);
    headlight.position.set(0, 1.2, -1.2);
    headlight.target.position.set(0, 0, -8);
    roverGroup.add(headlight);
    roverGroup.add(headlight.target);

    // Glow indicator on front
    const glowGeo = new THREE.SphereGeometry(0.2, 12, 12);
    const glowMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const indicator = new THREE.Mesh(glowGeo, glowMat);
    indicator.position.set(0, 1.1, -1.35);
    roverGroup.add(indicator);

    scene.add(roverGroup);
    syncRoverMeshPosition();
  }

  function spawnGems() {
    gems.forEach(g => scene.remove(g.mesh));
    gems = [];

    const gemGeo = new THREE.OctahedronGeometry(0.7, 0);
    const gemMat = new THREE.MeshStandardMaterial({
      color: 0x10b981,
      emissive: 0x059669,
      emissiveIntensity: 0.7,
      metalness: 0.4,
      roughness: 0.1
    });

    GEM_POSITIONS.forEach(pos => {
      const mesh = new THREE.Mesh(gemGeo, gemMat);
      mesh.position.set(pos.x * TILE_SIZE, 1.4, pos.z * TILE_SIZE);
      mesh.castShadow = true;
      scene.add(mesh);

      // Light glow above gem
      const pointLight = new THREE.PointLight(0x10b981, 1, 4);
      pointLight.position.set(pos.x * TILE_SIZE, 1.8, pos.z * TILE_SIZE);
      scene.add(pointLight);

      gems.push({
        x: pos.x,
        z: pos.z,
        mesh: mesh,
        light: pointLight,
        collected: false
      });
    });
  }

  function syncRoverMeshPosition() {
    if (!roverGroup) return;
    roverGroup.position.x = roverState.x * TILE_SIZE;
    roverGroup.position.z = roverState.z * TILE_SIZE;
    roverGroup.rotation.y = (roverState.angle * Math.PI) / 180;
  }

  function setCameraPerspective(mode) {
    currentCameraMode = mode;
    if (mode === 'isometric') {
      camera.position.set(16, 20, 22);
      camera.lookAt(0, 0, 0);
    } else if (mode === 'topdown') {
      camera.position.set(0, 32, 0.01);
      camera.lookAt(0, 0, 0);
    } else if (mode === 'chase' && roverGroup) {
      camera.position.set(roverGroup.position.x, 6, roverGroup.position.z + 10);
      camera.lookAt(roverGroup.position.x, 1, roverGroup.position.z - 4);
    }
  }

  // Autonomous Rover Movement API
  const roverAPI = {
    forward: function () {
      const rad = (roverState.angle * Math.PI) / 180;
      // In Three.js: angle 0 points forward along -Z
      const dx = Math.round(-Math.sin(rad));
      const dz = Math.round(-Math.cos(rad));

      const newX = roverState.x + dx;
      const newZ = roverState.z + dz;

      // Check bounds (-3 to +3)
      if (Math.abs(newX) <= 3 && Math.abs(newZ) <= 3) {
        roverState.x = newX;
        roverState.z = newZ;
        syncRoverMeshPosition();
        if (window.CodeQuest) window.CodeQuest.playTone('click');
        logStatus(`Rover advanced to (${newX}, ${newZ}).`);
      } else {
        logStatus(`⚠️ Warning: Terrain boundary reached at (${newX}, ${newZ})!`, true);
      }
      updateHUD();
    },

    turnLeft: function () {
      roverState.angle = (roverState.angle + 90) % 360;
      syncRoverMeshPosition();
      if (window.CodeQuest) window.CodeQuest.playTone('click');
      logStatus(`Rover turned left. Heading: ${roverState.angle}°`);
      updateHUD();
    },

    turnRight: function () {
      roverState.angle = (roverState.angle - 90 + 360) % 360;
      syncRoverMeshPosition();
      if (window.CodeQuest) window.CodeQuest.playTone('click');
      logStatus(`Rover turned right. Heading: ${roverState.angle}°`);
      updateHUD();
    },

    collect: function () {
      let found = false;
      gems.forEach(g => {
        if (!g.collected && g.x === roverState.x && g.z === roverState.z) {
          g.collected = true;
          scene.remove(g.mesh);
          scene.remove(g.light);
          collectedCount++;
          found = true;
        }
      });

      if (found) {
        if (window.CodeQuest) window.CodeQuest.playTone('success');
        logStatus(`💎 Extracted energy crystal! (${collectedCount}/${TOTAL_GEMS})`);
        updateHUD();

        if (collectedCount >= TOTAL_GEMS) {
          triggerMissionSuccess();
        }
      } else {
        logStatus(`No crystal detected at coordinate (${roverState.x}, ${roverState.z}).`, true);
      }
    }
  };

  function triggerMissionSuccess() {
    const banner = document.getElementById('missionSuccessBanner');
    if (banner) banner.style.display = 'flex';
    if (window.CodeQuest) {
      window.CodeQuest.playTone('win');
      window.CodeQuest.fireConfetti();
    }
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    const csrf = match ? match[1] : '';
    fetch('/api/games/rover-3d/score/', { method: 'POST', headers: { 'X-CSRFToken': csrf } }).catch(() => {});
  }

  function resetMission() {
    const banner = document.getElementById('missionSuccessBanner');
    if (banner) banner.style.display = 'none';
    roverState = { x: 0, z: 0, angle: 0 };
    collectedCount = 0;
    syncRoverMeshPosition();
    spawnGems();
    updateHUD();
    logStatus("Mission reset. Rover online at (0, 0).");
  }

  function updateHUD() {
    const coordsEl = document.getElementById('hudCoords');
    const gemsEl = document.getElementById('hudGems');
    if (coordsEl) coordsEl.textContent = `(${roverState.x}, ${roverState.z})`;
    if (gemsEl) gemsEl.textContent = `${collectedCount} / ${TOTAL_GEMS}`;
  }

  function logStatus(msg, isWarn = false) {
    const statusEl = document.getElementById('roverStatusMsg');
    if (statusEl) {
      statusEl.textContent = `Status: ${msg}`;
      statusEl.style.color = isWarn ? '#f59e0b' : 'var(--text-muted)';
    }
  }

  function onWindowResize() {
    const container = document.getElementById('rover3dCanvas');
    if (!container || !renderer || !camera) return;
    const w = container.clientWidth;
    const h = container.clientHeight;
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  }

  function animate() {
    requestAnimationFrame(animate);

    // Floating gem animation
    const time = Date.now() * 0.0025;
    gems.forEach(g => {
      if (!g.collected && g.mesh) {
        g.mesh.rotation.y += 0.03;
        g.mesh.position.y = 1.4 + Math.sin(time + g.x) * 0.25;
      }
    });

    if (controls) controls.update();
    if (renderer && scene && camera) {
      renderer.render(scene, camera);
    }
  }

  function bindControls() {
    const btnFwd = document.getElementById('btnForward');
    const btnLeft = document.getElementById('btnTurnLeft');
    const btnRight = document.getElementById('btnTurnRight');
    const btnGrab = document.getElementById('btnCollect');
    const btnRun = document.getElementById('btnRunScript');
    const btnReset = document.getElementById('resetMissionBtn');

    const camIso = document.getElementById('camIsoBtn');
    const camTop = document.getElementById('camTopBtn');
    const camChase = document.getElementById('camChaseBtn');

    if (btnFwd) btnFwd.onclick = roverAPI.forward;
    if (btnLeft) btnLeft.onclick = roverAPI.turnLeft;
    if (btnRight) btnRight.onclick = roverAPI.turnRight;
    if (btnGrab) btnGrab.onclick = roverAPI.collect;
    if (btnReset) btnReset.onclick = resetMission;

    if (camIso) camIso.onclick = () => setCameraPerspective('isometric');
    if (camTop) camTop.onclick = () => setCameraPerspective('topdown');
    if (camChase) camChase.onclick = () => setCameraPerspective('chase');

    // Keyboard bindings
    window.addEventListener('keydown', function (e) {
      if (document.activeElement && document.activeElement.tagName === 'TEXTAREA') return;
      if (e.key === 'w' || e.key === 'ArrowUp') { roverAPI.forward(); e.preventDefault(); }
      if (e.key === 'a' || e.key === 'ArrowLeft') { roverAPI.turnLeft(); e.preventDefault(); }
      if (e.key === 'd' || e.key === 'ArrowRight') { roverAPI.turnRight(); e.preventDefault(); }
      if (e.key === ' ' || e.key === 'Enter') { roverAPI.collect(); e.preventDefault(); }
    });

    // Run script execution
    if (btnRun) {
      btnRun.onclick = function () {
        const scriptBox = document.getElementById('roverScriptBox');
        if (!scriptBox) return;
        const code = scriptBox.value;

        try {
          const fn = new Function('rover', code);
          fn(roverAPI);
          logStatus("Autonomous script execution complete.");
        } catch (err) {
          logStatus(`Syntax Error in script: ${err.message}`, true);
        }
      };
    }
  }

  window.addEventListener('DOMContentLoaded', init3DWorld);
})();
