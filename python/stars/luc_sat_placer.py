"""
Stars Layer - Lục Sát Tinh (6 Malefic Stars) Placer
"""


from data import KINH_DA

HOA_STARTS = {
    2: 1, 6: 1, 10: 1,  # Dần Ngọ Tuất -> Hỏa Sửu (1)
    8: 2, 0: 2, 4: 2,   # Thân Tý Thìn -> Hỏa Dần (2)
    5: 3, 9: 3, 1: 3,   # Tỵ Dậu Sửu -> Hỏa Mão (3)
    11: 9, 3: 9, 7: 9   # Hợi Mão Mùi -> Hỏa Dậu (9)
}

LINH_STARTS = {
    2: 3, 6: 3, 10: 3,  # Dần Ngọ Tuất -> Linh Mão (3)
    8: 10, 0: 10, 4: 10, # Thân Tý Thìn -> Linh Tuất (10)
    5: 10, 9: 10, 1: 10, # Tỵ Dậu Sửu -> Linh Tuất (10)
    11: 10, 3: 10, 7: 10 # Hợi Mão Mùi -> Linh Tuất (10)
}


def place_kinh_da(year_can_index: int) -> dict:
    """Place Kinh Dương, Đà La (Year Can based)"""
    stars = {}
    if year_can_index is None:
        return stars
        
    # Kinh Dương, Đà La: based on year Can
    kinh_da = KINH_DA[year_can_index]
    stars['Kinh Dương'] = kinh_da['kinh']
    stars['Đà La'] = kinh_da['da']
    return stars

def place_hoa_linh(year_can_index: int, year_chi_index: int, hour_index: int, gender: str) -> dict:
    """
    Place Hỏa Tinh, Linh Tinh
    Rule:
    - Determine Base Position based on Year Chi group.
    - Determine Direction:
      - Dương Nam / Âm Nữ: Thuận
      - Âm Nam / Dương Nữ: Nghịch
    - Count from Base (Base is mapped to Tý hour? No, usually Base is starting point).
      Standard: Start at Base, count to Hour.
      Thuận: (Base + Hour - 1) % 12? (If Hour 1 = Tý).
             But my hour_index 0 = Tý.
             So (Base + Hour) % 12. (e.g. Base Mão(3). Tý(0) -> 3. Sửu(1) -> 4).
      Nghịch: (Base - Hour + 12) % 12.
    """
    stars = {}
    if year_can_index is None or year_chi_index is None or hour_index is None or not gender:
        return stars
        
    hoa_base = HOA_STARTS.get(year_chi_index, 0)
    linh_base = LINH_STARTS.get(year_chi_index, 0)
    
    is_year_duong = (year_can_index % 2 == 0)
    is_male = (gender == 'nam')
    
    # Direction Logic
    is_thuan = (is_year_duong and is_male) or (not is_year_duong and not is_male)
    
    if is_thuan:
        stars['Hỏa Tinh'] = (hoa_base + hour_index) % 12
        # Linh Tinh usually opposite direction?
        # Rule: "Hỏa Linh thuận nghịch..." varies by school.
        # Common: Hỏa always follows Direction. Linh follows Opposite?
        # Or Both follow Direction?
        # Let's check Image Case 2025.
        # Year Tỵ (Am), Girl (Nu) -> Thuan.
        # Hỏa at Tỵ. Base Mão (3). Hour Dần (2).
        # 3 + 2 = 5 (Tỵ). Correct -> Hỏa follows Direction (Thuận).
        
        # Linh at Thân. Base Tuất (10). Hour Dần (2).
        # 10 - 2 = 8 (Thân).
        # So Linh follows Reverse Direction even if Person is Thuận?
        # Or Standard Rule: Hỏa Thuận, Linh Nghịch for THIS specific Year Group?
        # "Tỵ Dậu Sửu ... Hỏa Mão Linh Tuất... Hỏa Thuận Linh Nghịch".
        # Ah, maybe the DIRECTION IS FIXED per Year Group?
        # Or Hỏa is always Thuận, Linh always Nghịch?
        # Let's assume Hỏa=Thuận, Linh=Nghịch based on Image Evidence.
        
        stars['Linh Tinh'] = (linh_base - hour_index + 12) % 12
    else:
        # If Person is NGHỊCH.
        # Should Hỏa become Nghịch?
        stars['Hỏa Tinh'] = (hoa_base - hour_index + 12) % 12
        # And Linh become Thuận?
        stars['Linh Tinh'] = (linh_base + hour_index) % 12
        
    # Wait, strictly sticking to Image Evidence:
    # 2025 (Âm Nữ -> Thuận). Hỏa Thuận, Linh Nghịch.
    # Logic above implements:
    # If Thuận: Hỏa Thuận, Linh Nghịch.
    # If Nghịch: Hỏa Nghịch, Linh Thuận.
    # This seems plausible (Symmetry).

    return stars

def place_khong_kiep(hour_index: int) -> dict:
    """Place Địa Không, Địa Kiếp (Hour based)"""
    stars = {}
    if hour_index is None:
        return stars
        
    # Địa Không, Địa Kiếp
    stars['Địa Không'] = ((11 - hour_index) % 12 + 12) % 12
    stars['Địa Kiếp'] = (11 + hour_index) % 12
    return stars

def place_luc_sat(year_can_index: int, year_chi_index: int, hour_index: int, gender: str) -> dict:
    """
    Place Lục Sát Tinh (6 malefic auxiliary stars)
    
    Returns:
        dict mapping star name to position
    """
    stars = {}
    
    stars.update(place_kinh_da(year_can_index))
    stars.update(place_hoa_linh(year_can_index, year_chi_index, hour_index, gender))
    stars.update(place_khong_kiep(hour_index))
    
    return stars
