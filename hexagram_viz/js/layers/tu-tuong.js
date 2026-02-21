/**
 * tu-tuong.js - Layer 4: Tứ Tượng
 * Thái Âm, Thiếu Dương, Thiếu Âm, Thái Dương
 */

const HexViz = window.HexViz || {};

HexViz.drawTuTuong = function () {
    const { svg, r2, r4, tuTuongNames, tuTuongColors } = HexViz;

    const arc4 = d3.arc()
        .innerRadius(r2 + 5)
        .outerRadius(r4 - 5)
        .startAngle(d => d.startAngle)
        .endAngle(d => d.endAngle);

    const pie4 = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);

    const tuTuongData = pie4(tuTuongNames).map((d, i) => ({
        ...d, name: tuTuongNames[i], color: tuTuongColors[i]
    }));

    // Draw arcs
    svg.append("g").attr("class", "layer-tu-tuong")
        .selectAll("path")
        .data(tuTuongData)
        .enter().append("path")
        .attr("d", arc4)
        .attr("fill", d => d.color)
        .attr("class", "ring-sector")
        .style("opacity", 0.7)
        .on("mouseover", function () { d3.select(this).style("opacity", 1); })
        .on("mouseout", function () { d3.select(this).style("opacity", 0.7); });

    // Draw labels
    svg.append("g").attr("class", "layer-tu-tuong-labels")
        .selectAll("text")
        .data(tuTuongData)
        .enter().append("text")
        .attr("transform", d => `translate(${arc4.centroid(d)})`)
        .attr("class", "ring-label")
        .text(d => d.name);
};

window.HexViz = HexViz;
