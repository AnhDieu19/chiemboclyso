"""
Data Layer - Vòng Thái Tuế (12 Stars) Constants
"""

# Thái Tuế vòng (theo Địa Chi năm sinh đi thuận)
THAI_TUE_STARS = [
    'Thái Tuế', 'Thiếu Dương', 'Tang Môn', 'Thiếu Âm', 'Quan Phù', 'Từ Phù',
    'Tuế Phá', 'Long Đức', 'Bạch Hổ', 'Phúc Đức', 'Điếu Khách', 'Trực Phù'
]

# Tuế Phá, Thiên Khốc, Thiên Hư theo Địa Chi năm sinh
TUE_STARS = {
    # thien_khoc: Ngọ nghịch, thien_hu: Ngọ thuận
    0: {'tue_pha': 6, 'thien_khoc': 6, 'thien_hu': 6},   # Tý (Khốc Hư đồng cung Ngọ)
    1: {'tue_pha': 7, 'thien_khoc': 5, 'thien_hu': 7},   # Sửu
    2: {'tue_pha': 8, 'thien_khoc': 4, 'thien_hu': 8},   # Dần
    3: {'tue_pha': 9, 'thien_khoc': 3, 'thien_hu': 9},   # Mão
    4: {'tue_pha': 10, 'thien_khoc': 2, 'thien_hu': 10}, # Thìn
    5: {'tue_pha': 11, 'thien_khoc': 1, 'thien_hu': 11}, # Tỵ
    6: {'tue_pha': 0, 'thien_khoc': 0, 'thien_hu': 0},   # Ngọ (Khốc Hư đồng cung Tý)
    7: {'tue_pha': 1, 'thien_khoc': 11, 'thien_hu': 1},  # Mùi
    8: {'tue_pha': 2, 'thien_khoc': 10, 'thien_hu': 2},  # Thân
    9: {'tue_pha': 3, 'thien_khoc': 9, 'thien_hu': 3},   # Dậu
    10: {'tue_pha': 4, 'thien_khoc': 8, 'thien_hu': 4},  # Tuất (Khốc Thân, Hư Thìn)
    11: {'tue_pha': 5, 'thien_khoc': 7, 'thien_hu': 5}   # Hợi
}
