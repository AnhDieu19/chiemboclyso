/**
 * Hà Đồ (河圖) — Interactive Visualization
 * ==========================================
 * SVG 1: Classic dot diagram (Sinh-Thành Ngũ Hành) with Viên-Phương frame + info panel
 * SVG 2: Tiên Thiên Bát Quái (先天八卦) circle with 4 labeled axes + interaction diagram
 *
 * Data source: HA_DO constant from data.js
 * Reference: Viên Như — "Công thức tính Hà Đồ thành Lạc Thư" (2019)
 */

const HaDoViz = (() => {
    /* ═══ Layout constants ═══ */
    const DOT_R   = 3.8;
    const SP      = 11;            // dot grid spacing
    const CX      = 155, CY = 155; // dot diagram center
    const DIST    = 78;            // direction cluster distance from center
    const GOFF    = 22;            // sinh ↔ thành group offset
    const MARGIN  = { top: 55, right: 265, bottom: 45, left: 55 };
    const FRAME_R = DIST + GOFF + 34;

    // Tiên Thiên circle radius
    const TT_R = 105;

    /* Element → color (fixed, independent of LacThuMode) */
    const EC = {
        "Thủy": "#4FC3F7", "Hỏa": "#EF5350",
        "Mộc":  "#66BB6A", "Kim":  "#B0BEC5", "Thổ": "#FFB300"
    };

    /* Tiên Thiên Bát Quái: 8 trigrams clockwise from top (Nam), 45° apart */
    const TRIGRAMS = [
        { name: "Càn",  sym: "☰", han: "乾", deg: 0,   dir: "Nam",     nature: "Trời",  bin: "111" },
        { name: "Tốn",  sym: "☴", han: "巽", deg: 45,  dir: "Tây Nam", nature: "Gió",   bin: "011" },
        { name: "Khảm", sym: "☵", han: "坎", deg: 90,  dir: "Tây",     nature: "Nước",  bin: "010" },
        { name: "Cấn",  sym: "☶", han: "艮", deg: 135, dir: "Tây Bắc", nature: "Núi",   bin: "001" },
        { name: "Khôn", sym: "☷", han: "坤", deg: 180, dir: "Bắc",     nature: "Đất",   bin: "000" },
        { name: "Chấn", sym: "☳", han: "震", deg: 225, dir: "Đông Bắc", nature: "Sấm",  bin: "100" },
        { name: "Ly",   sym: "☲", han: "離", deg: 270, dir: "Đông",    nature: "Lửa",   bin: "101" },
        { name: "Đoài", sym: "☱", han: "兌", deg: 315, dir: "Đông Nam", nature: "Đầm",  bin: "110" },
    ];

    /* 4 axes (Tứ Trục) — matching HA_DO_LAC_THU_TRANSFORM.haDo.axes */
    const AXES = [
        { id: 1, name: "Tung",  hanName: "縱軸", yin: "Dương", quai: ["Càn", "Khôn"],
          nums: "1-6 (Bắc·Âm), 2-7 (Nam·Dương)", degs: [0, 180], color: "#42A5F5",
          desc: "Dọc — Trục chính, mang lý số Dương khi biến dịch" },
        { id: 2, name: "Hoành", hanName: "橫軸", yin: "Âm",    quai: ["Ly", "Khảm"],
          nums: "3-8 (Đông·Dương), 4-9 (Tây·Âm)", degs: [270, 90], color: "#FF7043",
          desc: "Ngang — Trục phụ, mang lý số Âm khi biến dịch" },
        { id: 3, name: "Tả",   hanName: "左軸", yin: "Dương", quai: ["Đoài", "Chấn"],
          nums: "Không mang số", degs: [315, 225], color: "#66BB6A",
          desc: "Chéo trái — Chỉ mang quái, không số" },
        { id: 4, name: "Hữu",  hanName: "右軸", yin: "Âm",    quai: ["Tốn", "Cấn"],
          nums: "Không mang số", degs: [45, 135], color: "#AB47BC",
          desc: "Chéo phải — Chỉ mang quái, không số" },
    ];

    let containerId;

    /* ═══ Public API ═══ */
    function init(id) { containerId = id; render(); }

    function render() {
        const container = d3.select(containerId);
        container.selectAll("*").remove();

        /* ── SVG 1: Classic Dot Diagram + Info Panel ── */
        const W1 = CX * 2 + MARGIN.left + MARGIN.right;
        const H1 = CY * 2 + MARGIN.top + MARGIN.bottom;

        const svg1 = container.append("svg")
            .attr("viewBox", `0 0 ${W1} ${H1}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%").style("overflow", "visible");

        const g = svg1.append("g")
            .attr("transform", `translate(${MARGIN.left}, ${MARGIN.top})`);

        drawFrame(g);
        drawAllDots(g);
        drawCompass(g);
        drawInfoPanel(g);

        /* ── Divider title ── */
        container.append("div").attr("class", "hd-section-divider")
            .style("text-align", "center").style("margin", "20px 0 8px")
            .style("padding-top", ".8rem")
            .style("border-top", "1px solid var(--border-color)")
            .style("font-size", "15px").style("font-weight", "700")
            .style("color", "var(--accent-gold)")
            .html("Tiên Thiên Bát Quái 先天八卦 — Tứ Trục");

        /* ── SVG 2: Tiên Thiên Circle + Axes Panel ── */
        const W2 = 760, H2 = 420;
        const svg2 = container.append("svg")
            .attr("viewBox", `0 0 ${W2} ${H2}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%").style("overflow", "visible");

        // Arrow marker defs
        const defs = svg2.append("defs");
        ["#FF7043", "#66BB6A"].forEach((c, i) => {
            defs.append("marker").attr("id", `hd-arr-${i}`)
                .attr("viewBox", "0 0 10 6").attr("refX", 9).attr("refY", 3)
                .attr("markerWidth", 7).attr("markerHeight", 5).attr("orient", "auto")
                .append("path").attr("d", "M0,0 L10,3 L0,6 Z").attr("fill", c);
        });

        drawTienThien(svg2, W2, H2);
    }

    /* ═══════════════════════════════════════════
       SVG 1: Classic Hà Đồ Dot Diagram
       ═══════════════════════════════════════════ */

    /* ── Viên (circle) + Phương (square) cosmic frame ── */
    function drawFrame(g) {
        // Viên = Dương = Trời (outer circle, dashed)
        g.append("circle")
            .attr("cx", CX).attr("cy", CY).attr("r", FRAME_R)
            .attr("fill", "none")
            .attr("stroke", "rgba(79,195,247,0.12)")
            .attr("stroke-width", 1.5).attr("stroke-dasharray", "5,3");
        g.append("text")
            .attr("x", CX).attr("y", CY - FRAME_R - 6)
            .attr("text-anchor", "middle")
            .attr("font-size", "8px").attr("fill", "rgba(79,195,247,0.4)")
            .text("Viên ○ — Dương — Thể Hà Đồ");

        // Phương = Âm = Đất (inscribed square, dashed)
        const s = FRAME_R / Math.SQRT2;
        g.append("rect")
            .attr("x", CX - s).attr("y", CY - s)
            .attr("width", s * 2).attr("height", s * 2)
            .attr("fill", "none")
            .attr("stroke", "rgba(239,83,80,0.10)")
            .attr("stroke-width", 1.5).attr("stroke-dasharray", "5,3");
        g.append("text")
            .attr("x", CX + s + 4).attr("y", CY + s + 14)
            .attr("font-size", "7px").attr("fill", "rgba(239,83,80,0.35)")
            .text("Phương □ — Âm");

        // Subtle cross (Tung + Hoành axes hint)
        [0, Math.PI / 2].forEach(a => {
            g.append("line")
                .attr("x1", CX + FRAME_R * Math.cos(a))
                .attr("y1", CY - FRAME_R * Math.sin(a))
                .attr("x2", CX - FRAME_R * Math.cos(a))
                .attr("y2", CY + FRAME_R * Math.sin(a))
                .attr("stroke", "rgba(255,255,255,0.04)").attr("stroke-width", 1);
        });
    }

    /* ── All 5 × 2 dot clusters (sinh + thành per direction) ── */
    function drawAllDots(g) {
        const dirCfg = {
            "Bắc":   { dx: 0,     dy: DIST,   sdx: 0,  sdy: -1, horiz: true },
            "Nam":   { dx: 0,     dy: -DIST,  sdx: 0,  sdy: 1,  horiz: true },
            "Đông":  { dx: -DIST, dy: 0,      sdx: 1,  sdy: 0,  horiz: false },
            "Tây":   { dx: DIST,  dy: 0,      sdx: -1, sdy: 0,  horiz: false },
            "Trung": { dx: 0,     dy: 0,      sdx: 0,  sdy: 0,  horiz: true, center: true }
        };

        HA_DO.pairs.forEach(pair => {
            const d = dirCfg[pair.dir];
            const color = EC[pair.element];
            const sinhHollow = pair.sinhType === "Thiên";  // odd → hollow (Thiên)

            if (d.center) {
                // Center: 5 Thiên in cross + 10 Địa in ring
                _drawCluster(g, pair.sinh, CX, CY, color, sinhHollow, true);
                _drawRing(g, pair.thanh, CX, CY, 27, color, !sinhHollow);
            } else {
                // Sinh group (closer to diagram center)
                const sx = CX + d.dx + d.sdx * GOFF;
                const sy = CY + d.dy + d.sdy * GOFF;
                _drawCluster(g, pair.sinh, sx, sy, color, sinhHollow, d.horiz);

                // Thành group (at edge)
                const tx = CX + d.dx - d.sdx * GOFF;
                const ty = CY + d.dy - d.sdy * GOFF;
                _drawCluster(g, pair.thanh, tx, ty, color, !sinhHollow, d.horiz);
            }

            // Number label for each direction
            if (!d.center) {
                const lx = CX + d.dx;
                const ly = CY + d.dy;
                g.append("text")
                    .attr("x", lx + (d.horiz ? 0 : (d.sdx > 0 ? -2 : 2)))
                    .attr("y", ly + (d.horiz ? (d.sdy > 0 ? -8 : 8) : 3))
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px").attr("font-weight", "600")
                    .attr("fill", color).attr("opacity", 0.7)
                    .text(`${pair.sinh}·${pair.thanh}`);
            } else {
                g.append("text")
                    .attr("x", CX).attr("y", CY + 42)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px").attr("font-weight", "600")
                    .attr("fill", EC["Thổ"]).attr("opacity", 0.7)
                    .text("5·10");
            }
        });
    }

    /* ── Draw N dots in a grid cluster ── */
    function _drawCluster(g, n, cx, cy, color, hollow, horiz) {
        _dotPos(n, horiz).forEach(p => {
            hollow ? _hDot(g, cx + p.dx, cy + p.dy, color)
                   : _fDot(g, cx + p.dx, cy + p.dy, color);
        });
    }

    /* ── Draw N dots in a ring ── */
    function _drawRing(g, n, cx, cy, r, color, filled) {
        for (let i = 0; i < n; i++) {
            const a = (i / n) * 2 * Math.PI - Math.PI / 2;
            const x = cx + r * Math.cos(a), y = cy + r * Math.sin(a);
            filled ? _fDot(g, x, y, color) : _hDot(g, x, y, color);
        }
    }

    /** Hollow dot (Thiên = odd = Dương) */
    function _hDot(g, x, y, c) {
        g.append("circle").attr("cx", x).attr("cy", y).attr("r", DOT_R)
            .attr("fill", "none").attr("stroke", c)
            .attr("stroke-width", 1.5).attr("stroke-opacity", 0.9);
    }

    /** Filled dot (Địa = even = Âm) */
    function _fDot(g, x, y, c) {
        g.append("circle").attr("cx", x).attr("cy", y).attr("r", DOT_R)
            .attr("fill", c).attr("fill-opacity", 0.8);
    }

    /** Grid positions for N dots — returns [{dx, dy}] */
    function _dotPos(n, horiz) {
        const s = SP;
        const L = {
            1:  [[0, 0]],
            2:  [[-0.5, 0], [0.5, 0]],
            3:  [[-1, 0], [0, 0], [1, 0]],
            4:  [[-0.5, -0.5], [0.5, -0.5], [-0.5, 0.5], [0.5, 0.5]],
            5:  [[0, -1], [-1, 0], [0, 0], [1, 0], [0, 1]],   // cross ✚
            6:  [[-1, -0.5], [0, -0.5], [1, -0.5],
                 [-1,  0.5], [0,  0.5], [1,  0.5]],
            7:  [[-1, -1], [0, -1], [1, -1],
                                    [0,  0],
                 [-1,  1], [0,  1], [1,  1]],
            8:  [[-1.5, -0.5], [-0.5, -0.5], [0.5, -0.5], [1.5, -0.5],
                 [-1.5,  0.5], [-0.5,  0.5], [0.5,  0.5], [1.5,  0.5]],
            9:  [[-1, -1], [0, -1], [1, -1],
                 [-1,  0], [0,  0], [1,  0],
                 [-1,  1], [0,  1], [1,  1]],   // 3×3
            10: [[-2, -0.5], [-1, -0.5], [0, -0.5], [1, -0.5], [2, -0.5],
                 [-2,  0.5], [-1,  0.5], [0,  0.5], [1,  0.5], [2,  0.5]],
        };
        return (L[n] || L[1]).map(([c, r]) => ({
            dx: (horiz ? c : r) * s,
            dy: (horiz ? r : c) * s
        }));
    }

    /* ── Compass direction labels ── */
    function drawCompass(g) {
        const lR = FRAME_R + 16;
        // Top = Nam (Hỏa)
        g.append("text").attr("x", CX).attr("y", CY - lR)
            .attr("text-anchor", "middle").attr("font-size", "12px").attr("font-weight", "600")
            .attr("fill", EC["Hỏa"]).text("Nam — Hỏa 🔥");
        // Bottom = Bắc (Thủy)
        g.append("text").attr("x", CX).attr("y", CY + lR + 14)
            .attr("text-anchor", "middle").attr("font-size", "12px").attr("font-weight", "600")
            .attr("fill", EC["Thủy"]).text("Bắc — Thủy 💧");
        // Left = Đông (Mộc)
        g.append("text")
            .attr("transform", `translate(${CX - lR - 6}, ${CY}) rotate(-90)`)
            .attr("text-anchor", "middle").attr("font-size", "12px").attr("font-weight", "600")
            .attr("fill", EC["Mộc"]).text("Đông — Mộc 🌿");
        // Right = Tây (Kim)
        g.append("text")
            .attr("transform", `translate(${CX + lR + 6}, ${CY}) rotate(90)`)
            .attr("text-anchor", "middle").attr("font-size", "12px").attr("font-weight", "600")
            .attr("fill", EC["Kim"]).text("Tây — Kim ⚙️");
    }

    /* ── Info panel (right side) ── */
    function drawInfoPanel(g) {
        const ix = CX * 2 + 50;
        const ig = g.append("g").attr("transform", `translate(${ix}, 0)`);

        // Title
        ig.append("text").attr("y", -10)
            .attr("font-size", "14px").attr("font-weight", "700")
            .attr("fill", "var(--accent-red)")
            .text("Hà Đồ — 河圖");
        ig.append("text").attr("y", 8)
            .attr("font-size", "10px").attr("fill", "var(--text-muted)")
            .text("Thiên Sinh Địa Thành — Ngũ Hành Sinh Thành");

        // Totals
        ig.append("text").attr("y", 32)
            .attr("font-size", "11px").attr("fill", "var(--accent-gold)")
            .text(`Tổng = ${HA_DO.totalSum}  ·  Thiên ${HA_DO.thienSum}  ·  Địa ${HA_DO.diaSum}`);

        // Dot legend
        ig.append("text").attr("y", 54)
            .attr("font-size", "10px").attr("font-weight", "600")
            .attr("fill", "var(--text-primary)").text("Ký hiệu:");
        // hollow
        ig.append("circle").attr("cx", 6).attr("cy", 68).attr("r", 4)
            .attr("fill", "none").attr("stroke", "#fff").attr("stroke-width", 1.5);
        ig.append("text").attr("x", 16).attr("y", 72)
            .attr("font-size", "9px").attr("fill", "var(--text-secondary)")
            .text("○ Thiên (lẻ: 1,3,5,7,9) — Dương");
        // filled
        ig.append("circle").attr("cx", 6).attr("cy", 86).attr("r", 4)
            .attr("fill", "#fff").attr("fill-opacity", 0.7);
        ig.append("text").attr("x", 16).attr("y", 90)
            .attr("font-size", "9px").attr("fill", "var(--text-secondary)")
            .text("● Địa (chẵn: 2,4,6,8,10) — Âm");

        // ── Sinh-Thành pairs ──
        ig.append("text").attr("y", 115)
            .attr("font-size", "12px").attr("font-weight", "700")
            .attr("fill", "var(--accent-gold)")
            .text("Ngũ Hành Sinh Thành");

        HA_DO.pairs.forEach((p, i) => {
            const c = EC[p.element];
            const y = 133 + i * 20;
            // Element color dot
            ig.append("circle").attr("cx", 4).attr("cy", y - 3).attr("r", 4)
                .attr("fill", c).attr("fill-opacity", 0.7);
            // Pair numbers
            ig.append("text").attr("x", 14).attr("y", y)
                .attr("font-size", "10px").attr("font-weight", "600").attr("fill", c)
                .text(`${p.sinh}–${p.thanh}  ${p.element} (${p.dir})`);
            // Description
            ig.append("text").attr("x", 14).attr("y", y + 12)
                .attr("font-size", "8px").attr("fill", "var(--text-muted)")
                .text(p.desc);
        });

        // ── Thể & Dụng ──
        const tdY = 133 + 5 * 20 + 20;
        ig.append("text").attr("y", tdY)
            .attr("font-size", "12px").attr("font-weight", "700")
            .attr("fill", "var(--accent-blue)")
            .text("Thể & Dụng");
        ig.append("text").attr("y", tdY + 18)
            .attr("font-size", "10px").attr("fill", "var(--text-secondary)")
            .text("河圖體圓而用方");
        ig.append("text").attr("y", tdY + 34)
            .attr("font-size", "9px").attr("fill", "var(--text-muted)")
            .text("Hà Đồ thể viên (tròn) nhi dụng phương (vuông)");
        ig.append("text").attr("y", tdY + 52)
            .attr("font-size", "10px").attr("fill", AXES[0].color)
            .text("Thể = Trục Tung (Càn–Khôn) — Dương");
        ig.append("text").attr("y", tdY + 68)
            .attr("font-size", "10px").attr("fill", AXES[1].color)
            .text("Dụng = Trục Hoành (Khảm–Ly) — Âm");
    }

    /* ═══════════════════════════════════════════
       SVG 2: Tiên Thiên Bát Quái + Tứ Trục
       ═══════════════════════════════════════════ */

    function drawTienThien(svg, W, H) {
        const cx = 185, cy = H / 2;
        const ttG = svg.append("g").attr("transform", `translate(${cx}, ${cy})`);

        // Title
        ttG.append("text").attr("y", -TT_R - 28)
            .attr("text-anchor", "middle")
            .attr("font-size", "13px").attr("font-weight", "700")
            .attr("fill", "var(--accent-red)")
            .text("Hà Đồ — Tiên Thiên Bát Quái");
        ttG.append("text").attr("y", -TT_R - 14)
            .attr("text-anchor", "middle")
            .attr("font-size", "9px").attr("fill", "var(--text-muted)")
            .text("Nam trên · Bắc dưới — Sơ đồ vũ trụ bản thể");

        // Outer circle
        ttG.append("circle").attr("r", TT_R)
            .attr("fill", "none")
            .attr("stroke", "rgba(255,255,255,0.08)").attr("stroke-width", 1.5);

        // Center 5-10 dot
        ttG.append("circle").attr("r", 12)
            .attr("fill", EC["Thổ"]).attr("fill-opacity", 0.12)
            .attr("stroke", EC["Thổ"]).attr("stroke-width", 1).attr("stroke-opacity", 0.4);
        ttG.append("text").attr("dy", "0.35em").attr("text-anchor", "middle")
            .attr("font-size", "9px").attr("font-weight", "700")
            .attr("fill", EC["Thổ"]).text("5·10");

        // ── 4 Axes as colored lines ──
        AXES.forEach(ax => {
            const a1 = ax.degs[0] * Math.PI / 180;
            const a2 = ax.degs[1] * Math.PI / 180;
            // Convention: 0° = top (Nam), CW. SVG: x = sin(a), y = -cos(a)
            const x1 = TT_R * Math.sin(a1), y1 = -TT_R * Math.cos(a1);
            const x2 = TT_R * Math.sin(a2), y2 = -TT_R * Math.cos(a2);

            ttG.append("line")
                .attr("x1", x1).attr("y1", y1).attr("x2", x2).attr("y2", y2)
                .attr("stroke", ax.color).attr("stroke-width", 1.8)
                .attr("stroke-opacity", 0.45);

            // Axis label near center (offset perpendicular to axis)
            const midDeg = (ax.degs[0] + 22) * Math.PI / 180;
            const lx = 38 * Math.sin(midDeg), ly = -38 * Math.cos(midDeg);
            ttG.append("text").attr("x", lx).attr("y", ly)
                .attr("text-anchor", "middle").attr("dy", "0.35em")
                .attr("font-size", "7px").attr("fill", ax.color).attr("opacity", 0.75)
                .text(`${ax.name}(${ax.yin})`);
        });

        // ── 8 Trigrams around circle ──
        TRIGRAMS.forEach(t => {
            const a = t.deg * Math.PI / 180;
            const x = (TT_R + 32) * Math.sin(a);
            const y = -(TT_R + 32) * Math.cos(a);

            // Trigram symbol (large)
            ttG.append("text").attr("x", x).attr("y", y - 4)
                .attr("text-anchor", "middle")
                .attr("font-size", "18px").attr("fill", "#fff").attr("opacity", 0.55)
                .text(t.sym);
            // Name
            ttG.append("text").attr("x", x).attr("y", y + 12)
                .attr("text-anchor", "middle")
                .attr("font-size", "10px").attr("font-weight", "600")
                .attr("fill", "#fff")
                .text(t.name);
            // Direction + nature
            ttG.append("text").attr("x", x).attr("y", y + 24)
                .attr("text-anchor", "middle")
                .attr("font-size", "7px").attr("fill", "var(--text-muted)")
                .text(`${t.dir} · ${t.nature}`);
        });

        // ── Rotation indicators (nội tại + ngoại tại) ──
        _drawRotationArcs(ttG);

        // ── 4 Quadrants labels (A, B, C, D) ──
        const qR = TT_R * 0.55;
        const quads = [
            { label: "A", deg: 45,  desc: "Thành" },
            { label: "B", deg: 135, desc: "Trụ" },
            { label: "C", deg: 225, desc: "Hoại" },
            { label: "D", deg: 315, desc: "Không" },
        ];
        quads.forEach(q => {
            const a = q.deg * Math.PI / 180;
            const qx = qR * Math.sin(a), qy = -qR * Math.cos(a);
            ttG.append("text").attr("x", qx).attr("y", qy)
                .attr("text-anchor", "middle").attr("dy", "0.35em")
                .attr("font-size", "10px").attr("font-weight", "600")
                .attr("fill", "rgba(255,255,255,0.12)")
                .text(q.label);
        });

        // ── Right panel: Axis table + interaction ──
        _drawAxisPanel(svg, W, H);
    }

    /* ── Rotation arcs (CW + CCW indicators on circle) ── */
    function _drawRotationArcs(g) {
        const r = TT_R + 8;
        // CW arc (ngoại tại) — right side, orange
        g.append("path")
            .attr("d", _arc(0, 0, r, -50, 50))
            .attr("fill", "none")
            .attr("stroke", "#FF7043").attr("stroke-width", 1.5).attr("stroke-opacity", 0.35)
            .attr("marker-end", "url(#hd-arr-0)");
        g.append("text").attr("x", r + 12).attr("y", 4)
            .attr("font-size", "7px").attr("fill", "#FF7043").attr("opacity", 0.55)
            .text("CW");
        g.append("text").attr("x", r + 12).attr("y", 14)
            .attr("font-size", "6px").attr("fill", "#FF7043").attr("opacity", 0.4)
            .text("Ngoại tại");

        // CCW arc (nội tại) — left side, green
        g.append("path")
            .attr("d", _arc(0, 0, r, 230, 130))
            .attr("fill", "none")
            .attr("stroke", "#66BB6A").attr("stroke-width", 1.5).attr("stroke-opacity", 0.35)
            .attr("marker-end", "url(#hd-arr-1)");
        g.append("text").attr("x", -r - 28).attr("y", 4)
            .attr("font-size", "7px").attr("fill", "#66BB6A").attr("opacity", 0.55)
            .text("CCW");
        g.append("text").attr("x", -r - 28).attr("y", 14)
            .attr("font-size", "6px").attr("fill", "#66BB6A").attr("opacity", 0.4)
            .text("Nội tại");
    }

    /** SVG arc path: startDeg→endDeg (0°=top, CW) */
    function _arc(cx, cy, r, startDeg, endDeg) {
        const toRad = d => (d - 90) * Math.PI / 180;
        const x1 = cx + r * Math.cos(toRad(startDeg));
        const y1 = cy + r * Math.sin(toRad(startDeg));
        const x2 = cx + r * Math.cos(toRad(endDeg));
        const y2 = cy + r * Math.sin(toRad(endDeg));
        const sweep = 1;
        const large = Math.abs(endDeg - startDeg) > 180 ? 1 : 0;
        return `M${x1},${y1} A${r},${r} 0 ${large},${sweep} ${x2},${y2}`;
    }

    /* ── Right panel: Axis properties + Tương Tác ── */
    function _drawAxisPanel(svg, W, H) {
        const px = 395, py = 18;
        const pg = svg.append("g").attr("transform", `translate(${px}, ${py})`);

        pg.append("text").attr("y", 0)
            .attr("font-size", "13px").attr("font-weight", "700")
            .attr("fill", "var(--accent-gold)")
            .text("Tứ Trục (四軸)");

        AXES.forEach((ax, i) => {
            const y = 20 + i * 54;
            // Background box
            pg.append("rect")
                .attr("x", 0).attr("y", y)
                .attr("width", 330).attr("height", 44).attr("rx", 6)
                .attr("fill", ax.color).attr("fill-opacity", 0.07)
                .attr("stroke", ax.color).attr("stroke-width", 1).attr("stroke-opacity", 0.25);

            // Axis ID circle
            pg.append("circle")
                .attr("cx", 18).attr("cy", y + 22).attr("r", 11)
                .attr("fill", ax.color).attr("fill-opacity", 0.2);
            pg.append("text").attr("x", 18).attr("y", y + 26)
                .attr("text-anchor", "middle")
                .attr("font-size", "12px").attr("font-weight", "700")
                .attr("fill", ax.color).text(ax.id);

            // Axis name + yin/yang
            pg.append("text").attr("x", 38).attr("y", y + 15)
                .attr("font-size", "11px").attr("font-weight", "600")
                .attr("fill", "#fff")
                .text(`Trục ${ax.name} ${ax.hanName} — ${ax.yin}`);

            // Quai pair + numbers
            pg.append("text").attr("x", 38).attr("y", y + 30)
                .attr("font-size", "9px").attr("fill", "var(--text-secondary)")
                .text(`${ax.quai.join(" – ")}  │  ${ax.nums}`);

            // Desc
            pg.append("text").attr("x", 38).attr("y", y + 42)
                .attr("font-size", "7px").attr("fill", "var(--text-muted)")
                .text(ax.desc);

            // Thể / Dụng badge
            if (ax.id === 1) {
                pg.append("rect").attr("x", 280).attr("y", y + 4).attr("width", 36).attr("height", 16).attr("rx", 8)
                    .attr("fill", "var(--accent-blue)").attr("fill-opacity", 0.2);
                pg.append("text").attr("x", 298).attr("y", y + 16)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px").attr("font-weight", "700")
                    .attr("fill", "var(--accent-blue)").text("THỂ");
            }
            if (ax.id === 2) {
                pg.append("rect").attr("x", 280).attr("y", y + 4).attr("width", 36).attr("height", 16).attr("rx", 8)
                    .attr("fill", "var(--accent-orange)").attr("fill-opacity", 0.2);
                pg.append("text").attr("x", 298).attr("y", y + 16)
                    .attr("text-anchor", "middle")
                    .attr("font-size", "8px").attr("font-weight", "700")
                    .attr("fill", "var(--accent-orange)").text("DỤNG");
            }
        });

        // ── Tương Tác section ──
        const intY = 20 + 4 * 54 + 12;
        pg.append("text").attr("y", intY)
            .attr("font-size", "12px").attr("font-weight", "700")
            .attr("fill", "var(--accent-gold)")
            .text("Tương Tác Âm Dương");

        // Nội tại
        pg.append("rect")
            .attr("x", 0).attr("y", intY + 8)
            .attr("width", 330).attr("height", 32).attr("rx", 6)
            .attr("fill", "#66BB6A").attr("fill-opacity", 0.06)
            .attr("stroke", "#66BB6A").attr("stroke-width", 1).attr("stroke-opacity", 0.2);
        pg.append("text").attr("x", 8).attr("y", intY + 22)
            .attr("font-size", "10px").attr("font-weight", "600")
            .attr("fill", "#66BB6A")
            .text("↺ Nội tại (ngược KĐH): 4 → 1 → 2 → 3 → 4");
        pg.append("text").attr("x", 8).attr("y", intY + 36)
            .attr("font-size", "8px").attr("fill", "var(--text-muted)")
            .text("Hữu→Tung→Hoành→Tả — Biến dịch nội tại Hà Đồ");

        // Ngoại tại
        pg.append("rect")
            .attr("x", 0).attr("y", intY + 48)
            .attr("width", 330).attr("height", 32).attr("rx", 6)
            .attr("fill", "#FF7043").attr("fill-opacity", 0.06)
            .attr("stroke", "#FF7043").attr("stroke-width", 1).attr("stroke-opacity", 0.2);
        pg.append("text").attr("x", 8).attr("y", intY + 62)
            .attr("font-size", "10px").attr("font-weight", "600")
            .attr("fill", "#FF7043")
            .text("↻ Ngoại tại (thuận KĐH): 1 → 4 → 3 → 2 → 1");
        pg.append("text").attr("x", 8).attr("y", intY + 76)
            .attr("font-size", "8px").attr("fill", "var(--text-muted)")
            .text("Tung→Hữu→Tả→Hoành — Sinh ra Lạc Thư (Hậu Thiên)");

        // ── Binary complement note ──
        const binY = intY + 90;
        pg.append("text").attr("y", binY)
            .attr("font-size", "10px").attr("font-weight", "600")
            .attr("fill", "var(--accent-purple)")
            .text("Đối Quái: Nhị phân bù");
        pg.append("text").attr("y", binY + 16)
            .attr("font-size", "9px").attr("fill", "var(--text-secondary)")
            .text("Càn 111 + Khôn 000 = 111  ·  Ly 101 + Khảm 010 = 111");
        pg.append("text").attr("y", binY + 30)
            .attr("font-size", "9px").attr("fill", "var(--text-secondary)")
            .text("Chấn 100 + Tốn 011 = 111  ·  Cấn 001 + Đoài 110 = 111");
    }

    return { init, render };
})();
