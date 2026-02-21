/**
 * Fano Plane Visualization
 * =========================
 * Draws the 7-point projective plane (Fano plane) with Bát Quái labels.
 * Uses D3.js for SVG rendering.
 *
 * Layout: Equilateral triangle with vertices (e₁, e₂, e₄),
 *         midpoints (e₃, e₅, e₆), center (e₇).
 *         7 lines (3 sides + 3 medians + 1 inscribed circle).
 */

const FanoPlane = (() => {
    let svg, g;
    let selectedNode = null;
    let width, height;
    const R = 180; // Triangle circumradius

    // Node positions in Fano plane layout
    // Vertices of equilateral triangle
    const positions = {};
    const nodeRadius = 34;

    function computePositions() {
        const cx = 0, cy = 0;
        // Triangle vertices (pointing up)
        positions[1] = { x: cx, y: cy - R };                           // e₁ (Chấn) — top
        positions[2] = { x: cx - R * Math.sin(Math.PI / 3), y: cy + R * 0.5 };  // e₂ (Khảm) — bottom-left
        positions[4] = { x: cx + R * Math.sin(Math.PI / 3), y: cy + R * 0.5 };  // e₄ (Cấn) — bottom-right

        // Midpoints
        positions[3] = midpoint(positions[1], positions[2]); // e₃ (Đoài) — left edge mid
        positions[5] = midpoint(positions[1], positions[4]); // e₅ (Ly) — right edge mid
        positions[6] = midpoint(positions[2], positions[4]); // e₆ (Tốn) — bottom edge mid

        // Center
        positions[7] = { x: cx, y: cy + R * 0.5 / 3 * (-1) + R * 0.5 * 2 / 3 };
        // Actually compute centroid properly
        positions[7] = {
            x: (positions[1].x + positions[2].x + positions[4].x) / 3,
            y: (positions[1].y + positions[2].y + positions[4].y) / 3
        };
    }

    function midpoint(a, b) {
        return { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
    }

    /**
     * Each Fano line = 3 points. We draw:
     * - Straight lines for triangle sides & medians
     * - A circle through midpoints (inscribed circle)
     */
    const lines = [
        { points: [1, 3, 2], type: "side",   label: "e₁e₂=e₃" },  // left side
        { points: [1, 5, 4], type: "side",   label: "e₁e₄=e₅" },  // right side
        { points: [2, 6, 4], type: "side",   label: "e₂e₄=e₆" },  // bottom side
        { points: [3, 7, 4], type: "median", label: "e₃e₄=e₇" },  // median: left-mid → center → right-vertex
        { points: [1, 7, 6], type: "median", label: "e₁e₆=e₇" },  // median: top → center → bottom-mid
        { points: [2, 7, 5], type: "median", label: "e₂e₅=e₇" },  // median: bot-left → center → right-mid
        { points: [3, 6, 5], type: "circle", label: "e₃e₅=e₆" }   // inscribed circle (midpoints)
    ];

    const lineColors = [
        "#FF7043", "#42A5F5", "#66BB6A", "#AB47BC",
        "#FFCA28", "#26C6DA", "#EF5350"
    ];

    function init(containerId) {
        const container = d3.select(containerId);
        const rect = container.node().getBoundingClientRect();
        width = rect.width || 500;
        height = rect.height || 500;

        computePositions();

        svg = container.append("svg")
            .attr("viewBox", `-${width/2} -${height/2} ${width} ${height}`)
            .attr("preserveAspectRatio", "xMidYMid meet");

        // Defs for glow filter
        const defs = svg.append("defs");
        const filter = defs.append("filter").attr("id", "glow");
        filter.append("feGaussianBlur").attr("stdDeviation", "4").attr("result", "coloredBlur");
        const feMerge = filter.append("feMerge");
        feMerge.append("feMergeNode").attr("in", "coloredBlur");
        feMerge.append("feMergeNode").attr("in", "SourceGraphic");

        // Arrow marker
        defs.append("marker")
            .attr("id", "arrowhead")
            .attr("markerWidth", 8)
            .attr("markerHeight", 6)
            .attr("refX", 8)
            .attr("refY", 3)
            .attr("orient", "auto")
            .append("polygon")
            .attr("points", "0 0, 8 3, 0 6")
            .attr("fill", "#fff")
            .attr("opacity", 0.6);

        g = svg.append("g").attr("class", "fano-group");

        drawLines();
        drawNodes();
        drawLegend();
    }

    function drawLines() {
        const linesGroup = g.append("g").attr("class", "fano-lines");

        lines.forEach((line, idx) => {
            const color = lineColors[idx];

            if (line.type === "circle") {
                // Draw arc through the 3 midpoints
                const pts = line.points.map(id => positions[id]);
                const circle = circumscribedCircle(pts[0], pts[1], pts[2]);
                if (circle) {
                    linesGroup.append("circle")
                        .attr("cx", circle.cx)
                        .attr("cy", circle.cy)
                        .attr("r", circle.r)
                        .attr("fill", "none")
                        .attr("stroke", color)
                        .attr("stroke-width", 2.5)
                        .attr("stroke-dasharray", "8,4")
                        .attr("opacity", 0.7)
                        .attr("class", `fano-line fano-line-${idx}`)
                        .attr("data-triple", line.points.join(","));
                }
            } else {
                // Straight line through all 3 points
                const pts = line.points.map(id => positions[id]);
                // Draw line from first to last point (passing through middle)
                linesGroup.append("line")
                    .attr("x1", pts[0].x)
                    .attr("y1", pts[0].y)
                    .attr("x2", pts[2].x)
                    .attr("y2", pts[2].y)
                    .attr("stroke", color)
                    .attr("stroke-width", 2.5)
                    .attr("opacity", 0.6)
                    .attr("class", `fano-line fano-line-${idx}`)
                    .attr("data-triple", line.points.join(","));
            }

            // Line label  
            const labelPt = line.points.map(id => positions[id]);
            const tripleData = FANO_TRIPLES[idx];
            const labelX = (labelPt[0].x + labelPt[1].x + labelPt[2].x) / 3;
            const labelY = (labelPt[0].y + labelPt[1].y + labelPt[2].y) / 3;
        });
    }

    function drawNodes() {
        const nodesGroup = g.append("g").attr("class", "fano-nodes");

        for (let id = 1; id <= 7; id++) {
            const pos = positions[id];
            const tri = TRIGRAMS[id];

            const nodeG = nodesGroup.append("g")
                .attr("class", `fano-node node-${id}`)
                .attr("transform", `translate(${pos.x}, ${pos.y})`)
                .style("cursor", "pointer")
                .on("click", () => toggleNode(id))
                .on("mouseenter", () => highlightNode(id, true))
                .on("mouseleave", () => highlightNode(id, false));

            // Outer glow circle
            nodeG.append("circle")
                .attr("r", nodeRadius + 4)
                .attr("fill", "none")
                .attr("stroke", tri.color)
                .attr("stroke-width", 2)
                .attr("opacity", 0.3)
                .attr("class", "node-glow");

            // Main circle
            nodeG.append("circle")
                .attr("r", nodeRadius)
                .attr("fill", tri.color)
                .attr("fill-opacity", 0.2)
                .attr("stroke", tri.color)
                .attr("stroke-width", 2.5)
                .attr("class", "node-circle");

            // Trigram symbol
            nodeG.append("text")
                .attr("text-anchor", "middle")
                .attr("dy", "-0.3em")
                .attr("font-size", "20px")
                .attr("fill", "#fff")
                .text(tri.symbol);

            // Trigram name
            nodeG.append("text")
                .attr("text-anchor", "middle")
                .attr("dy", "1.2em")
                .attr("font-size", "11px")
                .attr("fill", tri.color)
                .attr("font-weight", "bold")
                .text(`${tri.name} (e${id})`);
        }
    }

    function drawLegend() {
        const legendG = g.append("g")
            .attr("class", "fano-legend")
            .attr("transform", `translate(${-width/2 + 20}, ${-height/2 + 20})`);

        legendG.append("text")
            .attr("fill", "#aaa")
            .attr("font-size", "11px")
            .attr("font-weight", "bold")
            .text("7 đường Fano (click quái để xem)");

        lines.forEach((line, idx) => {
            const tripleData = FANO_TRIPLES[idx];
            const row = legendG.append("g")
                .attr("transform", `translate(0, ${18 + idx * 16})`);

            row.append("line")
                .attr("x1", 0).attr("y1", 0)
                .attr("x2", 18).attr("y2", 0)
                .attr("stroke", lineColors[idx])
                .attr("stroke-width", 2)
                .attr("stroke-dasharray", line.type === "circle" ? "4,2" : "none");

            row.append("text")
                .attr("x", 24)
                .attr("dy", "0.35em")
                .attr("fill", "#ccc")
                .attr("font-size", "10px")
                .text(tripleData.meaning);
        });
    }

    function toggleNode(id) {
        if (selectedNode === id) {
            selectedNode = null;
            clearHighlights();
            updateInfoPanel(null);
        } else {
            selectedNode = id;
            showNodeRelations(id);
            updateInfoPanel(id);
        }
    }

    function highlightNode(id, active) {
        const node = g.select(`.node-${id}`);
        if (active) {
            node.select(".node-circle")
                .transition().duration(200)
                .attr("fill-opacity", 0.5)
                .attr("r", nodeRadius + 4);
            node.select(".node-glow")
                .transition().duration(200)
                .attr("opacity", 0.8)
                .attr("r", nodeRadius + 10);
        } else {
            if (selectedNode !== id) {
                node.select(".node-circle")
                    .transition().duration(200)
                    .attr("fill-opacity", 0.2)
                    .attr("r", nodeRadius);
                node.select(".node-glow")
                    .transition().duration(200)
                    .attr("opacity", 0.3)
                    .attr("r", nodeRadius + 4);
            }
        }
    }

    function showNodeRelations(id) {
        clearHighlights();
        const tri = TRIGRAMS[id];

        // Highlight connected lines
        lines.forEach((line, idx) => {
            if (line.points.includes(id)) {
                g.selectAll(`.fano-line-${idx}`)
                    .transition().duration(300)
                    .attr("opacity", 1)
                    .attr("stroke-width", 4);
            } else {
                g.selectAll(`.fano-line-${idx}`)
                    .transition().duration(300)
                    .attr("opacity", 0.15);
            }
        });

        // Highlight connected nodes
        const connectedNodes = new Set();
        lines.forEach(line => {
            if (line.points.includes(id)) {
                line.points.forEach(p => connectedNodes.add(p));
            }
        });

        for (let nid = 1; nid <= 7; nid++) {
            const node = g.select(`.node-${nid}`);
            if (nid === id) {
                node.select(".node-circle")
                    .transition().duration(300)
                    .attr("fill-opacity", 0.6)
                    .attr("r", nodeRadius + 6);
                node.select(".node-glow")
                    .transition().duration(300)
                    .attr("opacity", 1)
                    .attr("r", nodeRadius + 14);
            } else if (connectedNodes.has(nid)) {
                node.select(".node-circle")
                    .transition().duration(300)
                    .attr("fill-opacity", 0.4);
            } else {
                node.select(".node-circle")
                    .transition().duration(300)
                    .attr("fill-opacity", 0.08);
                node.selectAll("text")
                    .transition().duration(300)
                    .attr("opacity", 0.3);
            }
        }
    }

    function clearHighlights() {
        lines.forEach((_, idx) => {
            g.selectAll(`.fano-line-${idx}`)
                .transition().duration(300)
                .attr("opacity", idx === 6 ? 0.7 : 0.6)
                .attr("stroke-width", 2.5);
        });

        for (let nid = 1; nid <= 7; nid++) {
            const node = g.select(`.node-${nid}`);
            node.select(".node-circle")
                .transition().duration(300)
                .attr("fill-opacity", 0.2)
                .attr("r", nodeRadius);
            node.select(".node-glow")
                .transition().duration(300)
                .attr("opacity", 0.3)
                .attr("r", nodeRadius + 4);
            node.selectAll("text")
                .transition().duration(300)
                .attr("opacity", 1);
        }
    }

    function updateInfoPanel(id) {
        const panel = document.getElementById("fano-info");
        if (!panel) return;

        if (!id) {
            panel.innerHTML = `<p class="hint">Click vào một quái trên mặt phẳng Fano để xem quan hệ nhân.</p>`;
            return;
        }

        const tri = TRIGRAMS[id];
        let html = `<h4 style="color:${tri.color}">${tri.symbol} ${tri.name} (${tri.han}) — ${tri.octonion}</h4>`;
        html += `<p class="nature-tag">${tri.nature} · ${tri.element} · ${tri.binary}</p>`;
        html += `<table class="relation-table"><thead><tr><th>Phép nhân</th><th>Kết quả</th><th>Ý nghĩa</th></tr></thead><tbody>`;

        for (let j = 1; j <= 7; j++) {
            if (j === id) continue;
            const r = MULT_TABLE[id][j];
            const target = TRIGRAMS[r.index];
            const signClass = r.sign > 0 ? "sinh" : "khac";
            const signLabel = r.sign > 0 ? "SINH" : "KHẮC";
            html += `<tr class="${signClass}">
                <td>${tri.symbol} × ${TRIGRAMS[j].symbol}</td>
                <td>${r.sign < 0 ? "−" : "+"}${target.symbol} ${target.name}</td>
                <td><span class="sign-badge ${signClass}">${signLabel}</span></td>
            </tr>`;
        }

        html += `</tbody></table>`;
        panel.innerHTML = html;
    }

    // Utility: circumscribed circle through 3 points
    function circumscribedCircle(p1, p2, p3) {
        const ax = p1.x, ay = p1.y;
        const bx = p2.x, by = p2.y;
        const cx = p3.x, cy = p3.y;
        const d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by));
        if (Math.abs(d) < 1e-10) return null;
        const ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d;
        const uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d;
        const r = Math.sqrt((ax - ux) ** 2 + (ay - uy) ** 2);
        return { cx: ux, cy: uy, r };
    }

    return { init };
})();
