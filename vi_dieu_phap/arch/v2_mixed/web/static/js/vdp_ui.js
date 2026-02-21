// Module: VDP.UI
// Responsibility: Filter Logic, Tooltips, Search, Color Modes

window.VDP = window.VDP || {};

VDP.UI = (function () {
    let tooltip;

    function init() {
        tooltip = d3.select("#tooltip");
    }

    // --- TOOLTIPS ---
    function handleMouseOver(event, d) {
        let content = `<strong>${d.name}</strong>`;
        if (d.name_pali) content += `<br><em>${d.name_pali}</em>`;
        if (d.group) content += `<br>Group: ${d.group}`;
        if (d.vedana) {
            content += `<br><span style="color: ${d.vedana_color || '#FFD700'}">● Vedana: ${d.vedana}</span>`;
        }
        if (d.description) content += `<br><small>${d.description}</small>`;

        tooltip.style("display", "block")
            .html(content)
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY + 10) + "px");

        // Highlight logic could go here
    }

    function handleMouseOut(event, d) {
        tooltip.style("display", "none");
    }

    function handleNodeClick(event, d) {
        console.log("Clicked:", d);
    }

    // --- DYNAMIC FILTERS ---
    function renderDynamicFilters(nodes) {
        const container = document.getElementById('dynamic-filters');
        container.innerHTML = '';

        const groupsByType = {
            'citta': new Set(),
            'cetasika': new Set(),
            'rupa': new Set(),
            'nibbana': new Set(),
            'other': new Set()
        };

        nodes.forEach(n => {
            if (n.group === 'Structure' || n.group === 'Root') { // Hetu has group 'Root'
                groupsByType['other'].add(n.group);
                return;
            }
            if (groupsByType[n.type]) {
                groupsByType[n.type].add(n.group);
            } else {
                groupsByType['other'].add(n.group);
            }
        });

        const createSection = (title, typeKey, showAllId) => {
            const groups = Array.from(groupsByType[typeKey]).sort();
            if (groups.length === 0) return;

            const strong = document.createElement('strong');
            strong.innerText = title;
            container.appendChild(strong);

            const groupDiv = document.createElement('div');
            groupDiv.className = 'filter-group';

            const chkAll = document.createElement('input');
            chkAll.type = 'checkbox';
            chkAll.id = showAllId;
            chkAll.checked = false; // Changed to false for hierarchical default view
            chkAll.onchange = updateFilters; // Hook
            groupDiv.appendChild(chkAll);
            groupDiv.appendChild(document.createTextNode(' Show All'));
            groupDiv.appendChild(document.createElement('br'));

            groups.forEach(grp => {
                const label = document.createElement('label');
                label.style.marginLeft = "10px";
                label.style.display = "block";

                const chk = document.createElement('input');
                chk.type = 'checkbox';
                chk.className = 'chk-sub';
                chk.value = grp;
                chk.checked = false; // Changed to false for hierarchical default view
                chk.onchange = updateFilters;

                label.appendChild(chk);
                label.appendChild(document.createTextNode(` ${grp}`));
                groupDiv.appendChild(label);
            });

            container.appendChild(groupDiv);
        };

        createSection('Citta (Tâm)', 'citta', 'chk-citta');
        createSection('Cetasika (Sở Hữu)', 'cetasika', 'chk-cetasika');
        createSection('Rupa (Sắc Pháp)', 'rupa', 'chk-rupa');
        createSection('Nibbana (Niết Bàn)', 'nibbana', 'chk-nibbana');
    }

    // --- UPDATE LOGIC ---
    function updateFilters() {
        const { nodeElements, linkElements, labelElements } = VDP.Core.getElements();
        const allLinks = VDP.Main.getAllLinks(); // Access Main's data

        const checkedGroups = new Set();
        document.querySelectorAll('.chk-sub:checked').forEach(cb => checkedGroups.add(cb.value));

        // Default state: Show only structure nodes, hide detailed content
        const showCitta = document.getElementById('chk-citta')?.checked ?? false; // Changed default to false
        const showCetasika = document.getElementById('chk-cetasika')?.checked ?? false; // Changed default to false
        const showRupa = document.getElementById('chk-rupa')?.checked ?? false; // Changed default to false
        const showNibbana = document.getElementById('chk-nibbana')?.checked ?? false; // Changed default to false

        const showStructure = document.getElementById('chk-link-structure')?.checked ?? true;
        const showAssociation = document.getElementById('chk-link-association')?.checked ?? false;
        const showRoot = document.getElementById('chk-link-root')?.checked ?? false;

        // 1. Filter Nodes (CSS)
        nodeElements.style("display", d => isNodeVisible(d, showCitta, showCetasika, showRupa, showNibbana, checkedGroups) ? "block" : "none");
        labelElements.style("display", d => isNodeVisible(d, showCitta, showCetasika, showRupa, showNibbana, checkedGroups) ? "block" : "none");

        // 2. Filter Links & Update Simulation
        const visibleLinks = allLinks.filter(d => {
            if (d.type === 'structure' && !showStructure) return false;
            if (d.type === 'association' && !showAssociation) return false;
            if (d.type === 'root_cause' && !showRoot) return false;

            const sourceVisible = isNodeVisible(d.source, showCitta, showCetasika, showRupa, showNibbana, checkedGroups);
            const targetVisible = isNodeVisible(d.target, showCitta, showCetasika, showRupa, showNibbana, checkedGroups);
            return sourceVisible && targetVisible;
        });

        linkElements.style("display", d => {
            // Basic display check logic again to match visibleLinks (or just rely on Sim update if we used exit/enter)
            // For CSS hide:
            const isVisible = visibleLinks.includes(d);
            return isVisible ? "block" : "none";
        });

        // Critical: Update Simulation
        VDP.Core.updateSimulationLinks(visibleLinks);
    }

    function isNodeVisible(node, showCitta, showCetasika, showRupa, showNibbana, checkedGroups) {
        if (node.type === 'citta' && !showCitta) return false;
        if (node.type === 'cetasika' && !showCetasika) return false;
        if (node.type === 'rupa' && !showRupa) return false;
        if (node.type === 'nibbana' && !showNibbana) return false;

        return checkedGroups.has(node.group);
    }

    function updateColors() {
        const mode = document.querySelector('input[name="color-mode"]:checked').value;
        const { nodeElements, colorScale } = VDP.Core.getElements();

        nodeElements.transition().duration(500).attr("fill", d => {
            if (mode === 'vedana') {
                if (d.vedana_color) return d.vedana_color;
                if (d.type === 'cetasika') return "#ccc"; // Dim others
                if (d.type === 'rupa') return "#ccc";
                return "#555";
            }
            return colorScale(d.type);
        });
    }

    function searchNode() {
        // Implement search highlight
    }

    return {
        init: init,
        renderDynamicFilters: renderDynamicFilters,
        updateFilters: updateFilters,
        updateColors: updateColors,
        searchNode: searchNode,
        handleMouseOver: handleMouseOver,
        handleMouseOut: handleMouseOut,
        handleNodeClick: handleNodeClick
    };
})();
