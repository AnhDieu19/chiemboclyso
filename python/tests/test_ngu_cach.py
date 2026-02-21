"""
Unit tests cho module Ngu Cach
Test logic tinh Thien - Nhan - Dia - Ngoai - Tong Cach
"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic.ngu_cach_engine import NguCachEngine, analyze_name
from data.ngu_cach_meanings import get_meaning, get_type_display, DAI_CAT, HUNG


class TestNguCachEngine:
    """Test class NguCachEngine"""
    
    def test_example_tran_van_hung(self):
        """
        Test vi du tu tai lieu: TRAN VAN HUNG
        - TRAN: 16 net
        - VAN: 4 net
        - HUNG: 12 net
        - Thien Cach: 16 + 1 = 17 (Dai Cat)
        - Nhan Cach: 16 + 4 = 20 (Hung)
        - Dia Cach: 12 + 1 = 13 (Dai Cat)  # Tai lieu ghi 12 + 1 cho Dia Cach (chi lay ten)
        - Ngoai Cach: 16 + 12 = 28 (Hung)
        - Tong Cach: 16 + 4 + 12 = 32 (Dai Cat)
        """
        engine = NguCachEngine("Tran", "Van", "Hung", 
                               ho_stroke=16, dem_stroke=4, ten_stroke=12)
        
        assert engine.is_valid()
        
        # Thien Cach = Ho + 1 = 17
        thien = engine.get_thien_cach()
        assert thien["value"] == 17
        assert thien["type"] == DAI_CAT
        
        # Nhan Cach = Ho + Dem = 20
        nhan = engine.get_nhan_cach()
        assert nhan["value"] == 20
        assert nhan["type"] == HUNG
        
        # Dia Cach = Dem + Ten + 1 = 4 + 12 + 1 = 17
        # Luu y: Tai lieu ghi 13 vi chi tinh Ten + 1, nhung cong thuc chuan la Dem + Ten + 1
        # Chung ta dung cong thuc: Dem + Ten + 1 = 17
        dia = engine.get_dia_cach()
        assert dia["value"] == 17  # 4 + 12 + 1 = 17
        
        # Ngoai Cach = Ho + Ten = 28
        ngoai = engine.get_ngoai_cach()
        assert ngoai["value"] == 28
        assert ngoai["type"] == HUNG
        
        # Tong Cach = Ho + Dem + Ten = 32
        tong = engine.get_tong_cach()
        assert tong["value"] == 32
        assert tong["type"] == DAI_CAT
    
    def test_no_middle_name(self):
        """Test truong hop khong co ten dem"""
        engine = NguCachEngine("Nguyen", None, "Hoa",
                               ho_stroke=13, ten_stroke=10)
        
        assert engine.is_valid()
        
        # Thien Cach = Ho + 1 = 14
        thien = engine.get_thien_cach()
        assert thien["value"] == 14
        
        # Nhan Cach = Ho + Ten (vi khong co dem) = 23
        nhan = engine.get_nhan_cach()
        assert nhan["value"] == 23
        
        # Dia Cach = Ten + 1 = 11
        dia = engine.get_dia_cach()
        assert dia["value"] == 11
        
        # Ngoai Cach = Ho + Ten = 23
        ngoai = engine.get_ngoai_cach()
        assert ngoai["value"] == 23
        
        # Tong Cach = Ho + Ten = 23
        tong = engine.get_tong_cach()
        assert tong["value"] == 23
    
    def test_number_normalization(self):
        """Test chuyen so > 81 ve khoang 1-81"""
        # So 82 -> 1, 100 -> 19, 162 -> 81
        engine = NguCachEngine("Nguyen", "Thi", "Lan",
                               ho_stroke=50, dem_stroke=30, ten_stroke=25)
        
        # Tong Cach = 50 + 30 + 25 = 105 -> 105 % 81 = 24
        tong = engine.get_tong_cach()
        assert tong["raw_value"] == 105
        assert tong["value"] == 24  # 105 % 81 = 24
    
    def test_lookup_auto(self):
        """Test tra cuu tu dong so net"""
        engine = NguCachEngine("Nguyen", "Thi", "Hoa")
        
        assert engine.is_valid()
        assert engine.ho_stroke == 13
        assert engine.dem_stroke == 6
        assert engine.ten_stroke == 10
    
    def test_invalid_name_not_found(self):
        """Test ten khong tim thay trong database"""
        engine = NguCachEngine("XYZ", None, "ABC")
        
        assert not engine.is_valid()
        errors = engine.get_validation_errors()
        assert len(errors) > 0
    
    def test_full_analysis(self):
        """Test phan tich day du"""
        result = analyze_name("Tran", "Van", "Hung",
                              ho_stroke=16, dem_stroke=4, ten_stroke=12)
        
        assert result["success"]
        assert result["input"]["full_name"] == "TRAN VAN HUNG"
        assert "ngu_cach" in result
        assert "summary" in result
        
        # Kiem tra summary
        summary = result["summary"]
        assert summary["dai_cat_count"] >= 2  # It nhat 2 Dai Cat
        assert summary["hung_count"] >= 1     # It nhat 1 Hung


class TestNguCachMeanings:
    """Test module ngu_cach_meanings"""
    
    def test_get_meaning_valid(self):
        """Test lay y nghia so hop le"""
        meaning = get_meaning(13)
        assert meaning is not None
        assert meaning["type"] == DAI_CAT
        # Ten chua "Tri" hoac "tue" (tieng Viet co dau)
        assert "tuệ" in meaning["name"].lower() or "trí" in meaning["name"].lower()
    
    def test_get_meaning_81(self):
        """Test so 81 - Hoan nguyen"""
        meaning = get_meaning(81)
        assert meaning is not None
        assert meaning["type"] == DAI_CAT
    
    def test_get_meaning_over_81(self):
        """Test so > 81 duoc chuyen doi"""
        # 82 -> 1
        meaning82 = get_meaning(82)
        meaning1 = get_meaning(1)
        assert meaning82["name"] == meaning1["name"]
        
        # 162 -> 81 (162 % 81 = 0 -> 81)
        meaning162 = get_meaning(162)
        meaning81 = get_meaning(81)
        assert meaning162["name"] == meaning81["name"]
    
    def test_get_type_display(self):
        """Test hien thi loai"""
        # get_type_display tra ve tieng Viet co dau
        assert "Cát" in get_type_display(DAI_CAT)  # "Đại Cát"
        assert get_type_display(HUNG) == "Hung"


class TestStrokeCount:
    """Test module stroke_count"""
    
    def test_common_surnames(self):
        """Test ho pho bien"""
        from data.stroke_count import get_stroke_count
        
        assert get_stroke_count("Nguyen", "ho") == 13
        assert get_stroke_count("TRAN", "ho") == 16
        assert get_stroke_count("Le", "ho") == 7
        assert get_stroke_count("Pham", "ho") == 15
    
    def test_common_names(self):
        """Test ten pho bien"""
        from data.stroke_count import get_stroke_count
        
        assert get_stroke_count("Hung", "ten") == 12
        assert get_stroke_count("Minh", "ten") == 8
        assert get_stroke_count("Hoa", "ten") == 10
        assert get_stroke_count("Lan", "ten") == 21
    
    def test_auto_lookup(self):
        """Test tra cuu tu dong"""
        from data.stroke_count import get_stroke_count
        
        # Tim trong tat ca cac bang
        assert get_stroke_count("Nguyen") == 13  # Ho
        assert get_stroke_count("Van") == 4       # Ten dem
        assert get_stroke_count("Hung") == 12     # Ten
    
    def test_not_found(self):
        """Test khong tim thay"""
        from data.stroke_count import get_stroke_count
        
        assert get_stroke_count("XYZABC") is None


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
