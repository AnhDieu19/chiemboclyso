/**
 * Thái Ất · Kỳ Môn Độn Giáp — Mathematical Data Model
 * =====================================================
 * Core constants, cyclic groups, mappings, and structures
 * shared across all visualization modules.
 */

/* ═══════════════ 1. Lạc Thư Magic Square ═══════════════ */

/**
 * Current active mode: 'TQ' (Trung Quốc standard) or 'DV' (Đại Việt)
 * Changed via LacThuMode.toggle() or LacThuMode.set()
 */
const LacThuMode = {
    _current: 'TQ',
    get current() { return this._current; },
    set current(v) { this._current = v; },
    toggle() { this._current = this._current === 'TQ' ? 'DV' : 'TQ'; return this._current; },
    isTQ() { return this._current === 'TQ'; },
    isDV() { return this._current === 'DV'; },
    label() { return this._current === 'TQ' ? 'Trung Quốc (Hậu Thiên)' : 'Đại Việt'; },
};

/**
 * Cửu Tinh (九星) — Nine Flying Stars
 * Phi Tinh traditional star names and colors, shared by both TQ and DV.
 * Each number 1–9 has a fixed star name and traditional color.
 */
const CUU_TINH = [
    null,
    { id: 1, star: "Nhất Bạch",  hanStar: "一白", fullName: "Tham Lang",   starColor: "#B3D4FC", starColorName: "Bạch (Trắng)" },
    { id: 2, star: "Nhị Hắc",    hanStar: "二黑", fullName: "Cự Môn",     starColor: "#424242", starColorName: "Hắc (Đen)" },
    { id: 3, star: "Tam Bích",   hanStar: "三碧", fullName: "Lộc Tồn",    starColor: "#00897B", starColorName: "Bích (Ngọc)" },
    { id: 4, star: "Tứ Lục",     hanStar: "四綠", fullName: "Văn Xương",   starColor: "#43A047", starColorName: "Lục (Xanh lá)" },
    { id: 5, star: "Ngũ Hoàng",  hanStar: "五黃", fullName: "Liêm Trinh",  starColor: "#FFB300", starColorName: "Hoàng (Vàng)" },
    { id: 6, star: "Lục Bạch",   hanStar: "六白", fullName: "Vũ Khúc",    starColor: "#B0BEC5", starColorName: "Bạch (Trắng)" },
    { id: 7, star: "Thất Xích",  hanStar: "七赤", fullName: "Phá Quân",    starColor: "#E53935", starColorName: "Xích (Đỏ)" },
    { id: 8, star: "Bát Bạch",   hanStar: "八白", fullName: "Tả Phụ",     starColor: "#ECEFF1", starColorName: "Bạch (Trắng)" },
    { id: 9, star: "Cửu Tử",     hanStar: "九紫", fullName: "Hữu Bật",    starColor: "#8E24AA", starColorName: "Tử (Tím)" },
];

/**
 * Trung Quốc standard: Nam on top, Ly=9, Đoài=7, Tốn=SE, Khôn=SW
 * Elements: Hậu Thiên Bát Quái (trigram-based)
 * Colors: Phi Tinh traditional colors (Bạch/Hắc/Bích/Lục/Hoàng/Xích/Tử)
 */
