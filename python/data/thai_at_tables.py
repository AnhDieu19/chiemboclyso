"""
Thái Ất Data Tables - Lookup tables cho Thái Ất Thần Số

Bao gồm: 16 Thần, Ngũ Nguyên, Hội, Kỷ, Ngũ Hành 16 Thần, Thập Can Hóa Khí

Tham khảo:
  - Sách Thái Ất (mục Ngũ Hành 16 Thần, mục Thập Can Hóa Khí)
  - Thái Ất Thần Kinh
"""

# =============================================
# 16 THẦN THÁI ẤT
# =============================================

THAP_LUC_THAN = {
    # 1. Thái Ất (Chủ Tướng) - Chu kỳ 1 (mỗi năm 1 cung)
    1: {
        'name': 'Thái Ất',
        'han': '太乙',
        'nature': 'cat',
        'score': 10,
        'meaning': 'Đế tinh, chủ quyền, vận quốc thịnh',
        'fields': ['chính trị', 'lãnh đạo', 'quyền lực'],
        'cycle_length': 1,  # Di chuyển mỗi năm 1 cung (tuy nhiên logic Thái Ất đặc biệt)
        'type': 'chu_tuong'
    },
    # 2. Văn Xương (Chủ Tướng) - Di chuyển 3 năm 1 cung (logic sách Gốc tích số chia 18)
    # Tuy nhiên sách Ref ghi: "Văn Xương tới Ngọ...". Logic thường là mỗi 3 năm 1 cung.
    # Trong sách có đoạn: "Thời gian an cung của sao Ngũ Phúc là 45".
    # Ta sẽ giả định các cycle_length cơ bản dựa trên tài liệu Thái Ất Thống Tông:
    # Thái Ất (1), Văn Xương (3), Chủ Đại Tướng (3), Khách Đại Tướng (3)...
    2: {
        'name': 'Văn Xương',
        'han': '文昌',
        'nature': 'cat',
        'score': 8,
        'meaning': 'Văn chương, học vấn, khoa cử',
        'fields': ['giáo dục', 'văn học', 'nghiên cứu'],
        'cycle_length': 3, # 3 năm 1 cung
        'type': 'chu_tuong'
    },
    # 3. Chủ Đại Tướng (Thay cho Chiêu Dao cũ)
    3: {
        'name': 'Chủ Đại Tướng',
        'han': '主大将',
        'nature': 'cat',
        'score': 9,
        'meaning': 'Đại tướng quân, quyền uy quân sự phe Chủ',
        'fields': ['quân sự', 'chiến lược', 'quyền lực'],
        'cycle_length': 3,
        'type': 'chu_tuong'
    },
    # 4. Chủ Tham Tướng (Thay cho Hiên Dư cũ)
    4: {
        'name': 'Chủ Tham Tướng',
        'han': '主参将',
        'nature': 'trung',
        'score': 6,
        'meaning': 'Tham mưu, hỗ trợ phe Chủ',
        'fields': ['tham mưu', 'kế hoạch', 'hậu cần'],
        'cycle_length': 3,
        'type': 'chu_tuong'
    },
    
    # 5. Khách Đại Tướng (Thay Thiên Phù)
    5: {
        'name': 'Khách Đại Tướng',
        'han': '客大将',
        'nature': 'hung',
        'score': -5,
        'meaning': 'Đại tướng phe Khách, đối đầu',
        'fields': ['đối thủ', 'cạnh tranh', 'xâm lấn'],
        'cycle_length': 3,
        'type': 'khach_tuong'
    },
    # 6. Khách Tham Tướng (Thay Thanh Long)
    6: {
        'name': 'Khách Tham Tướng',
        'han': '客参将',
        'nature': 'hung',
        'score': -3,
        'meaning': 'Tham mưu phe Khách',
        'fields': ['mưu kế', 'gián điệp', 'phá hoại'],
        'cycle_length': 3,
        'type': 'khach_tuong'
    },
    
    # CÁC SAO ĐỊNH CÁT HUNG
    # 7. Ngũ Phúc (Thay Tiểu Cát) - Chu kỳ 45 (Theo bài viết Ref)
    # Ref: "Thời gian An cung của sao Ngũ Phúc là 45 năm" -> Chia tích tuế cho 225, rút theo 45
    7: {
        'name': 'Ngũ Phúc',
        'han': '五福',
        'nature': 'dai_cat',
        'score': 15,
        'meaning': 'Hiền, Đức, An, Khang, Thọ. Đại cát tinh',
        'fields': ['phúc đức', 'bình an', 'thọ'],
        'cycle_length': 45, # 45 năm 1 cung (vòng 225 năm)
        'type': 'cat_hung'
    },
    # 8. Quân Cơ (Thay Tùng Khuê) - Chu kỳ thường là 1 (như Thái Ất)
    8: {
        'name': 'Quân Cơ',
        'han': '君基',
        'nature': 'cat',
        'score': 10,
        'meaning': 'Nền tảng vua chúa, gốc rễ',
        'fields': ['nền tảng', 'gốc rễ', 'ổn định'],
        'cycle_length': 1,
        'type': 'cat_hung'
    },
    # 9. Thần Cơ (Thay Thắng Quang)
    9: {
        'name': 'Thần Cơ',
        'han': '臣基',
        'nature': 'cat',
        'score': 8,
        'meaning': 'Nền tảng quan lại, bộ máy',
        'fields': ['quan chức', 'công vụ', 'hành chính'],
        'cycle_length': 1,
        'type': 'cat_hung'
    },
    # 10. Dân Cơ (Thay Thái Xung)
    10: {
        'name': 'Dân Cơ',
        'han': '民基',
        'nature': 'trung',
        'score': 5,
        'meaning': 'Nền tảng dân chúng',
        'fields': ['dân sinh', 'xã hội', 'đám đông'],
        'cycle_length': 1,
        'type': 'cat_hung'
    },
    
    # 11. Thủy Kích (Thay Thiên Cương)
    11: {
        'name': 'Thủy Kích',
        'han': '水击',
        'nature': 'dai_hung',
        'score': -10,
        'meaning': 'Tai họa, binh đao, sóng thần, chết chóc',
        'fields': ['tai họa', 'chiến tranh', 'thiên tai'],
        'cycle_length': 1, # Thường đi nghịch
        'type': 'cat_hung'
    },
    # 12. Đại Du (Thay Thái Ất Phó) - Chu kỳ 36
    12: {
        'name': 'Đại Du',
        'han': '大游',
        'nature': 'hung',
        'score': -5,
        'meaning': 'Di chuyển lớn, biến động mạnh',
        'fields': ['di cư', 'biến động', 'lang thang'],
        'cycle_length': 36,
        'type': 'cat_hung'
    },
    # 13. Tiểu Du (Thay Thắng Tiên)
    13: {
        'name': 'Tiểu Du',
        'han': '小游',
        'nature': 'trung',
        'score': -2,
        'meaning': 'Di chuyển nhỏ, thay đổi nhỏ',
        'fields': ['du lịch', 'thay đổi', 'dịch chuyển'],
        'cycle_length': 24, # Vòng 24
        'type': 'cat_hung'
    },
    # 14. Tứ Thần (Thay Tiểu Cát Phó)
    14: {
        'name': 'Tứ Thần',
        'han': '四神',
        'nature': 'hung',
        'score': -8,
        'meaning': 'Hung thần, sát khí bốn phương',
        'fields': ['sát khí', 'hung hiểm', 'đe dọa'],
        'cycle_length': 3,
        'type': 'cat_hung'
    },
    # 15. Thiên Ất (Thay Thái Ất Tam)
    15: {
        'name': 'Thiên Ất',
        'han': '天乙',
        'nature': 'cat',
        'score': 12,
        'meaning': 'Quý nhân phù trợ, thần may mắn',
        'fields': ['quý nhân', 'may mắn', 'hóa giải'],
        'cycle_length': 1,
        'type': 'cat_hung'
    },
    # 16. Địa Ất (Thay Cửu Thiên)
    16: {
        'name': 'Địa Ất',
        'han': '地乙',
        'nature': 'cat',
        'score': 10,
        'meaning': 'Thần đất đai, thổ địa, bền vững',
        'fields': ['đất đai', 'bất động sản', 'nông nghiệp'],
        'cycle_length': 1,
        'type': 'cat_hung'
    }
}


