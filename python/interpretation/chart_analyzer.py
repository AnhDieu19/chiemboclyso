"""
Interpretation Layer - Chart Analyzer
Comprehensive interpretation generation with detailed analysis
"""

from .meanings import STAR_MEANINGS, PALACE_MEANINGS, CHINH_TINH_MEANINGS
from .meanings import (
    get_star_meaning, get_star_in_palace_meaning,
    get_giap_meaning, get_phi_hoa_in_palace, get_than_cu_meaning
)
from .patterns import detect_patterns, summarize_patterns
# from .cach_cuc import detect_cach_cuc, generate_cach_cuc_interpretation


def get_star_nature(star: str) -> str:
    """Get the nature of a star"""
    if star in CHINH_TINH_MEANINGS:
        return 'Chính Tinh'
    meaning = STAR_MEANINGS.get(star, {})
    return meaning.get('nature', 'Trung')


def get_star_name(star) -> str:
    """Helper: Lấy tên sao từ string hoặc dict"""
    if isinstance(star, dict):
        return star.get('name', '')
    return star


def analyze_star_combination(stars: list, palace_name: str) -> dict:
    """Analyze star combinations in a palace"""
    analysis = {
        'strength': 'Trung bình',
        'key_stars': [],
        'positive_aspects': [],
        'negative_aspects': [],
        'combination_effects': []
    }
    
    chinh_tinh = []
    cat_tinh = []
    sat_tinh = []
    
    for star_item in stars:
        star = get_star_name(star_item)
        if star in CHINH_TINH_MEANINGS:
            chinh_tinh.append(star)
            meaning = CHINH_TINH_MEANINGS[star]
            analysis['positive_aspects'].append(meaning.get('positive', ''))
            if meaning.get('negative'):
                analysis['negative_aspects'].append(meaning.get('negative', ''))
        elif star in STAR_MEANINGS:
            meaning = STAR_MEANINGS[star]
            nature = meaning.get('nature', '')
            if nature in ['Cát', 'Đại Cát']:
                cat_tinh.append(star)
                analysis['positive_aspects'].append(meaning.get('effect', ''))
            elif nature in ['Sát', 'Hung']:
                sat_tinh.append(star)
                analysis['negative_aspects'].append(meaning.get('effect', ''))
    
    analysis['key_stars'] = chinh_tinh
    
    # Determine overall strength
    cat_count = len(chinh_tinh) + len(cat_tinh)
    sat_count = len(sat_tinh)
    
    if cat_count >= 4 and sat_count <= 1:
        analysis['strength'] = 'Rất tốt'
    elif cat_count >= 3 and sat_count <= 2:
        analysis['strength'] = 'Tốt'
    elif sat_count >= 4:
        analysis['strength'] = 'Khó khăn'
    elif sat_count >= 3 and cat_count <= 1:
        analysis['strength'] = 'Nhiều thử thách'
    
    # Check special combinations
    star_names = [get_star_name(s) for s in stars]
    star_set = set(star_names)
    
    # Tử Phủ Vũ Tướng
    if {'Tử Vi', 'Thiên Phủ'} & star_set:
        analysis['combination_effects'].append('Có sao Đế (Tử Vi/Thiên Phủ) - quyền quý, sung túc')
    
    # Sát Phá Liêm Tham
    if len({'Thất Sát', 'Phá Quân', 'Liêm Trinh', 'Tham Lang'} & star_set) >= 2:
        analysis['combination_effects'].append('Sát Phá Liêm Tham hội tụ - đời sống biến động, cần mạnh mẽ')
    
    # Tả Hữu giáp
    if 'Tả Phụ' in star_set or 'Hữu Bật' in star_set:
        analysis['combination_effects'].append('Có Tả Hữu - được quý nhân phò tá')
    
    # Song Lộc
    if 'Lộc Tồn' in star_set:
        analysis['combination_effects'].append('Có Lộc Tồn - tài lộc dồi dào')
    
    # Thiên Mã hội
    if 'Thiên Mã' in star_set and 'Lộc Tồn' in star_set:
        analysis['combination_effects'].append('Lộc Mã giao trì - phát tài nhờ di chuyển, kinh doanh')
    
    # Kình Đà Hỏa Linh
    if len({'Kinh Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh'} & star_set) >= 2:
        analysis['combination_effects'].append('Nhiều Sát tinh hội tụ - cần cẩn thận tai nạn, xung đột')
    
    # Không Kiếp
    if 'Địa Không' in star_set or 'Địa Kiếp' in star_set:
        analysis['combination_effects'].append('Có Không Kiếp - dễ thất bại rồi thành công, tư tưởng đột phá')
    
    return analysis

