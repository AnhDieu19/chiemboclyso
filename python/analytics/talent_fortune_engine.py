"""
Talent vs Fortune Analysis - "Chữ Tài Chữ Mệnh Khéo Là Ghét Nhau"
Based on Nguyễn Du's Truyện Kiều philosophy.

TÀI (Talent): Intelligence, skills, artistic ability, career excellence
MỆNH (Fortune): Luck, happiness, ease of life, protection from hardship
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TalentFortuneAnalyzer:
    """Analyze the relationship between Talent (TÀI) and Fortune (MỆNH)"""
    
    # Talent stars (TÀI - Tài năng)
    TAI_STARS = {
        'van_tinh': ['Văn Xương', 'Văn Khúc'],           # Văn học, trí tuệ
        'khoa_giap': ['Hóa Khoa'],                       # Học vấn, danh tiếng
        'thong_minh': ['Thiên Khôi', 'Thiên Việt'],      # Thông minh, quý nhân
        'nghe_thuat': ['Hoa Cái', 'Long Trì', 'Phượng Các'],  # Nghệ thuật
        'quyen_luc': ['Hóa Quyền'],                      # Năng lực lãnh đạo
    }
    
    # Fortune stars (MỆNH - May mắn, hạnh phúc)
    MENH_STARS = {
        'loc': ['Lộc Tồn', 'Hóa Lộc'],                  # Tài lộc, sung túc
        'phuc': ['Thiên Phủ', 'Thái Âm', 'Thiên Đồng'], # Phúc hậu
        'quy_nhan': ['Tả Phụ', 'Hữu Bật'],              # Quý nhân phù trợ
        'hanh_phuc': ['Hồng Loan', 'Thiên Hỹ'],         # Hạnh phúc gia đình
        'bao_ve': ['Thiên Khôi', 'Thiên Việt'],         # Bảo vệ khỏi tai họa
    }
    
    # Negative factors (reduce scores)
    TAI_NEGATIVE = ['Địa Không', 'Địa Kiếp']  # Tài mà gặp Không = Tài hão
    MENH_NEGATIVE = ['Kinh Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh', 
                     'Cô Thần', 'Quả Tú', 'Thiên Hình', 'Hóa Kỵ']
    
    def __init__(self, chart_data):
        self.chart = chart_data
        self.menh_stars = self._get_stars_in_palace("Mệnh")
        self.than_stars = self._get_stars_in_palace("Thân")
        self.profile_stars = self.menh_stars.union(self.than_stars)
        self.phu_the_stars = self._get_stars_in_palace("Phu Thê")
        self.quan_loc_stars = self._get_stars_in_palace("Quan Lộc")
    
    def _get_stars_in_palace(self, palace_name):
        """Get all stars at a palace"""
        for idx, name in self.chart.get('cung_map', {}).items():
            if name == palace_name:
                pos_data = self.chart.get('positions', {}).get(idx, {})
                return set(s['name'] for s in pos_data.get('stars', []))
        return set()
    
    def score_talent(self):
        """
        Score TÀI (Talent) - 0 to 10
        Higher = More talented
        """
        score = 5.0
        factors = []
        
        # 1. Văn tinh at Mệnh/Thân (trí tuệ văn chương)
        for star in self.TAI_STARS['van_tinh']:
            if star in self.profile_stars:
                score += 1.5
                factors.append(f"{star} tại Mệnh/Thân (+1.5)")
        
        # 2. Hóa Khoa (danh tiếng học vấn)
        if 'Hóa Khoa' in self.profile_stars:
            score += 2.0
            factors.append("Hóa Khoa tại Mệnh/Thân (+2.0)")
        elif 'Hóa Khoa' in self.quan_loc_stars:
            score += 1.0
            factors.append("Hóa Khoa tại Quan Lộc (+1.0)")
        
        # 3. Thiên Khôi / Thiên Việt (thông minh)
        for star in self.TAI_STARS['thong_minh']:
            if star in self.profile_stars:
                score += 0.5
                factors.append(f"{star} (+0.5)")
        
        # 4. Hoa Cái (nghệ thuật)
        if 'Hoa Cái' in self.profile_stars:
            score += 1.0
            factors.append("Hoa Cái - Nghệ thuật (+1.0)")
        
        # 5. Hóa Quyền (năng lực lãnh đạo)
        if 'Hóa Quyền' in self.profile_stars:
            score += 1.0
            factors.append("Hóa Quyền - Lãnh đạo (+1.0)")
        
        # 6. Thiên Cơ sáng (cơ trí, mưu lược)
        if 'Thiên Cơ' in self.menh_stars:
            score += 1.0
            factors.append("Thiên Cơ tại Mệnh (+1.0)")
        
        # Negative: Tài gặp Không = Tài hão
        for neg in self.TAI_NEGATIVE:
            if neg in self.profile_stars:
                score -= 1.5
                factors.append(f"{neg} phá Tài (-1.5)")
        
        return {'score': max(0, min(10, score)), 'factors': factors}
    
    def score_fortune(self):
        """
        Score MỆNH (Fortune) - 0 to 10
        Higher = More fortunate/happy life
        """
        score = 5.0
        factors = []
        
        # 1. Lộc Tồn / Hóa Lộc (sung túc)
        for star in self.MENH_STARS['loc']:
            if star in self.profile_stars:
                score += 1.5
                factors.append(f"{star} - Sung túc (+1.5)")
        
        # 2. Thiên Phủ / Thái Âm / Thiên Đồng (phúc hậu)
        for star in self.MENH_STARS['phuc']:
            if star in self.menh_stars:
                score += 1.0
                factors.append(f"{star} tại Mệnh - Phúc hậu (+1.0)")
        
        # 3. Tả Phụ + Hữu Bật (quý nhân đôi bên)
        if 'Tả Phụ' in self.profile_stars and 'Hữu Bật' in self.profile_stars:
            score += 1.5
            factors.append("Tả Hữu hội - Quý nhân (+1.5)")
        
        # 4. Hồng Loan / Thiên Hỹ tại Phu Thê (hạnh phúc hôn nhân)
        for star in self.MENH_STARS['hanh_phuc']:
            if star in self.phu_the_stars:
                score += 1.0
                factors.append(f"{star} tại Phu Thê (+1.0)")
        
        # 5. Tuần/Triệt bảo vệ Mệnh
        menh_idx = self.chart.get('menh_position')
        if menh_idx is not None:
            pos_data = self.chart.get('positions', {}).get(menh_idx, {})
            if pos_data.get('in_tuan') or pos_data.get('in_triet'):
                score += 0.5
                factors.append("Tuần/Triệt bảo vệ (+0.5)")
        
        # Negative: Sát tinh / Cô Quả
        for neg in self.MENH_NEGATIVE:
            if neg in self.menh_stars:
                score -= 0.5
                factors.append(f"{neg} tại Mệnh (-0.5)")
            if neg in self.phu_the_stars:
                score -= 0.3
                factors.append(f"{neg} tại Phu Thê (-0.3)")
        
        return {'score': max(0, min(10, score)), 'factors': factors}
    
    def analyze(self):
        """
        Full analysis of Tài vs Mệnh
        Returns classification and insight
        """
        tai = self.score_talent()
        menh = self.score_fortune()
        
        tai_score = tai['score']
        menh_score = menh['score']
        
        # Classification
        if tai_score >= 7.0 and menh_score >= 7.0:
            category = "Tài Mệnh Song Toàn"
            insight = "Rất hiếm! Cả tài năng và may mắn đều cao."
        elif tai_score >= 7.0 and menh_score <= 4.0:
            category = "Tài Cao Mệnh Thấp"
            insight = "Đúng như Kiều: Tài năng xuất chúng nhưng đời lắm gian truân."
        elif tai_score <= 4.0 and menh_score >= 7.0:
            category = "Mệnh Cao Tài Thấp"
            insight = "Bình dị mà hạnh phúc, tuy không xuất chúng nhưng đời an nhàn."
        elif tai_score <= 4.0 and menh_score <= 4.0:
            category = "Tài Mệnh Đều Thấp"
            insight = "Cần nỗ lực nhiều hơn người khác để vượt qua nghịch cảnh."
        elif abs(tai_score - menh_score) >= 3.0:
            if tai_score > menh_score:
                category = "Tài Vượt Mệnh"
                insight = "Tài năng không được may mắn hỗ trợ, có thể gặp trắc trở."
            else:
                category = "Mệnh Vượt Tài"
                insight = "May mắn nhiều hơn tài năng, nên biết ơn và tu dưỡng."
        else:
            category = "Tài Mệnh Cân Bằng"
            insight = "Tài năng và may mắn tương đối cân bằng."
        
        return {
            'tai_score': round(tai_score, 1),
            'tai_factors': tai['factors'],
            'menh_score': round(menh_score, 1),
            'menh_factors': menh['factors'],
            'category': category,
            'insight': insight,
            'gap': round(tai_score - menh_score, 1)
        }


# Standalone test
if __name__ == "__main__":
    from chart import generate_birth_chart
    
    # Test with sample chart
    c = generate_birth_chart(28, 3, 1994, 4, 'nu')
    analyzer = TalentFortuneAnalyzer(c)
    result = analyzer.analyze()
    
    print("=" * 60)
    print("TAI MENH ANALYSIS")
    print("=" * 60)
    print(f"TÀI Score: {result['tai_score']}")
    print(f"MỆNH Score: {result['menh_score']}")
    print(f"Gap: {result['gap']}")
    print(f"Category: {result['category']}")
    print(f"Insight: {result['insight']}")
