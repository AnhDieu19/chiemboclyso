/**
 * Tu Vi Knowledge Graph - Core Graph Class Module
 * Class TuViKnowledgeGraph chính để render và quản lý D3.js visualization
 */

class TuViKnowledgeGraph {
    constructor(containerId = '#graph') {
        this.containerId = containerId;
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.data = TUVI_GRAPH_DATA;
        this.config = window.TuViGraphConfig;
        this.showLabels = true;
        this.activeFilters = new Set(['all']);

        this.init();
    }

    init() {
        this.setupSVG();
        this.setupArrowMarkers();
        this.setupSimulation();
        this.setupFiveElementsSphere(); // Apply 5 Elements Layout
        this.render();
        this.updateStats();
        this.setupEventListeners();
    }

    getNodeColor(node) {
        const colors = this.config.colors.types;
        const nguHanhColors = this.config.colors.ngu_hanh;

        // Ưu tiên màu riêng của Ngũ Hành (Kim, Mộc, Thủy, Hỏa, Thổ)
        if (nguHanhColors[node.id]) {
            return nguHanhColors[node.id];
        }

        return colors[node.type] || colors.default || '#888888';
    }

    setupSVG() {
        this.svg = d3.select(this.containerId)
            .attr("width", this.width)
            .attr("height", this.height);

        this.setupGradients(); // Initialize gradients

        // Zoom behavior
        this.zoom = d3.zoom()
            .scaleExtent([this.config.zoom.minScale, this.config.zoom.maxScale])
            .on("zoom", (event) => {
                this.container.attr("transform", event.transform);
                // If in cung grid mode, update node positions to match grid
                if (window.cungGridMode) {
                    this._latestTransform = event.transform;

                    if (!this._zoomUpdateTimer) {
                        this._zoomUpdateTimer = setTimeout(() => {
                            if (this._latestTransform) {
                                this.updateNodesForCungGrid(this._latestTransform);
                            }
                            this._zoomUpdateTimer = null;
                        }, 50);
                    }
                }
            });

        this.svg.call(this.zoom);
        this.container = this.svg.append("g");
    }

    setupArrowMarkers() {
        const linkColors = this.config.colors.links;
        const markers = [
            { id: "sinh", color: linkColors.sinh },
            { id: "khac", color: linkColors.khac },
            { id: "thuoc", color: linkColors.thuoc },
            { id: "vong", color: linkColors.vong },
            { id: "dong_hanh", color: linkColors.dong_hanh }
        ];

        const defs = this.svg.append("defs");

        markers.forEach(m => {
            defs.append("marker")
                .attr("id", `arrow-${m.id}`)
                .attr("viewBox", "0 -5 10 10")
                .attr("refX", 20)
                .attr("refY", 0)
                .attr("markerWidth", 6)
                .attr("markerHeight", 6)
                .attr("orient", "auto")
                .append("path")
                .attr("fill", m.color)
                .attr("d", "M0,-5L10,0L0,5");
        });
    }

    setupSimulation() {
        const simConfig = this.config.simulation;
        const padding = simConfig.collisionPadding;
        const collisionStrength = simConfig.collisionStrength;

        this.simulation = d3.forceSimulation(this.data.nodes)
            .force("link", d3.forceLink(this.data.links).id(d => d.id).distance(simConfig.linkDistance))
            .force("charge", d3.forceManyBody().strength(simConfig.chargeStrength).distanceMax(simConfig.chargeDistanceMax))
            .force("center", d3.forceCenter(this.width / 2, this.height / 2))
            .force("collision", d3.forceCollide().radius(d => d.size + padding).strength(collisionStrength));
    }

    setupGradients() {
        // Setup 3D Sphere Gradients
        const defs = this.svg.append("defs");
        const nguHanhColors = this.config.colors.ngu_hanh;

        // Define gradients for each element
        const elements = [
            { id: 'kim', color: nguHanhColors.Kim || '#FFFFFF' },
            { id: 'moc', color: nguHanhColors.Moc || '#2ecc71' },
            { id: 'thuy', color: nguHanhColors.Thuy || '#00a8ff' },
            { id: 'hoa', color: nguHanhColors.Hoa || '#ff4757' },
            { id: 'tho', color: nguHanhColors.Tho || '#ffa502' }
        ];

        elements.forEach(el => {
            const grad = defs.append("radialGradient")
                .attr("id", `grad-${el.id}`)
                .attr("cx", "30%")
                .attr("cy", "30%")
                .attr("r", "70%")
                .attr("fx", "30%")
                .attr("fy", "30%");

            grad.append("stop").attr("offset", "0%").attr("stop-color", "#ffffff").attr("stop-opacity", 0.8);
            grad.append("stop").attr("offset", "40%").attr("stop-color", el.color).attr("stop-opacity", 1);
            grad.append("stop").attr("offset", "100%").attr("stop-color", d3.color(el.color).darker(1.5)).attr("stop-opacity", 1);
        });
    }

