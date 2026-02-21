/**
 * Tu Vi Knowledge Graph - Cung Grid Module
 * Các hàm liên quan đến 12 cung: renderCungGrid, hideCungGrid, updateChartPositions, anSaoVaoCung
 */

// ═══════════════════════════════════════════════════════════════════════════
// GLOBAL STATE FOR CUNG GRID MODE
// ═══════════════════════════════════════════════════════════════════════════

// Global state for cung grid mode
window.cungGridMode = false;
window.currentChartData = null;
window.graphCalendarMode = 'solar';
window.nodeJitter = {};

// Chi names for reference
const CHI_NAMES = ['Ty', 'Suu', 'Dan', 'Mao', 'Thin', 'Ty', 'Ngo', 'Mui', 'Than', 'Dau', 'Tuat', 'Hoi'];

// ═══════════════════════════════════════════════════════════════════════════
// BIRTH FORM FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

function toggleBirthFormPanel() {
    const panel = document.getElementById('birth-form-panel');
    panel.classList.toggle('expanded');
}

function setGraphCalendarMode(mode) {
    window.graphCalendarMode = mode;
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

// ═══════════════════════════════════════════════════════════════════════════
// AN SAO VÀO CUNG - MAIN API CALL
// ═══════════════════════════════════════════════════════════════════════════

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
                calendar: window.graphCalendarMode,
                leap_month: leapMonth
            })
        });

        const result = await response.json();

        if (result.status === 'success') {
            window.currentChartData = result.data;
            renderCungGrid(result.data);
        } else {
            console.error('API Error:', result.message);
            alert('Loi: ' + result.message);
        }
    } catch (error) {
        console.error('Fetch Error:', error);
        alert('Loi ket noi: ' + error.message);
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// RENDER CUNG GRID
// ═══════════════════════════════════════════════════════════════════════════

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
        const content = cell.querySelector('.cung-cell-content');
        const label = cell.querySelector('.cung-cell-label');

        // Clear previous classes
        if (label) {
            label.classList.remove('is-menh', 'is-than');
        }

        // Update cung name
        const cungName = cungMap[pos] || '';
        const cungNameEl = label ? label.querySelector('.cung-name') : cell.querySelector('.cung-name');
        if (cungNameEl) cungNameEl.textContent = cungName;

        // Update Ngũ hành
        const nguHanh = posData?.ngu_hanh || '';
        const nguHanhElement = label ? label.querySelector('.cung-ngu-hanh') : cell.querySelector('.cung-ngu-hanh');
        if (nguHanhElement) {
            nguHanhElement.textContent = nguHanh ? `(${nguHanh})` : '';
        }

        // Mark Menh/Than on the label
        if (label) {
            if (pos === menhPos) label.classList.add('is-menh');
            if (pos === thanPos) label.classList.add('is-than');
        }

        // Clear stars container
        const starsContainer = content ? content.querySelector('.cung-stars') : cell.querySelector('.cung-stars');
        if (starsContainer) starsContainer.innerHTML = '';
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
    window.cungGridMode = true;
    window.currentChartData = chartData;

    // --- D3 FORCE MANIPULATION ---
    if (window.tuviGraph) {
        // 1. Reset Zoom
        window.tuviGraph.svg.call(
            window.tuviGraph.zoom.transform,
            d3.zoomIdentity
        );

        // 2. Build Map: Star Name -> Cung Index (with normalization)
        const starToCung = {};
        for (let pos = 0; pos < 12; pos++) {
            if (positions[pos] && positions[pos].stars) {
                positions[pos].stars.forEach(star => {
                    const rawName = typeof star === 'object' ? star.name : star;
                    const normalizedName = window.normalizeStarName(rawName);
                    starToCung[normalizedName] = pos;
                    starToCung[rawName] = pos;
                });
            }
        }

        // 3. Get SVG element position
        const svgNode = window.tuviGraph.svg.node();
        const svgRect = svgNode.getBoundingClientRect();

        // 4. Get Cell Centers
        const cellCenters = {};
        document.querySelectorAll('.cung-cell').forEach(cell => {
            const pos = parseInt(cell.dataset.position);
            const content = cell.querySelector('.cung-cell-content');
            const rect = content ? content.getBoundingClientRect() : cell.getBoundingClientRect();
            
            cellCenters[pos] = {
                x: (rect.left - svgRect.left) + rect.width / 2,
                y: (rect.top - svgRect.top) + rect.height / 2,
                w: rect.width,
                h: rect.height
            };
        });

        // 5. Group stars by cung for grid-based positioning
        const starsByCung = {};
        window.tuviGraph.data.nodes.forEach(d => {
            if (starToCung.hasOwnProperty(d.id)) {
                const pos = starToCung[d.id];
                if (!starsByCung[pos]) starsByCung[pos] = [];
                starsByCung[pos].push(d);
            }
        });
        
        // 6. Calculate grid positions for each cung
        Object.keys(starsByCung).forEach(pos => {
            const stars = starsByCung[pos];
            const center = cellCenters[pos];
            if (!center) return;
            
            const count = stars.length;
            const nodeRadius = 18;
            const padding = 8;
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
        
        // Handle stars not in current chart
        window.tuviGraph.data.nodes.forEach(d => {
            if (!starToCung.hasOwnProperty(d.id)) {
                d.fx = -500;
                d.fy = -500;
            }
        });

        // 7. Stop simulation
        window.tuviGraph.simulation.stop();
        
        // 8. Manually update positions
        window.tuviGraph.linkElements
            .attr("x1", d => d.source.fx || d.source.x)
            .attr("y1", d => d.source.fy || d.source.y)
            .attr("x2", d => d.target.fx || d.target.x)
            .attr("y2", d => d.target.fy || d.target.y);

        window.tuviGraph.nodeElements.attr("transform", d => {
            const x = d.fx !== null && d.fx !== undefined ? d.fx : d.x;
            const y = d.fy !== null && d.fy !== undefined ? d.fy : d.y;
            return `translate(${x},${y})`;
        });
        
        // 9. Apply playback filter
        if (window.applyPlaybackFilter) {
            window.applyPlaybackFilter();
        }
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// HIDE CUNG GRID
// ═══════════════════════════════════════════════════════════════════════════

function hideCungGrid() {
    document.getElementById('cung-grid-container').style.display = 'none';
    window.cungGridMode = false;

    // Release nodes
    if (window.tuviGraph) {
        window.tuviGraph.data.nodes.forEach(d => {
            d.fx = null;
            d.fy = null;
        });
        
        // Show all nodes again
        window.tuviGraph.nodeElements.style("display", null);
        window.tuviGraph.linkElements.style("display", null);
        
        window.tuviGraph.simulation.alpha(0.3).restart();
        window.tuviGraph.resetZoom();
    }
    
    // Clear jitter cache
    window.nodeJitter = {};
}

// ═══════════════════════════════════════════════════════════════════════════
// UPDATE CHART POSITIONS (FOR PLAYBACK)
// ═══════════════════════════════════════════════════════════════════════════

function updateChartPositions(chartData) {
    if (!window.tuviGraph) return;
    
    const positions = chartData.positions;
    const cungMap = chartData.cung_map;
    const menhPos = chartData.menh_position;
    const thanPos = chartData.than_position;

    // Update grid cells
    document.querySelectorAll('.cung-cell').forEach(cell => {
        const pos = parseInt(cell.dataset.position);
        const posData = positions[pos];
        const label = cell.querySelector('.cung-cell-label');

        if (label) {
            label.classList.remove('is-menh', 'is-than');
        }

        const cungName = cungMap[pos] || '';
        const cungNameEl = label ? label.querySelector('.cung-name') : cell.querySelector('.cung-name');
        if (cungNameEl) cungNameEl.textContent = cungName;

        const nguHanh = posData?.ngu_hanh || '';
        const nguHanhElement = label ? label.querySelector('.cung-ngu-hanh') : cell.querySelector('.cung-ngu-hanh');
        if (nguHanhElement) {
            nguHanhElement.textContent = nguHanh ? `(${nguHanh})` : '';
        }

        if (label) {
            if (pos === menhPos) label.classList.add('is-menh');
            if (pos === thanPos) label.classList.add('is-than');
        }
    });

    // Update center info
    const centerContent = document.getElementById('chart-summary');
    if (centerContent) {
        centerContent.innerHTML = `
            <div class="info-row"><span class="info-label">Cuc: </span><span class="info-value">${chartData.cuc?.name || '?'}</span></div>
            <div class="info-row"><span class="info-label">Nap Am: </span><span class="info-value">${chartData.nap_am?.element || '?'}</span></div>
            <div class="info-row"><span class="info-label">Menh: </span><span class="info-value">${chartData.menh_name || '?'}</span></div>
            <div class="info-row"><span class="info-label">Than: </span><span class="info-value">${chartData.than_name || '?'}</span></div>
        `;
    }

    // Reset zoom
    window.tuviGraph.svg.call(
        window.tuviGraph.zoom.transform,
        d3.zoomIdentity
    );

    // Build star to cung mapping
    const starToCung = {};
    for (let pos = 0; pos < 12; pos++) {
        if (positions[pos] && positions[pos].stars) {
            positions[pos].stars.forEach(star => {
                const rawName = typeof star === 'object' ? star.name : star;
                const normalizedName = window.normalizeStarName(rawName);
                starToCung[normalizedName] = pos;
                starToCung[rawName] = pos;
            });
        }
    }

    // Get SVG coordinates
    const svgNode = window.tuviGraph.svg.node();
    const svgRect = svgNode.getBoundingClientRect();

    // Get cell centers
    const cellCenters = {};
    document.querySelectorAll('.cung-cell').forEach(cell => {
        const pos = parseInt(cell.dataset.position);
        const content = cell.querySelector('.cung-cell-content');
        const rect = content ? content.getBoundingClientRect() : cell.getBoundingClientRect();
        cellCenters[pos] = {
            x: (rect.left - svgRect.left) + rect.width / 2,
            y: (rect.top - svgRect.top) + rect.height / 2,
            w: rect.width,
            h: rect.height
        };
    });

    // Stop simulation
    window.tuviGraph.simulation.stop();

    // Group stars by cung
    const starsByCung = {};
    window.tuviGraph.data.nodes.forEach(d => {
        if (starToCung.hasOwnProperty(d.id)) {
            const pos = starToCung[d.id];
            if (!starsByCung[pos]) starsByCung[pos] = [];
            starsByCung[pos].push(d);
        }
    });
    
    // Calculate grid positions
    Object.keys(starsByCung).forEach(pos => {
        const stars = starsByCung[pos];
        const center = cellCenters[pos];
        if (!center) return;
        
        const count = stars.length;
        const nodeRadius = 18;
        const padding = 8;
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
            d.x = d.fx;
            d.y = d.fy;
        });
    });
    
    // Handle stars not in chart
    window.tuviGraph.data.nodes.forEach(d => {
        if (!starToCung.hasOwnProperty(d.id)) {
            d.fx = -500;
            d.fy = -500;
            d.x = -500;
            d.y = -500;
        }
    });

    // Animate transition
    window.tuviGraph.nodeElements
        .transition()
        .duration(300)
        .attr("transform", d => `translate(${d.fx},${d.fy})`);

    window.tuviGraph.linkElements
        .transition()
        .duration(300)
        .attr("x1", d => d.source.fx || d.source.x)
        .attr("y1", d => d.source.fy || d.source.y)
        .attr("x2", d => d.target.fx || d.target.x)
        .attr("y2", d => d.target.fy || d.target.y);
    
    // Apply filter
    if (window.applyPlaybackFilter) {
        window.applyPlaybackFilter();
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// EXPORT TO GLOBAL SCOPE
// ═══════════════════════════════════════════════════════════════════════════

window.CHI_NAMES = CHI_NAMES;
window.toggleBirthFormPanel = toggleBirthFormPanel;
window.setGraphCalendarMode = setGraphCalendarMode;
window.anSaoVaoCung = anSaoVaoCung;
window.renderCungGrid = renderCungGrid;
window.hideCungGrid = hideCungGrid;
window.updateChartPositions = updateChartPositions;
