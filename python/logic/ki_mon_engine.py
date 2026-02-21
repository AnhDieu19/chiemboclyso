"""
Kì Môn Engine - Core engine tính toán Kì Môn Độn Giáp

Chức năng:
- Xác định Cục (1-9) dựa vào Tiết Khí
- Xác định Dương Độn/Âm Độn
- An Bát Môn, Cửu Tinh, Bát Thần vào 9 Cung
- Xác định Tam Kỳ
- Luận giải
"""

from typing import Dict, List, Tuple
from data.ki_mon_tables import (
    TAM_KY, BAT_MON, BAT_MON_ORDER, 
    CUU_TINH, CUU_TINH_ORDER,
    BAT_THAN, BAT_THAN_ORDER,
    DUONG_DON_CUC, AM_DON_CUC,
    get_cuc_by_yuan
)
from core.jie_qi_calculator import get_tiet_khi, is_duong_don, jd_from_date
from core.ngu_hanh_engine import NguHanhEngine
from core.palace_converter import LAC_THU_CUNG, phi_thuong


class KiMonEngine:
    """
    Engine tính toán Kì Môn Độn Giáp
    """
    
    def __init__(self, year: int, month: int, day: int, hour: int = 0):
        """
        Khởi tạo Kì Môn Engine
        
        Args:
            year: Năm dương lịch
            month: Tháng (1-12)
            day: Ngày (1-31)
            hour: Giờ (0-23)
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        
        # Tính Tiết Khí
        self.tiet_khi = get_tiet_khi(day, month, year)
        
        # Xác định Dương Độn / Âm Độn
        self.la_duong_don = is_duong_don(self.tiet_khi['index'])
        
        # Tính Cục
        self._calculate_cuc()
        
        # Tính Giờ Kì Môn (trong 1 Cục có 18 giờ)
        self._calculate_hour()
    
    def _calculate_cuc(self):
        """
        Tính Cục (1-9) dựa vào Tiết Khí và Nguyên (Thượng/Trung/Hạ).
        
        Mỗi tiết khí ~15 ngày = 3 nguyên x 5 ngày:
        - Thượng Nguyên: 5 ngày đầu
        - Trung Nguyên: 5 ngày giữa
        - Hạ Nguyên: 5 ngày cuối
        """
        tiet_khi_idx = self.tiet_khi['index']
        
        # Xác định nguyên (Thượng/Trung/Hạ) dựa vào Can Chi ngày
        # Tiêu chuẩn: Dựa vào càn chi ngày chia 15 (ngày trong tiết khí)
        # Đơn giản hóa: dùng ngày % 15 để xác định vị trí trong tiết khí
        # Can Chi ngày: (JD + 49) % 60
        try:
            jd = jd_from_date(self.day, self.month, self.year)
            can_chi_day = int((jd + 49) % 60)
            # Nguyên: dùng can chi ngày % 15
            # Ngày Giáp Tý = 0 trong 60 Can Chi
            # Mỗi nguyên 5 ngày: 0-4 = Thượng, 5-9 = Trung, 10-14 = Hạ
            day_in_yuan = can_chi_day % 15
            if day_in_yuan < 5:
                self.yuan = 0  # Thượng Nguyên
            elif day_in_yuan < 10:
                self.yuan = 1  # Trung Nguyên
            else:
                self.yuan = 2  # Hạ Nguyên
        except Exception:
            self.yuan = 0  # Default Thượng Nguyên
        
        self.cuc = get_cuc_by_yuan(tiet_khi_idx, self.yuan, self.la_duong_don)
    
    def _calculate_hour(self):
        """Tính giờ Kì Môn (0-17)"""
        # 1 Cục = 75 ngày = 18 giờ Kì Môn
        # Đơn giản hóa: dùng giờ trong ngày
        self.qimen_hour = self.hour % 12
    
    def get_cuc_info(self) -> Dict:
        """Lấy thông tin Cục hiện tại"""
        yuan_names = ['Thượng Nguyên', 'Trung Nguyên', 'Hạ Nguyên']
        return {
            'cuc': self.cuc,
            'yuan': self.yuan,
            'yuan_name': yuan_names[self.yuan],
            'la_duong_don': self.la_duong_don,
            'don_type': 'Dương Độn' if self.la_duong_don else 'Âm Độn',
            'tiet_khi': self.tiet_khi['name_vi'],
            'direction': 'Thuận' if self.la_duong_don else 'Nghịch'
        }
    
    def an_bat_mon(self) -> Dict[int, str]:
        """
        An Bát Môn vào 9 Cung
        
        Returns:
            Dict mapping cung (1-9) → tên Môn
        """
        positions = {}
        
        # Cung bắt đầu = Cục
        start_pos = self.cuc
        
        for i, mon in enumerate(BAT_MON_ORDER):
            pos = phi_thuong(start_pos, i, self.la_duong_don)
            positions[pos] = mon
        
        return positions
    
    def an_cuu_tinh(self) -> Dict[int, str]:
        """
        An Cửu Tinh vào 9 Cung (Thiên Cấm ở Trung Cung)
        
        Returns:
            Dict mapping cung (1-9) → tên Tinh
        """
        positions = {5: 'Thiên Cấm'}  # Trung Cung cố định
        
        # Cung bắt đầu cho 8 Tinh còn lại
        start_pos = self.cuc
        
        for i, tinh in enumerate(CUU_TINH_ORDER):
            pos = phi_thuong(start_pos, i, self.la_duong_don)
            if pos != 5:  # Bỏ qua Trung Cung
                positions[pos] = tinh
        
        return positions
    
    def an_bat_than(self) -> Dict[int, str]:
        """
        An Bát Thần vào 9 Cung
        
        Returns:
            Dict mapping cung (1-9) → tên Thần
        """
        positions = {}
        
        # Trực Phù đi theo Cục
        start_pos = self.cuc
        
        for i, than in enumerate(BAT_THAN_ORDER):
            pos = phi_thuong(start_pos, i, self.la_duong_don)
            positions[pos] = than
        
        return positions
    
    def find_tam_ky(self) -> Dict[int, str]:
        """
        Tìm vị trí Tam Kỳ (Ất, Bính, Đinh) theo Can Chi ngày.
        
        Tam Kỳ được ẩn trong 10 Thiên Can:
        - Dương Độn (Giáp Tý → Giáp Tuất): Ất Bính Đinh thuận theo can
        - Âm Độn (Giáp Ngọ → Giáp Thìn): Ất Bính Đinh nghịch
        
        Vị trí: Can Chi ngày → Giáp kí mật → Tìm Ất Bính Đinh
        
        Returns:
            Dict mapping cung (1-9) → Tam Kỳ
        """
        positions = {}
        
        try:
            jd = jd_from_date(self.day, self.month, self.year)
            can_chi_day = int((jd + 49) % 60)
            can_index = can_chi_day % 10  # 0=Giáp ... 9=Quý
            
            # Giáp(đầu cục) ẩn ở 1 trong 6 Mậu (Giáp Tý/Tuất/Thân/Ngọ/Thìn/Dần)
            # Dương Độn: Ất(1), Bính(2), Đinh(3) theo thứ tự sau Giáp
            # Âm Độn: nghịch lại
            
            # Offset từ Giáp: Ất=+1, Bính=+2, Đinh=+3
            tam_ky_offsets = [1, 2, 3]  # Ất, Bính, Đinh
            tam_ky_names = ['Ất', 'Bính', 'Đinh']
            
            # Cung của Giáp: determined by Cục
            giap_palace = self.cuc
            
            for i, ky in enumerate(tam_ky_names):
                offset = tam_ky_offsets[i]
                pos = phi_thuong(giap_palace, offset, self.la_duong_don)
                positions[pos] = ky
        except Exception:
            # Fallback
            tam_ky_list = ['Ất', 'Bính', 'Đinh']
            for i, ky in enumerate(tam_ky_list):
                pos = phi_thuong(self.cuc, i + 1, self.la_duong_don)
                positions[pos] = ky
        
        return positions
    
    def analyze_palace(self, palace_idx: int) -> Dict:
        """
        Phân tích 1 cung
        
        Args:
            palace_idx: 1-9
            
        Returns:
            Dict với Môn, Tinh, Thần, Tam Kỳ, điểm số
        """
        mon_positions = self.an_bat_mon()
        tinh_positions = self.an_cuu_tinh()
        than_positions = self.an_bat_than()
        tam_ky_positions = self.find_tam_ky()
        
        # Lấy thông tin cung này
        mon = mon_positions.get(palace_idx)
        tinh = tinh_positions.get(palace_idx)
        than = than_positions.get(palace_idx)
        tam_ky = tam_ky_positions.get(palace_idx)
        
        # Tính điểm
        score = 0
        elements = []
        
        if mon:
            mon_info = BAT_MON[mon]
            score += mon_info['score']
            elements.append(f"Môn: {mon} ({mon_info['score']:+d})")
        
        if tinh:
            tinh_info = CUU_TINH[tinh]
            score += tinh_info['score']
            elements.append(f"Tinh: {tinh} ({tinh_info['score']:+d})")
        
        if than:
            than_info = BAT_THAN[than]
            score += than_info['score']
            elements.append(f"Thần: {than} ({than_info['score']:+d})")
        
        if tam_ky:
            ky_info = TAM_KY[tam_ky]
            score += ky_info['score']
            elements.append(f"Kỳ: {tam_ky} ({ky_info['score']:+d})")
        
        # Xác định tính chất
        if score >= 20:
            nature = 'dai_cat'
        elif score >= 10:
            nature = 'cat'
        elif score >= 0:
            nature = 'trung'
        elif score >= -10:
            nature = 'hung'
        else:
            nature = 'dai_hung'
        
        # Tổng hợp lời giải
        interpretations = []
        mon_detail = None
        tinh_detail = None
        than_detail = None
        ky_detail = None

        if mon:
            mi = BAT_MON[mon]
            interpretations.append(f"Môn - {mon}: {mi['meaning']}")
            mon_detail = {
                'name': mon, 'han': mi['han'], 'meaning': mi['meaning'],
                'nature': mi['nature'], 'score': mi['score'],
                'applications': mi.get('applications', [])
            }
        if tinh:
            ti = CUU_TINH[tinh]
            interpretations.append(f"Tinh - {tinh}: {ti['meaning']}")
            tinh_detail = {
                'name': tinh, 'han': ti['han'], 'meaning': ti['meaning'],
                'nature': ti['nature'], 'score': ti['score'],
                'ngu_hanh': ti.get('ngu_hanh', '')
            }
        if than:
            th = BAT_THAN[than]
            interpretations.append(f"Thần - {than}: {th['meaning']}")
            than_detail = {
                'name': than, 'han': th['han'], 'meaning': th['meaning'],
                'nature': th['nature'], 'score': th['score']
            }
        if tam_ky:
            ki = TAM_KY[tam_ky]
            interpretations.append(f"Kỳ - {tam_ky}: {ki['meaning']}")
            ky_detail = {
                'name': tam_ky, 'han': ki['han'], 'meaning': ki['meaning'],
                'alias': ki.get('alias', ''), 'score': ki['score'],
                'ngu_hanh': ki.get('ngu_hanh', '')
            }

        # Tổng hợp phân tích
        combined = self._combine_analysis(mon, tinh, than, tam_ky, score, nature)

        return {
            'palace': palace_idx,
            'palace_info': LAC_THU_CUNG[palace_idx],
            'mon': mon,
            'tinh': tinh,
            'than': than,
            'tam_ky': tam_ky,
            'mon_detail': mon_detail,
            'tinh_detail': tinh_detail,
            'than_detail': than_detail,
            'ky_detail': ky_detail,
            'score': score,
            'nature': nature,
            'elements': elements,
            'interpretation': interpretations,
            'combined_analysis': combined
        }

    def _combine_analysis(self, mon, tinh, than, tam_ky, score, nature) -> str:
        """
        Tổng hợp phân tích kết hợp các yếu tố Môn-Tinh-Thần-Kỳ.
        Đưa ra nhận định tổng thể dễ hiểu.
        """
        parts = []

        # Nhận định chung theo điểm
        if nature == 'dai_cat':
            parts.append("Cung rất tốt, đại cát.")
        elif nature == 'cat':
            parts.append("Cung tốt lành, thuận lợi.")
        elif nature == 'trung':
            parts.append("Cung bình thường, không tốt không xấu.")
        elif nature == 'hung':
            parts.append("Cung xấu, nên cẩn thận.")
        elif nature == 'dai_hung':
            parts.append("Cung rất xấu, nên tránh.")

        # Phân tích tương tác Môn-Tinh
        if mon and tinh:
            mi = BAT_MON[mon]
            ti = CUU_TINH[tinh]
            mon_good = mi['score'] > 0
            tinh_good = ti['score'] > 0
            if mon_good and tinh_good:
                parts.append(f"Môn {mon} cát gặp Tinh {tinh} cát, rất thuận lợi cho việc lớn.")
            elif mon_good and not tinh_good:
                parts.append(f"Môn {mon} tốt nhưng Tinh {tinh} xấu, cần thận trọng dù có cơ hội.")
            elif not mon_good and tinh_good:
                parts.append(f"Môn {mon} xấu dù Tinh {tinh} tốt, nên chờ thời cơ khác.")
            else:
                parts.append(f"Môn {mon} xấu gặp Tinh {tinh} xấu, tuyệt đối nên tránh.")

        # Bát Thần
        if than:
            th = BAT_THAN[than]
            if th['score'] >= 5:
                parts.append(f"Có Thần {than} phù trợ mạnh mẽ.")
            elif th['score'] <= -3:
                parts.append(f"Thần {than} gây bất lợi, cẩn thận.")

        # Tam Kỳ
        if tam_ky:
            ki = TAM_KY[tam_ky]
            parts.append(f"Được Tam Kỳ {tam_ky} ({ki['alias']}) chiếu, gia tăng may mắn đáng kể.")

        # Ứng dụng
        if mon:
            apps = BAT_MON[mon].get('applications', [])
            if apps:
                parts.append(f"Ứng dụng: {', '.join(apps)}.")

        return ' '.join(parts)
    
    def get_full_chart(self) -> Dict:
        """
        Lấy toàn bộ bàn Kì Môn
        
        Returns:
            Dict với tất cả thông tin
        """
        palaces = {}
        for i in range(1, 10):
            palaces[i] = self.analyze_palace(i)
        
        return {
            'input': {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'hour': self.hour
            },
            'cuc_info': self.get_cuc_info(),
            'palaces': palaces,
            'best_direction': self._find_best_direction(palaces),
            'worst_direction': self._find_worst_direction(palaces)
        }
    
    def _find_best_direction(self, palaces: Dict) -> Dict:
        """Tìm phương hướng tốt nhất"""
        best = max(palaces.values(), key=lambda p: p['score'])
        return {
            'palace': best['palace'],
            'direction': best['palace_info']['direction'],
            'score': best['score'],
            'reason': ', '.join(best['elements'])
        }
    
    def _find_worst_direction(self, palaces: Dict) -> Dict:
        """Tìm phương hướng xấu nhất"""
        worst = min(palaces.values(), key=lambda p: p['score'])
        return {
            'palace': worst['palace'],
            'direction': worst['palace_info']['direction'],
            'score': worst['score'],
            'reason': ', '.join(worst['elements'])
        }


# Test
if __name__ == '__main__':
    # Test với ngày 24/12/2024
    engine = KiMonEngine(2024, 12, 24, 10)
    
    print("=== KÌ MÔN ĐỘN GIÁP ===")
    print(f"Ngày: {engine.day}/{engine.month}/{engine.year}, Giờ: {engine.hour}h")
    print()
    
    cuc = engine.get_cuc_info()
    print(f"Cục {cuc['cuc']} - {cuc['don_type']} ({cuc['direction']})")
    print(f"Tiết Khí: {cuc['tiet_khi']}")
    print()
    
    print("--- Phân tích 9 Cung ---")
    chart = engine.get_full_chart()
    for i in range(1, 10):
        p = chart['palaces'][i]
        info = p['palace_info']
        print(f"Cung {i} ({info['name']} - {info['direction']}): {p['nature']}")
        print(f"  Môn: {p['mon'] or '-'}, Tinh: {p['tinh'] or '-'}, Thần: {p['than'] or '-'}, Kỳ: {p['tam_ky'] or '-'}")
        print(f"  Điểm: {p['score']}")
        print()
    
    print("--- Kết luận ---")
    print(f"Phương tốt nhất: {chart['best_direction']['direction']} (Cung {chart['best_direction']['palace']})")
    print(f"Phương xấu nhất: {chart['worst_direction']['direction']} (Cung {chart['worst_direction']['palace']})")
