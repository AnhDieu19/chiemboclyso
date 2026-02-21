"""
Stars Layer - Thái Tuế Ring (12 stars) Placer
"""

from data import THAI_TUE_STARS, TUE_STARS


def place_thai_tue_ring(year_chi_index: int) -> dict:
    """
    Place Thái Tuế ring (12 stars based on year Chi)
    
    Returns:
        dict mapping star name to position
    """
    stars = {}
    
    for i, star_name in enumerate(THAI_TUE_STARS):
        stars[star_name] = (year_chi_index + i) % 12
    
    # Also place Thiên Khốc, Thiên Hư from TUE_STARS
    tue = TUE_STARS[year_chi_index]
    stars['Thiên Khốc'] = tue['thien_khoc']
    stars['Thiên Hư'] = tue['thien_hu']
    
    return stars
