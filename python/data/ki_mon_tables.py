"""
Kì Môn Data Tables - Lookup tables cho Kì Môn Độn Giáp

Bao gồm: Tam Kỳ, Bát Môn, Cửu Tinh, Bát Thần
"""

# =============================================
# TAM KỲ (3 Kỳ)
# =============================================

TAM_KY = {
    'Ất': {
        'han': '乙',
        'alias': 'Nhật Kỳ',
        'meaning': 'Mặt trời, áng sáng, dương khí',
        'nature': 'dai_cat',
        'score': 10,
        'direction': 'Đông',
        'ngu_hanh': 'Mộc'
    },
    'Bính': {
        'han': '丙',
        'alias': 'Nguyệt Kỳ',
        'meaning': 'Mặt trăng, hy vọng, tài vận',
        'nature': 'dai_cat',
        'score': 9,
        'direction': 'Nam',
        'ngu_hanh': 'Hỏa'
    },
    'Đinh': {
        'han': '丁',
        'alias': 'Tinh Kỳ',
        'meaning': 'Sao, văn chương, quý nhân',
        'nature': 'dai_cat',
        'score': 8,
        'direction': 'Nam',
        'ngu_hanh': 'Hỏa'
    }
}


# =============================================
# BÁT MÔN (8 Cửa)
# =============================================

BAT_MON = {
    'Khai': {
        'han': '開門',
        'meaning': 'Mở cửa, khai thông, khởi đầu',
        'nature': 'cat',
        'score': 8,
        'direction': 'Tây Bắc',
        'applications': ['khởi nghiệp', 'xuất hành', 'khai trương']
    },
    'Hưu': {
        'han': '休門',
        'meaning': 'Nghỉ ngơi, an nhàn, phúc lộc',
        'nature': 'cat',
        'score': 7,
        'direction': 'Bắc',
        'applications': ['nghỉ dưỡng', 'cầu tài', 'yết kiến']
    },
    'Sinh': {
        'han': '生門',
        'meaning': 'Sinh sôi, phát triển, tài lộc',
        'nature': 'cat',
        'score': 9,
        'direction': 'Đông Bắc',
        'applications': ['kinh doanh', 'đầu tư', 'cầu tài']
    },
    'Thương': {
        'han': '傷門',
        'meaning': 'Tổn thương, tranh đấu, cạnh tranh',
        'nature': 'hung',
        'score': -5,
        'direction': 'Đông',
        'applications': ['tránh xuất hành', 'cẩn thận tai nạn']
    },
    'Đỗ': {
        'han': '杜門',
        'meaning': 'Đóng cửa, ẩn dật, bảo mật',
        'nature': 'trung',
        'score': 2,
        'direction': 'Đông Nam',
        'applications': ['ẩn náu', 'bảo mật', 'tránh né']
    },
    'Cảnh': {
        'han': '景門',
        'meaning': 'Cảnh đẹp, danh tiếng, văn chương',
        'nature': 'cat_hung',
        'score': 3,
        'direction': 'Nam',
        'applications': ['thi cử', 'văn chương', 'danh tiếng']
    },
    'Tử': {
        'han': '死門',
        'meaning': 'Chết chóc, kết thúc, tang lễ',
        'nature': 'hung',
        'score': -8,
        'direction': 'Tây Nam',
        'applications': ['tránh mọi việc', 'tang lễ OK']
    },
    'Kinh': {
        'han': '驚門',
        'meaning': 'Kinh sợ, lo lắng, kiện tụng',
        'nature': 'hung',
        'score': -6,
        'direction': 'Tây',
        'applications': ['tránh xuất hành', 'kiện tụng bất lợi']
    }
}

# Thứ tự Bát Môn phi cung
BAT_MON_ORDER = ['Hưu', 'Sinh', 'Thương', 'Đỗ', 'Cảnh', 'Tử', 'Kinh', 'Khai']


# =============================================
# CỬU TINH (9 Sao Kì Môn)
# =============================================

