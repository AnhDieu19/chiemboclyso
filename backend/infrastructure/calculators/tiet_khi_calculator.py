"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    TIẾT KHÍ CALCULATOR (24 SOLAR TERMS)                      ║
║                    Tính toán 24 Tiết Khí Âm Dương                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Purpose: Calculate 24 solar terms for Thái Ất & Kì Môn systems             ║
║  Dependencies: lunar_converter.py (sun_longitude, jd_from_date)              ║
║  Output: Tiết Khí name, index (0-23), solar longitude                       ║
╚══════════════════════════════════════════════════════════════════════════════╝

24 TIẾT KHÍ (SOLAR TERMS):
===========================
Mỗi tiết khí = 15° trên hoàng đạo (360° / 24 = 15°)

Xuân (Spring):
  0. Lập Xuân 立春 (315°) - Start of Spring
  1. Vũ Thủy 雨水 (330°) - Rain Water
  2. Kinh Trập 驚蟄 (345°) - Awakening of Insects
  3. Xuân Phân 春分 (0°) - Spring Equinox
  4. Thanh Minh 清明 (15°) - Pure Brightness
  5. Cốc Vũ 穀雨 (30°) - Grain Rain

Hạ (Summer):
  6. Lập Hạ 立夏 (45°) - Start of Summer
  7. Tiểu Mãn 小滿 (60°) - Grain Buds
  8. Mang Chủng 芒種 (75°) - Grain in Ear
  9. Hạ Chí 夏至 (90°) - Summer Solstice
  10. Tiểu Thử 小暑 (105°) - Minor Heat
  11. Đại Thử 大暑 (120°) - Major Heat

Thu (Autumn):
  12. Lập Thu 立秋 (135°) - Start of Autumn
  13. Xử Thử 處暑 (150°) - End of Heat
  14. Bạch Lộ 白露 (165°) - White Dew
  15. Thu Phân 秋分 (180°) - Autumn Equinox
  16. Hàn Lộ 寒露 (195°) - Cold Dew
  17. Sương Giáng 霜降 (210°) - Descent of Frost

Đông (Winter):
  18. Lập Đông 立冬 (225°) - Start of Winter
  19. Tiểu Tuyết 小雪 (240°) - Minor Snow
  20. Đại Tuyết 大雪 (255°) - Major Snow
  21. Đông Chí 冬至 (270°) - Winter Solstice
  22. Tiểu Hàn 小寒 (285°) - Minor Cold
  23. Đại Hàn 大寒 (300°) - Major Cold

