/**
 * Tu Vi Knowledge Graph - Star Filter Module
 * Các hàm filter sao: individual star filter, playback filter
 */

// ═══════════════════════════════════════════════════════════════════════════
// STAR TYPES CONFIGURATION
// ═══════════════════════════════════════════════════════════════════════════

// Star types that can be placed in 12 cung (not Ngu Hanh, Thien Can, Dia Chi)
const STAR_TYPES_IN_CUNG = ['chinh_tinh', 'chinh_tinh_tuvi', 'chinh_tinh_phu', 'luc_cat', 'luc_sat', 'tu_hoa', 'tap_tinh'];

// Playback filter - which star types to show (using filter checkbox values)
let playbackStarFilter = new Set(['chinh_tinh', 'luc_cat', 'luc_sat', 'tu_hoa', 'tap_tinh']);

// Individual star filter - set of selected star IDs
// null = all stars shown (default), Set with IDs = only those stars shown
let selectedIndividualStars = null; 
let allStarsList = []; // Will be populated from graph data

// ═══════════════════════════════════════════════════════════════════════════
// HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Check if a node type matches a filter value
 * chinh_tinh filter should match both chinh_tinh_tuvi and chinh_tinh_phu
 */
function matchesFilter(nodeType, filterValue) {
    if (filterValue === 'chinh_tinh') {
        return nodeType === 'chinh_tinh' || nodeType === 'chinh_tinh_tuvi' || nodeType === 'chinh_tinh_phu';
    }
    return nodeType === filterValue;
}

/**
 * Check if a node type is a star type (can be in 12 cung)
 */
function isStarType(nodeType) {
    return STAR_TYPES_IN_CUNG.includes(nodeType);
}

/**
 * Check if a node should be visible based on current filter
 */
function isNodeVisible(nodeType) {
    if (!isStarType(nodeType)) return false;
    
    for (const filterValue of playbackStarFilter) {
        if (matchesFilter(nodeType, filterValue)) {
            return true;
        }
    }
    return false;
}

/**
 * Check if a specific star is visible based on individual filter
 */
function isStarIndividuallyVisible(starId) {
    // If null (all selected), all stars are visible
    if (selectedIndividualStars === null) return true;
    // If empty set, no stars visible
    if (selectedIndividualStars.size === 0) return false;
    // Otherwise check if star is in the set
    return selectedIndividualStars.has(starId);
}

// ═══════════════════════════════════════════════════════════════════════════
// INDIVIDUAL STAR FILTER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Initialize individual star filter with all stars from the graph
 */
function initIndividualStarFilter() {
    if (!window.tuviGraph || !window.tuviGraph.data) return;
    
    allStarsList = window.tuviGraph.data.nodes
        .filter(node => isStarType(node.type))
        .map(node => ({
            id: node.id,
            name: node.id,
            type: node.type
        }))
        .sort((a, b) => a.name.localeCompare(b.name, 'vi'));
    
    // By default, all stars are selected (null means all)
    selectedIndividualStars = null;
    
    populateStarCheckboxList();
    updateSelectedStarsText();
}

/**
 * Populate the star checkbox list in the dropdown
 */
