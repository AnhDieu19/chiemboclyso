"""
Stars Layer - Chính Tinh (14 Main Stars) Placer
"""

from data import CHINH_TINH, TU_VI_GROUP_OFFSET, THIEN_PHU_GROUP_OFFSET



def calculate_tuvi_position(cuc_number: int, lunar_day: int) -> int:
    """
    Calculate Tử Vi star position using Tử Vi Nam Phái algorithm
    
    Algorithm (from hocvienlyso.org):
    1. Find 'a' (0-5) such that (Day + a) % Cuc == 0
    2. b = (Day + a) / Cuc
    3. Start from Dần (index 2), count forward b steps (Dần=1, Mão=2, ...)
    4. Adjustment based on 'a':
       - If 'a' is ODD (1, 3, 5): Go BACKWARD 'a' steps
       - If 'a' is EVEN (0, 2, 4): Go FORWARD 'a' steps
    
    Example: Day 13, Mộc Tam Cục (3)
    - 13 % 3 = 1, so a = 3 - 1 = 2 (to make 13+2=15 divisible by 3)
    - b = 15 / 3 = 5
    - From Dần(2), count 5 steps: Dần→Mão→Thìn→Tỵ→Ngọ = position 6 (Ngọ)
    - a=2 is EVEN, so go FORWARD 2 steps: Ngọ→Mùi→Thân = position 8 (Thân) ✓
    """
    day = min(lunar_day, 30)
    cuc = cuc_number
    
    # 1. Find complement 'a' (0 to cuc-1) such that (day + a) is divisible by cuc
    remainder = day % cuc
    if remainder == 0:
        complement = 0
    else:
        complement = cuc - remainder
    
    # 2. Calculate quotient b
    effective_day = day + complement
    quotient = effective_day // cuc
    
    # 3. Start from Dần (index 2), count forward b steps
    # Dần is step 1, so position = 2 + (b - 1) = 1 + b
    dan_index = 2
    anchor_pos = (dan_index + quotient - 1) % 12
    
    # 4. Adjust based on whether 'a' is odd or even
    if complement % 2 == 1:  # ODD: go BACKWARD
        final_pos = (anchor_pos - complement + 12) % 12
    else:  # EVEN (including 0): go FORWARD
        final_pos = (anchor_pos + complement) % 12
    
    return final_pos



def calculate_thien_phu_position(tu_vi_position: int) -> int:
    """
    Calculate Thiên Phủ position based on Tử Vi position
    Algorithm: Symmetry across the Dần - Thân axis.
    Formula: (16 - Tử Vi Index) % 12 (assuming Tý = 0)
    """
    return (16 - tu_vi_position) % 12


def place_chinh_tinh(tu_vi_position: int) -> dict:
    """
    Place all 14 Chính Tinh on the chart
    
    Args:
        tu_vi_position: Địa Chi index of Tử Vi
        
    Returns:
        dict mapping star name to position
    """
    stars = {}
    
    # Place Tử Vi group (going counter-clockwise with gaps)
    tu_vi_group = CHINH_TINH['tu_vi_group']
    offsets = TU_VI_GROUP_OFFSET
    
    for i, star in enumerate(tu_vi_group):
        pos = (tu_vi_position + offsets[i] + 12) % 12
        stars[star] = pos
    
    # Calculate Thiên Phủ position
    thien_phu_position = calculate_thien_phu_position(tu_vi_position)
    
    # Place Thiên Phủ group (going clockwise)
    thien_phu_group = CHINH_TINH['thien_phu_group']
    thien_phu_offsets = THIEN_PHU_GROUP_OFFSET
    
    for i, star in enumerate(thien_phu_group):
        pos = (thien_phu_position + thien_phu_offsets[i]) % 12
        stars[star] = pos
    
    return stars
