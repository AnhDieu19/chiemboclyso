"""
Chart Layer - Chart Builder
Main chart generation orchestration using modular components
Reference: CALCULATION_GUIDE.md (Section 1.1 - Quy Trình Lập Lá Số)
"""

from data import DIA_CHI, CUNG_ORDER, GIO_SINH_RANGE, get_star_brightness, STAR_BRIGHTNESS_TABLE
from core import (
    solar_to_lunar, 
    get_year_can_chi, get_month_can_chi, get_day_can_chi, get_hour_can_chi, hour_to_chi_index,
    calculate_cung_menh, calculate_cung_than,
    calculate_cung_menh, calculate_cung_than,
    determine_cuc, get_nap_am
)
from data import get_star_color
from stars import (
    calculate_tuvi_position, place_chinh_tinh,
    place_luc_cat, place_luc_sat, place_truong_sinh,
    place_bac_sy_ring, place_thai_tue_ring, place_other_stars,
    place_year_other_stars, place_month_other_stars,
    apply_tu_hoa,
    place_tuan_triet, place_additional_stars, get_tuan_triet_info,
    place_supplementary_stars, get_menh_than_chu,
    place_ta_huu, place_khoi_viet, place_xuong_khuc,
    place_kinh_da, place_hoa_linh, place_khong_kiep
)
from core.fortune_periods import calculate_tieu_han
from datetime import datetime


def arrange_cung(menh_position: int) -> dict:
    """Arrange 12 Cung on the chart starting from Cung Mệnh"""
    cung_map = {}
    for i in range(12):
        position = (menh_position + i) % 12
        cung_map[position] = CUNG_ORDER[i]
    return cung_map


def build_positions(all_stars: dict, tu_hoa: dict, cung_map: dict, 
                    menh_position: int, than_position: int,
                    tuan_triet_info: dict = None, tieu_han: dict = None) -> dict:
    """Build position data for display"""
    positions = {}
    
    # Get Tuần Triệt positions if available
    tuan_positions = []
    triet_positions = []
    if tuan_triet_info:
        tuan_positions = tuan_triet_info.get('tuan', {}).get('positions', [])
        triet_positions = tuan_triet_info.get('triet', {}).get('positions', [])
    
    for i in range(12):
        positions[i] = {
            'chi': DIA_CHI[i],
            'cung': cung_map.get(i, ''),
            'stars': [],
            'hoa': [],
            'in_tuan': i in tuan_positions,
            'in_triet': i in triet_positions
        }
        
        # Add stars at this position with brightness info
        for star, pos in all_stars.items():
            if pos == i:
                # Thêm độ sáng cho Chính Tinh (UC-03)
                if star in STAR_BRIGHTNESS_TABLE:
                    brightness = get_star_brightness(star, i)
                    star_color = get_star_color(star)
                    positions[i]['stars'].append({
                        'name': star,
                        'brightness': brightness['code'],
                        'brightness_name': brightness['name'],
                        'power': brightness['power'],
                        'color': star_color['code'],
                        'css_class': star_color['class'],
                        'element': star_color['element']
                    })
                else:
                    star_color = get_star_color(star)
                    positions[i]['stars'].append({
                        'name': star,
                        'color': star_color['code'],
                        'css_class': star_color['class'],
                        'element': star_color['element']
                    })
        
        # Add Tứ Hóa at this position
        for hoa_name, hoa_info in tu_hoa.items():
            if hoa_info['position'] == i:
                positions[i]['hoa'].append({'name': hoa_name, 'star': hoa_info['star']})
        
        # Mark Cung Mệnh and Cung Thân
        if i == menh_position:
            positions[i]['is_menh'] = True
        if i == menh_position:
            positions[i]['is_menh'] = True
        if i == than_position:
            positions[i]['is_than'] = True
            
        # Add Tieu Han info
        if tieu_han and tieu_han.get('position') == i:
            positions[i]['tieu_han_age'] = tieu_han.get('age')
    
    return positions


