"""
Beauty Fate Analyzer Engine
"""
from analytics.definitions import BEAUTY_STARS, LUCKY_STARS, TRAGIC_STARS

class BeautyFateAnalyzer:
    def __init__(self, chart_data):
        self.chart = chart_data
        self.menh_stars = self._get_stars_in_palace_by_name("Mệnh")
        self.than_stars = self._get_stars_in_palace_by_name_or_attr("Thân")
        
        # Gộp sao Mệnh và Thân để xét tạng người chung
        self.profile_stars = self.menh_stars.union(self.than_stars)
        
        # Lấy cung Phu Thê để check hạnh phúc gia đình
        self.phu_the_stars = self._get_stars_in_palace_by_name("Phu Thê")

    def _get_stars_in_palace_by_name(self, palace_name):
        """Find stars in a palace by its logic name (Mệnh, Phụ Mẫu...)"""
        if not self.chart or 'positions' not in self.chart or 'cung_map' not in self.chart:
            return set()
            
        # Use cung_map to find the index of the requested palace
        target_idx = -1
        # cung_map keys are int (indices)
        for idx, name in self.chart['cung_map'].items():
            if name == palace_name:
                target_idx = idx
                break
                
        if target_idx != -1:
             pos = self.chart['positions'].get(target_idx) # .get incase dict uses str keys but unlikely
             if pos:
                 return set(s['name'] for s in pos['stars'])
                 
        return set()

    def _get_stars_in_palace_by_name_or_attr(self, attr_name):
        """Find stars in Mệnh or Thân using explicit attributes or map"""
        # First try standard lookup
        stars = self._get_stars_in_palace_by_name(attr_name)
        if stars: return stars
        
        # Fallback to is_menh / is_than attributes if name lookup fails
        key = 'is_menh' if attr_name == 'Mệnh' else 'is_than'
        for pos in self.chart['positions'].values():
            if pos.get(key):
                return set(s['name'] for s in pos['stars'])
        return set()

    def check_beauty(self):
        """
        Kiểm tra xem lá số có thuộc nhóm 'Người Đẹp' không.
        Criteria: Must have at least one strong Beauty Set.
        """
        # 1. Check Đào Hồng Hỷ
        has_dao_hong = not BEAUTY_STARS["DAO_HONG"].isdisjoint(self.profile_stars)
        
        # 2. Check Xương Khúc (Văn Tinh)
        has_xuong_khuc = not BEAUTY_STARS["VAN_TINH"].isdisjoint(self.profile_stars)
        
        # 3. Check Tham Lang / Liêm Trinh (Quyến rũ) - Yêu cầu đi cùng Đào/Hồng mới tính là Đẹp Sắc Sảo
        # Nếu đứng một mình vẫn đẹp nhưng cần check thêm. 
        # For simplicity MVP: Tham/Liêm + (Đào or Hồng or Xương or Khúc or Thái Âm)
        has_quyen_ru = not BEAUTY_STARS["QUYEN_RU"].isdisjoint(self.profile_stars)
        supporting_beauty = has_dao_hong or has_xuong_khuc or ("Thái Âm" in self.profile_stars)
        
        # 4. Check Thái Âm / Thiên Phủ (Phúc hậu)
        has_phuc_hau = ("Thái Âm" in self.profile_stars) or ("Thiên Phủ" in self.profile_stars) or ("Thiên Tướng" in self.profile_stars)
        
        # Logic tổng hợp
        is_beauty = False
        
        if has_dao_hong: 
            is_beauty = True # Đào Hồng là tiêu chuẩn cứng
        elif has_xuong_khuc and has_phuc_hau:
            is_beauty = True # Nét đẹp thanh tú phúc hậu
        elif has_quyen_ru and supporting_beauty:
            is_beauty = True # Đẹp sắc sảo
            
        return is_beauty

    def calculate_fate_score(self):
        """
        Tính điểm Sướng vs Khổ.
        Return: (lucky_score, tragic_score)
        """
        lucky_set = set().union(*LUCKY_STARS.values())
        tragic_set = set().union(*TRAGIC_STARS.values())
        
        # Base scores from Profile (Mệnh + Thân)
        score_lucky = len(self.profile_stars.intersection(lucky_set))
        score_tragic = len(self.profile_stars.intersection(tragic_set))
        
        # --- SPECIAL RULES (COMBO) ---
        
        # 1. Đào Hồng + Không Kiếp ("Đóa hoa trước bão")
        if ("Đào Hoa" in self.profile_stars or "Hồng Loan" in self.profile_stars):
            if not TRAGIC_STARS["KHONG_KIEP"].isdisjoint(self.profile_stars):
                score_tragic += 5  # Penalty cực nặng
            
            # Đào Hồng + Hình Riêu (Sắc dục, thị phi)
            if "Thiên Hình" in self.profile_stars and "Thiên Riêu" in self.profile_stars:
                score_tragic += 3
                
            # Đào Hồng + Hóa Kỵ (Duyên nghiệp, oan trái)
            if "Hóa Kỵ" in self.profile_stars:
                score_tragic += 3

        # 2. Phu Thê bất lợi (Ảnh hưởng hạnh phúc người đẹp)
        # Check Sát tinh ở Phu Thê
        phu_the_tragic = len(self.phu_the_stars.intersection(tragic_set))
        if phu_the_tragic >= 2:
            score_tragic += 2 # Hôn nhân trắc trở trừ điểm hạnh phúc
            
        # Check Tuần/Triệt ở Phu Thê (Logic: Phu Thê usually bad with Tuan/Triet if early marriage)
        # Note: Chart data needs Tuan/Triet info. Usually they are distinct lists or stars.
        # Assuming they are in star list for now or we skip for MVP.
        if "Tuần" in self.phu_the_stars or "Triệt" in self.phu_the_stars:
            score_tragic += 1

        return score_lucky, score_tragic

    def identify_beauty_sets(self):
        """Return list of Beauty Sets satisfied by this chart"""
        sets = []
        if not BEAUTY_STARS["DAO_HONG"].isdisjoint(self.profile_stars):
            sets.append("DAO_HONG")
        if not BEAUTY_STARS["VAN_TINH"].isdisjoint(self.profile_stars) and \
           (("Thái Âm" in self.profile_stars) or ("Thiên Phủ" in self.profile_stars) or ("Thiên Tướng" in self.profile_stars)):
            sets.append("VAN_TINH") # Văn Tinh + Phúc Hậu
        if not BEAUTY_STARS["QUYEN_RU"].isdisjoint(self.profile_stars):
             sets.append("QUYEN_RU")
        if not BEAUTY_STARS["PHUC_THIEN"].isdisjoint(self.profile_stars) or "Thái Âm" in self.profile_stars:
             sets.append("PHUC_THIEN")
             
        return list(set(sets)) # Unique

    def classify_detailed(self):
        """
        Phân loại chi tiết 5 mức độ.
        """
        if not self.check_beauty():
            return "NOT_BEAUTY", []
            
        lucky, tragic = self.calculate_fate_score()
        diff = lucky - tragic
        beauty_sets = self.identify_beauty_sets()
        
        if diff >= 4:
            return "VERY_HAPPY", beauty_sets # Rất sung túc an nhàn
        elif diff >= 1:
            return "HAPPY", beauty_sets      # Hơi sướng
        elif diff >= -1:
            return "NEUTRAL", beauty_sets    # Bình thường
        elif diff >= -4:
            return "TRAGIC", beauty_sets     # Hơi vất vả
        else:
            return "VERY_TRAGIC", beauty_sets # Rất vất vả lận đận

    def classify(self):
        # Legacy Wrapper
        cls, _ = self.classify_detailed()
        return cls

    def get_chart_summary(self):
        """
        Return structured summary of the chart for export.
        - Chính Tinh (Mệnh)
        - Phụ Tinh (Mệnh)
        - Độ Sáng (Mệnh) - included in Chinh Tinh name usually or separate
        - Cung Cục (Mệnh Name + Cục)
        - Tứ Hóa (in Mệnh or global? usually key stars in Menh/Than)
        """
        if not self.chart: return {}
        
        # Mệnh Position
        menh_idx = self.chart.get('menh_position')
        if menh_idx is None: return {}
        
        pos_data = self.chart['positions'][menh_idx]
        
        # Chính Tinh & Độ Sáng
        chinh_tinh = []
        brightness = []
        # Chinh tinh usually have 'power' attr or check name against list
        from data import STAR_BRIGHTNESS_TABLE
        
        for s in pos_data['stars']:
            if s['name'] in STAR_BRIGHTNESS_TABLE:
                 chinh_tinh.append(s['name'])
                 brightness.append(s.get('brightness_name', ''))
        
        # Phụ Tinh (All other stars in Menh)
        phu_tinh = [s['name'] for s in pos_data['stars'] if s['name'] not in STAR_BRIGHTNESS_TABLE]
        
        # Cung Cục
        # "Can Chi Cung Mệnh" + "Cục"
        # Can Chi is not directly stored in 'positions' but can be derived or checking 'menh_name' (Chi)
        # We have menh_name in chart root.
        # Cục is in chart['cuc']
        cung_cuc = f"{self.chart.get('menh_name', '')} | {self.chart.get('cuc', {}).get('name', '')}"
        
        # Tứ Hóa
        # List all Tu Hua in the chart or just in Menh? Usually global Tu Hua for the year/age is calculated.
        # chart['tu_hoa'] has mapped info.
        # Let's stringify all 4:
        tu_hoa_list = []
        if 'tu_hoa' in self.chart:
             for hoa, info in self.chart['tu_hoa'].items():
                 # hoa: Hóa Lộc, info: {'star': 'Liêm Trinh', 'position': 5}
                 tu_hoa_list.append(f"{hoa}: {info['star']}")
                 
        return {
            "ChinhTinh": ", ".join(chinh_tinh),
            "PhuTinh": ", ".join(phu_tinh),
            "DoSang": ", ".join(brightness),
            "CungCuc": cung_cuc,
            "TuHoa": " | ".join(tu_hoa_list)
        }
        
    def identify_major_sets(self):
        """
        Identify classical Tu Vi star set at Mệnh ONLY.
        Returns a list with AT MOST ONE set name (or 'Vô Chính Diệu').
        FIX: Use self.menh_stars (only stars at Mệnh palace), not profile_stars.
        """
        from data import CHINH_TINH
        
        # CHINH_TINH is a dict, extract flat list of all 14 Chính Tinh
        all_chinh_tinh = CHINH_TINH.get('tu_vi_group', []) + CHINH_TINH.get('thien_phu_group', [])
        
        # Get only Chính Tinh at Mệnh
        chinh_tinh_at_menh = [s for s in self.menh_stars if s in all_chinh_tinh]
        
        # Check VCD first
        if len(chinh_tinh_at_menh) == 0:
            return ["Vô Chính Diệu"]
        
        # Now identify set based on which Chinh Tinh is present
        # Priority order (most specific to least)
        
        # 1. Sát Phá Tham (Any of: Thất Sát, Phá Quân, Tham Lang)
        if any(s in chinh_tinh_at_menh for s in ['Thất Sát', 'Phá Quân', 'Tham Lang']):
            return ["Sát Phá Tham"]
        
        # 2. Tử Phủ Vũ Tướng (Any of: Tử Vi, Thiên Phủ, Vũ Khúc, Thiên Tướng, Liêm Trinh)
        if any(s in chinh_tinh_at_menh for s in ['Tử Vi', 'Thiên Phủ', 'Vũ Khúc', 'Thiên Tướng', 'Liêm Trinh']):
            return ["Tử Phủ Vũ Tướng"]
            
        # 3. Cự Nhật (Cự Môn, Thái Dương)
        if any(s in chinh_tinh_at_menh for s in ['Cự Môn', 'Thái Dương']):
            return ["Cự Nhật"]
        
        # 4. Cơ Nguyệt Đồng Lương (Thiên Cơ, Thái Âm, Thiên Đồng, Thiên Lương)
        if any(s in chinh_tinh_at_menh for s in ['Thiên Cơ', 'Thái Âm', 'Thiên Đồng', 'Thiên Lương']):
            return ["Cơ Nguyệt Đồng Lương"]
        
        return ["Khác"]

    def classify_beauty_fortune(self):
        """
        Phân loại Hồng Nhan theo 5 cấp độ may mắn:
        
        Level 1: Rất May Mắn (8.0-10.0) - Hồng Nhan + Phú Quý + Hạnh Phúc
        Level 2: May Mắn (6.5-8.0) - Hồng Nhan + Nhiều yếu tố tốt
        Level 3: Trung Bình (5.0-6.5) - Hồng Nhan + Yếu tố hỗn hợp
        Level 4: Vất Vả (3.0-5.0) - Hồng Nhan + Một số yếu tố xấu
        Level 5: Bạc Mệnh (0-3.0) - Hồng Nhan + Nhiều sát tinh/cô quả
        
        Returns:
            dict: {level, name, score, factors_good, factors_bad, analysis}
        """
        # Kiểm tra có phải Hồng Nhan không
        is_beauty = self.check_beauty()
        if not is_beauty:
            return {
                'level': 0,
                'name': 'Không phải Hồng Nhan',
                'score': 0,
                'factors_good': [],
                'factors_bad': [],
                'analysis': 'Không đủ tiêu chuẩn Hồng Nhan để phân loại.'
            }
        
        # ===== YẾU TỐ TỐT (Sung Sướng) =====
        factors_good = []
        score = 5.0  # Base score
        
        # 1. Lộc Tồn / Hóa Lộc tại Mệnh/Thân
        if 'Lộc Tồn' in self.profile_stars:
            factors_good.append('Lộc Tồn tại Mệnh/Thân (+1.5)')
            score += 1.5
        if 'Hóa Lộc' in self.profile_stars:
            factors_good.append('Hóa Lộc tại Mệnh/Thân (+1.0)')
            score += 1.0
        
        # 2. Thiên Khôi / Thiên Việt (Quý nhân phù trợ)
        if 'Thiên Khôi' in self.profile_stars:
            factors_good.append('Thiên Khôi (+0.5)')
            score += 0.5
        if 'Thiên Việt' in self.profile_stars:
            factors_good.append('Thiên Việt (+0.5)')
            score += 0.5
        
        # 3. Tả Phụ / Hữu Bật (Hỗ trợ)
        if 'Tả Phụ' in self.profile_stars and 'Hữu Bật' in self.profile_stars:
            factors_good.append('Tả Hữu hội (+1.0)')
            score += 1.0
        
        # 4. Hồng Loan / Thiên Hỹ tại Phu Thê (Hạnh phúc hôn nhân)
        if 'Hồng Loan' in self.phu_the_stars or 'Thiên Hỹ' in self.phu_the_stars:
            factors_good.append('Hồng Loan/Thiên Hỹ tại Phu Thê (+1.0)')
            score += 1.0
        
        # 5. Thiên Đồng / Thái Âm sáng tại Phu Thê
        if 'Thiên Đồng' in self.phu_the_stars or 'Thái Âm' in self.phu_the_stars:
            factors_good.append('Thiên Đồng/Thái Âm tại Phu Thê (+0.5)')
            score += 0.5
        
        # 6. Tuần/Triệt bảo vệ Mệnh (VCD đắc Không)
        menh_idx = self.chart.get('menh_position')
        if menh_idx is not None:
            pos_data = self.chart.get('positions', {}).get(menh_idx, {})
            if pos_data.get('in_tuan') or pos_data.get('in_triet'):
                factors_good.append('Tuần/Triệt bảo vệ Mệnh (+0.5)')
                score += 0.5
        
        # ===== YẾU TỐ XẤU (Bạc Mệnh) =====
        factors_bad = []
        
        # 1. Sát tinh tại Mệnh
        sat_menh = ['Kinh Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh', 'Địa Không', 'Địa Kiếp']
        for sat in sat_menh:
            if sat in self.menh_stars:
                factors_bad.append(f'{sat} tại Mệnh (-1.0)')
                score -= 1.0
        
        # 2. Sát tinh tại Phu Thê (Hôn nhân bất hạnh)
        for sat in sat_menh:
            if sat in self.phu_the_stars:
                factors_bad.append(f'{sat} tại Phu Thê (-0.5)')
                score -= 0.5
        
        # 3. Cô Thần / Quả Tú (Cô đơn)
        if 'Cô Thần' in self.profile_stars:
            factors_bad.append('Cô Thần - Cô đơn (-1.5)')
            score -= 1.5
        if 'Quả Tú' in self.profile_stars:
            factors_bad.append('Quả Tú - Góa bụa (-1.5)')
            score -= 1.5
        
        # 4. Hóa Kỵ tại Phu Thê
        if 'Hóa Kỵ' in self.phu_the_stars:
            factors_bad.append('Hóa Kỵ tại Phu Thê (-1.0)')
            score -= 1.0
        
        # 5. Thiên Hình / Tang Môn / Điếu Khách tại Mệnh
        tragic_menh = ['Thiên Hình', 'Tang Môn', 'Điếu Khách', 'Bạch Hổ']
        for t in tragic_menh:
            if t in self.menh_stars:
                factors_bad.append(f'{t} tại Mệnh (-0.5)')
                score -= 0.5
        
        # 6. Đào Hoa + Tham Lang + Sát tinh = Bất hạnh tình duyên
        has_dao_tham = ('Đào Hoa' in self.profile_stars and 'Tham Lang' in self.profile_stars)
        has_sat_menh = any(sat in self.menh_stars for sat in sat_menh)
        if has_dao_tham and has_sat_menh:
            factors_bad.append('Đào Tham gặp Sát - Bất hạnh tình duyên (-1.0)')
            score -= 1.0
        
        # Normalize score
        score = max(0.0, min(10.0, score))
        
        # Determine level
        if score >= 8.0:
            level = 1
            name = 'Rất May Mắn'
            analysis = 'Hồng Nhan đại phú quý, hạnh phúc viên mãn.'
        elif score >= 6.5:
            level = 2
            name = 'May Mắn'
            analysis = 'Hồng Nhan được hưởng phúc, tình duyên thuận lợi.'
        elif score >= 5.0:
            level = 3
            name = 'Trung Bình'
            analysis = 'Hồng Nhan có lúc vui lúc buồn, đời sống cần nỗ lực.'
        elif score >= 3.0:
            level = 4
            name = 'Vất Vả'
            analysis = 'Hồng Nhan gặp nhiều trắc trở, tình duyên không trọn vẹn.'
        else:
            level = 5
            name = 'Bạc Mệnh'
            analysis = 'Hồng Nhan bạc mệnh, đời lắm gian truân, cần tu tâm dưỡng tính.'
        
        return {
            'level': level,
            'name': name,
            'score': round(score, 1),
            'factors_good': factors_good,
            'factors_bad': factors_bad,
            'analysis': analysis
        }
