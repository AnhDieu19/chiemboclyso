"""
Ngũ Hành Engine - Tương Sinh Tương Khắc

Tái sử dụng cho: Tử Vi, Huyền Không, Thái Ất, Kì Môn
"""

from typing import Dict, List, Optional


class NguHanhEngine:
    """
    Engine xử lý Ngũ Hành: Kim, Mộc, Thủy, Hỏa, Thổ
    """
    
    # Ngũ Hành Tương Sinh: A sinh B
    NGU_HANH_SINH = {
        'Kim': 'Thủy',   # Kim sinh Thủy
        'Thủy': 'Mộc',   # Thủy sinh Mộc
        'Mộc': 'Hỏa',    # Mộc sinh Hỏa
        'Hỏa': 'Thổ',    # Hỏa sinh Thổ
        'Thổ': 'Kim'     # Thổ sinh Kim
    }
    
    # Ngũ Hành Tương Khắc: A khắc B
    NGU_HANH_KHAC = {
        'Kim': 'Mộc',    # Kim khắc Mộc
        'Mộc': 'Thổ',    # Mộc khắc Thổ
        'Thổ': 'Thủy',   # Thổ khắc Thủy
        'Thủy': 'Hỏa',   # Thủy khắc Hỏa
        'Hỏa': 'Kim'     # Hỏa khắc Kim
    }
    
    # Địa Chi (12 Cung) → Ngũ Hành
    CHI_NGU_HANH = {
        0: 'Thủy',   # Tý
        1: 'Thổ',    # Sửu
        2: 'Mộc',    # Dần
        3: 'Mộc',    # Mão
        4: 'Thổ',    # Thìn
        5: 'Hỏa',    # Tỵ
        6: 'Hỏa',    # Ngọ
        7: 'Thổ',    # Mùi
        8: 'Kim',    # Thân
        9: 'Kim',    # Dậu
        10: 'Thổ',   # Tuất
        11: 'Thủy'   # Hợi
    }
    
    # 9 Cung Lạc Thư → Ngũ Hành
    LAC_THU_NGU_HANH = {
        1: 'Thủy',   # Khảm (Bắc)
        2: 'Thổ',    # Khôn (Tây Nam)
        3: 'Mộc',    # Chấn (Đông)
        4: 'Mộc',    # Tốn (Đông Nam)
        5: 'Thổ',    # Trung Cung
        6: 'Kim',    # Càn (Tây Bắc)
        7: 'Kim',    # Đoài (Tây)
        8: 'Thổ',    # Cấn (Đông Bắc)
        9: 'Hỏa'     # Ly (Nam)
    }
    
    @classmethod
    def get_relation(cls, hanh1: str, hanh2: str) -> str:
        """
        Xác định mối quan hệ giữa 2 Ngũ Hành
        
        Args:
            hanh1: Ngũ Hành thứ nhất
            hanh2: Ngũ Hành thứ hai
            
        Returns:
            'sinh' - hanh1 sinh hanh2
            'bi_sinh' - hanh1 được hanh2 sinh
            'khac' - hanh1 khắc hanh2
            'bi_khac' - hanh1 bị hanh2 khắc
            'dong' - Đồng hành
        """
        if hanh1 == hanh2:
            return 'dong'
        if cls.NGU_HANH_SINH.get(hanh1) == hanh2:
            return 'sinh'
        if cls.NGU_HANH_SINH.get(hanh2) == hanh1:
            return 'bi_sinh'
        if cls.NGU_HANH_KHAC.get(hanh1) == hanh2:
            return 'khac'
        if cls.NGU_HANH_KHAC.get(hanh2) == hanh1:
            return 'bi_khac'
        return 'trung_hoa'  # Không sinh không khắc
    
    @classmethod
    def get_relation_score(cls, hanh1: str, hanh2: str) -> int:
        """
        Tính điểm quan hệ Ngũ Hành
        
        Returns:
            +2: được sinh
            +1: đồng hành
            0: trung hòa
            -1: khắc người
            -2: bị khắc
        """
        relation = cls.get_relation(hanh1, hanh2)
        scores = {
            'bi_sinh': 2,
            'dong': 1,
            'sinh': 0,  # Sinh người = hao
            'trung_hoa': 0,
            'khac': -1,
            'bi_khac': -2
        }
        return scores.get(relation, 0)
    
    @classmethod
    def get_chi_ngu_hanh(cls, chi_index: int) -> str:
        """Lấy Ngũ Hành của Địa Chi (0-11)"""
        return cls.CHI_NGU_HANH.get(chi_index, 'Thổ')
    
    @classmethod
    def get_lac_thu_ngu_hanh(cls, palace_idx: int) -> str:
        """Lấy Ngũ Hành của 9 Cung Lạc Thư (1-9)"""
        return cls.LAC_THU_NGU_HANH.get(palace_idx, 'Thổ')
    
    # Thiên Can → Ngũ Hành
    CAN_NGU_HANH = {
        0: 'Mộc',    # Giáp
        1: 'Mộc',    # Ất
        2: 'Hỏa',    # Bính
        3: 'Hỏa',    # Đinh
        4: 'Thổ',    # Mậu
        5: 'Thổ',    # Kỷ
        6: 'Kim',    # Canh
        7: 'Kim',    # Tân
        8: 'Thủy',   # Nhâm
        9: 'Thủy'    # Quý
    }
    
    # Thiên Can danh sách
    THIEN_CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    
    @classmethod
    def get_can_ngu_hanh(cls, can_index: int) -> str:
        """
        Lấy Ngũ Hành của Thiên Can (0-9)
        
        Args:
            can_index: Index của Thiên Can (0=Giáp, 1=Ất, ..., 9=Quý)
            
        Returns:
            Ngũ Hành tương ứng
        """
        return cls.CAN_NGU_HANH.get(can_index % 10, 'Thổ')
    
    @classmethod
    def get_year_ngu_hanh(cls, year: int) -> dict:
        """
        Tính Ngũ Hành của một năm dựa trên Thiên Can
        
        Công thức:
            - Can index = (year - 4) % 10
            - Hành = Can index // 2 (0-1=Mộc, 2-3=Hỏa, 4-5=Thổ, 6-7=Kim, 8-9=Thủy)
        
        Args:
            year: Năm dương lịch (ví dụ: 2024, 1990, 1985)
            
        Returns:
            Dict chứa thông tin:
                - year: Năm
                - can_index: Index của Thiên Can (0-9)
                - can_name: Tên Thiên Can
                - ngu_hanh: Ngũ Hành của năm
                - am_duong: Âm/Dương (chẵn=Dương, lẻ=Âm)
                
        Ví dụ:
            2024 → Giáp Thìn → Mộc (Dương)
            1990 → Canh Ngọ → Kim (Dương)
            1985 → Ất Sửu → Mộc (Âm)
        """
        can_index = (year - 4) % 10
        ngu_hanh = cls.CAN_NGU_HANH.get(can_index, 'Thổ')
        am_duong = 'Dương' if can_index % 2 == 0 else 'Âm'
        
        return {
            'year': year,
            'can_index': can_index,
            'can_name': cls.THIEN_CAN[can_index],
            'ngu_hanh': ngu_hanh,
            'am_duong': am_duong,
            'full_hanh': f"{am_duong} {ngu_hanh}"
        }
    
    @classmethod
    def analyze_combination(cls, hanh_list: List[str]) -> Dict:
        """
        Phân tích tổ hợp nhiều Ngũ Hành
        
        Args:
            hanh_list: Danh sách các Ngũ Hành
            
        Returns:
            Dict với thống kê và đánh giá
        """
        if not hanh_list:
            return {'score': 0, 'nature': 'neutral'}
        
        # Đếm từng loại
        count = {}
        for h in hanh_list:
            count[h] = count.get(h, 0) + 1
        
        # Tính điểm tổng hợp
        total_score = 0
        for i, h1 in enumerate(hanh_list):
            for h2 in hanh_list[i+1:]:
                total_score += cls.get_relation_score(h1, h2)
        
        return {
            'count': count,
            'total_score': total_score,
            'nature': 'cat' if total_score > 0 else ('hung' if total_score < 0 else 'neutral'),
            'dominant': max(count, key=count.get) if count else None
        }


# Test
if __name__ == '__main__':
    engine = NguHanhEngine()
    
    # Test quan hệ
    print("Kim - Thủy:", engine.get_relation('Kim', 'Thủy'))  # sinh
    print("Kim - Mộc:", engine.get_relation('Kim', 'Mộc'))    # khac
    print("Kim - Hỏa:", engine.get_relation('Kim', 'Hỏa'))    # bi_khac
    
    # Test Địa Chi
    print("\nTý (0):", engine.get_chi_ngu_hanh(0))  # Thủy
    print("Dần (2):", engine.get_chi_ngu_hanh(2))   # Mộc
    
    # Test Lạc Thư
    print("\nCung 1 (Khảm):", engine.get_lac_thu_ngu_hanh(1))  # Thủy
    print("Cung 9 (Ly):", engine.get_lac_thu_ngu_hanh(9))      # Hỏa
    
    # Test Year Ngũ Hành
    print("\n=== Test Ngũ Hành của Năm ===")
    for year in [2024, 2025, 1990, 1985, 1984]:
        result = engine.get_year_ngu_hanh(year)
        print(f"{year}: {result['can_name']} - {result['full_hanh']}")

