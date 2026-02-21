/**
 * bat-quai.js - Layer 8: Bát Quái
 * 8 quái: Khôn, Cấn, Khảm, Tốn, Chấn, Ly, Đoài, Càn
 */

const HexViz = window.HexViz || {};

HexViz.drawBatQuai = function () {
    const { svg, r4, r8, baguaNames, baguaColors } = HexViz;

    const arc8 = d3.arc()
        .innerRadius(r4 + 5)
        .outerRadius(r8 - 5)
        .startAngle(d => d.startAngle)
        .endAngle(d => d.endAngle);

    const pie8 = d3.pie()
        .value(1)
        .sort(null)
        .startAngle(0)
        .endAngle(2 * Math.PI);

    const baguaData = pie8(baguaNames).map((d, i) => ({
        ...d,
        name: baguaNames[i],
        color: baguaColors[i],
        index: i
    }));

    // Draw arcs
    svg.append("g").attr("class", "layer-bat-quai")
        .selectAll("path")
        .data(baguaData)
        .enter().append("path")
        .attr("d", arc8)
        .attr("fill", d => d.color)
        .attr("class", "ring-sector")
        .style("opacity", 0.6)
        .on("mouseover", function () { d3.select(this).style("opacity", 1); })
        .on("mouseout", function () {
            if (HexViz.activeFilterSector !== d3.select(this).datum().index) {
                d3.select(this).style("opacity", 0.6);
            }
        })
        .on("click", function (event, d) {
            HexViz.toggleFilter(d.index);

            // Highlight logic for sectors
            svg.selectAll(".ring-sector").style("stroke", "#222").style("stroke-width", "1px");
            if (HexViz.activeFilterSector !== null) {
                d3.select(this).style("stroke", "#fff").style("stroke-width", "3px").style("opacity", 1);
            }
        });

    // Draw labels
    svg.append("g").attr("class", "layer-bat-quai-labels")
        .selectAll("text")
        .data(baguaData)
        .enter().append("text")
        .attr("transform", d => `translate(${arc8.centroid(d)})`)
        .attr("class", "ring-label")
        .text(d => d.name)
        .style("pointer-events", "none");
};

window.HexViz = HexViz;
