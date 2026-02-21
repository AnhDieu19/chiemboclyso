"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    TUẦN - TRIỆT VÀ CÁC SAO PHỤ QUAN TRỌNG                    ║
║                    Tuần Không, Triệt Lộ, Cô Thần, Quả Tú...                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  TUẦN (Tuần Không / Không Vong):                                            ║
║  - Dựa vào Can Chi năm sinh                                                 ║
║  - Mỗi Tuần có 10 năm, 2 Chi còn lại là vị trí Tuần                        ║
║                                                                              ║
║  TRIỆT (Triệt Lộ):                                                          ║
║  - Dựa vào Can năm sinh                                                     ║
║  - Mỗi Can có 2 cung bị Triệt cố định                                      ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════════════════════
# TRIỆT LỘ - Theo Thiên Can năm sinh
# Triệt = chặn, cắt đứt - sao hội ở cung Triệt bị giảm lực
# ═══════════════════════════════════════════════════════════════════════════════

TRIET_POSITION = {
    # Can năm: (Triệt 1, Triệt 2)
    0: (8, 9),    # Giáp: Thân, Dậu
    1: (8, 9),    # Ất: Thân, Dậu
    2: (6, 7),    # Bính: Ngọ, Mùi
    3: (6, 7),    # Đinh: Ngọ, Mùi
    4: (4, 5),    # Mậu: Thìn, Tỵ
    5: (2, 3),    # Kỷ: Dần, Mão
    6: (0, 1),    # Canh: Tý, Sửu
    7: (0, 1),    # Tân: Tý, Sửu
    8: (10, 11),  # Nhâm: Tuất, Hợi
    9: (10, 11),  # Quý: Tuất, Hợi
}

# ═══════════════════════════════════════════════════════════════════════════════
# CÔ THẦN - QUẢ TÚ
# Cô Thần (nam dùng), Quả Tú (nữ dùng) - Theo Địa Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

CO_THAN_QUA_TU = {
    # Chi năm: (Cô Thần, Quả Tú)
    # Dần, Mão, Thìn
    2: (5, 1),   # Dần: Cô Thần tại Tỵ, Quả Tú tại Sửu
    3: (5, 1),   # Mão: Cô Thần tại Tỵ, Quả Tú tại Sửu
    4: (5, 1),   # Thìn: Cô Thần tại Tỵ, Quả Tú tại Sửu
    # Tỵ, Ngọ, Mùi
    5: (8, 4),   # Tỵ: Cô Thần tại Thân, Quả Tú tại Thìn
    6: (8, 4),   # Ngọ: Cô Thần tại Thân, Quả Tú tại Thìn
    7: (8, 4),   # Mùi: Cô Thần tại Thân, Quả Tú tại Thìn
    # Thân, Dậu, Tuất
    8: (11, 7),  # Thân: Cô Thần tại Hợi, Quả Tú tại Mùi
    9: (11, 7),  # Dậu: Cô Thần tại Hợi, Quả Tú tại Mùi
    10: (11, 7), # Tuất: Cô Thần tại Hợi, Quả Tú tại Mùi
    # Hợi, Tý, Sửu
    11: (2, 10), # Hợi: Cô Thần tại Dần, Quả Tú tại Tuất
    0: (2, 10),  # Tý: Cô Thần tại Dần, Quả Tú tại Tuất
    1: (2, 10),  # Sửu: Cô Thần tại Dần, Quả Tú tại Tuất
}

# ═══════════════════════════════════════════════════════════════════════════════
# THAI PHỤ - PHONG CÁC
# Theo Địa Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

THAI_PHU_PHONG_CAC = {
    # Chi năm: (Thái Phụ, Phong Các)
    0: (5, 3),   # Tý: Thái Phụ tại Tỵ, Phong Các tại Mão
    1: (6, 4),   # Sửu: Thái Phụ tại Ngọ, Phong Các tại Thìn
    2: (7, 5),   # Dần: Thái Phụ tại Mùi, Phong Các tại Tỵ
    3: (8, 6),   # Mão: Thái Phụ tại Thân, Phong Các tại Ngọ
    4: (9, 7),   # Thìn: Thái Phụ tại Dậu, Phong Các tại Mùi
    5: (10, 8),  # Tỵ: Thái Phụ tại Tuất, Phong Các tại Thân
    6: (11, 9),  # Ngọ: Thái Phụ tại Hợi, Phong Các tại Dậu
    7: (0, 10),  # Mùi: Thái Phụ tại Tý, Phong Các tại Tuất
    8: (1, 11),  # Thân: Thái Phụ tại Sửu, Phong Các tại Hợi
    9: (2, 0),   # Dậu: Thái Phụ tại Dần, Phong Các tại Tý
    10: (3, 1),  # Tuất: Thái Phụ tại Mão, Phong Các tại Sửu
    11: (4, 2),  # Hợi: Thái Phụ tại Thìn, Phong Các tại Dần
}

