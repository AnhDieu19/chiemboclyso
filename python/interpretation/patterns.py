"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CÁCH CỤC RECOGNITION (NHẬN DIỆN CÁCH CỤC)                 ║
║                    Patterns in Tử Vi Charts - Nam Phái                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Cách cục là các mẫu sao đặc biệt, quyết định vận mệnh tổng quát            ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from data.star_brightness import get_star_brightness


# ═══════════════════════════════════════════════════════════════════════════════
# ĐỊNH NGHĨA CÁC CÁCH CỤC
# ═══════════════════════════════════════════════════════════════════════════════

CACH_CUC_DEFINITIONS = {
    # === CÁCH CỤC ĐẶC BIỆT (VIDEO KNOWLEDGE) ===
    'phuong_lam_cao_cuong': {
        'name': 'Phượng Lãm Cao Cương',
        'stars_required': ['Thiên Lương'],
        'condition': 'star_at_specific_position',
        'params': {'position_idx': 0}, # 0 = Tý
        'description': 'Thiên Lương tạ thủ cung Tý',
        'meaning': 'Tượng chim Phượng hoàng đậu trên núi cao. Thông minh xuất chúng, có tài làm thầy, làm cố vấn, địa vị cao trong xã hội, được kính trọng.',
        'nature': 'Đại Cát',
        'scope': 'menh'
    },
    # === CÁCH CỤC ĐẸP ===
    'tu_phu_trieu_vien': {
        'name': 'Tử Phủ Triều Viên',
        'stars_required': ['Tử Vi', 'Thiên Phủ'],
        'condition': 'same_palace_or_opposite',
        'description': 'Tử Vi và Thiên Phủ đồng cung hoặc đối chiếu',
        'meaning': 'Cách cục của bậc vương giả, quyền quý, thành công lớn trong sự nghiệp',
        'nature': 'Đại Cát',
        'scope': 'menh'
    },
    'nhat_nguyet_tinh_minh': {
        'name': 'Nhật Nguyệt Tịnh Minh',
        'stars_required': ['Thái Dương', 'Thái Âm'],
        'condition': 'both_mieu_vuong',
        'description': 'Thái Dương và Thái Âm đều ở Miếu hoặc Vượng',
        'meaning': 'Cuộc đời sáng sủa, thuận lợi, danh tiếng, được mọi người yêu quý',
        'nature': 'Đại Cát',
        'scope': 'menh'
    },
    'song_loc_trieu_vien': {
        'name': 'Song Lộc Triều Viên',
        'stars_required': ['Lộc Tồn'],
        'condition': 'with_hoa_loc',
        'description': 'Lộc Tồn và Hóa Lộc cùng tam hợp hoặc đồng cung với Mệnh',
        'meaning': 'Giàu có, tài lộc dồi dào, không lo cơm áo',
        'nature': 'Đại Cát'
    },
    'loc_ma_giao_tri': {
        'name': 'Lộc Mã Giao Trì',
        'stars_required': ['Lộc Tồn', 'Thiên Mã'],
        'condition': 'same_palace_or_tam_hop',
        'description': 'Lộc Tồn gặp Thiên Mã',
        'meaning': 'Phát tài nhờ di chuyển, kinh doanh, xuất ngoại thành công',
        'nature': 'Cát'
    },
    'ta_huu_giap': {
        'name': 'Tả Hữu Giáp',
        'stars_required': ['Tả Phụ', 'Hữu Bật'],
        'condition': 'flanking_menh',
        'description': 'Tả Phụ và Hữu Bật kẹp Cung Mệnh',
        'meaning': 'Được quý nhân phò tá suốt đời, thành công trong sự nghiệp',
        'nature': 'Cát'
    },
    'xuong_khuc_giap': {
        'name': 'Xương Khúc Giáp',
        'stars_required': ['Văn Xương', 'Văn Khúc'],
        'condition': 'flanking_menh',
        'description': 'Văn Xương và Văn Khúc kẹp Cung Mệnh',
        'meaning': 'Thông minh, học giỏi, có tài văn chương, nghệ thuật',
        'nature': 'Cát'
    },
    'khoi_viet_giap': {
        'name': 'Khôi Việt Giáp',
        'stars_required': ['Thiên Khôi', 'Thiên Việt'],
        'condition': 'flanking_menh',
        'description': 'Thiên Khôi và Thiên Việt kẹp Cung Mệnh',
        'meaning': 'Có quý nhân phù hộ, gặp may mắn trong những lúc khó khăn',
        'nature': 'Cát'
    },
    
    # === CÁCH CỤC TRUNG TÍNH/XẤU ===
    'sat_pha_liem_tham': {
        'name': 'Sát Phá Liêm Tham',
        'stars_required': ['Thất Sát', 'Phá Quân', 'Liêm Trinh', 'Tham Lang'],
        'condition': 'two_or_more_present',
        'description': 'Có từ 2 sao trở lên trong nhóm Sát Phá Liêm Tham',
        'meaning': 'Đời sống biến động, nhiều thử thách, nhưng nếu vượt qua sẽ thành công lớn. (Chỉ tính khi sao thủ Mệnh)',
        'nature': 'Hung hóa Cát',
        'scope': 'menh'
    },
    'khong_kiep_hiep': {
        'name': 'Không Kiếp Hiệp',
        'stars_required': ['Địa Không', 'Địa Kiếp'],
        'condition': 'same_palace',
        'description': 'Địa Không và Địa Kiếp đồng cung',
        'meaning': 'Hay thất bại trước khi thành công, tư tưởng đột phá, không theo lối mòn',
        'nature': 'Hung hóa Cát'
    },
    'kinh_da_hiep': {
        'name': 'Kình Đà Hiệp',
        'stars_required': ['Kinh Dương', 'Đà La'],
        'condition': 'flanking_menh',
        'description': 'Kinh Dương và Đà La kẹp Cung Mệnh',
        'meaning': 'Dễ gặp tai nạn, xung đột, cần cẩn thận trong giao tiếp',
        'nature': 'Hung'
    },
    'hoa_linh_giap': {
        'name': 'Hỏa Linh Giáp',
        'stars_required': ['Hỏa Tinh', 'Linh Tinh'],
        'condition': 'same_palace_or_flanking',
        'description': 'Hỏa Tinh và Linh Tinh đồng cung hoặc kẹp',
        'meaning': 'Nóng nảy, vội vàng, hay gặp biến cố bất ngờ',
        'nature': 'Hung'
    },
    'tu_hoa_ky_menh': {
        'name': 'Hóa Kỵ Thủ Mệnh',
        'stars_required': [],
        'condition': 'hoa_ky_in_menh',
        'description': 'Hóa Kỵ nằm tại Cung Mệnh',
        'meaning': 'Dễ gặp trở ngại và thị phi trong cuộc sống. Cần cẩn thận đề phòng tiểu nhân, tránh nóng vội trong quyết định. Nên tu tâm dưỡng tính, làm nhiều việc thiện để hóa giải',
        'nature': 'Hung (có thể hóa giải)',
        'scope': 'menh'
    }
}


