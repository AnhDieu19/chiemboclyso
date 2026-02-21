"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ĐẠI HẠN - TIỂU HẠN - LƯU NIÊN                             ║
║                    Fortune Periods Calculator                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Đại Hạn: Chu kỳ 10 năm, mỗi người trải qua 12 Đại Hạn                       ║
║  Tiểu Hạn: Chu kỳ 1 năm, xoay vòng theo 12 cung                              ║
║  Lưu Niên: Sao lưu niên theo năm xem                                         ║
╚══════════════════════════════════════════════════════════════════════════════╝

KHÁI NIỆM:
==========
- ĐẠI HẠN: Vận mệnh 10 năm, khởi từ Cung Mệnh, thuận/nghịch theo Âm Dương năm sinh
- TIỂU HẠN: Vận mệnh 1 năm, khởi từ cung theo tuổi, thuận/nghịch theo nam/nữ
- LƯU NIÊN: Các sao lưu động theo năm xem (Thái Tuế, Lưu Tả Hữu...)

CÔNG THỨC:
==========
1. Đại Hạn khởi từ Cung Mệnh, tuổi bắt đầu = Số Cục
   - Nam Dương, Nữ Âm: Thuận hành
   - Nam Âm, Nữ Dương: Nghịch hành

2. Tiểu Hạn khởi từ cung:
   - Tuổi Dần, Ngọ, Tuất: Khởi Thìn
   - Tuổi Thân, Tý, Thìn: Khởi Tuất
   - Tuổi Tỵ, Dậu, Sửu: Khởi Mùi
   - Tuổi Hợi, Mão, Mùi: Khởi Sửu
