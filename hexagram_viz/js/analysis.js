/**
 * analysis.js - Algorithmic Analysis Engine
 * Phân tích quẻ dịch bằng thuật toán
 */

const HexViz = window.HexViz || {};

/**
 * Phân tích quẻ dựa trên giá trị nhị phân
 * @param {number} val - Giá trị thập phân (0-63)
 * @returns {string} Kết quả phân tích
 */
HexViz.analyzeHexagramAlgo = function (val) {
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
};

window.HexViz = HexViz;
