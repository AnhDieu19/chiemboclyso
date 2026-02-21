
// Logic: Fuxi Sequence (0-63)
const hexagramsData = [];

const fullNames = [
    "Khôn (Thuần Khôn)", "Bác (Sơn Địa Bác)", "Tỷ (Thủy Địa Tỷ)", "Quan (Phong Địa Quan)", "Dự (Lôi Địa Dự)", "Tấn (Hỏa Địa Tấn)", "Tụy (Trạch Địa Tụy)", "Bĩ (Thiên Địa Bĩ)",
    "Khiêm (Địa Sơn Khiêm)", "Cấn (Thuần Cấn)", "Kiển (Thủy Sơn Kiển)", "Tiệm (Phong Sơn Tiệm)", "Tiểu Quá (Lôi Sơn Tiểu Quá)", "Lữ (Hỏa Sơn Lữ)", "Hàm (Trạch Sơn Hàm)", "Độn (Thiên Sơn Độn)",
    "Sư (Địa Thủy Sư)", "Mông (Sơn Thủy Mông)", "Khảm (Thuần Khảm)", "Hoán (Phong Thủy Hoán)", "Giải (Lôi Thủy Giải)", "Vị Tế (Hỏa Thủy Vị Tế)", "Khốn (Trạch Thủy Khốn)", "Tụng (Thiên Thủy Tụng)",
    "Thăng (Địa Phong Thăng)", "Cổ (Sơn Phong Cổ)", "Tỉnh (Thủy Phong Tỉnh)", "Tốn (Thuần Tốn)", "Hằng (Lôi Phong Hằng)", "Đỉnh (Hỏa Phong Đỉnh)", "Đại Quá (Trạch Phong Đại Quá)", "Cấu (Thiên Phong Cấu)",
    "Phục (Địa Lôi Phục)", "Di (Sơn Lôi Di)", "Truân (Thủy Lôi Truân)", "Ích (Phong Lôi Ích)", "Chấn (Thuần Chấn)", "Phệ Hạp (Hỏa Lôi Phệ Hạp)", "Tùy (Trạch Lôi Tùy)", "Vô Vọng (Thiên Lôi Vô Vọng)",
    "Minh Di (Địa Hỏa Minh Di)", "Bí (Sơn Hỏa Bí)", "Ký Tế (Thủy Hỏa Ký Tế)", "Gia Nhân (Phong Hỏa Gia Nhân)", "Phong (Lôi Hỏa Phong)", "Ly (Thuần Ly)", "Cách (Trạch Hỏa Cách)", "Đồng Nhân (Thiên Hỏa Đồng Nhân)",
    "Lâm (Địa Trạch Lâm)", "Tổn (Sơn Trạch Tổn)", "Tiết (Thủy Trạch Tiết)", "Trung Phu (Phong Trạch Trung Phu)", "Quy Muội (Lôi Trạch Quy Muội)", "Khuê (Hỏa Trạch Khuê)", "Đoài (Thuần Đoài)", "Lý (Thiên Trạch Lý)",
    "Thái (Địa Thiên Thái)", "Đại Súc (Sơn Thiên Đại Súc)", "Nhu (Thủy Thiên Nhu)", "Tiểu Súc (Phong Thiên Tiểu Súc)", "Đại Tráng (Lôi Thiên Đại Tráng)", "Đại Hữu (Hỏa Thiên Đại Hữu)", "Quải (Trạch Thiên Quải)", "Càn (Thuần Càn)"
];

for (let i = 0; i < 64; i++) {
    hexagramsData.push({
        id: i,
        name: fullNames[i] || `Quẻ số ${i}`,
        binary: i,
        image_text: "Đang cập nhật...",
        meaning: "Đang cập nhật...",
        judgment: "Đang cập nhật...",
        advice: "Đang cập nhật..."
    });
}

// Sample Data Overrides
hexagramsData[56].image_text = "Hỷ Báo Tam Nguyên";
hexagramsData[56].meaning = "Hanh thông, thời vận tốt, trời đất giao hòa.";
hexagramsData[56].judgment = "Tiểu vãng đại lai, cát hanh.";
hexagramsData[56].advice = "Giữ đạo trung, phòng khi suy vi. Dùng quân tử, xa tiểu nhân.";

hexagramsData[63].image_text = "Khốn Long Đắc Thủy";
hexagramsData[63].meaning = "Cương kiện, mạnh mẽ, đầu đàn.";
hexagramsData[63].judgment = "Nguyên, hanh, lợi, trinh.";
hexagramsData[63].advice = "Phấn đấu không ngừng, nhưng cần biết thời thế.";

