"""
Stars Layer - Trường Sinh Cycle (12 stars) Placer
"""






def place_truong_sinh(year_can_index: int, gender: str, cuc_number: int) -> dict:
    """
    Place Trường Sinh cycle (12 stars)
    Direction: Dương Nam/Âm Nữ go forward, Âm Nam/Dương Nữ go backward
    Base logic:
    - Kim(4) -> Tỵ(5)
    - Mộc(3) -> Hợi(11)
    - Thủy(2)/Thổ(5) -> Thân(8)
    - Hỏa(6) -> Dần(2)
    """
    stars = {}
    
    is_duong_nam = (year_can_index % 2 == 0) and (gender == 'nam')
    is_am_nu = (year_can_index % 2 == 1) and (gender == 'nu')
    go_forward = is_duong_nam or is_am_nu
    
    # Map Cục Number -> Base Position
    # Thủy(2)->8, Mộc(3)->11, Kim(4)->5, Thổ(5)->8, Hỏa(6)->2
    BASE_MAP = {
        2: 8,  # Thân
        3: 11, # Hợi
        4: 5,  # Tỵ
        5: 8,  # Thân (Thủy Thổ đồng hành)
        6: 2   # Dần
    }
    
    truong_sinh_base = BASE_MAP.get(cuc_number, 8)
    
    TRUONG_SINH_STARS = [
        "Trường Sinh", "Mộc Dục", "Quan Đới", "Lâm Quan", "Đế Vượng", "Suy", 
        "Bệnh", "Tử", "Mộ", "Tuyệt", "Thai", "Dưỡng"
    ]
    
    for i, star_name in enumerate(TRUONG_SINH_STARS):
        if go_forward:
            pos = (truong_sinh_base + i) % 12
        else:
            pos = (truong_sinh_base - i + 12) % 12
        stars[star_name] = pos
    
    return stars
