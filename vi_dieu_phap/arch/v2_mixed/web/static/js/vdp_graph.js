// Vi Dieu Phap Knowledge Graph - D3.js Implementation (Loop 2)

const width = window.innerWidth;
const height = window.innerHeight;

// Container
const svg = d3.select("#graph-container")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("background-color", "#1a1a1a")
    .on("click", resetHighlight); // Click background to reset

const container = svg.append("g");

let nodes = [];
let links = [];
let nodeElements, linkElements, labelElements;

// Zoom
const zoom = d3.zoom()
    .scaleExtent([0.1, 4])
    .on("zoom", (event) => {
        container.attr("transform", event.transform);
    });

svg.call(zoom);

// Simulation
const simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(width / 2, height / 2))
    .force("collide", d3.forceCollide().radius(d => d.val + 5));

// 4. Define Color Scale for new types
const colorScale = d3.scaleOrdinal()
    .domain(["root", "category", "sub_category", "citta", "cetasika", "rupa", "nibbana"])
    .range([
        "#FFD700", // Root: Gold
        "#87CEFA", // Category: Light Sky Blue
        "#B0C4DE", // Sub-category: Light Steel Blue
        "#ff7f0e", // Citta: Orange
        "#2ca02c", // Cetasika: Green
        "#8B4513", // Rupa: Saddle Brown (Earth)
        "#ffffff"  // Nibbana: White
    ]);

// Tooltip logic
const tooltip = d3.select("#tooltip");

// Data Loading
// UPDATED URL: /api/vdp/data
d3.json("/api/vdp/data").then(data => {
    console.log("Data loaded:", data);
    document.getElementById("node-count").innerText = data.nodes.length;
    document.getElementById("link-count").innerText = data.links.length;

    links = data.links.map(d => Object.create(d));
    nodes = data.nodes.map(d => Object.create(d));

    // Links
    linkElements = container.append("g")
        .attr("stroke", "#999")
        .attr("stroke-opacity", 0.6)
        .selectAll("line")
        .data(links)
        .join("line")
        .attr("stroke-width", 1);

    // Nodes
    nodeElements = container.append("g")
        .attr("stroke", "#fff")
        .attr("stroke-width", 1.5)
        .selectAll("circle")
        .data(nodes)
        .join("circle")
        .attr("r", d => d.val ? d.val : 5)
        // Default Color Logic
        .attr("fill", d => colorScale(d.type))
        .call(drag(simulation));

    // Labels
    labelElements = container.append("g")
        .attr("class", "labels")
        .selectAll("text")
        .data(nodes)
        .join("text")
        .attr("class", "node-label")
        .attr("dx", 12)
        .attr("dy", ".35em")
        .text(d => d.name);

    // Interaction
    nodeElements.on("mouseover", function (event, d) {
        tooltip.transition().duration(200).style("opacity", .9);
        tooltip.style("display", "block");

        let content = `<strong>${d.full_name || d.name}</strong><br>`;
        if (d.name_pali) content += `<i>${d.name_pali}</i><br>`;
        content += `<hr style="border:0.5px solid #444">`;
        content += `Type: ${d.type}<br>`;
        if (d.group) content += `Group: ${d.group}<br>`;

        // Show Vedana if available
        if (d.vedana) {
            content += `<br><span style="color: ${d.vedana_color || '#FFD700'}">● Vedana: ${d.vedana}</span>`;
        }

        if (d.description) {
            content += `<p style="margin:5px 0; font-style:italic; color:#ffd700">${d.description}</p>`;
        }

        content += `<hr style="border:0.5px solid #444"><small>ID: ${d.id}</small>`;

        tooltip.html(content)
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 28) + "px");
    })
        .on("mouseout", function (d) {
            tooltip.transition().duration(500).style("opacity", 0);
            tooltip.style("display", "none");
        })
        .on("click", (event, d) => {
            event.stopPropagation(); // Prevent background click
            highlightNode(d);
        });

    // Simulation Tick
    simulation.on("tick", () => {
        linkElements
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        nodeElements
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        labelElements
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    });

    simulation.nodes(nodes);
    simulation.force("link").links(links);
});

// --- FILTER & HIGHLIGHT LOGIC ---

// --- FILTER & HIGHLIGHT LOGIC ---

// Store original data
let allNodes = [];
let allLinks = [];

// Modify Data Loading to save to 'allNodes'/'allLinks' instead of direct 'nodes'/'links'
// NOTE: This requires updating the d3.json callback slightly in a real refactor, 
// but here we assume 'nodes' and 'links' are mutable global vars managed by updateFilters.
// Actually, let's keep it simple: We will NOT use the 'CSS hide' approach anymore.
// We will filter 'nodes' and 'links' and restart simulation.

// But wait, restarting simulation on every checkbox click is jarring. 
// A better "10/10" approach for now considering constraint:
// 1. Keep CSS hiding for small toggles (Group toggle).
// 2. For the HEAVY "Association Link" toggle, we should remove them from simulation.

