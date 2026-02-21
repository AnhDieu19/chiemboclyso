// Module: VDP.Core
// Responsibility: D3.js Simulation, Rendering, Physics

window.VDP = window.VDP || {};

VDP.Core = (function () {
    let simulation, svg, g;
    let linkElements, nodeElements, labelElements;
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Color Scale
    const colorScale = d3.scaleOrdinal()
        .domain(['root', 'category', 'sub_category', 'citta', 'cetasika', 'rupa', 'nibbana', 'hetu'])
        .range(['#ff00ff', '#ff9900', '#00ccff', '#ffee00', '#99ff99', '#ffcc99', '#ffffff', '#9370DB']); // Hetu = Purple

    function init() {
        svg = d3.select("#graph-container").append("svg")
            .attr("width", width)
            .attr("height", height)
            .call(d3.zoom().on("zoom", (event) => {
                g.attr("transform", event.transform);
            }));

        g = svg.append("g");

        // Define Arrowhead
        svg.append("defs").append("marker")
            .attr("id", "arrowhead")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 15) // Distance from node
            .attr("refY", 0)
            .attr("markerWidth", 6)
            .attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path")
            .attr("d", "M0,-5L10,0L0,5")
            .attr("fill", "#555");

        simulation = d3.forceSimulation()
            .force("link", d3.forceLink().id(d => d.id).distance(150))
            .force("charge", d3.forceManyBody().strength(-500))
            .force("center", d3.forceCenter(width / 2, height / 2).strength(0.05))
            .force("collide", d3.forceCollide().radius(d => (d.val ? Math.sqrt(d.val) * 2 : 5) + 10).iterations(3));
    }

    function render(nodes, links) {
        // Links
        linkElements = g.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(links)
            .enter().append("line")
            .attr("stroke-width", d => {
                if (d.type === 'structure') return 1.5;
                if (d.type === 'root_cause') return 1.0;
                return 0.5;
            })
            .attr("stroke", d => {
                if (d.type === 'structure') return "#555";
                if (d.type === 'root_cause') return "#FF4500"; // OrangeRed
                return "#333";
            })
            .attr("marker-end", d => (d.type === 'structure' || d.type === 'root_cause') ? "url(#arrowhead)" : null)
            .attr("stroke-dasharray", d => {
                if (d.type === 'association') return "4 2";
                if (d.type === 'root_cause') return "6 3";
                return null;
            });

        // Nodes
        nodeElements = g.append("g")
            .attr("class", "nodes")
            .selectAll("circle")
            .data(nodes)
            .enter().append("circle")
            .attr("r", d => d.val ? Math.sqrt(d.val) * 2 : 5)
            .attr("fill", d => colorScale(d.type))
            .call(d3.drag()
                .on("start", dragstarted)
                .on("drag", dragged)
                .on("end", dragended));

        // Labels
        labelElements = g.append("g")
            .attr("class", "labels")
            .selectAll("text")
            .data(nodes)
            .enter().append("text")
            .attr("class", "node-label")
            .attr("dy", -10)
            .attr("text-anchor", "middle")
            .text(d => d.name);

        // Interactions
        nodeElements.on("mouseover", VDP.UI.handleMouseOver)
            .on("mouseout", VDP.UI.handleMouseOut)
            .on("click", VDP.UI.handleNodeClick);

        // CRITICAL FIX: Set random initial positions BEFORE simulation setup
        nodes.forEach(d => {
            d.x = Math.random() * width;
            d.y = Math.random() * height;
        });

        // Setup simulation
        simulation.nodes(nodes).on("tick", ticked);
        simulation.force("link").links(links);

        // Start simulation naturally
        simulation.alpha(1).restart();
    }

    function ticked() {
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
    }

    // Drag Functions
    function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }

    // Expose update function for Filtering
    function updateSimulationLinks(visibleLinks) {
        simulation.force("link").links(visibleLinks);
        simulation.alpha(0.3).restart();
    }

    function getElements() {
        return { nodeElements, linkElements, labelElements, colorScale };
    }

    return {
        init: init,
        render: render,
        updateSimulationLinks: updateSimulationLinks,
        getElements: getElements
    };
})();