    getFillUrl(node) {
        const idLower = node.id.toLowerCase();
        const map = { 'kim': 'kim', 'mộc': 'moc', 'thủy': 'thuy', 'hỏa': 'hoa', 'thổ': 'tho' };
        if (map[idLower]) return `url(#grad-${map[idLower]})`;
        return this.getNodeColor(node);
    }

    setupFiveElementsSphere() {
        // Find 5 Elements nodes
        const elements = {};
        const map = { 'kim': 'Kim', 'mộc': 'Mộc', 'thủy': 'Thủy', 'hỏa': 'Hỏa', 'thổ': 'Thổ' };

        this.data.nodes.forEach(n => {
            const name = n.id.toLowerCase();
            // Check matches
            for (let k in map) {
                if (name === k || name === map[k].toLowerCase()) {
                    elements[map[k]] = n;
                }
            }
        });

        // Only proceed if we have 'Thổ' (Earth) as center
        if (!elements['Thổ']) return;

        const cx = this.width / 2;
        const cy = this.height / 2;
        const R = Math.min(this.width, this.height) / 4; // Radius for the sphere surface

        // Render Background Sphere (Visible)
        // Check if exists
        let sphereBg = this.container.select(".five-elements-sphere");
        if (sphereBg.empty()) {
            sphereBg = this.container.insert("circle", ":first-child")
                .attr("class", "five-elements-sphere")
                .attr("r", R) // Match Layout Radius so nodes sit on the "surface/tangent"
                .attr("cx", cx)
                .attr("cy", cy)
                .attr("fill", "url(#grad-sphere-bg)")
                .style("pointer-events", "none");

            // Define visible sphere gradient
            const defs = this.svg.select("defs");
            // Remove old if exists to update style (or select and update)
            defs.select("#grad-sphere-bg").remove();

            const grad = defs.append("radialGradient")
                .attr("id", "grad-sphere-bg")
                .attr("cx", "50%").attr("cy", "50%").attr("r", "50%");
            // Increased opacity for "độ rõ"
            grad.append("stop").attr("offset", "0%").attr("stop-color", "#ffffff").attr("stop-opacity", 0.4);
            grad.append("stop").attr("offset", "70%").attr("stop-color", "#e0e0e0").attr("stop-opacity", 0.2);
            grad.append("stop").attr("offset", "100%").attr("stop-color", "#cccccc").attr("stop-opacity", 0.1);
        } else {
            // Update existing if present (e.g. resize)
            sphereBg.attr("r", R).attr("cx", cx).attr("cy", cy);
        }

        // Fix Positions (Layout)
        // Thổ Center
        const tho = elements['Thổ'];
        tho.fx = cx;
        tho.fy = cy;
        tho.isFixedElement = true; // Mark to prevent physics override if needed

        // Others on surface
        // Hỏa (Fire) Top
        if (elements['Hỏa']) {
            elements['Hỏa'].fx = cx;
            elements['Hỏa'].fy = cy - R;
        }
        // Thủy (Water) Bottom
        if (elements['Thủy']) {
            elements['Thủy'].fx = cx;
            elements['Thủy'].fy = cy + R;
        }
        // Kim (Metal) Right
        if (elements['Kim']) {
            elements['Kim'].fx = cx + R;
            elements['Kim'].fy = cy;
        }
        // Mộc (Wood) Left
        if (elements['Mộc']) {
            elements['Mộc'].fx = cx - R;
            elements['Mộc'].fy = cy;
        }
    }