# ═══════════════════════════════════════════════════════════════════════════════
# GIẢI THẦN - THIÊN GIẢI
# Theo Địa Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

GIAI_THAN_THIEN_GIAI = {
    # Chi năm: (Giải Thần, Thiên Giải)
    # Giải Thần: An theo Phượng Các (nghịch từ Tuất)
    # Thiên Giải: An theo Chi năm (như bảng cũ)
    0: (10, 11),  # Tý
    1: (9, 0),    # Sửu
    2: (8, 1),    # Dần
    3: (7, 2),    # Mão
    4: (6, 3),    # Thìn
    5: (5, 4),    # Tỵ
    6: (4, 5),    # Ngọ
    7: (3, 6),    # Mùi
    8: (2, 7),    # Thân
    9: (1, 8),    # Dậu
    10: (0, 9),   # Tuất
    11: (11, 10), # Hợi
}

# ═══════════════════════════════════════════════════════════════════════════════
# THIÊN ĐỨC - NGUYỆT ĐỨC (Theo Chi năm, khác với Long Đức Nguyệt Đức theo tháng)
# ═══════════════════════════════════════════════════════════════════════════════

THIEN_DUC_NGUYET_DUC_YEAR = {
    # Chi năm: (Thiên Đức, Nguyệt Đức)
    0: (9, 9),    # Tý: Dậu, Dậu
    1: (8, 8),    # Sửu: Thân, Thân
    2: (7, 7),    # Dần: Mùi, Mùi
    3: (6, 6),    # Mão: Ngọ, Ngọ
    4: (5, 5),    # Thìn: Tỵ, Tỵ
    5: (4, 4),    # Tỵ: Thìn, Thìn
    6: (3, 3),    # Ngọ: Mão, Mão
    7: (2, 2),    # Mùi: Dần, Dần
    8: (1, 1),    # Thân: Sửu, Sửu
    9: (0, 0),    # Dậu: Tý, Tý
    10: (11, 11), # Tuất: Hợi, Hợi
    11: (10, 10), # Hợi: Tuất, Tuất
}

# ═══════════════════════════════════════════════════════════════════════════════
# LƯU HÀ (Theo Thiên Can năm sinh)
# ═══════════════════════════════════════════════════════════════════════════════

LUU_HA_POSITION = {
    # Can năm: vị trí Lưu Hà
    0: 9,   # Giáp: Dậu
    1: 10,  # Ất: Tuất
    2: 7,   # Bính: Mùi
    3: 8,   # Đinh: Thân
    4: 5,   # Mậu: Tỵ
    5: 6,   # Kỷ: Ngọ
    6: 4,   # Canh: Thìn
    7: 3,   # Tân: Mão
    8: 11,  # Nhâm: Hợi
    9: 2,   # Quý: Dần
}

# (Thiên Y nay tính theo tháng trong logic code)


# ═══════════════════════════════════════════════════════════════════════════════
# KIẾP SÁT - PHÁ TOÁI
# Theo Địa Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

KIEP_SAT_POSITION = {
    # Chi năm: vị trí Kiếp Sát
    # Thân Tý Thìn → Tỵ, Tỵ Dậu Sửu → Dần, Dần Ngọ Tuất → Hợi, Hợi Mão Mùi → Thân
    0: 5,   # Tý → Tỵ
    1: 2,   # Sửu → Dần
    2: 11,  # Dần → Hợi
    3: 8,   # Mão → Thân
    4: 5,   # Thìn → Tỵ
    5: 2,   # Tỵ → Dần
    6: 11,  # Ngọ → Hợi
    7: 8,   # Mùi → Thân
    8: 5,   # Thân → Tỵ
    9: 2,   # Dậu → Dần
    10: 11, # Tuất → Hợi
    11: 8,  # Hợi → Thân
}