def generate_birth_chart(day: int, month: int, year: int, hour: int, gender: str, viewing_year: int = None) -> dict:
    """
    Generate complete birth chart (Lá Số Tử Vi) from solar date
    """
    # Convert to lunar calendar
    lunar = solar_to_lunar(day, month, year)
    # Note: hour is already chi index (0-11) from frontend, not 24h format
    hour_index = hour
    
    # Get Can Chi
    year_can_chi = get_year_can_chi(lunar['year'])
    month_can_chi = get_month_can_chi(lunar['month'], lunar['year'])
    day_can_chi = get_day_can_chi(day, month, year)
    hour_can_chi = get_hour_can_chi(hour_index, day, month, year)
    
    # Calculate positions
    menh_position = calculate_cung_menh(lunar['month'], hour_index)
    than_position = calculate_cung_than(lunar['month'], hour_index)
    nap_am = get_nap_am(year_can_chi['can_index'], year_can_chi['chi_index'])
    cuc = determine_cuc(year_can_chi['can_index'], menh_position)
    
    # Calculate Tử Vi and place Chính Tinh
    tu_vi_position = calculate_tuvi_position(cuc['number'], lunar['day'])
    chinh_tinh = place_chinh_tinh(tu_vi_position)
    
    # Place all Phụ Tinh
    luc_cat = place_luc_cat(year_can_chi['can_index'], lunar['month'], hour_index)
    
    # Extract dependencies for derived stars
    ta_huu = {'Tả Phụ': luc_cat.get('Tả Phụ'), 'Hữu Bật': luc_cat.get('Hữu Bật')}
    xuong_khuc = {'Văn Xương': luc_cat.get('Văn Xương'), 'Văn Khúc': luc_cat.get('Văn Khúc')}
    
    luc_sat = place_luc_sat(year_can_chi['can_index'], year_can_chi['chi_index'], hour_index, gender)
    truong_sinh = place_truong_sinh(year_can_chi['can_index'], gender, cuc['number'])
    bac_sy = place_bac_sy_ring(year_can_chi['can_index'], gender)
    thai_tue = place_thai_tue_ring(year_can_chi['chi_index'])
    other = place_other_stars(year_can_chi['can_index'], year_can_chi['chi_index'], 
                               lunar['month'], hour_index, lunar['day'],
                               ta_huu, xuong_khuc)
    
    # Place Tuần, Triệt và các sao phụ bổ sung
    tuan_triet = place_tuan_triet(year_can_chi['can_index'], year_can_chi['chi_index'])
    additional = place_additional_stars(year_can_chi['can_index'], year_can_chi['chi_index'], 
                                         lunar['month'], gender)
    tuan_triet_info = get_tuan_triet_info(year_can_chi['can_index'], year_can_chi['chi_index'])
    
    # Place sao bổ sung (để đạt >= 114 sao)
    supplementary = place_supplementary_stars(year_can_chi['chi_index'], hour_index, 
                                               lunar['month'], menh_position, than_position)
    menh_than_chu = get_menh_than_chu(menh_position, year_can_chi['chi_index'])
    
    # Combine all stars
    all_stars = {**chinh_tinh, **luc_cat, **luc_sat, **truong_sinh, **bac_sy, **thai_tue, **other, 
                 **tuan_triet, **additional, **supplementary}
    
    # Apply Tứ Hóa
    tu_hoa = apply_tu_hoa(year_can_chi['can_index'], all_stars)
    
    # Add Tứ Hóa as positional stars in all_stars for display
    for hoa_name, hoa_info in tu_hoa.items():
        all_stars[hoa_name] = hoa_info['position']
    
    # Calculate Tieu Han for current/viewing year
    if viewing_year is None:
        viewing_year = datetime.now().year
    
    current_age_am = viewing_year - lunar['year'] + 1
    tieu_han = calculate_tieu_han(year_can_chi['chi_index'], gender, current_age_am)

    # Arrange Cung and build positions
    cung_map = arrange_cung(menh_position)
    positions = build_positions(all_stars, tu_hoa, cung_map, menh_position, than_position, tuan_triet_info, tieu_han)
    
    return {
        'solar_date': {'day': day, 'month': month, 'year': year},
        'lunar_date': lunar,
        'hour': hour_index,
        'hour_name': DIA_CHI[hour_index],
        'gender': gender,
        'year_can_chi': year_can_chi,
        'month_can_chi': month_can_chi,
        'day_can_chi': day_can_chi,
        'hour_can_chi': hour_can_chi,
        'nap_am': nap_am,
        'menh_position': menh_position,
        'menh_name': DIA_CHI[menh_position],
        'than_position': than_position,
        'than_name': DIA_CHI[than_position],
        'cuc': cuc,
        'tu_vi_position': tu_vi_position,
        'chinh_tinh': chinh_tinh,
        'all_stars': all_stars,
        'tu_hoa': tu_hoa,
        'cung_map': cung_map,
        'positions': positions,
        'tuan_triet': tuan_triet_info,
        'menh_chu': menh_than_chu['menh_chu'],
        'than_chu': menh_than_chu['than_chu']
    }


