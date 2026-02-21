"""
Ngũ Cách Engine - Tính toán 5 cách trong đặt tên theo Phong Thủy

Ngũ Cách (5 cách) là phương pháp tính số nét chữ Hán trong tên để xác định
vận số tốt/xấu theo Danh Tính học.

Công thức:
- Thiên Cách: Họ + 1  (đại diện cho vận mệnh tiền kiếp, tổ tiên)
- Nhân Cách: Họ + Tên Đệm (đại diện cho tính cách, vận mệnh chủ yếu)
- Địa Cách: Tên Đệm + Tên + 1 (đại diện cho vận mệnh nửa đời trước)
- Ngoại Cách: Họ + Tên (đại diện cho quan hệ xã hội, ngoại giao)
- Tổng Cách: Họ + Tên Đệm + Tên (đại diện cho vận mệnh tổng quát, nửa đời sau)

Nếu không có tên đệm:
- Nhân Cách: Họ + Tên
- Địa Cách: Tên + 1

Số từ 1-81 có ý nghĩa Cát/Hung, số > 81 thì lấy phần dư.
"""

from data.stroke_count import get_stroke_count, HO_STROKE_COUNT, TEN_DEM_STROKE_COUNT, TEN_STROKE_COUNT
from data.ngu_cach_meanings import get_meaning, get_type_display, DAI_CAT, CAT, TRUNG_CAT, HUNG


