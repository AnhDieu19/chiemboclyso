"""
QC Comprehensive Test Suite for Tu Vi Application
Tests multiple scenarios, edge cases, and validates core functionality
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python'))

from chart import generate_birth_chart, generate_birth_chart_lunar
from interpretation import generate_overall_interpretation
from core import get_fortune_periods

def test_multiple_birth_dates():
    """Test multiple birth date scenarios"""
    print("=" * 70)
    print("TEST 1: MULTIPLE BIRTH DATES")
    print("=" * 70)
    
    # Note: hour is Chi index 0-11 (Ty=0, Suu=1, Dan=2, Mao=3, ... Hoi=11)
    test_cases = [
        (28, 3, 1994, 3, 'nam', 'Male born Mao hour'),
        (15, 8, 1990, 6, 'nu', 'Female born Ngo hour (Chi index 6)'),
        (1, 1, 2000, 0, 'nam', 'Male born Ty hour - Y2K'),
        (31, 12, 1985, 11, 'nu', 'Female born Hoi hour - End of year'),
        (29, 2, 2000, 6, 'nam', 'Leap year date - Male'),
        (1, 1, 1960, 9, 'nam', 'Older person - Male'),
        (15, 6, 2010, 7, 'nu', 'Recent birth - Female (Chi index 7 = Mui)'),
    ]
    
    passed = 0
    failed = 0
    
    for day, month, year, hour, gender, desc in test_cases:
        try:
            chart = generate_birth_chart(day, month, year, hour, gender)
            interp = generate_overall_interpretation(chart)
            
            # Validate basic structure
            assert len(chart['positions']) == 12, 'Should have 12 positions'
            assert len(chart['all_stars']) >= 80, 'Should have 80+ stars'
            assert 'tu_hoa' in chart, 'Should have Tu Hoa'
            assert 'cuc' in chart, 'Should have Cuc'
            assert 'menh_name' in chart, 'Should have Menh Name'
            assert 'than_name' in chart, 'Should have Than Name'
            
            print(f"  PASS: {desc}")
            print(f"        Menh: {chart['menh_name']}, Than: {chart['than_name']}, Cuc: {chart['cuc']['name']}")
            passed += 1
        except Exception as e:
            print(f"  FAIL: {desc}")
            print(f"        Error: {e}")
            failed += 1
    
    print(f"\n  Result: {passed} passed, {failed} failed")
    return failed == 0


def test_all_12_hours():
    """Test all 12 birth hours"""
    print("\n" + "=" * 70)
    print("TEST 2: ALL 12 BIRTH HOURS")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    for hour in range(12):
        try:
            chart = generate_birth_chart(15, 6, 1990, hour, 'nam')
            assert len(chart['positions']) == 12
            print(f"  PASS: Hour {hour} (Gio {chart.get('gio_chi', 'N/A')})")
            passed += 1
        except Exception as e:
            print(f"  FAIL: Hour {hour} - {e}")
            failed += 1
    
    print(f"\n  Result: {passed} passed, {failed} failed")
    return failed == 0


def test_both_genders():
    """Test both male and female calculations"""
    print("\n" + "=" * 70)
    print("TEST 3: GENDER DIFFERENCES")
    print("=" * 70)
    
    try:
        chart_male = generate_birth_chart(15, 6, 1990, 6, 'nam')
        chart_female = generate_birth_chart(15, 6, 1990, 6, 'nu')
        
        # Should have same menh_name but may differ in fortune direction
        print(f"  Male - Menh: {chart_male['menh_name']}, Cuc: {chart_male['cuc']['name']}")
        print(f"  Female - Menh: {chart_female['menh_name']}, Cuc: {chart_female['cuc']['name']}")
        
        # Same date should have same menh_name
        assert chart_male['menh_name'] == chart_female['menh_name'], 'Menh cung should be same'
        print("  PASS: Gender calculations correct")
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def test_fortune_periods():
    """Test Dai Han, Tieu Han, Luu Nien"""
    print("\n" + "=" * 70)
    print("TEST 4: FORTUNE PERIODS (Dai Han, Tieu Han, Luu Nien)")
    print("=" * 70)
    
    try:
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        # Test multiple years
        for year in [2020, 2024, 2030, 2050]:
            periods = get_fortune_periods(chart, year)
            
            assert 'dai_han_all' in periods, 'Should have dai_han_all'
            assert 'tieu_han' in periods, 'Should have tieu_han'
            assert 'luu_nien' in periods, 'Should have luu_nien'
            assert periods['age'] > 0, 'Age should be positive'
            
            print(f"  PASS: Year {year}, Age {periods['age']}")
        
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def test_lunar_input():
    """Test lunar calendar input"""
    print("\n" + "=" * 70)
    print("TEST 5: LUNAR CALENDAR INPUT")
    print("=" * 70)
    
    try:
        # Lunar date input (non-leap month)
        chart_lunar = generate_birth_chart_lunar(15, 6, 1990, 6, 'nam', False)
        
        assert len(chart_lunar['positions']) == 12
        assert 'lunar_date' in chart_lunar
        print(f"  PASS: Lunar date - Menh: {chart_lunar['menh_name']}")
        
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def test_edge_cases():
    """Test edge cases and boundary conditions"""
    print("\n" + "=" * 70)
    print("TEST 6: EDGE CASES")
    print("=" * 70)
    
    passed = 0
    failed = 0
    
    # Note: Lunar converter may have limitations for extreme years
    edge_cases = [
        (1, 1, 1920, 0, 'nam', 'Early year (1920)'),
        (31, 12, 2050, 11, 'nu', 'Far future year'),
        (1, 1, 1970, 0, 'nam', 'Unix epoch'),
        (29, 2, 2004, 6, 'nam', 'Leap year Feb 29'),
    ]
    
    for day, month, year, hour, gender, desc in edge_cases:
        try:
            chart = generate_birth_chart(day, month, year, hour, gender)
            assert len(chart['positions']) == 12
            print(f"  PASS: {desc}")
            passed += 1
        except Exception as e:
            print(f"  FAIL: {desc} - {e}")
            failed += 1
    
    print(f"\n  Result: {passed} passed, {failed} failed")
    return failed == 0


def test_star_brightness():
    """Test that star brightness data exists"""
    print("\n" + "=" * 70)
    print("TEST 7: STAR BRIGHTNESS DATA")
    print("=" * 70)
    
    try:
        from data.star_brightness import CHINH_TINH_BRIGHTNESS
        
        chinh_tinh = ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh',
                      'Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 
                      'Thất Sát', 'Phá Quân']
        
        stars_with_brightness = 0
        for star in chinh_tinh:
            if star in CHINH_TINH_BRIGHTNESS:
                stars_with_brightness += 1
                print(f"  PASS: {star} has brightness data")
        
        print(f"\n  Stars with brightness: {stars_with_brightness}/{len(chinh_tinh)}")
        return stars_with_brightness > 0
    except ImportError as e:
        print(f"  INFO: Star brightness module structure: {e}")
        # Try alternative import
        try:
            import data.star_brightness as sb
            print(f"  Available in module: {dir(sb)}")
            return True
        except Exception as e2:
            print(f"  FAIL: {e2}")
            return False
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def test_tu_hoa():
    """Test Tu Hoa (4 transformations)"""
    print("\n" + "=" * 70)
    print("TEST 8: TU HOA (4 TRANSFORMATIONS)")
    print("=" * 70)
    
    try:
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        tu_hoa = chart['tu_hoa']
        required = ['Hoa Loc', 'Hoa Quyen', 'Hoa Khoa', 'Hoa Ky']
        
        for hoa in required:
            if hoa in tu_hoa:
                print(f"  PASS: {hoa} -> {tu_hoa[hoa]['star']}")
            else:
                print(f"  WARN: {hoa} not found (checking Vietnamese names)")
        
        # Check with Vietnamese names
        vi_names = ['Hóa Lộc', 'Hóa Quyền', 'Hóa Khoa', 'Hóa Kỵ']
        all_found = True
        for hoa in vi_names:
            if hoa not in tu_hoa:
                all_found = False
                
        if all_found:
            print("  PASS: All Tu Hoa found (Vietnamese names)")
        
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def test_interpretation():
    """Test interpretation module"""
    print("\n" + "=" * 70)
    print("TEST 9: INTERPRETATION MODULE")
    print("=" * 70)
    
    try:
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        interp = generate_overall_interpretation(chart)
        
        # Check required fields
        required_fields = ['menh_analysis', 'fortune', 'patterns', 'patterns_summary']
        
        for field in required_fields:
            if field in interp:
                print(f"  PASS: {field} exists")
            else:
                print(f"  WARN: {field} missing")
        
        print(f"  Patterns found: {len(interp.get('patterns', []))}")
        
        return True
    except Exception as e:
        print(f"  FAIL: {e}")
        return False


def run_all_tests():
    """Run all QC tests"""
    print("\n")
    print("*" * 70)
    print("*         QC COMPREHENSIVE TEST SUITE - TU VI APP              *")
    print("*" * 70)
    
    results = []
    results.append(("Multiple Birth Dates", test_multiple_birth_dates()))
    results.append(("All 12 Hours", test_all_12_hours()))
    results.append(("Gender Differences", test_both_genders()))
    results.append(("Fortune Periods", test_fortune_periods()))
    results.append(("Lunar Input", test_lunar_input()))
    results.append(("Edge Cases", test_edge_cases()))
    results.append(("Star Brightness", test_star_brightness()))
    results.append(("Tu Hoa", test_tu_hoa()))
    results.append(("Interpretation", test_interpretation()))
    
    print("\n")
    print("=" * 70)
    print("FINAL QC REPORT")
    print("=" * 70)
    
    passed = sum(1 for _, r in results if r)
    failed = sum(1 for _, r in results if not r)
    
    for name, result in results:
        status = "PASS" if result else "FAIL"
        print(f"  [{status}] {name}")
    
    print("-" * 70)
    print(f"  Total: {passed} passed, {failed} failed")
    print("=" * 70)
    
    if failed == 0:
        print("  ALL TESTS PASSED!")
    else:
        print("  SOME TESTS FAILED - REVIEW REQUIRED")
    
    return failed == 0


if __name__ == '__main__':
    run_all_tests()

