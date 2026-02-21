"""
Script verify logic fixes:
1. Check Pattern Sát Phá Tham (scope menh)
2. Check Tuần Triệt impact
3. Check Special combinations
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.lunar_converter import solar_to_lunarth_chart_lunar
from interpretation.chart_analyzer import generate_overall_interpretation
import json

def run_verify():
    print("=== VERIFYING LOGIC FIXES (LUNAR DATE) ===")
    
    # 1. Lá số User: 28/3/1994 Âm Lịch - Giờ Mão
    # Mệnh Cơ Nguyệt Đồng Lương (User nói)
    print("\n[TEST 1] Lá số 28/3/1994 ÂL - Giờ Mão")
    chart = generate_birth_chart_lunar(28, 3, 1994, 4, 'Nam')
    interpretation = generate_overall_interpretation(chart)
    
    patterns = interpretation.get('cach_cuc', [])
    pattern_names = [p['name'] for p in patterns]
    print(f"Cach cuc detected: {pattern_names}")
    
    # DEBUG: Print Menh Stars
    menh_id = [k for k,v in chart['positions'].items() if v.get('is_menh')][0]
    menh_stars_debug = [s['name'] if isinstance(s, dict) else s for s in chart['positions'][menh_id]['stars']]
    print(f"DEBUG: Menh Stars: {menh_stars_debug}")
    
    if 'Sát Phá Liêm Tham' in pattern_names:
        print("❌ FAIL: Still detecting Sát Phá Liêm Tham for custom scope")
    else:
        print("✅ PASS: Sát Phá Liêm Tham ignored (Correct scope)")

    # 2. Check Tuần Triệt tại Tài Bạch (Cung Thân)
    # Cung Tài Bạch của User (Giáp Tuất): Tuổi Giáp -> Tuần tại Thân-Dậu.
    # Cung Tài Bạch ở đâu?
    # Nếu Mệnh Cơ Lương tại Thìn -> Tài Bạch tại Tý (Vô Chính Diệu có Thái Âm chiếu hoặc gì đó?).
    # User nói: "Cung Tài Bạch có sao Thiên Phủ... Gặp Triệt hoặc Tuần".
    # User nói: "Mệnh Cơ Lương".
    # Nếu Mệnh Cơ Lương ở Thìn. Tài Bạch ở Tý. -> Tý không có Tuần Triệt.
    # USER INPUT TEST CASE TRONG PROMPT:
    # "Cung Tài Bạch có sao Thiên Phủ (Kho tàng...)"
    # Nếu user test case là hypothetical?
    # Test case 5: "Cung Tài Bạch có sao Thiên Phủ... Gặp Triệt hoặc Tuần".
    # Tôi sẽ scan các cung xem cung nào có Thiên Phủ + Tuần/Triệt.
    
    print("\n[TEST 2] Scan for Thiên Phủ + Tuần/Triệt impact")
    found_case = False
    for cung, data in interpretation['all_palaces'].items():
        key_stars = data.get('key_stars', [])
        effects = str(data.get('combination_effects', []))
        if 'Thiên Phủ' in key_stars:
            print(f"Found Thiên Phủ at {cung}")
            print(f"Effects: {effects}")
            if 'Tuần' in effects or 'Triệt' in effects:
                print("✅ PASS: Detected Tuần/Triệt impact on Thiên Phủ")
                found_case = True
            
    if not found_case:
        print("⚠️ WARNING: No palace has Thiên Phủ + Tuần/Triệt in this specific chart. Verify logic manually.")
        # Nếu lá số này không có case đó, ta không thể verify pass/fail tự động trừ khi mock data.
        # Tuy nhiên ta check logic chung Tuần Triệt đã hoạt động chưa.
        # Check cung có Tuần hoặc Triệt bất kỳ
        for cung, data in interpretation['all_palaces'].items():
             effects = str(data.get('combination_effects', []))
             if 'Tuần' in effects or 'Triệt' in effects:
                 print(f"✅ PASS GENERAL: Detected Tuần/Triệt at {cung}")
                 break

    # 3. Check Thiên Đồng + Hỏa Tinh
    # Scan xem cung nào có Thiên Đồng + Hỏa Tinh
    print("\n[TEST 3] Check Thiên Đồng + Hỏa/Linh")
    found_td_ht = False
    for cung, data in interpretation['all_palaces'].items():
         effects = str(data.get('combination_effects', []))
         if "Phản vi kỳ cách" in effects and "Thiên Đồng" in effects: 
             # Note: My code text is 'Thiên Đồng gặp Hỏa/Linh: Phản vi kỳ cách'
             print(f"✅ PASS: Detected Thiên Đồng + Hỏa Tinh at {cung}")
             found_td_ht = True
             break
    
    if not found_td_ht:
        # Check if stars exist together
        for ps_id, ps_data in chart['positions'].items():
            stars = [s['name'] if isinstance(s, dict) else s for s in ps_data['stars']]
            if 'Thiên Đồng' in stars and ('Hỏa Tinh' in stars or 'Linh Tinh' in stars):
                print(f"DEBUG: Found Thiên Đồng + Hỏa/Linh at {ps_data['cung']} but Logic NOT triggered?")
                print(f"Stars: {stars}")

if __name__ == '__main__':
    run_verify()