def check_special_combinations(stars: list, palace_name: str, modifiers: list = []) -> list:
    """Check for special star combinations that defy normal rules"""
    # Extract star names from dicts if necessary
    star_names = [s.get('name') if isinstance(s, dict) else s for s in stars]
    star_set = set(star_names)
    special_effects = []
    
    # 1. Thiên Đồng + Hỏa Tinh (Phản vi kỳ cách) tại Thìn/Tuất/Sửu/Mùi
    # Thiên Đồng hãm gặp Hỏa Tinh -> Kích phát
    if 'Thiên Đồng' in star_set and ('Hỏa Tinh' in star_set or 'Linh Tinh' in star_set):
        # Check cung Thìn/Tuất (assumed from implementation context or generalized)
        # For simplicity, if Thien Dong is Ham (usually present logic checks brightness), 
        # but here we emphasize the combination.
        special_effects.append('Thiên Đồng gặp Hỏa/Linh: Phản vi kỳ cách - trở nên năng động, giỏi kỹ thuật/công nghệ, làm việc nhanh nhạy.')
        
    # 2. Cơ Âm + Tuần/Triệt + Không Kiếp (Cung Thân/Tài Bạch)
    if 'Thiên Cơ' in star_set and 'Thái Âm' in star_set:
        if 'tuan' in modifiers or 'triet' in modifiers:
            if 'Địa Không' in star_set or 'Địa Kiếp' in star_set:
                special_effects.append('Cơ Âm gặp Tuần/Triệt kết hợp Không/Kiếp: Đây là cách cục "phá rồi mới xây". Tiền bạc giai đoạn tiền vận (trước 35 tuổi) thường bế tắc, khó tụ tài. Tuy nhiên, nhờ Không Kiếp đắc địa nên có khả năng bùng nổ mạnh mẽ về tài chính (bạo phát) ở giai đoạn hậu vận.')
            else:
                special_effects.append('Cơ Âm gặp Tuần/Triệt: Tình cảm và tài lộc có giai đoạn trắc trở, cần kiên trì.')

    # 3. Tử Vi + Tuần/Triệt
    if 'Tử Vi' in star_set and ('tuan' in modifiers or 'triet' in modifiers):
        special_effects.append('Tử Vi gặp Tuần/Triệt: Như vua mất ngôi, quyền lực bị giảm sút. Trong gia đạo dễ có sự xa cách hoặc bất đồng quan điểm.')

    # 4. Thiên Lương + Linh Tinh/Tang Môn (Mệnh)
    # Check if this is applied to Mệnh palace generally or interpret specially
    if 'Thiên Lương' in star_set and ('Linh Tinh' in star_set or 'Tang Môn' in star_set):
        special_effects.append('Thiên Lương hội Linh/Tang: Nội tâm hay lo âu, suy nghĩ nhiều, đôi khi cảm thấy cô độc ngay cả khi giữa đám đông. Có lòng tự trọng cao.')

    return special_effects


