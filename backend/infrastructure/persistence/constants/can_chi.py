"""
Data Layer - Can Chi and Nạp Âm Constants
"""

# 10 Thiên Can (Heavenly Stems)
THIEN_CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']

# 12 Địa Chi (Earthly Branches)
DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

# Ngũ Hành (Five Elements)
NGU_HANH = ['Kim', 'Thủy', 'Mộc', 'Hỏa', 'Thổ']

# Ngũ Hành của 12 Địa Chi (Cung vị)
# Mapping: Chi index (0-11) -> Ngũ Hành
CHI_NGU_HANH = {
    0: 'Thủy',   # Tý
    1: 'Thổ',    # Sửu
    2: 'Mộc',    # Dần
    3: 'Mộc',    # Mão
    4: 'Thổ',    # Thìn
    5: 'Hỏa',    # Tỵ
    6: 'Hỏa',    # Ngọ
    7: 'Thổ',    # Mùi
    8: 'Kim',    # Thân
    9: 'Kim',    # Dậu
    10: 'Thổ',   # Tuất
    11: 'Thủy'   # Hợi
}

# Giờ sinh ranges
GIO_SINH_RANGE = {
    0: '23:00 - 01:00',
    1: '01:00 - 03:00',
    2: '03:00 - 05:00',
    3: '05:00 - 07:00',
    4: '07:00 - 09:00',
    5: '09:00 - 11:00',
    6: '11:00 - 13:00',
    7: '13:00 - 15:00',
    8: '15:00 - 17:00',
    9: '17:00 - 19:00',
    10: '19:00 - 21:00',
    11: '21:00 - 23:00'
}

# Ngũ Hành Nạp Âm theo Thiên Can và Địa Chi
NAP_AM = {
    (0, 0): 'Hải Trung Kim', (1, 1): 'Hải Trung Kim',
    (2, 2): 'Lô Trung Hỏa', (3, 3): 'Lô Trung Hỏa',
    (4, 4): 'Đại Lâm Mộc', (5, 5): 'Đại Lâm Mộc',
    (6, 6): 'Lộ Bàng Thổ', (7, 7): 'Lộ Bàng Thổ',
    (8, 8): 'Kiếm Phong Kim', (9, 9): 'Kiếm Phong Kim',
    (0, 10): 'Sơn Đầu Hỏa', (1, 11): 'Sơn Đầu Hỏa',
    (2, 0): 'Giản Hạ Thủy', (3, 1): 'Giản Hạ Thủy',
    (4, 2): 'Thành Đầu Thổ', (5, 3): 'Thành Đầu Thổ',
    (6, 4): 'Bạch Lạp Kim', (7, 5): 'Bạch Lạp Kim',
    (8, 6): 'Dương Liễu Mộc', (9, 7): 'Dương Liễu Mộc',
    (0, 8): 'Tuyền Trung Thủy', (1, 9): 'Tuyền Trung Thủy',
    (2, 10): 'Ốc Thượng Thổ', (3, 11): 'Ốc Thượng Thổ',
    (4, 0): 'Tích Lịch Hỏa', (5, 1): 'Tích Lịch Hỏa',
    (6, 2): 'Tùng Bách Mộc', (7, 3): 'Tùng Bách Mộc',
    (8, 4): 'Trường Lưu Thủy', (9, 5): 'Trường Lưu Thủy',
    (0, 6): 'Sa Trung Kim', (1, 7): 'Sa Trung Kim',
    (2, 8): 'Sơn Hạ Hỏa', (3, 9): 'Sơn Hạ Hỏa',
    (4, 10): 'Bình Địa Mộc', (5, 11): 'Bình Địa Mộc',
    (6, 0): 'Bích Thượng Thổ', (7, 1): 'Bích Thượng Thổ',
    (8, 2): 'Kim Bạc Kim', (9, 3): 'Kim Bạc Kim',
    (0, 4): 'Phú Đăng Hỏa', (1, 5): 'Phú Đăng Hỏa',
    (2, 6): 'Thiên Hà Thủy', (3, 7): 'Thiên Hà Thủy',
    (4, 8): 'Đại Dịch Thổ', (5, 9): 'Đại Dịch Thổ',
    (6, 10): 'Thoa Xuyến Kim', (7, 11): 'Thoa Xuyến Kim',
    (8, 0): 'Tang Đố Mộc', (9, 1): 'Tang Đố Mộc',
    (0, 2): 'Đại Khê Thủy', (1, 3): 'Đại Khê Thủy',
    (2, 4): 'Sa Trung Thổ', (3, 5): 'Sa Trung Thổ',
    (4, 6): 'Thiên Thượng Hỏa', (5, 7): 'Thiên Thượng Hỏa',
    (6, 8): 'Thạch Lựu Mộc', (7, 9): 'Thạch Lựu Mộc',
    (8, 10): 'Đại Hải Thủy', (9, 11): 'Đại Hải Thủy',
}
