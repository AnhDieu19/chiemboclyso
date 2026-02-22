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
    const MARGIN = { top: 55, right: 280, bottom: 120, left: 55 };

    let containerId, svg, activeCell = null;

    /* ── public init ── */
    function init(id) {
        containerId = id;
        render();
    }

    /* ── full (re)draw ── */
    function render() {
        const container = d3.select(containerId);
        container.selectAll("svg").remove();
        container.selectAll(".transform-title").remove();
        container.selectAll(".lt-sub-panels").remove();
        activeCell = null;

        const cfg = _cfg();
        const totalW = GRID_W + MARGIN.left + MARGIN.right;
        // Right panel extends much further than grid in TQ mode
        const rightPanelH = cfg.mode === 'TQ' ? 660 : 380;
        const leftPanelH = GRID_H + MARGIN.bottom;  // grid + opposition + sums
        const totalH = MARGIN.top + Math.max(leftPanelH, rightPanelH) + 20;

        svg = container.append("svg")
            .attr("viewBox", `0 0 ${totalW} ${totalH}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%");

        const g = svg.append("g")
            .attr("transform", `translate(${MARGIN.left}, ${MARGIN.top})`);

        drawCompass(g, cfg);
        drawGrid(g, cfg);
        drawSumLabels(g);
        drawOppositionDiagram(g, cfg);  // below grid, before info
        drawInfoPanel(g, cfg);

        // Transformation diagram (Viên Như formula)
        drawTransformDiagram(container, cfg);
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
                // TQ mode: use Phi Tinh star color for background
                const bgFill = hasCan ? hanhColor.bg : (palace.color || hanhColor.bg);
                const bgOpacity = hasCan ? 0.25 : 0.35;

                // Background
                cellG.append("rect").attr("class", "lt-bg")
                    .attr("width", CELL_SIZE).attr("height", CELL_SIZE)
                    .attr("rx", 8)
                    .attr("fill", bgFill).attr("fill-opacity", bgOpacity)
                    .attr("stroke", "rgba(255,255,255,0.2)").attr("stroke-width", 1.5);

                // Number
                const displayNum = (val === 5 && hasCan) ? "5·10" : String(val);
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2)
                    .attr("y", hasCan ? 20 : 26)
                    .attr("text-anchor", "middle")
                    .attr("font-size", hasCan ? "22px" : "28px")
                    .attr("font-weight", "700")
                    .attr("fill", hasCan ? hanhColor.bg : (palace.color || hanhColor.bg))
                    .text(displayNum);

                // Star name — Cửu Tinh (e.g. "Nhất Bạch")
                if (palace.star) {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2)
                        .attr("y", hasCan ? 38 : 46)
                        .attr("text-anchor", "middle")
                        .attr("font-size", hasCan ? "11px" : "14px")
                        .attr("font-weight", "600")
                        .attr("fill", hasCan ? "rgba(255,255,255,0.7)" : "#fff")
                        .text(palace.star);
                }

                // Thiên Can (Đại Việt only)
                if (hasCan && palace.can) {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 54)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "14px").attr("font-weight", "700")
                        .attr("fill", "#fff")
                        .text(palace.can);
                }

                // Trigram name / symbol
                if (hasCan) {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 70)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "12px")
                        .attr("fill", "rgba(255,255,255,0.85)")
                        .text(palace.name);
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 86)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "16px")
                        .attr("fill", "rgba(255,255,255,0.5)")
                        .text(palace.symbol);
                } else {
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 66)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "12px")
                        .attr("fill", "rgba(255,255,255,0.85)")
                        .text(palace.name);
                    cellG.append("text")
                        .attr("x", CELL_SIZE / 2).attr("y", 84)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "18px")
                        .attr("fill", "rgba(255,255,255,0.5)")
                        .text(palace.symbol);
                }

                // Element badge (top-right) — Hậu Thiên trigram element
                cellG.append("rect")
                    .attr("x", CELL_SIZE - 36).attr("y", 4)
                    .attr("width", 32).attr("height", 16).attr("rx", 8)
                    .attr("fill", hanhColor.bg).attr("fill-opacity", 0.6);
                cellG.append("text")
                    .attr("x", CELL_SIZE - 20).attr("y", 15)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px").attr("font-weight", "600")
                    .attr("fill", hanhColor.fg)
                    .text(palace.element);

                // Hà Đồ element badge (bottom-left) — always show
                if (palace.haDoElement) {
                    const hdColor = NGU_HANH.colors[palace.haDoElement];
                    const isSame = palace.haDoElement === palace.element;
                    const badgeW = isSame ? 28 : 42;
                    cellG.append("rect")
                        .attr("x", 3).attr("y", CELL_SIZE - 20)
                        .attr("width", badgeW).attr("height", 16).attr("rx", 6)
                        .attr("fill", hdColor.bg).attr("fill-opacity", isSame ? 0.25 : 0.5);
                    cellG.append("text")
                        .attr("x", 3 + badgeW / 2).attr("y", CELL_SIZE - 9)
                        .attr("text-anchor", "middle")
                        .attr("font-size", "7px").attr("font-weight", "600")
                        .attr("fill", isSame ? hdColor.bg : "#fff")
                        .text(isSame ? `HĐ` : `HĐ ${palace.haDoElement}`);
                }

                // Direction label — drawn after badges so text is on top
                cellG.append("text")
                    .attr("x", CELL_SIZE / 2).attr("y", hasCan ? 102 : 100)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "9px")
                    .attr("fill", "var(--text-muted)")
                    .text(palace.dir);
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

        // Cửu Tinh (Nine Stars) section — TQ mode emphasis
        if (cfg.mode === 'TQ') {
            const csY = formulaY + 44;
            infoG.append("text").attr("y", csY)
                .attr("font-size", "13px").attr("font-weight", "700")
                .attr("fill", "var(--accent-gold)")
                .text("Cửu Tinh — 九星 Phi Tinh");
            for (let i = 1; i <= 9; i++) {
                const st = CUU_TINH[i];
                infoG.append("circle")
                    .attr("cx", 4).attr("cy", csY + 10 + i * 14)
                    .attr("r", 4)
                    .attr("fill", st.starColor).attr("fill-opacity", 0.8);
                infoG.append("text").attr("x", 14).attr("y", csY + 14 + i * 14)
                    .attr("font-size", "9px")
                    .attr("fill", "var(--text-secondary)")
                    .text(`${st.hanStar} ${st.star} — ${st.fullName}`);
            }

            // Element comparison table: Hậu Thiên vs Hà Đồ
            const cmpY = csY + 10 * 14 + 10;
            infoG.append("text").attr("y", cmpY)
                .attr("font-size", "11px").attr("font-weight", "700")
                .attr("fill", "var(--accent-blue)")
                .text("Ngũ Hành: Hậu Thiên ↔ Hà Đồ");
            infoG.append("text").attr("y", cmpY + 14)
                .attr("font-size", "8px")
                .attr("fill", "var(--text-muted)")
                .text("Số  Hậu Thiên  Hà Đồ");
            for (let i = 1; i <= 9; i++) {
                const p = cfg.palaces[i];
                const htC = NGU_HANH.colors[p.element];
                const hdC = NGU_HANH.colors[p.haDoElement];
                const isSame = p.element === p.haDoElement;
                const y = cmpY + 26 + (i - 1) * 13;
                // number
                infoG.append("text").attr("x", 0).attr("y", y)
                    .attr("font-size", "9px").attr("font-weight", "600")
                    .attr("fill", "#fff")
                    .text(i);
                // Hậu Thiên element
                infoG.append("text").attr("x", 20).attr("y", y)
                    .attr("font-size", "9px").attr("font-weight", "500")
                    .attr("fill", htC.bg)
                    .text(p.element);
                // arrow
                infoG.append("text").attr("x", 55).attr("y", y)
                    .attr("font-size", "8px")
                    .attr("fill", isSame ? "var(--text-muted)" : "var(--accent-gold)")
                    .text(isSame ? "=" : "≠");
                // Hà Đồ element
                infoG.append("text").attr("x", 68).attr("y", y)
                    .attr("font-size", "9px").attr("font-weight", "500")
                    .attr("fill", hdC.bg)
                    .text(p.haDoElement);
            }
        }

        // Hà Đồ Sinh-Thành section
        const hdY = cfg.mode === 'TQ' ? (formulaY + 44 + 10 * 14 + 10 + 9 * 13 + 40) : (formulaY + 48);
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

    /* ── opposition diagram (below grid) ── */
    function drawOppositionDiagram(g, cfg) {
        const cx = GRID_W / 2;
        const cy = GRID_H + 75;  // below grid + sum labels
        const r = 36;
        const oppG = g.append("g").attr("class", "lt-opp")
            .attr("transform", `translate(${cx}, ${cy})`);

        oppG.append("text").attr("y", -r - 12).attr("text-anchor", "middle")
            .attr("font-size", "11px").attr("font-weight", "600")
            .attr("fill", "var(--accent-gold)")
            .text("Đối Xứng: p ↔ 10−p");

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
        const defaultOpacity = LacThuMode.isTQ() ? 0.35 : 0.25;
        for (let v = 1; v <= 9; v++) {
            const cell = g.select(`.lt-cell-${v}`);
            cell.select("rect.lt-bg")
                .attr("fill-opacity", defaultOpacity)
                .attr("stroke", "rgba(255,255,255,0.2)")
                .attr("stroke-width", 1.5);
            cell.selectAll("text").attr("opacity", 1);
        }
    }

    /* ═══════════ Viên Như Transform Diagram ═══════════ */

    /**
     * Draws a second SVG showing the Hà Đồ ↔ Lạc Thư transformation.
     * Left: Hà Đồ 4-axis diagram.  Right: Lạc Thư 4-axis diagram.
     * Center: 4 transformation steps with arrows.
     */
    function drawTransformDiagram(container, cfg) {
        const T = HA_DO_LAC_THU_TRANSFORM;
        const W = 700, H = 420;
        const axisR = 100;  // radius of axis diagrams

        // Title
        container.append("div").attr("class", "transform-title")
            .style("text-align", "center").style("margin-top", "18px")
            .style("font-size", "15px").style("font-weight", "700")
            .style("color", "var(--accent-gold)")
            .html("Công thức Hà Đồ ↔ Lạc Thư — Viên Như");

        const svg2 = container.append("svg")
            .attr("class", "transform-svg")
            .attr("viewBox", `0 0 ${W} ${H}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%")
            .style("max-height", "440px")
            .style("margin-top", "6px");

        // Defs: arrow markers
        const defs = svg2.append("defs");
        ["#42A5F5", "#FFD700", "#66BB6A", "#FF7043"].forEach((color, i) => {
            defs.append("marker").attr("id", `arrow-step-${i}`)
                .attr("viewBox", "0 0 10 6").attr("refX", 9).attr("refY", 3)
                .attr("markerWidth", 8).attr("markerHeight", 6).attr("orient", "auto")
                .append("path").attr("d", "M0,0 L10,3 L0,6 Z").attr("fill", color);
        });
        // Generic white arrow
        defs.append("marker").attr("id", "arrow-white")
            .attr("viewBox", "0 0 10 6").attr("refX", 9).attr("refY", 3)
            .attr("markerWidth", 7).attr("markerHeight", 5).attr("orient", "auto")
            .append("path").attr("d", "M0,0 L10,3 L0,6 Z").attr("fill", "rgba(255,255,255,0.6)");

        /* ── Left: Hà Đồ axes ── */
        const hdCx = 140, hdCy = H / 2;
        const hdG = svg2.append("g").attr("transform", `translate(${hdCx}, ${hdCy})`);
        drawAxisCircle(hdG, T.haDo.axes, axisR, "Hà Đồ", "Tiên Thiên Bát Quái", true);

        /* ── Right: Lạc Thư axes ── */
        const ltCx = W - 140, ltCy = H / 2;
        const ltG = svg2.append("g").attr("transform", `translate(${ltCx}, ${ltCy})`);
        drawAxisCircle(ltG, T.lacThu.axes, axisR, "Lạc Thư", "Hậu Thiên Bát Quái", false);

        /* ── Center: 4 transformation steps ── */
        const stepColors = ["#42A5F5", "#FFD700", "#66BB6A", "#FF7043"];
        const stepX = W / 2;
        const stepsG = svg2.append("g").attr("transform", `translate(${stepX}, 30)`);

        // Big arrow HĐ → LT
        svg2.append("line")
            .attr("x1", hdCx + axisR + 20).attr("y1", hdCy)
            .attr("x2", ltCx - axisR - 20).attr("y2", ltCy)
            .attr("stroke", "rgba(255,255,255,0.1)").attr("stroke-width", 2)
            .attr("stroke-dasharray", "6,4")
            .attr("marker-end", "url(#arrow-white)");
        svg2.append("text")
            .attr("x", stepX).attr("y", hdCy + 2)
            .attr("text-anchor", "middle")
            .attr("font-size", "9px").attr("fill", "var(--text-muted)")
            .text("Ngoại tại → thuận KĐH");

        // Title for steps
        stepsG.append("text")
            .attr("text-anchor", "middle")
            .attr("font-size", "12px").attr("font-weight", "700")
            .attr("fill", "var(--accent-blue)")
            .text("4 Bước Biến Đổi");

        T.haDoToLacThu.steps.forEach((s, i) => {
            const y = 22 + i * 52;
            const color = stepColors[i];

            // Step box
            stepsG.append("rect")
                .attr("x", -105).attr("y", y)
                .attr("width", 210).attr("height", 42).attr("rx", 6)
                .attr("fill", color).attr("fill-opacity", 0.1)
                .attr("stroke", color).attr("stroke-width", 1).attr("stroke-opacity", 0.4);

            // Step number
            stepsG.append("circle")
                .attr("cx", -85).attr("cy", y + 21)
                .attr("r", 10)
                .attr("fill", color).attr("fill-opacity", 0.25)
                .attr("stroke", color).attr("stroke-width", 1);
            stepsG.append("text")
                .attr("x", -85).attr("y", y + 25)
                .attr("text-anchor", "middle")
                .attr("font-size", "11px").attr("font-weight", "700")
                .attr("fill", color)
                .text(s.step);

            // Formula label
            stepsG.append("text")
                .attr("x", -65).attr("y", y + 15)
                .attr("font-size", "10px").attr("font-weight", "600")
                .attr("fill", "#fff")
                .text(`${s.from.name}(${s.from.quai.join("-")}) + ${s.to.name}(${s.to.quai.join("-")})`);

            // Result
            stepsG.append("text")
                .attr("x", -65).attr("y", y + 32)
                .attr("font-size", "9px")
                .attr("fill", color)
                .text(`→ ${s.to.name} = ${s.result.quai.join("-")} (${s.result.rotation})`);
        });

        /* ── Bottom: Number rules ── */
        const rulesG = svg2.append("g").attr("transform", `translate(${W / 2}, ${H - 50})`);

        // Viên / Phương rule
        const rules = T.numberRules;
        const ruleItems = [
            { label: "Viên ○", nums: rules.placement.vien.numbers.join(","), type: "Dương", color: "#42A5F5" },
            { label: "Phương □", nums: rules.placement.phuong.numbers.join(","), type: "Âm", color: "#FF7043" },
            { label: "Trung ◎", nums: "5", type: "Cố định", color: "#FFD700" },
            { label: "Đối xung", nums: "Σ = 10", type: "10 ẩn", color: "#66BB6A" },
        ];
        ruleItems.forEach((r, i) => {
            const x = (i - 1.5) * 140;
            rulesG.append("text")
                .attr("x", x).attr("y", 0)
                .attr("text-anchor", "middle")
                .attr("font-size", "10px").attr("font-weight", "600")
                .attr("fill", r.color)
                .text(r.label);
            rulesG.append("text")
                .attr("x", x).attr("y", 16)
                .attr("text-anchor", "middle")
                .attr("font-size", "10px")
                .attr("fill", "var(--text-secondary)")
                .text(`${r.nums} — ${r.type}`);
        });

        // Thể/Dụng comparison
        const tdG = svg2.append("g").attr("transform", `translate(${W / 2}, ${H - 10})`);
        tdG.append("text").attr("x", -140).attr("text-anchor", "middle")
            .attr("font-size", "9px").attr("fill", "var(--text-muted)")
            .text(`HĐ: ${T.haDo.the.desc} · ${T.haDo.dung.desc}`);
        tdG.append("text").attr("x", 140).attr("text-anchor", "middle")
            .attr("font-size", "9px").attr("fill", "var(--text-muted)")
            .text(`LT: ${T.lacThu.the.desc} · ${T.lacThu.dung.desc}`);
    }

    /**
     * Draw an axis circle diagram: 4 axes through center with quái + numbers
     * @param {d3 group} g — group element (already translated)
     * @param {Array} axes — array of axis objects from HA_DO_LAC_THU_TRANSFORM
     * @param {number} r — radius
     * @param {string} title — diagram title
     * @param {string} subtitle — sub label
     * @param {boolean} isHaDo — true for Hà Đồ
     */
    function drawAxisCircle(g, axes, r, title, subtitle, isHaDo) {
        const axisColors = ["#42A5F5", "#FF7043", "#66BB6A", "#AB47BC"];
        // Angles: Tung=vertical(90°), Hoành=horizontal(0°), Tả=left diag(135°), Hữu=right diag(45°)
        const axisAngles = isHaDo
            ? [Math.PI / 2, 0, (3 * Math.PI) / 4, Math.PI / 4]       // HĐ: Tung↕, Hoành↔, Tả⟋, Hữu⟍
            : [Math.PI / 2, 0, (3 * Math.PI) / 4, Math.PI / 4];      // LT: same axis directions

        // Title
        g.append("text")
            .attr("y", -r - 24)
            .attr("text-anchor", "middle")
            .attr("font-size", "13px").attr("font-weight", "700")
            .attr("fill", isHaDo ? "var(--accent-red)" : "var(--accent-blue)")
            .text(title);
        g.append("text")
            .attr("y", -r - 10)
            .attr("text-anchor", "middle")
            .attr("font-size", "9px")
            .attr("fill", "var(--text-muted)")
            .text(subtitle);

        // Outer circle
        g.append("circle")
            .attr("r", r)
            .attr("fill", "none")
            .attr("stroke", "rgba(255,255,255,0.1)").attr("stroke-width", 1);

        // Center dot
        g.append("circle")
            .attr("r", 4)
            .attr("fill", "#FFB300").attr("fill-opacity", 0.5);
        g.append("text")
            .attr("dy", "0.35em")
            .attr("text-anchor", "middle")
            .attr("font-size", "7px").attr("fill", "#fff")
            .text("5");

        // Draw each axis
        axes.forEach((axis, i) => {
            const angle = axisAngles[i];
            const color = axisColors[i];
            const cos = Math.cos(angle), sin = Math.sin(angle);

            // Axis line
            g.append("line")
                .attr("x1", -r * cos).attr("y1", r * sin)   // note: SVG y is inverted
                .attr("x2", r * cos).attr("y2", -r * sin)
                .attr("stroke", color).attr("stroke-width", 1.5)
                .attr("stroke-opacity", 0.6);

            // YinYang indicator
            const yyText = axis.yinYang === "Dương" ? "☰" : "☷";

            // Quái labels at endpoints
            if (axis.quai.length >= 2) {
                // End 1 (positive direction)
                const ex1 = (r + 18) * cos, ey1 = -(r + 18) * sin;
                g.append("text")
                    .attr("x", ex1).attr("y", ey1)
                    .attr("dy", "0.35em")
                    .attr("text-anchor", "middle")
                    .attr("font-size", "10px").attr("font-weight", "600")
                    .attr("fill", color)
                    .text(axis.quaiSymbol ? axis.quaiSymbol[0] : axis.quai[0]);
                g.append("text")
                    .attr("x", ex1).attr("y", ey1 + 12)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px")
                    .attr("fill", "var(--text-secondary)")
                    .text(axis.quai[0]);

                // End 2 (negative direction)
                const ex2 = -(r + 18) * cos, ey2 = (r + 18) * sin;
                g.append("text")
                    .attr("x", ex2).attr("y", ey2)
                    .attr("dy", "0.35em")
                    .attr("text-anchor", "middle")
                    .attr("font-size", "10px").attr("font-weight", "600")
                    .attr("fill", color)
                    .text(axis.quaiSymbol ? axis.quaiSymbol[1] : axis.quai[1]);
                g.append("text")
                    .attr("x", ex2).attr("y", ey2 + 12)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px")
                    .attr("fill", "var(--text-secondary)")
                    .text(axis.quai[1]);
            }

            // Number pairs along axis (if any)
            if (axis.numbers && axis.numbers.length > 0) {
                axis.numbers.forEach((pair, pi) => {
                    const t = 0.45 + pi * 0.3;  // position along axis
                    const nx = t * r * cos * (pi === 0 ? 1 : -1);
                    const ny = -t * r * sin * (pi === 0 ? 1 : -1);
                    g.append("text")
                        .attr("x", nx + (sin > 0.5 ? 10 : -10) * (Math.abs(cos) < 0.5 ? 0 : 1))
                        .attr("y", ny + (Math.abs(sin) < 0.5 ? -8 : 0))
                        .attr("text-anchor", "middle")
                        .attr("font-size", "9px").attr("font-weight", "600")
                        .attr("fill", "#fff").attr("opacity", 0.7)
                        .text(pair.join("-"));
                });
            }

            // Axis label (small, near center)
            const labelDist = 35;
            const perpAngle = angle + Math.PI / 2;
            const lx = labelDist * Math.cos(perpAngle) * 0.4;
            const ly = -labelDist * Math.sin(perpAngle) * 0.4;
            g.append("text")
                .attr("x", lx).attr("y", ly)
                .attr("text-anchor", "middle")
                .attr("font-size", "7px")
                .attr("fill", color).attr("opacity", 0.7)
                .text(`${axis.name}(${axis.yinYang})`);
        });
    }

    return { init, toggleMode, render };
})();
