/**
 * data.js - Hexagram Data & Names
 * Dữ liệu 64 quẻ theo Fuxi Sequence
 */

const HexViz = window.HexViz || {};

// Full names of 64 hexagrams (Fuxi order)
const fullNames = [
    "Khôn (Thuần Khôn)", "Bác (Sơn Địa Bác)", "Tỷ (Thủy Địa Tỷ)", "Quan (Phong Địa Quan)",
    "Dự (Lôi Địa Dự)", "Tấn (Hỏa Địa Tấn)", "Tụy (Trạch Địa Tụy)", "Bĩ (Thiên Địa Bĩ)",
    "Khiêm (Địa Sơn Khiêm)", "Cấn (Thuần Cấn)", "Kiển (Thủy Sơn Kiển)", "Tiệm (Phong Sơn Tiệm)",
    "Tiểu Quá (Lôi Sơn Tiểu Quá)", "Lữ (Hỏa Sơn Lữ)", "Hàm (Trạch Sơn Hàm)", "Độn (Thiên Sơn Độn)",
    "Sư (Địa Thủy Sư)", "Mông (Sơn Thủy Mông)", "Khảm (Thuần Khảm)", "Hoán (Phong Thủy Hoán)",
    "Giải (Lôi Thủy Giải)", "Vị Tế (Hỏa Thủy Vị Tế)", "Khốn (Trạch Thủy Khốn)", "Tụng (Thiên Thủy Tụng)",
    "Thăng (Địa Phong Thăng)", "Cổ (Sơn Phong Cổ)", "Tỉnh (Thủy Phong Tỉnh)", "Tốn (Thuần Tốn)",
    "Hằng (Lôi Phong Hằng)", "Đỉnh (Hỏa Phong Đỉnh)", "Đại Quá (Trạch Phong Đại Quá)", "Cấu (Thiên Phong Cấu)",
    "Phục (Địa Lôi Phục)", "Di (Sơn Lôi Di)", "Truân (Thủy Lôi Truân)", "Ích (Phong Lôi Ích)",
    "Chấn (Thuần Chấn)", "Phệ Hạp (Hỏa Lôi Phệ Hạp)", "Tùy (Trạch Lôi Tùy)", "Vô Vọng (Thiên Lôi Vô Vọng)",
    "Minh Di (Địa Hỏa Minh Di)", "Bí (Sơn Hỏa Bí)", "Ký Tế (Thủy Hỏa Ký Tế)", "Gia Nhân (Phong Hỏa Gia Nhân)",
    "Phong (Lôi Hỏa Phong)", "Ly (Thuần Ly)", "Cách (Trạch Hỏa Cách)", "Đồng Nhân (Thiên Hỏa Đồng Nhân)",
    "Lâm (Địa Trạch Lâm)", "Tổn (Sơn Trạch Tổn)", "Tiết (Thủy Trạch Tiết)", "Trung Phu (Phong Trạch Trung Phu)",
    "Quy Muội (Lôi Trạch Quy Muội)", "Khuê (Hỏa Trạch Khuê)", "Đoài (Thuần Đoài)", "Lý (Thiên Trạch Lý)",
    "Thái (Địa Thiên Thái)", "Đại Súc (Sơn Thiên Đại Súc)", "Nhu (Thủy Thiên Nhu)", "Tiểu Súc (Phong Thiên Tiểu Súc)",
    "Đại Tráng (Lôi Thiên Đại Tráng)", "Đại Hữu (Hỏa Thiên Đại Hữu)", "Quải (Trạch Thiên Quải)", "Càn (Thuần Càn)"
];

// Initialize hexagram data array
HexViz.hexagramsData = [];

for (let i = 0; i < 64; i++) {
    HexViz.hexagramsData.push({
        id: i,
        name: fullNames[i] || `Quẻ số ${i}`,
        binary: i,
        image_text: "Đang cập nhật...",
        meaning: "Đang cập nhật...",
        judgment: "Đang cập nhật...",
        advice: "Đang cập nhật..."
    });
}

// Sample data overrides
HexViz.hexagramsData[56].image_text = "Hỷ Báo Tam Nguyên";
HexViz.hexagramsData[56].meaning = "Hanh thông, thời vận tốt, trời đất giao hòa.";
HexViz.hexagramsData[56].judgment = "Tiểu vãng đại lai, cát hanh.";
HexViz.hexagramsData[56].advice = "Giữ đạo trung, phòng khi suy vi. Dùng quân tử, xa tiểu nhân.";

HexViz.hexagramsData[63].image_text = "Khốn Long Đắc Thủy";
HexViz.hexagramsData[63].meaning = "Cương kiện, mạnh mẽ, đầu đàn.";
HexViz.hexagramsData[63].judgment = "Nguyên, hanh, lợi, trinh.";
HexViz.hexagramsData[63].advice = "Phấn đấu không ngừng, nhưng cần biết thời thế.";

HexViz.hexagramsData[0].image_text = "Ngạ Hổ Đắc Thực";
HexViz.hexagramsData[0].meaning = "Nhu thuận, cưu mang vạn vật.";
HexViz.hexagramsData[0].judgment = "Nguyên, hanh, lợi tẫn mã chi trinh.";
HexViz.hexagramsData[0].advice = "Làm việc cần có người dẫn dắt, thuận theo thời thế.";

// Bát Quái data
HexViz.baguaNames = ["Khôn", "Cấn", "Khảm", "Tốn", "Chấn", "Ly", "Đoài", "Càn"];
HexViz.baguaColors = ["#3e2723", "#5d4037", "#1a237e", "#1b5e20", "#f57f17", "#b71c1c", "#00acc1", "#eeeeee"];

// Tứ Tượng data
HexViz.tuTuongNames = ["Thái Âm", "Thiếu Dương", "Thiếu Âm", "Thái Dương"];
HexViz.tuTuongColors = ["#212121", "#616161", "#9e9e9e", "#f5f5f5"];

// Lưỡng Nghi data
HexViz.luongNghiNames = ["Âm", "Dương"];
HexViz.luongNghiColors = ["#000", "#fff"];

window.HexViz = HexViz;
