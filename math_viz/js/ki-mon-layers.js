/**
 * Kỳ Môn 3-Layer System + Surjective Maps — Visualization
 * =========================================================
 * Shows Thiên Bàn (Cửu Tinh) / Nhân Bàn (Bát Môn) / Địa Bàn (fixed)
 * rotating independently on the Cửu Cung grid.
 * Also shows surjective maps: 12→9 (Chi→Cung), 16→9 (Thần→Cung).
 */

const KiMonViz = (() => {

    const W = 560, H = 400;
    const CELL = 70;
    const GRID_X_START = 20, GRID_Y_START = 30;
    const LAYER_GAP = 190;

    // Cửu Cung positions in 3×3 layout:  [4,9,2 / 3,5,7 / 8,1,6]
    const GRID_POS = {
        4: [0, 0], 9: [1, 0], 2: [2, 0],
        3: [0, 1], 5: [1, 1], 7: [2, 1],
        8: [0, 2], 1: [1, 2], 6: [2, 2],
    };

    let container;

    function init(containerId) {
        container = d3.select(containerId);

        // ── Section A: 3-Layer System ──
        container.append("h4").attr("class", "sub-title").text("A. Ba Tầng Bàn (天人地)");

        const ctrlA = container.append("div").attr("class", "tc-controls");
        ctrlA.append("label").text("Cục: ");
        const cucSelect = ctrlA.append("select").attr("class", "phi-select");
        for (let c = 1; c <= 9; c++) {
            cucSelect.append("option").attr("value", c).text(`Cục ${c}`);
        }
        ctrlA.append("label").text("  Kiểu: ");
        const dungSelect = ctrlA.append("select").attr("class", "phi-select");
        dungSelect.append("option").attr("value", "duong").text("Dương Độn (thuận)");
        dungSelect.append("option").attr("value", "am").text("Âm Độn (nghịch)");

        const svgLayers = container.append("svg")
            .attr("viewBox", `0 0 ${LAYER_GAP * 3 + 40} ${H}`)
            .attr("class", "km-svg");

        const layerInfoDiv = container.append("div").attr("class", "km-info");

        cucSelect.on("change", () => drawLayers(+cucSelect.node().value, dungSelect.node().value, svgLayers, layerInfoDiv));
        dungSelect.on("change", () => drawLayers(+cucSelect.node().value, dungSelect.node().value, svgLayers, layerInfoDiv));
        drawLayers(1, "duong", svgLayers, layerInfoDiv);

        // ── Section B: Surjective Maps ──
        container.append("h4").attr("class", "sub-title").text("B. Ánh Xạ Toàn Ánh (Surjective Maps)");
        const svgSurj = container.append("svg")
            .attr("viewBox", `0 0 860 380`)
            .attr("class", "km-svg surj-svg");
        drawSurjections(svgSurj);
    }

    /* ── Draw 3 Layers ── */
    function drawLayers(cuc, direction, svg, infoDiv) {
        svg.selectAll("*").remove();
        const isForward = direction === "duong";
        const LAYERS = KI_MON_LAYERS.layers;

        LAYERS.forEach((layer, li) => {
            const ox = GRID_X_START + li * LAYER_GAP;
            const oy = GRID_Y_START;
            const color = ["#4FC3F7", "#FFD54F", "#FF8A65"][li];
            const g = svg.append("g").attr("transform", `translate(${ox},${oy})`);

            // Title
            g.append("text")
                .attr("x", CELL * 1.5).attr("y", -10)
                .attr("text-anchor", "middle")
                .attr("fill", color)
                .attr("font-size", "13px")
                .attr("font-weight", "bold")
                .text(layer.name);

            // Draw 9 cells
            for (let p = 1; p <= 9; p++) {
                const [col, row] = GRID_POS[p];
                const x = col * CELL;
                const y = row * CELL;

                g.append("rect")
                    .attr("x", x).attr("y", y)
                    .attr("width", CELL).attr("height", CELL)
                    .attr("fill", "var(--bg-secondary)")
                    .attr("stroke", color)
                    .attr("stroke-width", 1)
                    .attr("rx", 4);

                // What's in this palace?
                let content, subContent;
                if (li === 2) {
                    // Địa Bàn: fixed Cửu Cung + Bát Thần
                    content = `${p}`;
                    subContent = LAC_THU.palaces[p].symbol;
                } else {
                    // Thiên Bàn or Nhân Bàn: rotated based on Cục
                    const phiPos = phiCung(cuc, p, isForward);
                    const idx = phiPos - 1;
                    const item = (idx < layer.labels.length) ? layer.labels[idx] : `(${phiPos})`;
                    content = item;
                    subContent = `cung ${phiPos}`;
                }

                g.append("text")
                    .attr("x", x + CELL / 2).attr("y", y + CELL / 2 - 2)
                    .attr("text-anchor", "middle")
                    .attr("fill", "var(--text-primary)")
                    .attr("font-size", "12px")
                    .attr("font-weight", "bold")
                    .text(content);

                g.append("text")
                    .attr("x", x + CELL / 2).attr("y", y + CELL / 2 + 14)
                    .attr("text-anchor", "middle")
                    .attr("fill", "var(--text-muted)")
                    .attr("font-size", "9px")
                    .text(subContent);
            }
        });

        // Info
        infoDiv.html(`
            <div class="mod-math-note">
                <strong>Cơ chế:</strong> Cục số ${cuc}, ${isForward ? "Dương Độn (thuận phi)" : "Âm Độn (nghịch phi)"}<br>
                Địa Bàn cố định (Lạc Thư). Thiên Bàn (Cửu Tinh) và Nhân Bàn (Bát Môn) xoay theo Phi Cung.<br>
                Công thức: ((s − 1) ${isForward ? "+" : "−"} n) mod 9 + 1, với s = cung gốc, n = cục số<br>
                <em>Chồng 3 tầng lên nhau → mỗi cung có: Địa Bàn (cung) + Thiên Bàn (sao) + Nhân Bàn (môn)</em>
            </div>
        `);
    }

    function phiCung(cuc, palace, forward) {
        if (palace === 5) return 5; // Trung Cung stays
        let shift = cuc - 1;
        let result;
        if (forward) {
            result = ((palace - 1 + shift) % 9) + 1;
        } else {
            result = ((palace - 1 - shift % 9 + 9) % 9) + 1;
        }
        return result === 0 ? 9 : result;
    }

    /* ── Draw Surjective Maps ── */
    function drawSurjections(svg) {
        // Wrap chi_to_9 with from/to
        const s1 = { ...SURJECTIONS.chi_to_9, from: 12, to: 9 };
        const s2 = { ...SURJECTIONS.ring16_to_9, from: 16, to: 8 };

        // Map 1: Chi (12) → Cung (9)
        drawOneMap(svg, 0, s1, "ℤ₁₂ → ℤ₉", "12 Địa Chi → 9 Cung", "#4FC3F7", "#AB47BC");

        // Map 2: Ring16 (16) → Cung (8)
        drawOneMap(svg, 440, s2, "ℤ₁₆ → ℤ₈", "16 Thần → 8 Cung Ngoài", "#FFD54F", "#AB47BC");
    }

    function drawOneMap(svg, ox, surj, formula, label, leftColor, rightColor) {
        const g = svg.append("g").attr("transform", `translate(${ox}, 10)`);

        // Title
        g.append("text")
            .attr("x", 200).attr("y", 0)
            .attr("text-anchor", "middle")
            .attr("fill", "var(--text-primary)")
            .attr("font-size", "14px")
            .attr("font-weight", "bold")
            .text(`${formula}: ${label}`);

        const leftX = 50, rightX = 340, startY = 30;
        const leftN = surj.from;
        const rightN = surj.to;
        const leftSpacing = Math.min(22, 340 / leftN);
        const rightSpacing = Math.min(30, 340 / rightN);

        // Left nodes
        for (let i = 0; i < leftN; i++) {
            const y = startY + i * leftSpacing;
            g.append("circle")
                .attr("cx", leftX).attr("cy", y)
                .attr("r", 8)
                .attr("fill", leftColor)
                .attr("opacity", 0.7);
            g.append("text")
                .attr("x", leftX - 20).attr("y", y + 4)
                .attr("text-anchor", "middle")
                .attr("fill", "var(--text-muted)")
                .attr("font-size", "10px")
                .text(i);
        }

        // Right nodes
        for (let j = 1; j <= rightN; j++) {
            const y = startY + (j - 1) * rightSpacing;
            g.append("circle")
                .attr("cx", rightX).attr("cy", y)
                .attr("r", 10)
                .attr("fill", rightColor)
                .attr("opacity", 0.7);
            g.append("text")
                .attr("x", rightX + 22).attr("y", y + 4)
                .attr("text-anchor", "start")
                .attr("fill", "var(--text-muted)")
                .attr("font-size", "10px")
                .text(`Cung ${j}`);
        }

        // Arrows from mapping
        surj.map.forEach((target, source) => {
            const y1 = startY + source * leftSpacing;
            const y2 = startY + (target - 1) * rightSpacing;
            g.append("line")
                .attr("x1", leftX + 10).attr("y1", y1)
                .attr("x2", rightX - 12).attr("y2", y2)
                .attr("stroke", "var(--text-muted)")
                .attr("stroke-width", 0.7)
                .attr("opacity", 0.4);
        });

        // Highlight shared pairs if any
        if (surj.sharedPairs) {
            const chiLabels = CYCLIC_GROUPS.Z12.labels;
            surj.sharedPairs.forEach(pair => {
                const idxA = chiLabels.indexOf(pair.chi[0]);
                const idxB = chiLabels.indexOf(pair.chi[1]);
                if (idxA < 0 || idxB < 0) return;
                const y1 = startY + idxA * leftSpacing;
                const y2 = startY + idxB * leftSpacing;
                g.append("line")
                    .attr("x1", leftX - 10).attr("y1", y1)
                    .attr("x2", leftX - 10).attr("y2", y2)
                    .attr("stroke", "#E91E63")
                    .attr("stroke-width", 2);
                g.append("text")
                    .attr("x", leftX - 35).attr("y", (y1 + y2) / 2 + 3)
                    .attr("text-anchor", "middle")
                    .attr("fill", "#E91E63")
                    .attr("font-size", "8px")
                    .text(`cung ${pair.palace}`);
            });
        }
    }

    return { init };
})();