# =============================================
# NGŨ NGUYÊN (5 Nguyên - chu kỳ 360 năm)
# =============================================

NGU_NGUYEN = {
    0: {
        'name': 'Giáp Tý Nguyên',
        'han': '甲子元',
        'can_chi': 'Giáp Tý',
        'start_year': 1984,  # Base year
        'end_year': 2055,
        'nature': 'Mộc',
        'description': 'Nguyên khởi đầu, sinh sôi phát triển'
    },
    1: {
        'name': 'Giáp Tuất Nguyên',
        'han': '甲戌元',
        'can_chi': 'Giáp Tuất',
        'start_year': 2056,
        'end_year': 2127,
        'nature': 'Thổ',
        'description': 'Nguyên ổn định, tích lũy'
    },
    2: {
        'name': 'Giáp Thân Nguyên',
        'han': '甲申元',
        'can_chi': 'Giáp Thân',
        'start_year': 2128,
        'end_year': 2199,
        'nature': 'Kim',
        'description': 'Nguyên thu hoạch, đoán định'
    },
    3: {
        'name': 'Giáp Ngọ Nguyên',
        'han': '甲午元',
        'can_chi': 'Giáp Ngọ',
        'start_year': 2200,
        'end_year': 2271,
        'nature': 'Hỏa',
        'description': 'Nguyên cực thịnh, hoàng kim'
    },
    4: {
        'name': 'Giáp Thìn Nguyên',
        'han': '甲辰元',
        'can_chi': 'Giáp Thìn',
        'start_year': 2272,
        'end_year': 2343,
        'nature': 'Thổ',
        'description': 'Nguyên chuyển tiếp, tái sinh'
    }
}


