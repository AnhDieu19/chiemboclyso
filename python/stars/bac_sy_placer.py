"""
Stars Layer - Bác Sĩ Ring (12 stars) and Lộc Tồn Placer
Reference: CALCULATION_GUIDE.md (Section 7.4 - Vòng Bác Sĩ)
"""

from data import LOC_TON_POSITION, BAC_SY_STARS


def place_bac_sy_ring(year_can_index: int, gender: str) -> dict:
    """
    Place Lộc Tồn and Bác Sĩ ring (12 stars).
    Direction:
    - Dương Nam / Âm Nữ: Thuận (Forward)
    - Âm Nam / Dương Nữ: Nghịch (Backward)
    
    Args:
        year_can_index: 0=Giáp (Dương), 1=Ất (Âm)...
        gender: 'Nam' or 'Nữ'
    """
    stars = {}
    
    loc_ton_pos = LOC_TON_POSITION[year_can_index]
    stars['Lộc Tồn'] = loc_ton_pos
    
    # Determine direction
    is_yang_can = (year_can_index % 2 == 0) # 0, 2, 4... -> Dương
    is_male = (gender.title() == 'Nam') # Default normalize
    
    # Dương Nam or Âm Nữ -> Thuận
    is_forward = (is_yang_can and is_male) or (not is_yang_can and not is_male)
    
    # Bác Sĩ vòng
    for i, star_name in enumerate(BAC_SY_STARS):
        if is_forward:
            stars[star_name] = (loc_ton_pos + i) % 12
        else:
            stars[star_name] = (loc_ton_pos - i + 12) % 12
    
    return stars