hexagramsData[0].image_text = "Ngạ Hổ Đắc Thực";
hexagramsData[0].meaning = "Nhu thuận, cưu mang vạn vật.";
hexagramsData[0].judgment = "Nguyên, hanh, lợi tẫn mã chi trinh.";
hexagramsData[0].advice = "Làm việc cần có người dẫn dắt, thuận theo thời thế.";


// Visualization Config
const width = window.innerWidth * 0.95;
const height = window.innerHeight * 0.95;
const maxRadius = Math.min(width, height) / 2;

// Layer Radii Configuration
// Center -> 2 -> 4 -> 8 -> 64 Boxes
// User Request: Tăng kích thước vòng tròn nhỏ (Inner Circles)
const r2 = maxRadius * 0.25; // Increased from 20%
const r4 = maxRadius * 0.45; // Increased from 35%
const r8 = maxRadius * 0.65; // Increased from 50%
// The 64 ring starts after r8.
// User Request: Tăng kích thước từng vòng tròn (Pushing out to max availability)
const r64_center = maxRadius * 0.88;
// Calculate Max Circle Radius based on new circumference
const circum = 2 * Math.PI * r64_center;
const maxHexR = (circum / 64) / 2 * 0.95; // 95% fill (tight packing)

const svg = d3.select("#container")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", `translate(${width / 2}, ${height / 2})`);

let activeFilterSector = null; // Track active filter

// --- LAYER 8: BÁT QUÁI (8 Sectors) --
// 8 slices, each covers 8 hexagrams
// Names: Khôn, Cấn, Khảm, Tốn, Chấn, Ly, Đoài, Càn
const baguaNames = [
    "Khôn", "Cấn", "Khảm", "Tốn",
    "Chấn", "Ly", "Đoài", "Càn"
];
const baguaColors = [
    "#3e2723", "#5d4037", "#1a237e", "#1b5e20",
    "#f57f17", "#b71c1c", "#00acc1", "#eeeeee"
];

const arc8 = d3.arc()
    .innerRadius(r4 + 5)
    .outerRadius(r8 - 5)
    .startAngle(d => d.startAngle)
    .endAngle(d => d.endAngle);

const pie8 = d3.pie()
    .value(1)
    .sort(null)
    .startAngle(0) // Align with 12 o'clock (Match Hexagrams)
    .endAngle(2 * Math.PI);

const baguaData = pie8(baguaNames).map((d, i) => ({
    ...d,
    name: baguaNames[i],
    color: baguaColors[i],
    index: i // Keep index 0-7 for filtering
}));

// Draw Arcs
svg.append("g").selectAll("path")
    .data(baguaData)
    .enter().append("path")
    .attr("d", arc8)
    .attr("fill", d => d.color)
    .attr("class", "ring-sector")
    .style("opacity", 0.6)
    .on("mouseover", function () { d3.select(this).style("opacity", 1); })
    .on("mouseout", function () {
        // Only reset opacity if this sector is NOT selected
        if (activeFilterSector !== d3.select(this).datum().index) {
            d3.select(this).style("opacity", 0.6);
        }
    })
    .on("click", function (event, d) {
        toggleFilter(d.index);

        // Highlight logic for sectors
        svg.selectAll(".ring-sector").style("stroke", "#222").style("stroke-width", "1px");
        if (activeFilterSector !== null) {
            d3.select(this).style("stroke", "#fff").style("stroke-width", "3px").style("opacity", 1);
        }
    });

// Draw Labels
svg.append("g").selectAll("text")
    .data(baguaData)
    .enter().append("text")
    .attr("transform", d => `translate(${arc8.centroid(d)})`)
    .attr("class", "ring-label")
    .text(d => d.name)
    .style("pointer-events", "none"); // Pass clicks through


// --- LAYER 4: TỨ TƯỢNG (4 Sectors) ---
const tuTuongNames = ["Thái Âm", "Thiếu Dương", "Thiếu Âm", "Thái Dương"];
const tuTuongColors = ["#212121", "#616161", "#9e9e9e", "#f5f5f5"];

const arc4 = d3.arc()
    .innerRadius(r2 + 5)
    .outerRadius(r4 - 5)
    .startAngle(d => d.startAngle)
    .endAngle(d => d.endAngle);

const pie4 = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);

const tuTuongData = pie4(tuTuongNames).map((d, i) => ({
    ...d, name: tuTuongNames[i], color: tuTuongColors[i]
}));

svg.append("g").selectAll("path")
    .data(tuTuongData)
    .enter().append("path")
    .attr("d", arc4)
    .attr("fill", d => d.color)
    .attr("class", "ring-sector")
    .style("opacity", 0.7)
    .on("mouseover", function () { d3.select(this).style("opacity", 1); })
    .on("mouseout", function () { d3.select(this).style("opacity", 0.7); });

