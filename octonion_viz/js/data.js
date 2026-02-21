/**
 * Octonion–Bát Quái Data Model
 * ==============================
 * Maps the 8 Octonion basis units (e₀…e₇) to the 8 Trigrams (Bát Quái)
 * using the Leibniz binary encoding (LSB bottom-up).
 *
 * Fano plane triples define the multiplication rules for imaginary units.
 */

const TRIGRAMS = [
    { id: 0, name: "Khôn",  han: "坤", symbol: "☷", element: "Thổ",  nature: "Đất",   binary: "000", color: "#8B6914", octonion: "e₀ (1)",  desc: "Tiếp nhận, nhu thuận" },
    { id: 1, name: "Chấn",  han: "震", symbol: "☳", element: "Mộc",  nature: "Sấm",   binary: "001", color: "#2E7D32", octonion: "e₁ (i)",  desc: "Kích động, chấn động" },
    { id: 2, name: "Khảm",  han: "坎", symbol: "☵", element: "Thủy", nature: "Nước",  binary: "010", color: "#1565C0", octonion: "e₂ (j)",  desc: "Hiểm trở, lưu chuyển" },
    { id: 3, name: "Đoài",  han: "兌", symbol: "☱", element: "Kim",  nature: "Hồ",    binary: "011", color: "#78909C", octonion: "e₃ (k)",  desc: "Vui vẻ, trao đổi" },
    { id: 4, name: "Cấn",   han: "艮", symbol: "☶", element: "Thổ",  nature: "Núi",   binary: "100", color: "#795548", octonion: "e₄ (l)",  desc: "Ngưng nghỉ, ổn định" },
    { id: 5, name: "Ly",    han: "離", symbol: "☲", element: "Hỏa",  nature: "Lửa",   binary: "101", color: "#D32F2F", octonion: "e₅ (il)", desc: "Sáng tỏ, phân tách" },
    { id: 6, name: "Tốn",   han: "巽", symbol: "☴", element: "Mộc",  nature: "Gió",   binary: "110", color: "#43A047", octonion: "e₆ (jl)", desc: "Thâm nhập, nhu thuận" },
    { id: 7, name: "Càn",   han: "乾", symbol: "☰", element: "Kim",  nature: "Trời",  binary: "111", color: "#F9A825", octonion: "e₇ (kl)", desc: "Sáng tạo, cương kiện" }
];

/* Ngũ Hành Colors for element badges */
const NGU_HANH_COLORS = {
    "Kim":  { bg: "#FFD700", fg: "#333" },
    "Mộc":  { bg: "#2E7D32", fg: "#fff" },
    "Thủy": { bg: "#1565C0", fg: "#fff" },
    "Hỏa":  { bg: "#D32F2F", fg: "#fff" },
    "Thổ":  { bg: "#8D6E63", fg: "#fff" }
};

/**
 * Fano Plane — 7 oriented triples (a,b,c) defining:
 *   eₐ × eᵦ = +eᵧ  (cyclic)
 *   eᵦ × eₐ = -eᵧ  (anti-cyclic → non-commutative!)
 *
 * The triples also encode XOR: a ⊕ b = c
 *
 * Each triple carries a Dịch interpretation:
 *   forward (Sinh) = generating/nurturing
 *   reverse (Khắc) = overcoming/restraining
 */
const FANO_TRIPLES = [
    { a: 1, b: 2, c: 3, meaning: "Chấn × Khảm = Đoài",    interp: "Sấm kích nước → Hồ vui" },
    { a: 1, b: 4, c: 5, meaning: "Chấn × Cấn = Ly",        interp: "Sấm chấn núi → Lửa bùng" },
    { a: 2, b: 4, c: 6, meaning: "Khảm × Cấn = Tốn",       interp: "Nước gặp núi → Gió thổi" },
    { a: 3, b: 4, c: 7, meaning: "Đoài × Cấn = Càn",        interp: "Hồ − Núi hợp → Trời sáng" },
    { a: 1, b: 6, c: 7, meaning: "Chấn × Tốn = Càn",        interp: "Sấm hợp gió → Trời vận" },
    { a: 2, b: 5, c: 7, meaning: "Khảm × Ly = Càn",         interp: "Nước − Lửa hợp → Trời thành" },
    { a: 3, b: 5, c: 6, meaning: "Đoài × Ly = Tốn",         interp: "Hồ − Lửa → Gió biến" }
];

/**
 * Full 8×8 Multiplication Table
 * mult[i][j] = { sign: +1/-1, index: 0..7 }
 * Meaning: eᵢ × eⱼ = sign * e_index
 */
const MULT_TABLE = buildMultTable();

function buildMultTable() {
    const T = Array.from({ length: 8 }, () => Array(8).fill(null));

    // e₀ is identity
    for (let i = 0; i < 8; i++) {
        T[0][i] = { sign: 1, index: i };
        T[i][0] = { sign: 1, index: i };
    }

    // eᵢ × eᵢ = -e₀ for i ≥ 1
    for (let i = 1; i < 8; i++) {
        T[i][i] = { sign: -1, index: 0 };
    }

    // Fano triples define the rest
    FANO_TRIPLES.forEach(({ a, b, c }) => {
        // Forward cycle: a→b→c→a
        T[a][b] = { sign: 1, index: c };
        T[b][c] = { sign: 1, index: a };
        T[c][a] = { sign: 1, index: b };
        // Reverse (anti-cyclic)
        T[b][a] = { sign: -1, index: c };
        T[c][b] = { sign: -1, index: a };
        T[a][c] = { sign: -1, index: b };
    });

    return T;
}

