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

// Colors
const colors = {
    citta: {
        Akusala: "#ff4757", // Red
        Ahetuka: "#70a1ff", // Blue (Vô Nhân)
        Kusala: "#2ecc71", // Green
        default: "#ff6b81"
    },
    cetasika: {
        Universals: "#ffa502", // Orange
        Occasionals: "#eccc68", // Light Orange
        Unwholesome: "#ff6348", // Dark Red
        Beautiful: "#7bed9f", // Light Green
        default: "#dfe6e9"
    }
};

function getNodeColor(d) {
    if (d.type === 'citta') {
        return colors.citta[d.group] || colors.citta.default;
    } else if (d.type === 'cetasika') {
        return colors.cetasika[d.group] || colors.cetasika.default;
    }
    return "#888";
}

// Tooltip logic
const tooltip = d3.select("#tooltip");

function showTooltip(event, d) {
    tooltip.style("display", "block")
        .style("left", (event.pageX + 15) + "px")
        .style("top", (event.pageY - 10) + "px")
        .html(`
            <strong>${d.name}</strong><br>
            <span style="color:#aaa">${d.name_pali || ''}</span><br>
            <hr style="border:0.5px solid #444">
            Type: ${d.type}<br>
            Group: ${d.group}<br>
            <small>ID: ${d.id}</small>
        `);
}

function hideTooltip() {
    tooltip.style("display", "none");
}

// Data Loading
d3.json("/api/data").then(data => {
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
        .attr("r", d => d.val)
        .attr("fill", d => getNodeColor(d))
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
        .text(d => d.type === 'citta' ? (d.short_name || d.id) : d.name);

    // Interaction
    nodeElements.on("mouseover", showTooltip)
        .on("mouseout", hideTooltip)
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

function updateFilters() {
    const checkedGroups = new Set();
    document.querySelectorAll('.chk-sub:checked').forEach(cb => checkedGroups.add(cb.value));

    const showCitta = document.getElementById('chk-citta').checked;
    const showCetasika = document.getElementById('chk-cetasika').checked;

    nodeElements.style("display", d => {
        if (d.type === 'citta' && !showCitta) return "none";
        if (d.type === 'cetasika' && !showCetasika) return "none";
        if (checkedGroups.has(d.group)) return "block";
        return "none";
    });

    labelElements.style("display", d => {
        if (d.type === 'citta' && !showCitta) return "none";
        if (d.type === 'cetasika' && !showCetasika) return "none";
        if (checkedGroups.has(d.group)) return "block";
        return "none";
    });

    // Hide links if connected node is hidden
    linkElements.style("display", d => {
        const sourceVisible = isNodeVisible(d.source, showCitta, showCetasika, checkedGroups);
        const targetVisible = isNodeVisible(d.target, showCitta, showCetasika, checkedGroups);
        return (sourceVisible && targetVisible) ? "block" : "none";
    });
}

function isNodeVisible(node, showCitta, showCetasika, checkedGroups) {
    if (node.type === 'citta' && !showCitta) return false;
    if (node.type === 'cetasika' && !showCetasika) return false;
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
