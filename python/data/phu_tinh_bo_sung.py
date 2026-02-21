"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    PHỤ TINH BỔ SUNG - ĐỂ ĐẠT >= 114 SAO                      ║
║              Long Trì, Phượng Các, Thiên Riêu, Thiên Không...               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Bổ sung các sao còn thiếu theo truyền thống Nam Phái                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════════════════════
# LONG TRÌ - PHƯỢNG CÁC
# Long Trì: Sao tốt, hỗ trợ văn chương, thi cử
# Phượng Các: Sao tốt, hỗ trợ nghệ thuật, tài hoa
# Theo Địa Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

LONG_TRI_PHUONG_CAC = {
    # Chi năm: (Long Trì, Phượng Các)
    # Long Trì: Khởi Thìn thuận
    # Phượng Các: Khởi Tuất nghịch
    0: (4, 10),   # Tý: Thìn, Tuất
    1: (5, 9),    # Sửu: Tỵ, Dậu
    2: (6, 8),    # Dần: Ngọ, Thân
    3: (7, 7),    # Mão: Mùi, Mùi
    4: (8, 6),    # Thìn: Thân, Ngọ
    5: (9, 5),    # Tỵ: Dậu, Tỵ
    6: (10, 4),   # Ngọ: Tuất, Thìn
    7: (11, 3),   # Mùi: Hợi, Mão
    8: (0, 2),    # Thân: Tý, Dần
    9: (1, 1),    # Dậu: Sửu, Sửu
    10: (2, 0),   # Tuất: Dần, Tý
    11: (3, 11),  # Hợi: Mão, Hợi
}

# ═══════════════════════════════════════════════════════════════════════════════
# THIÊN RIÊU
# Sao đào hoa, chủ về sắc dục, tình ái không chính đáng
# Theo Địa Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

THIEN_RIEU_POSITION = {
    # Chi năm: vị trí Thiên Riêu
    # Tứ Mộ (Thìn Tuất Sửu Mùi) → Dậu, Mão, Tý, Ngọ
    0: 9,   # Tý → Dậu
    1: 6,   # Sửu → Ngọ
    2: 3,   # Dần → Mão
    3: 0,   # Mão → Tý
    4: 9,   # Thìn → Dậu
    5: 6,   # Tỵ → Ngọ
    6: 3,   # Ngọ → Mão
    7: 0,   # Mùi → Tý
    8: 9,   # Thân → Dậu
    9: 6,   # Dậu → Ngọ
    10: 3,  # Tuất → Mão
    11: 0,  # Hợi → Tý
}

# ═══════════════════════════════════════════════════════════════════════════════
# HÀM TRÌ (ĐÀO HOA)
# ═══════════════════════════════════════════════════════════════════════════════

HAM_TRI_POSITION = {
    # Thân Tý Thìn -> Dậu (9)
    0: 9, 4: 9, 8: 9,
    # Dần Ngọ Tuất -> Mão (3)
    2: 3, 6: 3, 10: 3,
    # Tỵ Dậu Sửu -> Ngọ (6)
    1: 6, 5: 6, 9: 6,
    # Hợi Mão Mùi -> Tý (0)
    3: 0, 7: 0, 11: 0,
}

# ═══════════════════════════════════════════════════════════════════════════════
# THIÊN KHÔNG
# Sao Thiên Không trong vòng Thái Tuế
# Luôn đi cùng Thiếu Dương, trước Thái Tuế 1 cung
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_thien_khong(year_chi_index: int) -> int:
    """
    Tính vị trí Thiên Không (Vòng Thái Tuế)
    Luôn ở cung sau Thái Tuế (Thái Tuế + 1)
    """
    return (year_chi_index + 1) % 12

# ═══════════════════════════════════════════════════════════════════════════════
# ĐẨU QUÂN
# Sao chủ về mưu lược, quân sự
# Theo giờ + tháng
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_dau_quan(lunar_month: int, hour_index: int) -> int:
    """
    Tính vị trí Đẩu Quân
    Tháng 1 tại Dần, thuận đến tháng sinh, nghịch đến giờ sinh
    """
    start_month = (2 + lunar_month - 1) % 12
    return (start_month - hour_index + 12) % 12





# ═══════════════════════════════════════════════════════════════════════════════
# MỆNH CHỦ
# Sao chủ của Cung Mệnh, xác định dựa trên Địa Chi của CUNG MỆNH (không phải Chi năm sinh)
# ═══════════════════════════════════════════════════════════════════════════════

