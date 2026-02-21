import * as THREE from 'three';
import * as d3 from 'd3';

export class VisualizationManager {
    constructor(sceneManager) {
        this.sceneManager = sceneManager;
        this.acupoints = [];
        this.meridians = [];

        // Group to hold visualization elements
        this.vizGroup = new THREE.Group();
        this.sceneManager.scene.add(this.vizGroup);

        this.loadData();
    }

    async loadData() {
        try {
            // Use D3 to load JSON data
            // Note: d3.json returns a Promise
            const [acupointsData, meridiansData] = await Promise.all([
                d3.json('./assets/data/acupoints.json'),
                d3.json('./assets/data/meridians.json')
            ]);

            this.acupoints = acupointsData;
            this.meridians = meridiansData;

            console.log("Data loaded:", this.acupoints, this.meridians);

            this.renderVisualization();
        } catch (error) {
            console.error("Error loading data:", error);
        }
    }

    renderVisualization() {
        this.renderMeridians();
        this.renderPoints();
    }

    renderPoints() {
        const geometry = new THREE.SphereGeometry(0.015, 16, 16);

        // Create a color scale using D3 if needed, but we have hex colors in meridians
        // Map meridian ID to color
        const colorMap = {};
        this.meridians.forEach(m => {
            colorMap[m.id] = m.colorHex;
        });

        this.acupoints.forEach(point => {
            const color = colorMap[point.meridianId] || 0xffffff;
            const material = new THREE.MeshBasicMaterial({ color: color });
            const sphere = new THREE.Mesh(geometry, material);

            sphere.position.set(point.position.x, point.position.y, point.position.z);
            sphere.name = point.id; // naming for raycaster
            sphere.userData = { ...point }; // store data for interaction

            import { CSS2DObject } from 'three/addons/renderers/CSS2DRenderer.js';

            this.vizGroup.add(sphere);

            // Create CSS2D Label
            const div = document.createElement('div');
            div.className = 'acupoint-label';
            div.textContent = point.name;
            div.style.marginTop = '-1em';
            div.style.color = '#fff';
            div.style.fontSize = '12px';
            div.style.textShadow = '0 0 2px #000';
            div.style.pointerEvents = 'none';
            div.style.opacity = '0.7';

            const label = new CSS2DObject(div);
            label.position.set(0, 0.02, 0);
            sphere.add(label);
        });
    }

    highlightPoint(mesh) {
        if (mesh.userData) {
            mesh.material.color.setHex(0xff0000);
            mesh.scale.setScalar(1.5);
            this.updateInfoPanel(mesh.userData);
        }
    }

    resetHighlight(mesh) {
        if (mesh && mesh.userData) {
            // Find original color
            const mData = this.meridians.find(m => m.id === mesh.userData.meridianId);
            const color = mData ? mData.colorHex : 0xffffff;
            mesh.material.color.setHex(color);
            mesh.scale.setScalar(1.0);
        }
    }

    updateInfoPanel(data) {
        d3.select('#info-panel').remove();

        const panel = d3.select('body').append('div')
            .attr('id', 'info-panel')
            .style('position', 'absolute')
            .style('top', '20px')
            .style('left', '20px')
            .style('background', 'rgba(0,0,0,0.8)')
            .style('padding', '15px')
            .style('border-radius', '8px')
            .style('max-width', '300px')
            .style('border', '1px solid #444');

        panel.append('h3')
            .text(`${data.id} - ${data.name}`)
            .style('margin', '0 0 10px 0')
            .style('color', '#ffeb3b');

        panel.append('p')
            .html(`<strong>Kinh:</strong> ${(this.meridians.find(m => m.id === data.meridianId) || {}).name}<br>
                   <strong>Mô tả:</strong> ${data.description}`);
    }

    renderMeridians() {
        // Group points by meridian
        const pointsByMeridian = d3.group(this.acupoints, d => d.meridianId);

        pointsByMeridian.forEach((points, meridianId) => {
            const meridianInfo = this.meridians.find(m => m.id === meridianId);
            if (!meridianInfo) return;

            // Sort points if they have an order, for now assume array order is correct
            // Ideally we need a connectivity graph, but let's draw line through them sequentially for now

            const material = new THREE.LineBasicMaterial({
                color: meridianInfo.colorHex,
                linewidth: 2 // Note: WebGL linewidth doesn't always work on Windows/all browsers
            });

            const geometry = new THREE.BufferGeometry();
            const positions = [];

            points.forEach(p => {
                positions.push(p.position.x, p.position.y, p.position.z);
            });

            geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));

            const line = new THREE.Line(geometry, material);
            this.vizGroup.add(line);
        });
    }
}