const LAC_THU_TQ = {
    mode: 'TQ',
    modeName: 'Trung Quốc (Hậu Thiên)',
    orientation: 'Nam trên — Bắc dưới',
    matrix: [
        [4, 9, 2],  // Tốn(SE), Ly(S), Khôn(SW)
        [3, 5, 7],  // Chấn(E), Trung(Center), Đoài(W)
        [8, 1, 6],  // Cấn(NE), Khảm(N), Càn(NW)
    ],
    magicConstant: 15,
    palaces: [
        null,
        { id: 1, name: "Khảm",  han: "坎", symbol: "☵", element: "Thủy", haDoElement: "Thủy", star: "Nhất Bạch",  dir: "Bắc",     can: null,   row: 2, col: 1, color: "#1976D2" },
        { id: 2, name: "Khôn",  han: "坤", symbol: "☷", element: "Thổ",  haDoElement: "Hỏa",  star: "Nhị Hắc",    dir: "Tây Nam",  can: null,   row: 0, col: 2, color: "#424242" },
        { id: 3, name: "Chấn",  han: "震", symbol: "☳", element: "Mộc",  haDoElement: "Mộc",  star: "Tam Bích",   dir: "Đông",     can: null,   row: 1, col: 0, color: "#00897B" },
        { id: 4, name: "Tốn",   han: "巽", symbol: "☴", element: "Mộc",  haDoElement: "Kim",  star: "Tứ Lục",     dir: "Đông Nam", can: null,   row: 0, col: 0, color: "#43A047" },
        { id: 5, name: "Trung", han: "中", symbol: "◎", element: "Thổ",  haDoElement: "Thổ",  star: "Ngũ Hoàng",  dir: "Trung",    can: null,   row: 1, col: 1, color: "#FFB300" },
        { id: 6, name: "Càn",   han: "乾", symbol: "☰", element: "Kim",  haDoElement: "Thủy", star: "Lục Bạch",   dir: "Tây Bắc",  can: null,   row: 2, col: 2, color: "#B0BEC5" },
        { id: 7, name: "Đoài",  han: "兌", symbol: "☱", element: "Kim",  haDoElement: "Hỏa",  star: "Thất Xích",  dir: "Tây",      can: null,   row: 1, col: 2, color: "#E53935" },
        { id: 8, name: "Cấn",   han: "艮", symbol: "☶", element: "Thổ",  haDoElement: "Mộc",  star: "Bát Bạch",   dir: "Đông Bắc", can: null,   row: 2, col: 0, color: "#CFD8DC" },
        { id: 9, name: "Ly",    han: "離", symbol: "☲", element: "Hỏa",  haDoElement: "Kim",  star: "Cửu Tử",     dir: "Nam",      can: null,   row: 0, col: 1, color: "#8E24AA" },
    ],
    opposite(p) { return p === 5 ? 5 : 10 - p; },
    lines: [
        [4, 9, 2], [3, 5, 7], [8, 1, 6],
        [4, 3, 8], [9, 5, 1], [2, 7, 6],
        [4, 5, 6], [2, 5, 8],
    ],
    /** Direction labels for grid edges (top, right, bottom, left) */
    compassLabels: {
        top: "Nam — Hỏa 🔥", bottom: "Bắc — Thủy 💧",
        left: "Đông — Mộc 🌿", right: "Tây — Kim ⚙️"
    }
};

/**
 * Đại Việt variant: Bắc on top, Ly=7, Đoài=9, Tốn=SW, Khôn=SE
 * Mỗi Quái gán Thiên Can theo truyền thống Việt
 */
