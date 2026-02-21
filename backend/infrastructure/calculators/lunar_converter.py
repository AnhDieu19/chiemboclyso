"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LUNAR CALENDAR CONVERTER                                   ║
║                    Chuyển đổi Âm Dương Lịch                                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Based on: Hồ Ngọc Đức's algorithm (http://www.informatik.uni-leipzig.de)    ║
║  Purpose: Convert Gregorian (Solar) date to Vietnamese Lunar date            ║
╚══════════════════════════════════════════════════════════════════════════════╝

THUẬT TOÁN CHUYỂN ĐỔI ÂM DƯƠNG LỊCH:
=====================================
1. Tính Julius Day Number (JD) từ ngày Dương lịch
2. Tính điểm Sóc (New Moon) gần nhất
3. Xác định tháng 11 Âm lịch (tháng chứa Đông Chí)
4. Tính số tháng từ tháng 11 đến tháng hiện tại
5. Kiểm tra và xử lý tháng nhuận
6. Trả về ngày/tháng/năm Âm lịch

CÔNG THỨC CHÍNH:
================
- JD = dd + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045
- New Moon: JD = 2415020.75933 + 29.53058868*k + corrections
- Tháng Âm lịch ≈ 29.530588853 ngày (chu kỳ Sóc)
"""

import math

# ═══════════════════════════════════════════════════════════════════════════════
# HẰNG SỐ / CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

PI = math.pi

# Julius Day của ngày 15/10/1582 (ngày chuyển từ Julian sang Gregorian calendar)
JULIUS_DAY_OFFSET = 2299161

# Múi giờ Việt Nam (GMT+7)
TZ = 7


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH JULIUS DAY NUMBER
# Công thức: JD = dd + (153*m + 2)//5 + 365*y + y//4 - y//100 + y//400 - 32045
# ═══════════════════════════════════════════════════════════════════════════════

def jd_from_date(dd: int, mm: int, yy: int) -> int:
    """
    Tính Julius Day Number từ ngày Dương lịch (Gregorian)
    
    Công thức:
    - a = (14 - tháng) / 12  → điều chỉnh năm nếu tháng 1,2
    - y = năm + 4800 - a     → cộng 4800 để tránh số âm
    - m = tháng + 12*a - 3   → chuyển tháng bắt đầu từ tháng 3
    - JD = ngày + (153*m + 2)/5 + 365*y + y/4 - y/100 + y/400 - 32045
    
    Args:
        dd: Ngày (1-31)
        mm: Tháng (1-12)
        yy: Năm
        
    Returns:
        Julius Day Number (số ngày từ 1/1/4713 BC)
    """
    # Bước 1: Điều chỉnh năm nếu là tháng 1 hoặc 2
    # (vì trong công thức, năm bắt đầu từ tháng 3)
    a = (14 - mm) // 12
    
    # Bước 2: Cộng 4800 vào năm để tránh số âm trong tính toán
    y = yy + 4800 - a
    
    # Bước 3: Chuyển đổi tháng (bắt đầu từ tháng 3 = 0)
    m = mm + 12 * a - 3
    
    # Bước 4: Tính Julius Day theo công thức Gregorian
    # - 365*y: số ngày trong y năm
    # - y//4 - y//100 + y//400: điều chỉnh năm nhuận
    # - (153*m + 2)//5: số ngày tích lũy của các tháng trước
    # - 32045: hằng số điều chỉnh
    jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    
    # Bước 5: Nếu trước ngày 15/10/1582, dùng lịch Julian (không có y//100 và y//400)
    if jd < JULIUS_DAY_OFFSET:
        jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - 32083
    
    return jd


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH ĐIỂM SÓC (NEW MOON)
# Điểm Sóc là thời điểm Mặt Trăng ở giữa Trái Đất và Mặt Trời
# ═══════════════════════════════════════════════════════════════════════════════

def new_moon(k: int) -> float:
    """
    Tính thời điểm Trăng mới (Sóc) thứ k tính từ ngày 6/1/2000
    
    Công thức Jean Meeus (Astronomical Algorithms):
    - T = k / 1236.85 (số thế kỷ Julian từ năm 2000)
    - JD cơ sở = 2415020.75933 + 29.53058868*k
    - Cộng các hiệu chỉnh dựa trên:
      + M: Mean Anomaly của Mặt Trời
      + M': Mean Anomaly của Mặt Trăng
      + F: Argument of Latitude của Mặt Trăng
    
    Args:
        k: Số thứ tự của Trăng mới (k=0 tại 6/1/2000)
        
    Returns:
        Julian Day của điểm Sóc
    """
    # Tính số thế kỷ Julian từ J2000.0
    T = k / 1236.85
    T2 = T * T
    T3 = T2 * T
    dr = PI / 180  # Chuyển độ sang radian
    
    # Bước 1: Tính JD cơ sở của Trăng mới
    # 2415020.75933 là JD của Trăng mới gốc (6/1/1900)
    # 29.53058868 là chu kỳ Sóc trung bình (ngày)
    Jd1 = 2415020.75933 + 29.53058868 * k + 0.0001178 * T2 - 0.000000155 * T3
    
    # Hiệu chỉnh thêm dựa trên công thức thiên văn
    Jd1 = Jd1 + 0.00033 * math.sin((166.56 + 132.87 * T - 0.009173 * T2) * dr)
    
    # Bước 2: Tính các góc thiên văn
    # M: Mean Anomaly của Mặt Trời (vị trí góc của Mặt Trời)
    M = 359.2242 + 29.10535608 * k - 0.0000333 * T2 - 0.00000347 * T3
    
    # M': Mean Anomaly của Mặt Trăng (vị trí góc của Mặt Trăng)
    Mpr = 306.0253 + 385.81691806 * k + 0.0107306 * T2 + 0.00001236 * T3
    
    # F: Argument of Latitude (khoảng cách góc từ node)
    F = 21.2964 + 390.67050646 * k - 0.0016528 * T2 - 0.00000239 * T3
    
    # Bước 3: Tính hiệu chỉnh C1 (dựa trên vị trí Mặt Trời và Mặt Trăng)
    C1 = (0.1734 - 0.000393 * T) * math.sin(M * dr) + 0.0021 * math.sin(2 * dr * M)
    C1 = C1 - 0.4068 * math.sin(Mpr * dr) + 0.0161 * math.sin(dr * 2 * Mpr)
    C1 = C1 - 0.0004 * math.sin(dr * 3 * Mpr)
    C1 = C1 + 0.0104 * math.sin(dr * 2 * F) - 0.0051 * math.sin(dr * (M + Mpr))
    C1 = C1 - 0.0074 * math.sin(dr * (M - Mpr)) + 0.0004 * math.sin(dr * (2 * F + M))
    C1 = C1 - 0.0004 * math.sin(dr * (2 * F - M)) - 0.0006 * math.sin(dr * (2 * F + Mpr))
    C1 = C1 + 0.0010 * math.sin(dr * (2 * F - Mpr)) + 0.0005 * math.sin(dr * (2 * Mpr + M))
    
    # Bước 4: Hiệu chỉnh Delta-T (sự khác biệt giữa giờ thiên văn và giờ dân dụng)
    if T < -11:
        deltat = 0.001 + 0.000839 * T + 0.0002261 * T2 - 0.00000845 * T3 - 0.000000081 * T * T3
    else:
        deltat = -0.000278 + 0.000265 * T + 0.000262 * T2
    
    # Trả về JD của Trăng mới = JD cơ sở + hiệu chỉnh - delta-T
    return Jd1 + C1 - deltat


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH HOÀNG KINH MẶT TRỜI (SUN LONGITUDE)
# Hoàng kinh xác định vị trí Mặt Trời trên hoàng đạo
# ═══════════════════════════════════════════════════════════════════════════════

def sun_longitude(jdn: float) -> float:
    """
    Tính Hoàng kinh Mặt Trời tại thời điểm JD cho trước
    
    Hoàng kinh (Ecliptic Longitude) là góc của Mặt Trời trên hoàng đạo,
    tính từ điểm Xuân Phân (0°). Mỗi năm Mặt Trời đi qua 360°.
    
    Công thức VSOP87 đơn giản hóa:
    - L0: Mean longitude
    - M: Mean anomaly  
    - DL: Equation of center (hiệu chỉnh)
    - L = L0 + DL
    
    Args:
        jdn: Julius Day Number
        
    Returns:
        Hoàng kinh Mặt Trời (radian)
    """
    # Số thế kỷ Julian từ J2000.0 (1/1/2000 12:00 TT)
    T = (jdn - 2451545.0) / 36525
    T2 = T * T
    dr = PI / 180
    
    # Mean Anomaly của Mặt Trời (độ)
    M = 357.52910 + 35999.05030 * T - 0.0001559 * T2 - 0.00000048 * T * T2
    
    # Mean Longitude của Mặt Trời (độ)
    L0 = 280.46645 + 36000.76983 * T + 0.0003032 * T2
    
    # Equation of Center - hiệu chỉnh do quỹ đạo elip
    DL = (1.914600 - 0.004817 * T - 0.000014 * T2) * math.sin(dr * M)
    DL = DL + (0.019993 - 0.000101 * T) * math.sin(dr * 2 * M) + 0.000290 * math.sin(dr * 3 * M)
    
    # True Longitude = Mean + Equation of Center
    L = L0 + DL
    L = L * dr  # Chuyển sang radian
    
    # Chuẩn hóa về khoảng [0, 2π]
    L = L - PI * 2 * (L // (PI * 2))
    
    return L


def get_sun_longitude(day_number: float, time_zone: int) -> int:
    """
    Lấy Hoàng kinh Mặt Trời dạng số nguyên (0-11)
    
    Chia hoàng đạo thành 12 cung, mỗi cung 30°:
    - 0: Xuân Phân (0-30°)
    - 3: Hạ Chí (90-120°)
    - 6: Thu Phân (180-210°)
    - 9: Đông Chí (270-300°)
    
    Args:
        day_number: Julius Day Number
        time_zone: Múi giờ
        
    Returns:
        Số cung (0-11), mỗi cung = 30°
    """
    # Điều chỉnh về nửa đêm địa phương (-0.5 ngày) và múi giờ
    return int(sun_longitude(day_number - 0.5 - time_zone / 24) / PI * 6)


# ═══════════════════════════════════════════════════════════════════════════════
# XÁC ĐỊNH THÁNG 11 ÂM LỊCH
# Tháng 11 là tháng chứa điểm Đông Chí (Hoàng kinh = 270°)
# ═══════════════════════════════════════════════════════════════════════════════

def get_lunar_month_11(yy: int, time_zone: int) -> tuple:
    """
    Tìm tháng 11 Âm lịch của năm Dương lịch
    
    Tháng 11 Âm lịch là tháng CHỨA điểm Đông Chí (Hoàng kinh = 270° = cung 9).
    Đây là tháng cố định dùng làm mốc tính các tháng khác.
    
    Args:
        yy: Năm Dương lịch
        time_zone: Múi giờ
        
    Returns:
        Tuple (JD của Sóc tháng 11, Hoàng kinh tại Sóc)
    """
    # Tính số ngày từ mốc đến 31/12 năm yy
    off = jd_from_date(31, 12, yy) - 2415021
    
    # Ước tính số Trăng mới từ mốc
    k = int(off / 29.530588853)
    
    # Tìm Trăng mới gần nhất
    nm = new_moon(k)
    
    # Kiểm tra Hoàng kinh tại Sóc
    sun_long = get_sun_longitude(nm, time_zone)
    
    # Nếu Hoàng kinh >= 9 (Đông Chí), lùi lại 1 tháng
    # (vì tháng 11 phải CHỨA Đông Chí, không phải bắt đầu sau Đông Chí)
    if sun_long >= 9:
        nm = new_moon(k - 1)
    
    return (nm, get_sun_longitude(nm, time_zone))


# ═══════════════════════════════════════════════════════════════════════════════
# XÁC ĐỊNH THÁNG NHUẬN
# Tháng nhuận xảy ra khi có 13 Sóc trong khoảng từ tháng 11 năm trước đến tháng 11 năm sau
# ═══════════════════════════════════════════════════════════════════════════════

def get_leap_month_offset(a11: float, time_zone: int) -> int:
    """
    Tìm vị trí tháng nhuận (offset từ tháng 11)
    
    Quy tắc:
    - Năm có 13 tháng thì có 1 tháng nhuận
    - Tháng nhuận là tháng đầu tiên không chứa Trung Khí
    - Trung Khí: Đông Chí, Đại Hàn, Vũ Thủy... (mỗi 30° Hoàng kinh)
    
    Args:
        a11: JD của Sóc tháng 11 năm trước
        time_zone: Múi giờ
        
    Returns:
        Số tháng từ tháng 11 đến tháng nhuận
    """
    k = int((a11 - 2415021.076998695) / 29.530588853 + 0.5)
    last = 0
    i = 1
    
    # Duyệt qua các Sóc, tìm tháng đầu tiên có cùng Hoàng kinh với tháng trước
    # (tức là không chứa Trung Khí mới)
    arc = get_sun_longitude(new_moon(k + i), time_zone)
    while arc != last and i < 14:
        last = arc
        i += 1
        arc = get_sun_longitude(new_moon(k + i), time_zone)
    
    return i - 1


# ═══════════════════════════════════════════════════════════════════════════════
# HÀM CHÍNH: CHUYỂN ĐỔI DƯƠNG LỊCH → ÂM LỊCH
# ═══════════════════════════════════════════════════════════════════════════════

def solar_to_lunar(dd: int, mm: int, yy: int, tz: float = 7.0) -> dict:
    """
    Chuyển đổi ngày Dương lịch sang Âm lịch
    
    QUY TRÌNH:
    1. Tính Julius Day của ngày Dương lịch
    2. Tìm Sóc (Trăng mới) của tháng chứa ngày đó
    3. Tìm tháng 11 Âm lịch của năm trước và năm sau
    4. Tính số tháng từ tháng 11 đến tháng hiện tại
    5. Kiểm tra và xử lý tháng nhuận
    6. Tính ngày Âm lịch = Julius Day - Sóc + 1
    
    Args:
        dd: Ngày Dương lịch (1-31)
        mm: Tháng Dương lịch (1-12)
        yy: Năm Dương lịch
        tz: Múi giờ (mặc định 7 cho Việt Nam)
        
    Returns:
        dict với các key:
        - day: Ngày Âm lịch (1-30)
        - month: Tháng Âm lịch (1-12)
        - year: Năm Âm lịch
        - leap: True nếu là tháng nhuận
    """
    time_zone = int(tz)
    
    # Bước 1: Tính Julius Day của ngày Dương lịch
    day_number = jd_from_date(dd, mm, yy)
    
    # Bước 2: Ước tính số Sóc từ mốc và tìm Sóc của tháng hiện tại
    k = int((day_number - 2415021.076998695) / 29.530588853)
    month_start = new_moon(k + 1)  # Sóc tiếp theo
    
    # Nếu Sóc tiếp theo > ngày hiện tại, lùi lại 1 tháng
    if month_start > day_number:
        month_start = new_moon(k)
    
    # Bước 3: Tìm tháng 11 Âm lịch của năm chứa Sóc
    a11 = get_lunar_month_11(yy, time_zone)[0]  # Tháng 11 năm yy
    b11 = a11
    
    # Xác định năm Âm lịch
    if a11 >= month_start:
        # Sóc nằm trước tháng 11 năm yy → năm Âm lịch = yy
        lunar_year = yy
        a11 = get_lunar_month_11(yy - 1, time_zone)[0]  # Lấy tháng 11 năm trước
    else:
        # Sóc nằm sau tháng 11 năm yy → năm Âm lịch = yy + 1
        lunar_year = yy + 1
        b11 = get_lunar_month_11(yy + 1, time_zone)[0]  # Lấy tháng 11 năm sau
    
    # Bước 4: Tính ngày Âm lịch
    lunar_day = int(day_number - month_start + 1)
    
    # Bước 5: Tính số tháng từ tháng 11 năm trước đến tháng hiện tại
    diff = int((month_start - a11) / 29)  # Mỗi tháng ≈ 29.5 ngày
    lunar_leap = False
    lunar_month = diff + 11  # Tháng 11 là tháng 0 trong diff
    
    # Bước 6: Kiểm tra năm có tháng nhuận không
    # (nếu từ tháng 11 năm trước đến tháng 11 năm sau > 365 ngày → có 13 tháng)
    if b11 - a11 > 365:
        leap_month_diff = get_leap_month_offset(a11, time_zone)
        if diff >= leap_month_diff:
            lunar_month = diff + 10  # Trừ 1 vì có tháng nhuận
            if diff == leap_month_diff:
                lunar_leap = True  # Đây là tháng nhuận
    
    # Bước 7: Chuẩn hóa tháng về 1-12
    if lunar_month > 12:
        lunar_month = lunar_month - 12
        
    # Điều chỉnh năm nếu tháng >= 11 nhưng diff < 4 (thuộc năm trước)
    if lunar_month >= 11 and diff < 4:
        lunar_year -= 1
    
    return {
        'day': lunar_day,      # Ngày Âm lịch
        'month': lunar_month,  # Tháng Âm lịch (1-12)
        'year': lunar_year,    # Năm Âm lịch
        'leap': lunar_leap     # True nếu tháng nhuận
    }