function populateStarCheckboxList() {
    const container = document.getElementById('star-checkbox-list');
    if (!container) return;
    
    container.innerHTML = allStarsList.map(star => {
        const typeClass = getTypeClass(star.type);
        const typeName = getTypeName(star.type);
        // Escape special characters in star ID for onclick
        const escapedId = star.id.replace(/'/g, "\\'");
        return `
            <label data-star-id="${star.id}" data-star-name="${star.name.toLowerCase()}">
                <input type="checkbox" value="${star.id}" checked onchange="toggleIndividualStar('${escapedId}', this.checked)">
                <span>${star.name}</span>
                <span class="star-type-badge ${typeClass}">${typeName}</span>
            </label>
        `;
    }).join('');
}

/**
 * Get CSS class for star type badge
 */
function getTypeClass(type) {
    if (type === 'chinh_tinh_tuvi' || type === 'chinh_tinh_phu') return 'chinh-tinh';
    if (type === 'luc_cat') return 'luc-cat';
    if (type === 'luc_sat') return 'luc-sat';
    if (type === 'tu_hoa') return 'tu-hoa';
    if (type === 'tap_tinh') return 'tap-tinh';
    return '';
}

/**
 * Get display name for star type
 */
function getTypeName(type) {
    if (type === 'chinh_tinh_tuvi' || type === 'chinh_tinh_phu') return 'CT';
    if (type === 'luc_cat') return 'LC';
    if (type === 'luc_sat') return 'LS';
    if (type === 'tu_hoa') return 'TH';
    if (type === 'tap_tinh') return 'TT';
    return '';
}

/**
 * Toggle dropdown visibility
 */
function toggleStarSelectDropdown() {
    const dropdown = document.getElementById('star-select-dropdown');
    if (dropdown) {
        dropdown.classList.toggle('show');
    }
}

/**
 * Toggle individual star selection
 * @param {string} starId - ID của sao
 * @param {boolean} isChecked - Trạng thái checkbox mới
 */
function toggleIndividualStar(starId, isChecked) {
    // If was "all selected" mode (null), switch to explicit selection
    if (selectedIndividualStars === null) {
        selectedIndividualStars = new Set(allStarsList.map(s => s.id));
    }
    
    // Now add or remove based on checkbox state
    if (isChecked) {
        selectedIndividualStars.add(starId);
    } else {
        selectedIndividualStars.delete(starId);
    }
    
    // If all stars are now selected, switch back to "all" mode
    if (selectedIndividualStars.size === allStarsList.length) {
        selectedIndividualStars = null;
    }
    
    updateSelectedStarsText();
    applyPlaybackFilter();
}

/**
 * Select all stars
 */
function selectAllStars() {
    selectedIndividualStars = null; // null = all selected
    document.querySelectorAll('#star-checkbox-list input[type="checkbox"]').forEach(cb => {
        cb.checked = true;
    });
    updateSelectedStarsText();
    applyPlaybackFilter();
}

/**
 * Deselect all stars
 */
function deselectAllStars() {
    selectedIndividualStars = new Set(); // Empty set = none selected
    document.querySelectorAll('#star-checkbox-list input[type="checkbox"]').forEach(cb => {
        cb.checked = false;
    });
    updateSelectedStarsText();
    applyPlaybackFilter();
}

/**
 * Filter star list by search text
 */
function filterStarList() {
    const searchText = document.getElementById('star-search-input').value.toLowerCase();
    document.querySelectorAll('#star-checkbox-list label').forEach(label => {
        const starName = label.getAttribute('data-star-name');
        if (starName.includes(searchText)) {
            label.classList.remove('hidden');
        } else {
            label.classList.add('hidden');
        }
    });
}

/**
 * Update the selected stars text display
 */
function updateSelectedStarsText() {
    const textEl = document.getElementById('selected-stars-text');
    if (!textEl) return;
    
    if (selectedIndividualStars === null) {
        textEl.textContent = 'Tat ca sao';
    } else if (selectedIndividualStars.size === 0) {
        textEl.textContent = 'Khong chon sao nao';
    } else {
        const count = selectedIndividualStars.size;
        const total = allStarsList.length;
        textEl.textContent = `${count}/${total} sao`;
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// PLAYBACK FILTER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Update playback filter from checkboxes
 */
function updatePlaybackFilter() {
    playbackStarFilter.clear();
    document.querySelectorAll('.star-filter-checkboxes input[type="checkbox"]').forEach(cb => {
        if (cb.checked) {
            playbackStarFilter.add(cb.value);
        }
    });
    
    // Update visibility immediately if we have chart data
    if (window.currentChartData && window.tuviGraph) {
        applyPlaybackFilter();
    }
}

/**
 * Apply filter to show/hide nodes based on type AND individual star selection
 */
function applyPlaybackFilter() {
    if (!window.tuviGraph) return;
    
    window.tuviGraph.nodeElements.style("display", d => {
        // If this is a star type, check both filters
        if (isStarType(d.type)) {
            // First check group filter
            const groupVisible = isNodeVisible(d.type);
            // Then check individual star filter
            const individualVisible = isStarIndividuallyVisible(d.id);
            return (groupVisible && individualVisible) ? null : "none";
        }
        // Non-star types (Ngu Hanh, Thien Can, Dia Chi) - always hide in playback mode
        return window.cungGridMode ? "none" : null;
    });
    
    // Also hide links connected to hidden nodes
    window.tuviGraph.linkElements.style("display", d => {
        const sourceType = d.source.type;
        const targetType = d.target.type;
        
        // If in cung grid mode, only show links between visible stars
        if (window.cungGridMode) {
            const sourceGroupVisible = isStarType(sourceType) && isNodeVisible(sourceType);
            const targetGroupVisible = isStarType(targetType) && isNodeVisible(targetType);
            const sourceIndividualVisible = isStarIndividuallyVisible(d.source.id);
            const targetIndividualVisible = isStarIndividuallyVisible(d.target.id);
            return (sourceGroupVisible && targetGroupVisible && sourceIndividualVisible && targetIndividualVisible) ? null : "none";
        }
        return null;
    });
}

// ═══════════════════════════════════════════════════════════════════════════
// CLOSE DROPDOWN WHEN CLICKING OUTSIDE
// ═══════════════════════════════════════════════════════════════════════════

document.addEventListener('click', function(e) {
    const container = document.getElementById('individual-star-select');
    const dropdown = document.getElementById('star-select-dropdown');
    if (container && dropdown && !container.contains(e.target)) {
        dropdown.classList.remove('show');
    }
});

// ═══════════════════════════════════════════════════════════════════════════
// EXPORT TO GLOBAL SCOPE
// ═══════════════════════════════════════════════════════════════════════════

window.STAR_TYPES_IN_CUNG = STAR_TYPES_IN_CUNG;
window.matchesFilter = matchesFilter;
window.isStarType = isStarType;
window.isNodeVisible = isNodeVisible;
window.isStarIndividuallyVisible = isStarIndividuallyVisible;

window.initIndividualStarFilter = initIndividualStarFilter;
window.toggleStarSelectDropdown = toggleStarSelectDropdown;
window.toggleIndividualStar = toggleIndividualStar;
window.selectAllStars = selectAllStars;
window.deselectAllStars = deselectAllStars;
window.filterStarList = filterStarList;

window.updatePlaybackFilter = updatePlaybackFilter;
window.applyPlaybackFilter = applyPlaybackFilter;