const LAC_THU_DV = {
    mode: 'DV',
    modeName: 'Đại Việt',
    orientation: 'Bắc trên — Nam dưới',
    matrix: [
        [6, 1, 8],  // Càn(NW), Khảm(N), Cấn(NE)
        [9, 5, 3],  // Đoài(W), Trung(C), Chấn(E)
        [4, 7, 2],  // Tốn(SW), Ly(S), Khôn(SE)
    ],
    magicConstant: 15,
    palaces: [
        null,
        { id: 1, name: "Khảm",  han: "坎", symbol: "☵", element: "Thủy", haDoElement: "Thủy", star: "Nhất Bạch",  dir: "Bắc",      can: "Quý",  row: 0, col: 1, color: "#1565C0" },
        { id: 2, name: "Khôn",  han: "坤", symbol: "☷", element: "Hỏa",  haDoElement: "Hỏa",  star: "Nhị Hắc",    dir: "Đông Nam",  can: "Ất",   row: 2, col: 2, color: "#D32F2F" },
        { id: 3, name: "Chấn",  han: "震", symbol: "☳", element: "Mộc",  haDoElement: "Mộc",  star: "Tam Bích",   dir: "Đông",      can: "Bính", row: 1, col: 2, color: "#2E7D32" },
        { id: 4, name: "Tốn",   han: "巽", symbol: "☴", element: "Kim",  haDoElement: "Kim",  star: "Tứ Lục",     dir: "Tây Nam",   can: "Đinh", row: 2, col: 0, color: "#E0E0E0" },
        { id: 5, name: "Trung", han: "中", symbol: "◎", element: "Thổ",  haDoElement: "Thổ",  star: "Ngũ Hoàng",  dir: "Trung",     can: "Mậu/Quí", row: 1, col: 1, color: "#FFB300" },
        { id: 6, name: "Càn",   han: "乾", symbol: "☰", element: "Thủy", haDoElement: "Thủy", star: "Lục Bạch",   dir: "Tây Bắc",   can: "Nhâm", row: 0, col: 0, color: "#1565C0" },
        { id: 7, name: "Ly",    han: "離", symbol: "☲", element: "Hỏa",  haDoElement: "Hỏa",  star: "Thất Xích",  dir: "Nam",       can: "Canh", row: 2, col: 1, color: "#D32F2F" },
        { id: 8, name: "Cấn",   han: "艮", symbol: "☶", element: "Mộc",  haDoElement: "Mộc",  star: "Bát Bạch",   dir: "Đông Bắc",  can: "Tân",  row: 0, col: 2, color: "#2E7D32" },
        { id: 9, name: "Đoài",  han: "兌", symbol: "☱", element: "Kim",  haDoElement: "Kim",  star: "Cửu Tử",     dir: "Tây",       can: "Nhâm", row: 1, col: 0, color: "#E0E0E0" },
    ],
    opposite(p) { return p === 5 ? 5 : 10 - p; },
    lines: [
        [6, 1, 8], [9, 5, 3], [4, 7, 2],
        [6, 9, 4], [1, 5, 7], [8, 3, 2],
        [6, 5, 2], [8, 5, 4],
    ],
    compassLabels: {
        top: "Bắc — Thủy 💧", bottom: "Nam — Hỏa 🔥",
        left: "Tây — Kim ⚙️", right: "Đông — Mộc 🌿"
    }
};

/** Dynamic accessor — always returns the active configuration */
const LAC_THU = new Proxy({}, {
    get(_, prop) {
        const cfg = LacThuMode.isTQ() ? LAC_THU_TQ : LAC_THU_DV;
        if (prop in cfg) return cfg[prop];
        return undefined;
    }
});

/* ═══════════════ 1b. Hà Đồ (河圖) — Sinh Thành Ngũ Hành ═══════════════ */

/**
 * Hà Đồ — Thiên Sinh Địa Thành
 * ==============================
 * Thiên nhất sinh Thủy, Địa lục thành chi.    (1-6 → Thủy, Bắc)
 * Địa nhị sinh Hỏa, Thiên thất thành chi.     (2-7 → Hỏa, Nam)
 * Thiên tam sinh Mộc, Địa bát thành chi.      (3-8 → Mộc, Đông)
 * Địa tứ sinh Kim, Thiên cửu thành chi.       (4-9 → Kim, Tây)
 * Thiên ngũ sinh Thổ, Địa thập thành chi.     (5-10 → Thổ, Trung)
 *
 * Sinh số (1–5): số tạo thành, Thành số (6–10): số hoàn thành (= sinh + 5).
 * Thiên (lẻ): 1, 3, 5, 7, 9.  Địa (chẵn): 2, 4, 6, 8, 10.
 */
