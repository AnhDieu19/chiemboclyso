"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    STAR BRIGHTNESS (ĐỘ SÁNG SAO)                             ║
║                    Bảng Miếu Vượng Đắc Hãm - Nam Phái                        ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Mỗi Chính Tinh có độ sáng khác nhau tại 12 cung                            ║
║  M = Miếu (廟) - Mạnh nhất                                                   ║
║  V = Vượng (旺) - Mạnh                                                       ║
║  Đ = Đắc (得) - Trung bình khá                                              ║
║  B = Bình (平) - Trung bình                                                 ║
║  H = Hãm (陷) - Yếu nhất                                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝

Nguồn: Tử Vi Đại Toàn - Nam Phái
"""

# Ký hiệu độ sáng
BRIGHTNESS_LEVELS = {
    'M': {'name': 'Miếu', 'display': 'M', 'power': 5, 'color': '#006400'},
    'V': {'name': 'Vượng', 'display': 'V', 'power': 4, 'color': '#228B22'},
    'Đ': {'name': 'Đắc', 'display': 'Đ', 'power': 3, 'color': '#32CD32'},
    'B': {'name': 'Bình', 'display': 'B', 'power': 2, 'color': '#808080'},
    'H': {'name': 'Hãm', 'display': 'H', 'power': 1, 'color': '#8B0000'},
}

# Địa Chi index: 0=Tý, 1=Sửu, 2=Dần, 3=Mão, 4=Thìn, 5=Tỵ, 6=Ngọ, 7=Mùi, 8=Thân, 9=Dậu, 10=Tuất, 11=Hợi

# ═══════════════════════════════════════════════════════════════════════════════
# BẢNG ĐỘ SÁNG 14 CHÍNH TINH
# [Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi, Thân, Dậu, Tuất, Hợi]
# ═══════════════════════════════════════════════════════════════════════════════

STAR_BRIGHTNESS_TABLE = {
    # Nhóm Tử Vi
    'Tử Vi': ['V', 'M', 'Đ', 'Đ', 'M', 'B', 'V', 'M', 'Đ', 'Đ', 'M', 'B'],
    'Thiên Cơ': ['H', 'M', 'V', 'V', 'Đ', 'B', 'H', 'M', 'V', 'V', 'Đ', 'B'],
    'Thái Dương': ['H', 'Đ', 'V', 'M', 'M', 'V', 'M', 'Đ', 'B', 'H', 'H', 'H'],
    'Vũ Khúc': ['V', 'M', 'Đ', 'B', 'M', 'V', 'V', 'M', 'Đ', 'B', 'M', 'V'],
    'Thiên Đồng': ['V', 'Đ', 'B', 'H', 'Đ', 'M', 'V', 'Đ', 'B', 'H', 'Đ', 'M'],
    'Liêm Trinh': ['B', 'Đ', 'M', 'H', 'V', 'B', 'B', 'Đ', 'M', 'H', 'V', 'B'],
    
    # Nhóm Thiên Phủ
    'Thiên Phủ': ['M', 'M', 'V', 'Đ', 'M', 'V', 'M', 'M', 'V', 'Đ', 'M', 'V'],
    'Thái Âm': ['M', 'M', 'Đ', 'B', 'H', 'H', 'H', 'Đ', 'V', 'M', 'M', 'M'],
    'Tham Lang': ['V', 'Đ', 'M', 'H', 'Đ', 'B', 'V', 'Đ', 'M', 'H', 'Đ', 'B'],
    'Cự Môn': ['V', 'M', 'Đ', 'B', 'H', 'Đ', 'V', 'M', 'Đ', 'B', 'H', 'Đ'],
    'Thiên Tướng': ['M', 'Đ', 'V', 'B', 'M', 'Đ', 'M', 'Đ', 'V', 'B', 'M', 'Đ'],
    'Thiên Lương': ['M', 'V', 'Đ', 'B', 'Đ', 'V', 'M', 'V', 'Đ', 'B', 'Đ', 'V'],
    'Thất Sát': ['V', 'M', 'V', 'Đ', 'M', 'Đ', 'V', 'M', 'V', 'Đ', 'M', 'Đ'],
    'Phá Quân': ['H', 'Đ', 'B', 'H', 'Đ', 'V', 'H', 'Đ', 'B', 'H', 'Đ', 'V'],
}


def get_star_brightness(star_name: str, chi_index: int) -> dict:
    """
    Lấy độ sáng của sao tại một cung
    
    Args:
        star_name: Tên sao (phải là 1 trong 14 Chính Tinh)
        chi_index: Index Địa Chi của cung (0-11)
        
    Returns:
        dict chứa thông tin độ sáng:
        - code: 'M', 'V', 'Đ', 'B', 'H'
        - name: 'Miếu', 'Vượng'...
        - power: 1-5
        - color: mã màu
        
    Ví dụ:
        get_star_brightness('Tử Vi', 1) → {'code': 'M', 'name': 'Miếu', 'power': 5}
    """
    if star_name not in STAR_BRIGHTNESS_TABLE:
        return {'code': 'B', 'name': 'Bình', 'power': 2, 'color': '#808080'}
    
    brightness_code = STAR_BRIGHTNESS_TABLE[star_name][chi_index % 12]
    return {
        'code': brightness_code,
        **BRIGHTNESS_LEVELS[brightness_code]
    }


def get_brightness_display(star_name: str, chi_index: int) -> str:
    """
    Lấy ký hiệu độ sáng để hiển thị
    
    Returns:
        Ký hiệu: 'M', 'V', 'Đ', 'B', 'H' hoặc '' nếu không phải Chính Tinh
    """
    if star_name not in STAR_BRIGHTNESS_TABLE:
        return ''
    return STAR_BRIGHTNESS_TABLE[star_name][chi_index % 12]


def analyze_brightness_balance(stars: list, chi_index: int) -> dict:
    """
    Phân tích cân bằng độ sáng trong một cung
    
    Args:
        stars: Danh sách sao trong cung
        chi_index: Index Địa Chi của cung
        
    Returns:
        dict phân tích độ sáng
    """
    brightness_counts = {'M': 0, 'V': 0, 'Đ': 0, 'B': 0, 'H': 0}
    total_power = 0
    chinh_tinh_count = 0
    
    for star in stars:
        if star in STAR_BRIGHTNESS_TABLE:
            chinh_tinh_count += 1
            brightness = get_star_brightness(star, chi_index)
            brightness_counts[brightness['code']] += 1
            total_power += brightness['power']
    
    # Đánh giá tổng thể
    if chinh_tinh_count == 0:
        overall = 'Không có Chính Tinh'
    elif brightness_counts['M'] + brightness_counts['V'] >= 2:
        overall = 'Đắc địa - Rất mạnh'
    elif brightness_counts['M'] >= 1 or brightness_counts['V'] >= 2:
        overall = 'Tốt'
    elif brightness_counts['H'] >= 2:
        overall = 'Thất địa - Yếu'
    else:
        overall = 'Trung bình'
    
    return {
        'counts': brightness_counts,
        'total_power': total_power,
        'average_power': total_power / chinh_tinh_count if chinh_tinh_count > 0 else 0,
        'overall': overall
    }
