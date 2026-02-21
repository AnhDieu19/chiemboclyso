"""
Data Layer - Other Auxiliary Stars Constants
"""

# Thiên Mã theo Địa Chi năm sinh
THIEN_MA_POSITION = {
    0: 2, 1: 11, 2: 8, 3: 5, 4: 2, 5: 11, 6: 8, 7: 5, 8: 2, 9: 11, 10: 8, 11: 5
}

# Hồng Loan, Thiên Hỹ theo Địa Chi năm sinh
HONG_LOAN_THIEN_HY = {
    0: {'hong_loan': 3, 'thien_hy': 9},
    1: {'hong_loan': 2, 'thien_hy': 8},
    2: {'hong_loan': 1, 'thien_hy': 7},
    3: {'hong_loan': 0, 'thien_hy': 6},
    4: {'hong_loan': 11, 'thien_hy': 5},
    5: {'hong_loan': 10, 'thien_hy': 4},
    6: {'hong_loan': 9, 'thien_hy': 3},
    7: {'hong_loan': 8, 'thien_hy': 2},
    8: {'hong_loan': 7, 'thien_hy': 1},
    9: {'hong_loan': 6, 'thien_hy': 0},
    10: {'hong_loan': 5, 'thien_hy': 11},
    11: {'hong_loan': 4, 'thien_hy': 10}
}

# Đào Hoa theo Địa Chi năm sinh
DAO_HOA_POSITION = {0: 9, 1: 6, 2: 3, 3: 0, 4: 9, 5: 6, 6: 3, 7: 0, 8: 9, 9: 6, 10: 3, 11: 0}

# Hoa Cái theo Địa Chi năm sinh
HOA_CAI_POSITION = {0: 4, 1: 1, 2: 10, 3: 7, 4: 4, 5: 1, 6: 10, 7: 7, 8: 4, 9: 1, 10: 10, 11: 7}

# Long Đức, Nguyệt Đức theo tháng sinh
LONG_NGUYET_DUC = {
    1: {'long': 5, 'nguyet': 5}, 2: {'long': 6, 'nguyet': 8}, 3: {'long': 7, 'nguyet': 11},
    4: {'long': 8, 'nguyet': 2}, 5: {'long': 9, 'nguyet': 5}, 6: {'long': 10, 'nguyet': 8},
    7: {'long': 11, 'nguyet': 11}, 8: {'long': 0, 'nguyet': 2}, 9: {'long': 1, 'nguyet': 5},
    10: {'long': 2, 'nguyet': 8}, 11: {'long': 3, 'nguyet': 11}, 12: {'long': 4, 'nguyet': 2}
}


# Thiên Quan, Thiên Phúc theo Thiên Can năm sinh
THIEN_QUAN_PHUC = {
    0: {'quan': 7, 'phuc': 9}, 1: {'quan': 4, 'phuc': 8}, 2: {'quan': 0, 'phuc': 0},
    3: {'quan': 9, 'phuc': 11}, 4: {'quan': 3, 'phuc': 3}, 5: {'quan': 9, 'phuc': 2},
    6: {'quan': 11, 'phuc': 5}, 7: {'quan': 6, 'phuc': 6}, 8: {'quan': 11, 'phuc': 5},
    9: {'quan': 2, 'phuc': 2}
}


# Thiên Thường, Thiên Sứ base (Mão, Dậu)
THIEN_THUONG_SU_BASE = {'thuong': 3, 'su': 9}

# Phong Cáo theo Thiên Can năm sinh
PHONG_CAO_POSITION = {0: 8, 1: 9, 2: 8, 3: 9, 4: 10, 5: 11, 6: 8, 7: 9, 8: 8, 9: 9}

# Quốc Ấn theo Địa Chi năm sinh
QUOC_AN_POSITION = {0: 10, 1: 11, 2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 5, 8: 6, 9: 7, 10: 8, 11: 9}

# Đường Phù theo giờ sinh
DUONG_PHU_POSITION = {0: 5, 1: 4, 2: 3, 3: 2, 4: 1, 5: 0, 6: 11, 7: 10, 8: 9, 9: 8, 10: 7, 11: 6}


# Thiên Thọ, Thiên Tài theo tháng sinh
THIEN_THO_TAI = {
    1: {'tho': 1, 'tai': 5}, 2: {'tho': 0, 'tai': 4}, 3: {'tho': 11, 'tai': 3},
    4: {'tho': 10, 'tai': 2}, 5: {'tho': 9, 'tai': 1}, 6: {'tho': 8, 'tai': 0},
    7: {'tho': 7, 'tai': 11}, 8: {'tho': 6, 'tai': 10}, 9: {'tho': 5, 'tai': 9},
    10: {'tho': 2, 'tai': 8}, 11: {'tho': 3, 'tai': 7}, 12: {'tho': 2, 'tai': 6}
}

# Thiên Trù theo Thiên Can năm sinh
THIEN_TRU_POSITION = {0: 5, 1: 0, 2: 0, 3: 5, 4: 6, 5: 6, 6: 2, 7: 2, 8: 9, 9: 9}


# Thiên Diêu theo giờ sinh
THIEN_DIEU_POSITION = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 0}

# Thiên La, Địa Võng (cố định)
THIEN_LA_POSITION = 4   # Thìn
DIA_VONG_POSITION = 10  # Tuất

# Ân Quang, Thiên Quý theo Thiên Can năm sinh
AN_QUANG_THIEN_QUY = {
    0: {'an_quang': 1, 'thien_quy': 7}, 1: {'an_quang': 0, 'thien_quy': 6},
    2: {'an_quang': 11, 'thien_quy': 5}, 3: {'an_quang': 10, 'thien_quy': 4},
    4: {'an_quang': 9, 'thien_quy': 3}, 5: {'an_quang': 8, 'thien_quy': 2},
    6: {'an_quang': 7, 'thien_quy': 1}, 7: {'an_quang': 6, 'thien_quy': 0},
    8: {'an_quang': 5, 'thien_quy': 11}, 9: {'an_quang': 4, 'thien_quy': 10}
}

# Thiên Hình theo Thiên Can năm sinh
THIEN_HINH_POSITION = {0: 9, 1: 9, 2: 0, 3: 0, 4: 3, 5: 3, 6: 6, 7: 6, 8: 9, 9: 9}

# Tam Thai, Bát Tọa base (Dần, Thân)
TAM_THAI_BASE = 2
BAT_TOA_BASE = 8

# Địa Giải theo tháng sinh
# Tháng 1 Mùi, 2 Thân... (Mùi + month - 1)
def calculate_dia_giai(month: int) -> int:
    return (7 + month - 1) % 12

# Lưu Niên Văn Tinh (Theo Thiên Can)
LN_VAN_TINH = {
    0: 5,   # Giáp: Tỵ
    1: 6,   # Ất: Ngọ
    2: 8,   # Bính: Thân
    3: 9,   # Đinh: Dậu
    4: 8,   # Mậu: Thân
    5: 9,   # Kỷ: Dậu
    6: 11,  # Canh: Hợi
    7: 0,   # Tân: Tý
    8: 2,   # Nhâm: Dần
    9: 3,   # Quý: Mão
}