const HA_DO = {
    name: "Hà Đồ (河圖)",
    desc: "Thiên Sinh Địa Thành — Ngũ Hành Sinh Thành Số",

    /** Five Sinh-Thành pairs: each pair shares one element and one compass direction */
    pairs: [
        { sinh: 1, thanh: 6,  element: "Thủy", dir: "Bắc",   sinhType: "Thiên", thanhType: "Địa",
          desc: "Thiên nhất sinh Thủy, Địa lục thành chi" },
        { sinh: 2, thanh: 7,  element: "Hỏa",  dir: "Nam",   sinhType: "Địa",   thanhType: "Thiên",
          desc: "Địa nhị sinh Hỏa, Thiên thất thành chi" },
        { sinh: 3, thanh: 8,  element: "Mộc",  dir: "Đông",   sinhType: "Thiên", thanhType: "Địa",
          desc: "Thiên tam sinh Mộc, Địa bát thành chi" },
        { sinh: 4, thanh: 9,  element: "Kim",  dir: "Tây",    sinhType: "Địa",   thanhType: "Thiên",
          desc: "Địa tứ sinh Kim, Thiên cửu thành chi" },
        { sinh: 5, thanh: 10, element: "Thổ",  dir: "Trung",  sinhType: "Thiên", thanhType: "Địa",
          desc: "Thiên ngũ sinh Thổ, Địa thập thành chi" },
    ],

    /** Map any number 1–10 to its Ngũ Hành element */
    numberToElement(n) {
        const elements = ["Thủy", "Hỏa", "Mộc", "Kim", "Thổ"];
        return elements[((n - 1) % 5)];
    },

    /** Is this a Sinh number (1–5) or Thành number (6–10)? */
    isSinh(n)  { return n >= 1 && n <= 5; },
    isThanh(n) { return n >= 6 && n <= 10; },

    /** Get the partner: sinh ↔ thành (add or subtract 5) */
    partner(n) { return n <= 5 ? n + 5 : n - 5; },

    /** Thiên (odd) or Địa (even) */
    thienDia(n) { return n % 2 === 1 ? "Thiên" : "Địa"; },

    /** Compass layout: direction → element + number pair */
    directions: {
        "Bắc":   { element: "Thủy", numbers: [1, 6] },
        "Nam":   { element: "Hỏa",  numbers: [2, 7] },
        "Đông":  { element: "Mộc",  numbers: [3, 8] },
        "Tây":   { element: "Kim",  numbers: [4, 9] },
        "Trung": { element: "Thổ",  numbers: [5, 10] }
    },

    /** Sum of all Hà Đồ numbers: 1+2+…+10 = 55 (Thiên=25, Địa=30) */
    totalSum: 55,
    thienSum: 25,  // 1+3+5+7+9
    diaSum: 30,    // 2+4+6+8+10
};

/* ═══════════════ 2. Ngũ Hành (5 Elements) ═══════════════ */

/**
 * Đại Việt: Kim = Trắng (White), Thổ = Vàng (Yellow)
 * Trung Quốc: Kim = Vàng/Gold, Thổ = Nâu (Brown)
 * Mộc = Xanh lá, Thủy = Xanh dương, Hỏa = Đỏ — giống cả 2
 */
const NGU_HANH_COLORS_DV = {
    "Kim":  { bg: "#E0E0E0", fg: "#333" },   // Trắng (White/Silver)
    "Mộc":  { bg: "#2E7D32", fg: "#fff" },   // Xanh lá (Green)
    "Thủy": { bg: "#1565C0", fg: "#fff" },   // Xanh dương (Blue)
    "Hỏa":  { bg: "#D32F2F", fg: "#fff" },   // Đỏ (Red)
    "Thổ":  { bg: "#FFB300", fg: "#333" }    // Vàng (Yellow)
};
const NGU_HANH_COLORS_TQ = {
    "Kim":  { bg: "#FFD700", fg: "#333" },   // Vàng/Gold
    "Mộc":  { bg: "#2E7D32", fg: "#fff" },   // Xanh lá (Green)
    "Thủy": { bg: "#1565C0", fg: "#fff" },   // Xanh dương (Blue)
    "Hỏa":  { bg: "#D32F2F", fg: "#fff" },   // Đỏ (Red)
    "Thổ":  { bg: "#8D6E63", fg: "#fff" }    // Nâu (Brown)
};