def generate_birth_chart_lunar(lunar_day: int, lunar_month: int, lunar_year: int,
                                hour: int, gender: str, leap_month: bool = False) -> dict:
    """
    Generate complete birth chart from Lunar date directly
    """
    lunar = {'day': lunar_day, 'month': lunar_month, 'year': lunar_year, 'leap': leap_month}
    # Note: hour is already chi index (0-11) from frontend, not 24h format
    hour_index = hour
    
    year_can_chi = get_year_can_chi(lunar_year)
    month_can_chi = get_month_can_chi(lunar_month, lunar_year)
    
    menh_position = calculate_cung_menh(lunar_month, hour_index)
    than_position = calculate_cung_than(lunar_month, hour_index)
    nap_am = get_nap_am(year_can_chi['can_index'], year_can_chi['chi_index'])
    cuc = determine_cuc(year_can_chi['can_index'], menh_position)
    
    tu_vi_position = calculate_tuvi_position(cuc['number'], lunar_day)
    chinh_tinh = place_chinh_tinh(tu_vi_position)
    
    luc_cat = place_luc_cat(year_can_chi['can_index'], lunar_month, hour_index)
    
    # Extract dependencies for derived stars
    ta_huu = {'Tả Phụ': luc_cat.get('Tả Phụ'), 'Hữu Bật': luc_cat.get('Hữu Bật')}
    xuong_khuc = {'Văn Xương': luc_cat.get('Văn Xương'), 'Văn Khúc': luc_cat.get('Văn Khúc')}
    
    luc_sat = place_luc_sat(year_can_chi['can_index'], year_can_chi['chi_index'], hour_index, gender)
    truong_sinh = place_truong_sinh(year_can_chi['can_index'], gender, cuc['number'])
    bac_sy = place_bac_sy_ring(year_can_chi['can_index'], gender)
    thai_tue = place_thai_tue_ring(year_can_chi['chi_index'])
    other = place_other_stars(year_can_chi['can_index'], year_can_chi['chi_index'], 
                               lunar_month, hour_index, lunar_day,
                               ta_huu, xuong_khuc)
    
    # Place Tuần, Triệt và các sao phụ bổ sung
    tuan_triet = place_tuan_triet(year_can_chi['can_index'], year_can_chi['chi_index'])
    additional = place_additional_stars(year_can_chi['can_index'], year_can_chi['chi_index'], 
                                         lunar_month, gender)
    tuan_triet_info = get_tuan_triet_info(year_can_chi['can_index'], year_can_chi['chi_index'])
    
    # Place sao bổ sung (để đạt >= 114 sao)
    supplementary = place_supplementary_stars(year_can_chi['chi_index'], hour_index, 
                                               lunar_month, menh_position, than_position)
    menh_than_chu = get_menh_than_chu(menh_position, year_can_chi['chi_index'])
    
    all_stars = {**chinh_tinh, **luc_cat, **luc_sat, **truong_sinh, **bac_sy, **thai_tue, **other,
                 **tuan_triet, **additional, **supplementary}
    tu_hoa = apply_tu_hoa(year_can_chi['can_index'], all_stars)
    
    # Add Tứ Hóa as positional stars in all_stars for display
    for hoa_name, hoa_info in tu_hoa.items():
        all_stars[hoa_name] = hoa_info['position']
    
    cung_map = arrange_cung(menh_position)
    positions = build_positions(all_stars, tu_hoa, cung_map, menh_position, than_position, tuan_triet_info)
    
    hour_can_chi = {
        'can_index': (year_can_chi['can_index'] * 2 + hour_index) % 10,
        'chi_index': hour_index,
        'full': 'N/A (từ Âm lịch)'
    }
    
    return {
        'solar_date': {'day': '?', 'month': '?', 'year': lunar_year},
        'lunar_date': lunar,
        'hour': hour_index,
        'hour_name': DIA_CHI[hour_index],
        'gender': gender,
        'year_can_chi': year_can_chi,
        'month_can_chi': month_can_chi,
        'day_can_chi': {'full': 'N/A'},
        'hour_can_chi': hour_can_chi,
        'nap_am': nap_am,
        'menh_position': menh_position,
        'menh_name': DIA_CHI[menh_position],
        'than_position': than_position,
        'than_name': DIA_CHI[than_position],
        'cuc': cuc,
        'tu_vi_position': tu_vi_position,
        'chinh_tinh': chinh_tinh,
        'all_stars': all_stars,
        'tu_hoa': tu_hoa,
        'cung_map': cung_map,
        'positions': positions,
        'tuan_triet': tuan_triet_info,
        'menh_chu': menh_than_chu['menh_chu'],
        'than_chu': menh_than_chu['than_chu']
    }



