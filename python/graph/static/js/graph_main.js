/**
 * Tu Vi Knowledge Graph - Main Entry Point
 * initGraph và event handlers - file này phải load cuối cùng
 */

// ═══════════════════════════════════════════════════════════════════════════
// GLOBAL INSTANCE
// ═══════════════════════════════════════════════════════════════════════════

window.tuviGraph = null;

// ═══════════════════════════════════════════════════════════════════════════
// INITIALIZATION
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Initialize the Knowledge Graph
 */
function initGraph() {
    console.log("Initializing Tu Vi Graph...");
    window.tuviGraph = new window.TuViKnowledgeGraph('#graph');
    console.log("Graph initialized:", window.tuviGraph);

    // Initialize individual star filter after graph is ready
    setTimeout(() => {
        if (window.initIndividualStarFilter) {
            window.initIndividualStarFilter();
        }
    }, 100);
}

// ═══════════════════════════════════════════════════════════════════════════
// GLOBAL WRAPPER FUNCTIONS (for HTML onclick handlers)
// ═══════════════════════════════════════════════════════════════════════════

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

/**
 * Update chart positions for playback
 * Called from playback.js
 */
function updateChartPositions(chartData) {
    if (!window.tuviGraph) return;

    // Ensure we are in grid mode
    if (!window.cungGridMode) {
        document.getElementById('cung-grid-container').style.display = 'block';
        window.cungGridMode = true;
    }

    // Get current transform to maintain zoom/pan state
    // If _latestTransform is not available, default to identity
    const transform = window.tuviGraph._latestTransform || d3.zoomIdentity;

    // Update Cung Labels (Mệnh, Phụ Mẫu, Tài Bạch...) and Highlights
    // based on the new chartData
    if (chartData && chartData.cung_map) {
        document.querySelectorAll('.cung-cell').forEach(cell => {
            const pos = parseInt(cell.dataset.position);
            const cungName = chartData.cung_map[pos] || '';
            const cellLabel = cell.querySelector('.cung-cell-label');
            const cellContent = cell.querySelector('.cung-cell-content');

            if (cellLabel) {
                // Update Name
                const nameSpan = cellLabel.querySelector('.cung-name');
                if (nameSpan) nameSpan.textContent = cungName;

                // Update Badge/Highlight Classes
                // First remove old ones
                cellLabel.classList.remove('is-menh', 'is-than', 'is-tai');
                if (cellContent) cellContent.classList.remove('is-menh', 'is-than', 'is-tai');

                // Add new ones
                if (cungName.includes('Mệnh')) {
                    cellLabel.classList.add('is-menh');
                    if (cellContent) cellContent.classList.add('is-menh');
                } else if (cungName.includes('Thân')) {
                    cellLabel.classList.add('is-than');
                    if (cellContent) cellContent.classList.add('is-than');
                } else if (cungName.includes('Tài')) { // Check for Tài Bạch
                    cellLabel.classList.add('is-tai');
                    if (cellContent) cellContent.classList.add('is-tai');
                }
            }
        });
    }

    // Update node positions
    // Note: graph_core.js reads from window.currentChartData which is already updated by playback.js
    window.tuviGraph.updateNodesForCungGrid(transform);

    // Restart simulation with low alpha to settle into new positions immediately
    if (window.tuviGraph.simulation) {
        window.tuviGraph.simulation.alpha(0.1).restart();
    }
}
window.updateChartPositions = updateChartPositions;

// ═══════════════════════════════════════════════════════════════════════════
// DOM READY EVENT LISTENER
// ═══════════════════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
    initGraph();

    // Setup speed slider listener
    const speedSlider = document.getElementById('play-speed');
    if (speedSlider) {
        speedSlider.addEventListener('input', window.onSpeedChange);
    }
});

// ═══════════════════════════════════════════════════════════════════════════
// EXPORT TO GLOBAL SCOPE
// ═══════════════════════════════════════════════════════════════════════════

window.initGraph = initGraph;
window.resetZoom = resetZoom;
window.toggleLabels = toggleLabels;
window.filterByType = filterByType;
window.updateLinkVisibility = updateLinkVisibility;
window.toggleCheckboxArea = toggleCheckboxArea;
window.searchNodes = searchNodes;