    render() {
        // Links
        this.linkElements = this.container.append("g")
            .selectAll("line")
            .data(this.data.links)
            .enter().append("line")
            .attr("class", d => `link link-${d.relation}`)
            .attr("marker-end", d => `url(#arrow-${d.relation})`);

        // Node groups
        this.nodeElements = this.container.append("g")
            .selectAll("g")
            .data(this.data.nodes)
            .enter().append("g")
            .attr("class", "node")
            .call(d3.drag()
                .on("start", (e, d) => this.dragstarted(e, d))
                .on("drag", (e, d) => this.dragged(e, d))
                .on("end", (e, d) => this.dragended(e, d)));

        // Node circles (3D Spheres)
        this.nodeElements.append("circle")
            .attr("r", d => d.size)
            .attr("fill", d => this.getFillUrl(d))
            .attr("stroke", "#fff")
            .attr("stroke-width", this.config.dimensions.strokeWidth.node)
            .on("mouseover", (e, d) => this.showTooltip(e, d))
            .on("mouseout", () => this.hideTooltip())
            .on("click", (e, d) => this.highlightConnections(d));

        // Nature markers (+ or -)
        this.nodeElements.append("text")
            .attr("class", d => `nature-marker nature-${d.nature}-marker`)
            .attr("x", d => d.size - 8)
            .attr("y", d => -d.size + 12)
            .attr("font-size", "16px")
            .attr("font-weight", "bold")
            .text(d => {
                if (d.nature === 'cat') return '+';
                if (d.nature === 'hung') return '-';
                return '';
            });

        // Node labels
        this.labelElements = this.nodeElements.append("text")
            .attr("class", "node-label")
            .attr("x", 0)
            .attr("y", d => d.size + 14)
            .attr("text-anchor", "middle")
            .text(d => d.id);

        // Simulation tick
        this.simulation.on("tick", () => {
            this.linkElements
                .attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            this.nodeElements.attr("transform", d => `translate(${d.x},${d.y})`);
        });
    }

