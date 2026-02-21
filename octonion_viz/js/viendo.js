/**
 * Viên Đồ Bát Quái — 64 Hexagram Circular Diagram
 * ==================================================
 * Concentric rings: Thái Cực → Lưỡng Nghi → Tứ Tượng → Bát Quái → 64 Quẻ
 * with Octonion unit labels on the Bát Quái ring.
 *
 * Uses D3.js v7. Fuxi binary order (0-63).
 */

const VienDo = (() => {
    /* ── 64 Hexagram Names (Fuxi binary order 0–63) ── */
    const HEXAGRAM_NAMES = [
        "Khôn", "Bác", "Tỷ", "Quan", "Dự", "Tấn", "Tụy", "Bĩ",
        "Khiêm", "Cấn", "Kiển", "Tiệm", "Tiểu Quá", "Lữ", "Hàm", "Độn",
        "Sư", "Mông", "Khảm", "Hoán", "Giải", "Vị Tế", "Khốn", "Tụng",
        "Thăng", "Cổ", "Tỉnh", "Tốn", "Hằng", "Đỉnh", "Đại Quá", "Cấu",
        "Phục", "Di", "Truân", "Ích", "Chấn", "Phệ Hạp", "Tùy", "Vô Vọng",
        "Minh Di", "Bí", "Ký Tế", "Gia Nhân", "Phong", "Ly", "Cách", "Đồng Nhân",
        "Lâm", "Tổn", "Tiết", "Trung Phu", "Quy Muội", "Khuê", "Đoài", "Lý",
        "Thái", "Đại Súc", "Nhu", "Tiểu Súc", "Đại Tráng", "Đại Hữu", "Quải", "Càn"
    ];

    const HEXAGRAM_FULLNAMES = [
        "Thuần Khôn", "Sơn Địa Bác", "Thủy Địa Tỷ", "Phong Địa Quan", "Lôi Địa Dự", "Hỏa Địa Tấn", "Trạch Địa Tụy", "Thiên Địa Bĩ",
        "Địa Sơn Khiêm", "Thuần Cấn", "Thủy Sơn Kiển", "Phong Sơn Tiệm", "Lôi Sơn Tiểu Quá", "Hỏa Sơn Lữ", "Trạch Sơn Hàm", "Thiên Sơn Độn",
        "Địa Thủy Sư", "Sơn Thủy Mông", "Thuần Khảm", "Phong Thủy Hoán", "Lôi Thủy Giải", "Hỏa Thủy Vị Tế", "Trạch Thủy Khốn", "Thiên Thủy Tụng",
        "Địa Phong Thăng", "Sơn Phong Cổ", "Thủy Phong Tỉnh", "Thuần Tốn", "Lôi Phong Hằng", "Hỏa Phong Đỉnh", "Trạch Phong Đại Quá", "Thiên Phong Cấu",
        "Địa Lôi Phục", "Sơn Lôi Di", "Thủy Lôi Truân", "Phong Lôi Ích", "Thuần Chấn", "Hỏa Lôi Phệ Hạp", "Trạch Lôi Tùy", "Thiên Lôi Vô Vọng",
        "Địa Hỏa Minh Di", "Sơn Hỏa Bí", "Thủy Hỏa Ký Tế", "Phong Hỏa Gia Nhân", "Lôi Hỏa Phong", "Thuần Ly", "Trạch Hỏa Cách", "Thiên Hỏa Đồng Nhân",
        "Địa Trạch Lâm", "Sơn Trạch Tổn", "Thủy Trạch Tiết", "Phong Trạch Trung Phu", "Lôi Trạch Quy Muội", "Hỏa Trạch Khuê", "Thuần Đoài", "Thiên Trạch Lý",
        "Địa Thiên Thái", "Sơn Thiên Đại Súc", "Thủy Thiên Nhu", "Phong Thiên Tiểu Súc", "Lôi Thiên Đại Tráng", "Hỏa Thiên Đại Hữu", "Trạch Thiên Quải", "Thuần Càn"
    ];

    /* ── cohoc.net URLs for each hexagram (Fuxi binary order 0–63) ── */
    const HEXAGRAM_URLS = [
        "https://cohoc.net/thuan-khon-kid-2.html",           // 0  Thuần Khôn
        "https://cohoc.net/son-dia-bac-kid-23.html",          // 1  Sơn Địa Bác
        "https://cohoc.net/thuy-dia-ty-kid-8.html",           // 2  Thủy Địa Tỷ
        "https://cohoc.net/phong-dia-quan-kid-20.html",       // 3  Phong Địa Quan
        "https://cohoc.net/loi-dia-du-kid-16.html",           // 4  Lôi Địa Dự
        "https://cohoc.net/hoa-dia-tan-kid-35.html",          // 5  Hỏa Địa Tấn
        "https://cohoc.net/trach-dia-tuy-kid-45.html",        // 6  Trạch Địa Tụy
        "https://cohoc.net/thien-dia-bi-kid-12.html",         // 7  Thiên Địa Bĩ
        "https://cohoc.net/dia-son-khiem-kid-15.html",        // 8  Địa Sơn Khiêm
        "https://cohoc.net/thuan-can-kid-52.html",            // 9  Thuần Cấn
        "https://cohoc.net/thuy-son-kien-kid-39.html",        // 10 Thủy Sơn Kiển
        "https://cohoc.net/phong-son-tiem-kid-53.html",       // 11 Phong Sơn Tiệm
        "https://cohoc.net/loi-son-tieu-qua-kid-62.html",     // 12 Lôi Sơn Tiểu Quá
        "https://cohoc.net/hoa-son-lu-kid-56.html",           // 13 Hỏa Sơn Lữ
        "https://cohoc.net/trach-son-ham-kid-31.html",        // 14 Trạch Sơn Hàm
        "https://cohoc.net/thien-son-don-kid-33.html",        // 15 Thiên Sơn Độn
        "https://cohoc.net/dia-thuy-su-kid-7.html",           // 16 Địa Thủy Sư
        "https://cohoc.net/son-thuy-mong-kid-4.html",         // 17 Sơn Thủy Mông
        "https://cohoc.net/thuan-kham-kid-29.html",           // 18 Thuần Khảm
        "https://cohoc.net/phong-thuy-hoan-kid-59.html",      // 19 Phong Thủy Hoán
        "https://cohoc.net/loi-thuy-giai-kid-40.html",        // 20 Lôi Thủy Giải
        "https://cohoc.net/hoa-thuy-vi-te-kid-64.html",       // 21 Hỏa Thủy Vị Tế
        "https://cohoc.net/trach-thuy-khon-kid-47.html",      // 22 Trạch Thủy Khốn
        "https://cohoc.net/thien-thuy-tung-kid-6.html",       // 23 Thiên Thủy Tụng
        "https://cohoc.net/dia-phong-thang-kid-46.html",      // 24 Địa Phong Thăng
        "https://cohoc.net/son-phong-co-kid-18.html",         // 25 Sơn Phong Cổ
        "https://cohoc.net/thuy-phong-tinh-kid-48.html",      // 26 Thủy Phong Tỉnh
        "https://cohoc.net/thuan-ton-kid-57.html",            // 27 Thuần Tốn
        "https://cohoc.net/loi-phong-hang-kid-32.html",       // 28 Lôi Phong Hằng
        "https://cohoc.net/hoa-phong-dinh-kid-50.html",       // 29 Hỏa Phong Đỉnh
        "https://cohoc.net/trach-phong-dai-qua-kid-28.html",  // 30 Trạch Phong Đại Quá
        "https://cohoc.net/thien-phong-cau-kid-44.html",      // 31 Thiên Phong Cấu
        "https://cohoc.net/dia-loi-phuc-kid-24.html",         // 32 Địa Lôi Phục
        "https://cohoc.net/son-loi-di-kid-27.html",           // 33 Sơn Lôi Di
        "https://cohoc.net/thuy-loi-truan-kid-3.html",        // 34 Thủy Lôi Truân
        "https://cohoc.net/phong-loi-%C3%ADch-kid-42.html",   // 35 Phong Lôi Ích
        "https://cohoc.net/thuan-chan-kid-51.html",            // 36 Thuần Chấn
        "https://cohoc.net/hoa-loi-phe-hap-kid-21.html",      // 37 Hỏa Lôi Phệ Hạp
        "https://cohoc.net/trach-loi-tuy-kid-17.html",        // 38 Trạch Lôi Tùy
        "https://cohoc.net/thien-loi-vo-vong-kid-25.html",    // 39 Thiên Lôi Vô Vọng
        "https://cohoc.net/dia-hoa-minh-di-kid-36.html",      // 40 Địa Hỏa Minh Di
        "https://cohoc.net/son-hoa-bi-kid-22.html",           // 41 Sơn Hỏa Bí
        "https://cohoc.net/thuy-hoa-ky-te-kid-63.html",       // 42 Thủy Hỏa Ký Tế
        "https://cohoc.net/phong-hoa-gia-nhan-kid-37.html",   // 43 Phong Hỏa Gia Nhân
        "https://cohoc.net/loi-hoa-phong-kid-55.html",        // 44 Lôi Hỏa Phong
        "https://cohoc.net/thuan-ly-kid-30.html",             // 45 Thuần Ly
        "https://cohoc.net/trach-hoa-cach-kid-49.html",       // 46 Trạch Hỏa Cách
        "https://cohoc.net/thien-hoa-dong-nhan-kid-13.html",  // 47 Thiên Hỏa Đồng Nhân
        "https://cohoc.net/dia-trach-lam-kid-19.html",        // 48 Địa Trạch Lâm
        "https://cohoc.net/son-trach-ton-kid-41.html",        // 49 Sơn Trạch Tổn
        "https://cohoc.net/thuy-trach-tiet-kid-60.html",      // 50 Thủy Trạch Tiết
        "https://cohoc.net/phong-trach-trung-phu-kid-61.html",// 51 Phong Trạch Trung Phu
        "https://cohoc.net/loi-trach-quy-muoi-kid-54.html",   // 52 Lôi Trạch Quy Muội
        "https://cohoc.net/hoa-trach-khue-kid-38.html",       // 53 Hỏa Trạch Khuê
        "https://cohoc.net/thuan-doai-kid-58.html",           // 54 Thuần Đoài
        "https://cohoc.net/thien-trach-ly-kid-10.html",       // 55 Thiên Trạch Lý
        "https://cohoc.net/dia-thien-thai-kid-11.html",       // 56 Địa Thiên Thái
        "https://cohoc.net/son-thien-dai-suc-kid-26.html",    // 57 Sơn Thiên Đại Súc
        "https://cohoc.net/thuy-thien-nhu-kid-5.html",        // 58 Thủy Thiên Nhu
        "https://cohoc.net/phong-thien-tieu-suc-kid-9.html",  // 59 Phong Thiên Tiểu Súc
        "https://cohoc.net/loi-thien-dai-trang-kid-34.html",  // 60 Lôi Thiên Đại Tráng
        "https://cohoc.net/hoa-thien-dai-huu-kid-14.html",    // 61 Hỏa Thiên Đại Hữu
        "https://cohoc.net/trach-thien-quai-kid-43.html",     // 62 Trạch Thiên Quải
        "https://cohoc.net/thuan-can-kid-1.html"              // 63 Thuần Càn
    ];

    /* King Wen order number for each hexagram (Fuxi index → KW number) */
    const KING_WEN_NUM = [
         2, 23,  8, 20, 16, 35, 45, 12,
        15, 52, 39, 53, 62, 56, 31, 33,
         7,  4, 29, 59, 40, 64, 47,  6,
        46, 18, 48, 57, 32, 50, 28, 44,
        24, 27,  3, 42, 51, 21, 17, 25,
        36, 22, 63, 37, 55, 30, 49, 13,
        19, 41, 60, 61, 54, 38, 58, 10,
        11, 26,  5,  9, 34, 14, 43,  1
    ];

    /* ── Layer config ── */
    const LUONG_NGHI = [
        { name: "Âm",   binary: "0", color: "#1a1a2e" },
        { name: "Dương", binary: "1", color: "#e8d5a3" }
    ];

    const TU_TUONG = [
        { name: "Thái Âm",     binary: "00", color: "#1a1a2e" },
        { name: "Thiếu Dương", binary: "01", color: "#4a5568" },
        { name: "Thiếu Âm",   binary: "10", color: "#9ca3af" },
        { name: "Thái Dương",  binary: "11", color: "#e8d5a3" }
    ];

    /* Bát Quái colors matched with data.js TRIGRAMS (Fuxi id order) */
    const BAGUA_COLORS = [
        "#8B6914", "#2E7D32", "#1565C0", "#78909C",
        "#795548", "#D32F2F", "#43A047", "#F9A825"
    ];

    let svg, containerW, containerH;
    let maxR;
    let activeFilter = null;
    let tooltipEl;

    function init(containerId) {
        const container = d3.select(containerId);
        const rect = container.node().getBoundingClientRect();
        containerW = rect.width || 900;
        containerH = Math.max(rect.height, 700);
        maxR = Math.min(containerW, containerH) / 2 - 10;

        /* Radii */
        const rTJ = maxR * 0.08;   // Thái Cực
        const rLN = maxR * 0.18;   // Lưỡng Nghi
        const rTT = maxR * 0.30;   // Tứ Tượng
        const rBQ = maxR * 0.48;   // Bát Quái
        const r64 = maxR * 0.78;   // 64 quẻ center line
        const rOuter = maxR * 0.98; // outer boundary

        svg = container.append("svg")
            .attr("viewBox", `0 0 ${containerW} ${containerH}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%")
            .style("height", `${containerH}px`);

        const g = svg.append("g")
            .attr("transform", `translate(${containerW / 2}, ${containerH / 2})`);

        /* Tooltip */
        tooltipEl = d3.select(containerId).append("div")
            .attr("class", "vd-tooltip hidden");

        /* ── 0. Thái Cực (Yin-Yang) ── */
        drawTaiChi(g, rTJ);

        /* ── 1. Lưỡng Nghi ── */
        drawRing(g, LUONG_NGHI, rTJ + 3, rLN, "ln");

        /* ── 2. Tứ Tượng ── */
        drawRing(g, TU_TUONG, rLN + 3, rTT, "tt");

        /* ── 3. Bát Quái ── */
        drawBaguaRing(g, rTT + 3, rBQ);

        /* ── 4. 64 Quẻ ── */
        draw64Ring(g, rBQ + 3, rOuter, r64);

        /* ── Outer circle border ── */
        g.append("circle")
            .attr("r", rOuter + 2)
            .attr("fill", "none")
            .attr("stroke", "rgba(255,255,255,0.12)")
            .attr("stroke-width", 1);
    }

    /* ── Thái Cực (simplified yin-yang) ── */
    function drawTaiChi(g, r) {
        // Dark background circle
        g.append("circle").attr("r", r).attr("fill", "#1a1a2e").attr("stroke", "#555").attr("stroke-width", 1);

        // Yin-Yang using arcs
        const halfPI = Math.PI;
        // White (Yang) half — right
        g.append("path")
            .attr("d", d3.arc()({ innerRadius: 0, outerRadius: r, startAngle: -halfPI / 2, endAngle: halfPI / 2 }))
            .attr("fill", "#e8d5a3");
        // Small circles
        g.append("circle").attr("cx", 0).attr("cy", -r / 4).attr("r", r / 5).attr("fill", "#e8d5a3");
        g.append("circle").attr("cx", 0).attr("cy",  r / 4).attr("r", r / 5).attr("fill", "#1a1a2e");
        // Dots
        g.append("circle").attr("cx", 0).attr("cy", -r / 4).attr("r", r / 12).attr("fill", "#1a1a2e");
        g.append("circle").attr("cx", 0).attr("cy",  r / 4).attr("r", r / 12).attr("fill", "#e8d5a3");

        // Label
        g.append("text")
            .attr("y", r + 14)
            .attr("text-anchor", "middle")
            .attr("font-size", "9px")
            .attr("fill", "var(--text-muted)")
            .text("太極");
    }

    /* ── Generic ring with equal slices ── */
    function drawRing(g, data, rInner, rOuter, cls) {
        const n = data.length;
        const pie = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);
        const arcGen = d3.arc().innerRadius(rInner).outerRadius(rOuter);
        const pieData = pie(data);

        const ringG = g.append("g").attr("class", `ring-${cls}`);

        ringG.selectAll("path")
            .data(pieData)
            .enter().append("path")
            .attr("d", arcGen)
            .attr("fill", (d, i) => data[i].color)
            .attr("stroke", "#333")
            .attr("stroke-width", 1)
            .style("opacity", 0.75);

        ringG.selectAll("text")
            .data(pieData)
            .enter().append("text")
            .attr("transform", d => `translate(${arcGen.centroid(d)})`)
            .attr("text-anchor", "middle")
            .attr("dy", "0.35em")
            .attr("font-size", n <= 2 ? "11px" : "9px")
            .attr("fill", (d, i) => {
                const c = data[i].color;
                return (c === "#e8d5a3" || c === "#9ca3af") ? "#222" : "#ddd";
            })
            .attr("font-weight", "600")
            .attr("pointer-events", "none")
            .text((d, i) => data[i].name);
    }

    /* ── Bát Quái ring with Octonion labels ── */
    function drawBaguaRing(g, rInner, rOuter) {
        const pie = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);
        const arcGen = d3.arc().innerRadius(rInner).outerRadius(rOuter);
        const pieData = pie(TRIGRAMS);
        const rMid = (rInner + rOuter) / 2;

        const bqG = g.append("g").attr("class", "ring-bq");

        // Slices
        bqG.selectAll("path")
            .data(pieData)
            .enter().append("path")
            .attr("d", arcGen)
            .attr("fill", (d, i) => BAGUA_COLORS[i])
            .attr("fill-opacity", 0.5)
            .attr("stroke", "#444")
            .attr("stroke-width", 1.5)
            .attr("class", (d, i) => `bq-slice bq-slice-${i}`)
            .style("cursor", "pointer")
            .on("click", (event, d) => {
                const idx = d.index;
                toggleBaguaFilter(idx, g);
            })
            .on("mouseenter", function (event, d) {
                d3.select(this).attr("fill-opacity", 0.85);
                const tri = TRIGRAMS[d.index];
                showTooltipAt(event, `
                    <strong style="color:${tri.color}">${tri.symbol} ${tri.name} (${tri.han})</strong><br>
                    ${tri.octonion} · ${tri.element} · ${tri.nature}<br>
                    <span style="font-size:0.8em;color:#aaa">${tri.desc}</span><br>
                    <span style="font-size:0.8em;color:#aaa">Nhị phân: ${tri.binary} = Quẻ ${d.index * 8} → ${d.index * 8 + 7}</span>
                `);
            })
            .on("mouseleave", function () {
                if (activeFilter === null || activeFilter !== d3.select(this).datum().index) {
                    d3.select(this).attr("fill-opacity", 0.5);
                }
                hideTooltip();
            });

        // Trigram symbol label (large)
        bqG.selectAll(".bq-sym")
            .data(pieData)
            .enter().append("text")
            .attr("class", "bq-sym")
            .attr("transform", d => {
                const a = (d.startAngle + d.endAngle) / 2 - Math.PI / 2;
                const r1 = rMid - 6;
                return `translate(${r1 * Math.cos(a)}, ${r1 * Math.sin(a)})`;
            })
            .attr("text-anchor", "middle")
            .attr("dy", "0.35em")
            .attr("font-size", "18px")
            .attr("fill", "#fff")
            .attr("pointer-events", "none")
            .text((d, i) => TRIGRAMS[i].symbol);

        // Name + Octonion label
        bqG.selectAll(".bq-name")
            .data(pieData)
            .enter().append("text")
            .attr("class", "bq-name")
            .attr("transform", d => {
                const a = (d.startAngle + d.endAngle) / 2 - Math.PI / 2;
                const r1 = rMid + 12;
                return `translate(${r1 * Math.cos(a)}, ${r1 * Math.sin(a)})`;
            })
            .attr("text-anchor", "middle")
            .attr("dy", "0.35em")
            .attr("font-size", "8.5px")
            .attr("fill", (d, i) => TRIGRAMS[i].color)
            .attr("font-weight", "600")
            .attr("pointer-events", "none")
            .text((d, i) => `${TRIGRAMS[i].name} (e${subscript(i)})`);
    }

    /* ── 64 Hexagrams ring ── */
    function draw64Ring(g, rInner, rOuter, r64Center) {
        const n = 64;
        const angleStep = (2 * Math.PI) / n;
        const pie = d3.pie().value(1).sort(null).startAngle(0).endAngle(2 * Math.PI);
        const arcGen = d3.arc().innerRadius(rInner).outerRadius(rOuter);
        const pieData = pie(HEXAGRAM_NAMES);

        const hexG = g.append("g").attr("class", "ring-64");

        // Background slices (colored by parent trigram)
        hexG.selectAll("path")
            .data(pieData)
            .enter().append("path")
            .attr("d", arcGen)
            .attr("fill", (d, i) => BAGUA_COLORS[Math.floor(i / 8)])
            .attr("fill-opacity", 0.12)
            .attr("stroke", "rgba(255,255,255,0.08)")
            .attr("stroke-width", 0.5)
            .attr("class", (d, i) => `hex-slice hex-slice-${i}`)
            .style("cursor", "pointer")
            .on("mouseenter", function (event, d) {
                const i = d.index;
                d3.select(this).attr("fill-opacity", 0.45).attr("stroke", "#fff").attr("stroke-width", 1.5);
                const triIdx = Math.floor(i / 8);
                const upperIdx = Math.floor(i / 8); // Upper trigram
                const lowerIdx = i % 8;             // Lower trigram
                const binStr = i.toString(2).padStart(6, '0');
                const kwNum = KING_WEN_NUM[i];
                showTooltipAt(event, `
                    <strong style="color:${BAGUA_COLORS[triIdx]}">
                        Quẻ ${kwNum}. ${HEXAGRAM_NAMES[i]} (${HEXAGRAM_FULLNAMES[i]})
                    </strong><br>
                    Nhị phân: <code>${binStr}</code> (Fuxi #${i})<br>
                    Thượng: ${TRIGRAMS[upperIdx].symbol} ${TRIGRAMS[upperIdx].name} (e${subscript(upperIdx)}) ·
                    Hạ: ${TRIGRAMS[lowerIdx].symbol} ${TRIGRAMS[lowerIdx].name} (e${subscript(lowerIdx)})<br>
                    <span style="font-size:0.8em;color:var(--accent-gold)">
                        e${subscript(upperIdx)} × e${subscript(lowerIdx)} = ${formatMult(upperIdx, lowerIdx)}
                        ${formatMultFull(upperIdx, lowerIdx)}
                    </span><br>
                    <span style="font-size:0.75em;color:#8cf;margin-top:2px;display:inline-block">
                        🔗 Click để xem chi tiết trên cohoc.net
                    </span>
                `);
            })
            .on("mouseleave", function () {
                d3.select(this).attr("fill-opacity", 0.12).attr("stroke", "rgba(255,255,255,0.08)").attr("stroke-width", 0.5);
                hideTooltip();
            })
            .on("click", function (event, d) {
                const i = d.index;
                const url = HEXAGRAM_URLS[i];
                if (url) window.open(url, '_blank');
            });

        // Hexagram symbols (6-line yao figures)
        hexG.selectAll(".hex-yao")
            .data(pieData)
            .enter().append("g")
            .attr("class", (d, i) => `hex-yao hex-yao-${i}`)
            .attr("pointer-events", "none")
            .each(function (d, i) {
                const angle = (d.startAngle + d.endAngle) / 2 - Math.PI / 2;
                const cx = r64Center * Math.cos(angle);
                const cy = r64Center * Math.sin(angle);
                const yaoG = d3.select(this)
                    .attr("transform", `translate(${cx}, ${cy}) rotate(${angle * 180 / Math.PI + 90})`);

                const binStr = i.toString(2).padStart(6, '0');
                const w = 8;
                const lineH = 2.2;
                const totalH = 6 * lineH;

                for (let bit = 0; bit < 6; bit++) {
                    const isYang = binStr[bit] === '1';
                    const drawY = (2.5 - bit) * lineH;

                    if (isYang) {
                        yaoG.append("rect")
                            .attr("x", -w / 2)
                            .attr("y", drawY - lineH * 0.35)
                            .attr("width", w)
                            .attr("height", lineH * 0.7)
                            .attr("fill", "#e0e0e0")
                            .attr("rx", 0.3);
                    } else {
                        const gap = w * 0.25;
                        const segW = (w - gap) / 2;
                        yaoG.append("rect")
                            .attr("x", -w / 2)
                            .attr("y", drawY - lineH * 0.35)
                            .attr("width", segW)
                            .attr("height", lineH * 0.7)
                            .attr("fill", "#e0e0e0")
                            .attr("rx", 0.3);
                        yaoG.append("rect")
                            .attr("x", gap / 2)
                            .attr("y", drawY - lineH * 0.35)
                            .attr("width", segW)
                            .attr("height", lineH * 0.7)
                            .attr("fill", "#e0e0e0")
                            .attr("rx", 0.3);
                    }
                }
            });

        // Hexagram number labels (outside)
        hexG.selectAll(".hex-num")
            .data(pieData)
            .enter().append("text")
            .attr("class", "hex-num")
            .attr("pointer-events", "none")
            .attr("transform", d => {
                const angle = (d.startAngle + d.endAngle) / 2 - Math.PI / 2;
                const rLabel = rOuter - 9;
                return `translate(${rLabel * Math.cos(angle)}, ${rLabel * Math.sin(angle)}) rotate(${angle * 180 / Math.PI + 90})`;
            })
            .attr("text-anchor", "middle")
            .attr("dy", "0.35em")
            .attr("font-size", "5.5px")
            .attr("fill", "rgba(255,255,255,0.5)")
            .text((d, i) => HEXAGRAM_NAMES[i]);
    }

    /* ── Bát Quái filter (click to highlight 8 hexagrams) ── */
    function toggleBaguaFilter(idx, g) {
        if (activeFilter === idx) {
            activeFilter = null;
            // Reset all
            g.selectAll(".hex-slice").transition().duration(300).attr("fill-opacity", 0.12);
            g.selectAll(".hex-yao").transition().duration(300).style("opacity", 1);
            g.selectAll(".bq-slice").attr("fill-opacity", 0.5).attr("stroke-width", 1.5);
        } else {
            activeFilter = idx;
            const startId = idx * 8;
            const endId = startId + 8;

            g.selectAll(".hex-slice").transition().duration(300)
                .attr("fill-opacity", (d, i) => (i >= startId && i < endId) ? 0.45 : 0.04);

            g.selectAll(".hex-yao").transition().duration(300)
                .style("opacity", (d, i) => (i >= startId && i < endId) ? 1 : 0.15);

            g.selectAll(".bq-slice").attr("fill-opacity", 0.2).attr("stroke-width", 1);
            g.select(`.bq-slice-${idx}`).attr("fill-opacity", 0.85).attr("stroke-width", 3).attr("stroke", "#fff");
        }
    }

    /* ── Tooltip helpers ── */
    function showTooltipAt(event, html) {
        tooltipEl
            .html(html)
            .classed("hidden", false)
            .style("left", (event.offsetX + 20) + "px")
            .style("top", (event.offsetY - 10) + "px");
    }

    function hideTooltip() {
        tooltipEl.classed("hidden", true);
    }

    /* ── Subscript digits ── */
    function subscript(n) {
        return String(n).split("").map(c => "₀₁₂₃₄₅₆₇₈₉"[parseInt(c)]).join("");
    }

    return { init };
})();