const NGU_HANH = {
    elements: ["Kim", "Mộc", "Thủy", "Hỏa", "Thổ"],
    /** Dynamic colors — switches with LacThuMode */
    get colors() {
        return LacThuMode.isDV() ? NGU_HANH_COLORS_DV : NGU_HANH_COLORS_TQ;
    },
    /** Sinh cycle: Kim→Thủy→Mộc→Hỏa→Thổ→Kim */
    sinh: { "Kim": "Thủy", "Thủy": "Mộc", "Mộc": "Hỏa", "Hỏa": "Thổ", "Thổ": "Kim" },
    /** Khắc cycle: Kim→Mộc→Thổ→Thủy→Hỏa→Kim */
    khac: { "Kim": "Mộc", "Mộc": "Thổ", "Thổ": "Thủy", "Thủy": "Hỏa", "Hỏa": "Kim" }
};

/* ═══════════════ 3. Cyclic Groups ═══════════════ */

const CYCLIC_GROUPS = {
    /** Z₉: Phi Cung (Flying Palace) */
    Z9: {
        order: 9,
        name: "ℤ₉ — Phi Cung (飛宮)",
        desc: "Cửu Cung xoay vòng: 1→2→3→…→9→1. Phép cộng modulo 9.",
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        palaceNames: ["Khảm", "Khôn", "Chấn", "Tốn", "Trung", "Càn", "Đoài", "Cấn", "Ly"],
        /** phi_thuong: ((start-1 ± steps) mod 9) + 1 */
        phi(start, steps, forward = true) {
            if (forward) return ((start - 1 + steps) % 9 + 9) % 9 + 1;
            else return ((start - 1 - steps) % 9 + 9) % 9 + 1;
        }
    },

    /** Z₈: Hậu Thiên Bát Quái ring (skip palace 5) */
    Z8: {
        order: 8,
        name: "ℤ₈ — Bát Quái Ring",
        desc: "8 cung ngoài theo thứ tự Hậu Thiên: 1→8→3→4→9→2→7→6. Bỏ qua Trung Cung (5).",
        ring: [1, 8, 3, 4, 9, 2, 7, 6],
        labels: ["Khảm", "Cấn", "Chấn", "Tốn", "Ly", "Khôn", "Đoài", "Càn"],
        move(start, steps) {
            const idx = this.ring.indexOf(start);
            if (idx < 0) return start;
            return this.ring[((idx + steps) % 8 + 8) % 8];
        }
    },

    /** Z₁₂: Địa Chi (Earthly Branches) */
    Z12: {
        order: 12,
        name: "ℤ₁₂ — Địa Chi (地支)",
        desc: "12 chi: Tý→Sửu→Dần→Mão→Thìn→Tỵ→Ngọ→Mùi→Thân→Dậu→Tuất→Hợi.",
        labels: ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
                 "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"],
        elements: ["Thủy", "Thổ", "Mộc", "Mộc", "Thổ", "Hỏa",
                   "Hỏa", "Thổ", "Kim", "Kim", "Thổ", "Thủy"]
    },

    /** Z₁₆+2: Văn Xương ring (16 Thần + 2 dwell nodes) */
    Z16: {
        order: 16,
        effectiveOrder: 18,
        name: "ℤ₁₆ (trọng số) — Văn Xương Ring",
        desc: "16 Thần: 12 Địa Chi + 4 Quái (Càn, Khôn, Cấn, Tốn). Lưu 2 toán tại Càn & Khôn → chu kỳ hiệu dụng = 18.",
        ring: ["Thân", "Dậu", "Tuất", "Càn", "Hợi", "Tý", "Sửu", "Cấn",
               "Dần", "Mão", "Thìn", "Tốn", "Tỵ", "Ngọ", "Mùi", "Khôn"],
        dwellNodes: ["Càn", "Khôn"],
        weights: [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    },

    /** Z₆₀: Sexagenary cycle (Can Chi) */
    Z60: {
        order: 60,
        name: "ℤ₆₀ ≅ ℤ₁₀ × ℤ₁₂ — Lục Thập Hoa Giáp",
        desc: "60 Can Chi = LCM(10 Thiên Can, 12 Địa Chi). Isomorphic to ℤ₁₀ × ℤ₁₂ vì gcd(10,12)=2 nhưng dùng mapping (2k, 2k) → đồng bộ.",
        thienCan: ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"],
        diaChi: ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"],
        /** Convert index 0–59 to (Can, Chi) pair */
        fromIndex(i) {
            return { can: this.thienCan[i % 10], chi: this.diaChi[i % 12] };
        },
        /** JD → Can Chi index */
        fromJD(jd) {
            return ((Math.floor(jd) + 49) % 60 + 60) % 60;
        }
    }
};