/**
 * Format a multiplication result as a string
 */
function formatMult(i, j) {
    const r = MULT_TABLE[i][j];
    if (!r) return "?";
    const signStr = r.sign < 0 ? "−" : "";
    return `${signStr}${TRIGRAMS[r.index].symbol}`;
}

function formatMultFull(i, j) {
    const r = MULT_TABLE[i][j];
    if (!r) return "?";
    const signStr = r.sign < 0 ? "−" : "+";
    return `${signStr}${TRIGRAMS[r.index].name}`;
}

/**
 * Cayley-Dickson Construction stages
 */
const CAYLEY_DICKSON = [
    {
        level: 0,
        algebra: "R",
        name: "Số Thực",
        dich: "Thái Cực (太極)",
        dim: 1,
        props: ["Giao hoán", "Kết hợp", "Có thứ tự"],
        desc: "Trạng thái nguyên thủy, chưa phân định. Một chiều, toàn thể.",
        color: "#9E9E9E"
    },
    {
        level: 1,
        algebra: "C",
        name: "Số Phức",
        dich: "Lưỡng Nghi (兩儀)",
        dim: 2,
        props: ["Giao hoán", "Kết hợp", "Mất thứ tự"],
        desc: "Âm-Dương phân tách. 2 chiều: phần thực (Dương) và phần ảo (Âm).",
        color: "#42A5F5"
    },
    {
        level: 2,
        algebra: "H",
        name: "Quaternion",
        dich: "Tứ Tượng (四象)",
        dim: 4,
        props: ["Mất giao hoán", "Kết hợp"],
        desc: "Bốn trạng thái: Thái Dương, Thiếu Âm, Thiếu Dương, Thái Âm. Phép nhân mất tính giao hoán = trật tự có ý nghĩa.",
        color: "#AB47BC"
    },
    {
        level: 3,
        algebra: "O",
        name: "Octonion",
        dich: "Bát Quái (八卦)",
        dim: 8,
        props: ["Mất giao hoán", "Mất kết hợp", "Đại số chia thay thế"],
        desc: "8 đơn vị cơ sở = 8 quẻ đơn. Đại số phong phú nhất còn bảo toàn chuẩn (Định lý Hurwitz). Mất kết hợp = tương tác ba yếu tố (Tam Tài).",
        color: "#EF5350"
    }
];

/**
 * Non-commutativity examples (Sinh vs Khắc)
 */
const NONCOMMUTATIVE_EXAMPLES = [
    {
        a: 1, b: 2,
        forward: "Chấn × Khảm = +Đoài (Sấm kích nước → Hồ vui = SINH)",
        reverse: "Khảm × Chấn = −Đoài (Nước nuốt sấm → Hồ buồn = KHẮC)"
    },
    {
        a: 2, b: 5,
        forward: "Khảm × Ly = +Càn (Nước − Lửa giao hòa → Trời sáng = SINH)",
        reverse: "Ly × Khảm = −Càn (Lửa chống nước → Trời tối = KHẮC)"
    },
    {
        a: 1, b: 4,
        forward: "Chấn × Cấn = +Ly (Sấm chấn núi → Lửa bùng = SINH)",
        reverse: "Cấn × Chấn = −Ly (Núi chịu sấm → Lửa tắt = KHẮC)"
    }
];

/**
 * Non-associativity examples (Tam Tài)
 */
const NONASSOCIATIVE_EXAMPLES = [
    {
        a: 1, b: 2, c: 4,
        label: "Chấn, Khảm, Cấn",
        left: "(e₁e₂)e₄ = e₃e₄ = +e₇ → (Chấn·Khảm)·Cấn = +Càn",
        right: "e₁(e₂e₄) = e₁e₆ = +e₇ → Chấn·(Khảm·Cấn) = +Càn",
        result: "Kết hợp! (Trường hợp đặc biệt)"
    },
    {
        a: 1, b: 2, c: 5,
        label: "Chấn, Khảm, Ly",
        left: "(e₁e₂)e₅ = e₃e₅ = +e₆ → (Chấn·Khảm)·Ly = +Tốn",
        right: "e₁(e₂e₅) = e₁e₇ = −e₆ → Chấn·(Khảm·Ly) = −Tốn",
        result: "Mất kết hợp! +Tốn ≠ −Tốn (Tam Tài: thứ tự nhóm 3 yếu tố thay đổi kết quả)"
    },
    {
        a: 3, b: 5, c: 1,
        label: "Đoài, Ly, Chấn",
        left: "(e₃e₅)e₁ = e₆e₁ = −e₇ → (Đoài·Ly)·Chấn = −Càn",
        right: "e₃(e₅e₁) = e₃e₄ = +e₇ → Đoài·(Ly·Chấn) = +Càn",
        result: "Mất kết hợp! −Càn ≠ +Càn"
    }
];