def interpret_palace_detailed(palace_name: str, stars: list, hoa_list: list, tuan: bool = False, triet: bool = False) -> dict:
    """Detailed interpretation for a single palace with modifiers"""
    palace_info = PALACE_MEANINGS.get(palace_name, {})
    analysis = analyze_star_combination(stars, palace_name)
    
    modifiers = []
    if tuan: modifiers.append('tuan')
    if triet: modifiers.append('triet')
    
    # Special combinations
    special_effects = check_special_combinations(stars, palace_name, modifiers)
    if special_effects:
        analysis['combination_effects'].extend(special_effects)

    # Basic Tuần/Triệt impact
    tt_impact = []
    if tuan or triet:
        tt_str = "Tuần" if tuan else "Triệt"
        if tuan and triet: tt_str = "Tuần - Triệt"
        
        # Logic: Sáng -> Kém đi, Tối -> Khá lên
        # We rely on overall strength. 
        if analysis['strength'] in ['Rất tốt', 'Tốt']:
             analysis['strength'] = 'Khá'
             tt_impact.append(f"Gặp {tt_str}: Giảm bớt sự thuận lợi ban đầu, cần nỗ lực nhiều hơn.")
        elif analysis['strength'] in ['Xấu', 'Rất xấu']:
             analysis['strength'] = 'Trung bình' 
             tt_impact.append(f"Gặp {tt_str}: Hóa giải bớt cái xấu, trở nên bình ổn hơn (Phản vi kỳ cách).")
        else:
             tt_impact.append(f"Gặp {tt_str}: Gây ra sự trắc trở, chậm muộn trong giai đoạn đầu.")
             
        analysis['combination_effects'].extend(tt_impact)
    
    # Get Tứ Hóa effects in this palace
    tu_hoa_effects = []
    for hoa in hoa_list:
        hoa_name = hoa.get('name', '')
        hoa_star = hoa.get('star', '')
        if hoa_name == 'Hóa Lộc':
            tu_hoa_effects.append(f'{hoa_star} Hóa Lộc - tài lộc, may mắn trong {palace_info.get("governs", palace_name)}')
        elif hoa_name == 'Hóa Quyền':
            tu_hoa_effects.append(f'{hoa_star} Hóa Quyền - quyền lực, kiểm soát tốt về {palace_info.get("governs", palace_name)}')
        elif hoa_name == 'Hóa Khoa':
            tu_hoa_effects.append(f'{hoa_star} Hóa Khoa - danh tiếng, học thức trong {palace_info.get("governs", palace_name)}')
        elif hoa_name == 'Hóa Kỵ':
            tu_hoa_effects.append(f'{hoa_star} Hóa Kỵ - trở ngại, cần cẩn thận về {palace_info.get("governs", palace_name)}')
    
    # Generate detailed interpretation
    interpretation_parts = []
    
    if analysis['key_stars']:
        stars_str = ', '.join(analysis['key_stars'])
        interpretation_parts.append(f"Chính tinh chủ đạo: {stars_str}.")
    
    if analysis['positive_aspects'][:2]:
        interpretation_parts.append(' '.join(analysis['positive_aspects'][:2]))
    
    if analysis['combination_effects']:
        interpretation_parts.extend(analysis['combination_effects'])
    
    if tu_hoa_effects:
        interpretation_parts.extend(tu_hoa_effects)
    
    if analysis['negative_aspects'] and analysis['strength'] in ['Khó khăn', 'Nhiều thử thách']:
        interpretation_parts.append(f"Lưu ý: {analysis['negative_aspects'][0]}")
    
    return {
        'palace_info': palace_info,
        'strength': analysis['strength'],
        'key_stars': analysis['key_stars'],
        'interpretation': ' '.join(interpretation_parts) if interpretation_parts else f"Cung {palace_name} ở mức trung bình, không có sao chủ đạo nổi bật.",
        'tu_hoa_effects': tu_hoa_effects,
        'combination_effects': analysis['combination_effects']
    }


