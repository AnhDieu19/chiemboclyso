"""
API Adapters
Convert internal data structures to API Specification format (v1)
"""

from data import DIA_CHI
from data.star_nature import classify_star

def safe_get(d, keys, default=None):
    """
    Safely get nested dictionary value
    keys: string 'a.b.c' or list ['a', 'b', 'c']
    """
    if isinstance(keys, str):
        keys = keys.split('.')
    
    current = d
    for k in keys:
        if isinstance(current, dict):
            current = current.get(k)
        else:
            return default
        if current is None:
            return default
    return current


MAIN_STARS = ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh',
              'Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 'Thất Sát', 'Phá Quân']

# Hardcoded list for Vong Truong Sinh
TRUONG_SINH_STARS = ['Trường Sinh', 'Mộc Dục', 'Quan Đới', 'Lâm Quan', 'Đế Vượng', 
                     'Suy', 'Bệnh', 'Tử', 'Mộ', 'Tuyệt', 'Thai', 'Dưỡng']

def adapter_chart_response(internal_chart: dict, internal_interpretation: dict = None) -> dict:
    """
    Convert internal chart structure to API v1 format
    """
    
    # 1. Basic Info
    # Safely access nested keys using helper or direct .get checks
    
    # helper for dates
    lunar_date = internal_chart.get('lunar_date', {})
    year_can_chi_full = safe_get(internal_chart, 'year_can_chi.full', 'N/A')
    
    basic_info = {
        "lunar_date_str": f"{lunar_date.get('day', '?')}/{lunar_date.get('month', '?')}/{year_can_chi_full.split(' ')[-1]}", 
        "can_chi_nam": year_can_chi_full,
        "can_chi_thang": safe_get(internal_chart, 'month_can_chi.full', 'N/A'),
        "can_chi_ngay": safe_get(internal_chart, 'day_can_chi.full', 'N/A'),
        "can_chi_gio": safe_get(internal_chart, 'hour_can_chi.full', 'N/A'),
        "menh_chu": internal_chart.get('nap_am', 'N/A'),
        "nap_am": internal_chart.get('nap_am', 'N/A'),
        "cuc": safe_get(internal_chart, 'cuc.name', 'N/A'),
        "menh_chu_star": internal_chart.get('menh_chu', 'N/A'),
        "than_chu_star": internal_chart.get('than_chu', 'N/A')
    }
    
    # 2. Thien Ban
    thien_ban = {
        "menh_tai_vi": internal_chart.get('menh_name', 'N/A'),
        "than_tai_vi": internal_chart.get('than_name', 'N/A')
    }
    
    # 3. Dia Ban (12 Cung)
    dia_ban = []
    positions = internal_chart.get('positions', {})
    
    # Define star categorization helper
    # Use default args to bind global constants to local scope to avoid closure issues
    def categorize_stars(stars, MAIN_STARS=MAIN_STARS, TRUONG_SINH_STARS=TRUONG_SINH_STARS):
        chinh_tinh = []
        vong_truong_sinh = []
        # Note: MAIN_STARS and TRUONG_SINH_STARS are captured from default args
        
        phu_tinh_tot = [] # Initialize explicit lists for clarity
        phu_tinh_xau = []

        for s in stars:
            s_name = s.get('name', '')
            s_bright = s.get('brightness', '')
            
            # Create star object with full visual properties
            star_obj = {
                "name": s_name, 
                "brightness": s_bright,
                "color": s.get('color'),
                "css_class": s.get('css_class'),
                "element": s.get('element')
            }
            
            if s_name in MAIN_STARS:
                chinh_tinh.append(star_obj)
            elif s_name in TRUONG_SINH_STARS:
                vong_truong_sinh.append(star_obj)
            else:
                # Use centralized classification
                nature = classify_star(s_name)
                if nature == 'bad':
                    phu_tinh_xau.append(star_obj)
                else:
                    phu_tinh_tot.append(star_obj)
                
        return chinh_tinh, phu_tinh_tot, phu_tinh_xau, vong_truong_sinh

    for i in range(12):
        pos_data = positions.get(i, {})
        stars = pos_data.get('stars', [])
        
        chinh_tinh, phu_tinh_tot, phu_tinh_xau, vong_truong_sinh = categorize_stars(stars)
        
        # Inject Tu Hoa as stars
        for h in pos_data.get('hoa', []):
            # h = {'name': 'Hóa Khoa', 'star': 'Vũ Khúc'}
            # We add "Hóa Khoa" to phu_tinh
            # Tu Hoa is always Good? Kinda, except Ky.
            # But usually we display them separately or with the star.
            # Here we just append to phu_tinh_tot for display purposes
            phu_tinh_tot.append({
                "name": h.get('name', ''), 
                "brightness": "", 
                "associated_with": h.get('star', ''),
                "color": "#e74c3c" if h.get('name') == 'Hóa Kỵ' else "#f1c40f", # Basic coloring for Tu Hoa
                "css_class": "star-hoa-ky" if h.get('name') == 'Hóa Kỵ' else "star-tu-hoa",
                "element": "Thủy" if h.get('name') == 'Hóa Kỵ' else "Kim"
            })
        
        cung_obj = {
            "index": i + 1,
            "cung_name": pos_data.get('cung', ''),
            "dia_chi": pos_data.get('chi', ''),
            "is_than": pos_data.get('is_than', False),
            "is_menh": pos_data.get('is_menh', False),
            "chinh_tinh": chinh_tinh,
            "phu_tinh_tot": phu_tinh_tot,
            "phu_tinh_xau": phu_tinh_xau,
            "vong_truong_sinh": vong_truong_sinh,
            "tuan": pos_data.get('in_tuan', False),
            "triet": pos_data.get('in_triet', False),
            "dai_van": 0, # TODO: Map dai van start age
            "tieu_van": "", # TODO: Map tieu van year name
            "tieu_han_age": pos_data.get('tieu_han_age')
        }
        dia_ban.append(cung_obj)
        
    return {
        "status": "success",
        "data": {
            "basic_info": basic_info,
            "thien_ban": thien_ban,
            "dia_ban": dia_ban,
            "interpretation": internal_interpretation or {}
        }
    }