def generate_partial_chart(year: int, month: int = None, gender: str = None) -> dict:
    """
    Generate partial chart with available information (Year/Month)
    Used when Day/Hour is missing
    """
    # Initialize basic data
    lunar = {'year': year, 'month': month, 'day': None, 'leap': False}
    
    # Get Year Can Chi
    year_can_chi = get_year_can_chi(year)
    month_can_chi = {'full': 'N/A'}
    if month:
        month_can_chi = get_month_can_chi(month, year) # Ensure month is valid

        
    # Place Year-based stars
    wai_stars = {}
    
    # 1. Thái Tuế Ring (Year Chi)
    wai_stars.update(place_thai_tue_ring(year_can_chi['chi_index']))
    
    # 2. Lộc Tồn / Bác Sĩ (Year Can) - Bác Sĩ ring depends on Lộc Tồn
    wai_stars.update(place_bac_sy_ring(year_can_chi['can_index']))
    
    # 3. Year-based auxiliaries from Lục Cát (Khôi/Việt)
    wai_stars.update(place_khoi_viet(year_can_chi['can_index']))
    
    # 4. Year-based auxiliaries from Lục Sát (Kình/Đà)
    wai_stars.update(place_kinh_da(year_can_chi['can_index']))
    
    # 5. Other Year-based stars (Mã, Hồng, Đào, ...)
    wai_stars.update(place_year_other_stars(year_can_chi['can_index'], year_can_chi['chi_index']))
    
    # 6. Tuần Triệt (Year Can Chi)
    tuan_triet = place_tuan_triet(year_can_chi['can_index'], year_can_chi['chi_index'])
    wai_stars.update(tuan_triet)
    tuan_triet_info = get_tuan_triet_info(year_can_chi['can_index'], year_can_chi['chi_index'])
    
    # Place Month-based stars if month is available
    if month:
        # Tả Phụ / Hữu Bật
        wai_stars.update(place_ta_huu(month))
        # Long Đức, Nguyệt Đức, Thương, Sứ...
        wai_stars.update(place_month_other_stars(month))
        
    # Build positions (without Mệnh/Thân markers)
    # We use a dummy cung_map since we don't know Mệnh position
    cung_map = {}
    for i in range(12):
        cung_map[i] = '' # Unknown palace names
        
    # Tứ Hóa (Year Can based)
    tu_hoa = apply_tu_hoa(year_can_chi['can_index'], wai_stars)
    
    positions = build_positions(wai_stars, tu_hoa, cung_map, -1, -1, tuan_triet_info)
    
    # Get Nap Am
    nap_am = get_nap_am(year_can_chi['can_index'], year_can_chi['chi_index'])

    # Get Than Chu (depends on Year Chi)
    # Menh Chu depends on Menh position so it remains unknown
    from stars.bo_sung_placer import get_than_chu
    than_chu = get_than_chu(year_can_chi['chi_index'])
    
    return {
        'solar_date': {'day': '?', 'month': month or '?', 'year': year},
        'lunar_date': lunar,
        'hour': None,
        'hour_name': '?',
        'gender': gender,
        'year_can_chi': year_can_chi,
        'month_can_chi': month_can_chi,
        'day_can_chi': {'full': 'N/A'},
        'hour_can_chi': {'full': 'N/A'},
        'nap_am': nap_am,
        'menh_position': -1,
        'menh_name': '?',
        'than_position': -1,
        'than_name': '?',
        'cuc': {'name': '?', 'number': 0},
        'tu_vi_position': -1,
        'chinh_tinh': {},
        'all_stars': wai_stars,
        'tu_hoa': tu_hoa,
        'cung_map': cung_map,
        'positions': positions,
        'tuan_triet': tuan_triet_info,
        'menh_chu': '?',
        'than_chu': than_chu,
        'is_partial': True
    }