svg.append("g").selectAll("text")
    .data(tuTuongData)
    .enter().append("text")
    .attr("transform", d => `translate(${arc4.centroid(d)})`)
    .attr("class", "ring-label")
    .text(d => d.name);


// --- LAYER 2: LƯỠNG NGHI (2 Sectors) ---
const luongNghiNames = ["Âm", "Dương"];
const luongNghiColors = ["#000", "#fff"];

const arc2 = d3.arc()
    .innerRadius(0)
    .outerRadius(r2 - 5)
    .startAngle(d => d.startAngle)
    .endAngle(d => d.endAngle);

const pie2 = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);
const luongNghiData = pie2(luongNghiNames).map((d, i) => ({
    ...d, name: luongNghiNames[i], color: luongNghiColors[i]
}));

svg.append("g").selectAll("path")
    .data(luongNghiData)
    .enter().append("path")
    .attr("d", arc2)
    .attr("fill", d => d.color)
    .attr("stroke", "#555")
    .attr("class", "ring-sector")
    .style("opacity", 0.8)
    .on("mouseover", function () { d3.select(this).style("opacity", 1); })
    .on("mouseout", function () { d3.select(this).style("opacity", 0.8); });

svg.append("g").selectAll("text")
    .data(luongNghiData)
    .enter().append("text")
    .attr("transform", d => `translate(${arc2.centroid(d)})`)
    .attr("class", "ring-label")
    .attr("fill", (d, i) => i === 1 ? "#000" : "#fff") // Contrast text
    .text(d => d.name);


// --- LAYER 64: HEXAGRAM CIRCLES ---
const angleStep = (2 * Math.PI) / 64;

