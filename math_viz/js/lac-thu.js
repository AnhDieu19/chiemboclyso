/**
 * Lạc Thư (洛書) Magic Square — Interactive Visualization
 * ========================================================
 * Two modes:
 *   - Trung Quốc (Hậu Thiên): Nam on top, Ly=9, Đoài=7
 *   - Đại Việt: Bắc on top, Ly=7, Đoài=9, Thiên Can per palace
 *
 * Toggle via LacThuViz.toggleMode()
 */

const LacThuViz = (() => {
    const CELL_SIZE = 110;
    const GAP = 6;
    const GRID_W = CELL_SIZE * 3 + GAP * 4;
    const GRID_H = CELL_SIZE * 3 + GAP * 4;
    const MARGIN = { top: 55, right: 240, bottom: 55, left: 55 };

    let containerId, svg, activeCell = null;

    /* ── public init ── */
    function init(id) {
        containerId = id;
        render();
    }

    /* ── full (re)draw ── */
    function render() {
        const container = d3.select(containerId);
        container.select("svg").remove();
        activeCell = null;

        const cfg = _cfg();
        const totalW = GRID_W + MARGIN.left + MARGIN.right;
        const totalH = GRID_H + MARGIN.top + MARGIN.bottom;

        svg = container.append("svg")
            .attr("viewBox", `0 0 ${totalW} ${totalH}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%")
            .style("max-height", "560px");

        const g = svg.append("g")
            .attr("transform", `translate(${MARGIN.left}, ${MARGIN.top})`);

        drawCompass(g, cfg);
        drawGrid(g, cfg);
        drawSumLabels(g);
        drawInfoPanel(g, cfg);
        drawOppositionDiagram(g, cfg);
    }

    /* ── toggle mode & redraw ── */
    function toggleMode() {
        LacThuMode.toggle();
        render();
        return LacThuMode.current;
    }

    /* ── active config shortcut ── */
    function _cfg() {
        return LacThuMode.isTQ() ? LAC_THU_TQ : LAC_THU_DV;
    }

    /* ── Compass direction labels around grid ── */
    function drawCompass(g, cfg) {
        const cl = cfg.compassLabels;
        const midX = GRID_W / 2;
        const midY = GRID_H / 2;

        g.append("text").attr("x", midX).attr("y", -18)
            .attr("text-anchor", "middle").attr("font-size", "12px")
            .attr("font-weight", "600").attr("fill", "var(--accent-blue)")
            .text(cl.top);
        g.append("text").attr("x", midX).attr("y", GRID_H + 42)
            .attr("text-anchor", "middle").attr("font-size", "12px")
            .attr("font-weight", "600").attr("fill", "var(--accent-red)")
            .text(cl.bottom);
        g.append("text")
            .attr("transform", `translate(-18, ${midY}) rotate(-90)`)
            .attr("text-anchor", "middle").attr("font-size", "12px")
            .attr("font-weight", "600").attr("fill", "var(--accent-gold)")
            .text(cl.left);
        g.append("text")
            .attr("transform", `translate(${GRID_W + 18}, ${midY}) rotate(90)`)
            .attr("text-anchor", "middle").attr("font-size", "12px")
            .attr("font-weight", "600").attr("fill", "var(--accent-green)")
            .text(cl.right);
    }

    /* ── 3×3 grid cells ── */
    function drawGrid(g, cfg) {
        const gridG = g.append("g").attr("class", "lt-grid");
        const hasCan = cfg.mode === 'DV';

        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                const val = cfg.matrix[row][col];
                const palace = cfg.palaces[val];
                const x = GAP + col * (CELL_SIZE + GAP);
                const y = GAP + row * (CELL_SIZE + GAP);

                const cellG = gridG.append("g")
                    .attr("class", `lt-cell lt-cell-${val}`)
                    .attr("transform", `translate(${x}, ${y})`)
                    .style("cursor", "pointer")
                    .on("click", () => toggleCell(val, g, cfg))
                    .on("mouseenter", function () {
                        d3.select(this).select("rect.lt-bg").attr("stroke-width", 3).attr("stroke", "#fff");
                    })
                    .on("mouseleave", function () {
                        const isActive = activeCell === val;
                        d3.select(this).select("rect.lt-bg")
                            .attr("stroke-width", isActive ? 3 : 1.5)
                            .attr("stroke", isActive ? "#FFD700" : "rgba(255,255,255,0.2)");
                    });

                const hanhColor = NGU_HANH.colors[palace.element];

                // Background
                cellG.append("rect").attr("class", "lt-bg")
                    .attr("width", CELL_SIZE).attr("height", CELL_SIZE)
                    .attr("rx", 8)
                    .attr("fill", hanhColor.bg).attr("fill-opacity", 0.25)
                    .attr("stroke", "rgba(255,255,255,0.2)").attr("stroke-width", 1.5);

                // Number
                const displayNum = (val === 5 && hasCan) ? "5·10" : String(val);
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2)
                    .attr("y", hasCan ? 22 : (CELL_SIZE / 2 - 12))
                    .attr("text-anchor", "middle")
                    .attr("font-size", hasCan ? "24px" : "32px")
                    .attr("font-weight", "700")
                    .attr("fill", hanhColor.bg)
                    .text(displayNum);

                // Thiên Can (Đại Việt only)
                if (hasCan && palace.can) {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 42)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "15px").attr("font-weight", "700")
                        .attr("fill", "#fff")
                        .text(palace.can);
                }

                // Trigram name / symbol
                if (hasCan) {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 60)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "13px")
                        .attr("fill", "rgba(255,255,255,0.85)")
                        .text(palace.name);
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 78)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "18px")
                        .attr("fill", "rgba(255,255,255,0.5)")
                        .text(palace.symbol);
                } else {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", CELL_SIZE / 2 + 14)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "20px")
                        .attr("fill", "rgba(255,255,255,0.8)")
                        .text(palace.symbol);
                }

                // Direction label
                const dirY = hasCan ? 96 : (CELL_SIZE / 2 + 35);
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2).attr("y", dirY)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "10px")
                    .attr("fill", "var(--text-muted)")
                    .text(hasCan ? palace.dir : `${palace.name} · ${palace.dir}`);

                // Element badge (top-right) — trigram element
                cellG.append("rect")
                    .attr("x", CELL_SIZE - 32).attr("y", 4)
                    .attr("width", 28).attr("height", 16).attr("rx", 8)
                    .attr("fill", hanhColor.bg).attr("fill-opacity", 0.6);
                cellG.append("text")
                    .attr("x", CELL_SIZE - 18).attr("y", 15)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px").attr("font-weight", "600")
                    .attr("fill", hanhColor.fg)
                    .text(palace.element);

                // Hà Đồ element annotation (bottom-left) — show when differs from trigram
                if (palace.haDoElement && palace.haDoElement !== palace.element) {
                    const hdColor = NGU_HANH.colors[palace.haDoElement];
                    cellG.append("rect")
                        .attr("x", 4).attr("y", CELL_SIZE - 18)
                        .attr("width", 28).attr("height", 14).attr("rx", 6)
                        .attr("fill", hdColor.bg).attr("fill-opacity", 0.35);
                    cellG.append("text")
                        .attr("x", 18).attr("y", CELL_SIZE - 8)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "7px").attr("font-weight", "500")
                        .attr("fill", hdColor.bg)
                        .text(`H${palace.haDoElement}`);
                }
            }
        }
    }

    /* ── row/col sum labels ── */
    function drawSumLabels(g) {
        const sumG = g.append("g").attr("class", "lt-sums");
        for (let row = 0; row < 3; row++) {
            const y = GAP + row * (CELL_SIZE + GAP) + CELL_SIZE / 2;
            sumG.append("text")
                .attr("x", GRID_W + 8).attr("y", y).attr("dy", "0.35em")
                .attr("font-size", "14px").attr("font-weight", "600")
                .attr("fill", "var(--accent-gold)").text("= 15");
        }
        for (let col = 0; col < 3; col++) {
            const x = GAP + col * (CELL_SIZE + GAP) + CELL_SIZE / 2;
            sumG.append("text")
                .attr("x", x).attr("y", GRID_H + 20)
                .attr("text-anchor", "middle")
                .attr("font-size", "14px").attr("font-weight", "600")
                .attr("fill", "var(--accent-gold)").text("= 15");
        }
        sumG.append("text")
            .attr("x", GRID_W + 8).attr("y", GRID_H + 20)
            .attr("font-size", "11px").attr("fill", "var(--text-muted)")
            .text("↗↘ = 15");
    }

    /* ── info panel ── */
    function drawInfoPanel(g, cfg) {
        const infoX = GRID_W + 50;
        const infoG = g.append("g").attr("class", "lt-info")
            .attr("transform", `translate(${infoX}, 0)`);

        // Mode indicator
        infoG.append("text").attr("y", -10)
            .attr("font-size", "12px").attr("font-weight", "700")
            .attr("fill", cfg.mode === 'DV' ? "var(--accent-red)" : "var(--accent-blue)")
            .text(`⚙ ${cfg.modeName}`);
        infoG.append("text").attr("y", 8)
            .attr("font-size", "10px").attr("fill", "var(--text-muted)")
            .text(cfg.orientation);

        infoG.append("text").attr("y", 30)
            .attr("font-size", "14px").attr("font-weight", "700")
            .attr("fill", "var(--accent-gold)")
            .text("Tính Chất Toán Học");

        const props = [
            "Ma phương chuẩn 3×3",
            "Hằng số = 15",
            "8 đường (3 hàng + 3 cột + 2 chéo)",
            "Đối xứng: p + đối(p) = 10",
            "Duy nhất (trừ phép quay/lật)",
            "Trung Cung (5) = bất biến"
        ];
        if (cfg.mode === 'DV') {
            props.push("Bắc trên — chuẩn Đại Việt");
            props.push("Thiên Can gán mỗi Quái");
        }
        props.forEach((t, i) => {
            infoG.append("text")
                .attr("y", 50 + i * 18)
                .attr("font-size", "11px")
                .attr("fill", "var(--text-secondary)")
                .text("• " + t);
        });

        const formulaY = 50 + props.length * 18 + 12;
        infoG.append("text").attr("y", formulaY)
            .attr("font-size", "12px").attr("fill", "var(--accent-blue)")
            .attr("font-family", "var(--font-mono)")
            .text("opposite(p) = 10 − p");
        infoG.append("text").attr("y", formulaY + 20)
            .attr("font-size", "12px").attr("fill", "var(--accent-blue)")
            .attr("font-family", "var(--font-mono)")
            .text("∀ row,col,diag: Σ = 15");

        // Hà Đồ Sinh-Thành section
        const hdY = formulaY + 48;
        infoG.append("text").attr("y", hdY)
            .attr("font-size", "13px").attr("font-weight", "700")
            .attr("fill", "var(--accent-red)")
            .text("Hà Đồ — Sinh Thành");
        HA_DO.pairs.forEach((pair, i) => {
            const c = NGU_HANH.colors[pair.element];
            infoG.append("text").attr("y", hdY + 18 + i * 16)
                .attr("font-size", "10px")
                .attr("fill", c.bg)
                .text(`${pair.sinh}-${pair.thanh} ${pair.element} (${pair.dir}): ${pair.sinhType} ${pair.sinh} sinh, ${pair.thanhType} ${pair.thanh} thành`);
        });

        const tipY = hdY + 18 + 5 * 16 + 8;
        infoG.append("text").attr("y", tipY)
            .attr("font-size", "10px").attr("fill", "var(--text-muted)")
            .text("Click ô → highlight các đường qua ô đó");
    }

    /* ── opposition diagram ── */
    function drawOppositionDiagram(g, cfg) {
        const cx = GRID_W + 140;
        const cy = GRID_H - 30;
        const r = 40;
        const oppG = g.append("g").attr("class", "lt-opp")
            .attr("transform", `translate(${cx}, ${cy})`);

        oppG.append("text").attr("y", -r - 10).attr("text-anchor", "middle")
            .attr("font-size", "10px").attr("fill", "var(--text-muted)")
            .text("p ↔ 10−p");

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
                const pal = cfg.palaces[val];
                const c = NGU_HANH.colors[pal.element].bg;
                oppG.append("circle").attr("cx", x).attr("cy", y).attr("r", 12)
                    .attr("fill", c).attr("fill-opacity", 0.4)
                    .attr("stroke", c).attr("stroke-width", 1);
                oppG.append("text").attr("x", x).attr("y", y)
                    .attr("dy", "0.35em").attr("text-anchor", "middle")
                    .attr("font-size", "10px").attr("font-weight", "600")
                    .attr("fill", "#fff").text(val);
            });
        });

        oppG.append("circle").attr("r", 10)
            .attr("fill", "var(--accent-gold)").attr("fill-opacity", 0.3)
            .attr("stroke", "var(--accent-gold)");
        oppG.append("text").attr("dy", "0.35em").attr("text-anchor", "middle")
            .attr("font-size", "10px").attr("font-weight", "700")
            .attr("fill", "#fff").text("5");
    }

    /* ── cell click → highlight lines ── */
    function toggleCell(val, g, cfg) {
        if (activeCell === val) {
            activeCell = null;
            resetHighlight(g);
            return;
        }
        activeCell = val;
        resetHighlight(g);

        const matchLines = cfg.lines.filter(line => line.includes(val));
        const highlightVals = new Set();
        matchLines.forEach(line => line.forEach(v => highlightVals.add(v)));

        for (let v = 1; v <= 9; v++) {
            const cell = g.select(`.lt-cell-${v}`);
            if (highlightVals.has(v)) {
                cell.select("rect.lt-bg")
                    .attr("fill-opacity", 0.5)
                    .attr("stroke", v === val ? "#FFD700" : "#fff")
                    .attr("stroke-width", v === val ? 3 : 2);
            } else {
                cell.select("rect.lt-bg")
                    .attr("fill-opacity", 0.08)
                    .attr("stroke", "rgba(255,255,255,0.05)");
                cell.selectAll("text").attr("opacity", 0.3);
            }
        }
    }

    function resetHighlight(g) {
        for (let v = 1; v <= 9; v++) {
            const cell = g.select(`.lt-cell-${v}`);
            cell.select("rect.lt-bg")
                .attr("fill-opacity", 0.25)
                .attr("stroke", "rgba(255,255,255,0.2)")
                .attr("stroke-width", 1.5);
            cell.selectAll("text").attr("opacity", 1);
        }
    }

    return { init, toggleMode, render };
})();