# =============================================
# HỘI (12 Hội trong 1 Nguyên = 72 năm)
# =============================================

def get_hoi_info(hoi_index: int) -> dict:
    """
    Lấy thông tin Hội (1 Hội = 6 năm)
    
    Args:
        hoi_index: 0-11
        
    Returns:
        Dict với name, years, nature
    """
    THAP_NHI_HOI = [
        {'name': 'Tý Hội', 'nature': 'Thủy', 'direction': 'Bắc'},
        {'name': 'Sửu Hội', 'nature': 'Thổ', 'direction': 'Đông Bắc'},
        {'name': 'Dần Hội', 'nature': 'Mộc', 'direction': 'Đông'},
        {'name': 'Mão Hội', 'nature': 'Mộc', 'direction': 'Đông'},
        {'name': 'Thìn Hội', 'nature': 'Thổ', 'direction': 'Đông Nam'},
        {'name': 'Tỵ Hội', 'nature': 'Hỏa', 'direction': 'Nam'},
        {'name': 'Ngọ Hội', 'nature': 'Hỏa', 'direction': 'Nam'},
        {'name': 'Mùi Hội', 'nature': 'Thổ', 'direction': 'Tây Nam'},
        {'name': 'Thân Hội', 'nature': 'Kim', 'direction': 'Tây'},
        {'name': 'Dậu Hội', 'nature': 'Kim', 'direction': 'Tây'},
        {'name': 'Tuất Hội', 'nature': 'Thổ', 'direction': 'Tây Bắc'},
        {'name': 'Hợi Hội', 'nature': 'Thủy', 'direction': 'Bắc'},
    ]
    return THAP_NHI_HOI[hoi_index % 12]


# =============================================
# CỬU CUNG THÁI ẤT
# =============================================

