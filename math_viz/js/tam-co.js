/**
 * Tam Cơ Multi-Rate System — Visualization
 * ==========================================
 * Shows 3 concentric ℤ₁₂ rings rotating at different speeds:
 *   Quân Cơ (30yr), Thần Cơ (3yr), Dân Cơ (1yr)
 */

const TamCoViz = (() => {

    const W = 500, H = 500, cx = W / 2, cy = H / 2;
    const RADII = [190, 140, 90];
    const COLORS = ["#4FC3F7", "#FFD54F", "#FF8A65"];
    const LABELS = ["Quân Cơ (÷30)", "Thần Cơ (÷3)", "Dân Cơ (÷1)"];
    const CHI_NAMES = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
                       "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"];
    let container, svg;

    function init(containerId) {
        container = d3.select(containerId);

        // Controls
        const ctrl = container.append("div").attr("class", "tc-controls");
        ctrl.append("label").text("Tích Tuế: ");
        const yearInput = ctrl.append("input")
            .attr("type", "number")
            .attr("class", "mod-input")
            .attr("value", "50")
            .attr("min", "0")
            .attr("max", "3600");
        const btnCalc = ctrl.append("button").attr("class", "phi-btn").text("Tính");

        // SVG
        svg = container.append("svg")
            .attr("viewBox", `0 0 ${W} ${H}`)
            .attr("class", "tc-svg");

        // Legend
        const legend = container.append("div").attr("class", "tc-legend");
        TAM_CO.clocks.forEach((co, i) => {
            legend.append("span").attr("class", "tc-legend-item")
                .html(`<span class="tc-dot" style="background:${COLORS[i]}"></span> ${co.name} — tốc ${co.period} năm/bước　`);
        });

        // Info panel
        const infoDiv = container.append("div").attr("class", "tc-info");

        // Events
        btnCalc.on("click", () => draw(+yearInput.node().value, infoDiv));
        yearInput.on("keypress", (e) => { if (e.key === "Enter") draw(+yearInput.node().value, infoDiv); });

        draw(50, infoDiv);
    }

    function draw(tichTue, infoDiv) {
        svg.selectAll("*").remove();

        // Background circles
        RADII.forEach((r, i) => {
            svg.append("circle")
                .attr("cx", cx).attr("cy", cy).attr("r", r)
                .attr("fill", "none")
                .attr("stroke", COLORS[i])
                .attr("stroke-width", 1)
                .attr("stroke-dasharray", "4,4")
                .attr("opacity", 0.3);
        });

        // Center label
        svg.append("text")
            .attr("x", cx).attr("y", cy - 10)
            .attr("text-anchor", "middle")
            .attr("fill", "var(--text-primary)")
            .attr("font-size", "14px")
            .text("Trung Cung");

        svg.append("text")
            .attr("x", cx).attr("y", cy + 10)
            .attr("text-anchor", "middle")
            .attr("fill", "var(--text-muted)")
            .attr("font-size", "12px")
            .text(`t = ${tichTue}`);

        // Calculate positions
        const results = TAM_CO.calculate(tichTue);

        // Draw each ring
        results.forEach((res, ringIdx) => {
            const r = RADII[ringIdx];
            const pos = res.currentIdx;
            const color = COLORS[ringIdx];

            // Draw 12 nodes on ring
            for (let chi = 0; chi < 12; chi++) {
                const angle = (chi / 12) * 2 * Math.PI - Math.PI / 2;
                const nx = cx + r * Math.cos(angle);
                const ny = cy + r * Math.sin(angle);

                const isActive = chi === pos;

                svg.append("circle")
                    .attr("cx", nx).attr("cy", ny)
                    .attr("r", isActive ? 18 : 10)
                    .attr("fill", isActive ? color : "var(--bg-secondary)")
                    .attr("stroke", color)
                    .attr("stroke-width", isActive ? 3 : 1)
                    .attr("opacity", isActive ? 1 : 0.5);

                if (isActive || ringIdx === 0) {
                    svg.append("text")
                        .attr("x", nx).attr("y", ny + 4)
                        .attr("text-anchor", "middle")
                        .attr("fill", isActive ? "var(--bg-primary)" : "var(--text-muted)")
                        .attr("font-size", isActive ? "11px" : "9px")
                        .attr("font-weight", isActive ? "bold" : "normal")
                        .text(CHI_NAMES[chi]);
                }
            }

            // Ring label
            svg.append("text")
                .attr("x", cx + r + 5).attr("y", cy - r + 15)
                .attr("fill", color)
                .attr("font-size", "10px")
                .attr("opacity", 0.7)
                .text(LABELS[ringIdx]);

            // Active pointer line from center to active node
            const activeAngle = (pos / 12) * 2 * Math.PI - Math.PI / 2;
            const ax = cx + r * Math.cos(activeAngle);
            const ay = cy + r * Math.sin(activeAngle);
            svg.append("line")
                .attr("x1", cx).attr("y1", cy)
                .attr("x2", ax).attr("y2", ay)
                .attr("stroke", color)
                .attr("stroke-width", 2)
                .attr("stroke-dasharray", "6,3")
                .attr("opacity", 0.4);
        });

        // Draw ratio arrows
        svg.append("text")
            .attr("x", 20).attr("y", H - 20)
            .attr("fill", "var(--text-muted)")
            .attr("font-size", "11px")
            .text("Tỉ lệ: Quân 30 : Thần 3 : Dân 1");

        // Info panel
        infoDiv.html("");
        const table = infoDiv.append("table").attr("class", "mod-table");
        const headerRow = table.append("tr");
        ["Cơ", "Công thức", "Chi vị", "Địa Chi"].forEach(h => {
            headerRow.append("th").text(h);
        });

        results.forEach((res, i) => {
            const pos = res.currentIdx;
            const row = table.append("tr");
            row.append("td").html(`<span style="color:${COLORS[i]}">${res.name}</span>`);
            row.append("td").html(`⌊${tichTue} / ${res.period}⌋ mod 12`);
            row.append("td").text(pos);
            row.append("td").html(`<strong>${CHI_NAMES[pos]}</strong>`);
        });

        // Gear ratio explanation
        infoDiv.append("div").attr("class", "mod-math-note").html(`
            <strong>Cấu trúc:</strong> 3 nhóm ℤ₁₂ với tốc độ khác nhau<br>
            Quân Cơ quay 1 bước mỗi 30 năm, Thần Cơ mỗi 3 năm, Dân Cơ mỗi năm<br>
            Tỉ lệ tốc độ 30 : 3 : 1 → Quân chậm nhất (chiến lược), Dân nhanh nhất (chiến thuật)<br>
            <em>Tổng hợp 3 nhịp → phán đoán tình thế quốc gia</em>
        `);
    }

    return { init };
})();
