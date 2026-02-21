/**
 * main.js - Application Entry Point
 * Khởi tạo SVG, load data, render các layers
 */

(function () {
    const HexViz = window.HexViz;

    // --- Initialize SVG ---
    HexViz.svg = d3.select("#container")
        .append("svg")
        .attr("width", HexViz.width)
        .attr("height", HexViz.height)
        .append("g")
        .attr("transform", `translate(${HexViz.width / 2}, ${HexViz.height / 2})`);

    // --- Draw all layers (inside -> outside) ---
    HexViz.drawLuongNghi();    // Layer 2
    HexViz.drawTuTuong();      // Layer 4
    HexViz.drawBatQuai();      // Layer 8
    HexViz.drawHexagrams();    // Layer 64

    // --- Load external data ---
    Promise.all([
        d3.json("data/hexagrams.json"),
        d3.json("data/trigrams_hetu.json")
    ]).then(function ([hexData, trigramData]) {
        // 1. Enrich hexagram data with loaded JSON
        HexViz.hexagramsData.forEach(d => {
            const ext = hexData[d.id];
            if (ext) {
                d.name = `${ext.king_wen_order}. ${ext.name}`;
                d.han = ext.han;
                d.meaning = ext.description;
                d.analysis = ext.analysis;
            } else {
                d.analysis = HexViz.analyzeHexagramAlgo(d.binary);
            }
        });

        // 2. Store trigram data
        HexViz.trigramHetuMap = trigramData;

        // 3. Attach trigram interactions after data is ready
        HexViz.attachTrigramInteractions();

    }).catch(err => {
        console.error("Could not load data files", err);
        // Fallback: use algorithmic analysis
        HexViz.hexagramsData.forEach(d => {
            d.analysis = HexViz.analyzeHexagramAlgo(d.binary);
        });
    });
})();
