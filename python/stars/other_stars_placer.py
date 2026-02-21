"""
Stars Layer - Other Auxiliary Stars Placer
"""


from data import (
    THIEN_MA_POSITION, HONG_LOAN_THIEN_HY, DAO_HOA_POSITION, HOA_CAI_POSITION,
    LONG_NGUYET_DUC, THIEN_QUAN_PHUC, THIEN_THUONG_SU_BASE,
    THIEN_THO_TAI, THIEN_DIEU_POSITION,

    THIEN_LA_POSITION, DIA_VONG_POSITION, 
    THIEN_TRU_POSITION,
    TAM_THAI_BASE, BAT_TOA_BASE, LOC_TON_POSITION, calculate_dia_giai, LN_VAN_TINH
)


def place_year_other_stars(year_can_index: int, year_chi_index: int) -> dict:
    """Place Year-dependent other stars (Invariant)"""
    stars = {}
    
    # Thiên Mã
    stars['Thiên Mã'] = THIEN_MA_POSITION[year_chi_index]
    
    # Hồng Loan, Thiên Hỹ
    hong_hy = HONG_LOAN_THIEN_HY[year_chi_index]
    stars['Hồng Loan'] = hong_hy['hong_loan']
    stars['Thiên Hỹ'] = hong_hy['thien_hy']
    
    # Đào Hoa, Hoa Cái
    stars['Đào Hoa'] = DAO_HOA_POSITION[year_chi_index]
    stars['Hoa Cái'] = HOA_CAI_POSITION[year_chi_index]
    
    # Thiên Quan, Thiên Phúc
    quan_phuc = THIEN_QUAN_PHUC[year_can_index]
    stars['Thiên Quan'] = quan_phuc['quan']
    stars['Thiên Phúc'] = quan_phuc['phuc']
    
    # Thiên La, Địa Võng (cố định)
    stars['Thiên La'] = THIEN_LA_POSITION
    stars['Địa Võng'] = DIA_VONG_POSITION
    
    # LN.Văn Tinh
    stars['LN.Văn Tinh'] = LN_VAN_TINH[year_can_index]
    
    # Thiên Trù
    stars['Thiên Trù'] = THIEN_TRU_POSITION[year_can_index]
    
    return stars

def place_month_other_stars(lunar_month: int) -> dict:
    """Place Month-dependent other stars (Invariant)"""
    stars = {}
    if not lunar_month: 
        return stars
    month_key = min(max(lunar_month, 1), 12)
    
    # Long Đức, Nguyệt Đức (theo tháng)
    long_nguyet = LONG_NGUYET_DUC.get(month_key, {'long': 0, 'nguyet': 0})
    stars['L.Long Đức'] = long_nguyet['long']
    stars['L.Nguyệt Đức'] = long_nguyet['nguyet']
    
    # Thiên Hình (Theo tháng: Tháng 1 Dậu, mỗi tháng tiến 1 cung)
    stars['Thiên Hình'] = (9 + lunar_month - 1) % 12
    
    # Thiên Thọ, Thiên Tài (Logic bảng cũ - có thể sai so với Nam Phái chuẩn)
    # Đã bổ sung logic chuẩn ở place_bo_sung_stars (theo Mệnh/Thân)
    # Giữ lại nếu cần hoặc xóa đi để đồng nhất
    # Xóa đi để dùng logic chuẩn ở bo_sung_placer
    
    return stars

def place_hour_other_stars(hour_index: int) -> dict:
    """Place Hour-dependent other stars (Variant)"""
    stars = {}
    if hour_index is None:
        return stars
    
    # Thái Phụ: Khởi Ngọ, Thuận
    stars['Thái Phụ'] = (6 + hour_index) % 12
    
    # Phong Cáo: Khởi Dần, Thuận
    stars['Phong Cáo'] = (2 + hour_index) % 12
    
    # Thiên Diêu (moved to bo_sung_placer Month based)

    
    return stars

def place_quang_quy(lunar_day: int, xuong_pos: int, khuc_pos: int) -> dict:
    """
    An Ân Quang, Thiên Quý
    """
    stars = {}
    if not lunar_day or xuong_pos is None or khuc_pos is None:
        return stars
        
    stars['Ân Quang'] = (xuong_pos + lunar_day - 2) % 12
    stars['Thiên Quý'] = (khuc_pos - (lunar_day - 1) + 1) % 12
    
    return stars

def place_thai_toa(lunar_day: int, ta_pos: int, huu_pos: int) -> dict:
    """
    An Tam Thai, Bát Tọa
    """
    stars = {}
    if not lunar_day or ta_pos is None or huu_pos is None:
        return stars
        
    stars['Tam Thai'] = (ta_pos + lunar_day - 1) % 12
    stars['Bát Tọa'] = (huu_pos - (lunar_day - 1) + 12) % 12
    
    return stars

def place_loc_ton_based_stars(year_can_index: int) -> dict:
    """
    An Quốc Ấn, Đường Phù (theo Lộc Tồn)
    """
    stars = {}
    loc_ton_pos = LOC_TON_POSITION.get(year_can_index)
    if loc_ton_pos is None:
        return stars
        
    # Đường Phù: Lộc Tồn + 5 (cùng cung Tàu Thu)
    stars['Đường Phù'] = (loc_ton_pos + 5) % 12
    
    # Quốc Ấn: Lộc Tồn + 9 (Tam hơp voi Loc Ton + X -> xung chieu duong phu?)
    # Kinh Dương (Loc+1). 
    # Standard: Quốc Ấn = Lộc Tồn + 8.
    # Let's verify Image later. Used +8 for now.
    stars['Quốc Ấn'] = (loc_ton_pos + 8) % 12
    
    return stars

def place_other_stars(year_can_index: int, year_chi_index: int, lunar_month: int, 
                      hour_index: int, lunar_day: int,
                      ta_huu: dict = None, xuong_khuc: dict = None) -> dict:
    """
    Place all other auxiliary stars (Updated to accept Dependencies)
    """
    stars = {}
    ta_huu = ta_huu or {}
    xuong_khuc = xuong_khuc or {}
    
    stars.update(place_year_other_stars(year_can_index, year_chi_index))
    stars.update(place_month_other_stars(lunar_month))
    stars.update(place_hour_other_stars(hour_index))
    
    # Derived Stars
    stars.update(place_quang_quy(lunar_day, xuong_khuc.get('Văn Xương'), xuong_khuc.get('Văn Khúc')))
    stars.update(place_thai_toa(lunar_day, ta_huu.get('Tả Phụ'), ta_huu.get('Hữu Bật')))
    stars.update(place_loc_ton_based_stars(year_can_index))
    
    return stars