CUU_TINH = {
    'Thiên Bồng': {
        'han': '天蓬',
        'ngu_hanh': 'Thủy',
        'palace': 1,   # Cung Khảm
        'nature': 'hung',
        'score': -4,
        'meaning': 'Hung tinh, phá hoại, trộm cắp'
    },
    'Thiên Nhuế': {
        'han': '天芮',
        'ngu_hanh': 'Thổ',
        'palace': 2,   # Cung Khôn
        'nature': 'hung',
        'score': -5,
        'meaning': 'Bệnh phù, hung tinh, tật bệnh'
    },
    'Thiên Xung': {
        'han': '天衝',
        'ngu_hanh': 'Mộc',
        'palace': 3,   # Cung Chấn
        'nature': 'cat_hung',
        'score': 2,
        'meaning': 'Xung đột, nhưng có thể hóa giải'
    },
    'Thiên Phụ': {
        'han': '天輔',
        'ngu_hanh': 'Mộc',
        'palace': 4,   # Cung Tốn
        'nature': 'cat',
        'score': 8,
        'meaning': 'Phù trợ, quý nhân, giúp đỡ'
    },
    'Thiên Cấm': {
        'han': '天禽',
        'ngu_hanh': 'Thổ',
        'palace': 5,   # Trung Cung
        'nature': 'trung',
        'score': 3,
        'meaning': 'Trung cung, ổn định, thiền Phật'
    },
    'Thiên Tâm': {
        'han': '天心',
        'ngu_hanh': 'Kim',
        'palace': 6,   # Cung Kiền
        'nature': 'cat',
        'score': 9,
        'meaning': 'Đại cát, chữa bệnh, giúp người'
    },
    'Thiên Trụ': {
        'han': '天柱',
        'ngu_hanh': 'Kim',
        'palace': 7,   # Cung Đoài
        'nature': 'cat_hung',
        'score': 1,
        'meaning': 'Cột trụ, nhưng cũng khắc nghiệt'
    },
    'Thiên Nhậm': {
        'han': '天任',
        'ngu_hanh': 'Thổ',
        'palace': 8,   # Cung Cấn
        'nature': 'cat',
        'score': 7,
        'meaning': 'Cát tinh, trung hậu, đáng tin'
    },
    'Thiên Anh': {
        'han': '天英',
        'ngu_hanh': 'Hỏa',
        'palace': 9,   # Cung Ly
        'nature': 'cat_hung',
        'score': 0,
        'meaning': 'Hỏa tính, biến động, sáng tạo'
    }
}

# Thứ tự Cửu Tinh phi cung (bỏ Thiên Cấm ở Trung Cung)
# Khảm(1)→Khôn(2)→Chấn(3)→Tốn(4)→Kiền(6)→Đoài(7)→Cấn(8)→Ly(9)
CUU_TINH_ORDER = ['Thiên Bồng', 'Thiên Nhuế', 'Thiên Xung', 'Thiên Phụ', 
                  'Thiên Tâm', 'Thiên Trụ', 'Thiên Nhậm', 'Thiên Anh']


# =============================================
# BÁT THẦN (8 Thần)
# =============================================

BAT_THAN = {
    'Trực Phù': {
        'han': '值符',
        'meaning': 'Thần chủ, đứng đầu, quý nhân',
        'nature': 'dai_cat',
        'score': 10
    },
    'Đằng Xà': {
        'han': '螣蛇',
        'meaning': 'Rắn lượn, biến hóa, mưu kế',
        'nature': 'hung',
        'score': -3
    },
    'Thái Âm': {
        'han': '太陰',
        'meaning': 'Âm nhu, ẩn giấu, bí mật',
        'nature': 'cat',
        'score': 6
    },
    'Lục Hợp': {
        'han': '六合',
        'meaning': 'Hòa hợp, kết hợp, hôn nhân',
        'nature': 'cat',
        'score': 7
    },
    'Câu Trần': {
        'han': '勾陳',
        'meaning': 'Câu trần, trì trệ, chậm trễ',
        'nature': 'hung',
        'score': -4
    },
    'Chu Tước': {
        'han': '朱雀',
        'meaning': 'Khẩu thiệt, văn chương, thị phi',
        'nature': 'cat_hung',
        'score': 0
    },
    'Cửu Địa': {
        'han': '九地',
        'meaning': 'Ổn định, bền vững, bất động sản',
        'nature': 'cat',
        'score': 5
    },
    'Cửu Thiên': {
        'han': '九天',
        'meaning': 'Cao quý, tôn kính, quyền uy',
        'nature': 'dai_cat',
        'score': 9
    }
}