def generate_overall_interpretation(chart: dict) -> dict:
    """Generate comprehensive interpretation for a chart"""
    positions = chart.get('positions', {})
    menh_pos = chart.get('menh_position', 0)
    than_pos = chart.get('than_position', 0)
    cung_map = chart.get('cung_map', {})
    
    # Basic info
    basic_info = {
        'year_can_chi': chart.get('year_can_chi', {}).get('full', ''),
        'cuc': chart.get('cuc', {}).get('name', ''),
        'menh_cung': cung_map.get(menh_pos, 'Mệnh'),
        'than_cung': cung_map.get(than_pos, 'Thân'),
        'nap_am': chart.get('nap_am', ''),
        'menh_chi': chart.get('menh_name', ''),
        'than_chi': chart.get('than_name', ''),
        'menh_chu': chart.get('menh_chu', ''),
        'than_chu': chart.get('than_chu', '')
    }
    
    # Detailed Cung Mệnh interpretation
    menh_data = positions.get(menh_pos, {})
    menh_interp = interpret_palace_detailed(
        'Mệnh', 
        menh_data.get('stars', []), 
        menh_data.get('hoa', []),
        menh_data.get('in_tuan', False),
        menh_data.get('in_triet', False)
    )
    
    # Cung Thân interpretation
    than_data = positions.get(than_pos, {})
    than_interp = interpret_palace_detailed(
        'Thân', 
        than_data.get('stars', []), 
        than_data.get('hoa', []),
        than_data.get('in_tuan', False),
        than_data.get('in_triet', False)
    )
    
    # All 12 palace interpretations
    all_palaces = {}
    for i in range(12):
        pos_data = positions.get(i, {})
        cung_name = pos_data.get('cung', '')
        if cung_name:
            all_palaces[cung_name] = interpret_palace_detailed(
                cung_name,
                pos_data.get('stars', []), 
                pos_data.get('hoa', []),
                pos_data.get('in_tuan', False),
                pos_data.get('in_triet', False)
            )
    
    # Key life aspects with detailed analysis
    life_aspects = {
        'su_nghiep': all_palaces.get('Quan Lộc', {}),
        'tai_chinh': all_palaces.get('Tài Bạch', {}),
        'hon_nhan': all_palaces.get('Phu Thê', {}),
        'suc_khoe': all_palaces.get('Tật Ách', {}),
        'con_cai': all_palaces.get('Tử Tức', {}),
        'gia_dinh': all_palaces.get('Điền Trạch', {}),
        'di_chuyen': all_palaces.get('Thiên Di', {})
    }
    
    # Tứ Hóa analysis
    tu_hoa = chart.get('tu_hoa', {})
    tu_hoa_analysis = []
    for hoa_name, hoa_info in tu_hoa.items():
        star = hoa_info.get('star', '')
        pos = hoa_info.get('position', 0)
        cung = cung_map.get(pos, '')
        if hoa_name == 'Hóa Lộc':
            tu_hoa_analysis.append(f"🌟 {star} Hóa Lộc tại cung {cung}: Tài lộc, may mắn và cơ hội đến từ lĩnh vực {PALACE_MEANINGS.get(cung, {}).get('governs', cung)}.")
        elif hoa_name == 'Hóa Quyền':
            tu_hoa_analysis.append(f"👑 {star} Hóa Quyền tại cung {cung}: Có quyền lực, kiểm soát trong {PALACE_MEANINGS.get(cung, {}).get('governs', cung)}.")
        elif hoa_name == 'Hóa Khoa':
            tu_hoa_analysis.append(f"📚 {star} Hóa Khoa tại cung {cung}: Danh tiếng, uy tín trong {PALACE_MEANINGS.get(cung, {}).get('governs', cung)}.")
        elif hoa_name == 'Hóa Kỵ':
            tu_hoa_analysis.append(f"⚠️ {star} Hóa Kỵ tại cung {cung}: Cần cẩn thận, tránh vội vàng trong {PALACE_MEANINGS.get(cung, {}).get('governs', cung)}.")
    
    # Overall fortune based on Cung Mệnh strength
    fortune_parts = []
    
    # Detect patterns (Cách Cục)
    patterns = detect_patterns(chart)
    patterns_summary = summarize_patterns(patterns)
    
    # Add pattern-based fortune
    if patterns_summary['cat_count'] >= 2:
        fortune_parts.append(f"Lá số có {patterns_summary['cat_count']} cách cục đẹp: {', '.join([p['name'] for p in patterns if 'Cát' in p.get('nature', '')][:3])}.")
    
    if menh_interp['strength'] in ['Rất tốt', 'Tốt']:
        fortune_parts.append("Lá số có cách cục tốt, chủ nhân có nhiều may mắn và quý nhân phù trợ.")
        fortune_parts.append("Cuộc đời phát triển thuận lợi, có cơ hội thành công trong sự nghiệp và tài chính.")
    elif menh_interp['strength'] == 'Trung bình':
        fortune_parts.append("Lá số ở mức trung bình, cần nỗ lực bản thân để đạt được thành công.")
        fortune_parts.append("Có cả thuận lợi và thử thách, quan trọng là biết cách tận dụng thời cơ.")
    else:
        fortune_parts.append("Lá số có nhiều thử thách, nhưng vượt qua sẽ đạt thành tựu.")
        fortune_parts.append("Cần kiên trì, cẩn thận trong quyết định, tránh nóng vội.")
    
    # Advice based on chart
    advice_parts = []
    if life_aspects.get('su_nghiep', {}).get('strength') in ['Rất tốt', 'Tốt']:
        advice_parts.append("Tập trung phát triển sự nghiệp, có khả năng thăng tiến cao.")
    if life_aspects.get('tai_chinh', {}).get('strength') in ['Rất tốt', 'Tốt']:
        advice_parts.append("Có tài vận tốt, nên đầu tư và tích lũy tài sản.")
    if life_aspects.get('suc_khoe', {}).get('strength') in ['Khó khăn', 'Nhiều thử thách']:
        advice_parts.append("Chú ý sức khỏe, nên khám định kỳ và tập thể dục đều đặn.")
    if life_aspects.get('hon_nhan', {}).get('strength') in ['Khó khăn', 'Nhiều thử thách']:
        advice_parts.append("Cần nhẫn nhịn trong tình cảm, tránh nóng giận, xung đột.")
    
    # Add pattern-based advice
    for p in patterns:
        if 'Hung' in p.get('nature', ''):
            advice_parts.append(f"Lưu ý cách cục {p['name']}: {p.get('meaning', '')}.")
            break
    
    if not advice_parts:
        advice_parts.append("Sống tích cực, nỗ lực không ngừng, và biết ơn những gì mình có.")
    
    # Detect Cách Cục đặc biệt từ module cach_cuc - DISABLED logic cũ
    # cach_cuc = detect_cach_cuc(chart)
    # cach_cuc_text = generate_cach_cuc_interpretation(cach_cuc)
    cach_cuc = []
    cach_cuc_text = ""
    
    return {
        'basic_info': basic_info,
        'menh_interpretation': menh_interp,
        'than_interpretation': than_interp,
        'all_palaces': all_palaces,
        'life_aspects': life_aspects,
        'tu_hoa_analysis': tu_hoa_analysis,
        'patterns': patterns,
        'patterns_summary': patterns_summary,
        'cach_cuc': cach_cuc,
        'cach_cuc_interpretation': cach_cuc_text,
        'fortune': ' '.join(fortune_parts),
        'advice': ' '.join(advice_parts)
    }


