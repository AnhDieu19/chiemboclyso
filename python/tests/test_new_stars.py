import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python'))

from stars.other_stars_placer import place_year_other_stars, place_month_other_stars
from stars.bo_sung_placer import place_supplementary_stars

def test_new_stars():
    # Test Case: Year Tý (Index 0), Month 1 (Giêng)
    print("Testing Year Tý (0), Month 1...")
    
    # All new stars are now in place_supplementary_stars (stars layer)
    # Arguments: year_chi_index, hour_index, lunar_month, menh_position, than_position
    # Year Tý (0), Month 1. Hour/Menh/Than don't matter for these specific stars except Phuong Cac (Year based)
    
    stars_bosung = place_supplementary_stars(0, 0, 1, 0, 0)
    
    # 1. Tam Giải
    # Thiên Giải: Month 1 -> Thân (8)
    print(f"Thiên Giải: {stars_bosung.get('Thiên Giải')} (Expected 8)")
    
    # Địa Giải: Month 1 -> Mùi (7)
    print(f"Địa Giải: {stars_bosung.get('Địa Giải')} (Expected 7)")
    
    # Giải Thần: Same as Phượng Các. Year Tý -> Phượng Các at Tuất (10).
    print(f"Giải Thần: {stars_bosung.get('Giải Thần')} (Expected 10)")
    
    # 2. Tứ Đức (Thiên/Nguyệt/Phúc) - Nam Phái Standard
    # Year Tý (0) -> Đào Hoa at Dậu (9)
    # Thiên Đức: Year Tý -> Tỵ (5)
    print(f"Thiên Đức: {stars_bosung.get('Thiên Đức')} (Expected 5)")
    
    # Nguyệt Đức: Đào Hoa (9) + 1 = Tuất (10)
    print(f"Nguyệt Đức: {stars_bosung.get('Nguyệt Đức')} (Expected 10)")
    
    # Phúc Đức: Đào Hoa (9) + 9 = 18 % 12 = 6 (Ngọ)
    # Note: Thai Tue Phuc Duc for Year Tý is at Dậu (9). This overwrites it.
    print(f"Phúc Đức: {stars_bosung.get('Phúc Đức')} (Expected 6)")

if __name__ == "__main__":
    test_new_stars()