MENH_CHU_TABLE = {
    # Index Địa Chi cung Mệnh: Tên sao Mệnh Chủ
    0: "Tham Lang",     # Tý → Tham Lang
    1: "Cự Môn",        # Sửu → Cự Môn
    2: "Lộc Tồn",       # Dần → Lộc Tồn
    3: "Văn Khúc",      # Mão → Văn Khúc
    4: "Liêm Trinh",    # Thìn → Liêm Trinh
    5: "Vũ Khúc",       # Tỵ → Vũ Khúc
    6: "Phá Quân",      # Ngọ → Phá Quân
    7: "Vũ Khúc",       # Mùi → Vũ Khúc
    8: "Liêm Trinh",    # Thân → Liêm Trinh
    9: "Văn Khúc",      # Dậu → Văn Khúc
    10: "Lộc Tồn",      # Tuất → Lộc Tồn
    11: "Cự Môn",       # Hợi → Cự Môn
}

# ═══════════════════════════════════════════════════════════════════════════════
# THÂN CHỦ
# Sao chủ của Cung Thân, xác định dựa trên Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

THAN_CHU_TABLE = {
    # Index Chi năm: Tên sao Thân Chủ
    0: "Linh Tinh",     # Tý → Linh Tinh
    1: "Thiên Tướng",   # Sửu → Thiên Tướng
    2: "Thiên Lương",   # Dần → Thiên Lương
    3: "Thiên Đồng",    # Mão → Thiên Đồng
    4: "Văn Xương",     # Thìn → Văn Xương
    5: "Thiên Cơ",      # Tỵ → Thiên Cơ
    6: "Hỏa Tinh",      # Ngọ → Hỏa Tinh
    7: "Thiên Tướng",   # Mùi → Thiên Tướng
    8: "Thiên Lương",   # Thân → Thiên Lương
    9: "Thiên Đồng",    # Dậu → Thiên Đồng
    10: "Văn Xương",    # Tuất → Văn Xương
    11: "Thiên Cơ",     # Hợi → Thiên Cơ
}



# ═══════════════════════════════════════════════════════════════════════════════
# TẤT CẢ CÁC SAO BỔ SUNG (TỔNG HỢP)
# ═══════════════════════════════════════════════════════════════════════════════

def place_bo_sung_stars(year_chi_index: int, hour_index: int, 
                        lunar_month: int, menh_position: int,
                        than_position: int) -> dict:
    """
    An tất cả các sao bổ sung để đạt >= 114 sao
    
    Returns:
        dict mapping star name to position
    """
    stars = {}
    
    # Long Trì, Phượng Các
    long_phuong = LONG_TRI_PHUONG_CAC.get(year_chi_index, (4, 10))
    stars['Long Trì'] = long_phuong[0]
    stars['Phượng Các'] = long_phuong[1]
    
    # Giải Thần: Luôn đồng cung với Phượng Các
    stars['Giải Thần'] = stars['Phượng Các']
    
    # Thiên Diêu (Theo tháng: Tháng 1 Sửu, mỗi tháng tiến 1 cung)
    stars['Thiên Diêu'] = (1 + lunar_month - 1) % 12
    
    # Thiên Không
    stars['Thiên Không'] = calculate_thien_khong(year_chi_index)
    
    # Đẩu Quân
    stars['Đẩu Quân'] = calculate_dau_quan(lunar_month, hour_index)
    
    # Hàm Trì
    stars['Hàm Trì'] = HAM_TRI_POSITION.get(year_chi_index, 3)
    
    # Thiên Thường (Nô Bộc), Thiên Sứ (Tật Ách)
    stars['Thiên Thường'] = (menh_position + 5) % 12
    stars['Thiên Sứ'] = (menh_position + 7) % 12
    
    # Thiên Tài: Cung Mệnh + Chi năm
    stars['Thiên Tài'] = (menh_position + year_chi_index) % 12
    
    # Thiên Thọ: Cung Thân + Chi năm
    stars['Thiên Thọ'] = (than_position + year_chi_index) % 12
    
    return stars



def get_menh_chu(menh_position: int) -> str:
    """Lấy tên sao Mệnh Chủ dựa trên Địa Chi của Cung Mệnh (không phải Chi năm sinh)"""
    return MENH_CHU_TABLE.get(menh_position, "Tham Lang")



def get_than_chu(year_chi_index: int) -> str:
    """Lấy tên sao Thân Chủ dựa trên Chi năm sinh"""
    return THAN_CHU_TABLE.get(year_chi_index, "Linh Tinh")


