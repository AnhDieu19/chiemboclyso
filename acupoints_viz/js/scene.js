import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

import { CSS2DRenderer } from 'three/addons/renderers/CSS2DRenderer.js';

export class SceneManager {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.labelRenderer = null; // New CSS2DRenderer
        this.controls = null;
        this.model = null;

        this.init();
    }

    init() {
        // 1. Setup Scene
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x202020);

        // 2. Setup Camera
        this.camera = new THREE.PerspectiveCamera(
            75,
            window.innerWidth / window.innerHeight,
            0.1,
            1000
        );
        this.camera.position.set(0, 1.5, 3);

        // 3. Setup WebGL Renderer
        this.renderer = new THREE.WebGLRenderer({ antialias: true });
        this.renderer.setSize(window.innerWidth, window.innerHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.container.appendChild(this.renderer.domElement);

        // 3b. Setup CSS2D Renderer (Labels)
        this.labelRenderer = new CSS2DRenderer();
        this.labelRenderer.setSize(window.innerWidth, window.innerHeight);
        this.labelRenderer.domElement.style.position = 'absolute';
        this.labelRenderer.domElement.style.top = '0px';
        this.labelRenderer.domElement.style.pointerEvents = 'none'; // Click through labels to scene
        this.container.appendChild(this.labelRenderer.domElement);

        // 4. Setup Controls
        // Note: Controls now need to listen to labelRenderer's DOM used for overlay if pointer events not blocked?
        // Usually we attach controls to the top-most element if we want interaction there.
        // But we set pointerEvents: none on labelRenderer, so clicks pass through to renderer.domElement.
        this.controls = new OrbitControls(this.camera, this.renderer.domElement);
        this.controls.enableDamping = true;
        this.controls.target.set(0, 1, 0);

        // 5. Setup Lights
        this.setupLights();

        // 6. Handle Resize
        window.addEventListener('resize', () => {
            this.camera.aspect = window.innerWidth / window.innerHeight;
            this.camera.updateProjectionMatrix();
            this.renderer.setSize(window.innerWidth, window.innerHeight);
            this.labelRenderer.setSize(window.innerWidth, window.innerHeight);
        });

        // 7. Start Loop
        this.renderer.setAnimationLoop(() => {
            this.controls.update();
            this.renderer.render(this.scene, this.camera);
            this.labelRenderer.render(this.scene, this.camera);
        });
    }

    setupLights() {
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.6); // Soft white light
        this.scene.add(ambientLight);

        const dirLight = new THREE.DirectionalLight(0xffffff, 1);
        dirLight.position.set(5, 10, 7.5);
        this.scene.add(dirLight);

        const backLight = new THREE.DirectionalLight(0xffffff, 0.5);
        backLight.position.set(-5, 5, -5);
        this.scene.add(backLight);
    }

    loadModel(url) {
        const loader = new GLTFLoader();
        const loadingEl = document.getElementById('loading');

        // Placeholder fallback if URL is dummy
        if (url === 'path/to/human_model.glb') {
            console.warn('Using fallback geometry because model URL is placeholder.');
            this.createFallbackModel();
            loadingEl.classList.add('hidden');
            return;
        }

        loader.load(
            url,
            (gltf) => {
                this.model = gltf.scene;

                // Adjust Material: Transparent to see internal points
                this.model.traverse((child) => {
                    if (child.isMesh) {
                        child.material.transparent = true;
                        child.material.opacity = 0.5;
                        child.material.depthWrite = false; // Fix transparency sorting issues mostly
                        // content wireframe option
                        // child.material.wireframe = true; 
                    }
                });

                this.scene.add(this.model);
                loadingEl.classList.add('hidden');
                console.log('Model loaded successfully');
            },
            (xhr) => {
                const percent = (xhr.loaded / xhr.total * 100);
                if (loadingEl) loadingEl.innerText = `Loading: ${Math.round(percent)}%`;
            },
            (error) => {
                console.error('An error happened loading the model:', error);
                loadingEl.innerText = 'Error loading model (Check console)';
                // Fallback
                this.createFallbackModel();
            }
        );
    }

    createFallbackModel() {
        // Create a simple capsule/cylinder to represent a human
        const geometry = new THREE.CapsuleGeometry(0.5, 1.8, 4, 8);
        const material = new THREE.MeshStandardMaterial({
            color: 0x00ff00,
            transparent: true,
            opacity: 0.5,
            wireframe: true
        });
        const capsule = new THREE.Mesh(geometry, material);
        capsule.position.set(0, 0.9, 0); // Lift up so bottom is at 0
        this.scene.add(capsule);
        this.model = capsule;
    }
}
