"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CÁCH CỤC ĐẶC BIỆT - TỬ VI NAM PHÁI                        ║
║                    Nhận diện và luận giải các cách cục quan trọng            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Cách cục là sự kết hợp đặc biệt của các sao trong lá số                    ║
║  Có thể là Cát (tốt), Hung (xấu), hoặc Trung tính                           ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# Danh sách 14 Chính Tinh
CHINH_TINH_LIST = [
    'Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 
    'Thiên Đồng', 'Liêm Trinh', 'Thiên Phủ', 'Thái Âm',
    'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương',
    'Thất Sát', 'Phá Quân'
]

# ═══════════════════════════════════════════════════════════════════════════════
# DANH SÁCH CÁCH CỤC ĐẶC BIỆT
# ═══════════════════════════════════════════════════════════════════════════════

CACH_CUC_LIST = {
    # ═══════════════════════════════════════════════════════════════════════════
    # CÁCH CỤC CÁT (TỐT)
    # ═══════════════════════════════════════════════════════════════════════════
    
    "tu_phu_vu_tuong": {
        "name": "Tử Phủ Vũ Tướng",
        "stars": ["Tử Vi", "Thiên Phủ", "Vũ Khúc", "Thiên Tướng"],
        "condition": "any_2_same_cung",
        "rank": "Đại Cát",
        "meaning": "Cách cục quý hiển, chủ quyền cao chức trọng, phú quý song toàn. Đại diện cho người lãnh đạo, cấp cao, tuổi trung niên (40-50).",
        "detail": "Đây là cách cục của những người có tư chất lãnh đạo, uy quyền. Tử Vi là Đế tinh, Thiên Phủ là Tài khố, Vũ Khúc chủ tài lộc, Thiên Tướng chủ ấn tín. Bốn sao này hội tụ tạo nên cách cục phú quý bậc nhất. Cốt cách anh hùng, tôn quý; có khả năng xây dựng, kiến thiết và duy trì trật tự xã hội; đại diện cho thời bình, sự ôn hòa và giàu sang.",
        "advice": "Nên phát huy tố chất lãnh đạo, giữ gìn đạo đức người quân tử, đừng kiêu ngạo.",
        "icon": "👑"
    },
    
    "phu_tuong_trieu_vien": {
        "name": "Phủ Tướng Triều Viên",
        "stars": ["Thiên Phủ", "Thiên Tướng"],
        "condition": "menh_hoi_tu",
        "rank": "Đại Cát",
        "meaning": "Thiên Phủ, Thiên Tướng hội chiếu về Mệnh. Chủ về tài lộc, sự nghiệp vững chắc, được quý nhân phù trợ. Đại diện cho người lãnh đạo, cấp cao.",
        "detail": "Thiên Phủ là kho trời, Thiên Tướng là ấn tín. Hai sao này hội về Mệnh (đặc biệt khi Mệnh Vô Chính Diệu) tạo cách cục giàu có, uy quyền. Cốt cách anh hùng, tôn quý; có khả năng xây dựng, kiến thiết và duy trì trật tự. Đại diện cho sự ổn định và giàu sang.",
        "advice": "Tận dụng sự giúp đỡ của quý nhân, phát triển sự nghiệp bền vững.",
        "icon": "🏦"
    },
    
    "sat_pha_tham": {
        "name": "Sát Phá Tham",
        "stars": ["Thất Sát", "Phá Quân", "Tham Lang"],
        "condition": "menh_hoi_tu",
        "rank": "Mạnh Mẽ",
        "meaning": "Bộ ba Sát Phá Tham hội tụ. Tính cách mạnh mẽ, quyết đoán, cuộc đời nhiều biến động. Đại diện cho tầng lớp binh biến, trẻ con (thích quậy phá).",
        "detail": "Thất Sát, Phá Quân, Tham Lang nằm ở Mệnh hoặc hội chiếu. Chủ về người có năng lực hành động, thích thử thách, dễ thành công trong môi trường biến động. Tính cách ngang tàn, quyết liệt, hành động theo cảm hứng; đại diện cho sự cạnh tranh, biến cố và thời loạn lạc. Phù hợp với võ nghiệp, kinh doanh mạo hiểm.",
        "advice": "Rèn luyện sự kiên nhẫn và đạo đức để thành công bền vững. Cần rèn luyện kỷ luật, tránh hành động bốc đồng gây hậu quả.",
        "icon": "⚔️"
    },
    
    "song_loc": {
        "name": "Song Lộc",
        "stars": ["Lộc Tồn"],  # + Hóa Lộc
        "condition": "loc_ton_with_hoa_loc",
        "rank": "Đại Cát",
        "meaning": "Hai Lộc hội tụ, tài lộc dồi dào, suốt đời không thiếu tiền.",
        "detail": "Lộc Tồn và Hóa Lộc cùng cung hoặc tam hợp. "
                  "Lộc Tồn là Chính Lộc (tài sản ổn định), Hóa Lộc là Hóa tinh (cơ hội kiếm tiền). "
                  "Người có Song Lộc tài chính dồi dào, nhiều nguồn thu nhập.",
        "advice": "Biết chia sẻ, làm từ thiện để tích đức.",
        "icon": "💰"
    },
    
    # ... (Keep other items) ...


    "loc_ma_giao_tri": {
        "stars": ["Lộc Tồn", "Thiên Mã"],
        "condition": "same_cung_or_tam_hop",
        "rank": "Cát",
        "meaning": "Lộc và Mã gặp nhau, tài lộc đến từ xa, kinh doanh xuất nhập khẩu tốt.",
        "detail": "Lộc Tồn gặp Thiên Mã, tài lộc liên quan đến di chuyển, đi xa. "
                  "Thích hợp kinh doanh vận chuyển, xuất nhập khẩu, du lịch.",
        "advice": "Nên tìm cơ hội ở xa hoặc làm việc liên quan đến di chuyển.",
        "icon": "🏇"
    },
    
    "ta_huu_giap_menh": {
        "name": "Tả Hữu Giáp Mệnh",
        "stars": ["Tả Phụ", "Hữu Bật"],
        "condition": "flank_menh",
        "rank": "Cát",
        "meaning": "Tả Phụ Hữu Bật kẹp Mệnh, có nhiều quý nhân phò tá.",
        "detail": "Hai sao phụ tá ở hai bên Cung Mệnh. "
                  "Được nhiều người giúp đỡ, có cấp dưới trung thành, công việc thuận lợi.",
        "advice": "Biết trọng dụng người khác, đừng tự mình ôm hết việc.",
        "icon": "🤝"
    },
    
    "xuong_khuc_giap_menh": {
        "name": "Xương Khúc Giáp Mệnh",
        "stars": ["Văn Xương", "Văn Khúc"],
        "condition": "flank_menh",
        "rank": "Cát",
        "meaning": "Văn Xương Văn Khúc kẹp Mệnh, thông minh tài hoa, học hành giỏi.",
        "detail": "Hai sao văn tinh kẹp Mệnh. Thông minh, học giỏi, có tài văn chương, "
                  "nghệ thuật sáng tạo, dễ đỗ đạt thăng tiến.",
        "advice": "Phát huy trí tuệ, theo đuổi con đường học vấn.",
        "icon": "📚"
    },
    
    "khoi_viet_giap_menh": {
        "name": "Khôi Việt Giáp Mệnh",
        "stars": ["Thiên Khôi", "Thiên Việt"],
        "condition": "flank_menh",
        "rank": "Cát",
        "meaning": "Quý nhân lưỡng bên, đời đi đến đâu cũng gặp may, có người giúp.",
        "detail": "Thiên Khôi (quý nhân nam) và Thiên Việt (quý nhân nữ) kẹp Mệnh. "
                  "Gặp quý nhân ở mọi nơi, khi khó khăn có người giúp, thi cử dễ đậu.",
        "advice": "Khi thành công nhớ giúp lại người khác.",
        "icon": "🌟"
    },
    
    "nhat_nguyet_tinh_minh": {
        "name": "Nhật Nguyệt Tịnh Minh",
        "stars": ["Thái Dương", "Thái Âm"],
        "condition": "both_mieu_vuong",
        "rank": "Đại Cát",
        "meaning": "Thái Dương Thái Âm đều sáng, văn võ song toàn, đời người thuận lợi.",
        "detail": "Thái Dương và Thái Âm đều ở vị trí Miếu/Vượng. "
                  "Thái Dương tốt ở Mão, Thìn, Tỵ, Ngọ. Thái Âm tốt ở Dậu, Tuất, Hợi, Tý. "
                  "Đời người sáng sủa, ít gian nan, có cả tài và đức.",
        "advice": "Phát huy điểm mạnh, giúp đỡ người khác.",
        "icon": "☀️🌙"
    },
    
    "co_quan_lam_menh": {
        "name": "Cơ Nguyệt Đồng Lương",
        "stars": ["Thiên Cơ", "Thái Âm", "Thiên Đồng", "Thiên Lương"],
        "condition": "any_2_same_cung",
        "rank": "Cát",
        "meaning": "Bốn sao phúc đức hội tụ, đời sống an nhàn, nhiều phúc lộc. Đại diện cho tuổi trẻ, sinh viên, trí thức (18-30 tuổi).",
        "detail": "Thiên Cơ (trí tuệ), Thái Âm (tài lộc), Thiên Đồng (phúc), Thiên Lương (ấm). Cách cục này chủ đời sống an nhàn, không vất vả. Đại diện cho sự phấn đấu, học hành, đam mê và nghị lực; phù hợp làm chuyên môn như kỹ sư, kiến trúc sư, công chức nhà nước, công việc văn phòng ổn định.",
        "advice": "Tận hưởng cuộc sống nhưng đừng quên cống hiến. Tập trung phát triển chuyên môn sâu, trau dồi kiến thức.",
        "icon": "🎓"
    },
    
    "co_cu_dong": {
        "name": "Cơ Cự Đồng",
        "stars": ["Thiên Cơ", "Cự Môn", "Thiên Đồng"],
        "condition": "menh_hoi_tu",
        "rank": "Cát",
        "meaning": "Tầng lớp quan lại, quản lý (dưới bộ Tử Phủ).",
        "detail": "Sử dụng ngoại giao, ngôn ngữ và trí tuệ để tiến thân; chuyên về nghiên cứu, thiết kế hành lang pháp lý và xây dựng xã hội. Chủ về tài ăn nói, mưu trí.",
        "advice": "Phát huy khả năng ngôn ngữ, ngoại giao, nghiên cứu.",
        "icon": "🗣️"
    },
    
    "am_duong_luong": {
        "name": "Âm Dương Lương",
        "stars": ["Thái Âm", "Thái Dương", "Thiên Lương"],
        "condition": "menh_hoi_tu",
        "rank": "Cát",
        "meaning": "Tầng lớp ngoại giao, kinh tế, tuổi già.",
        "detail": "Làm kinh thương, mậu dịch, đầu tư (Thái Âm) hoặc làm quan chức (Thái Dương); có nhiều người làm thầy giáo, thầy thuốc (Thiên Lương). Chủ về sự thông tuệ, uy tín.",
        "advice": "Cân bằng giữa danh vọng và tài lộc, giữ tâm sáng.",
        "icon": "⚖️"
    },
    
    # ═══════════════════════════════════════════════════════════════════════════
    # CÁCH CỤC HUNG (XẤU)
    # ═══════════════════════════════════════════════════════════════════════════
    
    "kinh_da_giap_menh": {
        "name": "Kình Đà Giáp Mệnh",
        "stars": ["Kinh Dương", "Đà La"],
        "condition": "flank_menh",
        "rank": "Hung",
        "meaning": "Hung tinh kẹp Mệnh, đời nhiều gian nan, hay gặp tiểu nhân.",
        "detail": "Kinh Dương (tranh đấu) và Đà La (cản trở) kẹp Mệnh. "
                  "Cuộc sống nhiều trắc trở, hay gặp tiểu nhân, công việc bị cản trở.",
        "advice": "Cần nhẫn nhịn, tránh đối đầu trực tiếp. Tìm cách hóa giải.",
        "icon": "⚠️"
    },
    
    "hoa_linh_giap_menh": {
        "name": "Hỏa Linh Giáp Mệnh",
        "stars": ["Hỏa Tinh", "Linh Tinh"],
        "condition": "flank_menh",
        "rank": "Hung",
        "meaning": "Hai sao nóng nảy kẹp Mệnh, tính cách dễ nổi nóng, hay gặp tai nạn.",
        "detail": "Hỏa Tinh (nóng nảy) và Linh Tinh (thất thường) kẹp Mệnh. "
                  "Tính tình nóng nảy, dễ gây xung đột, hay gặp tai nạn nhỏ.",
        "advice": "Học cách kiềm chế cảm xúc, tập thiền định.",
        "icon": "🔥"
    },
    
    "khong_kiep_giap_menh": {
        "name": "Không Kiếp Giáp Mệnh",
        "stars": ["Địa Không", "Địa Kiếp"],
        "condition": "flank_menh",
        "rank": "Hung",
        "meaning": "Hai sao hao tán kẹp Mệnh, tài chính hay thất thoát, cuộc sống nhiều biến động.",
        "detail": "Địa Không (trống rỗng) và Địa Kiếp (cướp đoạt) kẹp Mệnh. "
                  "Tài chính thất thường, hay mất tiền bất ngờ. "
                  "Tuy nhiên có thể hợp với nghệ thuật, tôn giáo.",
        "advice": "Đừng đầu tư mạo hiểm, theo đuổi nghệ thuật hoặc tâm linh.",
        "icon": "💫"
    },
    
    "menh_vo_chinh_dieu": {
        "name": "Mệnh Vô Chính Diệu",
        "stars": [],
        "condition": "no_chinh_tinh_in_menh",
        "rank": "Trung tính",
        "meaning": "Cung Mệnh không có Chính Tinh, phải xem cung đối diện và tam hợp.",
        "detail": "Cung Mệnh không có Chính Tinh nào tọa thủ. "
                  "Phải nhìn cung đối diện (Thiên Di) và cung Tam Hợp để luận. "
                  "Tính cách không rõ ràng, dễ bị ảnh hưởng bởi hoàn cảnh, linh hoạt.",
        "advice": "Chú ý đến phụ tinh và cung đối diện để hiểu rõ hơn về bản thân.",
        "icon": "❓"
    },
    
    "liem_sat_dong_cung": {
        "name": "Liêm Sát Đồng Cung",
        "stars": ["Liêm Trinh", "Thất Sát"],
        "condition": "same_cung_check_cat",  # Kiểm tra có cát tinh hay không
        "rank_with_cat": "Cát",  # Nếu có cát tinh
        "rank_without_cat": "Hung",  # Nếu không có cát tinh
        "meaning_with_cat": "Liêm Sát hóa Cát nhờ có cát tinh hỗ trợ, thành công lớn trong pháp luật, quân đội.",
        "meaning_without_cat": "Liêm Trinh gặp Thất Sát không có cát tinh, cuộc đời lao đao, nhiều biến động.",
        "detail": "Liêm Trinh (quan tinh) gặp Thất Sát (sát tinh) tạo nên cách cục mạnh mẽ.",
        "advice_with_cat": "Phù hợp ngành pháp luật, quân đội, y tế. Phát huy sức mạnh bản thân.",
        "advice_without_cat": "Cần tìm cách hóa giải bằng cách làm việc trong ngành pháp luật, quân đội, hoặc tu dưỡng.",
        "icon": "⚔️"
    },
}