function updateFilters() {
    const checkedGroups = new Set();
    document.querySelectorAll('.chk-sub:checked').forEach(cb => checkedGroups.add(cb.value));

    const showCitta = document.getElementById('chk-citta')?.checked ?? true;
    const showCetasika = document.getElementById('chk-cetasika')?.checked ?? true;
    const showRupa = document.getElementById('chk-rupa')?.checked ?? true;
    const showNibbana = document.getElementById('chk-nibbana')?.checked ?? true;

    const showStructure = document.getElementById('chk-link-structure')?.checked ?? true;
    const showAssociation = document.getElementById('chk-link-association')?.checked ?? false;

    // 1. Filter Nodes (CSS Hiding is fine for Nodes as count is low < 500)
    nodeElements.style("display", d => isNodeVisible(d, showCitta, showCetasika, showRupa, showNibbana, checkedGroups) ? "block" : "none");
    labelElements.style("display", d => isNodeVisible(d, showCitta, showCetasika, showRupa, showNibbana, checkedGroups) ? "block" : "none");

    // 2. Filter Links (CRITICAL PERFORMANCE FIX)
    // Instead of just hiding, verify if we should exclude them from calculation?
    // D3 Force calculates all links in 'links' array.
    // To optimize, we must Update values in simulation.force("link").links(...)

    // Determine which links are visible
    const visibleLinks = links.filter(d => {
        if (d.type === 'structure' && !showStructure) return false;
        if (d.type === 'association' && !showAssociation) return false;

        // Also hide if endpoints are hidden
        const sourceVisible = isNodeVisible(d.source, showCitta, showCetasika, showRupa, showNibbana, checkedGroups);
        const targetVisible = isNodeVisible(d.target, showCitta, showCetasika, showRupa, showNibbana, checkedGroups);
        return sourceVisible && targetVisible;
    });

    // Update Visualization
    linkElements.style("display", d => {
        // We still use CSS for smooth transition of existing elements
        // But for true performance we should use exit/enter. 
        // For this quick fix, let's stick to CSS but pause simulation if too heavy?
        // No, user requested "10/10".

        // Simple Logic: 
        if (d.type === 'structure' && !showStructure) return "none";
        if (d.type === 'association' && !showAssociation) return "none";

        const sourceVisible = isNodeVisible(d.source, showCitta, showCetasika, showRupa, showNibbana, checkedGroups);
        const targetVisible = isNodeVisible(d.target, showCitta, showCetasika, showRupa, showNibbana, checkedGroups);
        return (sourceVisible && targetVisible) ? "block" : "none";
    });

    // PERFORMANCE BOOSTER:
    // Only feed visible links to the Force Engine!
    simulation.force("link").links(visibleLinks);
    simulation.alpha(0.3).restart(); // Wake up simulation to adjust to new constraints
}

function isNodeVisible(node, showCitta, showCetasika, showRupa, showNibbana, checkedGroups) {
    if (node.type === 'citta' && !showCitta) return false;
    if (node.type === 'cetasika' && !showCetasika) return false;
    if (node.type === 'rupa' && !showRupa) return false;
    if (node.type === 'nibbana' && !showNibbana) return false;

    return checkedGroups.has(node.group);
}

function highlightNode(d) {
    // Find connected nodes
    const connected = new Set();
    connected.add(d.id);
    links.forEach(l => {
        if (l.source.id === d.id) connected.add(l.target.id);
        if (l.target.id === d.id) connected.add(l.source.id);
    });

    // Dim others
    nodeElements.style("opacity", n => connected.has(n.id) ? 1 : 0.1);
    linkElements.style("opacity", l => (l.source.id === d.id || l.target.id === d.id) ? 1 : 0.05);
    labelElements.style("opacity", n => connected.has(n.id) ? 1 : 0.1);
}

function resetHighlight() {
    nodeElements.style("opacity", 1);
    linkElements.style("opacity", 0.6);
    labelElements.style("opacity", 1);
}

// --- COLOR LOGIC ---
function updateColors() {
    const mode = document.querySelector('input[name="color-mode"]:checked').value;

    nodeElements.transition().duration(500).attr("fill", d => {
        if (mode === 'vedana') {
            // Apply Vedana Color if exists, else dim grey
            if (d.vedana_color) return d.vedana_color;
            if (d.type === 'cetasika') return "#ccc"; // Dim Cetasika in Vedana mode
            if (d.type === 'rupa') return "#ccc";
            return "#555"; // Default dim
        }
        // Default Structure Mode
        return colorScale(d.type);
    });
}

// --- SEARCH LOGIC ---
function searchNode() {
    const query = document.getElementById('search-box').value.toLowerCase();

    if (!query) {
        resetHighlight();
        updateFilters(); // Re-apply filters
        return;
    }

    const matched = nodes.filter(d =>
        d.name.toLowerCase().includes(query) ||
        (d.name_pali && d.name_pali.toLowerCase().includes(query)) ||
        d.id.toLowerCase().includes(query)
    );

    if (matched.length > 0) {
        const matchedIds = new Set(matched.map(d => d.id));

        nodeElements.style("opacity", d => matchedIds.has(d.id) ? 1 : 0.1);
        linkElements.style("opacity", 0.05);
        labelElements.style("opacity", d => matchedIds.has(d.id) ? 1 : 0.1);
    } else {
        // No match - dim all
        nodeElements.style("opacity", 0.1);
        linkElements.style("opacity", 0.05);
        labelElements.style("opacity", 0.1);
    }
}

// Drag Helper
function drag(simulation) {
    function dragstarted(event) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        event.subject.fx = event.subject.x;
        event.subject.fy = event.subject.y;
    }
    function dragged(event) {
        event.subject.fx = event.x;
        event.subject.fy = event.y;
    }
    function dragended(event) {
        if (!event.active) simulation.alphaTarget(0);
        event.subject.fx = null;
        event.subject.fy = null;
    }
    return d3.drag().on("start", dragstarted).on("drag", dragged).on("end", dragended);
}