/* ═══════════════ 4. Surjective Mappings ═══════════════ */

const SURJECTIONS = {
    /** 12 Địa Chi → 9 Cung */
    chi_to_9: {
        name: "12 → 9: Địa Chi → Cửu Cung",
        desc: "Ánh xạ toàn ánh (surjective) nhưng không đơn ánh. 4 cặp chia sẻ cung. Trung Cung (5) không có nghịch ảnh.",
        map: [1, 8, 3, 3, 4, 9, 9, 2, 7, 7, 6, 1],
        // index = Địa Chi index (0=Tý, ..., 11=Hợi)
        labels: CYCLIC_GROUPS.Z12.labels,
        /** Pairs that share the same palace */
        sharedPairs: [
            { chi: ["Dần", "Mão"],   palace: 3 },
            { chi: ["Tỵ", "Ngọ"],   palace: 9 },
            { chi: ["Thân", "Dậu"], palace: 7 },
            { chi: ["Tý", "Hợi"],   palace: 1 }
        ],
        noPreimage: 5 // Trung Cung — structural singularity
    },

    /** 16 Thần → 9 Cung (skip 5) */
    ring16_to_9: {
        name: "16 → 8: 16 Thần → 8 Cung Ngoài",
        desc: "Ánh xạ 16 vị trí Thần → 8 cung ngoài (bỏ Trung Cung). Chỉ Ngũ Phúc mới đến được cung 5.",
        map: [7, 7, 6, 6, 1, 1, 8, 8, 3, 3, 4, 4, 9, 9, 2, 2]
    }
};

/* ═══════════════ 5. Nested Modular Chain (Thái Ất) ═══════════════ */

const MODULAR_CHAIN = {
    epoch: 10153917,
    name: "Chuỗi Module Lồng — Tích Niên",
    desc: "Thời gian phân cấp: 10 Kỷ (3600) → 1 Kỷ (360) → 1 Nguyên (72) → 1 Hội (6)",
    levels: [
        { mod: 3600, name: "10 Kỷ", desc: "10 × 360 năm", sub: "10 Kỷ" },
        { mod: 360,  name: "1 Kỷ",  desc: "5 × 72 năm = 5 Nguyên", sub: "5 Nguyên" },
        { mod: 72,   name: "1 Nguyên", desc: "12 × 6 năm = 12 Hội", sub: "12 Hội" }
    ],
    /** Run the nested reduction */
    reduce(year) {
        const tichNien = year + this.epoch;
        const steps = [];
        let val = tichNien;
        for (const level of this.levels) {
            const prev = val;
            val = val % level.mod;
            steps.push({ level: level.name, mod: level.mod, input: prev, output: val });
        }
        return { tichNien, steps, kyDu: val };
    }
};

/* ═══════════════ 6. Multi-Rate System (Tam Cơ) ═══════════════ */

