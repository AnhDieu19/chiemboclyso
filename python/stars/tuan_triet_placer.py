"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    TUẦN - TRIỆT VÀ CÁC SAO PHỤ PLACER                        ║
║                    Reference: CALCULATION_GUIDE.md (Section 7.8)             ║
║                    An Tuần, Triệt, Cô Thần, Quả Tú...                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Đặt các sao quan trọng còn thiếu vào lá số                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from data import (
    CO_THAN_QUA_TU, THAI_PHU_PHONG_CAC,
    LUU_HA_POSITION, KIEP_SAT_POSITION, PHA_TOAI_POSITION,
    THIEN_VU_POSITION, THIEN_TAI_THO_YEAR
)


def calculate_tuan_logic(year_can_index: int, year_chi_index: int) -> tuple:
    """
    Tính vị trí Tuần Trung công thức toán học
    Tuần = (Chi - Can + 10) % 12
    Kết quả là cung đầu tiên trong 2 cung Tuần.
    """
    # Ex: Giáp Tuất (0, 10) -> (10 - 0 + 10) % 12 = 8 (Thân) -> Thân, Dậu.
    tuan_1 = (year_chi_index - year_can_index + 10) % 12
    tuan_2 = (tuan_1 + 1) % 12
    return tuan_1, tuan_2

def calculate_triet_logic(year_can_index: int) -> tuple:
    """
    Tính vị trí Triệt Lộ công thức toán học
    Triệt = (8 - (Can % 5) * 2) % 12
    """
    # Ex: Giáp (0) -> (8 - 0) = 8 (Thân) -> Thân, Dậu.
    triet_1 = (8 - (year_can_index % 5) * 2) % 12
    triet_2 = (triet_1 + 1) % 12
    return triet_1, triet_2

def place_tuan_triet(year_can_index: int, year_chi_index: int) -> dict:
    """
    An sao Tuần và Triệt (Algorithmic)
    """
    stars = {}
    
    # Tính vị trí Tuần
    tuan_1, tuan_2 = calculate_tuan_logic(year_can_index, year_chi_index)
    stars['Tuần 1'] = tuan_1
    stars['Tuần 2'] = tuan_2
    
    # Tính vị trí Triệt
    triet_1, triet_2 = calculate_triet_logic(year_can_index)
    stars['Triệt 1'] = triet_1
    stars['Triệt 2'] = triet_2
    
    return stars


def place_additional_stars(year_can_index: int, year_chi_index: int, 
                           lunar_month: int, gender: str) -> dict:
    """
    An các sao phụ quan trọng còn thiếu
    
    *Lưu ý*: Giải Thần, Thiên Giải, Thiên Đức, Nguyệt Đức đã được chuyển sang 
    `bo_sung_placer.py` (theo chuẩn Nam Phái).
    """
    stars = {}
    month_key = min(max(lunar_month, 1), 12)
    
    # ═══════════════════════════════════════════════════════════════════════
    # CÔ THẦN - QUẢ TÚ
    # ═══════════════════════════════════════════════════════════════════════
    co_qua = CO_THAN_QUA_TU.get(year_chi_index, (2, 10))
    stars['Cô Thần'] = co_qua[0]
    stars['Quả Tú'] = co_qua[1]
    
    # ═══════════════════════════════════════════════════════════════════════
    # LƯU HÀ - THIÊN Y
    # Lưu Hà: Theo Can năm
    # Thiên Y: Theo Tháng (Tháng 1 Sửu, tiến 1 cung)
    # ═══════════════════════════════════════════════════════════════════════
    stars['Lưu Hà'] = LUU_HA_POSITION.get(year_can_index, 9)
    # Thiên Y: (1 + month - 1) % 12
    stars['Thiên Y'] = (1 + lunar_month - 1) % 12
    
    # ═══════════════════════════════════════════════════════════════════════
    # KIẾP SÁT - PHÁ TOÁI
    # Kiếp Sát: hung tinh, tai họa bất ngờ
    # Phá Toái: phá hoại, hao tán
    # ═══════════════════════════════════════════════════════════════════════
    stars['Kiếp Sát'] = KIEP_SAT_POSITION.get(year_chi_index, 5)
    stars['Phá Toái'] = PHA_TOAI_POSITION.get(year_chi_index, 5)
    
    # ═══════════════════════════════════════════════════════════════════════
    # THIÊN VU (theo tháng)
    # Thiên Vu: khóc lóc, buồn phiền
    # ═══════════════════════════════════════════════════════════════════════
    stars['Thiên Vu'] = THIEN_VU_POSITION.get(month_key, 6)
    
    # Thiên Tài - Thiên Thọ đã chuyển sang place_supplementary_stars (theo Mệnh/Thân)
    
    return stars


def get_tuan_triet_info(year_can_index: int, year_chi_index: int) -> dict:
    """
    Lấy thông tin chi tiết về Tuần và Triệt cho hiển thị
    """
    from data import DIA_CHI
    
    tuan_1, tuan_2 = calculate_tuan_logic(year_can_index, year_chi_index)
    triet_1, triet_2 = calculate_triet_logic(year_can_index)
    
    return {
        'tuan': {
            'positions': [tuan_1, tuan_2],
            'names': [DIA_CHI[tuan_1], DIA_CHI[tuan_2]],
            'description': 'Sao trong cung Tuần bị giảm lực, có thể hóa giải hung tinh'
        },
        'triet': {
            'positions': [triet_1, triet_2],
            'names': [DIA_CHI[triet_1], DIA_CHI[triet_2]],
            'description': 'Sao trong cung Triệt bị cắt đứt lực, ảnh hưởng Đại Hạn'
        }
    }


def check_star_in_tuan_triet(star_position: int, year_can_index: int, 
                               year_chi_index: int) -> dict:
    """
    Kiểm tra một sao có nằm trong Tuần hoặc Triệt không
    """
    tuan_1, tuan_2 = calculate_tuan_logic(year_can_index, year_chi_index)
    triet_1, triet_2 = calculate_triet_logic(year_can_index)
    
    in_tuan = star_position in [tuan_1, tuan_2]
    in_triet = star_position in [triet_1, triet_2]
    
    return {
        'in_tuan': in_tuan,
        'in_triet': in_triet,
        'effect': 'Giảm lực' if in_tuan or in_triet else 'Bình thường'
    }

