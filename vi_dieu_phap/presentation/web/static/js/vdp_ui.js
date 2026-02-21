// Module: VDP.UI
// Responsibility: Filter Logic, Tooltips, Search, Detail Panel, Color Modes

window.VDP = window.VDP || {};

VDP.UI = (function () {
    let tooltip;
    let searchTimeout;

    function init() {
        tooltip = d3.select("#tooltip");
        initSearch();
    }

    // --- SEARCH ---
    function initSearch() {
        const input = document.getElementById('search-input');
        if (!input) return;

        input.addEventListener('input', function () {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                const q = input.value.trim();
                const count = VDP.Core.highlightSearch(q);
                const countEl = document.getElementById('search-count');
                if (countEl) {
                    countEl.innerText = q.length >= 2 ? `${count} found` : '';
                }
            }, 200);
        });

        input.addEventListener('keydown', function (e) {
            if (e.key === 'Escape') {
                input.value = '';
                VDP.Core.resetHighlight();
                const countEl = document.getElementById('search-count');
                if (countEl) countEl.innerText = '';
            }
        });
    }

    // --- TOOLTIPS ---
    function handleMouseOver(event, d) {
        let content = `<div class="tooltip-title">${d.name}</div>`;
        if (d.name_pali) content += `<div class="tooltip-pali">${d.name_pali}</div>`;
        content += `<div>Type: ${d.type} | Group: ${d.group || '-'}</div>`;
        if (d.plane) content += `<div>Plane: ${d.plane}</div>`;
        if (d.vedana) {
            content += `<div><span style="color: ${d.vedana_color || '#FFD700'}">● ${d.vedana}</span></div>`;
        }
        if (d.description) content += `<div style="margin-top:4px;color:#aaa;font-size:11px;">${d.description}</div>`;

        tooltip.style("display", "block")
            .html(content)
            .style("left", (event.pageX + 12) + "px")
            .style("top", (event.pageY + 12) + "px");
    }

    function handleMouseOut() {
        tooltip.style("display", "none");
    }

    // --- DETAIL PANEL ---
    function showDetail(d) {
        const panel = document.getElementById('detail-panel');
        if (!panel) return;

        // Count connections
        const allLinks = VDP.Core.getAllLinks();
        const connections = allLinks.filter(l => {
            const sid = typeof l.source === 'object' ? l.source.id : l.source;
            const tid = typeof l.target === 'object' ? l.target.id : l.target;
            return sid === d.id || tid === d.id;
        });

        const structCount = connections.filter(l => l.type === 'structure').length;
        const assocCount = connections.filter(l => l.type === 'association').length;
        const rootCount = connections.filter(l => l.type === 'root_cause').length;

        let html = `<span class="close-btn" onclick="VDP.UI.hideDetail()">&times;</span>`;
        html += `<h3>${d.name}</h3>`;
        if (d.name_pali) html += `<div class="detail-row"><span class="detail-label">Pali</span><br><span class="detail-value">${d.name_pali}</span></div>`;
        html += `<div class="detail-row"><span class="detail-label">Type</span><br><span class="detail-value">${d.type}</span></div>`;
        html += `<div class="detail-row"><span class="detail-label">Group</span><br><span class="detail-value">${d.group || '-'}</span></div>`;
        if (d.plane) html += `<div class="detail-row"><span class="detail-label">Plane</span><br><span class="detail-value">${d.plane}</span></div>`;
        if (d.vedana) html += `<div class="detail-row"><span class="detail-label">Vedana</span><br><span class="detail-value" style="color:${d.vedana_color || '#FFD700'}">${d.vedana}</span></div>`;
        if (d.description) html += `<div class="detail-row"><span class="detail-label">Description</span><br><span class="detail-value">${d.description}</span></div>`;

        html += `<div class="detail-row" style="margin-top:8px;">`;
        html += `<span class="detail-label">Connections</span><br>`;
        html += `<span class="detail-value">Structure: ${structCount} | Assoc: ${assocCount} | Root: ${rootCount}</span>`;
        html += `</div>`;

        panel.innerHTML = html;
        panel.classList.add('visible');
    }

    function hideDetail() {
        const panel = document.getElementById('detail-panel');
        if (panel) panel.classList.remove('visible');
    }

    // --- MAIN FILTER LOGIC ---
    function renderDynamicFilters(nodes, activePage) {
        const container = document.getElementById('filter-panel');
        if (!container) return;
        container.innerHTML = '<h3 style="margin-top:0; border-bottom:1px solid #555; padding-bottom:5px; font-size:15px;">Filters</h3>';

        // 1. Link Filters
        const linkContainer = document.createElement('div');
        linkContainer.className = 'filter-section';
        linkContainer.innerHTML = '<strong>Links</strong>';
        container.appendChild(linkContainer);

        const linkTypes = [
            { id: 'structure', label: 'Structure', default: activePage === 'structure' },
            { id: 'association', label: 'Association', default: activePage === 'association' },
            { id: 'root_cause', label: 'Root Cause', default: activePage === 'root_cause' }
        ];

        linkTypes.forEach(l => {
            createCheckbox(linkContainer, `link-${l.id}`, l.label, l.default, 'link-filter');
        });

        // 2. Node Filters (Dynamic Groups)
        const nodeContainer = document.createElement('div');
        nodeContainer.className = 'filter-section';
        nodeContainer.style.marginTop = '12px';
        nodeContainer.innerHTML = '<strong>Nodes (Groups)</strong>';
        container.appendChild(nodeContainer);

        // Select All / Deselect All buttons
        const btnRow = document.createElement('div');
        btnRow.style.cssText = 'margin:4px 0 8px;display:flex;gap:6px;';
        const btnAll = document.createElement('button');
        btnAll.innerText = 'All';
        btnAll.style.cssText = 'padding:2px 8px;font-size:11px;cursor:pointer;background:#333;color:#e0e0e0;border:1px solid #555;border-radius:3px;';
        btnAll.onclick = () => { document.querySelectorAll('.node-filter').forEach(c => c.checked = true); updateFilters(); };
        const btnNone = document.createElement('button');
        btnNone.innerText = 'None';
        btnNone.style.cssText = btnAll.style.cssText;
        btnNone.onclick = () => { document.querySelectorAll('.node-filter').forEach(c => c.checked = false); updateFilters(); };
        btnRow.appendChild(btnAll);
        btnRow.appendChild(btnNone);
        nodeContainer.appendChild(btnRow);

        const groupsByType = {};
        nodes.forEach(n => {
            const t = n.type || 'other';
            const g = n.group || 'Other';
            if (!groupsByType[t]) groupsByType[t] = new Set();
            groupsByType[t].add(g);
        });

        const typeOrder = ['root', 'structure', 'category', 'sub_category', 'citta', 'cetasika', 'rupa', 'nibbana', 'hetu', 'other'];

        typeOrder.forEach(type => {
            if (groupsByType[type]) {
                const grps = Array.from(groupsByType[type]).sort();
                if (grps.length === 0) return;

                const displayTitle = type.charAt(0).toUpperCase() + type.slice(1);
                const catHeader = document.createElement('div');
                catHeader.style.cssText = 'margin-top:6px;font-weight:bold;color:#90caf9;font-size:12px;';
                catHeader.innerText = displayTitle;
                nodeContainer.appendChild(catHeader);

                grps.forEach(g => {
                    let isChecked = true;
                    if (activePage === 'structure' && (type === 'cetasika' || type === 'rupa')) isChecked = false;
                    if (activePage === 'association' && (type === 'structure' || type === 'root' || type === 'category')) isChecked = false;
                    if (activePage === 'root_cause' && (type === 'structure' || type === 'category')) isChecked = false;

                    createCheckbox(nodeContainer, `group-${g.replace(/\s+/g, '-')}`, g, isChecked, 'node-filter', g);
                });
            }
        });
    }

    function createCheckbox(parent, id, label, checked, className, value) {
        const wrapper = document.createElement('div');
        wrapper.style.padding = '1px 0';
        const chk = document.createElement('input');
        chk.type = 'checkbox';
        chk.id = id;
        chk.className = className;
        chk.checked = checked;
        chk.value = value || id.replace('link-', '');
        chk.onchange = updateFilters;

        const lbl = document.createElement('label');
        lbl.htmlFor = id;
        lbl.style.cssText = 'margin-left:6px;cursor:pointer;';
        lbl.innerText = label;

        wrapper.appendChild(chk);
        wrapper.appendChild(lbl);
        parent.appendChild(wrapper);
    }

    // --- UPDATE LOGIC ---
    function updateFilters() {
        const { nodeElements, linkElements, labelElements } = VDP.Core.getElements();
        const allLinks = VDP.Core.getAllLinks();

        const checkedLinkTypes = new Set();
        document.querySelectorAll('.link-filter:checked').forEach(c => checkedLinkTypes.add(c.value));

        const checkedGroups = new Set();
        document.querySelectorAll('.node-filter:checked').forEach(c => checkedGroups.add(c.value));

        const visibleLinks = allLinks.filter(l => {
            const typeOk = checkedLinkTypes.has(l.type);
            const sourceGroup = (typeof l.source === 'object' ? l.source.group : null) || 'Other';
            const targetGroup = (typeof l.target === 'object' ? l.target.group : null) || 'Other';
            return typeOk && checkedGroups.has(sourceGroup) && checkedGroups.has(targetGroup);
        });

        const visibleLinkSet = new Set(visibleLinks);

        // SVG elements use display:inline by default — use null to restore, not 'block'
        nodeElements.style('display', d => checkedGroups.has(d.group || 'Other') ? null : 'none');
        labelElements.style('display', d => checkedGroups.has(d.group || 'Other') ? null : 'none');
        linkElements.style('display', d => visibleLinkSet.has(d) ? null : 'none');

        VDP.Core.updateSimulationLinks(visibleLinks);
    }

    function updateColors() {
        const modeInput = document.querySelector('input[name="color-mode"]:checked');
        if (!modeInput) return;

        const mode = modeInput.value;
        const { nodeElements, colorScale } = VDP.Core.getElements();

        nodeElements.transition().duration(500).attr("fill", d => {
            if (mode === 'vedana') {
                if (d.vedana_color) return d.vedana_color;
                if (d.type === 'cetasika') return "#ccc";
                return "#555";
            }
            return colorScale(d.type);
        });
    }

    // --- LOADING ---
    function hideLoading() {
        const overlay = document.getElementById('loading-overlay');
        if (overlay) overlay.classList.add('hidden');
    }

    return {
        init,
        renderDynamicFilters,
        updateFilters,
        updateColors,
        handleMouseOver,
        handleMouseOut,
        showDetail,
        hideDetail,
        hideLoading
    };
})();