def detect_patterns(chart: dict) -> list:
    """
    Nhận diện các cách cục trong lá số (Dynamic & Scoped Logic)
    
    Args:
        chart: Dữ liệu lá số từ generate_birth_chart()
        
    Returns:
        list các cách cục được nhận diện
    """
    patterns_found = []
    positions = chart.get('positions', {})
    menh_pos = chart.get('menh_position', 0)
    tu_hoa = chart.get('tu_hoa', {})
    all_stars = chart.get('all_stars', {})
    
    # Helper functions
    def get_star_name(star):
        """Lấy tên sao từ string hoặc dict"""
        if isinstance(star, dict):
            return star.get('name', '')
        return star
    
    def get_stars_at(pos):
        """Lấy danh sách tên sao tại một cung"""
        stars = positions.get(pos, {}).get('stars', [])
        return [get_star_name(s) for s in stars]
    
    def star_position(star):
        return all_stars.get(star)
    
    def is_mieu_or_vuong(star, pos):
        brightness = get_star_brightness(star, pos)
        return brightness['code'] in ['M', 'V']
    
    def tam_hop_positions(pos):
        """Lấy các cung tam hợp (cách 4 cung)"""
        return [(pos + 4) % 12, (pos + 8) % 12]
    
    def has_bad_stars(pos):
        """Kiểm tra cung có bị Sát Tinh/Tuần/Triệt/Kỵ xâm phạm không"""
        # 1. Tuần/Triệt
        pos_data = positions.get(pos, {})
        if pos_data.get('in_tuan') or pos_data.get('in_triet'): return True
        
        # 2. Hóa Kỵ
        hk_pos = tu_hoa.get('Hóa Kỵ', {}).get('position')
        if hk_pos == pos: return True
        
        # 3. Sát tinh hạng nặng (Lục Sát + Hình)
        bad_list = ['Địa Không', 'Địa Kiếp', 'Kinh Dương', 'Đà La', 'Linh Tinh', 'Hỏa Tinh', 'Thiên Hình']
        stars_at_pos = get_stars_at(pos)
        if any(s in stars_at_pos for s in bad_list): return True
        
        return False
    
    menh_stars = get_stars_at(menh_pos)
    
    # Loop dynamic qua definitions
    for key, definition in CACH_CUC_DEFINITIONS.items():
        required = definition.get('stars_required', [])
        condition = definition.get('condition', '')
        scope = definition.get('scope', 'global')
        stars_found = []
        is_match = False
        
        # 1. SCOPE CHECK
        # Nếu scope là 'menh', bắt buộc các sao nòng cốt phải nằm trong Mệnh
        # hoặc liên quan trực tiếp Mệnh (tuỳ logic condition bên dưới)
        if scope == 'menh':
            if key == 'sat_pha_liem_tham':
                 # Sát Phá Tham: Bắt buộc ít nhất 1 sao nằm trong Mệnh
                 intersect = [s for s in required if s in menh_stars]
                 if not intersect: continue
            elif key in ['tu_phu_trieu_vien', 'nhat_nguyet_tinh_minh']:
                 # Các cách cục này yêu cầu tính chất chiếu về Mệnh mạnh mẽ
                 # Logic bên dưới sẽ handle vị trí, nhưng ở đây ta check sơ bộ
                 pass
            elif key == 'tu_hoa_ky_menh':
                 pass

        # 2. CONDITION CHECK
        if condition == 'same_palace_or_opposite':
            if len(required) == 2:
                s1, s2 = required
                p1, p2 = star_position(s1), star_position(s2)
                if p1 is not None and p2 is not None:
                    if (p1 == p2) or (abs(p1 - p2) == 6):
                        # Scope check additional
                        if scope == 'menh':
                             # Must involve Menh position (at Menh or opposite Menh)
                             if p1 != menh_pos and p1 != (menh_pos+6)%12:
                                 continue
                        is_match = True
                        stars_found = required

        elif condition == 'both_mieu_vuong':
            if len(required) == 2:
                s1, s2 = required
                p1, p2 = star_position(s1), star_position(s2)
                if p1 is not None and p2 is not None:
                    if is_mieu_or_vuong(s1, p1) and is_mieu_or_vuong(s2, p2):
                         # Check bad stars (Phá cách)
                         if has_bad_stars(p1) or has_bad_stars(p2):
                             continue
                             
                         if scope == 'menh':
                             # Must be in Menh or Tam Hop/Chieu
                             valid_pos = tam_hop_positions(menh_pos) + [menh_pos, (menh_pos+6)%12]
                             if p1 not in valid_pos or p2 not in valid_pos:
                                 continue
                         is_match = True
                         stars_found = required

        elif condition == 'with_hoa_loc':
             lt_pos = star_position('Lộc Tồn')
             hl = tu_hoa.get('Hóa Lộc', {})
             hl_pos = hl.get('position')
             if lt_pos is not None and hl_pos is not None:
                 tam_hop = tam_hop_positions(menh_pos) + [menh_pos]
                 if lt_pos in tam_hop and hl_pos in tam_hop:
                     is_match = True
                     stars_found = ['Lộc Tồn', hl.get('star', '')]

        elif condition == 'same_palace_or_tam_hop':
            if len(required) == 2:
                s1, s2 = required
                p1, p2 = star_position(s1), star_position(s2)
                if p1 is not None and p2 is not None:
                    if p1 == p2 or p2 in tam_hop_positions(p1):
                         is_match = True
                         stars_found = required

        elif condition == 'flanking_menh':
            if len(required) == 2:
                s1, s2 = required
                p1, p2 = star_position(s1), star_position(s2)
                if p1 is not None and p2 is not None:
                    if (p1 == (menh_pos - 1) % 12 and p2 == (menh_pos + 1) % 12) or \
                       (p1 == (menh_pos + 1) % 12 and p2 == (menh_pos - 1) % 12):
                        is_match = True
                        stars_found = required

        elif condition == 'same_palace':
            if len(required) == 2:
                s1, s2 = required
                p1, p2 = star_position(s1), star_position(s2)
                if p1 is not None and p2 is not None and p1 == p2:
                    is_match = True
                    stars_found = required
        
        elif condition == 'same_palace_or_flanking':
             if len(required) == 2:
                s1, s2 = required
                p1, p2 = star_position(s1), star_position(s2)
                # Logic for Hỏa Linh: Đồng cung hoặc giáp Mệnh?
                # Definition says: "đồng cung hoặc kẹp". 
                # Nếu kẹp thì là kẹp Mệnh? Or kẹp chính tinh? Assuming kẹp Mệnh like others.
                if p1 is not None and p2 is not None:
                    is_same = (p1 == p2)
                    is_flanking_menh = (
                        (p1 == (menh_pos - 1) % 12 and p2 == (menh_pos + 1) % 12) or 
                        (p1 == (menh_pos + 1) % 12 and p2 == (menh_pos - 1) % 12)
                    )
                    if is_same or is_flanking_menh:
                        is_match = True
                        stars_found = required

        elif condition == 'two_or_more_present':
            # Logic for Sát Phá Tham
            # Ở bước Scope check đã lọc rồi.
            # Giờ chỉ cần collect stars thôi.
            present = [s for s in required if s in menh_stars]
            # Nếu scope != menh (ví dụ cách cục khác dùng condition này), ta cần logic tổng quát hơn
            # Nhưng hiện tại chỉ dùng cho SPT scoped menh.
            if len(present) >= 1: # Chấp nhận 1 sao thủ mệnh là đủ tính chất (vd Liêm Trinh thủ mệnh)
                # Tuy nhiên label là "Sát Phá Liêm Tham", user có thể confuse.
                # User complaint: "Máy thấy trong lá số có bộ sao... nhưng tự động bốc vào".
                # Nếu Mệnh User là Thiên Lương, thì present sẽ là Empty. -> Correct.
                is_match = True
                stars_found = present

        elif condition == 'hoa_ky_in_menh':
            hk_pos = tu_hoa.get('Hóa Kỵ', {}).get('position')
            if hk_pos == menh_pos:
                is_match = True
                stars_found = ['Hóa Kỵ']

        elif condition == 'star_at_specific_position':
            # Check if required star is at specific position
            params = definition.get('params', {})
            target_pos = params.get('position_idx')
            
            if target_pos is not None:
                # If scope is 'menh', we also require Menh to be at this position?
                # Usually Phượng Lãm Cao Cương means Thien Luong at Ty, and Menh is at Ty (Thien Luong thu Menh).
                # So verify Menh pos first if scope is menh.
                if scope == 'menh' and menh_pos != target_pos:
                    pass # Not applicable
                else:
                    # Check if star exists at target_pos
                    s_name = required[0] 
                    p = star_position(s_name)
                    if p == target_pos:
                        is_match = True
                        stars_found = required

        if is_match:
            patterns_found.append({
                **definition,
                'stars_found': stars_found
            })
            
    return patterns_found


def summarize_patterns(patterns: list) -> dict:
    """
    Tổng hợp các cách cục đã nhận diện
    
    Returns:
        dict với thống kê và đánh giá tổng quát
    """
    if not patterns:
        return {
            'count': 0,
            'cat_count': 0,
            'hung_count': 0,
            'overall': 'Không có cách cục đặc biệt',
            'patterns': []
        }
    
    cat_count = sum(1 for p in patterns if 'Cát' in p.get('nature', ''))
    hung_count = sum(1 for p in patterns if 'Hung' in p.get('nature', ''))
    
    if cat_count >= 3:
        overall = 'Lá số có nhiều cách cục đẹp - Đại Cát'
    elif cat_count >= 2 and hung_count <= 1:
        overall = 'Lá số tốt với nhiều điểm sáng'
    elif hung_count >= 2:
        overall = 'Lá số có thử thách cần vượt qua'
    else:
        overall = 'Lá số cân bằng, tùy thuộc nỗ lực cá nhân'
    
    return {
        'count': len(patterns),
        'cat_count': cat_count,
        'hung_count': hung_count,
        'overall': overall,
        'patterns': patterns
    }
