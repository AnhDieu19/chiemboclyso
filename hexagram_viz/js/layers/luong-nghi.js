/**
 * luong-nghi.js - Layer 2: Lưỡng Nghi (Âm / Dương)
 * Vòng trong cùng: 2 sectors
 */

const HexViz = window.HexViz || {};

HexViz.drawLuongNghi = function () {
    const { svg, r2, luongNghiNames, luongNghiColors } = HexViz;

    const arc2 = d3.arc()
        .innerRadius(0)
        .outerRadius(r2 - 5)
        .startAngle(d => d.startAngle)
        .endAngle(d => d.endAngle);

    const pie2 = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);

    const luongNghiData = pie2(luongNghiNames).map((d, i) => ({
        ...d, name: luongNghiNames[i], color: luongNghiColors[i]
    }));

    // Draw arcs
    svg.append("g").attr("class", "layer-luong-nghi")
        .selectAll("path")
        .data(luongNghiData)
        .enter().append("path")
        .attr("d", arc2)
        .attr("fill", d => d.color)
        .attr("stroke", "#555")
        .attr("class", "ring-sector")
        .style("opacity", 0.8)
        .on("mouseover", function () { d3.select(this).style("opacity", 1); })
        .on("mouseout", function () { d3.select(this).style("opacity", 0.8); });

    // Draw labels
    svg.append("g").attr("class", "layer-luong-nghi-labels")
        .selectAll("text")
        .data(luongNghiData)
        .enter().append("text")
        .attr("transform", d => `translate(${arc2.centroid(d)})`)
        .attr("class", "ring-label")
        .attr("fill", (d, i) => i === 1 ? "#000" : "#fff")
        .text(d => d.name);
};

window.HexViz = HexViz;