const TAM_CO = {
    name: "Tam Cơ (三基) — Hệ Đa Tốc Độ",
    desc: "Ba đồng hồ trên cùng vòng ℤ₁₂ nhưng tốc độ khác nhau. Tỷ số 30:3:1.",
    clocks: [
        {
            name: "Quân Cơ (君基)",
            role: "Vua — Xu thế lớn",
            start: "Ngọ",
            startIdx: 6,
            period: 30,
            totalCycle: 360,
            color: "#FFD700",
            desc: "30 năm/cung. Chu kỳ 360 năm. Chuyển động chậm nhất."
        },
        {
            name: "Thần Cơ (臣基)",
            role: "Bề tôi — Chính sách",
            start: "Ngọ",
            startIdx: 6,
            period: 3,
            totalCycle: 36,
            color: "#42A5F5",
            desc: "3 năm/cung. Chu kỳ 36 năm. Trung bình."
        },
        {
            name: "Dân Cơ (民基)",
            role: "Dân — Đời sống",
            start: "Tuất",
            startIdx: 10,
            period: 1,
            totalCycle: 12,
            color: "#66BB6A",
            desc: "1 năm/cung. Chu kỳ 12 năm. Nhanh nhất."
        }
    ],
    /** Calculate positions for a given Tích Tuế */
    calculate(tichTue) {
        return this.clocks.map(c => {
            const steps = Math.floor(tichTue / c.period) % 12;
            const pos = (c.startIdx + steps) % 12;
            return { ...c, steps, currentIdx: pos, currentChi: CYCLIC_GROUPS.Z12.labels[pos] };
        });
    }
};

/* ═══════════════ 7. Special Paths (Thái Ất) ═══════════════ */

const SPECIAL_PATHS = [
    {
        name: "Ngũ Phúc (五福)",
        path: [1, 8, 4, 2, 5],
        pathNames: ["Khảm", "Cấn", "Tốn", "Khôn", "Trung"],
        period: 45,
        totalCycle: 225,
        offset: 115,
        color: "#AB47BC",
        desc: "Chu kỳ duy nhất đến được Trung Cung (5). 5 cung × 45 năm = 225 năm.",
        note: "ℤ₅ tuần hoàn trên tập {1,8,4,2,5}"
    },
    {
        name: "Đại Du (大遊)",
        path: [7, 8, 9, 1, 2, 3, 4, 6],
        pathNames: ["Đoài", "Cấn", "Ly", "Khảm", "Khôn", "Chấn", "Tốn", "Càn"],
        period: 36,
        totalCycle: 288,
        offset: 34,
        color: "#FF7043",
        desc: "8 cung ngoài theo thứ tự tuần tự (bỏ 5). 8 × 36 năm = 288 năm.",
        note: "ℤ₈ tuần hoàn trên tập {7,8,9,1,2,3,4,6}"
    }
];

/* ═══════════════ 8. Kỳ Môn 3-Layer System ═══════════════ */

const KI_MON_LAYERS = {
    name: "Kỳ Môn Tam Bàn (三盤)",
    desc: "3 lớp xoay độc lập trên Cửu Cung → Tích Trực (Direct Product) của nhóm hoán vị.",
    layers: [
        {
            name: "Thiên Bàn (天盤)",
            components: ["Cửu Tinh"],
            labels: ["Bồng", "Nhuế", "Xung", "Phụ", "Cầm", "Tâm", "Trụ", "Nhậm", "Anh"],
            fullLabels: ["Thiên Bồng", "Thiên Nhuế", "Thiên Xung", "Thiên Phụ", "Thiên Cầm",
                         "Thiên Tâm", "Thiên Trụ", "Thiên Nhậm", "Thiên Anh"],
            color: "#42A5F5",
            rotation: "Phi Cung ℤ₉: theo Cục số, Dương thuận / Âm nghịch"
        },
        {
            name: "Nhân Bàn (人盤)",
            components: ["Bát Môn"],
            labels: ["Hưu", "Sinh", "Thương", "Đỗ", "Cảnh", "Tử", "Kinh", "Khai"],
            color: "#66BB6A",
            rotation: "Phi Cung ℤ₉: Trực Phù → Trực Sử → phân phối 8 cửa"
        },
        {
            name: "Địa Bàn (地盤)",
            components: ["Bát Quái", "Cửu Cung"],
            labels: ["Khảm", "Khôn", "Chấn", "Tốn", "Trung", "Càn", "Đoài", "Cấn", "Ly"],
            color: "#FF7043",
            rotation: "Cố định — Lạc Thư vĩnh cửu"
        }
    ],
    spirits: {
        name: "Bát Thần (八神)",
        labels: ["Trực Phù", "Đằng Xà", "Thái Âm", "Lục Hợp", "Câu Trần", "Chu Tước", "Cửu Địa", "Cửu Thiên"],
        color: "#AB47BC",
        rotation: "Phi Cung ℤ₉: theo vị trí Trực Phù"
    },
    tamKy: {
        name: "Tam Kỳ (三奇)",
        labels: ["Ất (日奇·Nhật)", "Bính (月奇·Nguyệt)", "Đinh (星奇·Tinh)"],
        desc: "3 Kỳ ẩn trong 6 Nghi (Mậu→Quý) → tổng 9 yếu tố Thiên Can trên Cửu Cung"
    }
};

