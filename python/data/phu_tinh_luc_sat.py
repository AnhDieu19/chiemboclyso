"""
Data Layer - Lục Sát Tinh (6 Malefic Stars) Constants
"""

# Bảng tra Kinh Dương, Đà La theo Thiên Can năm sinh
KINH_DA = {
    0: {'kinh': 3, 'da': 1},   # Giáp: Mão, Sửu
    1: {'kinh': 4, 'da': 2},   # Ất: Thìn, Dần
    2: {'kinh': 6, 'da': 4},   # Bính: Ngọ, Thìn
    3: {'kinh': 7, 'da': 5},   # Đinh: Mùi, Tỵ
    4: {'kinh': 6, 'da': 4},   # Mậu: Ngọ, Thìn
    5: {'kinh': 7, 'da': 5},   # Kỷ: Mùi, Tỵ
    6: {'kinh': 9, 'da': 7},   # Canh: Dậu, Mùi
    7: {'kinh': 10, 'da': 8},  # Tân: Tuất, Thân
    8: {'kinh': 0, 'da': 10},  # Nhâm: Tý, Tuất
    9: {'kinh': 1, 'da': 11}   # Quý: Sửu, Hợi
}

# Bảng tra Hỏa Tinh, Linh Tinh theo Địa Chi năm sinh và giới tính
HOA_LINH_BASE = {
    'nam': {
        'hoa': [2, 3, 1, 1, 9, 10, 2, 3, 1, 1, 9, 10],
        'linh': [10, 10, 3, 3, 10, 10, 3, 3, 10, 10, 3, 3]
    },
    'nu': {
        'hoa': [10, 10, 1, 1, 10, 10, 1, 1, 10, 10, 1, 1],
        'linh': [2, 3, 1, 1, 9, 10, 2, 3, 1, 1, 9, 10]
    }
}
