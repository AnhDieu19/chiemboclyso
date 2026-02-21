/**
 * Nested Modular Chain — Visualization
 * ======================================
 * Shows the Tích Niên → mod 3600 → mod 360 → mod 72 reduction
 * with interactive year input.
 */

const ModularViz = (() => {

    let container;

    function init(containerId) {
        container = d3.select(containerId);

        // Controls
        const ctrl = container.append("div").attr("class", "mod-controls");
        ctrl.append("label").text("Năm dương lịch: ");
        const yearInput = ctrl.append("input")
            .attr("type", "number")
            .attr("class", "mod-input")
            .attr("value", "2026")
            .attr("min", "-5000")
            .attr("max", "10000");
        const btnCalc = ctrl.append("button").attr("class", "phi-btn").text("Tính");

        // Result container
        const resultDiv = container.append("div").attr("class", "mod-result");

        // Events
        btnCalc.on("click", () => calculate(+yearInput.node().value, resultDiv));
        yearInput.on("keypress", (e) => { if (e.key === "Enter") calculate(+yearInput.node().value, resultDiv); });

        // Initial calculation
        calculate(2026, resultDiv);
    }

    function calculate(year, resultDiv) {
        const result = MODULAR_CHAIN.reduce(year);
        resultDiv.html("");

        // Tích Niên
        const headerDiv = resultDiv.append("div").attr("class", "mod-header");
        headerDiv.html(`
            <div class="mod-epoch">Epoch (E) = <strong>${MODULAR_CHAIN.epoch.toLocaleString()}</strong></div>
            <div class="mod-tich">Tích Niên = ${year} + ${MODULAR_CHAIN.epoch.toLocaleString()} = 
                <strong class="mod-highlight">${result.tichNien.toLocaleString()}</strong>
            </div>
        `);

        // Chain visualization
        const chainDiv = resultDiv.append("div").attr("class", "mod-chain");

        result.steps.forEach((step, i) => {
            const stepDiv = chainDiv.append("div").attr("class", "mod-step");

            stepDiv.append("div").attr("class", "mod-step-label")
                .html(`<span class="mod-level">${step.level}</span>`);

            stepDiv.append("div").attr("class", "mod-step-calc")
                .html(`
                    <span class="mod-input-val">${step.input.toLocaleString()}</span>
                    <span class="mod-op">mod</span>
                    <span class="mod-mod-val">${step.mod.toLocaleString()}</span>
                    <span class="mod-eq">=</span>
                    <span class="mod-result-val">${step.output.toLocaleString()}</span>
                `);

            if (i < result.steps.length - 1) {
                chainDiv.append("div").attr("class", "mod-arrow").text("↓");
            }
        });

        // Final result
        const finalDiv = resultDiv.append("div").attr("class", "mod-final");
        finalDiv.html(`
            <div class="mod-ky-du">
                <strong>Kỷ Dư = ${result.kyDu}</strong>
                <span class="mod-note">(dùng cho tất cả tính toán Thái Ất)</span>
            </div>
        `);

        // Breakdown
        const breakDiv = resultDiv.append("div").attr("class", "mod-breakdown");
        const kyDu = result.kyDu;
        const duongAm = kyDu <= 36 ? "Dương Cục" : "Âm Cục";
        const cuc = kyDu <= 36 ? kyDu : 72 - kyDu;

        // Thái Ất position
        let thaiAtCung;
        if (kyDu > 24) {
            const step8 = Math.floor((kyDu - 25) / 3);
            const ring8 = [1, 8, 3, 4, 9, 2, 7, 6];
            thaiAtCung = ring8[step8 % 8];
        } else {
            const step8 = Math.floor((24 - kyDu) / 3);
            const ring8 = [1, 6, 7, 2, 9, 4, 3, 8]; // reverse
            thaiAtCung = ring8[step8 % 8];
        }

        breakDiv.html(`
            <table class="mod-table">
                <tr><td>Kỷ Dư</td><td><strong>${kyDu}</strong></td></tr>
                <tr><td>Dương/Âm</td><td><span class="mod-badge ${kyDu <= 36 ? 'mod-duong' : 'mod-am'}">${duongAm}</span></td></tr>
                <tr><td>Cục số</td><td><strong>${cuc}</strong></td></tr>
                <tr><td>Ngũ Phúc</td><td>${calcPath(SPECIAL_PATHS[0], result.tichNien)}</td></tr>
                <tr><td>Đại Du</td><td>${calcPath(SPECIAL_PATHS[1], result.tichNien)}</td></tr>
            </table>
        `);

        // Mathematical note
        resultDiv.append("div").attr("class", "mod-math-note").html(`
            <strong>Cấu trúc toán:</strong>
            ℤ<sub>3600</sub> ↠ ℤ<sub>360</sub> ↠ ℤ<sub>72</sub><br>
            3600 = 10 Kỷ · 360 năm, &nbsp; 360 = 5 Nguyên · 72 năm, &nbsp; 72 = 12 Hội · 6 năm<br>
            <code>${result.tichNien.toLocaleString()} mod 3600 = ${result.steps[0].output} → mod 360 = ${result.steps[1].output} → mod 72 = ${result.steps[2].output}</code>
        `);
    }

    function calcPath(pathInfo, tichNien) {
        const val = ((tichNien + pathInfo.offset) % pathInfo.totalCycle + pathInfo.totalCycle) % pathInfo.totalCycle;
        const idx = Math.floor(val / pathInfo.period) % pathInfo.path.length;
        const palace = pathInfo.path[idx];
        const pal = LAC_THU.palaces[palace];
        return `Cung ${palace} ${pal.symbol} ${pal.name} <span style="color:var(--text-muted)">(idx ${idx}/${pathInfo.path.length})</span>`;
    }

    return { init };
})();