def get_detailed_star_interpretation(star_name: str, palace_name: str = None) -> dict:
    """Get detailed interpretation for a star using JSON meanings.
    
    Args:
        star_name: Name of the star
        palace_name: Optional - name of palace for in_palace meaning
        
    Returns:
        Dict with detailed interpretation
    """
    result = {
        'name': star_name,
        'basic': None,
        'detailed': None,
        'in_palace': None
    }
    
    # Get detailed meaning from JSON
    meaning = get_star_meaning(star_name)
    if meaning:
        result['basic'] = {
            'nature': meaning.get('nature', ''),
            'positive': meaning.get('positive', ''),
            'negative': meaning.get('negative', '')
        }
        result['detailed'] = meaning.get('detailed', '')
        
        # Get palace-specific meaning if available
        if palace_name:
            in_palace = get_star_in_palace_meaning(star_name, palace_name)
            if in_palace:
                result['in_palace'] = in_palace
    
    return result


def get_than_cu_interpretation(palace_name: str) -> dict:
    """Get detailed interpretation for Than (Body) palace position.
    
    Args:
        palace_name: Name of the palace where Than is located
        
    Returns:
        Dict with Than Cu interpretation
    """
    meaning = get_than_cu_meaning(palace_name)
    if meaning:
        return {
            'palace': palace_name,
            'title': meaning.get('title', f'Thân cư {palace_name}'),
            'personality': meaning.get('personality', ''),
            'description': meaning.get('description', ''),
            'career': meaning.get('career', []),
            'tendency': meaning.get('tendency', '')
        }
    return {'palace': palace_name, 'title': f'Thân cư {palace_name}'}