KÌ MÔN ÂM DƯƠNG ĐỘN:
=====================
- Đông Chí (21) → Hạ Chí (9): Dương Độn (Yang Escape)
- Hạ Chí (9) → Đông Chí (21): Âm Độn (Yin Escape)
"""

import math
from typing import Dict, Tuple
from core.lunar_converter import sun_longitude, jd_from_date

# ═══════════════════════════════════════════════════════════════════════════════
# HẰNG SỐ / CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

PI = math.pi

# 24 Tiết Khí (Vietnamese names)
TIET_KHI_NAMES = [
    "Lập Xuân",     # 0: 315° (Feb 4-5)
    "Vũ Thủy",      # 1: 330° (Feb 18-19)
    "Kinh Trập",    # 2: 345° (Mar 5-6)
    "Xuân Phân",    # 3: 0° (Mar 20-21)
    "Thanh Minh",   # 4: 15° (Apr 4-5)
    "Cốc Vũ",       # 5: 30° (Apr 19-20)
    "Lập Hạ",       # 6: 45° (May 5-6)
    "Tiểu Mãn",     # 7: 60° (May 20-21)
    "Mang Chủng",   # 8: 75° (Jun 5-6)
    "Hạ Chí",       # 9: 90° (Jun 21-22)
    "Tiểu Thử",     # 10: 105° (Jul 6-7)
    "Đại Thử",      # 11: 120° (Jul 22-23)
    "Lập Thu",      # 12: 135° (Aug 7-8)
    "Xử Thử",       # 13: 150° (Aug 22-23)
    "Bạch Lộ",      # 14: 165° (Sep 7-8)
    "Thu Phân",     # 15: 180° (Sep 22-23)
    "Hàn Lộ",       # 16: 195° (Oct 8-9)
    "Sương Giáng",  # 17: 210° (Oct 23-24)
    "Lập Đông",     # 18: 225° (Nov 7-8)
    "Tiểu Tuyết",   # 19: 240° (Nov 21-22)
    "Đại Tuyết",    # 20: 255° (Dec 6-7)
    "Đông Chí",     # 21: 270° (Dec 21-22)
    "Tiểu Hàn",     # 22: 285° (Jan 5-6)
    "Đại Hàn",      # 23: 300° (Jan 19-20)
]

# Chinese names (for reference/fallback)
TIET_KHI_CHINESE = [
    "立春", "雨水", "驚蟄", "春分", "清明", "穀雨",
    "立夏", "小滿", "芒種", "夏至", "小暑", "大暑",
    "立秋", "處暑", "白露", "秋分", "寒露", "霜降",
    "立冬", "小雪", "大雪", "冬至", "小寒", "大寒"
]

# Hoàng kinh tương ứng (độ)
TIET_KHI_LONGITUDES = [
    315, 330, 345, 0, 15, 30,      # Xuân
    45, 60, 75, 90, 105, 120,      # Hạ
    135, 150, 165, 180, 195, 210,  # Thu
    225, 240, 255, 270, 285, 300   # Đông
]

# Tiết Khí đặc biệt
DONG_CHI_INDEX = 21  # Đông Chí (Winter Solstice)
HA_CHI_INDEX = 9     # Hạ Chí (Summer Solstice)


# ═══════════════════════════════════════════════════════════════════════════════
# CORE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_tiet_khi(year: int, month: int, day: int, tz: int = 7) -> Dict:
    """
    Tính Tiết Khí cho một ngày cụ thể
    
    Thuật toán:
    1. Tính Julius Day Number từ ngày dương lịch
    2. Lấy hoàng kinh Mặt Trời (sun longitude) tại thời điểm đó
    3. Chia hoàng kinh thành 24 khoảng (mỗi khoảng 15°)
    4. Xác định Tiết Khí tương ứng
    
    Args:
        year: Năm dương lịch
        month: Tháng dương lịch (1-12)
        day: Ngày dương lịch (1-31)
        tz: Múi giờ (mặc định = 7 cho Việt Nam)
        
    Returns:
        {
            'index': int (0-23),
            'name': str (Tên tiết khí tiếng Việt),
            'chinese': str (Tên tiết khí Hán tự),
            'longitude': float (Hoàng kinh độ),
            'longitude_deg': int (Hoàng kinh tròn)
        }
    """
    # Tính JD
    jd = jd_from_date(day, month, year)
    
    # Điều chỉnh về nửa đêm địa phương
    jd_local = jd - 0.5 - tz / 24.0
    
    # Tính hoàng kinh Mặt Trời (radian)
    longitude_rad = sun_longitude(jd_local)
    
    # Chuyển sang độ (0-360°)
    longitude_deg = (longitude_rad * 180 / PI) % 360
    
    # Xác định tiết khí (mỗi tiết = 15°)
    # Lưu ý: Lập Xuân bắt đầu từ 315°, nên cần điều chỉnh
    # Công thức: index = ((longitude + 45) / 15) % 24
    tiet_khi_index = int((longitude_deg + 45) / 15) % 24
    
    return {
        'index': tiet_khi_index,
        'name': TIET_KHI_NAMES[tiet_khi_index],
        'chinese': TIET_KHI_CHINESE[tiet_khi_index],
        'longitude': longitude_rad,
        'longitude_deg': int(longitude_deg),
        'expected_longitude': TIET_KHI_LONGITUDES[tiet_khi_index]
    }


def is_between_dong_chi_and_ha_chi(tiet_khi_info: Dict) -> bool:
    """
    Kiểm tra xem Tiết Khí có nằm giữa Đông Chí và Hạ Chí không
    
    Dùng cho Kì Môn Độn Giáp:
    - Đông Chí → Hạ Chí: Dương Độn (Yang Escape)
    - Hạ Chí → Đông Chí: Âm Độn (Yin Escape)
    
    Args:
        tiet_khi_info: Dict từ calculate_tiet_khi()
        
    Returns:
        True nếu Dương Độn (từ Đông Chí đến Hạ Chí)
        False nếu Âm Độn (từ Hạ Chí đến Đông Chí)
    """
    index = tiet_khi_info['index']
    
    # Dương Độn: Đông Chí (21) → Tiểu Hàn (22) → Đại Hàn (23) → 
    #            Lập Xuân (0) → ... → Hạ Chí (9)
    # Điều kiện: index >= 21 hoặc index <= 9
    if index >= DONG_CHI_INDEX or index <= HA_CHI_INDEX:
        return True  # Dương Độn
    else:
        return False  # Âm Độn


def get_current_tiet_khi(tiet_khi_info: Dict) -> str:
    """
    Lấy tên Tiết Khí hiện tại (tiếng Việt)
    
    Args:
        tiet_khi_info: Dict từ calculate_tiet_khi()
        
    Returns:
        Tên Tiết Khí (str)
    """
    return tiet_khi_info['name']


def get_duong_am_don_status(tiet_khi_info: Dict) -> Dict:
    """
    Lấy trạng thái Dương Độn / Âm Độn
    
    Args:
        tiet_khi_info: Dict từ calculate_tiet_khi()
        
    Returns:
        {
            'is_duong_don': bool,
            'status': str ('Dương Độn' hoặc 'Âm Độn'),
            'description': str
        }
    """
    la_duong_don = is_between_dong_chi_and_ha_chi(tiet_khi_info)
    
    return {
        'is_duong_don': la_duong_don,
        'status': 'Dương Độn' if la_duong_don else 'Âm Độn',
        'description': (
            'Từ Đông Chí đến Hạ Chí - Dương khí tăng' if la_duong_don
            else 'Từ Hạ Chí đến Đông Chí - Âm khí tăng'
        )
    }


def get_season(tiet_khi_info: Dict) -> str:
    """
    Lấy mùa tương ứng với Tiết Khí
    
    Args:
        tiet_khi_info: Dict từ calculate_tiet_khi()
        
    Returns:
        'Xuân', 'Hạ', 'Thu', hoặc 'Đông'
    """
    index = tiet_khi_info['index']
    
    if 0 <= index <= 5:
        return 'Xuân'
    elif 6 <= index <= 11:
        return 'Hạ'
    elif 12 <= index <= 17:
        return 'Thu'
    else:  # 18-23
        return 'Đông'


def find_tiet_khi_date(year: int, tiet_khi_index: int, tz: int = 7) -> Tuple[int, int, int]:
    """
    Tìm ngày xảy ra Tiết Khí cụ thể trong năm
    
    Thuật toán:
    1. Ước lượng ngày gần đúng dựa vào tháng
    2. Quét ±5 ngày để tìm ngày chính xác
    
    Args:
        year: Năm dương lịch
        tiet_khi_index: Index tiết khí (0-23)
        tz: Múi giờ
        
    Returns:
        (day, month, year) của ngày Tiết Khí xảy ra
    """
    # Ước lượng tháng dựa vào index
    # Lập Xuân (0) ~ tháng 2, Xuân Phân (3) ~ tháng 3, v.v.
    estimated_month = (tiet_khi_index // 2) + 1
    if estimated_month > 12:
        estimated_month -= 12
        
    # Ngày giữa tháng
    estimated_day = 15
    
    # Quét ±15 ngày để tìm Tiết Khí
    for offset in range(-15, 16):
        # Điều chỉnh tràn tháng bằng datetime để xử lý chính xác
        import datetime as dt
        try:
            base_date = dt.date(year, estimated_month, 15)
            actual_date = base_date + dt.timedelta(days=offset)
            test_day = actual_date.day
            test_month = actual_date.month
            test_year = actual_date.year
        except (ValueError, OverflowError):
            continue
            
        try:
            tiet_khi = calculate_tiet_khi(test_year, test_month, test_day, tz)
            if tiet_khi['index'] == tiet_khi_index:
                return (test_day, test_month, test_year)
        except Exception:
            continue
            
    # Không tìm thấy (hiếm khi xảy ra)
    return (None, None, None)


# ═══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def format_tiet_khi_info(tiet_khi_info: Dict) -> str:
    """
    Format thông tin Tiết Khí thành chuỗi dễ đọc
    
    Args:
        tiet_khi_info: Dict từ calculate_tiet_khi()
        
    Returns:
        Chuỗi formatted
    """
    duong_am = get_duong_am_don_status(tiet_khi_info)
    season = get_season(tiet_khi_info)
    
    return (
        f"Tiết Khí: {tiet_khi_info['name']} ({tiet_khi_info['chinese']})\n"
        f"Index: {tiet_khi_info['index']}/23\n"
        f"Hoàng kinh: {tiet_khi_info['longitude_deg']}° "
        f"(mong đợi: {tiet_khi_info['expected_longitude']}°)\n"
        f"Mùa: {season}\n"
        f"Âm Dương Độn: {duong_am['status']}\n"
        f"Mô tả: {duong_am['description']}"
    )


# ═══════════════════════════════════════════════════════════════════════════════
# TESTING
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    # Test với một số ngày đặc biệt
    test_dates = [
        (21, 12, 2024, "Đông Chí 2024"),
        (4, 2, 2024, "Lập Xuân 2024"),
        (21, 6, 2024, "Hạ Chí 2024"),
        (15, 1, 2024, "Giữa tháng 1/2024"),
    ]
    
    print("=" * 80)
    print("TESTING TIẾT KHÍ CALCULATOR")
    print("=" * 80)
    
    for day, month, year, description in test_dates:
        print(f"\n{description} ({day}/{month}/{year}):")
        print("-" * 80)
        
        tiet_khi = calculate_tiet_khi(year, month, day)
        print(format_tiet_khi_info(tiet_khi))
