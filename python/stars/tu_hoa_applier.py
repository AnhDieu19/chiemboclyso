"""
Stars Layer - Tứ Hóa (Four Transformations) Applier
Reference: CALCULATION_GUIDE.md (Section 8.1 - An Tứ Hóa)
"""

from data import TU_HOA_TABLE


def apply_tu_hoa(year_can_index: int, all_stars: dict) -> dict:
    """
    Apply Tứ Hóa transformations
    
    Args:
        year_can_index: Thiên Can index of birth year
        all_stars: dict of all star positions
        
    Returns:
        dict mapping transformation to {star, position}
    """
    tu_hoa = TU_HOA_TABLE[year_can_index]
    result = {}
    
    # Hóa Lộc
    if tu_hoa['loc'] in all_stars:
        result['Hóa Lộc'] = {'star': tu_hoa['loc'], 'position': all_stars[tu_hoa['loc']]}
    
    # Hóa Quyền
    if tu_hoa['quyen'] in all_stars:
        result['Hóa Quyền'] = {'star': tu_hoa['quyen'], 'position': all_stars[tu_hoa['quyen']]}
    
    # Hóa Khoa
    if tu_hoa['khoa'] in all_stars:
        result['Hóa Khoa'] = {'star': tu_hoa['khoa'], 'position': all_stars[tu_hoa['khoa']]}
    
    # Hóa Kỵ
    if tu_hoa['ky'] in all_stars:
        result['Hóa Kỵ'] = {'star': tu_hoa['ky'], 'position': all_stars[tu_hoa['ky']]}
    
    return result
