"""
Stars Layer - Sao Bổ Sung Placer
An các sao bổ sung để đạt >= 114 sao
Reference: CALCULATION_GUIDE.md (Section 7.6 - Các Sao Đã Hiệu Chỉnh)
"""

from data import place_bo_sung_stars, get_menh_chu, get_than_chu

# ==============================================================================
# 1. BỘ TAM GIẢI (Thiên Giải, Địa Giải, Giải Thần)
# ==============================================================================

def an_bo_tam_giai(lunar_month: int, phuong_cac_index: int = None) -> dict:
    """
    An bộ Tam Giải: Thiên Giải, Địa Giải, Giải Thần
    
    Quy tắc:
    - Thiên Giải: Khởi Thân (8) là tháng 1, đếm nghịch đến tháng sinh.
    - Địa Giải: Khởi Mùi (7) là tháng 1, đếm thuận đến tháng sinh.
    - Giải Thần: Đồng cung Phượng Các.
    """
    stars = {}
    
    # 1. Thiên Giải: Khởi Thân (8), thuận theo tháng
    # Formula: 8 + (month - 1)
    stars['Thiên Giải'] = (8 + (lunar_month - 1)) % 12
    
    # 2. Địa Giải: Khởi Mùi (7), thuận theo tháng
    # Formula: 7 + (month - 1)
    stars['Địa Giải'] = (7 + (lunar_month - 1)) % 12
    
    # 3. Giải Thần: Đồng cung Phượng Các
    if phuong_cac_index is not None:
        stars['Giải Thần'] = phuong_cac_index
        
    return stars

# ==============================================================================
# 2. BỘ TỨ ĐỨC (Thiên Đức, Nguyệt Đức) - Long Đức, Phúc Đức đã có nơi khác
# ==============================================================================

# ==============================================================================
# 2. BỘ TỨ ĐỨC (Thiên Đức, Nguyệt Đức, Phúc Đức, Long Đức)
# ==============================================================================

def an_bo_tu_duc(lunar_month: int, year_chi_index: int = None, dao_hoa_idx: int = None) -> dict:
    """
    An Bộ Tứ Đức: Thiên Đức, Nguyệt Đức.
    
    Quy tắc chuẩn Nam Phái:
    - Thiên Đức: An theo Tháng sinh. Công thức: (tháng * 2 + 3) % 12
      Tháng 1→Tỵ(5), Tháng 2→Mùi(7), Tháng 3→Dậu(9), Tháng 4→Hợi(11),
      Tháng 5→Sửu(1), Tháng 6→Mão(3), chu kỳ 6 tháng.
    - Nguyệt Đức: An theo Tháng sinh tại vị trí Địa Chi của tháng.
      Công thức: (tháng + 1) % 12 (Chính Nguyệt khởi Dần)
      Tháng 1→Dần(2), Tháng 2→Mão(3), Tháng 3→Thìn(4), ...
    """
    stars = {}
    
    # 1. AN THIÊN ĐỨC (Theo Tháng sinh - chuẩn Nam Phái)
    # Công thức: (lunar_month * 2 + 3) % 12
    stars['Thiên Đức'] = (lunar_month * 2 + 3) % 12
        
    # 2. AN NGUYỆT ĐỨC (Theo Tháng sinh - vị trí Địa Chi tháng)
    # Chính nguyệt khởi Dần: Tháng 1 = Dần(2), Tháng 2 = Mão(3), ...
    stars['Nguyệt Đức'] = (lunar_month + 1) % 12
        
    return stars


def calculate_dao_hoa(year_chi_index: int) -> int:
    """Tính vị trí Đào Hoa dựa trên Chi Năm"""
    # Dần Ngọ Tuất -> Mão (3)
    if year_chi_index in [2, 6, 10]: return 3
    # Thân Tý Thìn -> Dậu (9)
    if year_chi_index in [8, 0, 4]: return 9
    # Tỵ Dậu Sửu -> Ngọ (6)
    if year_chi_index in [5, 9, 1]: return 6
    # Hợi Mão Mùi -> Tý (0)
    if year_chi_index in [11, 3, 7]: return 0
    return 0


def place_supplementary_stars(year_chi_index: int, hour_index: int, 
                               lunar_month: int, menh_position: int, 
                               than_position: int) -> dict:
    """
    An tất cả các sao bổ sung.
    Kết hợp logic cũ (data/phu_tinh_bo_sung) và logic mới (Tam Giải, Tứ Đức).
    """
    # 1. Logic cơ bản từ Data Layer (bao gồm Long Trì, Phượng Các, Đẩu Quân...)
    stars = place_bo_sung_stars(year_chi_index, hour_index, lunar_month, menh_position, than_position)
    
    # 2. Logic Tam Giải (Cần vị trí Phượng Các từ step 1)
    phuong_cac = stars.get('Phượng Các')
    stars_tam_giai = an_bo_tam_giai(lunar_month, phuong_cac)
    stars.update(stars_tam_giai)
    
    # 3. Logic Tứ Đức (Thiên Đức, Nguyệt Đức) chuẩn Nam Phái
    stars_tu_duc = an_bo_tu_duc(lunar_month, year_chi_index)
    stars.update(stars_tu_duc)
    
    return stars


def get_menh_than_chu(menh_position: int, year_chi_index: int) -> dict:
    """
    Lấy thông tin Mệnh Chủ và Thân Chủ
    - Mệnh Chủ: dựa trên Địa Chi của Cung Mệnh
    - Thân Chủ: dựa trên Địa Chi của Năm Sinh
    """
    return {
        'menh_chu': get_menh_chu(menh_position),
        'than_chu': get_than_chu(year_chi_index)
    }