class NguCachEngine:
    """Engine tính Ngũ Cách đặt tên theo Phong Thủy"""
    
    def __init__(self, ho, dem=None, ten=None, ho_stroke=None, dem_stroke=None, ten_stroke=None):
        """
        Khởi tạo với tên đầy đủ hoặc số nét trực tiếp
        
        Args:
            ho: Họ (ví dụ: "Trần")
            dem: Tên đệm (ví dụ: "Văn"), có thể None nếu không có
            ten: Tên (ví dụ: "Hùng")
            ho_stroke: Số nét của họ (nếu muốn nhập trực tiếp)
            dem_stroke: Số nét của tên đệm
            ten_stroke: Số nét của tên
        """
        self.ho = ho.upper().strip() if ho else ""
        self.dem = dem.upper().strip() if dem else None
        self.ten = ten.upper().strip() if ten else ""
        
        # Ưu tiên số nét được cung cấp, nếu không thì tra cứu
        self.ho_stroke = ho_stroke if ho_stroke is not None else self._lookup_stroke(self.ho, "ho")
        self.dem_stroke = dem_stroke if dem_stroke is not None else (
            self._lookup_stroke(self.dem, "dem") if self.dem else None
        )
        self.ten_stroke = ten_stroke if ten_stroke is not None else self._lookup_stroke(self.ten, "ten")
        
        # Validation
        self._validate()
    
    def _lookup_stroke(self, name, name_type):
        """Tra cứu số nét từ bảng dữ liệu"""
        if not name:
            return None
        return get_stroke_count(name, name_type)
    
    def _validate(self):
        """Kiểm tra dữ liệu đầu vào hợp lệ"""
        errors = []
        
        if self.ho_stroke is None:
            errors.append(f"Không tìm thấy số nét cho họ '{self.ho}'. Vui lòng nhập số nét trực tiếp.")
        
        if self.dem and self.dem_stroke is None:
            errors.append(f"Không tìm thấy số nét cho tên đệm '{self.dem}'. Vui lòng nhập số nét trực tiếp.")
        
        if self.ten_stroke is None:
            errors.append(f"Không tìm thấy số nét cho tên '{self.ten}'. Vui lòng nhập số nét trực tiếp.")
        
        if errors:
            self.validation_errors = errors
        else:
            self.validation_errors = []
    
    def is_valid(self):
        """Kiểm tra xem dữ liệu có hợp lệ để tính toán không"""
        return len(self.validation_errors) == 0
    
    def get_validation_errors(self):
        """Trả về danh sách lỗi validation"""
        return self.validation_errors
    
    def _normalize_number(self, number):
        """Chuẩn hóa số về khoảng 1-81"""
        if number > 81:
            number = number % 81
            if number == 0:
                number = 81
        return number
    
    def get_thien_cach(self):
        """
        Thiên Cách = Họ + 1
        Đại diện cho vận mệnh tiền kiếp, phúc ấm tổ tiên
        """
        if not self.is_valid():
            return None
        
        raw = self.ho_stroke + 1
        normalized = self._normalize_number(raw)
        meaning = get_meaning(normalized)
        
        return {
            "name": "Thiên Cách",
            "formula": f"{self.ho} ({self.ho_stroke}) + 1",
            "raw_value": raw,
            "value": normalized,
            "type": meaning["type"],
            "type_display": get_type_display(meaning["type"]),
            "meaning_name": meaning["name"],
            "meaning": meaning["meaning"],
            "details": meaning["details"]
        }
    
    def get_nhan_cach(self):
        """
        Nhân Cách = Họ + Tên Đệm (hoặc Họ + Tên nếu không có đệm)
        Đại diện cho tính cách, vận mệnh chủ yếu
        """
        if not self.is_valid():
            return None
        
        if self.dem and self.dem_stroke:
            raw = self.ho_stroke + self.dem_stroke
            formula = f"{self.ho} ({self.ho_stroke}) + {self.dem} ({self.dem_stroke})"
        else:
            raw = self.ho_stroke + self.ten_stroke
            formula = f"{self.ho} ({self.ho_stroke}) + {self.ten} ({self.ten_stroke})"
        
        normalized = self._normalize_number(raw)
        meaning = get_meaning(normalized)
        
        return {
            "name": "Nhân Cách",
            "formula": formula,
            "raw_value": raw,
            "value": normalized,
            "type": meaning["type"],
            "type_display": get_type_display(meaning["type"]),
            "meaning_name": meaning["name"],
            "meaning": meaning["meaning"],
            "details": meaning["details"]
        }
    
    def get_dia_cach(self):
        """
        Địa Cách = Tên Đệm + Tên + 1 (hoặc Tên + 1 nếu không có đệm)
        Đại diện cho vận mệnh nửa đời trước (trước 35 tuổi)
        """
        if not self.is_valid():
            return None
        
        if self.dem and self.dem_stroke:
            raw = self.dem_stroke + self.ten_stroke + 1
            formula = f"{self.dem} ({self.dem_stroke}) + {self.ten} ({self.ten_stroke}) + 1"
        else:
            raw = self.ten_stroke + 1
            formula = f"{self.ten} ({self.ten_stroke}) + 1"
        
        normalized = self._normalize_number(raw)
        meaning = get_meaning(normalized)
        
        return {
            "name": "Địa Cách",
            "formula": formula,
            "raw_value": raw,
            "value": normalized,
            "type": meaning["type"],
            "type_display": get_type_display(meaning["type"]),
            "meaning_name": meaning["name"],
            "meaning": meaning["meaning"],
            "details": meaning["details"]
        }
    
    def get_ngoai_cach(self):
        """
        Ngoại Cách = Họ + Tên
        Đại diện cho quan hệ xã hội, ngoại giao
        """
        if not self.is_valid():
            return None
        
        raw = self.ho_stroke + self.ten_stroke
        formula = f"{self.ho} ({self.ho_stroke}) + {self.ten} ({self.ten_stroke})"
        
        normalized = self._normalize_number(raw)
        meaning = get_meaning(normalized)
        
        return {
            "name": "Ngoại Cách",
            "formula": formula,
            "raw_value": raw,
            "value": normalized,
            "type": meaning["type"],
            "type_display": get_type_display(meaning["type"]),
            "meaning_name": meaning["name"],
            "meaning": meaning["meaning"],
            "details": meaning["details"]
        }
    
    def get_tong_cach(self):
        """
        Tổng Cách = Họ + Tên Đệm + Tên (hoặc Họ + Tên nếu không có đệm)
        Đại diện cho vận mệnh tổng quát, nửa đời sau
        """
        if not self.is_valid():
            return None
        
        if self.dem and self.dem_stroke:
            raw = self.ho_stroke + self.dem_stroke + self.ten_stroke
            formula = f"{self.ho} ({self.ho_stroke}) + {self.dem} ({self.dem_stroke}) + {self.ten} ({self.ten_stroke})"
        else:
            raw = self.ho_stroke + self.ten_stroke
            formula = f"{self.ho} ({self.ho_stroke}) + {self.ten} ({self.ten_stroke})"
        
        normalized = self._normalize_number(raw)
        meaning = get_meaning(normalized)
        
        return {
            "name": "Tổng Cách",
            "formula": formula,
            "raw_value": raw,
            "value": normalized,
            "type": meaning["type"],
            "type_display": get_type_display(meaning["type"]),
            "meaning_name": meaning["name"],
            "meaning": meaning["meaning"],
            "details": meaning["details"]
        }
    
    def get_full_analysis(self):
        """
        Phân tích đầy đủ Ngũ Cách
        
        Returns:
            Dict chứa thông tin đầy đủ về 5 cách và đánh giá tổng quan
        """
        if not self.is_valid():
            return {
                "success": False,
                "errors": self.validation_errors,
                "input": {
                    "ho": self.ho,
                    "dem": self.dem,
                    "ten": self.ten
                }
            }
        
        # Tính 5 cách
        thien_cach = self.get_thien_cach()
        nhan_cach = self.get_nhan_cach()
        dia_cach = self.get_dia_cach()
        ngoai_cach = self.get_ngoai_cach()
        tong_cach = self.get_tong_cach()
        
        # Đánh giá tổng quan
        all_cach = [thien_cach, nhan_cach, dia_cach, ngoai_cach, tong_cach]
        
        dai_cat_count = sum(1 for c in all_cach if c["type"] == DAI_CAT)
        cat_count = sum(1 for c in all_cach if c["type"] == CAT)
        trung_cat_count = sum(1 for c in all_cach if c["type"] == TRUNG_CAT)
        hung_count = sum(1 for c in all_cach if c["type"] == HUNG)
        
        # Đánh giá chung
        if dai_cat_count >= 4:
            overall = "RẤT TỐT - Tên có nhiều số Đại Cát"
            overall_type = DAI_CAT
        elif dai_cat_count + cat_count >= 4:
            overall = "TỐT - Tên có nhiều số Cát"
            overall_type = CAT
        elif hung_count >= 3:
            overall = "KHÔNG TỐT - Tên có nhiều số Hung, nên xem xét đổi tên"
            overall_type = HUNG
        else:
            overall = "TRUNG BÌNH - Tên có cả số Cát và Hung"
            overall_type = TRUNG_CAT
        
        # Tên đầy đủ
        if self.dem:
            full_name = f"{self.ho} {self.dem} {self.ten}"
            stroke_info = f"{self.ho_stroke} + {self.dem_stroke} + {self.ten_stroke}"
        else:
            full_name = f"{self.ho} {self.ten}"
            stroke_info = f"{self.ho_stroke} + {self.ten_stroke}"
        
        return {
            "success": True,
            "input": {
                "ho": self.ho,
                "ho_stroke": self.ho_stroke,
                "dem": self.dem,
                "dem_stroke": self.dem_stroke,
                "ten": self.ten,
                "ten_stroke": self.ten_stroke,
                "full_name": full_name,
                "stroke_info": stroke_info
            },
            "ngu_cach": {
                "thien_cach": thien_cach,
                "nhan_cach": nhan_cach,
                "dia_cach": dia_cach,
                "ngoai_cach": ngoai_cach,
                "tong_cach": tong_cach
            },
            "summary": {
                "dai_cat_count": dai_cat_count,
                "cat_count": cat_count,
                "trung_cat_count": trung_cat_count,
                "hung_count": hung_count,
                "overall": overall,
                "overall_type": overall_type,
                "overall_type_display": get_type_display(overall_type)
            }
        }
    
    def print_analysis(self):
        """In kết quả phân tích ra console (tiện cho debug)"""
        result = self.get_full_analysis()
        
        if not result["success"]:
            print("LỖI:", result["errors"])
            return
        
        print("=" * 60)
        print(f"PHÂN TÍCH NGŨ CÁCH: {result['input']['full_name']}")
        print(f"Số nét: {result['input']['stroke_info']}")
        print("=" * 60)
        
        for key in ["thien_cach", "nhan_cach", "dia_cach", "ngoai_cach", "tong_cach"]:
            cach = result["ngu_cach"][key]
            print(f"\n{cach['name']}: {cach['formula']} = {cach['value']} ({cach['type_display']})")
            print(f"  - {cach['meaning_name']}: {cach['meaning']}")
        
        print("\n" + "=" * 60)
        summary = result["summary"]
        print(f"ĐÁNH GIÁ: {summary['overall']}")
        print(f"  - Đại Cát: {summary['dai_cat_count']}, Cát: {summary['cat_count']}, "
              f"Trung Cát: {summary['trung_cat_count']}, Hung: {summary['hung_count']}")
        print("=" * 60)


# Convenience function
def analyze_name(ho, dem=None, ten=None, ho_stroke=None, dem_stroke=None, ten_stroke=None):
    """
    Hàm tiện ích để phân tích nhanh một cái tên
    
    Ví dụ:
        result = analyze_name("Trần", "Văn", "Hùng")
        result = analyze_name("Trần", "Văn", "Hùng", ho_stroke=16, dem_stroke=4, ten_stroke=12)
    """
    engine = NguCachEngine(ho, dem, ten, ho_stroke, dem_stroke, ten_stroke)
    return engine.get_full_analysis()


if __name__ == "__main__":
    # Test với ví dụ từ tài liệu
    print("TEST: TRẦN VĂN HÙNG")
    engine = NguCachEngine("Trần", "Văn", "Hùng", ho_stroke=16, dem_stroke=4, ten_stroke=12)
    engine.print_analysis()
    
    print("\n\nTEST: NGUYỄN THỊ HOA (tự động tra cứu)")
    engine2 = NguCachEngine("Nguyễn", "Thị", "Hoa")
    engine2.print_analysis()
