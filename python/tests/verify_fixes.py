
# Test script to verify fixes for Thien Giai and Bac Sy Ring
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from stars.bo_sung_placer import an_bo_tam_giai
from stars.bac_sy_placer import place_bac_sy_ring

def test_thien_giai():
    print("Testing Thiên Giải (Target: Forward from Thân)...")
    # T1: Thân (8)
    # T2: Dậu (9)
    res_t1 = an_bo_tam_giai(1)['Thiên Giải']
    res_t2 = an_bo_tam_giai(2)['Thiên Giải']
    
    print(f"Tháng 1: {res_t1} (Expected 8)")
    print(f"Tháng 2: {res_t2} (Expected 9)")
    
    if res_t1 == 8 and res_t2 == 9:
        print("✅ Thiên Giải PASS")
    else:
        print("❌ Thiên Giải FAIL")

def test_bac_sy_ring():
    print("\nTesting Vòng Bác Sĩ...")
    # Case 1: Giáp Tý (Can 0 - Dương), Nam => Dương Nam => Thuận
    # Lộc Tồn tại Dần (2). Bác Sĩ (2), Lục Sĩ (3)... Phúc Bình (pos 10 -> 2+10=12->0 Tý)
    
    print("Case 1: Giáp (0), Nam (Thuận)")
    stars_1 = place_bac_sy_ring(0, 'Nam')
    pb_1 = stars_1['Phúc Bình']
    print(f"Phúc Bình: {pb_1} (Expected: (2+10)%12 = 0 Tý)")
    
    # Case 2: Ất Sửu (Can 1 - Âm), Nam => Âm Nam => Nghịch
    # Lộc Tồn tại Mão (3). Bác Sĩ (3). Lục Sĩ (2)... Phúc Bình (pos 10 -> 3-10 = -7 -> 5 Tỵ)
    print("Case 2: Ất (1), Nam (Nghịch)")
    stars_2 = place_bac_sy_ring(1, 'Nam')
    pb_2 = stars_2['Phúc Bình']
    print(f"Phúc Bình: {pb_2} (Expected: (3-10)%12 = 5 Tỵ)")
    
    if pb_1 == 0 and pb_2 == 5:
        print("✅ Bác Sĩ Ring PASS")
    else:
        print("❌ Bác Sĩ Ring FAIL")

if __name__ == "__main__":
    test_thien_giai()
    test_bac_sy_ring()
