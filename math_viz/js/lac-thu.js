/**
 * Lạc Thư (洛書) Magic Square — Interactive Visualization
 * ========================================================
 * Shows the 3×3 magic square with:
 * - Palace Ngũ Hành colors
 * - Row/Col/Diagonal sums = 15
 * - Opposition pairs (p ↔ 10−p)
 * - Click to highlight lines through a cell
 */

const LacThuViz = (() => {
    const CELL_SIZE = 100;
    const GAP = 6;
    const GRID_W = CELL_SIZE * 3 + GAP * 4;
    const GRID_H = CELL_SIZE * 3 + GAP * 4;
    const MARGIN = { top: 40, right: 240, bottom: 60, left: 40 };

    let svg, activeCell = null;

    function init(containerId) {
        const container = d3.select(containerId);
        const totalW = GRID_W + MARGIN.left + MARGIN.right;
        const totalH = GRID_H + MARGIN.top + MARGIN.bottom;

        svg = container.append("svg")
            .attr("viewBox", `0 0 ${totalW} ${totalH}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%")
            .style("max-height", "500px");

        const g = svg.append("g")
            .attr("transform", `translate(${MARGIN.left}, ${MARGIN.top})`);

        drawGrid(g);
        drawSumLabels(g);
        drawInfoPanel(g);
        drawOppositionDiagram(g);
    }

    function drawGrid(g) {
        const gridG = g.append("g").attr("class", "lt-grid");

        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                const val = LAC_THU.matrix[row][col];
                const palace = LAC_THU.palaces[val];
                const x = GAP + col * (CELL_SIZE + GAP);
                const y = GAP + row * (CELL_SIZE + GAP);

                const cellG = gridG.append("g")
                    .attr("class", `lt-cell lt-cell-${val}`)
                    .attr("transform", `translate(${x}, ${y})`)
                    .style("cursor", "pointer")
                    .on("click", () => toggleCell(val, g))
                    .on("mouseenter", function () {
                        d3.select(this).select("rect").attr("stroke-width", 3).attr("stroke", "#fff");
                    })
                    .on("mouseleave", function () {
                        const isActive = activeCell === val;
                        d3.select(this).select("rect")
                            .attr("stroke-width", isActive ? 3 : 1.5)
                            .attr("stroke", isActive ? "#FFD700" : "rgba(255,255,255,0.2)");
                    });

                // Element-colored background
                const hanhColor = NGU_HANH.colors[palace.element];
                cellG.append("rect")
                    .attr("width", CELL_SIZE)
                    .attr("height", CELL_SIZE)
                    .attr("rx", 8)
                    .attr("fill", hanhColor.bg)
                    .attr("fill-opacity", 0.25)
                    .attr("stroke", "rgba(255,255,255,0.2)")
                    .attr("stroke-width", 1.5);

                // Number (large)
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2)
                    .attr("y", CELL_SIZE / 2 - 12)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "32px")
                    .attr("font-weight", "700")
                    .attr("fill", hanhColor.bg)
                    .text(val);

                // Trigram symbol
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2)
                    .attr("y", CELL_SIZE / 2 + 14)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "20px")
                    .attr("fill", "rgba(255,255,255,0.8)")
                    .text(palace.symbol);

                // Palace name + direction
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2)
                    .attr("y", CELL_SIZE / 2 + 35)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "10px")
                    .attr("fill", "var(--text-muted)")
                    .text(`${palace.name} · ${palace.dir}`);

                // Element badge
                cellG.append("rect")
                    .attr("x", CELL_SIZE - 32)
                    .attr("y", 4)
                    .attr("width", 28)
                    .attr("height", 16)
                    .attr("rx", 8)
                    .attr("fill", hanhColor.bg)
                    .attr("fill-opacity", 0.6);
                cellG.append("text")
                    .attr("x", CELL_SIZE - 18)
                    .attr("y", 15)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px")
                    .attr("font-weight", "600")
                    .attr("fill", hanhColor.fg)
                    .text(palace.element);
            }
        }
    }

    function drawSumLabels(g) {
        const sumG = g.append("g").attr("class", "lt-sums");
        // Row sums
        for (let row = 0; row < 3; row++) {
            const y = GAP + row * (CELL_SIZE + GAP) + CELL_SIZE / 2;
            sumG.append("text")
                .attr("x", GRID_W + 8)
                .attr("y", y)
                .attr("dy", "0.35em")
                .attr("font-size", "14px")
                .attr("font-weight", "600")
                .attr("fill", "var(--accent-gold)")
                .text("= 15");
        }
        // Col sums
        for (let col = 0; col < 3; col++) {
            const x = GAP + col * (CELL_SIZE + GAP) + CELL_SIZE / 2;
            sumG.append("text")
                .attr("x", x)
                .attr("y", GRID_H + 20)
                .attr("text-anchor", "middle")
                .attr("font-size", "14px")
                .attr("font-weight", "600")
                .attr("fill", "var(--accent-gold)")
                .text("= 15");
        }
        // Diagonal indicators
        sumG.append("text")
            .attr("x", GRID_W + 8).attr("y", GRID_H + 20)
            .attr("font-size", "11px").attr("fill", "var(--text-muted)")
            .text("↗↘ = 15");
    }

    function drawInfoPanel(g) {
        const infoX = GRID_W + 50;
        const infoG = g.append("g").attr("class", "lt-info").attr("transform", `translate(${infoX}, 0)`);

        infoG.append("text").attr("y", 0).attr("font-size", "14px").attr("font-weight", "700").attr("fill", "var(--accent-gold)").text("Tính Chất Toán Học");

        const props = [
            "Ma phương chuẩn 3×3",
            "Hằng số = 15",
            "8 đường (3 hàng + 3 cột + 2 chéo)",
            "Đối xứng: p + đối(p) = 10",
            "Duy nhất (trừ phép quay/lật)",
            "Trung Cung (5) = bất biến"
        ];
        props.forEach((t, i) => {
            infoG.append("text")
                .attr("y", 24 + i * 18)
                .attr("font-size", "11px")
                .attr("fill", "var(--text-secondary)")
                .text("• " + t);
        });

        // Formula
        infoG.append("text").attr("y", 160).attr("font-size", "12px").attr("fill", "var(--accent-blue)").attr("font-family", "var(--font-mono)").text("opposite(p) = 10 − p");
        infoG.append("text").attr("y", 180).attr("font-size", "12px").attr("fill", "var(--accent-blue)").attr("font-family", "var(--font-mono)").text("∀ row,col,diag: Σ = 15");

        // Interaction hint
        infoG.append("text").attr("y", 220).attr("font-size", "10px").attr("fill", "var(--text-muted)").text("Click ô → highlight các đường qua ô đó");
    }

    function drawOppositionDiagram(g) {
        const cx = GRID_W + 140;
        const cy = GRID_H - 30;
        const r = 40;
        const oppG = g.append("g").attr("class", "lt-opp").attr("transform", `translate(${cx}, ${cy})`);

        oppG.append("text").attr("y", -r - 10).attr("text-anchor", "middle").attr("font-size", "10px").attr("fill", "var(--text-muted)").text("p ↔ 10−p");

        const pairs = [[1, 9], [2, 8], [3, 7], [4, 6]];
        pairs.forEach((pair, i) => {
            const angle = (i / pairs.length) * Math.PI;
            const x1 = r * Math.cos(angle), y1 = r * Math.sin(angle);
            const x2 = -x1, y2 = -y1;

            oppG.append("line")
                .attr("x1", x1).attr("y1", y1).attr("x2", x2).attr("y2", y2)
                .attr("stroke", "rgba(255,255,255,0.15)").attr("stroke-width", 1);

            [pair[0], pair[1]].forEach((val, j) => {
                const x = j === 0 ? x1 : x2;
                const y = j === 0 ? y1 : y2;
                const pal = LAC_THU.palaces[val];
                const c = NGU_HANH.colors[pal.element].bg;
                oppG.append("circle").attr("cx", x).attr("cy", y).attr("r", 12).attr("fill", c).attr("fill-opacity", 0.4).attr("stroke", c).attr("stroke-width", 1);
                oppG.append("text").attr("x", x).attr("y", y).attr("dy", "0.35em").attr("text-anchor", "middle").attr("font-size", "10px").attr("font-weight", "600").attr("fill", "#fff").text(val);
            });
        });
        // Center 5
        oppG.append("circle").attr("r", 10).attr("fill", "var(--accent-gold)").attr("fill-opacity", 0.3).attr("stroke", "var(--accent-gold)");
        oppG.append("text").attr("dy", "0.35em").attr("text-anchor", "middle").attr("font-size", "10px").attr("font-weight", "700").attr("fill", "#fff").text("5");
    }

    function toggleCell(val, g) {
        if (activeCell === val) {
            activeCell = null;
            resetHighlight(g);
            return;
        }
        activeCell = val;
        resetHighlight(g);

        // Find all lines containing this value
        const matchLines = LAC_THU.lines.filter(line => line.includes(val));
        const highlightVals = new Set();
        matchLines.forEach(line => line.forEach(v => highlightVals.add(v)));

        // Highlight
        for (let v = 1; v <= 9; v++) {
            const cell = g.select(`.lt-cell-${v}`);
            if (highlightVals.has(v)) {
                cell.select("rect").attr("fill-opacity", 0.5).attr("stroke", v === val ? "#FFD700" : "#fff").attr("stroke-width", v === val ? 3 : 2);
            } else {
                cell.select("rect").attr("fill-opacity", 0.08).attr("stroke", "rgba(255,255,255,0.05)");
                cell.selectAll("text").attr("opacity", 0.3);
            }
        }
    }

    function resetHighlight(g) {
        for (let v = 1; v <= 9; v++) {
            const pal = LAC_THU.palaces[v];
            const cell = g.select(`.lt-cell-${v}`);
            cell.select("rect").attr("fill-opacity", 0.25).attr("stroke", "rgba(255,255,255,0.2)").attr("stroke-width", 1.5);
            cell.selectAll("text").attr("opacity", 1);
        }
    }

    return { init };
})();
