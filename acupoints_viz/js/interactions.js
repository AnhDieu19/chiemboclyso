import * as THREE from 'three';

export class InteractionManager {
    constructor(sceneManager) {
        this.sceneManager = sceneManager;
        this.raycaster = new THREE.Raycaster();
        this.pointer = new THREE.Vector2();

        // Container for persistent markers
        this.markerGroup = new THREE.Group();
        this.sceneManager.scene.add(this.markerGroup);

        this.initEventListeners();
    }

    initEventListeners() {
        window.addEventListener('click', (event) => this.onMouseClick(event));
        window.addEventListener('mousemove', (event) => this.onMouseMove(event));
    }

    onMouseMove(event) {
        this.pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
        this.pointer.y = - (event.clientY / window.innerHeight) * 2 + 1;

        this.raycaster.setFromCamera(this.pointer, this.sceneManager.camera);

        const intersects = this.raycaster.intersectObjects(this.sceneManager.scene.children, true);

        // Check for acupoint spheres (they have userData.isAcupoint or similar, 
        // but in viz.js we didn't explicitly set isAcupoint flag in userData, let's rely on checking if it has meridianId)
        const hit = intersects.find(i => i.object.userData && i.object.userData.meridianId);

        if (hit) {
            if (this.hoveredObj !== hit.object) {
                if (this.hoveredObj) this.sceneManager.vizManager?.resetHighlight(this.hoveredObj);

                this.hoveredObj = hit.object;
                this.sceneManager.vizManager?.highlightPoint(this.hoveredObj);
                document.body.style.cursor = 'pointer';
            }
        } else {
            if (this.hoveredObj) {
                this.sceneManager.vizManager?.resetHighlight(this.hoveredObj);
                this.hoveredObj = null;
                document.body.style.cursor = 'default';
            }
        }
    }

    onMouseClick(event) {
        // 1. Calculate pointer position in normalized device coordinates (-1 to +1)
        this.pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
        this.pointer.y = - (event.clientY / window.innerHeight) * 2 + 1;

        // 2. Update the raycaster
        this.raycaster.setFromCamera(this.pointer, this.sceneManager.camera);

        // 3. Find intersections
        // Note: Recursive = true to check all descendants of the scene
        const intersects = this.raycaster.intersectObjects(this.sceneManager.scene.children, true);

        if (intersects.length > 0) {
            // Find the first object that is NOT a marker and NOT a helper
            // We want to click on the Human Model (or fallback capsule)
            const hit = intersects.find(i => !this.isMarker(i.object) && i.object.type === 'Mesh');

            if (hit) {
                console.log(`🎯 Hit at: x=${hit.point.x.toFixed(4)}, y=${hit.point.y.toFixed(4)}, z=${hit.point.z.toFixed(4)}`);
                console.log(`   Object: ${hit.object.name || hit.object.uuid}`);

                this.addMarker(hit.point);
                this.updateDebugUI(hit.point);
            }
        }
    }

    isMarker(object) {
        // Simple check if object belongs to our marker group
        return object.parent === this.markerGroup;
    }

    addMarker(position) {
        // Create a small red sphere
        const geometry = new THREE.SphereGeometry(0.02, 16, 16);
        const material = new THREE.MeshBasicMaterial({ color: 0xff0000 });
        const marker = new THREE.Mesh(geometry, material);

        marker.position.copy(position);
        this.markerGroup.add(marker);

        // Optional: Remove old markers if too many? For now keep them to trace meridians.
    }

    updateDebugUI(point) {
        // Create or update a simple HTML overlay to show coordinates
        let coordDiv = document.getElementById('debug-coords');
        if (!coordDiv) {
            coordDiv = document.createElement('div');
            coordDiv.id = 'debug-coords';
            coordDiv.style.position = 'absolute';
            coordDiv.style.bottom = '10px';
            coordDiv.style.left = '10px';
            coordDiv.style.backgroundColor = 'rgba(0,0,0,0.7)';
            coordDiv.style.color = '#fff';
            coordDiv.style.padding = '10px';
            coordDiv.style.fontFamily = 'monospace';
            coordDiv.style.borderRadius = '5px';
            document.body.appendChild(coordDiv);
        }

        const jsonString = `{"x": ${point.x.toFixed(4)}, "y": ${point.y.toFixed(4)}, "z": ${point.z.toFixed(4)}}`;

        coordDiv.innerHTML = `
            <strong>Last Picked Point:</strong><br>
            x: ${point.x.toFixed(4)}<br>
            y: ${point.y.toFixed(4)}<br>
            z: ${point.z.toFixed(4)}<br>
            <button onclick="navigator.clipboard.writeText('${jsonString}')" style="margin-top:5px; cursor:pointer;">Copy JSON</button>
        `;
    }
}
