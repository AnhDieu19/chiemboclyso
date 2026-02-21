// Module: VDP.Core
// Responsibility: D3.js Simulation, Rendering, Physics, Neighbor Highlighting

window.VDP = window.VDP || {};

VDP.Core = (function () {
    let simulation, svg, g;
    let linkElements, nodeElements, labelElements;
    let allLinksData = [];
    let allNodesData = [];
    let neighborMap = {};  // nodeId -> Set of neighbor IDs
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Color Scale
    const colorScale = d3.scaleOrdinal()
        .domain(['root', 'category', 'sub_category', 'citta', 'cetasika', 'rupa', 'nibbana', 'hetu'])
        .range(['#ff00ff', '#ff9900', '#00ccff', '#ffee00', '#99ff99', '#ffcc99', '#ffffff', '#9370DB']);

    function init() {
        svg = d3.select("#graph-container").append("svg")
            .attr("width", width)
            .attr("height", height)
            .call(d3.zoom().scaleExtent([0.1, 8]).on("zoom", (event) => {
                g.attr("transform", event.transform);
            }));

        g = svg.append("g");

        // Define Arrowheads
        const defs = svg.append("defs");

        // Structure arrow (gray)
        defs.append("marker")
            .attr("id", "arrow-structure")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 18).attr("refY", 0)
            .attr("markerWidth", 6).attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path").attr("d", "M0,-5L10,0L0,5").attr("fill", "#555");

        // Root cause arrow (orange-red)
        defs.append("marker")
            .attr("id", "arrow-rootcause")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 18).attr("refY", 0)
            .attr("markerWidth", 6).attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path").attr("d", "M0,-5L10,0L0,5").attr("fill", "#FF4500");

        // Highlight arrow (gold)
        defs.append("marker")
            .attr("id", "arrow-highlight")
            .attr("viewBox", "0 -5 10 10")
            .attr("refX", 18).attr("refY", 0)
            .attr("markerWidth", 6).attr("markerHeight", 6)
            .attr("orient", "auto")
            .append("path").attr("d", "M0,-5L10,0L0,5").attr("fill", "#ffd740");

        simulation = d3.forceSimulation()
            .force("link", d3.forceLink().id(d => d.id).distance(d => {
                if (d.type === 'structure') return 120;
                if (d.type === 'root_cause') return 180;
                return 100;
            }))
            .force("charge", d3.forceManyBody().strength(-400))
            .force("center", d3.forceCenter(width / 2, height / 2).strength(0.05))
            .force("collide", d3.forceCollide().radius(d => getRadius(d) + 8).iterations(2));
    }

    function getRadius(d) {
        return d.val ? Math.sqrt(d.val) * 2.5 : 5;
    }

    function render(nodes, links) {
        allLinksData = links;
        allNodesData = nodes;

        // Build neighbor map for highlighting
        neighborMap = {};
        nodes.forEach(n => { neighborMap[n.id] = new Set(); });
        links.forEach(l => {
            const sid = typeof l.source === 'object' ? l.source.id : l.source;
            const tid = typeof l.target === 'object' ? l.target.id : l.target;
            if (neighborMap[sid]) neighborMap[sid].add(tid);
            if (neighborMap[tid]) neighborMap[tid].add(sid);
        });

        // Links
        linkElements = g.append("g")
            .attr("class", "links")
            .selectAll("line")
            .data(links)
            .enter().append("line")
            .attr("stroke-width", d => {
                if (d.type === 'structure') return 1.5;
                if (d.type === 'root_cause') return 1.2;
                return 0.5;
            })
            .attr("stroke", d => {
                if (d.type === 'structure') return "#555";
                if (d.type === 'root_cause') return "#FF4500";
                return "#444";
            })
            .attr("stroke-opacity", d => d.type === 'association' ? 0.4 : 0.7)
            .attr("marker-end", d => {
                if (d.type === 'structure') return "url(#arrow-structure)";
                if (d.type === 'root_cause') return "url(#arrow-rootcause)";
                return null;
            })
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
            .attr("r", d => getRadius(d))
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
            .attr("dy", d => -(getRadius(d) + 4))
            .attr("text-anchor", "middle")
            .text(d => d.name);

        // Interactions
        nodeElements
            .on("mouseover", VDP.UI.handleMouseOver)
            .on("mouseout", VDP.UI.handleMouseOut)
            .on("click", handleNodeClick);

        // Click on background to reset highlight
        svg.on("click", function(event) {
            if (event.target.tagName === 'svg' || event.target.tagName === 'rect') {
                resetHighlight();
                VDP.UI.hideDetail();
            }
        });

        // Set random initial positions
        nodes.forEach(d => {
            d.x = Math.random() * width;
            d.y = Math.random() * height;
        });

        // Setup simulation
        simulation.nodes(nodes).on("tick", ticked);
        simulation.force("link").links(links);
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

    // --- Neighbor Highlighting ---
    function handleNodeClick(event, d) {
        event.stopPropagation();
        highlightNeighbors(d);
        VDP.UI.showDetail(d);
    }

    function highlightNeighbors(d) {
        const neighbors = neighborMap[d.id] || new Set();

        nodeElements
            .classed("node-dimmed", n => n.id !== d.id && !neighbors.has(n.id))
            .classed("node-highlight", n => n.id === d.id);

        linkElements
            .classed("link-dimmed", l => {
                const sid = typeof l.source === 'object' ? l.source.id : l.source;
                const tid = typeof l.target === 'object' ? l.target.id : l.target;
                return sid !== d.id && tid !== d.id;
            })
            .classed("link-highlight", l => {
                const sid = typeof l.source === 'object' ? l.source.id : l.source;
                const tid = typeof l.target === 'object' ? l.target.id : l.target;
                return sid === d.id || tid === d.id;
            })
            .attr("marker-end", l => {
                const sid = typeof l.source === 'object' ? l.source.id : l.source;
                const tid = typeof l.target === 'object' ? l.target.id : l.target;
                if (sid === d.id || tid === d.id) return "url(#arrow-highlight)";
                if (l.type === 'structure') return "url(#arrow-structure)";
                if (l.type === 'root_cause') return "url(#arrow-rootcause)";
                return null;
            });

        labelElements
            .classed("node-dimmed", n => n.id !== d.id && !neighbors.has(n.id));
    }

    function resetHighlight() {
        nodeElements.classed("node-dimmed", false).classed("node-highlight", false).classed("search-match", false);
        linkElements.classed("link-dimmed", false).classed("link-highlight", false)
            .attr("marker-end", d => {
                if (d.type === 'structure') return "url(#arrow-structure)";
                if (d.type === 'root_cause') return "url(#arrow-rootcause)";
                return null;
            });
        labelElements.classed("node-dimmed", false);
    }

    // --- Search Highlight ---
    function highlightSearch(query) {
        if (!query || query.length < 2) {
            resetHighlight();
            return 0;
        }
        const q = query.toLowerCase();
        let matchCount = 0;

        nodeElements.classed("search-match", d => {
            const match = (d.name && d.name.toLowerCase().includes(q)) ||
                          (d.name_pali && d.name_pali.toLowerCase().includes(q));
            if (match) matchCount++;
            return match;
        });
        nodeElements.classed("node-dimmed", d => {
            return !(d.name && d.name.toLowerCase().includes(q)) &&
                   !(d.name_pali && d.name_pali.toLowerCase().includes(q));
        });
        labelElements.classed("node-dimmed", d => {
            return !(d.name && d.name.toLowerCase().includes(q)) &&
                   !(d.name_pali && d.name_pali.toLowerCase().includes(q));
        });
        linkElements.classed("link-dimmed", true);

        return matchCount;
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

    function updateSimulationLinks(visibleLinks) {
        simulation.force("link").links(visibleLinks);
        simulation.alpha(0.3).restart();
    }

    function getElements() {
        return { nodeElements, linkElements, labelElements, colorScale };
    }

    function getAllLinks() {
        return allLinksData;
    }

    function getAllNodes() {
        return allNodesData;
    }

    return {
        init,
        render,
        updateSimulationLinks,
        getElements,
        getAllLinks,
        getAllNodes,
        highlightNeighbors,
        highlightSearch,
        resetHighlight,
        getRadius
    };
})();
