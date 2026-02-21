/**
 * config.js - Visualization Configuration
 * Các hằng số kích thước, bán kính cho Viên Đồ 64 Quẻ
 */

const HexViz = window.HexViz || {};

// Viewport dimensions
HexViz.width = window.innerWidth * 0.95;
HexViz.height = window.innerHeight * 0.95;
HexViz.maxRadius = Math.min(HexViz.width, HexViz.height) / 2;

// Layer Radii Configuration
// Center -> 2 (Lưỡng Nghi) -> 4 (Tứ Tượng) -> 8 (Bát Quái) -> 64 (Quẻ)
HexViz.r2 = HexViz.maxRadius * 0.25;
HexViz.r4 = HexViz.maxRadius * 0.45;
HexViz.r8 = HexViz.maxRadius * 0.65;
HexViz.r64_center = HexViz.maxRadius * 0.88;

// Calculate max hexagram circle radius based on circumference
const circum = 2 * Math.PI * HexViz.r64_center;
HexViz.maxHexR = (circum / 64) / 2 * 0.95; // 95% fill (tight packing)

// State
HexViz.activeFilterSector = null;
HexViz.trigramHetuMap = {};

window.HexViz = HexViz;