hexagramsData.forEach((d, i) => {
    // Calc Center Position
    const angle = i * angleStep - Math.PI / 2 + (angleStep / 2);
    const cx = r64_center * Math.cos(angle);
    const cy = r64_center * Math.sin(angle);

    // Group at (cx, cy)
    // ADDED CLASS .hex-group AND .data-id for FILTERING
    const g = svg.append("g")
        .attr("class", "hex-group")
        .attr("data-id", i)
        .attr("transform", `translate(${cx}, ${cy})`);

    // 1. The Container Circle
    g.append("circle")
        .attr("r", maxHexR)
        .attr("fill", "#1e1e1e")
        .attr("stroke", "#555")
        .attr("stroke-width", 1)
        .style("cursor", "pointer")
        .on("mouseover", function () {
            d3.select(this).attr("stroke", "#fff").attr("stroke-width", 2);
            showTooltip(d3.event || event, d); // Event handling
        })
        .on("mouseout", function () {
            d3.select(this).attr("stroke", "#555").attr("stroke-width", 1);
            hideTooltip();
        });

    // 2. The Hexagram Symbol (6 Lines) inside
    const symbolG = g.append("g")
        .attr("transform", `rotate(${angle * 180 / Math.PI + 90})`);

    const binaryStr = d.binary.toString(2).padStart(6, '0');
    // Inner-most (Bottom Line) = Bit 5 (Index 0).

    const h = maxHexR * 1.5; // Total height of stack
    const w = maxHexR * 1.4; // Width of lines
    const lineH = h / 7;     // Height of single line (inc gap)

    for (let bit = 0; bit < 6; bit++) {
        const isYang = binaryStr[bit] === '1';
        const drawY = (2.5 - bit) * lineH;

        if (isYang) {
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


// FILTER FUNCTION
function toggleFilter(sectorIndex) {
    if (activeFilterSector === sectorIndex) {
        // Reset
        activeFilterSector = null;
        d3.selectAll(".hex-group").transition().style("opacity", 1);
    } else {
        // Filter
        activeFilterSector = sectorIndex;
        const startId = sectorIndex * 8;
        const endId = (sectorIndex + 1) * 8;

        d3.selectAll(".hex-group").transition().style("opacity", function () {
            const id = parseInt(d3.select(this).attr("data-id"));
            if (id >= startId && id < endId) return 1;
            return 0.1; // Dim others
        });
    }
}



// 1. Fetch Data & Initialize
let trigramHetuMap = {}; // Global store for Trigram Data

Promise.all([
    d3.json("hexagrams.json"),
    d3.json("trigrams_hetu.json")
]).then(function ([hexData, trigramData]) {
    // 1. Process Hexagram Data
    hexagramsData.forEach(d => {
        const ext = hexData[d.id];
        if (ext) {
            d.name = `${ext.king_wen_order}. ${ext.name}`;
            d.han = ext.han;
            d.meaning = ext.description;
            d.analysis = ext.analysis;
        } else {
            d.analysis = analyzeHexagramAlgo(d.binary);
        }
    });

    // 2. Process Trigram Data
    trigramHetuMap = trigramData;

}).catch(err => {
    console.error("Could not load data files", err);
    // Fallback
    hexagramsData.forEach(d => {
        d.analysis = analyzeHexagramAlgo(d.binary);
    });
});


// --- ALGORITHMIC ANALYSIS ENGINE ---
function analyzeHexagramAlgo(val) {
    const binaryStr = val.toString(2).padStart(6, '0');
    const ones = binaryStr.split('1').length - 1;
    const zeros = 6 - ones;

    let algoText = "";

    // 1. Energy Balance
    if (ones === 6) algoText += "Pure Yang Energy (Entropy Min). ";
    else if (zeros === 6) algoText += "Pure Yin Space (Memory Empty). ";
    else if (Math.abs(ones - zeros) <= 2) algoText += "Cân bằng Âm Dương. ";
    else algoText += ones > zeros ? "Dương khí thịnh. " : "Âm khí thịnh. ";

    // 2. Structural Analysis
    if (ones === 1) {
        const pos = 6 - binaryStr.indexOf('1');
        algoText += `Tập trung quyền lực (Centralized). Dương hào ${pos} kiểm soát hệ thống.`;
    } else if (zeros === 1) {
        const pos = 6 - binaryStr.indexOf('0');
        algoText += `Điểm yếu/mạnh duy nhất (Single Point). Âm hào ${pos} chi phối.`;
    }

    if (binaryStr === "010101" || binaryStr === "101010") {
        algoText += "Cấu trúc xen kẽ hoàn hảo (Interleaved). Hệ thống dao động ổn định.";
    }

    return algoText;
}


// --- UPDATE LAYER 8 INTEACTIVITY ---
// We need to re-select the Layer 8 paths to add the new tooltip behavior
// Since d3.json is async, we can just attach the listener now, and it will read 'trigramHetuMap' when triggered (which will be populated by then)

svg.selectAll(".ring-sector")
    .on("mouseover", function (event, d) {
        d3.select(this).style("opacity", 1);

        // Check if this is a Trigram (Layer 8 has 'index' property from baguaData map)
        if (d.data && trigramHetuMap[d.data]) {
            showTrigramTooltip(event, d.data, trigramHetuMap[d.data]);
        }
    })
    .on("mouseout", function () {
        if (activeFilterSector !== d3.select(this).datum().index) {
            d3.select(this).style("opacity", 0.6);
        }
        hideTooltip();
    });


// Tooltip Functions (Updated)
function showTooltip(event, d) {
    const tooltip = d3.select("#tooltip");
    const rightEdge = window.innerWidth - 320;
    const leftPos = Math.min(event.pageX + 20, rightEdge);

    d3.select("#hex-name").html(`${d.name} <span style="color:#aaa; font-size:0.9em">(${d.han || ''})</span>`);

    // ADDED: Decimal Value (Vị trí)
    d3.select("#hex-image").html(`Binary: ${d.binary.toString(2).padStart(6, '0')} <br> <span style="color:#4fc3f7">Vị trí (Dec): ${d.binary}</span>`);

    d3.select("#hex-meaning").text(d.meaning);
    d3.select("#hex-judgment").text(d.analysis);
    d3.select("#hex-advice").html("<em>System Logic:</em> " + analyzeHexagramAlgo(d.binary));

    tooltip.style("left", leftPos + "px")
        .style("top", (event.pageY - 20) + "px")
        .classed("hidden", false);
}

function showTrigramTooltip(event, name, info) {
    const tooltip = d3.select("#tooltip");
    const rightEdge = window.innerWidth - 320;
    const leftPos = Math.min(event.pageX + 20, rightEdge);

    d3.select("#hex-name").text(`Quái: ${name}`);

    // Construct rich content for He Tu
    let htmlContent = `
        <strong>Số Hà Đồ:</strong> ${info.number} <br>
        <strong>Thiên Can:</strong> ${info.stem} <br>
        <strong>Ngũ Hành:</strong> ${info.element} <br>
        <strong>Mùa:</strong> ${info.season} <br>
        <strong>Cơ thể:</strong> ${info.organ || '...'} <br>
        <em style="color:#888; font-size:0.9em">${info.image_note || ''}</em>
    `;

    d3.select("#hex-meaning").html(htmlContent);
    // Clear other fields
    d3.select("#hex-image").text("");
    d3.select("#hex-judgment").text("");
    d3.select("#hex-advice").text("");

    tooltip.style("left", leftPos + "px")
        .style("top", (event.pageY - 20) + "px")
        .classed("hidden", false);
}

function hideTooltip() {
    d3.select("#tooltip").classed("hidden", true);
}
