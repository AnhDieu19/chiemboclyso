"""
Tiết Khí Calculator - Tính 24 Tiết Khí từ kinh độ mặt trời

Tái sử dụng: sun_longitude() từ lunar_converter.py
"""

from typing import Dict, Tuple
import math

# 24 Tiết Khí với tên Việt và Hán
TIET_KHI_NAMES = [
    ('Tiểu Hàn', '小寒', 285),      # 0: ~6/1
    ('Đại Hàn', '大寒', 300),       # 1: ~20/1
    ('Lập Xuân', '立春', 315),      # 2: ~4/2
    ('Vũ Thủy', '雨水', 330),       # 3: ~19/2
    ('Kinh Trập', '驚蟄', 345),     # 4: ~6/3
    ('Xuân Phân', '春分', 0),       # 5: ~21/3
    ('Thanh Minh', '清明', 15),     # 6: ~5/4
    ('Cốc Vũ', '穀雨', 30),         # 7: ~20/4
    ('Lập Hạ', '立夏', 45),         # 8: ~6/5
    ('Tiểu Mãn', '小滿', 60),       # 9: ~21/5
    ('Mang Chủng', '芒種', 75),     # 10: ~6/6
    ('Hạ Chí', '夏至', 90),         # 11: ~21/6
    ('Tiểu Thử', '小暑', 105),      # 12: ~7/7
    ('Đại Thử', '大暑', 120),       # 13: ~23/7
    ('Lập Thu', '立秋', 135),       # 14: ~8/8
    ('Xử Thử', '處暑', 150),        # 15: ~23/8
    ('Bạch Lộ', '白露', 165),       # 16: ~8/9
    ('Thu Phân', '秋分', 180),      # 17: ~23/9
    ('Hàn Lộ', '寒露', 195),        # 18: ~8/10
    ('Sương Giáng', '霜降', 210),   # 19: ~24/10
    ('Lập Đông', '立冬', 225),      # 20: ~8/11
    ('Tiểu Tuyết', '小雪', 240),    # 21: ~22/11
    ('Đại Tuyết', '大雪', 255),     # 22: ~7/12
    ('Đông Chí', '冬至', 270),      # 23: ~22/12
]


def jd_from_date(dd: int, mm: int, yy: int) -> float:
    """
    Tính Julius Day Number từ ngày dương lịch
    
    Args:
        dd: Ngày (1-31)
        mm: Tháng (1-12)
        yy: Năm
        
    Returns:
        Julian Day Number (float)
    """
    a = (14 - mm) // 12
    y = yy + 4800 - a
    m = mm + 12 * a - 3
    
    jd = dd + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
    return float(jd)


def sun_longitude(jd: float) -> float:
    """
    Tính kinh độ mặt trời tại thời điểm Julian Day
    
    Công thức VSOP87 đơn giản hóa
    
    Args:
        jd: Julian Day Number
        
    Returns:
        Kinh độ mặt trời (0-360 độ)
    """
    T = (jd - 2451545.0) / 36525.0  # Julian centuries từ J2000.0
    
    # Mean longitude of the Sun
    L0 = 280.4664567 + 360007.6982779 * T + 0.03032028 * T * T
    
    # Mean anomaly of the Sun
    M = 357.5291092 + 35999.0502909 * T - 0.0001536 * T * T
    M_rad = math.radians(M % 360)
    
    # Equation of center
    C = (1.9146 - 0.004817 * T - 0.000014 * T * T) * math.sin(M_rad)
    C += (0.019993 - 0.000101 * T) * math.sin(2 * M_rad)
    C += 0.00029 * math.sin(3 * M_rad)
    
    # Sun's true longitude
    sun_lon = (L0 + C) % 360
    
    return sun_lon


def get_tiet_khi(day: int, month: int, year: int) -> Dict:
    """
    Xác định Tiết Khí hiện tại dựa vào kinh độ mặt trời
    
    Args:
        day: Ngày dương lịch
        month: Tháng dương lịch
        year: Năm dương lịch
        
    Returns:
        Dict với thông tin Tiết Khí:
        - index: 0-23
        - name_vi: Tên tiếng Việt
        - name_han: Tên chữ Hán
        - longitude: Kinh độ mặt trời thực tế
    """
    jd = jd_from_date(day, month, year)
    longitude = sun_longitude(jd)
    
    # Tìm Tiết Khí dựa vào kinh độ
    # Mỗi Tiết Khí = 15 độ
    for i, (name_vi, name_han, start_lon) in enumerate(TIET_KHI_NAMES):
        next_i = (i + 1) % 24
        end_lon = TIET_KHI_NAMES[next_i][2]
        
        # Xử lý case vượt qua 360°
        if start_lon > end_lon:  # VD: 345° - 0°
            if longitude >= start_lon or longitude < end_lon:
                return {
                    'index': i,
                    'name_vi': name_vi,
                    'name_han': name_han,
                    'longitude': longitude,
                    'start_longitude': start_lon
                }
        else:
            if start_lon <= longitude < end_lon:
                return {
                    'index': i,
                    'name_vi': name_vi,
                    'name_han': name_han,
                    'longitude': longitude,
                    'start_longitude': start_lon
                }
    
    # Default: Đông Chí
    return {
        'index': 23,
        'name_vi': 'Đông Chí',
        'name_han': '冬至',
        'longitude': longitude,
        'start_longitude': 270
    }


def is_duong_don(tiet_khi_index: int) -> bool:
    """
    Xác định Dương Độn hay Âm Độn
    
    Dương Độn: Đông Chí (23) → Hạ Chí (11) [Tiết Khí 23, 0-11]
    Âm Độn: Hạ Chí (11) → Đông Chí (23) [Tiết Khí 12-22]
    
    Args:
        tiet_khi_index: 0-23
        
    Returns:
        True nếu Dương Độn, False nếu Âm Độn
    """
    # Dương Độn: từ Đông Chí (23) đến trước Hạ Chí (11)
    # Index 23 hoặc 0-10
    if tiet_khi_index == 23 or tiet_khi_index <= 10:
        return True
    # Âm Độn: từ Hạ Chí (11) đến trước Đông Chí (23)
    # Index 11-22
    return False


def get_tiet_khi_for_ki_mon(day: int, month: int, year: int) -> Dict:
    """
    Lấy thông tin Tiết Khí cho Kì Môn calculation
    
    Returns:
        Dict với:
        - tiet_khi: Thông tin Tiết Khí
        - la_duong_don: True/False
        - fu_head: Phù Đầu (Giáp Tý, Giáp Tuất...)
    """
    tiet_khi = get_tiet_khi(day, month, year)
    la_duong_don = is_duong_don(tiet_khi['index'])
    
    return {
        'tiet_khi': tiet_khi,
        'la_duong_don': la_duong_don,
        'direction': 'thuận' if la_duong_don else 'nghịch'
    }


# Test
if __name__ == '__main__':
    # Test với ngày 24/12/2024
    result = get_tiet_khi(24, 12, 2024)
    print(f"Ngày 24/12/2024:")
    print(f"  Tiết Khí: {result['name_vi']} ({result['name_han']})")
    print(f"  Kinh độ mặt trời: {result['longitude']:.2f}°")
    print(f"  Dương Độn: {is_duong_don(result['index'])}")
