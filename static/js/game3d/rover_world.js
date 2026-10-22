/**
 * CodeQuest 3D - Three.js WebGL Rover World
 * Procedural 3D Isometric Grid, High-Tech Rover Mesh, Dynamic Lighting & Particles.
 */

class RoverWorld3D {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        if (!this.container) {
            console.error(`RoverWorld3D: Container #${containerId} not found.`);
            return;
        }

        // Configuration
        this.cols = options.cols || 8;
        this.rows = options.rows || 8;
        this.startPos = options.start || { x: 0, z: 0, dir: 'east' };
        this.portalPos = options.portal || { x: this.cols - 1, z: this.rows - 1 };
        this.obstacles = options.obstacles || []; // [{x, z}]
        this.gems = options.gems || []; // [{x, z}]
        this.tileSize = 2.0;

        // State
        this.roverState = { ...this.startPos };
        this.collectedGemsCount = 0;
        this.totalGemsCount = this.gems.length;
        this.energy = options.maxEnergy || 100;
        this.maxEnergy = options.maxEnergy || 100;
        this.cameraMode = 'isometric'; // 'isometric' | 'topdown' | 'follow'

        // Animation & Telemetry
        this.lastTime = performance.now();
        this.fps = 60;
        this.frameCount = 0;
        this.fpsTimer = performance.now();
        this.crystalsMap = new Map();
        this.particleSystems = [];

        this.initThree();
        this.buildStage();
        this.buildRover();
        this.buildObstacles();
        this.buildCrystals();
        this.buildPortal();
        this.setupControls();
        this.setupResizeListener();

