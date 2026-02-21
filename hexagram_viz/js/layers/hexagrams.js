/**
 * hexagrams.js - Layer 64: Hexagram Circles
 * Vẽ 64 quẻ dịch trên vòng ngoài cùng
 */

const HexViz = window.HexViz || {};

HexViz.drawHexagrams = function () {
    const { svg, r64_center, maxHexR, hexagramsData } = HexViz;
    const angleStep = (2 * Math.PI) / 64;

    hexagramsData.forEach((d, i) => {
        // Calculate center position
        const angle = i * angleStep - Math.PI / 2 + (angleStep / 2);
        const cx = r64_center * Math.cos(angle);
        const cy = r64_center * Math.sin(angle);

        // Group with class and data-id for filtering
        const g = svg.append("g")
            .attr("class", "hex-group")
            .attr("data-id", i)
            .attr("transform", `translate(${cx}, ${cy})`);

        // 1. Container Circle
        g.append("circle")
            .attr("r", maxHexR)
            .attr("fill", "#1e1e1e")
            .attr("stroke", "#555")
            .attr("stroke-width", 1)
            .style("cursor", "pointer")
            .on("mouseover", function (event) {
                d3.select(this).attr("stroke", "#fff").attr("stroke-width", 2);
                HexViz.showTooltip(event, d);
            })
            .on("mouseout", function () {
                d3.select(this).attr("stroke", "#555").attr("stroke-width", 1);
                HexViz.hideTooltip();
            });

        // 2. Hexagram Symbol (6 lines)
        const symbolG = g.append("g")
            .attr("transform", `rotate(${angle * 180 / Math.PI + 90})`);

        const binaryStr = d.binary.toString(2).padStart(6, '0');

        const h = maxHexR * 1.5;  // Total height of stack
        const w = maxHexR * 1.4;  // Width of lines
        const lineH = h / 7;      // Height of single line (inc gap)

        for (let bit = 0; bit < 6; bit++) {
            const isYang = binaryStr[bit] === '1';
            const drawY = (2.5 - bit) * lineH;

            if (isYang) {
                // Yang: Solid bar
                symbolG.append("rect")
                    .attr("x", -w / 2)
                    .attr("y", drawY - lineH / 2 * 0.8)
                    .attr("width", w)
                    .attr("height", lineH * 0.8)
                    .attr("fill", "#fff");
            } else {
                // Yin: Two bars with gap
                const gap = w * 0.2;
                const segW = (w - gap) / 2;

                symbolG.append("rect")
                    .attr("x", -w / 2)
                    .attr("y", drawY - lineH / 2 * 0.8)
                    .attr("width", segW)
                    .attr("height", lineH * 0.8)
                    .attr("fill", "#fff");

                symbolG.append("rect")
                    .attr("x", gap / 2)
                    .attr("y", drawY - lineH / 2 * 0.8)
                    .attr("width", segW)
                    .attr("height", lineH * 0.8)
                    .attr("fill", "#fff");
            }
        }
    });
};

window.HexViz = HexViz;
