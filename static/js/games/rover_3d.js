/**
 * CodeQuest BD — Cyber Rover 3D WebGL Simulation Engine
 * 15 Playable Planetary Robotics Missions using Three.js
 */
(function () {
  'use strict';

  const MISSIONS = [
    {
      id: 1,
      title: "Mars Crater Alpha",
      planet: "Mars",
      color: 0x993311,
      briefing: "Collect 3 glowing energy crystals scattered near the landing pod.",
      gems: [{ x: 1, z: -2 }, { x: -2, z: 1 }, { x: 2, z: 2 }],
    },
    {
      id: 2,
      title: "Olympus Mons Foothills",
      planet: "Mars",
      color: 0x882808,
      briefing: "Drive around volcanic terrain to harvest 3 mineral deposits.",
      gems: [{ x: -3, z: -1 }, { x: 0, z: -3 }, { x: 3, z: 1 }],
    },
    {
      id: 3,
      title: "Valles Marineris Diagonal Canyon",
      planet: "Mars",
      color: 0xaa4422,
      briefing: "Navigate the deep tectonic trench to retrieve 4 geological cores.",
      gems: [{ x: -2, z: -2 }, { x: -1, z: -1 }, { x: 1, z: 1 }, { x: 2, z: 2 }],
    },
    {
      id: 4,
      title: "Utopia Planitia Basin",
      planet: "Mars",
      color: 0x773311,
      briefing: "Locate 4 perimeter crystals in the ancient northern plain.",
      gems: [{ x: 0, z: -3 }, { x: 3, z: 0 }, { x: 0, z: 3 }, { x: -3, z: 0 }],
    },
    {
      id: 5,
      title: "Elysium Planitia Volcanic Ridge",
      planet: "Mars",
      color: 0x883818,
      briefing: "Ascend the basalt slope to extract 3 geothermal telemetry cores.",
      gems: [{ x: -1, z: -3 }, { x: 2, z: -1 }, { x: -2, z: 3 }],
    },
    {
      id: 6,
      title: "Jezero Delta Riverbeds",
      planet: "Mars",
      color: 0x994411,
      briefing: "Follow the dried river delta across 4 sediment sample locations.",
      gems: [{ x: -3, z: -2 }, { x: -1, z: 0 }, { x: 1, z: 2 }, { x: 3, z: 3 }],
    },
    {
      id: 7,
      title: "Gale Crater Spiral",
      planet: "Mars",
      color: 0x772211,
      briefing: "Spiral outwards from the landing zone to collect 4 stratus layers.",
      gems: [{ x: 1, z: 0 }, { x: 1, z: -2 }, { x: -2, z: -2 }, { x: -2, z: 2 }],
    },
    {
      id: 8,
      title: "Europa Subsurface Ice Sheets",
      planet: "Europa",
      color: 0x1e3a5f,
      briefing: "Traverse icy fracture lines on Jupiter's moon to secure 3 cryo-crystals.",
      gems: [{ x: -2, z: -1 }, { x: 2, z: -2 }, { x: 0, z: 2 }],
    },
    {
      id: 9,
      title: "Europa Thermal Vent Hydrothermal Zone",
      planet: "Europa",
      color: 0x0f2c4d,
      briefing: "Navigate around boiling ice geysers to sample 4 hydrothermal nodes.",
      gems: [{ x: -3, z: 1 }, { x: -1, z: -2 }, { x: 1, z: 2 }, { x: 3, z: -1 }],
    },
    {
      id: 10,
      title: "Titan Methane Ocean Shoreline",
      planet: "Titan",
      color: 0x78350f,
      briefing: "Survey hydrocarbon crystals on Saturn's atmospheric moon.",
      gems: [{ x: 0, z: -2 }, { x: 2, z: 1 }, { x: -2, z: 2 }],
    },
    {
      id: 11,
      title: "Titan Xanadu Dune Crossing",
      planet: "Titan",
      color: 0x92400e,
      briefing: "Cross the radar-bright Xanadu region to extract 4 atmospheric beacons.",
      gems: [{ x: -2, z: -3 }, { x: 3, z: -1 }, { x: -3, z: 2 }, { x: 1, z: 3 }],
    },
    {
      id: 12,
      title: "Enceladus Tiger Stripes Vents",
      planet: "Enceladus",
      color: 0x155e75,
      briefing: "Collect 4 vaporized water-ice plumes along south polar fractures.",
      gems: [{ x: -1, z: -2 }, { x: -2, z: 1 }, { x: 2, z: -1 }, { x: 1, z: 2 }],
    },
    {
      id: 13,
      title: "Lunar Shackleton Deep Crater",
      planet: "Moon",
      color: 0x334155,
      briefing: "Descend into perpetual shadow at the lunar south pole to find 4 water-ice caches.",
      gems: [{ x: -2, z: -2 }, { x: 2, z: -2 }, { x: 2, z: 2 }, { x: -2, z: 2 }],
    },
    {
      id: 14,
      title: "Asteroid 16 Psyche Metallic Core",
      planet: "Asteroids",
      color: 0x475569,
      briefing: "Survey a nickel-iron protoplanetary core for 3 heavy isotope modules.",
      gems: [{ x: -1, z: -3 }, { x: 3, z: 1 }, { x: -2, z: 2 }],
    },
    {
      id: 15,
      title: "Kuiper Belt Outpost Omega",
      planet: "Deep Space",
      color: 0x020617,
      briefing: "Recover 4 quantum telemetry transponders at humanity's farthest frontier.",
      gems: [{ x: -3, z: -3 }, { x: 3, z: -3 }, { x: -3, z: 3 }, { x: 3, z: 3 }],
    },
  ];

  let currentMissionIdx = 0;
  let scene, camera, renderer, controls;
  let roverGroup, groundMesh, gridHelper;
  let gems = [];
  let currentCameraMode = 'isometric';
  let collectedCount = 0;

  const GRID_SIZE = 7;
  const TILE_SIZE = 4;
  let roverState = {
    x: 0,
    z: 0,
    angle: 0
  };

  const completedMissions = new Set(JSON.parse(localStorage.getItem('cq_completed_rover') || '[]'));

  function getQueryLevel() {
    const params = new URLSearchParams(window.location.search);
    const lvl = parseInt(params.get('level'), 10);
    if (!isNaN(lvl) && lvl >= 1 && lvl <= MISSIONS.length) {
      return lvl - 1;
    }
    return 0;
  }

  function getCsrf() {
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function init3DWorld() {
    const container = document.getElementById('rover3dCanvas');
    if (!container || !window.THREE) return;

    currentMissionIdx = getQueryLevel();

    const width = container.clientWidth || 600;
    const height = container.clientHeight || 480;

    scene = new THREE.Scene();
    scene.background = new THREE.Color(0x070913);
    scene.fog = new THREE.FogExp2(0x070913, 0.025);

    camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    setCameraPerspective('isometric');

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    if (window.THREE.OrbitControls) {
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.05;
      controls.maxPolarAngle = Math.PI / 2 - 0.05;
    }

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

    createTerrain();
    createRover();
    loadMission(currentMissionIdx);

    window.addEventListener('resize', onWindowResize);
    animate();
    bindControls();
    renderMissionSelector();
  }

  function createTerrain() {
    const planeGeo = new THREE.PlaneGeometry(GRID_SIZE * TILE_SIZE, GRID_SIZE * TILE_SIZE);
    const planeMat = new THREE.MeshStandardMaterial({
      color: MISSIONS[currentMissionIdx].color,
      roughness: 0.85,
      metalness: 0.1
    });
    groundMesh = new THREE.Mesh(planeGeo, planeMat);
    groundMesh.rotation.x = -Math.PI / 2;
    groundMesh.receiveShadow = true;
    scene.add(groundMesh);

    gridHelper = new THREE.GridHelper(GRID_SIZE * TILE_SIZE, GRID_SIZE, 0x38bdf8, 0x1e293b);
    gridHelper.position.y = 0.02;
    scene.add(gridHelper);
  }

  function createRover() {
    roverGroup = new THREE.Group();

    const bodyGeo = new THREE.BoxGeometry(2.4, 0.9, 3.2);
    const bodyMat = new THREE.MeshStandardMaterial({
      color: 0x1e293b,
      metalness: 0.6,
      roughness: 0.3
    });
    const body = new THREE.Mesh(bodyGeo, bodyMat);
    body.position.y = 0.85;
    body.castShadow = true;
    body.receiveShadow = true;
    roverGroup.add(body);

    const panelGeo = new THREE.BoxGeometry(2.1, 0.05, 1.8);
    const panelMat = new THREE.MeshStandardMaterial({
      color: 0x0284c7,
      metalness: 0.9,
      roughness: 0.1,
      emissive: 0x0369a1,
      emissiveIntensity: 0.4
    });
    const solarPanel = new THREE.Mesh(panelGeo, panelMat);
    solarPanel.position.set(0, 1.35, 0.3);
    roverGroup.add(solarPanel);

    const antennaGeo = new THREE.CylinderGeometry(0.04, 0.04, 1.4);
    const antennaMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.8 });
    const antenna = new THREE.Mesh(antennaGeo, antennaMat);
    antenna.position.set(0.9, 1.8, 1.1);
    roverGroup.add(antenna);

    const dishGeo = new THREE.ConeGeometry(0.4, 0.2, 16);
    const dishMat = new THREE.MeshStandardMaterial({ color: 0xe2e8f0 });
    const dish = new THREE.Mesh(dishGeo, dishMat);
    dish.position.set(0.9, 2.5, 1.1);
    dish.rotation.x = Math.PI / 4;
    roverGroup.add(dish);

    const wheelGeo = new THREE.CylinderGeometry(0.5, 0.5, 0.45, 16);
    const wheelMat = new THREE.MeshStandardMaterial({
      color: 0x0f172a,
      roughness: 0.9,
      metalness: 0.2
    });

    const wheelPositions = [
      [-1.4, 0.5, -1.1],
      [1.4, 0.5, -1.1],
      [-1.4, 0.5, 0],
      [1.4, 0.5, 0],
      [-1.4, 0.5, 1.1],
      [1.4, 0.5, 1.1],
    ];

    wheelPositions.forEach(pos => {
      const wheel = new THREE.Mesh(wheelGeo, wheelMat);
      wheel.rotation.z = Math.PI / 2;
      wheel.position.set(pos[0], pos[1], pos[2]);
      wheel.castShadow = true;
      roverGroup.add(wheel);
    });

    const headlight = new THREE.SpotLight(0x38bdf8, 3, 15, Math.PI / 4, 0.3);
    headlight.position.set(0, 1.2, -1.2);
    headlight.target.position.set(0, 0, -8);
    roverGroup.add(headlight);
    roverGroup.add(headlight.target);

    const glowGeo = new THREE.SphereGeometry(0.2, 12, 12);
    const glowMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
    const indicator = new THREE.Mesh(glowGeo, glowMat);
    indicator.position.set(0, 1.1, -1.35);
    roverGroup.add(indicator);

    scene.add(roverGroup);
    syncRoverMeshPosition();
  }

  function spawnGems(mission) {
    gems.forEach(g => {
      scene.remove(g.mesh);
      scene.remove(g.light);
    });
    gems = [];

    const gemGeo = new THREE.OctahedronGeometry(0.7, 0);
    const gemMat = new THREE.MeshStandardMaterial({
      color: 0x10b981,
      emissive: 0x059669,
      emissiveIntensity: 0.7,
      metalness: 0.4,
      roughness: 0.1
    });

    mission.gems.forEach(pos => {
      const mesh = new THREE.Mesh(gemGeo, gemMat);
      mesh.position.set(pos.x * TILE_SIZE, 1.4, pos.z * TILE_SIZE);
      mesh.castShadow = true;
      scene.add(mesh);

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

  function loadMission(idx) {
    currentMissionIdx = idx;
    const mission = MISSIONS[idx];

    roverState = { x: 0, z: 0, angle: 0 };
    collectedCount = 0;

    if (groundMesh) {
      groundMesh.material.color.setHex(mission.color);
    }

    spawnGems(mission);
    syncRoverMeshPosition();

    const titleEl = document.getElementById('roverMissionTitle');
    const briefEl = document.getElementById('roverMissionBrief');
    const planetEl = document.getElementById('roverPlanetBadge');
    const banner = document.getElementById('missionSuccessBanner');

    if (titleEl) titleEl.textContent = `Mission ${mission.id} of 15: ${mission.title}`;
    if (briefEl) briefEl.textContent = mission.briefing;
    if (planetEl) planetEl.textContent = `${mission.planet} Sector`;
    if (banner) banner.style.display = 'none';

    updateHUD();
    logStatus(`Mission ${mission.id} initialized. Rover online at (0, 0).`);
  }

  function renderMissionSelector() {
    const container = document.getElementById('roverMissionPills');
    if (!container) return;
    container.innerHTML = "";
    MISSIONS.forEach(function (m, idx) {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "btn " + (idx === currentMissionIdx ? "btn-primary" : "btn-ghost");
      btn.style.padding = "0.3rem 0.65rem";
      btn.style.fontSize = "0.76rem";
      btn.style.fontFamily = "var(--font-mono)";
      btn.style.borderRadius = "6px";
      btn.style.minWidth = "36px";

      const isDone = completedMissions.has(m.id);
      btn.innerHTML = `${m.id}${isDone ? ' <span style="color:#10b981;">✓</span>' : ''}`;
      btn.title = `Mission ${m.id}: ${m.title} (${m.planet})`;

      btn.onclick = function () {
        loadMission(idx);
        renderMissionSelector();
      };
      container.appendChild(btn);
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

  const roverAPI = {
    forward: function () {
      const rad = (roverState.angle * Math.PI) / 180;
      const dx = Math.round(-Math.sin(rad));
      const dz = Math.round(-Math.cos(rad));

      const newX = roverState.x + dx;
      const newZ = roverState.z + dz;

      if (Math.abs(newX) <= 3 && Math.abs(newZ) <= 3) {
        roverState.x = newX;
        roverState.z = newZ;
        syncRoverMeshPosition();
        if (window.CodeQuest) window.CodeQuest.playTone('click');
        logStatus(`Rover advanced to (${newX}, ${newZ}).`);
      } else {
        logStatus(`⚠️ Boundary reached at (${newX}, ${newZ})!`, true);
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
      const totalRequired = MISSIONS[currentMissionIdx].gems.length;

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
        logStatus(`💎 Extracted energy crystal! (${collectedCount}/${totalRequired})`);
        updateHUD();

        if (collectedCount >= totalRequired) {
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
    completedMissions.add(MISSIONS[currentMissionIdx].id);
    localStorage.setItem('cq_completed_rover', JSON.stringify(Array.from(completedMissions)));
    renderMissionSelector();

    fetch('/api/games/rover-3d/score/', { method: 'POST', headers: { 'X-CSRFToken': getCsrf() } }).catch(() => {});
  }

  function updateHUD() {
    const coordsEl = document.getElementById('hudCoords');
    const gemsEl = document.getElementById('hudGems');
    const totalRequired = MISSIONS[currentMissionIdx] ? MISSIONS[currentMissionIdx].gems.length : 3;

    if (coordsEl) coordsEl.textContent = `(${roverState.x}, ${roverState.z})`;
    if (gemsEl) gemsEl.textContent = `${collectedCount} / ${totalRequired}`;
  }

  function logStatus(msg, isWarn = false) {
    const statusEl = document.getElementById('roverStatusMsg');
    if (statusEl) {
      statusEl.textContent = `Status: ${msg}`;
      statusEl.style.color = isWarn ? '#f59e0b' : 'var(--text-muted)';
    }
  }

  function bindControls() {
    const btnFwd = document.getElementById('dpadFwd');
    const btnLeft = document.getElementById('dpadLeft');
    const btnRight = document.getElementById('dpadRight');
    const btnCollect = document.getElementById('dpadCollect');
    const btnReset = document.getElementById('btnResetMission');
    const btnRunCode = document.getElementById('btnRunRoverScript');
    const nextMissionBtn = document.getElementById('nextMissionBtn');

    if (btnFwd) btnFwd.onclick = roverAPI.forward;
    if (btnLeft) btnLeft.onclick = roverAPI.turnLeft;
    if (btnRight) btnRight.onclick = roverAPI.turnRight;
    if (btnCollect) btnCollect.onclick = roverAPI.collect;
    if (btnReset) btnReset.onclick = () => loadMission(currentMissionIdx);

    if (nextMissionBtn) {
      nextMissionBtn.onclick = function () {
        if (currentMissionIdx < MISSIONS.length - 1) {
          loadMission(currentMissionIdx + 1);
        } else {
          loadMission(0);
        }
        renderMissionSelector();
      };
    }

    const isoBtn = document.getElementById('camIsoBtn');
    const topBtn = document.getElementById('camTopBtn');
    const chaseBtn = document.getElementById('camChaseBtn');
    if (isoBtn) isoBtn.onclick = () => setCameraPerspective('isometric');
    if (topBtn) topBtn.onclick = () => setCameraPerspective('topdown');
    if (chaseBtn) chaseBtn.onclick = () => setCameraPerspective('chase');

    if (btnRunCode) {
      btnRunCode.onclick = function () {
        const codeInput = document.getElementById('roverCodeInput');
        if (!codeInput) return;
        const lines = codeInput.value.split('\n');
        let delay = 0;

        lines.forEach(line => {
          const trimmed = line.trim();
          if (trimmed.startsWith('rover.forward()')) {
            setTimeout(roverAPI.forward, delay);
            delay += 400;
          } else if (trimmed.startsWith('rover.turnLeft()')) {
            setTimeout(roverAPI.turnLeft, delay);
            delay += 400;
          } else if (trimmed.startsWith('rover.turnRight()')) {
            setTimeout(roverAPI.turnRight, delay);
            delay += 400;
          } else if (trimmed.startsWith('rover.collect()')) {
            setTimeout(roverAPI.collect, delay);
            delay += 400;
          }
        });
      };
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

    gems.forEach((g, i) => {
      if (!g.collected && g.mesh) {
        g.mesh.rotation.y += 0.03;
        g.mesh.position.y = 1.4 + Math.sin(Date.now() * 0.003 + i) * 0.2;
      }
    });

    if (controls) controls.update();
    if (currentCameraMode === 'chase' && roverGroup) {
      camera.position.x = roverGroup.position.x;
      camera.position.z = roverGroup.position.z + 10;
      camera.lookAt(roverGroup.position.x, 1, roverGroup.position.z - 4);
    }

    if (renderer && scene && camera) {
      renderer.render(scene, camera);
    }
  }

  window.roverAPI = roverAPI;

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init3DWorld);
  } else {
    init3DWorld();
  }
})();