PHA_TOAI_POSITION = {
    # Chi năm: vị trí Phá Toái
    # Tý Ngọ Mão Dậu → Tỵ
    # Dần Thân Tỵ Hợi → Dậu
    # Thìn Tuất Sửu Mùi → Sửu
    0: 5,   # Tý → Tỵ
    1: 1,   # Sửu → Sửu
    2: 9,   # Dần → Dậu
    3: 5,   # Mão → Tỵ
    4: 1,   # Thìn → Sửu
    5: 9,   # Tỵ → Dậu
    6: 5,   # Ngọ → Tỵ
    7: 1,   # Mùi → Sửu
    8: 9,   # Thân → Dậu
    9: 5,   # Dậu → Tỵ
    10: 1,  # Tuất → Sửu
    11: 9,  # Hợi → Dậu
}

# ═══════════════════════════════════════════════════════════════════════════════
# THIÊN VU - THIÊN KHỐC (bổ sung, theo tháng)
# ═══════════════════════════════════════════════════════════════════════════════

THIEN_VU_POSITION = {
    # Tháng: vị trí Thiên Vu
    1: 6, 2: 7, 3: 8, 4: 9, 5: 10, 6: 11,
    7: 0, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5
}

# ═══════════════════════════════════════════════════════════════════════════════
# THIÊN TÀI - THIÊN THỌ (bổ sung cho trường hợp tính theo năm)
# Đã có theo tháng trong phu_tinh_other.py, đây là theo năm
# ═══════════════════════════════════════════════════════════════════════════════

THIEN_TAI_THO_YEAR = {
    # Chi năm: (Thiên Tài, Thiên Thọ)
    0: (11, 9),   # Tý
    1: (0, 10),   # Sửu
    2: (1, 11),   # Dần
    3: (2, 0),    # Mão
    4: (3, 1),    # Thìn
    5: (4, 2),    # Tỵ
    6: (5, 3),    # Ngọ
    7: (6, 4),    # Mùi
    8: (7, 5),    # Thân
    9: (8, 6),    # Dậu
    10: (9, 7),   # Tuất
    11: (10, 8),  # Hợi
}

# ═══════════════════════════════════════════════════════════════════════════════
# HÀM TÍNH TUẦN (TUẦN KHÔNG / KHÔNG VONG)
# Tuần dựa vào Can Chi năm sinh, tìm 2 Chi "trống" không thuộc Tuần đó
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_tuan_position(can_index: int, chi_index: int) -> tuple:
    """
    Tính vị trí Tuần (Tuần Không) dựa trên Can Chi năm sinh
    
    NGUYÊN LÝ:
    - Mỗi Tuần có 10 năm, bắt đầu từ 1 năm Giáp (Can = 0)
    - 10 Can kết hợp với 10 Chi liên tiếp
    - 2 Chi còn lại (không có trong Tuần) là vị trí Tuần Không
    
    CÔNG THỨC:
    - Tìm Chi đầu Tuần (Chi tại năm Giáp đầu Tuần)
    - chi_đầu_tuần = (chi_năm - can_năm + 12) % 12
    - Tuần 1 = (chi_đầu_tuần + 10) % 12
    - Tuần 2 = (chi_đầu_tuần + 11) % 12
    
    VÍ DỤ:
    - Năm Giáp Tý (can=0, chi=0): Chi đầu = 0 (Tý) → Tuần tại 10 (Tuất), 11 (Hợi)
    - Năm Ất Sửu (can=1, chi=1): Chi đầu = (1-1+12)%12 = 0 (Tý) → Tuần tại Tuất, Hợi
    - Năm Giáp Tuất (can=0, chi=10): Chi đầu = 10 (Tuất) → Tuần tại 8 (Thân), 9 (Dậu)
    
    Args:
        can_index: Index Can năm (0-9)
        chi_index: Index Chi năm (0-11)
        
    Returns:
        tuple (tuan_1, tuan_2): 2 vị trí Tuần Không
    """
    # Tìm Chi đầu Tuần (Chi của năm Giáp trong Tuần này)
    chi_dau_tuan = (chi_index - can_index + 12) % 12
    
    # 2 Chi cuối cùng của Tuần (vị trí Tuần Không)
    tuan_1 = (chi_dau_tuan + 10) % 12
    tuan_2 = (chi_dau_tuan + 11) % 12
    
    return (tuan_1, tuan_2)

