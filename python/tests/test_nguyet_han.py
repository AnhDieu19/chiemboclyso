
import sys
import os

# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import core.fortune_periods
print(f"DEBUG: core.fortune_periods file: {core.fortune_periods.__file__}")
from core.fortune_periods import calculate_nguyet_han
from data import DIA_CHI

def test_nguyet_han_logic():
    print("Testing Nguyệt Hạn Logic based on docs/Tính Hạn Tháng.md...")
    
    # Input data from docs
    # "Tiểu Hạn năm Tỵ (2025)... nằm tại cung Tý" -> tieu_han_pos = 0 (Tý)
    tieu_han_pos = 0 
    # "Tháng sinh: Tháng 2 âm lịch"
    birth_month = 2
    # "Giờ sinh: Giờ Mão" -> Mão is index 3 (Tý=0, Sửu=1, Dần=2, Mão=3)
    birth_hour_index = 3
    
    print(f"Inputs: Tiểu Hạn={DIA_CHI[tieu_han_pos]}, Month={birth_month}, Hour={DIA_CHI[birth_hour_index]}")
    
    # Expected results from docs
    # "Tháng 1 Âm lịch năm 2025 nằm tại cung DẦN" -> Month 1 = 2 (Dần)
    # "Tháng 10: Hợi" -> Month 10 = 11 (Hợi)
    # "Tháng 11: Tý" -> Month 11 = 0 (Tý)
    
    results = calculate_nguyet_han(tieu_han_pos, birth_month, birth_hour_index)
    
    # Verify Month 1
    m1 = results[0]
    print(f"Month 1: {m1['chi']} (Pos {m1['position']}) - Expected: Dần")
    if m1['position'] == 2:
        print("  -> PASS")
    else:
        print("  -> FAIL")
        
    # Verify Month 10
    m10 = results[9]
    print(f"Month 10: {m10['chi']} (Pos {m10['position']}) - Expected: Hợi")
    if m10['position'] == 11:
        print("  -> PASS")
    else:
        print("  -> FAIL")

    # Verify Month 11
    m11 = results[10]
    print(f"Month 11: {m11['chi']} (Pos {m11['position']}) - Expected: Tý")
    if m11['position'] == 0:
        print("  -> PASS")
    else:
        print("  -> FAIL")

if __name__ == "__main__":
    test_nguyet_han_logic()
