"""
Data Layer - Lục Cát Tinh (6 Auspicious Stars) Constants
"""

# Phụ Tinh bases for Lục Cát
TA_PHU_BASE = 4    # Thìn
HUU_BAT_BASE = 10  # Tuất
VAN_XUONG_BASE = 10  # Tuất
VAN_KHUC_BASE = 4    # Thìn

# Bảng tra Thiên Khôi, Thiên Việt theo Thiên Can năm sinh
THIEN_KHOI_VIET = {
    0: {'khoi': 1, 'viet': 7},   # Giáp: Sửu, Mùi
    1: {'khoi': 0, 'viet': 8},   # Ất: Tý, Thân
    2: {'khoi': 11, 'viet': 9},  # Bính: Hợi, Dậu
    3: {'khoi': 11, 'viet': 9},  # Đinh: Hợi, Dậu
    4: {'khoi': 1, 'viet': 7},   # Mậu: Sửu, Mùi
    5: {'khoi': 0, 'viet': 8},   # Kỷ: Tý, Thân
    6: {'khoi': 6, 'viet': 2},   # Canh: Ngọ, Dần
    7: {'khoi': 6, 'viet': 3},   # Tân: Ngọ, Mão
    8: {'khoi': 3, 'viet': 5},   # Nhâm: Mão, Tỵ
    9: {'khoi': 3, 'viet': 5}    # Quý: Mão, Tỵ
}
