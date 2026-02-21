"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    BẢNG CỤC CHUẨN NAM PHÁI                                   ║
║                    Đã sửa theo tuvinamhai.vn                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Khẩu quyết: "Giáp Kỷ chi niên Bính tác thủ"                                ║
║  - Năm Giáp/Kỷ: Khởi Bính từ Dần, thuận hành theo Cung Mệnh                ║
║  - Năm Ất/Canh: Khởi Mậu từ Dần                                             ║
║  - Năm Bính/Tân: Khởi Canh từ Dần                                           ║
║  - Năm Đinh/Nhâm: Khởi Nhâm từ Dần                                          ║
║  - Năm Mậu/Quý: Khởi Giáp từ Dần                                            ║
╚══════════════════════════════════════════════════════════════════════════════╝

FIX DATE: 15/12/2025 → FIXED AGAIN: 2025
ISSUE: Bảng Cục sai dẫn đến Tử Vi sai vị trí (50/60 entries were WRONG!)
FIX: Tính Cục từ Nạp Âm theo thuật toán Ngũ Hổ Độn:
  1. Từ Can năm → tìm Can tháng Dần (Bính/Mậu/Canh/Nhâm/Giáp)
  2. Đếm thuận từ Dần đến Chi cung Mệnh → xác định Can cung Mệnh
  3. Nạp Âm (Can Mệnh, Chi Mệnh) → Ngũ Hành → Cục
