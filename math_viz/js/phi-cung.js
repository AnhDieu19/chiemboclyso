/**
 * Phi Cung (飛宮) Animation — ℤ₉ Rotation Demo
 * ===============================================
 * Animated demonstration of forward/reverse flight through 9 palaces.
 * User can select Cục number (1–9) and direction (Dương/Âm Độn).
 */

const PhiCungViz = (() => {

    let svg, gridG, pathG, infoG;
    let currentCuc = 1;
    let isForward = true;
    let animTimer = null;
    let step = 0;
    const CELL = 80;
    const GAP = 4;

    function init(containerId) {
        const container = d3.select(containerId);

        // Controls
        const controls = container.append("div").attr("class", "phi-controls");

        controls.append("label").text("Cục số: ");
        const cucSelect = controls.append("select").attr("class", "phi-select");
        for (let i = 1; i <= 9; i++) {
            cucSelect.append("option").attr("value", i).text(i).property("selected", i === 1);
        }

        controls.append("label").text(" Hướng: ");
        const dirSelect = controls.append("select").attr("class", "phi-select");
        dirSelect.append("option").attr("value", "duong").text("Dương Độn (thuận)").property("selected", true);
        dirSelect.append("option").attr("value", "am").text("Âm Độn (nghịch)");

        const btnPlay = controls.append("button").attr("class", "phi-btn").text("▶ Phi");
        const btnReset = controls.append("button").attr("class", "phi-btn phi-btn-sec").text("↺ Reset");

        // SVG area
        const totalW = CELL * 3 + GAP * 4 + 300;
        const totalH = CELL * 3 + GAP * 4 + 80;

        svg = container.append("svg")
            .attr("viewBox", `0 0 ${totalW} ${totalH}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%")
            .style("max-height", "420px");

        gridG = svg.append("g").attr("transform", "translate(20, 30)");
        pathG = svg.append("g").attr("transform", "translate(20, 30)");
        infoG = svg.append("g").attr("transform", `translate(${CELL * 3 + GAP * 4 + 40}, 30)`);

        drawStaticGrid();
        drawSequenceInfo();

        // Events
        cucSelect.on("change", function () { currentCuc = +this.value; resetAnim(); });
        dirSelect.on("change", function () { isForward = this.value === "duong"; resetAnim(); });
        btnPlay.on("click", () => startAnim());
        btnReset.on("click", () => resetAnim());
    }

    function drawStaticGrid() {
        gridG.selectAll("*").remove();

        for (let row = 0; row < 3; row++) {
            for (let col = 0; col < 3; col++) {
                const val = LAC_THU.matrix[row][col];
                const pal = LAC_THU.palaces[val];
                const x = GAP + col * (CELL + GAP);
                const y = GAP + row * (CELL + GAP);

                const cellG = gridG.append("g")
                    .attr("class", `phi-cell phi-cell-${val}`)
                    .attr("transform", `translate(${x}, ${y})`);

                cellG.append("rect")
                    .attr("width", CELL).attr("height", CELL).attr("rx", 6)
                    .attr("fill", "var(--bg-card)")
                    .attr("stroke", "rgba(255,255,255,0.15)")
                    .attr("stroke-width", 1);

                cellG.append("text")
                    .attr("x", CELL / 2).attr("y", CELL / 2 - 8)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "22px").attr("font-weight", "700")
                    .attr("fill", "rgba(255,255,255,0.3)")
                    .text(val);

                cellG.append("text")
                    .attr("class", `phi-star-${val}`)
                    .attr("x", CELL / 2).attr("y", CELL / 2 + 16)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "11px")
                    .attr("fill", "var(--text-muted)")
                    .text(pal.symbol + " " + pal.name);
            }
        }
    }

    function drawSequenceInfo() {
        infoG.selectAll("*").remove();

        infoG.append("text")
            .attr("font-size", "13px").attr("font-weight", "700").attr("fill", "var(--accent-gold)")
            .text("Chuỗi Phi Cung");

        const seqG = infoG.append("g").attr("transform", "translate(0, 24)");
        const seq = generateSequence();

        seq.forEach((s, i) => {
            const pal = LAC_THU.palaces[s];
            const y = i * 22;

            seqG.append("text")
                .attr("class", `phi-seq-${i}`)
                .attr("y", y)
                .attr("font-size", "11px")
                .attr("fill", "var(--text-secondary)")
                .html(`<tspan font-weight="600" fill="var(--accent-blue)">${i}.</tspan> Cung ${s} ${pal.symbol} ${pal.name}`);
        });

        // Formula
        const fY = seq.length * 22 + 20;
        infoG.append("text")
            .attr("y", 24 + fY)
            .attr("font-size", "10px")
            .attr("fill", "var(--text-muted)")
            .attr("font-family", "var(--font-mono)")
            .text(isForward
                ? `φ(${currentCuc}, n) = ((${currentCuc}−1+n) mod 9)+1`
                : `φ(${currentCuc}, n) = ((${currentCuc}−1−n) mod 9)+1`
            );
    }

    function generateSequence() {
        const seq = [];
        for (let n = 0; n <= 9; n++) {
            seq.push(CYCLIC_GROUPS.Z9.phi(currentCuc, n, isForward));
        }
        return seq;
    }

    function startAnim() {
        if (animTimer) clearInterval(animTimer);
        step = 0;
        const seq = generateSequence();
        highlightStep(seq, step);

        animTimer = setInterval(() => {
            step++;
            if (step >= seq.length) {
                clearInterval(animTimer);
                animTimer = null;
                return;
            }
            highlightStep(seq, step);
            drawArrow(seq, step);
        }, 600);
    }

    function highlightStep(seq, idx) {
        // Reset all
        for (let v = 1; v <= 9; v++) {
            gridG.select(`.phi-cell-${v} rect`)
                .attr("fill", "var(--bg-card)")
                .attr("stroke", "rgba(255,255,255,0.15)")
                .attr("stroke-width", 1);
        }

        // Highlight current
        const val = seq[idx];
        gridG.select(`.phi-cell-${val} rect`)
            .attr("fill", isForward ? "rgba(66,165,245,0.3)" : "rgba(239,83,80,0.3)")
            .attr("stroke", isForward ? "#42A5F5" : "#EF5350")
            .attr("stroke-width", 2.5);

        // Highlight sequence text
        infoG.selectAll("[class^='phi-seq-']").attr("opacity", 0.4);
        infoG.select(`.phi-seq-${idx}`).attr("opacity", 1);
    }

    function drawArrow(seq, idx) {
        if (idx < 1) return;
        const from = seq[idx - 1];
        const to = seq[idx];
        const pFrom = LAC_THU.palaces[from];
        const pTo = LAC_THU.palaces[to];

        const x1 = GAP + pFrom.col * (CELL + GAP) + CELL / 2;
        const y1 = GAP + pFrom.row * (CELL + GAP) + CELL / 2;
        const x2 = GAP + pTo.col * (CELL + GAP) + CELL / 2;
        const y2 = GAP + pTo.row * (CELL + GAP) + CELL / 2;

        pathG.append("line")
            .attr("x1", x1).attr("y1", y1).attr("x2", x2).attr("y2", y2)
            .attr("stroke", isForward ? "rgba(66,165,245,0.5)" : "rgba(239,83,80,0.5)")
            .attr("stroke-width", 2)
            .attr("marker-end", "url(#arrowhead)");

        // Ensure arrowhead marker exists
        if (!svg.select("#arrowhead").node()) {
            svg.append("defs").append("marker")
                .attr("id", "arrowhead").attr("viewBox", "0 0 10 10")
                .attr("refX", 8).attr("refY", 5)
                .attr("markerWidth", 6).attr("markerHeight", 6)
                .attr("orient", "auto-start-reverse")
                .append("path")
                .attr("d", "M 0 0 L 10 5 L 0 10 z")
                .attr("fill", isForward ? "#42A5F5" : "#EF5350");
        }
    }

    function resetAnim() {
        if (animTimer) { clearInterval(animTimer); animTimer = null; }
        step = 0;
        pathG.selectAll("*").remove();
        drawStaticGrid();
        drawSequenceInfo();
    }

    return { init };
})();