# Thứ tự Bát Thần phi cung
BAT_THAN_ORDER = ['Trực Phù', 'Đằng Xà', 'Thái Âm', 'Lục Hợp', 
                  'Câu Trần', 'Chu Tước', 'Cửu Địa', 'Cửu Thiên']


# =============================================
# BẢNG CỤC THEO TIẾT KHÍ - 3 NGUYÊN (Thượng/Trung/Hạ)
# =============================================
# Mỗi tiết khí ~15 ngày = 3 nguyên x 5 ngày.
# Thượng Nguyên: 5 ngày đầu
# Trung Nguyên: 5 ngày giữa 
# Hạ Nguyên: 5 ngày cuối
#
# Dương Độn: Đông Chí → Hạ Chí (tăng dần)
# Âm Độn: Hạ Chí → Đông Chí (giảm dần)
# =============================================

# Cục theo Tiết Khí (Dương Độn) - {index: (thượng, trung, hạ)}
# Đông Chí bắt đầu Dương Độn (index 23 theo jie_qi_calculator)
DUONG_DON_CUC = {
    23: (1, 7, 4),  # Đông Chí
    0:  (2, 8, 5),  # Tiểu Hàn
    1:  (3, 9, 6),  # Đại Hàn
    2:  (8, 5, 2),  # Lập Xuân
    3:  (9, 6, 3),  # Vũ Thủy
    4:  (1, 7, 4),  # Kinh Trập
    5:  (3, 9, 6),  # Xuân Phân
    6:  (4, 1, 7),  # Thanh Minh
    7:  (5, 2, 8),  # Cốc Vũ
    8:  (4, 1, 7),  # Lập Hạ
    9:  (5, 2, 8),  # Tiểu Mãn
    10: (6, 3, 9),  # Mang Chủng
}

# Cục theo Tiết Khí (Âm Độn) - {index: (thượng, trung, hạ)}
# Hạ Chí bắt đầu Âm Độn
AM_DON_CUC = {
    11: (9, 3, 6),  # Hạ Chí
    12: (8, 2, 5),  # Tiểu Thử
    13: (7, 1, 4),  # Đại Thử
    14: (2, 5, 8),  # Lập Thu
    15: (1, 4, 7),  # Xử Thử
    16: (9, 3, 6),  # Bạch Lộ
    17: (7, 1, 4),  # Thu Phân
    18: (6, 9, 3),  # Hàn Lộ
    19: (5, 8, 2),  # Sương Giáng
    20: (6, 9, 3),  # Lập Đông
    21: (5, 8, 2),  # Tiểu Tuyết
    22: (4, 7, 1),  # Đại Tuyết
}


# Legacy: Bảng đơn giản (1 cục/tiết khí) cho backward compatibility
def get_cuc_simple(tiet_khi_index: int, is_duong_don: bool) -> int:
    """Trả về cục Thượng Nguyên mặc định (cho backward compat)"""
    table = DUONG_DON_CUC if is_duong_don else AM_DON_CUC
    if tiet_khi_index in table:
        return table[tiet_khi_index][0]  # Thượng Nguyên
    # Fallback
    return 1


def get_cuc_by_yuan(tiet_khi_index: int, yuan: int, is_duong_don: bool) -> int:
    """
    Lấy Cục theo Tiết Khí và Nguyên (Thượng/Trung/Hạ).
    
    Args:
        tiet_khi_index: Index tiết khí (0-23)
        yuan: 0=Thượng, 1=Trung, 2=Hạ
        is_duong_don: True nếu Dương Độn
    
    Returns:
        Số cục (1-9)
    """
    table = DUONG_DON_CUC if is_duong_don else AM_DON_CUC
    if tiet_khi_index in table:
        return table[tiet_khi_index][yuan % 3]
    # Fallback: tìm trong bảng kia
    other = AM_DON_CUC if is_duong_don else DUONG_DON_CUC
    if tiet_khi_index in other:
        return other[tiet_khi_index][yuan % 3]
    return 1
