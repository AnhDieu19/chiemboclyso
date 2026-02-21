"""
Phase 4: Traceability Matrix Verification
Check that each Feature's files are properly connected
"""
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'python'))

print("=" * 60)
print("PHASE 4: TRACEABILITY MATRIX VERIFICATION")
print("=" * 60)

results = []

def check_feature(name, placer_import, data_import, meaning_file=None):
    """Check a feature's files are connected"""
    status = "OK"
    notes = []
    
    # Check placer
    try:
        exec(f"from stars import {placer_import}")
    except Exception as e:
        status = "FAIL"
        notes.append(f"Placer: {e}")
    
    # Check data
    if data_import:
        try:
            exec(f"from data import {data_import}")
        except Exception as e:
            status = "FAIL"
            notes.append(f"Data: {e}")
    
    # Check meaning file exists
    if meaning_file:
        path = os.path.join(os.getcwd(), 'python', 'data', 'meanings', meaning_file)
        if not os.path.exists(path):
            status = "WARN"
            notes.append(f"Meaning file missing: {meaning_file}")
    
    results.append((name, status, notes))
    print(f"  [{status}] {name}")

print("\n[CHÍNH TINH]")
check_feature("14 Chính Tinh", "place_chinh_tinh", "CHINH_TINH", "chinh_tinh.json")

print("\n[PHỤ TINH - LỤC CÁT]")
check_feature("Lục Cát", "place_luc_cat", "TA_PHU_BASE", "phu_tinh.json")

print("\n[PHỤ TINH - LỤC SÁT]")
check_feature("Lục Sát", "place_luc_sat", "KINH_DA", "phu_tinh.json")

print("\n[VÒNG THÁI TUẾ]")
check_feature("Thái Tuế", "place_thai_tue_ring", "THAI_TUE_STARS", "dai_van.json")

print("\n[VÒNG BÁC SĨ]")
check_feature("Bác Sĩ", "place_bac_sy_ring", "BAC_SY_STARS", "phu_tinh.json")

print("\n[VÒNG TRƯỜNG SINH]")
check_feature("Trường Sinh", "place_truong_sinh", "TRUONG_SINH_STARS", "truong_sinh.json")

print("\n[TỨ HÓA]")
check_feature("Tứ Hóa", "apply_tu_hoa", "TU_HOA_TABLE", "phu_tinh.json")

print("\n[TUẦN TRIỆT]")
check_feature("Tuần/Triệt", "place_tuan_triet", "TRIET_POSITION", None)

print("\n[SAO BỔ SUNG]")
check_feature("Sao Bổ Sung", "place_supplementary_stars", "MENH_CHU_TABLE", "phu_tinh_special.json")

print("\n[CORE - CỤC]")
try:
    from core import determine_cuc
    from data import CUC_TABLE
    print("  [OK] Cục Calculation")
except Exception as e:
    print(f"  [FAIL] Cục: {e}")

print("\n[CORE - MỆNH/THÂN]")
try:
    from core import calculate_cung_menh, calculate_cung_than
    print("  [OK] Mệnh/Thân Calculation")
except Exception as e:
    print(f"  [FAIL] Mệnh/Thân: {e}")

print("\n[CORE - ĐẠI VẬN]")
try:
    from core import get_fortune_periods
    path = os.path.join(os.getcwd(), 'python', 'data', 'meanings', 'dai_van.json')
    if os.path.exists(path):
        print("  [OK] Đại Vận + Meaning File")
    else:
        print("  [WARN] Đại Vận: Missing dai_van.json")
except Exception as e:
    print(f"  [FAIL] Đại Vận: {e}")

print("\n[FINDER]")
try:
    from logic import ReverseLookupEngine
    from data.finder_rules import FINDER_RULES
    print("  [OK] Finder Engine + Rules")
except Exception as e:
    print(f"  [FAIL] Finder: {e}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

ok_count = sum(1 for r in results if r[1] == "OK")
fail_count = sum(1 for r in results if r[1] == "FAIL")
warn_count = sum(1 for r in results if r[1] == "WARN")

print(f"  OK: {ok_count}")
print(f"  WARN: {warn_count}")
print(f"  FAIL: {fail_count}")

if fail_count == 0:
    print("\n[ALL FEATURES CONNECTED CORRECTLY]")
else:
    print("\n[SOME ISSUES FOUND - SEE ABOVE]")