# ═══════════════════════════════════════════════════════════════════════════════
# HÀM NHẬN DIỆN CÁCH CỤC
# ═══════════════════════════════════════════════════════════════════════════════

def get_stars_in_palace(positions: dict, palace_index: int) -> list:
    """Lấy danh sách tên sao trong một cung"""
    palace = positions.get(palace_index, {})
    stars = palace.get('stars', [])
    return [s['name'] if isinstance(s, dict) else s for s in stars]


def detect_cach_cuc(chart_data: dict) -> list:
    """
    Nhận diện các cách cục đặc biệt trong lá số
    
    Args:
        chart_data: Dữ liệu lá số từ chart_builder
        
    Returns:
        list các cách cục được phát hiện với đầy đủ thông tin
    """
    detected = []
    positions = chart_data.get('positions', {})
    menh_position = chart_data.get('menh_position', 0)
    tu_hoa = chart_data.get('tu_hoa', {})
    
    # Lấy danh sách sao trong Cung Mệnh
    menh_stars = get_stars_in_palace(positions, menh_position)
    
    # Lấy danh sách sao ở hai bên Cung Mệnh
    left_position = (menh_position - 1 + 12) % 12
    right_position = (menh_position + 1) % 12
    left_stars = get_stars_in_palace(positions, left_position)
    right_stars = get_stars_in_palace(positions, right_position)
    
    # Lấy vị trí Hóa Lộc
    hoa_loc_position = tu_hoa.get('Hóa Lộc', {}).get('position', -1)
    
    # Kiểm tra từng cách cục
    for cach_cuc_id, cach_cuc in CACH_CUC_LIST.items():
        condition = cach_cuc.get('condition', '')
        stars = cach_cuc.get('stars', [])
        
        is_detected = False
        detection_details = ""
        
        # Điều kiện: kẹp Mệnh
        if condition == 'flank_menh':
            if len(stars) == 2:
                if (stars[0] in left_stars and stars[1] in right_stars) or \
                   (stars[1] in left_stars and stars[0] in right_stars):
                    is_detected = True
                    detection_details = f"{stars[0]} và {stars[1]} kẹp Cung Mệnh"
        
        # Điều kiện: cùng cung
        elif condition == 'same_cung':
            for i in range(12):
                palace_stars = get_stars_in_palace(positions, i)
                if all(star in palace_stars for star in stars):
                    is_detected = True
                    from data import DIA_CHI
                    detection_details = f"Các sao cùng tại cung {DIA_CHI[i]}"
                    break
        
        # Điều kiện: cùng cung VÀ kiểm tra có cát tinh không
        elif condition == 'same_cung_check_cat':
            CAT_TINH = ['Tả Phụ', 'Hữu Bật', 'Văn Xương', 'Văn Khúc', 
                        'Thiên Khôi', 'Thiên Việt', 'Lộc Tồn', 'Thiên Mã',
                        'Hồng Loan', 'Thiên Hỹ', 'Giải Thần', 'Thiên Đức', 'Nguyệt Đức']
            for i in range(12):
                palace_stars = get_stars_in_palace(positions, i)
                if all(star in palace_stars for star in stars):
                    is_detected = True
                    from data import DIA_CHI
                    # Kiểm tra có cát tinh trong cung này không
                    has_cat_tinh = any(s in palace_stars for s in CAT_TINH)
                    # Cập nhật rank và meaning dựa trên kết quả
                    if has_cat_tinh:
                        cat_found = [s for s in CAT_TINH if s in palace_stars]
                        cach_cuc = dict(cach_cuc)  # Copy để không sửa gốc
                        cach_cuc['rank'] = cach_cuc.get('rank_with_cat', 'Cát')
                        cach_cuc['meaning'] = cach_cuc.get('meaning_with_cat', cach_cuc.get('meaning', ''))
                        cach_cuc['advice'] = cach_cuc.get('advice_with_cat', cach_cuc.get('advice', ''))
                        detection_details = f"Tại cung {DIA_CHI[i]}, CÓ cát tinh: {', '.join(cat_found[:3])}"
                    else:
                        cach_cuc = dict(cach_cuc)  # Copy để không sửa gốc
                        cach_cuc['rank'] = cach_cuc.get('rank_without_cat', 'Hung')
                        cach_cuc['meaning'] = cach_cuc.get('meaning_without_cat', cach_cuc.get('meaning', ''))
                        cach_cuc['advice'] = cach_cuc.get('advice_without_cat', cach_cuc.get('advice', ''))
                        detection_details = f"Tại cung {DIA_CHI[i]}, KHÔNG có cát tinh hỗ trợ"
                    break
        
        # Điều kiện: ít nhất 2 sao cùng cung
        elif condition == 'any_2_same_cung':
            for i in range(12):
                palace_stars = get_stars_in_palace(positions, i)
                matching_stars = [star for star in stars if star in palace_stars]
                if len(matching_stars) >= 2:
                    is_detected = True
                    from data import DIA_CHI
                    detection_details = f"{', '.join(matching_stars)} tại cung {DIA_CHI[i]}"
                    break
        
        # Điều kiện: Lộc Tồn cùng cung với Hóa Lộc (Song Lộc)
        elif condition == 'loc_ton_with_hoa_loc':
            from data import LOC_TON_POSITION
            year_can_index = chart_data.get('year_can_chi', {}).get('can_index', 0)
            loc_ton_pos = LOC_TON_POSITION.get(year_can_index, 0)
            if loc_ton_pos == hoa_loc_position:
                is_detected = True
                from data import DIA_CHI
                detection_details = f"Lộc Tồn và Hóa Lộc cùng tại {DIA_CHI[loc_ton_pos]}"
        
        # Điều kiện: cùng cung hoặc tam hợp
        elif condition == 'same_cung_or_tam_hop':
            for i in range(12):
                palace_stars = get_stars_in_palace(positions, i)
                if all(star in palace_stars for star in stars):
                    is_detected = True
                    from data import DIA_CHI
                    detection_details = f"Các sao cùng tại cung {DIA_CHI[i]}"
                    break
            # Kiểm tra tam hợp nếu chưa tìm thấy
            if not is_detected:
                tam_hop_groups = [
                    [0, 4, 8],   # Thân-Tý-Thìn
                    [2, 6, 10],  # Dần-Ngọ-Tuất
                    [1, 5, 9],   # Tỵ-Dậu-Sửu
                    [3, 7, 11]   # Hợi-Mão-Mùi
                ]
                for group in tam_hop_groups:
                    group_stars = []
                    for pos in group:
                        group_stars.extend(get_stars_in_palace(positions, pos))
                    if all(star in group_stars for star in stars):
                        is_detected = True
                        detection_details = f"Các sao ở cung Tam Hợp"
                        break
        
        # Điều kiện: Mệnh không có Chính Tinh
        elif condition == 'no_chinh_tinh_in_menh':
            has_chinh_tinh = any(star in menh_stars for star in CHINH_TINH_LIST)
            if not has_chinh_tinh:
                is_detected = True
                detection_details = "Cung Mệnh không có Chính Tinh tọa thủ"
        
        # Điều kiện: cả hai sao Miếu/Vượng
        elif condition == 'both_mieu_vuong':
            # Logic kiểm tra độ sáng - đơn giản hóa
            thai_duong_good = False
            thai_am_good = False
            
            for i in range(12):
                palace_stars = get_stars_in_palace(positions, i)
                # Thái Dương tốt ở Mão (3), Thìn (4), Tỵ (5), Ngọ (6)
                if 'Thái Dương' in palace_stars and i in [3, 4, 5, 6]:
                    thai_duong_good = True
                # Thái Âm tốt ở Dậu (9), Tuất (10), Hợi (11), Tý (0)
                if 'Thái Âm' in palace_stars and i in [9, 10, 11, 0]:
                    thai_am_good = True
            
            if thai_duong_good and thai_am_good:
                is_detected = True
                detection_details = "Thái Dương và Thái Âm đều ở vị trí sáng"
        
        # Nếu phát hiện cách cục, thêm vào danh sách
        if is_detected:
            detected.append({
                'id': cach_cuc_id,
                'detection_details': detection_details,
                **cach_cuc
            })
    
    return detected