    dragstarted(event, d) {
        if (!event.active) this.simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    dragended(event, d) {
        if (!event.active) this.simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

    showTooltip(event, d) {
        const tooltip = document.getElementById("tooltip");
        const title = document.getElementById("tooltip-title");
        const content = document.getElementById("tooltip-content");
        const typeLabel = document.getElementById("tooltip-type");

        // Nature badge
        let natureBadge = '';
        if (d.nature === 'cat') {
            natureBadge = '<span class="nature-badge nature-cat">CAT (+)</span>';
        } else if (d.nature === 'hung') {
            natureBadge = '<span class="nature-badge nature-hung">HUNG (-)</span>';
        } else {
            natureBadge = '<span class="nature-badge nature-trung">Trung tinh</span>';
        }

        title.innerHTML = `${d.id} ${natureBadge}`;
        content.textContent = d.desc || '';

        const typeNames = {
            ngu_hanh: 'Ngu Hanh',
            thien_can: 'Thien Can',
            dia_chi: 'Dia Chi',
            chinh_tinh_tuvi: 'Chinh Tinh - Vong Tu Vi',
            chinh_tinh_phu: 'Chinh Tinh - Vong Thien Phu',
            luc_cat: 'Luc Cat Tinh',
            luc_sat: 'Luc Sat Tinh',
            tu_hoa: 'Tu Hoa',
            thai_tue: 'Vong Thai Tue',
            truong_sinh: 'Vong Truong Sinh',
            bac_sy: 'Vong Bac Sy',
            tap_tinh: 'Tap Tinh'
        };

        typeLabel.textContent = typeNames[d.type] || d.type;

        tooltip.style.left = (event.pageX + 15) + "px";
        tooltip.style.top = (event.pageY - 10) + "px";
        tooltip.style.opacity = 1;
    }

    hideTooltip() {
        document.getElementById("tooltip").style.opacity = 0;
    }

    highlightConnections(d) {
        const connectedNodes = new Set([d.id]);

        this.data.links.forEach(l => {
            const sourceId = typeof l.source === 'object' ? l.source.id : l.source;
            const targetId = typeof l.target === 'object' ? l.target.id : l.target;

            if (sourceId === d.id) connectedNodes.add(targetId);
            if (targetId === d.id) connectedNodes.add(sourceId);
        });

        this.nodeElements.select("circle")
            .attr("opacity", n => connectedNodes.has(n.id) ? 1 : 0.15);

        this.linkElements.attr("opacity", l => {
            const sourceId = typeof l.source === 'object' ? l.source.id : l.source;
            const targetId = typeof l.target === 'object' ? l.target.id : l.target;
            return (sourceId === d.id || targetId === d.id) ? 1 : 0.05;
        });

        // Reset after 4 seconds
        setTimeout(() => {
            this.nodeElements.select("circle").attr("opacity", 1);
            this.linkElements.attr("opacity", 0.5);
        }, 4000);
    }

    resetZoom() {
        this.svg.transition().duration(750).call(
            this.zoom.transform,
            d3.zoomIdentity.translate(this.width / 2, this.height / 2).scale(1).translate(-this.width / 2, -this.height / 2)
        );
    }

    updateNodesForCungGrid(transform) {
        // Update node positions to match cung grid when zooming
        if (!window.currentChartData || !window.currentChartData.positions) return;
        if (!window.nodeJitter) return;

        const positions = window.currentChartData.positions;
        const starToCung = {};

        // Build map: Star Name -> Cung Index
        for (let pos = 0; pos < 12; pos++) {
            if (positions[pos] && positions[pos].stars) {
                positions[pos].stars.forEach(star => {
                    const name = typeof star === 'object' ? star.name : star;
                    starToCung[name] = pos;
                });
            }
        }

        // Calculate cell centers geometrically for perfect alignment (Center of 12 Cung Slices)
        const cellCenters = {};
        const svgW = this.width;
        const svgH = this.height;
        const cx = svgW / 2;
        const cy = svgH / 2;
        const R = Math.min(svgW, svgH) / 2;
        // Target Radius: Middle of the 24%-51% ring approx. 
        // 24% to 51% of Diameter => Radius ranges from 0.48*R to 1.02*R? 
        // CSS: transparent 24% (of diameter?? No usually radial-gradient % is of distance from center to corner or side).
        // Let's assume CSS % is relative to "closest-side" or 50% width.
        // If box is 100x100. 50% is edge. 
        // Gradient 24% -> 0.24 * 100 = 24px from center. 
        // Edge is 50px. So 24px is ~50% radius. 
        // Gradient 49% -> 0.49 * 100 = 49px. Edge is 50px.
        // So ring is from 0.48R to 0.98R.
        // Middle is approx 0.73R.

        const targetR = R * 0.82;

        for (let pos = 0; pos < 12; pos++) {
            // With CSS grid-rotation: 180deg, Tý is at 12h (Top), Ngọ at 6h (Bottom)
            // In D3/SVG: 0deg=East/3h, 90deg=South/6h, 180deg=West/9h, 270deg/-90deg=North/12h
            // Tý (pos 0) should be at -90deg (Top). Ngọ (pos 6) at 90deg (Bottom).
            // Formula: angleDeg = -90 + (pos * 30)
            // pos 0 -> -90 (Top). pos 6 -> -90 + 180 = 90 (Bottom). Correct!
            const angleDeg = -90 + (pos * 30);
            const angleRad = angleDeg * Math.PI / 180;

            const targetX = cx + targetR * Math.cos(angleRad);
            const targetY = cy + targetR * Math.sin(angleRad);

            // Convert Screen Coordinates to World Coordinates for D3 Simulation
            const worldX = (targetX - transform.x) / transform.k;
            const worldY = (targetY - transform.y) / transform.k;

            // Available space for packing (approx sector size)
            // Chord length approx width
            const availW = (targetR * 2 * Math.sin(15 * Math.PI / 180)) / transform.k;
            const availH = ((1.0 - 0.5) * R) / transform.k;

            cellCenters[pos] = {
                x: worldX,
                y: worldY,
                w: availW * 0.8,
                h: availH * 0.8
            };
        }

        // Group stars by cung for grid-based positioning
        const starsByCung = {};
        this.data.nodes.forEach(d => {
            if (starToCung.hasOwnProperty(d.id)) {
                const pos = starToCung[d.id];
                if (!starsByCung[pos]) starsByCung[pos] = [];
                starsByCung[pos].push(d);
            }
        });

        // Calculate grid positions for each cung
        Object.keys(starsByCung).forEach(pos => {
            const stars = starsByCung[pos];
            const center = cellCenters[pos];
            if (!center) return;

            const count = stars.length;
            const nodeRadius = 18 / transform.k;
            const padding = 8 / transform.k;
            const minDist = (nodeRadius * 2) + padding;

            const cols = Math.ceil(Math.sqrt(count));
            const rows = Math.ceil(count / cols);

            const availW = center.w * 0.7;
            const availH = center.h * 0.7;

            const spacingX = cols > 1 ? Math.max(minDist, availW / (cols - 1)) : 0;
            const spacingY = rows > 1 ? Math.max(minDist, availH / (rows - 1)) : 0;

            const startX = center.x - (cols - 1) * spacingX / 2;
            const startY = center.y - (rows - 1) * spacingY / 2;

            stars.forEach((d, i) => {
                const col = i % cols;
                const row = Math.floor(i / cols);
                d.fx = startX + col * spacingX;
                d.fy = startY + row * spacingY;
            });
        });

        // Manually update positions
        this.linkElements
            .attr("x1", d => d.source.fx || d.source.x)
            .attr("y1", d => d.source.fy || d.source.y)
            .attr("x2", d => d.target.fx || d.target.x)
            .attr("y2", d => d.target.fy || d.target.y);

        this.nodeElements.attr("transform", d => {
            const x = d.fx !== null && d.fx !== undefined ? d.fx : d.x;
            const y = d.fy !== null && d.fy !== undefined ? d.fy : d.y;
            return `translate(${x},${y})`;
        });
    }

    toggleLabels() {
        this.showLabels = !this.showLabels;
        this.labelElements.attr("opacity", this.showLabels ? 1 : 0);
    }

    filterByType(type) {
        if (type === 'all') {
            if (!this.activeFilters.has('all')) {
                this.activeFilters.clear();
                this.activeFilters.add('all');
            }
        } else {
            if (this.activeFilters.has('all')) {
                this.activeFilters.delete('all');
            }

            if (this.activeFilters.has(type)) {
                this.activeFilters.delete(type);
                if (this.activeFilters.size === 0) {
                    this.activeFilters.add('all');
                }
            } else {
                this.activeFilters.add(type);
            }
        }

        this.updateCheckboxUI();
        this.toggleNodeOpacity();
    }

    updateCheckboxUI() {
        const checkboxes = document.querySelectorAll('#node-type-checkboxes input');
        checkboxes.forEach(cb => {
            cb.checked = this.activeFilters.has(cb.value);
        });

        const textSpan = document.getElementById('multiselect-text');
        if (this.activeFilters.has('all')) {
            textSpan.textContent = "Tất cả Node";
        } else {
            const size = this.activeFilters.size;
            textSpan.textContent = `${size} Loại đã chọn`;
        }
    }

    toggleNodeOpacity() {
        if (this.activeFilters.has('all')) {
            this.nodeElements.attr("opacity", 1);
        } else {
            this.nodeElements.attr("opacity", d => {
                let isVisible = false;
                if (d.type === 'chinh_tinh_tuvi' || d.type === 'chinh_tinh_phu') {
                    isVisible = this.activeFilters.has('chinh_tinh');
                } else {
                    isVisible = this.activeFilters.has(d.type);
                }
                return isVisible ? 1 : 0.1;
            });
        }

        this.applyLinkFilter();
    }

    updateLinkVisibility() {
        const checkboxes = document.querySelectorAll('.link-filters input[type="checkbox"]');
        const checkedTypes = new Set();
        checkboxes.forEach(cb => {
            if (cb.checked) checkedTypes.add(cb.value);
        });

        this.linkElements.attr("opacity", d => {
            return checkedTypes.has(d.relation) ? 0.6 : 0;
        });

        this.currentLinkTypes = checkedTypes;
    }

    applyLinkFilter() {
        this.updateLinkVisibility();
    }

    search(query) {
        if (!query) {
            this.nodeElements.attr("opacity", 1);
            this.linkElements.attr("opacity", 0.5);
            return;
        }

        const lowerQuery = query.toLowerCase();
        const matchedNodes = new Set();

        this.data.nodes.forEach(n => {
            if (n.id.toLowerCase().includes(lowerQuery) ||
                (n.desc && n.desc.toLowerCase().includes(lowerQuery))) {
                matchedNodes.add(n.id);
            }
        });

        this.nodeElements.attr("opacity", d => matchedNodes.has(d.id) ? 1 : 0.15);
        this.linkElements.attr("opacity", 0.1);
    }

    updateStats() {
        let catCount = 0, hungCount = 0;
        this.data.nodes.forEach(n => {
            if (n.nature === 'cat') catCount++;
            else if (n.nature === 'hung') hungCount++;
        });

        const statsDiv = document.getElementById("stats");
        statsDiv.innerHTML = `
            <div>Tong so: <span>${this.data.nodes.length}</span> sao</div>
            <div>Cat tinh (+): <span style="color:#27ae60">${catCount}</span></div>
            <div>Hung tinh (-): <span style="color:#e74c3c">${hungCount}</span></div>
            <div>Quan he: <span>${this.data.links.length}</span></div>
        `;
    }

    setupEventListeners() {
        window.addEventListener('resize', () => {
            this.width = window.innerWidth;
            this.height = window.innerHeight;
            this.svg.attr("width", this.width).attr("height", this.height);
            this.simulation.force("center", d3.forceCenter(this.width / 2, this.height / 2));
            this.simulation.alpha(0.3).restart();
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (event) => {
            const container = document.getElementById('node-filter-container');
            if (container && !container.contains(event.target)) {
                document.getElementById('node-type-checkboxes').classList.remove('expanded');
            }
        });
    }
}

// Export to global scope
window.TuViKnowledgeGraph = TuViKnowledgeGraph;