        // Start render loop
        this.animate = this.animate.bind(this);
        requestAnimationFrame(this.animate);
    }

    initThree() {
        // Scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x0a0c14);
        this.scene.fog = new THREE.FogExp2(0x0a0c14, 0.025);

        // Camera
        const aspect = this.container.clientWidth / this.container.clientHeight;
        this.camera = new THREE.PerspectiveCamera(45, aspect, 0.1, 1000);

        // Renderer
        this.renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'high-performance' });
        this.renderer.setSize(this.container.clientWidth, this.container.clientHeight);
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
        this.renderer.toneMapping = THREE.ACESFilmicToneMapping;
        this.renderer.toneMappingExposure = 1.1;

        this.container.innerHTML = '';
        this.container.appendChild(this.renderer.domElement);

        // Lighting
        const ambientLight = new THREE.AmbientLight(0x334155, 1.2);
        this.scene.add(ambientLight);

        // Sun / Directional Shadow Light
        this.sunLight = new THREE.DirectionalLight(0xffffff, 1.4);
        this.sunLight.position.set(15, 25, 20);
        this.sunLight.castShadow = true;
        this.sunLight.shadow.mapSize.width = 2048;
        this.sunLight.shadow.mapSize.height = 2048;
        this.sunLight.shadow.camera.near = 0.5;
        this.sunLight.shadow.camera.far = 100;
        const d = 20;
        this.sunLight.shadow.camera.left = -d;
        this.sunLight.shadow.camera.right = d;
        this.sunLight.shadow.camera.top = d;
        this.sunLight.shadow.camera.bottom = -d;
        this.sunLight.shadow.bias = -0.0005;
        this.scene.add(this.sunLight);

        // Accent Cyan Fill Light
        const fillLight = new THREE.DirectionalLight(0x06b6d4, 0.6);
        fillLight.position.set(-15, 10, -15);
        this.scene.add(fillLight);

        this.setCameraView('isometric');
    }

    gridToWorld(gx, gz) {
        const ox = -(this.cols * this.tileSize) / 2 + this.tileSize / 2;
        const oz = -(this.rows * this.tileSize) / 2 + this.tileSize / 2;
        return {
            x: ox + gx * this.tileSize,
            y: 0,
            z: oz + gz * this.tileSize
        };
    }

    buildStage() {
        this.tileGroup = new THREE.Group();

        const tileGeo = new THREE.BoxGeometry(this.tileSize * 0.94, 0.3, this.tileSize * 0.94);

        for (let r = 0; r < this.rows; r++) {
            for (let c = 0; c < this.cols; c++) {
                const isEven = (r + c) % 2 === 0;
                const tileMat = new THREE.MeshStandardMaterial({
                    color: isEven ? 0x171e2e : 0x121724,
                    roughness: 0.5,
                    metalness: 0.4
                });

                const tile = new THREE.Mesh(tileGeo, tileMat);
                const pos = this.gridToWorld(c, r);
                tile.position.set(pos.x, -0.15, pos.z);
                tile.receiveShadow = true;

                // Subtle grid border accent
                const edgeGeo = new THREE.EdgesGeometry(tileGeo);
                const edgeMat = new THREE.LineBasicMaterial({ color: 0x1e293b, transparent: true, opacity: 0.4 });
                const wireframe = new THREE.LineSegments(edgeGeo, edgeMat);
                tile.add(wireframe);

                this.tileGroup.add(tile);
            }
        }

        // Sub-floor platform plane
        const baseFloorGeo = new THREE.BoxGeometry(this.cols * this.tileSize + 3, 0.6, this.rows * this.tileSize + 3);
        const baseFloorMat = new THREE.MeshStandardMaterial({ color: 0x090b10, roughness: 0.8, metalness: 0.2 });
        const baseFloor = new THREE.Mesh(baseFloorGeo, baseFloorMat);
        baseFloor.position.set(0, -0.6, 0);
        baseFloor.receiveShadow = true;
        this.tileGroup.add(baseFloor);

        this.scene.add(this.tileGroup);
    }

    buildRover() {
        this.roverMesh = new THREE.Group();

        // 1. Chassis Base
        const bodyGeo = new THREE.BoxGeometry(1.0, 0.4, 1.2);
        const bodyMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3, metalness: 0.7 });
        const body = new THREE.Mesh(bodyGeo, bodyMat);
        body.position.y = 0.35;
        body.castShadow = true;
        body.receiveShadow = true;
        this.roverMesh.add(body);

        // Chassis Armor Plates (Emerald stripes)
        const armorGeo = new THREE.BoxGeometry(0.7, 0.15, 0.9);
        const armorMat = new THREE.MeshStandardMaterial({ color: 0x0f172a, roughness: 0.4, metalness: 0.8 });
        const armor = new THREE.Mesh(armorGeo, armorMat);
        armor.position.set(0, 0.55, -0.05);
        this.roverMesh.add(armor);

        // 2. Cockpit Visor (Translucent glowing cyan)
        const visorGeo = new THREE.BoxGeometry(0.6, 0.2, 0.35);
        const visorMat = new THREE.MeshStandardMaterial({
            color: 0x06b6d4,
            emissive: 0x0891b2,
            emissiveIntensity: 0.6,
            roughness: 0.1,
            metalness: 0.9,
            transparent: true,
            opacity: 0.85
        });
        const visor = new THREE.Mesh(visorGeo, visorMat);
        visor.position.set(0, 0.55, 0.45);
        this.roverMesh.add(visor);

        // 3. Dual Headlight Spotlights
        this.headlight = new THREE.SpotLight(0x67e8f9, 2.5, 8, Math.PI / 6, 0.4, 1.2);
        this.headlight.position.set(0, 0.5, 0.6);
        this.headlightTarget = new THREE.Object3D();
        this.headlightTarget.position.set(0, 0, 4);
        this.roverMesh.add(this.headlightTarget);
        this.headlight.target = this.headlightTarget;
        this.roverMesh.add(this.headlight);

        // 4. Caterpillar Tracks / Wheels
        const trackGeo = new THREE.BoxGeometry(0.25, 0.35, 1.4);
        const trackMat = new THREE.MeshStandardMaterial({ color: 0x090b10, roughness: 0.9, metalness: 0.1 });

        const leftTrack = new THREE.Mesh(trackGeo, trackMat);
        leftTrack.position.set(-0.6, 0.2, 0);
        leftTrack.castShadow = true;
        this.roverMesh.add(leftTrack);

        const rightTrack = new THREE.Mesh(trackGeo, trackMat);
        rightTrack.position.set(0.6, 0.2, 0);
        rightTrack.castShadow = true;
        this.roverMesh.add(rightTrack);

        // 5. Rotating Radar Dish on top
        this.radarDish = new THREE.Group();
        const stalkGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.3, 8);
        const stalkMat = new THREE.MeshStandardMaterial({ color: 0x94a3b8, metalness: 0.8 });
        const stalk = new THREE.Mesh(stalkGeo, stalkMat);
        stalk.position.y = 0.75;
        this.radarDish.add(stalk);

        const dishGeo = new THREE.ConeGeometry(0.25, 0.12, 16, 1, true);
        const dishMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, emissive: 0x0284c7, emissiveIntensity: 0.4, side: THREE.DoubleSide });
        const dish = new THREE.Mesh(dishGeo, dishMat);
        dish.position.set(0, 0.9, 0);
        dish.rotation.x = Math.PI / 4;
        this.radarDish.add(dish);
        this.roverMesh.add(this.radarDish);

        // Position rover at start
        const startW = this.gridToWorld(this.roverState.x, this.roverState.z);
        this.roverMesh.position.set(startW.x, 0, startW.z);
        this.setRoverDirection(this.roverState.dir);

        this.scene.add(this.roverMesh);
    }

    buildCrystals() {
        this.crystalsMap.clear();
        this.crystalsGroup = new THREE.Group();

        const geo = new THREE.OctahedronGeometry(0.4, 0);
        const mat = new THREE.MeshStandardMaterial({
            color: 0x22d3ee,
            emissive: 0x06b6d4,
            emissiveIntensity: 0.8,
            roughness: 0.1,
            metalness: 0.9
        });

        this.gems.forEach((gem, idx) => {
            const mesh = new THREE.Mesh(geo, mat);
            const pos = this.gridToWorld(gem.x, gem.z);
            mesh.position.set(pos.x, 0.7, pos.z);
            mesh.castShadow = true;

            const light = new THREE.PointLight(0x06b6d4, 1.2, 3);
            light.position.set(0, 0, 0);
            mesh.add(light);

            mesh.userData = { gx: gem.x, gz: gem.z, initialY: 0.7, offset: idx * 1.5 };
            this.crystalsGroup.add(mesh);
            this.crystalsMap.set(`${gem.x},${gem.z}`, mesh);
        });

        this.scene.add(this.crystalsGroup);
    }

    buildObstacles() {
        this.obstaclesGroup = new THREE.Group();

        const pylonGeo = new THREE.CylinderGeometry(0.12, 0.16, 1.4, 8);
        const pylonMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.8, roughness: 0.2 });

        const beamGeo = new THREE.CylinderGeometry(0.08, 0.08, 1.2, 16);
        const beamMat = new THREE.MeshStandardMaterial({
            color: 0xf43f5e,
            emissive: 0xe11d48,
            emissiveIntensity: 1.5,
            transparent: true,
            opacity: 0.85
        });

        this.obstacles.forEach(obs => {
            const group = new THREE.Group();
            const pos = this.gridToWorld(obs.x, obs.z);
            group.position.set(pos.x, 0, pos.z);

            // Left Pylon
            const p1 = new THREE.Mesh(pylonGeo, pylonMat);
            p1.position.set(-0.7, 0.7, 0);
            p1.castShadow = true;
            group.add(p1);

            // Right Pylon
            const p2 = new THREE.Mesh(pylonGeo, pylonMat);
            p2.position.set(0.7, 0.7, 0);
            p2.castShadow = true;
            group.add(p2);

            // Laser Beam
            const beam = new THREE.Mesh(beamGeo, beamMat);
            beam.rotation.z = Math.PI / 2;
            beam.position.set(0, 0.7, 0);
            group.add(beam);

            const laserLight = new THREE.PointLight(0xf43f5e, 1.5, 3.5);
            laserLight.position.set(0, 0.7, 0);
            group.add(laserLight);

            this.obstaclesGroup.add(group);
        });

        this.scene.add(this.obstaclesGroup);
    }

    buildPortal() {
        this.portalGroup = new THREE.Group();
        const pos = this.gridToWorld(this.portalPos.x, this.portalPos.z);
        this.portalGroup.position.set(pos.x, 0, pos.z);

        // Concentric Torus Rings
        const torusGeo1 = new THREE.TorusGeometry(0.7, 0.08, 16, 32);
        const torusMat = new THREE.MeshStandardMaterial({
            color: 0x10b981,
            emissive: 0x059669,
            emissiveIntensity: 1.2,
            metalness: 0.7
        });
        this.portalRing1 = new THREE.Mesh(torusGeo1, torusMat);
        this.portalRing1.position.y = 0.8;
        this.portalGroup.add(this.portalRing1);

        const torusGeo2 = new THREE.TorusGeometry(0.45, 0.06, 16, 32);
        this.portalRing2 = new THREE.Mesh(torusGeo2, torusMat);
        this.portalRing2.position.y = 0.8;
        this.portalGroup.add(this.portalRing2);

        // Light Column Cylinder
        const beamGeo = new THREE.CylinderGeometry(0.5, 0.5, 4.0, 16, 1, true);
        const beamMat = new THREE.MeshBasicMaterial({
            color: 0x10b981,
            transparent: true,
            opacity: 0.25,
            side: THREE.DoubleSide
        });
        const beam = new THREE.Mesh(beamGeo, beamMat);
        beam.position.y = 2.0;
        this.portalGroup.add(beam);

        const portalLight = new THREE.PointLight(0x10b981, 2.0, 6);
        portalLight.position.set(0, 1.0, 0);
        this.portalGroup.add(portalLight);

        this.scene.add(this.portalGroup);
    }

    setupControls() {
        if (typeof THREE.OrbitControls !== 'undefined') {
            this.controls = new THREE.OrbitControls(this.camera, this.renderer.domElement);
            this.controls.enableDamping = true;
            this.controls.dampingFactor = 0.05;
            this.controls.maxPolarAngle = Math.PI / 2 - 0.05; // Don't go below floor
            this.controls.minDistance = 5;
            this.controls.maxDistance = 50;
        }
    }

    setCameraView(mode) {
        this.cameraMode = mode;
        const targetCenter = new THREE.Vector3(0, 0, 0);

        if (mode === 'isometric') {
            const dist = Math.max(this.cols, this.rows) * 1.8;
            this.camera.position.set(dist * 0.8, dist * 1.1, dist * 1.0);
            this.camera.lookAt(targetCenter);
            if (this.controls) {
                this.controls.target.copy(targetCenter);
                this.controls.enabled = true;
            }
        } else if (mode === 'topdown') {
            const h = Math.max(this.cols, this.rows) * 2.3;
            this.camera.position.set(0, h, 0.01);
            this.camera.lookAt(targetCenter);
            if (this.controls) {
                this.controls.target.copy(targetCenter);
                this.controls.enabled = true;
            }
        } else if (mode === 'follow') {
            if (this.controls) this.controls.enabled = false;
            this.updateFollowCamera();
        }
    }

    updateFollowCamera() {
        if (!this.roverMesh) return;
        const offset = new THREE.Vector3(0, 3.5, -4.5);
        offset.applyAxisAngle(new THREE.Vector3(0, 1, 0), this.roverMesh.rotation.y);
        this.camera.position.copy(this.roverMesh.position).add(offset);
        const lookTarget = this.roverMesh.position.clone().add(new THREE.Vector3(0, 0.8, 0));
        this.camera.lookAt(lookTarget);
    }

    setRoverDirection(dir) {
        this.roverState.dir = dir;
        let targetAngle = 0;
        if (dir === 'north') targetAngle = Math.PI;
        else if (dir === 'south') targetAngle = 0;
        else if (dir === 'east') targetAngle = Math.PI / 2;
        else if (dir === 'west') targetAngle = -Math.PI / 2;

        if (this.roverMesh) {
            this.roverMesh.rotation.y = targetAngle;
        }
    }

    collectCrystalAt(gx, gz) {
        const key = `${gx},${gz}`;
        if (this.crystalsMap.has(key)) {
            const crystal = this.crystalsMap.get(key);
            this.spawnCollectionParticles(crystal.position);
            this.crystalsGroup.remove(crystal);
            this.crystalsMap.delete(key);
            this.collectedGemsCount++;
            if (window.soundEngine) window.soundEngine.playGem();
            this.updateHUD();
        }
    }

    spawnCollectionParticles(pos) {
        const particleCount = 20;
        const geo = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);
        const velocities = [];

        for (let i = 0; i < particleCount; i++) {
            positions[i * 3] = pos.x;
            positions[i * 3 + 1] = pos.y;
            positions[i * 3 + 2] = pos.z;
            velocities.push(new THREE.Vector3(
                (Math.random() - 0.5) * 3,
                Math.random() * 3 + 1,
                (Math.random() - 0.5) * 3
            ));
        }

        geo.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        const mat = new THREE.PointsMaterial({ color: 0x22d3ee, size: 0.15, transparent: true, opacity: 1 });
        const particles = new THREE.Points(geo, mat);
        particles.userData = { velocities, life: 1.0 };
        this.scene.add(particles);
        this.particleSystems.push(particles);
    }

    reset() {
        this.roverState = { ...this.startPos };
        this.collectedGemsCount = 0;
        this.energy = this.maxEnergy;

        const startW = this.gridToWorld(this.startPos.x, this.startPos.z);
        this.roverMesh.position.set(startW.x, 0, startW.z);
        this.setRoverDirection(this.startPos.dir);

        // Rebuild crystals
        if (this.crystalsGroup) this.scene.remove(this.crystalsGroup);
        this.buildCrystals();

        this.updateHUD();
        if (this.cameraMode === 'follow') this.updateFollowCamera();
    }

    updateHUD() {
        const fpsEl = document.getElementById('hud-fps-count');
        const posEl = document.getElementById('hud-rover-coords');
        const gemEl = document.getElementById('hud-gem-count');
        const energyBar = document.getElementById('hud-energy-bar');

        if (fpsEl) fpsEl.textContent = `${this.fps} FPS`;
        if (posEl) posEl.textContent = `(${this.roverState.x}, ${this.roverState.z})`;
        if (gemEl) gemEl.textContent = `${this.collectedGemsCount} / ${this.totalGemsCount}`;
        if (energyBar) {
            const pct = Math.max(0, Math.min(100, (this.energy / this.maxEnergy) * 100));
            energyBar.style.width = `${pct}%`;
        }
    }

    setupResizeListener() {
        this.onResize = () => {
            if (!this.container) return;
            const w = this.container.clientWidth;
            const h = this.container.clientHeight;
            this.camera.aspect = w / h;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(w, h);
        };
        window.addEventListener('resize', this.onResize);
    }

    animate(now) {
        requestAnimationFrame(this.animate);

        const delta = (now - this.lastTime) / 1000;
        this.lastTime = now;

        // FPS Telemetry
        this.frameCount++;
        if (now - this.fpsTimer >= 1000) {
            this.fps = this.frameCount;
            this.frameCount = 0;
            this.fpsTimer = now;
            const fpsEl = document.getElementById('hud-fps-count');
            if (fpsEl) fpsEl.textContent = `${this.fps} FPS`;
        }

        // Radar Dish Spin
        if (this.radarDish) {
            this.radarDish.rotation.y += 2.5 * delta;
        }

        // Crystal Floating / Bobbing Animation
        if (this.crystalsMap) {
            this.crystalsMap.forEach(crystal => {
                crystal.rotation.y += 1.8 * delta;
                crystal.rotation.x += 0.8 * delta;
                const offset = crystal.userData.offset || 0;
                crystal.position.y = crystal.userData.initialY + Math.sin(now * 0.003 + offset) * 0.12;
            });
        }

        // Portal Rings Rotation
        if (this.portalRing1) {
            this.portalRing1.rotation.z += 1.5 * delta;
            this.portalRing2.rotation.z -= 2.0 * delta;
            this.portalRing2.rotation.x += 1.0 * delta;
        }

        // Particle Lifetimes
        for (let i = this.particleSystems.length - 1; i >= 0; i--) {
            const ps = this.particleSystems[i];
            ps.userData.life -= delta * 1.5;
            if (ps.userData.life <= 0) {
                this.scene.remove(ps);
                this.particleSystems.splice(i, 1);
            } else {
                ps.material.opacity = ps.userData.life;
                const positions = ps.geometry.attributes.position.array;
                for (let j = 0; j < ps.userData.velocities.length; j++) {
                    positions[j * 3] += ps.userData.velocities[j].x * delta;
                    positions[j * 3 + 1] += ps.userData.velocities[j].y * delta;
                    positions[j * 3 + 2] += ps.userData.velocities[j].z * delta;
                }
                ps.geometry.attributes.position.needsUpdate = true;
            }
        }

        // Controls / Camera
        if (this.cameraMode === 'follow') {
            this.updateFollowCamera();
        } else if (this.controls) {
            this.controls.update();
        }

        this.renderer.render(this.scene, this.camera);
    }
}

window.RoverWorld3D = RoverWorld3D;
