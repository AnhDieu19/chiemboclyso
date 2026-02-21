/**
 * Tu Vi Knowledge Graph - D3.js Visualization
 */

class TuViKnowledgeGraph {
    constructor(containerId = '#graph') {
        this.containerId = containerId;
        this.width = window.innerWidth;
        this.height = window.innerHeight;
        this.height = window.innerHeight;
        this.data = TUVI_GRAPH_DATA;
        this.config = window.TuViGraphConfig; // Use global config
        this.showLabels = true;
        this.config = window.TuViGraphConfig; // Use global config
        this.showLabels = true;
        this.activeFilters = new Set(['all']);

        this.init();
    }

    init() {
        this.setupSVG();
        this.setupArrowMarkers();
        this.setupSimulation();
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

        // Zoom behavior
        this.zoom = d3.zoom()
            .scaleExtent([this.config.zoom.minScale, this.config.zoom.maxScale])
            .on("zoom", (event) => {
                this.container.attr("transform", event.transform);
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
        const nodeRadius = this.config.dimensions.nodeRadius.default;
        const collisionStrength = simConfig.collisionStrength;
        const padding = simConfig.collisionPadding;

        this.simulation = d3.forceSimulation(this.data.nodes)
            .force("link", d3.forceLink(this.data.links).id(d => d.id).distance(simConfig.linkDistance))
            .force("charge", d3.forceManyBody().strength(simConfig.chargeStrength).distanceMax(simConfig.chargeDistanceMax))
            .force("center", d3.forceCenter(this.width / 2, this.height / 2))
            .force("collision", d3.forceCollide().radius(d => d.size + padding).strength(collisionStrength));
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

        // Node circles
        this.nodeElements.append("circle")
            .attr("r", d => d.size)
            .attr("fill", d => this.getNodeColor(d))
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

    toggleLabels() {
        this.showLabels = !this.showLabels;
        this.labelElements.attr("opacity", this.showLabels ? 1 : 0);
    }

    filterByType(type) {
        // Handle "all" selection
        if (type === 'all') {
            if (this.activeFilters.has('all')) {
                // Already selected 'all', ensure everything else is unchecked?
                // Usually if clicking 'all', we want to reset.
                // But checkboxes logic: if 'all' is checked, uncheck others.
            } else {
                // Selecting 'all'
                this.activeFilters.clear();
                this.activeFilters.add('all');
            }
        } else {
            // Specific type selected
            if (this.activeFilters.has('all')) {
                this.activeFilters.delete('all');
            }

            if (this.activeFilters.has(type)) {
                this.activeFilters.delete(type);
                // If nothing left, re-select 'all' or leave empty?
                if (this.activeFilters.size === 0) {
                    this.activeFilters.add('all');
                }
            } else {
                this.activeFilters.add(type);
            }
        }

        // Sync UI Checkboxes
        this.updateCheckboxUI();

        // Apply visual opacity
        this.toggleNodeOpacity();
    }

    updateCheckboxUI() {
        const checkboxes = document.querySelectorAll('#node-type-checkboxes input');
        checkboxes.forEach(cb => {
            cb.checked = this.activeFilters.has(cb.value);
        });

        // Update Text
        const textSpan = document.getElementById('multiselect-text');
        if (this.activeFilters.has('all')) {
            textSpan.textContent = "Tất cả Node";
        } else {
            const size = this.activeFilters.size;
            textSpan.textContent = `${size} Loại đã chọn`;
        }
    }

    toggleNodeOpacity() {
        // If 'all' is active, show everything (opacity 1)
        if (this.activeFilters.has('all')) {
            this.nodeElements.attr("opacity", 1);
        } else {
            this.nodeElements.attr("opacity", d => {
                // Check if node matches ANY of the active filters
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
        // Get all checked values
        const checkboxes = document.querySelectorAll('.link-filters input[type="checkbox"]');
        const checkedTypes = new Set();
        checkboxes.forEach(cb => {
            if (cb.checked) checkedTypes.add(cb.value);
        });

        this.linkElements.attr("opacity", d => {
            // Also consider node filter? For now, if node hidden, link hidden is handled by highlight/node logic
            // But fundamentally, Hide link if its type is not checked.
            return checkedTypes.has(d.relation) ? 0.6 : 0;
        });

        this.currentLinkTypes = checkedTypes;
    }



    applyLinkFilter() {
        // Re-apply whatever is checked
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
        // Update stats


        // Count by nature
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

// Global instance attached to window for safety
window.tuviGraph = null;

function initGraph() {
    console.log("Initializing Tu Vi Graph...");
    window.tuviGraph = new TuViKnowledgeGraph('#graph');
    console.log("Graph initialized:", window.tuviGraph);
}

function resetZoom() {
    if (window.tuviGraph) window.tuviGraph.resetZoom();
}

function toggleLabels() {
    if (window.tuviGraph) window.tuviGraph.toggleLabels();
}

function filterByType(type) {
    if (window.tuviGraph) window.tuviGraph.filterByType(type);
}

function updateLinkVisibility() {
    if (window.tuviGraph) window.tuviGraph.updateLinkVisibility();
}

function toggleCheckboxArea() {
    const checkboxes = document.getElementById('node-type-checkboxes');
    checkboxes.classList.toggle('expanded');
}

function searchNodes() {
    const query = document.getElementById('search-box').value;
    if (window.tuviGraph) window.tuviGraph.search(query);
}

// ═══════════════════════════════════════════════════════════════════════════
// 12 CUNG LAYER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

// Global state for cung grid mode
let cungGridMode = false;
let currentChartData = null;
let graphCalendarMode = 'solar';

// Chi names for reference
const CHI_NAMES = ['Ty', 'Suu', 'Dan', 'Mao', 'Thin', 'Ty', 'Ngo', 'Mui', 'Than', 'Dau', 'Tuat', 'Hoi'];

function toggleBirthFormPanel() {
    const panel = document.getElementById('birth-form-panel');
    panel.classList.toggle('expanded');
}

function setGraphCalendarMode(mode) {
    graphCalendarMode = mode;
    const btnSolar = document.getElementById('btnSolarGraph');
    const btnLunar = document.getElementById('btnLunarGraph');
    const leapRow = document.getElementById('graph-leap-month-row');

    if (mode === 'solar') {
        btnSolar.classList.add('active');
        btnLunar.classList.remove('active');
        leapRow.style.display = 'none';
    } else {
        btnSolar.classList.remove('active');
        btnLunar.classList.add('active');
        leapRow.style.display = 'block';
    }
}

async function anSaoVaoCung() {
    // Get form values
    const day = document.getElementById('graph-day').value;
    const month = document.getElementById('graph-month').value;
    const year = document.getElementById('graph-year').value;
    const hour = document.getElementById('graph-hour').value;
    const gender = document.getElementById('graph-gender').value;
    const leapMonth = document.getElementById('graph-leap-month').checked;

    try {
        // Call API to calculate chart
        const response = await fetch('/graph/api/chart', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                day: parseInt(day),
                month: parseInt(month),
                year: parseInt(year),
                hour: parseInt(hour),
                gender: gender,
                calendar: graphCalendarMode,
                leap_month: leapMonth
            })
        });

        const result = await response.json();

        if (result.status === 'success') {
            currentChartData = result.data;
            renderCungGrid(result.data);

            // Enable filter for 12 Cung if not already
            if (window.tuviGraph && !window.tuviGraph.activeFilters.has('muoi_hai_cung')) {
                window.tuviGraph.filterByType('muoi_hai_cung');
            }
        } else {
            console.error('API Error:', result.message);
            alert('Loi: ' + result.message);
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        alert('Loi ket noi: ' + error.message);
    }
}

function renderCungGrid(chartData) {
    const container = document.getElementById('cung-grid-container');
    const positions = chartData.positions;
    const cungMap = chartData.cung_map;
    const menhPos = chartData.menh_position;
    const thanPos = chartData.than_position;

    // Update each cell
    document.querySelectorAll('.cung-cell').forEach(cell => {
        const pos = parseInt(cell.dataset.position);
        const posData = positions[pos];

        // Clear previous
        cell.classList.remove('is-menh', 'is-than');

        // Update cung name
        const cungName = cungMap[pos] || '';
        cell.querySelector('.cung-name').textContent = cungName;

        // Mark Menh/Than
        if (pos === menhPos) cell.classList.add('is-menh');
        if (pos === thanPos) cell.classList.add('is-than');

        // Render stars
        const starsContainer = cell.querySelector('.cung-stars');
        starsContainer.innerHTML = '';

        if (posData && posData.stars) {
            // Stars are now rendered as D3 nodes
        }
    });

    // Update center info
    const centerContent = document.getElementById('chart-summary');
    centerContent.innerHTML = `
        <div class="info-row"><span class="info-label">Cuc: </span><span class="info-value">${chartData.cuc?.name || '?'}</span></div>
        <div class="info-row"><span class="info-label">Nap Am: </span><span class="info-value">${chartData.nap_am?.element || '?'}</span></div>
        <div class="info-row"><span class="info-label">Menh: </span><span class="info-value">${chartData.menh_name || '?'}</span></div>
        <div class="info-row"><span class="info-label">Than: </span><span class="info-value">${chartData.than_name || '?'}</span></div>
    `;

    // Show the grid
    container.style.display = 'block';
    cungGridMode = true;

    // --- D3 FORCE MANIPULATION ---
    if (window.tuviGraph) {
        // 1. Reset Zoom so screen coords match SVG coords
        // use .call immediately to avoid async transition issues during calculation
        window.tuviGraph.svg.call(
            window.tuviGraph.zoom.transform,
            d3.zoomIdentity
        );

        // 2. Build Map: Star Name -> Cung Index
        const starToCung = {};
        for (let pos = 0; pos < 12; pos++) {
            if (positions[pos] && positions[pos].stars) {
                positions[pos].stars.forEach(star => {
                    const name = typeof star === 'object' ? star.name : star;
                    starToCung[name] = pos;
                });
            }
        }

        // 3. Get Cell Centers (Screen Coords)
        const cellCenters = {};
        document.querySelectorAll('.cung-cell').forEach(cell => {
            const pos = parseInt(cell.dataset.position);
            const rect = cell.getBoundingClientRect();
            cellCenters[pos] = {
                x: rect.left + rect.width / 2,
                y: rect.top + rect.height / 2,
                w: rect.width,
                h: rect.height
            };
        });

        // 4. Update Nodes
        window.tuviGraph.data.nodes.forEach(d => {
            // Normalizing name logic? 
            // Graph Data usually has precise names.
            // If d.id in map, move it.
            if (starToCung.hasOwnProperty(d.id)) {
                const pos = starToCung[d.id];
                const center = cellCenters[pos];

                // Apply Jitter to avoid stacking perfectly
                // Box-Muller or just uniform
                const jitterX = (Math.random() - 0.5) * (center.w * 0.6); // Keep within 60% of cell width
                const jitterY = (Math.random() - 0.5) * (center.h * 0.6);

                d.fx = center.x + jitterX;
                d.fy = center.y + jitterY;
            } else {
                // Node not in chart (e.g. aux stars not calculated or mismatches)
                // Let them float? Or hide them?
                // For clarity, maybe push them away or let them float around.
                // We'll leave them to float (fx=null) 
                // But they might obstruct view. 
                // Let's set opacity low?
                // That requires updating `toggleNodeOpacity`.
            }
        });

        // 5. Restart Simulation
        window.tuviGraph.simulation.alpha(1).restart();
    }
}


function hideCungGrid() {
    document.getElementById('cung-grid-container').style.display = 'none';
    cungGridMode = false;

    // Release nodes
    if (window.tuviGraph) {
        window.tuviGraph.data.nodes.forEach(d => {
            d.fx = null;
            d.fy = null;
        });
        window.tuviGraph.simulation.alpha(0.3).restart();
        window.tuviGraph.resetZoom();
    }
}

// Override filterByType to handle 12 Cung mode switching
const originalFilterByType = TuViKnowledgeGraph.prototype.filterByType;
TuViKnowledgeGraph.prototype.filterByType = function (type) {
    originalFilterByType.call(this, type);

    // Check if 12 Cung is selected
    if (this.activeFilters.has('muoi_hai_cung') && currentChartData) {
        // Show grid if we have chart data
        document.getElementById('cung-grid-container').style.display = 'block';
        document.getElementById('graph').style.opacity = '1';
    } else if (!this.activeFilters.has('muoi_hai_cung')) {
        // Hide grid when 12 Cung is not selected
        hideCungGrid();
    }
};

// Initialize when DOM ready
document.addEventListener('DOMContentLoaded', initGraph);