def generate_cach_cuc_interpretation(detected_cach_cuc: list) -> dict:
    """
    Tạo luận giải từ các cách cục được phát hiện
    
    Args:
        detected_cach_cuc: Danh sách cách cục đã phát hiện
        
    Returns:
        dict chứa:
        - summary: Tóm tắt ngắn
        - details: Chi tiết đầy đủ
        - cat_cuc: Danh sách cách cục tốt
        - hung_cuc: Danh sách cách cục xấu
    """
    if not detected_cach_cuc:
        return {
            'summary': "Lá số không có cách cục đặc biệt nổi bật.",
            'details': "",
            'cat_cuc': [],
            'hung_cuc': [],
            'has_special': False
        }
    
    # Phân loại
    cat_cuc = [c for c in detected_cach_cuc if 'Cát' in c.get('rank', '')]
    hung_cuc = [c for c in detected_cach_cuc if 'Hung' in c.get('rank', '')]
    neutral_cuc = [c for c in detected_cach_cuc if 'Trung tính' in c.get('rank', '')]
    
    # Tạo summary
    summary_parts = []
    if cat_cuc:
        cat_names = ', '.join([c['name'] for c in cat_cuc[:3]])  # Tối đa 3
        summary_parts.append(f"✨ Cách cục tốt: {cat_names}")
    if hung_cuc:
        hung_names = ', '.join([c['name'] for c in hung_cuc[:2]])  # Tối đa 2
        summary_parts.append(f"⚠️ Cần lưu ý: {hung_names}")
    
    summary = ". ".join(summary_parts) if summary_parts else "Có một số cách cục đặc biệt."
    
    # Tạo chi tiết
    details_lines = []
    
    if cat_cuc:
        details_lines.append("\n## ✨ CÁCH CỤC CÁT (TỐT)\n")
        for cuc in cat_cuc:
            details_lines.append(f"### {cuc.get('icon', '⭐')} {cuc['name']} ({cuc['rank']})")
            details_lines.append(f"📍 *{cuc.get('detection_details', '')}*")
            details_lines.append(f"\n**Ý nghĩa:** {cuc['meaning']}")
            details_lines.append(f"\n{cuc['detail']}")
            details_lines.append(f"\n💡 **Lời khuyên:** {cuc['advice']}")
            details_lines.append("\n---\n")
    
    if hung_cuc:
        details_lines.append("\n## ⚠️ CÁCH CỤC CẦN LƯU Ý\n")
        for cuc in hung_cuc:
            details_lines.append(f"### {cuc.get('icon', '⚠️')} {cuc['name']} ({cuc['rank']})")
            details_lines.append(f"📍 *{cuc.get('detection_details', '')}*")
            details_lines.append(f"\n**Ý nghĩa:** {cuc['meaning']}")
            details_lines.append(f"\n{cuc['detail']}")
            details_lines.append(f"\n💡 **Cách hóa giải:** {cuc['advice']}")
            details_lines.append("\n---\n")
    
    if neutral_cuc:
        details_lines.append("\n## ❓ CÁCH CỤC TRUNG TÍNH\n")
        for cuc in neutral_cuc:
            details_lines.append(f"### {cuc.get('icon', '❓')} {cuc['name']}")
            details_lines.append(f"📍 *{cuc.get('detection_details', '')}*")
            details_lines.append(f"\n{cuc['detail']}")
            details_lines.append(f"\n💡 **Lưu ý:** {cuc['advice']}")
            details_lines.append("\n---\n")
    
    return {
        'summary': summary,
        'details': "\n".join(details_lines),
        'cat_cuc': cat_cuc,
        'hung_cuc': hung_cuc,
        'neutral_cuc': neutral_cuc,
        'has_special': len(detected_cach_cuc) > 0,
        'total_count': len(detected_cach_cuc)
    }


def get_cach_cuc_for_display(chart_data: dict) -> dict:
    """
    Hàm tiện ích để lấy cách cục và luận giải cho hiển thị
    
    Returns:
        dict ready for frontend display
    """
    detected = detect_cach_cuc(chart_data)
    interpretation = generate_cach_cuc_interpretation(detected)
    
    return {
        'detected': detected,
        'interpretation': interpretation
    }

