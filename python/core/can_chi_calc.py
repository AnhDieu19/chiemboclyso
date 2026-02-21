"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         CAN CHI CALCULATIONS                                  ║
║                         Tính toán Can Chi                                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Purpose: Calculate Thiên Can (Heavenly Stems) and Địa Chi (Earthly Branches)║
║           for Year, Month, Day, and Hour                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

HỆ THỐNG CAN CHI:
=================
- 10 Thiên Can: Giáp(0), Ất(1), Bính(2), Đinh(3), Mậu(4), 
                Kỷ(5), Canh(6), Tân(7), Nhâm(8), Quý(9)
- 12 Địa Chi:   Tý(0), Sửu(1), Dần(2), Mão(3), Thìn(4), Tỵ(5),
                Ngọ(6), Mùi(7), Thân(8), Dậu(9), Tuất(10), Hợi(11)
- Chu kỳ 60 năm (Can x Chi = 10 x 12 / GCD(10,12) = 60)

CÔNG THỨC TÍNH:
===============
1. NĂM: Can = (năm + 6) % 10, Chi = (năm + 8) % 12
2. THÁNG: Chi = tháng + 1 (tháng 1 = Dần), Can theo bảng tra năm Can
3. NGÀY: Dùng Julius Day, Can = (JD + 9) % 10, Chi = (JD + 1) % 12
4. GIỜ: Chi = giờ/2, Can = (Can ngày * 2 + Chi giờ) % 10
"""

from data import THIEN_CAN, DIA_CHI


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH CAN CHI NĂM
# Công thức: Can = (năm + 6) % 10, Chi = (năm + 8) % 12
# ═══════════════════════════════════════════════════════════════════════════════

def get_year_can_chi(lunar_year: int) -> dict:
    """
    Tính Can Chi của năm Âm lịch
    
    CÔNG THỨC:
    - Can năm = (năm + 6) mod 10
      + Năm 1984 (Giáp Tý): (1984 + 6) % 10 = 0 → Giáp
    - Chi năm = (năm + 8) mod 12
      + Năm 1984 (Giáp Tý): (1984 + 8) % 12 = 0 → Tý
    
    LÝ DO CÔNG THỨC:
    - Năm Giáp Tý = năm 4 trong chu kỳ 60
    - 1984 là năm Giáp Tý → dùng làm mốc
    - Offset +6 và +8 điều chỉnh để khớp với index 0
    
    Args:
        lunar_year: Năm Âm lịch
        
    Returns:
        dict chứa can_index, chi_index, can, chi, full
        
    Ví dụ:
        1994 → Can = (1994+6)%10 = 0 (Giáp)
             → Chi = (1994+8)%12 = 10 (Tuất)
             → Giáp Tuất
    """
    # Tính index của Thiên Can (0-9)
    can_index = (lunar_year + 6) % 10
    
    # Tính index của Địa Chi (0-11)
    chi_index = (lunar_year + 8) % 12
    
    return {
        'can_index': can_index,
        'chi_index': chi_index,
        'can': THIEN_CAN[can_index],
        'chi': DIA_CHI[chi_index],
        'full': f"{THIEN_CAN[can_index]} {DIA_CHI[chi_index]}"
    }


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH CAN CHI THÁNG
# Chi tháng: Tháng 1 = Dần (2), Tháng 2 = Mão (3)...
# Can tháng: Tra bảng theo Can năm
# ═══════════════════════════════════════════════════════════════════════════════

def get_month_can_chi(lunar_month: int, lunar_year: int) -> dict:
    """
    Tính Can Chi của tháng Âm lịch
    
    CÔNG THỨC CHI THÁNG:
    - Chi tháng = (tháng + 1) % 12
    - Tháng 1 Âm lịch luôn là tháng Dần (index 2)
    - Tháng 2 = Mão (3), Tháng 3 = Thìn (4)... 
    
    CÔNG THỨC CAN THÁNG (Ngũ Hổ Độn):
    ┌─────────────┬─────────────────────────────┐
    │ Can Năm     │ Can tháng 1 (Dần)           │
    ├─────────────┼─────────────────────────────┤
    │ Giáp / Kỷ   │ Bính Dần (Can index 2)      │
    │ Ất / Canh   │ Mậu Dần  (Can index 4)      │
    │ Bính / Tân  │ Canh Dần (Can index 6)      │
    │ Đinh / Nhâm │ Nhâm Dần (Can index 8)      │
    │ Mậu / Quý   │ Giáp Dần (Can index 0)      │
    └─────────────┴─────────────────────────────┘
    
    Args:
        lunar_month: Tháng Âm lịch (1-12)
        lunar_year: Năm Âm lịch
        
    Returns:
        dict chứa can_index, chi_index, can, chi, full
    """
    year_can_chi = get_year_can_chi(lunar_year)
    year_can = year_can_chi['can_index']
    
    # Chi tháng: Tháng 1 = Dần (2), Tháng 2 = Mão (3)...
    # Công thức: (tháng + 1) % 12
    chi_index = (lunar_month + 1) % 12
    
    # Can tháng: Tra bảng Ngũ Hổ Độn
    # Mảng chứa Can khởi đầu của tháng 1 (Dần) theo Can năm
    # Index: [Giáp, Ất, Bính, Đinh, Mậu, Kỷ, Canh, Tân, Nhâm, Quý]
    # Value: Can của tháng 1 (Dần)
    start_can = [2, 4, 6, 8, 0, 2, 4, 6, 8, 0]  # Bính, Mậu, Canh, Nhâm, Giáp (lặp lại)
    
    # Can tháng = Can khởi đầu + (tháng - 1)
    can_index = (start_can[year_can] + lunar_month - 1) % 10
    
    return {
        'can_index': can_index,
        'chi_index': chi_index,
        'can': THIEN_CAN[can_index],
        'chi': DIA_CHI[chi_index],
        'full': f"{THIEN_CAN[can_index]} {DIA_CHI[chi_index]}"
    }


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH CAN CHI NGÀY
# Dùng Julius Day Number để tính
# Công thức: Can = (JD + 9) % 10, Chi = (JD + 1) % 12
# ═══════════════════════════════════════════════════════════════════════════════

def get_day_can_chi(day: int, month: int, year: int) -> dict:
    """
    Tính Can Chi của ngày (dùng ngày Dương lịch)
    
    CÔNG THỨC:
    1. Tính Julius Day Number (JD) của ngày Dương lịch
    2. Can ngày = (JD + 9) mod 10
    3. Chi ngày = (JD + 1) mod 12
    
    LÝ DO OFFSET:
    - Ngày 1/1/4713 BC (JD = 0) là ngày Giáp Tý
    - Offset +9 và +1 điều chỉnh để khớp calendar hiện đại
    
    Args:
        day: Ngày Dương lịch (1-31)
        month: Tháng Dương lịch (1-12)
        year: Năm Dương lịch
        
    Returns:
        dict chứa can_index, chi_index, can, chi, full
    
    Ví dụ:
        28/3/1994 → JD = 2449439
        Can = (2449439 + 9) % 10 = 8 (Nhâm... cần verify)
    """
    # Bước 1: Tính Julius Day Number
    # Điều chỉnh năm nếu tháng 1 hoặc 2
    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3
    
    # Công thức Gregorian JD
    jd = day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    
    # Bước 2: Tính Can và Chi
    can_index = (jd + 9) % 10
    chi_index = (jd + 1) % 12
    
    return {
        'can_index': can_index,
        'chi_index': chi_index,
        'can': THIEN_CAN[can_index],
        'chi': DIA_CHI[chi_index],
        'full': f"{THIEN_CAN[can_index]} {DIA_CHI[chi_index]}"
    }


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH CAN CHI GIỜ
# Chi giờ: Theo 12 canh (Tý 23-01h, Sửu 01-03h...)
# Can giờ: Theo công thức Ngũ Thử Độn
# ═══════════════════════════════════════════════════════════════════════════════

def get_hour_can_chi(hour_index: int, day: int, month: int, year: int) -> dict:
    """
    Tính Can Chi của giờ sinh
    
    CHI GIỜ (12 canh):
    ┌────────┬───────────┬────────────┐
    │ Index  │ Chi       │ Giờ        │
    ├────────┼───────────┼────────────┤
    │ 0      │ Tý        │ 23 - 01h   │
    │ 1      │ Sửu       │ 01 - 03h   │
    │ 2      │ Dần       │ 03 - 05h   │
    │ 3      │ Mão       │ 05 - 07h   │
    │ 4      │ Thìn      │ 07 - 09h   │
    │ 5      │ Tỵ        │ 09 - 11h   │
    │ 6      │ Ngọ       │ 11 - 13h   │
    │ 7      │ Mùi       │ 13 - 15h   │
    │ 8      │ Thân      │ 15 - 17h   │
    │ 9      │ Dậu       │ 17 - 19h   │
    │ 10     │ Tuất      │ 19 - 21h   │
    │ 11     │ Hợi       │ 21 - 23h   │
    └────────┴───────────┴────────────┘
    
    CAN GIỜ (Ngũ Thử Độn):
    Công thức: Can giờ = (Can ngày * 2 + Chi giờ) mod 10
    
    ┌─────────────┬─────────────────────────────┐
    │ Can Ngày    │ Can giờ Tý (23-01h)         │
    ├─────────────┼─────────────────────────────┤
    │ Giáp / Kỷ   │ Giáp Tý (Can index 0)       │
    │ Ất / Canh   │ Bính Tý (Can index 2)       │
    │ Bính / Tân  │ Mậu Tý  (Can index 4)       │
    │ Đinh / Nhâm │ Canh Tý (Can index 6)       │
    │ Mậu / Quý   │ Nhâm Tý (Can index 8)       │
    └─────────────┴─────────────────────────────┘
    
    Args:
        hour_index: Index giờ Chi (0-11), 0=Tý, 3=Mão...
        day, month, year: Ngày Dương lịch (để tính Can ngày)
        
    Returns:
        dict chứa can_index, chi_index, can, chi, full
    """
    # Lấy Can của ngày
    day_can_chi = get_day_can_chi(day, month, year)
    day_can = day_can_chi['can_index']
    
    # Tính Can giờ theo công thức Ngũ Thử Độn
    # Can giờ = (Can ngày * 2 + Chi giờ) mod 10
    hour_can = (day_can * 2 + hour_index) % 10
    
    return {
        'can_index': hour_can,
        'chi_index': hour_index,  # Chi giờ = index được truyền vào
        'can': THIEN_CAN[hour_can],
        'chi': DIA_CHI[hour_index],
        'full': f"{THIEN_CAN[hour_can]} {DIA_CHI[hour_index]}"
    }


# ═══════════════════════════════════════════════════════════════════════════════
# CHUYỂN ĐỔI GIỜ 24H SANG CHI INDEX
# ═══════════════════════════════════════════════════════════════════════════════

def hour_to_chi_index(hour: int) -> int:
    """
    Chuyển đổi giờ 24h sang index Chi (0-11)
    
    BẢNG CHUYỂN ĐỔI:
    - 23h hoặc 0h  → 0 (Tý)
    - 1-2h         → 1 (Sửu)
    - 3-4h         → 2 (Dần)
    - 5-6h         → 3 (Mão)
    - 7-8h         → 4 (Thìn)
    - 9-10h        → 5 (Tỵ)
    - 11-12h       → 6 (Ngọ)
    - 13-14h       → 7 (Mùi)
    - 15-16h       → 8 (Thân)
    - 17-18h       → 9 (Dậu)
    - 19-20h       → 10 (Tuất)
    - 21-22h       → 11 (Hợi)
    
    Công thức: (hour + 1) // 2
    
    LƯU Ý: Hàm này chỉ được dùng khi nhận hour ở dạng 24h.
           Frontend hiện tại gửi hour_index trực tiếp (0-11).
    
    Args:
        hour: Giờ dạng 24h (0-23)
        
    Returns:
        Index Chi (0-11)
    """
    # Xử lý đặc biệt cho giờ Tý (23h và 0h)
    if hour == 23 or hour == 0:
        return 0  # Tý
    
    # Công thức chung: mỗi Chi = 2 giờ
    return (hour + 1) // 2


# ═══════════════════════════════════════════════════════════════════════════════
# XỬ LÝ GIỜ TÝ ĐẦU (BR-03)
# Giờ Tý đầu (23h-0h) thuộc ngày hôm TRƯỚC theo Nam Phái
# ═══════════════════════════════════════════════════════════════════════════════

def is_early_ty_hour(hour: int) -> bool:
    """
    Kiểm tra có phải giờ Tý đầu (23h-0h) không
    
    BR-03: Giờ Tý đầu thuộc ngày hôm trước
    - Giờ Tý đầu: 23:00 - 00:00 (thuộc ngày hôm trước)
    - Giờ Tý muộn: 00:00 - 01:00 (thuộc ngày hôm sau)
    
    LƯU Ý: Trong Tử Vi có 2 cách tính:
    1. Chính Tý (全子時): Cả 23h-1h đều thuộc ngày hôm sau
    2. Dạ Tý (夜子時): 23h-0h thuộc ngày hôm trước, 0h-1h thuộc ngày hôm sau
    
    Theo BA yêu cầu BR-03, chúng ta dùng cách Dạ Tý.
    
    Args:
        hour: Giờ dạng 24h (0-23)
        
    Returns:
        True nếu là giờ Tý đầu (23h)
    """
    return hour == 23


def adjust_date_for_early_ty(day: int, month: int, year: int, hour: int) -> tuple:
    """
    Điều chỉnh ngày nếu sinh vào giờ Tý đầu (23h)
    
    Theo BR-03: Giờ Tý đầu thuộc ngày hôm trước
    Nếu sinh lúc 23:30 ngày 15/3/1994, thì:
    - Ngày để tính Can Chi ngày = 14/3/1994
    - Giờ vẫn là Tý
    
    Args:
        day, month, year: Ngày tháng năm Dương lịch
        hour: Giờ 24h (0-23), chỉ xử lý khi hour=23
        
    Returns:
        tuple (day, month, year) đã điều chỉnh
    """
    if not is_early_ty_hour(hour):
        return (day, month, year)
    
    # Giờ Tý đầu (23h) thuộc ngày hôm trước
    # Lùi ngày lại 1
    from datetime import date, timedelta
    original_date = date(year, month, day)
    adjusted_date = original_date - timedelta(days=1)
    
    return (adjusted_date.day, adjusted_date.month, adjusted_date.year)