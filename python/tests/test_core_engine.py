"""
Core Engine Verification Script
Based on User's Test Cases (TC_01 -> TC_12)
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart.chart_builder import generate_birth_chart
# Updated imports from core package directly
from core import (
    solar_to_lunar, 
    get_hour_can_chi, 
    determine_cuc,
    calculate_luu_nien,
    calculate_luu_nien_tu_hoa
)
from data import THIEN_CAN, DIA_CHI, NAP_AM
import json

def run_tests():
    print("=== CORE ENGINE VERIFICATION ===")
    
    # === TC_01: Convert Dương sang Âm ===
    print("\n[TC_01] Convert Dương -> Âm (28/03/1994)")
    lunar = solar_to_lunar(28, 3, 1994)
    # Expected: 17/02/1994
    if lunar['day'] == 17 and lunar['month'] == 2 and lunar['year'] == 1994:
        print("✅ PASS: Correct Lunar Date (17/02/1994)")
    else:
        print(f"❌ FAIL: Expected 17/02/1994, Got {lunar['day']}/{lunar['month']}/{lunar['year']}")

    # === TC_02: Tính Can Chi Giờ ===
    print("\n[TC_02] Tính Can Chi Giờ (Ngày Quý, Giờ Mão)")
    chart = generate_birth_chart(28, 3, 1994, 3, 'Nam') 
    
    hour_can_chi = chart['hour_can_chi']
    # Expected: Ất Mão
    if 'Ất Mão' in hour_can_chi['full']:
        print("✅ PASS: Giờ Ất Mão")
    else:
        print(f"❌ FAIL: Expected Ất Mão, Got {hour_can_chi['full']}")

    # === TC_03: Tính Cục ===
    print("\n[TC_03] Tính Cục (Can Giáp, Mệnh Tý)")
    cuc_name = chart['cuc']['name']
    # Expected: Thủy Nhị Cục
    if cuc_name == 'Thủy Nhị Cục':
        print("✅ PASS: Thủy Nhị Cục")
    else:
        print(f"❌ FAIL: Expected Thủy Nhị Cục, Got {cuc_name}")

    # === TC_05: Vị trí Tuần - Triệt ===
    print("\n[TC_05] Vị trí Tuần - Triệt (Tuổi Giáp Tuất)")
    positions = chart['positions']
    than_palace = positions[8] # Thân
    dau_palace = positions[9]  # Dậu
    
    # Expected: Tuần/Triệt at Thân & Dậu
    if than_palace.get('in_tuan') and than_palace.get('in_triet'):
        print("✅ PASS: Cung Thân có Tuan & Triet")
    else:
        print(f"❌ FAIL: Cung Thân missing Tuan/Triet (Tuan={than_palace.get('in_tuan')}, Triet={than_palace.get('in_triet')})")
        
    if dau_palace.get('in_tuan') and dau_palace.get('in_triet'):
        print("✅ PASS: Cung Dậu có Tuan & Triet")
    else:
        print(f"❌ FAIL: Cung Dậu missing Tuan/Triet (Tuan={dau_palace.get('in_tuan')}, Triet={dau_palace.get('in_triet')})")

    # === TC_06: Chính tinh tại Mệnh (Tý) ===
    print("\n[TC_06] Chính tinh tại Mệnh (Tý)")
    menh_id = chart['menh_position']
    menh_data = positions[menh_id]
    
    stars_in_menh = [s['name'] if isinstance(s,dict) else s for s in menh_data['stars']]
    brightness = {s['name']: s.get('brightness') for s in menh_data['stars'] if isinstance(s, dict)}
    
    if 'Thiên Lương' in stars_in_menh:
        br = brightness.get('Thiên Lương')
        print(f"✅ PASS: Có Thiên Lương ({br})")
    else:
         print(f"❌ FAIL: Missing Thiên Lương at Mệnh. Found: {stars_in_menh}")

    # === TC_07: Chính tinh tại Thân (Body) ===
    print("\n[TC_07] Chính tinh tại Thân (Body) - Cung Ngọ")
    than_body_pos = chart['than_position']
    than_stars = [s['name'] if isinstance(s,dict) else s for s in positions[than_body_pos]['stars']]
    than_br = {s['name']: s.get('brightness') for s in positions[than_body_pos]['stars'] if isinstance(s, dict)}
    
    if 'Thái Dương' in than_stars:
        print(f"✅ PASS: Có Thái Dương ({than_br.get('Thái Dương')})")
    else:
        print(f"❌ FAIL: Missing Thái Dương at Thân. Found: {than_stars}")

    # === TC_08: Sao đôi tại Tài Bạch (Thân) ===
    print("\n[TC_08] Sao đôi tại Tài Bạch (Thân)")
    tb_stars = [s['name'] if isinstance(s,dict) else s for s in positions[8]['stars']]
    tb_br = {s['name']: s.get('brightness') for s in positions[8]['stars'] if isinstance(s, dict)}
    
    if 'Thiên Cơ' in tb_stars and 'Thái Âm' in tb_stars:
        print(f"✅ PASS: Có Thiên Cơ ({tb_br.get('Thiên Cơ')}) & Thái Âm ({tb_br.get('Thái Âm')})")
    else:
        print(f"❌ FAIL: Missing Cơ/Âm at Thân. Found: {tb_stars}")

    # === TC_09: Vị trí Lộc Tồn ===
    print("\n[TC_09] Vị trí Lộc Tồn (Can Giáp)")
    lt_pos_id = -1
    for pid, pdata in positions.items():
        snames = [s['name'] if isinstance(s,dict) else s for s in pdata['stars']]
        if 'Lộc Tồn' in snames:
            lt_pos_id = pid
            break
            
    if lt_pos_id == 2: # Dần
        print("✅ PASS: Lộc Tồn tại Dần")
    else:
        print(f"❌ FAIL: Expected Dần (2), Got {lt_pos_id} ({DIA_CHI[lt_pos_id] if lt_pos_id >=0 else 'None'})")

    # === PHASE 2: DYNAMIC / LƯU NIÊN ===
    print("\n=== PHASE 2: LƯU NIÊN 2030 (Canh Tuất) ===")
    
    viewing_year = 2030
    
    # TC_11: Lưu Thái Tuế
    print("[TC_11] Lưu Thái Tuế (Năm Tuất)")
    luu_nien = calculate_luu_nien(viewing_year)
    ltt_pos = luu_nien['stars'].get('Lưu Thái Tuế')
    if ltt_pos == 10: # Tuất
        print(f"✅ PASS: Lưu Thái Tuế tại Tuất")
    else:
        print(f"❌ FAIL: Lưu Thái Tuế tại {ltt_pos} (Expected Tuất/10)")
        
    # TC_10: Tứ Hóa Năm Xem (Can Canh)
    print("\n[TC_10] Tứ Hóa Lưu Niên 2030 (Can Canh)")
    # Can Canh: Nhật - Vũ - Âm - Đồng (Lộc Quyền Khoa Kỵ)
    tu_hoa_luu = calculate_luu_nien_tu_hoa(viewing_year, chart['all_stars'])
    
    # Verify mapping
    # Note: Structure of luu_nien_tu_hoa is {'Lưu Hóa Lộc': {'star': ..., 'position': ...}, ...}
    # User expects: Nhật(Lộc)-Vũ(Quyền)-Âm(Khoa)-Đồng(Kỵ)
    
    expected_tu_hoa_map = {
        'Lưu Hóa Lộc': 'Thái Dương',
        'Lưu Hóa Quyền': 'Vũ Khúc',
        'Lưu Hóa Khoa': 'Thái Âm',
        'Lưu Hóa Kỵ': 'Thiên Đồng'
    }
    
    print(f"Debug: Generated Hóa: {list(tu_hoa_luu.keys())}")
    
    pass_th = True
    for hoa_key, expected_star in expected_tu_hoa_map.items():
        if hoa_key in tu_hoa_luu:
            generated_star = tu_hoa_luu[hoa_key]['star']
            if generated_star != expected_star:
                print(f"❌ FAIL: {hoa_key} expected {expected_star}, got {generated_star}")
                pass_th = False
        else:
            print(f"❌ FAIL: Missing {hoa_key}")
            pass_th = False

    if pass_th:
        print("✅ PASS: Tứ Hóa Lưu Niên Can Canh (Nhật-Vũ-Âm-Đồng) Correct")
        
    # TC_12: Lưu Lộc Tồn (Can Canh)
    print("\n[TC_12] Lưu Lộc Tồn (Can Canh -> Cung Thân)")
    if 'Lưu Lộc Tồn' in luu_nien['stars']:
        llt_pos = luu_nien['stars']['Lưu Lộc Tồn']
    else:
        print("⚠️  Lưu Lộc Tồn calculation not found in calculate_luu_nien output.")
        llt_pos = None
        
    if llt_pos == 8: # Thân
        print("✅ PASS: Lưu Lộc Tồn tại Thân")
    elif llt_pos is not None:
        print(f"❌ FAIL: Lưu Lộc Tồn tại {llt_pos} ({DIA_CHI[llt_pos]}) - Expected Thân/8")

if __name__ == '__main__':
    run_tests()