VERIFIED: Thuật toán _determine_cuc_algorithmic() cho kết quả trùng khớp
"""

# 12 Cung (Palaces) - Fixed order starting from Mệnh
CUNG_ORDER = ['Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 'Quan Lộc', 'Nô Bộc', 
              'Thiên Di', 'Tật Ách', 'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ']

# Ngũ Hành Cục với số cục
CUC_TYPE = {
    'Thủy Nhị Cục': 2,
    'Mộc Tam Cục': 3,
    'Kim Tứ Cục': 4,
    'Thổ Ngũ Cục': 5,
    'Hỏa Lục Cục': 6
}

# ═══════════════════════════════════════════════════════════════════════════════
# BẢNG TRA CỤC CHUẨN NAM PHÁI
# 
# Bảng tra theo Thiên Can năm sinh (hàng) và Địa Chi Cung Mệnh (cột)
# 
# | Can năm    | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |
# |------------|:--:|:---:|:---:|:---:|:----:|:--:|:---:|:---:|:----:|:---:|:----:|:---:|
# | Giáp/Kỷ   |  2 |  6  |  3  |  3  |   4  |  4 |  5  |  5  |   6  |  6  |   2  |  2  |
# | Ất/Canh   |  6 |  2  |  4  |  4  |   5  |  5 |  6  |  6  |   2  |  2  |   3  |  3  |
# | Bính/Tân  |  2 |  3  |  5  |  5  |   6  |  6 |  2  |  2  |   3  |  3  |   4  |  4  |
# | Đinh/Nhâm |  3 |  4  |  6  |  6  |   2  |  2 |  3  |  3  |   4  |  4  |   5  |  5  |
# | Mậu/Quý   |  4 |  5  |  2  |  2  |   3  |  3 |  4  |  4  |   5  |  5  |   6  |  6  |
#
# Chú thích: 2=Thủy, 3=Mộc, 4=Kim, 5=Thổ, 6=Hỏa
# ═══════════════════════════════════════════════════════════════════════════════

CUC_TABLE = {
    # Giáp/Kỷ (0, 5) - "Giáp Kỷ chi niên Bính tác thủ"
    # Khởi Bính(2) từ Dần, đếm thuận → Nạp Âm xác định Cục
    0: {
        0: 'Thủy Nhị Cục',   # Tý  - Bính Tý → Giản Hạ Thủy
        1: 'Thủy Nhị Cục',   # Sửu - Đinh Sửu → Giản Hạ Thủy
        2: 'Hỏa Lục Cục',    # Dần - Bính Dần → Lô Trung Hỏa
        3: 'Hỏa Lục Cục',    # Mão - Đinh Mão → Lô Trung Hỏa
        4: 'Mộc Tam Cục',    # Thìn - Mậu Thìn → Đại Lâm Mộc
        5: 'Mộc Tam Cục',    # Tỵ  - Kỷ Tỵ → Đại Lâm Mộc
        6: 'Thổ Ngũ Cục',    # Ngọ - Canh Ngọ → Lộ Bàng Thổ
        7: 'Thổ Ngũ Cục',    # Mùi - Tân Mùi → Lộ Bàng Thổ
        8: 'Kim Tứ Cục',     # Thân - Nhâm Thân → Kiếm Phong Kim
        9: 'Kim Tứ Cục',     # Dậu - Quý Dậu → Kiếm Phong Kim
        10: 'Hỏa Lục Cục',   # Tuất - Giáp Tuất → Sơn Đầu Hỏa
        11: 'Hỏa Lục Cục',   # Hợi - Ất Hợi → Sơn Đầu Hỏa
    },
    5: {
        0: 'Thủy Nhị Cục',   # Tý
        1: 'Thủy Nhị Cục',   # Sửu
        2: 'Hỏa Lục Cục',    # Dần
        3: 'Hỏa Lục Cục',    # Mão
        4: 'Mộc Tam Cục',    # Thìn
        5: 'Mộc Tam Cục',    # Tỵ
        6: 'Thổ Ngũ Cục',    # Ngọ
        7: 'Thổ Ngũ Cục',    # Mùi
        8: 'Kim Tứ Cục',     # Thân
        9: 'Kim Tứ Cục',     # Dậu
        10: 'Hỏa Lục Cục',   # Tuất
        11: 'Hỏa Lục Cục',   # Hợi
    },
    # Ất/Canh (1, 6) - "Ất Canh chi niên Mậu tác thủ"
    # Khởi Mậu(4) từ Dần, đếm thuận → Nạp Âm xác định Cục
    1: {
        0: 'Hỏa Lục Cục',    # Tý  - Mậu Tý → Tích Lịch Hỏa
        1: 'Hỏa Lục Cục',    # Sửu - Kỷ Sửu → Tích Lịch Hỏa
        2: 'Thổ Ngũ Cục',    # Dần - Mậu Dần → Thành Đầu Thổ
        3: 'Thổ Ngũ Cục',    # Mão - Kỷ Mão → Thành Đầu Thổ
        4: 'Kim Tứ Cục',     # Thìn - Canh Thìn → Bạch Lạp Kim
        5: 'Kim Tứ Cục',     # Tỵ  - Tân Tỵ → Bạch Lạp Kim
        6: 'Mộc Tam Cục',    # Ngọ - Nhâm Ngọ → Dương Liễu Mộc
        7: 'Mộc Tam Cục',    # Mùi - Quý Mùi → Dương Liễu Mộc
        8: 'Thủy Nhị Cục',   # Thân - Giáp Thân → Tuyền Trung Thủy
        9: 'Thủy Nhị Cục',   # Dậu - Ất Dậu → Tuyền Trung Thủy
        10: 'Thổ Ngũ Cục',   # Tuất - Bính Tuất → Ốc Thượng Thổ
        11: 'Thổ Ngũ Cục',   # Hợi - Đinh Hợi → Ốc Thượng Thổ
    },
    6: {
        0: 'Hỏa Lục Cục',    # Tý
        1: 'Hỏa Lục Cục',    # Sửu
        2: 'Thổ Ngũ Cục',    # Dần
        3: 'Thổ Ngũ Cục',    # Mão
        4: 'Kim Tứ Cục',     # Thìn
        5: 'Kim Tứ Cục',     # Tỵ
        6: 'Mộc Tam Cục',    # Ngọ
        7: 'Mộc Tam Cục',    # Mùi
        8: 'Thủy Nhị Cục',   # Thân
        9: 'Thủy Nhị Cục',   # Dậu
        10: 'Thổ Ngũ Cục',   # Tuất
        11: 'Thổ Ngũ Cục',   # Hợi
    },
    # Bính/Tân (2, 7) - "Bính Tân chi niên Canh tác thủ"
    # Khởi Canh(6) từ Dần, đếm thuận → Nạp Âm xác định Cục
    2: {
        0: 'Thổ Ngũ Cục',    # Tý  - Canh Tý → Bích Thượng Thổ
        1: 'Thổ Ngũ Cục',    # Sửu - Tân Sửu → Bích Thượng Thổ
        2: 'Mộc Tam Cục',    # Dần - Canh Dần → Tùng Bách Mộc
        3: 'Mộc Tam Cục',    # Mão - Tân Mão → Tùng Bách Mộc
        4: 'Thủy Nhị Cục',   # Thìn - Nhâm Thìn → Trường Lưu Thủy
        5: 'Thủy Nhị Cục',   # Tỵ  - Quý Tỵ → Trường Lưu Thủy
        6: 'Kim Tứ Cục',     # Ngọ - Giáp Ngọ → Sa Trung Kim
        7: 'Kim Tứ Cục',     # Mùi - Ất Mùi → Sa Trung Kim
        8: 'Hỏa Lục Cục',    # Thân - Bính Thân → Sơn Hạ Hỏa
        9: 'Hỏa Lục Cục',    # Dậu - Đinh Dậu → Sơn Hạ Hỏa
        10: 'Mộc Tam Cục',   # Tuất - Mậu Tuất → Bình Địa Mộc
        11: 'Mộc Tam Cục',   # Hợi - Kỷ Hợi → Bình Địa Mộc
    },
    7: {
        0: 'Thổ Ngũ Cục',    # Tý
        1: 'Thổ Ngũ Cục',    # Sửu
        2: 'Mộc Tam Cục',    # Dần
        3: 'Mộc Tam Cục',    # Mão
        4: 'Thủy Nhị Cục',   # Thìn
        5: 'Thủy Nhị Cục',   # Tỵ
        6: 'Kim Tứ Cục',     # Ngọ
        7: 'Kim Tứ Cục',     # Mùi
        8: 'Hỏa Lục Cục',    # Thân
        9: 'Hỏa Lục Cục',    # Dậu
        10: 'Mộc Tam Cục',   # Tuất
        11: 'Mộc Tam Cục',   # Hợi
    },
    # Đinh/Nhâm (3, 8) - "Đinh Nhâm chi niên Nhâm tác thủ"
    # Khởi Nhâm(8) từ Dần, đếm thuận → Nạp Âm xác định Cục
    3: {
        0: 'Mộc Tam Cục',    # Tý  - Nhâm Tý → Tang Đố Mộc
        1: 'Mộc Tam Cục',    # Sửu - Quý Sửu → Tang Đố Mộc
        2: 'Kim Tứ Cục',     # Dần - Nhâm Dần → Kim Bạc Kim
        3: 'Kim Tứ Cục',     # Mão - Quý Mão → Kim Bạc Kim
        4: 'Hỏa Lục Cục',    # Thìn - Giáp Thìn → Phú Đăng Hỏa
        5: 'Hỏa Lục Cục',    # Tỵ  - Ất Tỵ → Phú Đăng Hỏa
        6: 'Thủy Nhị Cục',   # Ngọ - Bính Ngọ → Thiên Hà Thủy
        7: 'Thủy Nhị Cục',   # Mùi - Đinh Mùi → Thiên Hà Thủy
        8: 'Thổ Ngũ Cục',    # Thân - Mậu Thân → Đại Dịch Thổ
        9: 'Thổ Ngũ Cục',    # Dậu - Kỷ Dậu → Đại Dịch Thổ
        10: 'Kim Tứ Cục',    # Tuất - Canh Tuất → Thoa Xuyến Kim
        11: 'Kim Tứ Cục',    # Hợi - Tân Hợi → Thoa Xuyến Kim
    },
    8: {
        0: 'Mộc Tam Cục',    # Tý
        1: 'Mộc Tam Cục',    # Sửu
        2: 'Kim Tứ Cục',     # Dần
        3: 'Kim Tứ Cục',     # Mão
        4: 'Hỏa Lục Cục',    # Thìn
        5: 'Hỏa Lục Cục',    # Tỵ
        6: 'Thủy Nhị Cục',   # Ngọ
        7: 'Thủy Nhị Cục',   # Mùi
        8: 'Thổ Ngũ Cục',    # Thân
        9: 'Thổ Ngũ Cục',    # Dậu
        10: 'Kim Tứ Cục',    # Tuất
        11: 'Kim Tứ Cục',    # Hợi
    },
    # Mậu/Quý (4, 9) - "Mậu Quý chi niên Giáp tác thủ"
    # Khởi Giáp(0) từ Dần, đếm thuận → Nạp Âm xác định Cục
    4: {
        0: 'Kim Tứ Cục',     # Tý  - Giáp Tý → Hải Trung Kim
        1: 'Kim Tứ Cục',     # Sửu - Ất Sửu → Hải Trung Kim
        2: 'Thủy Nhị Cục',   # Dần - Giáp Dần → Đại Khê Thủy
        3: 'Thủy Nhị Cục',   # Mão - Ất Mão → Đại Khê Thủy
        4: 'Thổ Ngũ Cục',    # Thìn - Bính Thìn → Sa Trung Thổ
        5: 'Thổ Ngũ Cục',    # Tỵ  - Đinh Tỵ → Sa Trung Thổ
        6: 'Hỏa Lục Cục',    # Ngọ - Mậu Ngọ → Thiên Thượng Hỏa
        7: 'Hỏa Lục Cục',    # Mùi - Kỷ Mùi → Thiên Thượng Hỏa
        8: 'Mộc Tam Cục',    # Thân - Canh Thân → Thạch Lựu Mộc
        9: 'Mộc Tam Cục',    # Dậu - Tân Dậu → Thạch Lựu Mộc
        10: 'Thủy Nhị Cục',  # Tuất - Nhâm Tuất → Đại Hải Thủy
        11: 'Thủy Nhị Cục',  # Hợi - Quý Hợi → Đại Hải Thủy
    },
    9: {
        0: 'Kim Tứ Cục',     # Tý
        1: 'Kim Tứ Cục',     # Sửu
        2: 'Thủy Nhị Cục',   # Dần
        3: 'Thủy Nhị Cục',   # Mão
        4: 'Thổ Ngũ Cục',    # Thìn
        5: 'Thổ Ngũ Cục',    # Tỵ
        6: 'Hỏa Lục Cục',    # Ngọ
        7: 'Hỏa Lục Cục',    # Mùi
        8: 'Mộc Tam Cục',    # Thân
        9: 'Mộc Tam Cục',    # Dậu
        10: 'Thủy Nhị Cục',  # Tuất
        11: 'Thủy Nhị Cục',  # Hợi
    },
}
