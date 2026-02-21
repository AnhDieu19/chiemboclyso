"""
Verification Script: Check all imports work correctly
"""
import sys
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'python'))

print("=" * 60)
print("PHASE 2: IMPORT CHAIN VERIFICATION")
print("=" * 60)

errors = []
successes = []

# 1. Check core imports
print("\n[1] Checking core/ imports...")
try:
    from core import (
        solar_to_lunar, get_year_can_chi, get_month_can_chi, get_day_can_chi, get_hour_can_chi,
        calculate_cung_menh, calculate_cung_than, determine_cuc, get_nap_am, get_fortune_periods
    )
    successes.append("core/ - All 10 key imports OK")
except ImportError as e:
    errors.append(f"core/ - ImportError: {e}")

# 2. Check stars imports
print("[2] Checking stars/ imports...")
try:
    from stars import (
        calculate_tuvi_position, place_chinh_tinh, place_luc_cat, place_luc_sat,
        place_truong_sinh, place_bac_sy_ring, place_thai_tue_ring, place_other_stars,
        apply_tu_hoa, place_tuan_triet, place_additional_stars, get_tuan_triet_info,
        place_supplementary_stars, get_menh_than_chu
    )
    successes.append("stars/ - All 14 key imports OK")
except ImportError as e:
    errors.append(f"stars/ - ImportError: {e}")

# 3. Check data imports
print("[3] Checking data/ imports...")
try:
    from data import (
        THIEN_CAN, DIA_CHI, GIO_SINH_RANGE, NAP_AM, CUNG_ORDER, CUC_TABLE,
        CHINH_TINH, TU_HOA_TABLE, STAR_BRIGHTNESS_TABLE, get_star_brightness,
        TRIET_POSITION, CHINH_TINH_DETAILS
    )
    successes.append("data/ - All 12 key imports OK")
except ImportError as e:
    errors.append(f"data/ - ImportError: {e}")

# 4. Check chart imports
print("[4] Checking chart/ imports...")
try:
    from chart import generate_birth_chart, generate_birth_chart_lunar, generate_partial_chart
    successes.append("chart/ - All 3 imports OK")
except ImportError as e:
    errors.append(f"chart/ - ImportError: {e}")

# 5. Check interpretation imports
print("[5] Checking interpretation/ imports...")
try:
    from interpretation import (
        generate_overall_interpretation, STAR_MEANINGS, PALACE_MEANINGS,
        detect_cach_cuc, detect_patterns
    )
    successes.append("interpretation/ - All 5 imports OK")
except ImportError as e:
    errors.append(f"interpretation/ - ImportError: {e}")

# 6. Check adapters
print("[6] Checking adapters.py...")
try:
    from adapters import adapter_chart_response
    successes.append("adapters.py - Import OK")
except ImportError as e:
    errors.append(f"adapters.py - ImportError: {e}")

# 7. Check logic (Finder)
print("[7] Checking logic/ imports...")
try:
    from logic import ReverseLookupEngine
    successes.append("logic/ - ReverseLookupEngine OK")
except ImportError as e:
    errors.append(f"logic/ - ImportError: {e}")

# 8. Check services
print("[8] Checking services/ imports...")
try:
    from services.gemini_client import ask_master_ai
    successes.append("services/ - gemini_client OK")
except ImportError as e:
    errors.append(f"services/ - ImportError: {e}")

print("\n" + "=" * 60)
print("RESULTS")
print("=" * 60)

print(f"\n[SUCCESS] {len(successes)} modules OK:")
for s in successes:
    print(f"  + {s}")

if errors:
    print(f"\n[ERRORS] {len(errors)} issues found:")
    for e in errors:
        print(f"  - {e}")
else:
    print("\n[ALL CLEAR] No import errors detected!")

print("\n" + "=" * 60)