CUU_CUNG_THAI_AT = {
    1: {'name': 'Thái Ất Cung', 'han': '太乙宮', 'nature': 'Thủy'},
    2: {'name': 'Thiên Mục Cung', 'han': '天目宮', 'nature': 'Thổ'},
    3: {'name': 'Thiên Đình Cung', 'han': '天庭宮', 'nature': 'Mộc'},
    4: {'name': 'Thiên Lý Cung', 'han': '天理宮', 'nature': 'Mộc'},
    5: {'name': 'Trung Cung', 'han': '中宮', 'nature': 'Thổ'},
    6: {'name': 'Thiên Cao Cung', 'han': '天高宮', 'nature': 'Kim'},
    7: {'name': 'Thiên Quan Cung', 'han': '天關宮', 'nature': 'Kim'},
    8: {'name': 'Thiên Anh Cung', 'han': '天英宮', 'nature': 'Thổ'},
    9: {'name': 'Thiên Phủ Cung', 'han': '天府宮', 'nature': 'Hỏa'},
}


# =============================================
# NGŨ HÀNH 16 THẦN - Sách Thái Ất mục 24
# =============================================
# Phi Phù, Thủy Kích = Hỏa
# Chủ Đại Tướng, Thiên Ất = Kim
# Văn Xương, Kể Thần, Địa Mục, Cơ (Quân/Thần/Dân), Phúc (Ngũ Phúc) = Thổ
# Tiểu Du, Khách Tham Tướng = Mộc
# Chủ Tham Tướng, Khách Đại Tướng, Tứ Thần = Thủy

THAP_LUC_THAN_NGU_HANH = {
    'Thái Ất':         'Thổ',    # Phi Phù danh xưng khác
    'Văn Xương':       'Thổ',
    'Chủ Đại Tướng':   'Kim',
    'Chủ Tham Tướng':  'Thủy',
    'Khách Đại Tướng': 'Thủy',
    'Khách Tham Tướng':'Mộc',
    'Ngũ Phúc':        'Thổ',
    'Quân Cơ':         'Thổ',
    'Thần Cơ':         'Thổ',
    'Dân Cơ':          'Thổ',
    'Thủy Kích':       'Hỏa',
    'Đại Du':          'Hỏa',    # Phi Phù loại
    'Tiểu Du':         'Mộc',
    'Tứ Thần':         'Thủy',
    'Thiên Ất':        'Kim',
    'Địa Ất':          'Thổ',
    'Kể Thần':         'Thổ',
    'Trực Phù':        'Thổ',
}


# =============================================
# THẬP CAN HÓA KHÍ - Sách Thái Ất mục 25
# =============================================
# Mỗi cặp Thiên Can hóa thành 1 hành, mỗi hạn 10 năm
# Dùng để luận Thái Ất Vận Hạn
#
# Đinh Nhâm hóa Mộc (hành_số 3, Hợi)
# Giáp Kỷ  hóa Thổ (hành_số 5, Ngọ)
# Bính Tân hóa Thủy (hành_số 1, Thân)
# Mậu Quý  hóa Hỏa (hành_số 2, Dần)
# Ất Canh  hóa Kim  (hành_số 4, Tỵ)

THAP_CAN_HOA_KHI = {
    ('Đinh', 'Nhâm'): {'hanh': 'Mộc', 'hanh_so': 3, 'dia_chi': 'Hợi', 'han': 10},
    ('Giáp', 'Kỷ'):   {'hanh': 'Thổ', 'hanh_so': 5, 'dia_chi': 'Ngọ', 'han': 10},
    ('Bính', 'Tân'):   {'hanh': 'Thủy', 'hanh_so': 1, 'dia_chi': 'Thân', 'han': 10},
    ('Mậu', 'Quý'):    {'hanh': 'Hỏa', 'hanh_so': 2, 'dia_chi': 'Dần', 'han': 10},
    ('Ất', 'Canh'):     {'hanh': 'Kim', 'hanh_so': 4, 'dia_chi': 'Tỵ', 'han': 10},
}

# Lookup nhanh: Can → Hóa Khí
THIEN_CAN_HOA_KHI_LOOKUP = {
    'Giáp': 'Thổ', 'Kỷ': 'Thổ',
    'Ất': 'Kim',    'Canh': 'Kim',
    'Bính': 'Thủy', 'Tân': 'Thủy',
    'Đinh': 'Mộc',  'Nhâm': 'Mộc',
    'Mậu': 'Hỏa',   'Quý': 'Hỏa',
}