"""

from data import DIA_CHI


# ═══════════════════════════════════════════════════════════════════════════════
# BẢNG TRA KHỞI ĐIỂM TIỂU HẠN
# ═══════════════════════════════════════════════════════════════════════════════

# Chi năm sinh → Cung khởi Tiểu Hạn tuổi 1
TIEU_HAN_START = {
    # Dần, Ngọ, Tuất (Hỏa cục) → Khởi Thìn
    2: 4, 6: 4, 10: 4,
    # Thân, Tý, Thìn (Thủy cục) → Khởi Tuất
    8: 10, 0: 10, 4: 10,
    # Tỵ, Dậu, Sửu (Kim cục) → Khởi Mùi
    5: 7, 9: 7, 1: 7,
    # Hợi, Mão, Mùi (Mộc cục) → Khởi Sửu
    11: 1, 3: 1, 7: 1,
}


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH ĐẠI HẠN
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_dai_han(menh_position: int, cuc_number: int, 
                       year_can_index: int, gender: str) -> list:
    """
    Tính 12 Đại Hạn (vận 10 năm)
    
    CÔNG THỨC:
    - Khởi từ Cung Mệnh, tuổi bắt đầu = Số Cục
    - Thuận/Nghịch theo Âm Dương năm sinh và giới tính:
      + Nam Dương, Nữ Âm: Thuận hành (đếm tăng cung)
      + Nam Âm, Nữ Dương: Nghịch hành (đếm giảm cung)
    
    Args:
        menh_position: Index Cung Mệnh (0-11)
        cuc_number: Số Cục (2-6)
        year_can_index: Index Can năm (0-9), dùng xác định Âm/Dương
        gender: 'nam' hoặc 'nu'
        
    Returns:
        list 12 dict, mỗi dict chứa:
        - start_age: Tuổi bắt đầu
        - end_age: Tuổi kết thúc
        - position: Index cung Đại Hạn
        - chi: Tên Địa Chi của cung
    """
    dai_han_list = []
    
    # Xác định Âm/Dương năm (Can chẵn = Dương, Can lẻ = Âm)
    is_duong_year = (year_can_index % 2 == 0)
    
    # Xác định chiều (thuận = +1, nghịch = -1)
    # Nam Dương, Nữ Âm → Thuận
    # Nam Âm, Nữ Dương → Nghịch
    if gender.lower() == 'nam':
        direction = 1 if is_duong_year else -1
    else:
        direction = -1 if is_duong_year else 1
    
    # Tuổi bắt đầu = Số Cục
    start_age = cuc_number
    
    # Tính 12 Đại Hạn
    for i in range(12):
        position = (menh_position + direction * i) % 12
        
        dai_han_list.append({
            'index': i + 1,
            'start_age': start_age + i * 10,
            'end_age': start_age + i * 10 + 9,
            'position': position,
            'chi': DIA_CHI[position],
            'direction': 'Thuận' if direction == 1 else 'Nghịch'
        })
    
    return dai_han_list


def get_current_dai_han(dai_han_list: list, age: int) -> dict:
    """
    Lấy Đại Hạn hiện tại theo tuổi
    
    Args:
        dai_han_list: List Đại Hạn từ calculate_dai_han()
        age: Tuổi hiện tại
        
    Returns:
        dict Đại Hạn hiện tại hoặc None
    """
    for dh in dai_han_list:
        if dh['start_age'] <= age <= dh['end_age']:
            return dh
    return None


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH TIỂU HẠN
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_tieu_han(year_chi_index: int, gender: str, age: int) -> dict:
    """
    Tính Tiểu Hạn cho một tuổi cụ thể
    
    CÔNG THỨC:
    - Khởi từ cung tra theo Chi năm sinh
    - Thuận/Nghịch theo giới tính:
      + Nam: Thuận hành
      + Nữ: Nghịch hành
    - Đếm theo tuổi
    
    Args:
        year_chi_index: Index Chi năm sinh (0-11)
        gender: 'nam' hoặc 'nu'
        age: Tuổi muốn tính Tiểu Hạn
        
    Returns:
        dict chứa position, chi
    """
    # Lấy cung khởi điểm
    start_position = TIEU_HAN_START.get(year_chi_index, 4)  # Default Thìn
    
    # Chiều: Nam thuận, Nữ nghịch
    direction = 1 if gender.lower() == 'nam' else -1
    
    # Tính vị trí: khởi từ start_position, đếm (age - 1) bước
    position = (start_position + direction * (age - 1)) % 12
    
    return {
        'age': age,
        'position': position,
        'chi': DIA_CHI[position],
        'direction': 'Thuận' if direction == 1 else 'Nghịch'
    }


def calculate_tieu_han_range(year_chi_index: int, gender: str, 
                              start_age: int, end_age: int) -> list:
    """
    Tính Tiểu Hạn cho một khoảng tuổi
    
    Returns:
        list các dict Tiểu Hạn
    """
    return [
        calculate_tieu_han(year_chi_index, gender, age)
        for age in range(start_age, end_age + 1)
    ]


# ═══════════════════════════════════════════════════════════════════════════════
# LƯU NIÊN SAO
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_luu_nien(viewing_year: int) -> dict:
    """
    Tính các sao Lưu Niên theo năm xem
    
    Các sao Lưu Niên:
    - Lưu Thái Tuế: Tại cung Chi của năm xem
    - Lưu Tang Môn, Bạch Hổ...: Theo vòng Thái Tuế lưu niên
    - Lưu Thiên Mã: Đối xung với Thái Tuế
    
    Args:
        viewing_year: Năm xem (Dương lịch)
        
    Returns:
        dict các sao lưu niên và vị trí
    """
    # Tính Chi năm xem
    chi_index = (viewing_year + 8) % 12
    
    # Các sao Lưu Niên theo vòng Thái Tuế
    luu_nien_stars = {
        'Lưu Thái Tuế': chi_index,
        'Lưu Thiếu Dương': (chi_index + 1) % 12,
        'Lưu Tang Môn': (chi_index + 2) % 12,
        'Lưu Thiếu Âm': (chi_index + 3) % 12,
        'Lưu Quan Phù': (chi_index + 4) % 12,
        'Lưu Từ Phù': (chi_index + 5) % 12,
        'Lưu Tuế Phá': (chi_index + 6) % 12,
        'Lưu Long Đức': (chi_index + 7) % 12,
        'Lưu Bạch Hổ': (chi_index + 8) % 12,
        'Lưu Phúc Đức': (chi_index + 9) % 12,
        'Lưu Điếu Khách': (chi_index + 10) % 12,
        'Lưu Trực Phù': (chi_index + 11) % 12,
    }
    
    # Lưu Thiên Mã (theo Tam Hợp Chi năm xem)
    # Dần-Ngọ-Tuất → Thân
    # Thân-Tý-Thìn → Dần
    # Tỵ-Dậu-Sửu → Hợi
    # Hợi-Mão-Mùi → Tỵ
    if chi_index in [2, 6, 10]:   # Dần, Ngọ, Tuất
        luu_nien_stars['Lưu Thiên Mã'] = 8  # Thân
    elif chi_index in [8, 0, 4]:  # Thân, Tý, Thìn
        luu_nien_stars['Lưu Thiên Mã'] = 2  # Dần
    elif chi_index in [5, 9, 1]:  # Tỵ, Dậu, Sửu
        luu_nien_stars['Lưu Thiên Mã'] = 11 # Hợi
    else:                         # Hợi, Mão, Mùi
        luu_nien_stars['Lưu Thiên Mã'] = 5  # Tỵ
    
    # Lưu Thiên Mã (theo Tam Hợp Chi năm xem)
    # ... (code check previously updated)
    
    # Lưu Lộc Tồn (theo Can năm xem)
    can_index = (viewing_year + 6) % 10
    loc_ton_positions = [2, 3, 5, 6, 5, 6, 8, 9, 11, 0]  # Giáp→Dần, Ất→Mão...
    lt_pos = loc_ton_positions[can_index]
    luu_nien_stars['Lưu Lộc Tồn'] = lt_pos
    
    # Lưu Kinh Dương (Trước Lộc Tồn), Lưu Đà La (Sau Lộc Tồn)
    luu_nien_stars['Lưu Kinh Dương'] = (lt_pos + 1) % 12
    luu_nien_stars['Lưu Đà La'] = (lt_pos - 1 + 12) % 12

    # Lưu Thiên Khốc, Lưu Thiên Hư (theo Chi năm xem)
    # Khốc: Ngọ nghịch, Hư: Ngọ thuận
    # Ngọ = 6
    luu_nien_stars['Lưu Thiên Khốc'] = (6 - chi_index + 12) % 12
    luu_nien_stars['Lưu Thiên Hư'] = (6 + chi_index) % 12
    
    return {
        'year': viewing_year,
        'chi_index': chi_index,
        'chi_name': DIA_CHI[chi_index],
        'can_index': can_index,
        'stars': luu_nien_stars,
        'stars_detail': {
            star: {'position': pos, 'chi': DIA_CHI[pos]}
            for star, pos in luu_nien_stars.items()
        }
    }


# ═══════════════════════════════════════════════════════════════════════════════
# LƯU NIÊN TỨ HÓA (UC-05: Theo yêu cầu BA)
# Tứ Hóa theo Can của năm xem (không phải năm sinh)
# ═══════════════════════════════════════════════════════════════════════════════

# Bảng Tứ Hóa
LUU_NIEN_TU_HOA_TABLE = {
    0: {'loc': 'Liêm Trinh', 'quyen': 'Phá Quân', 'khoa': 'Vũ Khúc', 'ky': 'Thái Dương'},     # Giáp
    1: {'loc': 'Thiên Cơ', 'quyen': 'Thiên Lương', 'khoa': 'Tử Vi', 'ky': 'Thái Âm'},          # Ất
    2: {'loc': 'Thiên Đồng', 'quyen': 'Thiên Cơ', 'khoa': 'Văn Xương', 'ky': 'Liêm Trinh'},    # Bính
    3: {'loc': 'Thái Âm', 'quyen': 'Thiên Đồng', 'khoa': 'Thiên Cơ', 'ky': 'Cự Môn'},          # Đinh
    4: {'loc': 'Tham Lang', 'quyen': 'Thái Âm', 'khoa': 'Hữu Bật', 'ky': 'Thiên Cơ'},          # Mậu
    5: {'loc': 'Vũ Khúc', 'quyen': 'Tham Lang', 'khoa': 'Thiên Lương', 'ky': 'Văn Khúc'},      # Kỷ
    6: {'loc': 'Thái Dương', 'quyen': 'Vũ Khúc', 'khoa': 'Thái Âm', 'ky': 'Thiên Đồng'},       # Canh
    7: {'loc': 'Cự Môn', 'quyen': 'Thái Dương', 'khoa': 'Văn Khúc', 'ky': 'Văn Xương'},        # Tân
    8: {'loc': 'Thiên Lương', 'quyen': 'Tử Vi', 'khoa': 'Tả Phụ', 'ky': 'Vũ Khúc'},            # Nhâm
    9: {'loc': 'Phá Quân', 'quyen': 'Cự Môn', 'khoa': 'Thái Âm', 'ky': 'Tham Lang'}            # Quý
}


def calculate_luu_nien_tu_hoa(viewing_year: int, all_stars: dict) -> dict:
    """
    Tính Lưu Niên Tứ Hóa (Tứ Hóa theo năm xem)
    
    QUAN TRỌNG: Khác với Tứ Hóa bản mệnh, Lưu Niên Tứ Hóa tính theo
    Can của năm đang xem, không phải năm sinh.
    
    Args:
        viewing_year: Năm xem (Dương lịch)
        all_stars: Dict vị trí tất cả các sao trong lá số
        
    Returns:
        dict Lưu Niên Tứ Hóa và vị trí
    """
    can_index = (viewing_year + 6) % 10
    tu_hoa = LUU_NIEN_TU_HOA_TABLE[can_index]
    
    result = {
        'year': viewing_year,
        'can_index': can_index,
    }
    
    # Lưu Hóa Lộc
    if tu_hoa['loc'] in all_stars:
        result['Lưu Hóa Lộc'] = {
            'star': tu_hoa['loc'], 
            'position': all_stars[tu_hoa['loc']]
        }
    
    # Lưu Hóa Quyền
    if tu_hoa['quyen'] in all_stars:
        result['Lưu Hóa Quyền'] = {
            'star': tu_hoa['quyen'], 
            'position': all_stars[tu_hoa['quyen']]
        }
    
    # Lưu Hóa Khoa
    if tu_hoa['khoa'] in all_stars:
        result['Lưu Hóa Khoa'] = {
            'star': tu_hoa['khoa'], 
            'position': all_stars[tu_hoa['khoa']]
        }
    
    # Lưu Hóa Kỵ
    if tu_hoa['ky'] in all_stars:
        result['Lưu Hóa Kỵ'] = {
            'star': tu_hoa['ky'], 
            'position': all_stars[tu_hoa['ky']]
        }
    
    return result


def calculate_luu_nguyet(viewing_year: int, viewing_month: int) -> dict:
    """
    Tính Lưu Nguyệt (tháng lưu niên)
    
    Args:
        viewing_year: Năm xem
        viewing_month: Tháng xem (1-12)
        
    Returns:
        dict vị trí cung tháng
    """
    # Cung tháng: Tháng Giêng = Dần, Tháng 2 = Mão...
    month_position = (viewing_month + 1) % 12
    
    return {
        'year': viewing_year,
        'month': viewing_month,
        'position': month_position,
        'chi': DIA_CHI[month_position]
    }


# ═══════════════════════════════════════════════════════════════════════════════
# HÀM TIỆN ÍCH
# ═══════════════════════════════════════════════════════════════════════════════

def get_fortune_periods(chart: dict, current_year: int = None) -> dict:
    """
    Tính đầy đủ Đại Hạn, Tiểu Hạn, Lưu Niên, Lưu Niên Tứ Hóa
    
    Args:
        chart: Dữ liệu lá số
        current_year: Năm hiện tại (mặc định: năm hiện tại)
        
    Returns:
        dict đầy đủ thông tin vận hạn
    """
    if current_year is None:
        from datetime import datetime
        current_year = datetime.now().year
    # Lấy thông tin từ chart
    menh_position = chart.get('menh_position', 0)
    cuc_number = chart.get('cuc', {}).get('number', 5)
    year_can_index = chart.get('year_can_chi', {}).get('can_index', 0)
    year_chi_index = chart.get('year_can_chi', {}).get('chi_index', 0)
    gender = chart.get('gender', 'nam')
    birth_year = chart.get('lunar_date', {}).get('year', 1990)
    all_stars = chart.get('all_stars', {})
    
    # Tính tuổi (tính theo tuổi mụ)
    age = current_year - birth_year + 1
    
    # Tính Đại Hạn
    dai_han = calculate_dai_han(menh_position, cuc_number, year_can_index, gender)
    current_dai_han = get_current_dai_han(dai_han, age)
    
    # Tính Tiểu Hạn hiện tại
    tieu_han = calculate_tieu_han(year_chi_index, gender, age)
    
    # Tính Lưu Niên
    luu_nien = calculate_luu_nien(current_year)
    
    # Tính Lưu Niên Tứ Hóa (UC-05 theo yêu cầu BA)
    luu_nien_tu_hoa = calculate_luu_nien_tu_hoa(current_year, all_stars)
    
    return {
        'birth_year': birth_year,
        'current_year': current_year,
        'age': age,
        'dai_han_all': dai_han,
        'current_dai_han': current_dai_han,
        'tieu_han': tieu_han,
        'luu_nien': luu_nien,
        'luu_nien_tu_hoa': luu_nien_tu_hoa
    }
