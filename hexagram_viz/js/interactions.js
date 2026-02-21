/**
 * interactions.js - Filter & Interaction Logic
 * Xử lý tương tác người dùng: lọc quẻ theo quái
 */

const HexViz = window.HexViz || {};

/**
 * Toggle filter theo sector index của Bát Quái
 * Click vào quái -> highlight 8 quẻ thuộc quái đó
 */
HexViz.toggleFilter = function (sectorIndex) {
    if (HexViz.activeFilterSector === sectorIndex) {
        // Reset - bỏ filter
        HexViz.activeFilterSector = null;
        d3.selectAll(".hex-group").transition().style("opacity", 1);
    } else {
        // Apply filter
        HexViz.activeFilterSector = sectorIndex;
        const startId = sectorIndex * 8;
        const endId = (sectorIndex + 1) * 8;

        d3.selectAll(".hex-group").transition().style("opacity", function () {
            const id = parseInt(d3.select(this).attr("data-id"));
            if (id >= startId && id < endId) return 1;
            return 0.1; // Dim others
        });
    }
};

/**
 * Gắn sự kiện tương tác cho Layer 8 (Bát Quái) sau khi load data
 */
HexViz.attachTrigramInteractions = function () {
    HexViz.svg.selectAll(".ring-sector")
        .on("mouseover", function (event, d) {
            d3.select(this).style("opacity", 1);

            if (d.data && HexViz.trigramHetuMap[d.data]) {
                HexViz.showTrigramTooltip(event, d.data, HexViz.trigramHetuMap[d.data]);
            }
        })
        .on("mouseout", function () {
            if (HexViz.activeFilterSector !== d3.select(this).datum().index) {
                d3.select(this).style("opacity", 0.6);
            }
            HexViz.hideTooltip();
        });
};

window.HexViz = HexViz;
