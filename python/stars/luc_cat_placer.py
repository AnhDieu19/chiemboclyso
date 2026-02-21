"""
Stars Layer - Lục Cát Tinh (6 Auspicious Stars) Placer
"""

from data import TA_PHU_BASE, HUU_BAT_BASE, VAN_XUONG_BASE, VAN_KHUC_BASE, THIEN_KHOI_VIET


def place_ta_huu(lunar_month: int) -> dict:
    """Place Tả Phụ, Hữu Bật (Month based)"""
    stars = {}
    if not lunar_month:
        return stars
        
    # Tả Phụ: from Thìn, count forward by (month - 1)
    stars['Tả Phụ'] = (TA_PHU_BASE + lunar_month - 1) % 12
    
    # Hữu Bật: from Tuất, count backward by (month - 1)
    stars['Hữu Bật'] = ((HUU_BAT_BASE - (lunar_month - 1)) % 12 + 12) % 12
    return stars

def place_xuong_khuc(hour_index: int) -> dict:
    """Place Văn Xương, Văn Khúc (Hour based)"""
    stars = {}
    if hour_index is None:
        return stars
        
    # Văn Xương: from Tuất, count backward by hour
    stars['Văn Xương'] = ((VAN_XUONG_BASE - hour_index) % 12 + 12) % 12
    
    # Văn Khúc: from Thìn, count forward by hour
    stars['Văn Khúc'] = (VAN_KHUC_BASE + hour_index) % 12
    return stars

def place_khoi_viet(year_can_index: int) -> dict:
    """Place Thiên Khôi, Thiên Việt (Year Can based)"""
    stars = {}
    if year_can_index is None:
        return stars
        
    # Thiên Khôi, Thiên Việt: based on year Can
    khoi_viet = THIEN_KHOI_VIET[year_can_index]
    stars['Thiên Khôi'] = khoi_viet['khoi']
    stars['Thiên Việt'] = khoi_viet['viet']
    return stars

def place_luc_cat(year_can_index: int, lunar_month: int, hour_index: int) -> dict:
    """
    Place Lục Cát Tinh (6 auspicious auxiliary stars)
    
    Returns:
        dict mapping star name to position
    """
    stars = {}
    
    stars.update(place_ta_huu(lunar_month))
    stars.update(place_xuong_khuc(hour_index))
    stars.update(place_khoi_viet(year_can_index))
    
    return stars
