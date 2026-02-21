/**
 * tooltip.js - Tooltip Display Functions
 * Hiển thị thông tin chi tiết khi hover quẻ hoặc quái
 */

const HexViz = window.HexViz || {};

/**
 * Hiển thị tooltip cho quẻ dịch
 */
HexViz.showTooltip = function (event, d) {
    const tooltip = d3.select("#tooltip");
    const rightEdge = window.innerWidth - 320;
    const leftPos = Math.min(event.pageX + 20, rightEdge);

    d3.select("#hex-name").html(
        `${d.name} <span style="color:#aaa; font-size:0.9em">(${d.han || ''})</span>`
    );

    d3.select("#hex-image").html(
        `Binary: ${d.binary.toString(2).padStart(6, '0')} <br> ` +
        `<span style="color:#4fc3f7">Vị trí (Dec): ${d.binary}</span>`
    );

    d3.select("#hex-meaning").text(d.meaning);
    d3.select("#hex-judgment").text(d.analysis);
    d3.select("#hex-advice").html("<em>System Logic:</em> " + HexViz.analyzeHexagramAlgo(d.binary));

    tooltip.style("left", leftPos + "px")
        .style("top", (event.pageY - 20) + "px")
        .classed("hidden", false);
};

/**
 * Hiển thị tooltip cho quái (trigram)
 */
HexViz.showTrigramTooltip = function (event, name, info) {
    const tooltip = d3.select("#tooltip");
    const rightEdge = window.innerWidth - 320;
    const leftPos = Math.min(event.pageX + 20, rightEdge);

    d3.select("#hex-name").text(`Quái: ${name}`);

    let htmlContent = `
        <strong>Số Hà Đồ:</strong> ${info.number} <br>
        <strong>Thiên Can:</strong> ${info.stem} <br>
        <strong>Ngũ Hành:</strong> ${info.element} <br>
        <strong>Mùa:</strong> ${info.season} <br>
        <strong>Cơ thể:</strong> ${info.organ || '...'} <br>
        <em style="color:#888; font-size:0.9em">${info.image_note || ''}</em>
    `;

    d3.select("#hex-meaning").html(htmlContent);
    d3.select("#hex-image").text("");
    d3.select("#hex-judgment").text("");
    d3.select("#hex-advice").text("");

    tooltip.style("left", leftPos + "px")
        .style("top", (event.pageY - 20) + "px")
        .classed("hidden", false);
};

/**
 * Ẩn tooltip
 */
HexViz.hideTooltip = function () {
    d3.select("#tooltip").classed("hidden", true);
};

window.HexViz = HexViz;