/* ═══════════════ 9. Cục Determination (Kỳ Môn) ═══════════════ */

const KI_MON_CUC = {
    /** 24 Tiết Khí boundaries at 15° intervals of solar longitude */
    tietKhi: [
        "Tiểu Hàn", "Đại Hàn", "Lập Xuân", "Vũ Thủy", "Kinh Trập", "Xuân Phân",
        "Thanh Minh", "Cốc Vũ", "Lập Hạ", "Tiểu Mãn", "Mang Chủng", "Hạ Chí",
        "Tiểu Thử", "Đại Thử", "Lập Thu", "Xử Thử", "Bạch Lộ", "Thu Phân",
        "Hàn Lộ", "Sương Giáng", "Lập Đông", "Tiểu Tuyết", "Đại Tuyết", "Đông Chí"
    ],

    /** Dương Độn table: [Tiết Khí index] → [Thượng, Trung, Hạ] */
    duongDon: {
        23: [1, 7, 4], 0: [2, 8, 5], 1: [3, 9, 6],
        2: [8, 5, 2], 3: [9, 6, 3], 4: [1, 7, 4],
        5: [3, 9, 6], 6: [4, 1, 7], 7: [5, 2, 8],
        8: [4, 1, 7], 9: [5, 2, 8], 10: [6, 3, 9]
    },

    /** Âm Độn table */
    amDon: {
        11: [9, 3, 6], 12: [8, 2, 5], 13: [7, 1, 4],
        14: [2, 5, 8], 15: [1, 4, 7], 16: [9, 3, 6],
        17: [7, 1, 4], 18: [6, 9, 3], 19: [5, 8, 2],
        20: [6, 9, 3], 21: [5, 8, 2], 22: [4, 7, 1]
    },

    /** Day partition: can_chi_day mod 15 → Nguyên */
    dayToNguyen(canChiDay) {
        const d = canChiDay % 15;
        if (d < 5) return { nguyen: "Thượng", index: 0 };
        if (d < 10) return { nguyen: "Trung", index: 1 };
        return { nguyen: "Hạ", index: 2 };
    }
};

/* ═══════════════ 10. Key Constants ═══════════════ */

const MATH_CONSTANTS = [
    { value: "10,153,917", name: "THAI_AT_EPOCH", meaning: "Thượng Cổ Giáp Tý — gốc niên đại" },
    { value: "3,600",      name: "10 Kỷ",        meaning: "10 × 360 = siêu chu kỳ" },
    { value: "360",        name: "1 Kỷ",          meaning: "5 × 72 = 5 Nguyên" },
    { value: "72",         name: "1 Nguyên",       meaning: "12 × 6 = 12 Hội" },
    { value: "60",         name: "Lục Thập",       meaning: "LCM(10 Can, 12 Chi)" },
    { value: "225",        name: "Ngũ Phúc",       meaning: "5 × 45 = 5 cung × 45 năm" },
    { value: "288",        name: "Đại Du",         meaning: "8 × 36 = 8 cung × 36 năm" },
    { value: "18",         name: "Văn Xương eff.", meaning: "16 Thần + 2 lưu = hiệu dụng" },
    { value: "15",         name: "Magic Constant", meaning: "Hằng số Lạc Thư (mỗi dòng=15)" },
    { value: "55",         name: "Hà Đồ tổng",    meaning: "1+2+…+10 = 55 (Thiên 25, Địa 30)" },
    { value: "15°",        name: "Tiết Khí khoảng", meaning: "360° ÷ 24 = 15° kinh độ Mặt Trời" },
];