def analyze_giap_cung(left_stars: list, right_stars: list) -> list:
    """Analyze Giap (flanking) configuration for a palace.
    
    Args:
        left_stars: Stars in the left adjacent palace
        right_stars: Stars in the right adjacent palace
        
    Returns:
        List of applicable Giap meanings
    """
    giap_effects = []
    
    left_names = [s.get('name') if isinstance(s, dict) else s for s in left_stars]
    right_names = [s.get('name') if isinstance(s, dict) else s for s in right_stars]
    all_flank = set(left_names + right_names)
    
    # Check various Giap configurations
    giap_patterns = [
        (['Đà La'], 'Đà La'),
        (['Hóa Lộc'], 'Hóa Lộc'),
        (['Phá Quân'], 'Phá Quân'),
        (['Kinh Dương', 'Đà La'], None),
        (['Hỏa Tinh', 'Linh Tinh'], None),
        (['Địa Không', 'Địa Kiếp'], None),
        (['Tả Phụ', 'Hữu Bật'], None),
        (['Văn Xương', 'Văn Khúc'], None),
        (['Thiên Khôi', 'Thiên Việt'], None),
        (['Lộc Tồn', 'Thiên Mã'], None),
        (['Hồng Loan', 'Thiên Hỹ'], None),
        (['Tử Vi', 'Thiên Phủ'], None),
        (['Thái Dương', 'Thái Âm'], None),
    ]
    
    for pattern, single in giap_patterns:
        if single:
            # Single star giap
            if single in left_names or single in right_names:
                meaning = get_giap_meaning(single)
                if meaning:
                    giap_effects.append(meaning)
        else:
            # Pair giap - need one on each side or both present
            if len(set(pattern) & all_flank) >= 2:
                meaning = get_giap_meaning(pattern[0], pattern[1] if len(pattern) > 1 else None)
                if meaning:
                    giap_effects.append(meaning)
    
    return giap_effects


def get_phi_hoa_nam_interpretation(tu_hoa: dict, cung_map: dict) -> list:
    """Get interpretations for Phi Hoa (Flying Transformations) for the year.
    
    Args:
        tu_hoa: Tu Hoa dict from chart
        cung_map: Palace position mapping
        
    Returns:
        List of Phi Hoa interpretations
    """
    interpretations = []
    
    hoa_mapping = {
        'Hóa Lộc': 'phi_hoa_loc',
        'Hóa Quyền': 'phi_hoa_quyen', 
        'Hóa Khoa': 'phi_hoa_khoa',
        'Hóa Kỵ': 'phi_hoa_ky'
    }
    
    for hoa_name, hoa_info in tu_hoa.items():
        star = hoa_info.get('star', '')
        pos = hoa_info.get('position', 0)
        palace = cung_map.get(pos, '')
        
        hoa_type = hoa_mapping.get(hoa_name)
        if hoa_type:
            meaning = get_phi_hoa_in_palace(hoa_type, palace)
            if meaning:
                interpretations.append({
                    'hoa': hoa_name,
                    'star': star,
                    'palace': palace,
                    'meaning': meaning.get('meaning', ''),
                    'detail': meaning.get('detail', '')
                })
    
    return interpretations

