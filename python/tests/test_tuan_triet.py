"""
Test file cho Tuần, Triệt và các sao phụ mới bổ sung
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chart import generate_birth_chart
from data import DIA_CHI, THIEN_CAN
from stars import get_tuan_triet_info, place_tuan_triet, place_additional_stars


def test_tuan_calculation():
    """Test tính Tuần theo các năm Can Chi khác nhau"""
    print("=" * 70)
    print("TEST 1: TÍNH TUẦN THEO CAN CHI NĂM")
    print("=" * 70)
    
    # Test cases: (can_index, chi_index, expected_tuan_1, expected_tuan_2, description)
    test_cases = [
        (0, 0, 10, 11, "Giáp Tý → Tuần tại Tuất, Hợi"),
        (1, 1, 10, 11, "Ất Sửu → Tuần tại Tuất, Hợi"),
        (0, 10, 8, 9, "Giáp Tuất → Tuần tại Thân, Dậu"),
        (0, 2, 0, 1, "Giáp Dần → Tuần tại Tý, Sửu"),
        (6, 0, 4, 5, "Canh Tý → Tuần tại Thìn, Tỵ"),
    ]
    
    passed = 0
    failed = 0
    
    for can, chi, exp1, exp2, desc in test_cases:
        try:
            info = get_tuan_triet_info(can, chi)
            actual = info['tuan']['positions']
            
            if actual == [exp1, exp2]:
                print(f"  ✓ PASS: {desc}")
                print(f"          Tuần tại {DIA_CHI[actual[0]]}, {DIA_CHI[actual[1]]}")
                passed += 1
            else:
                print(f"  ✗ FAIL: {desc}")
                print(f"          Expected: {DIA_CHI[exp1]}, {DIA_CHI[exp2]}")
                print(f"          Actual: {DIA_CHI[actual[0]]}, {DIA_CHI[actual[1]]}")
                failed += 1
        except Exception as e:
            print(f"  ✗ ERROR: {desc} - {e}")
            failed += 1
    
    print(f"\n  Result: {passed} passed, {failed} failed")
    return failed == 0


def test_triet_positions():
    """Test vị trí Triệt theo Can năm"""
    print("\n" + "=" * 70)
    print("TEST 2: VỊ TRÍ TRIỆT THEO CAN NĂM")
    print("=" * 70)
    
    # Test cases based on TRIET_POSITION table
    test_cases = [
        (0, (8, 9), "Giáp → Triệt tại Thân, Dậu"),
        (1, (8, 9), "Ất → Triệt tại Thân, Dậu"),
        (2, (6, 7), "Bính → Triệt tại Ngọ, Mùi"),
        (5, (2, 3), "Kỷ → Triệt tại Dần, Mão"),
        (6, (0, 1), "Canh → Triệt tại Tý, Sửu"),
        (8, (10, 11), "Nhâm → Triệt tại Tuất, Hợi"),
    ]
    
    passed = 0
    for can, (exp1, exp2), desc in test_cases:
        info = get_tuan_triet_info(can, 0)  # chi doesn't matter for Triệt
        actual = info['triet']['positions']
        
        if actual == [exp1, exp2]:
            print(f"  ✓ PASS: {desc}")
            passed += 1
        else:
            print(f"  ✗ FAIL: {desc} - Expected {exp1}, {exp2}, got {actual}")
    
    print(f"\n  Result: {passed}/{len(test_cases)} passed")
    return passed == len(test_cases)


def test_additional_stars():
    """Test các sao phụ mới"""
    print("\n" + "=" * 70)
    print("TEST 3: CÁC SAO PHỤ MỚI BỔ SUNG")
    print("=" * 70)
    
    stars = place_additional_stars(0, 2, 3, 'nam')  # Giáp Dần, tháng 3, nam
    
    required_stars = [
        'Cô Thần', 'Quả Tú', 'Thái Phụ', 'Phong Các',
        'Giải Thần', 'Thiên Giải', 'Thiên Đức', 'Nguyệt Đức',
        'Lưu Hà', 'Thiên Y', 'Kiếp Sát', 'Phá Toái', 'Thiên Vu'
    ]
    
    passed = 0
    for star in required_stars:
        if star in stars:
            pos = stars[star]
            print(f"  ✓ {star}: {DIA_CHI[pos]} ({pos})")
            passed += 1
        else:
            print(f"  ✗ {star}: MISSING")
    
    print(f"\n  Result: {passed}/{len(required_stars)} stars found")
    return passed == len(required_stars)


def test_full_chart_with_new_stars():
    """Test lá số hoàn chỉnh có đủ sao mới"""
    print("\n" + "=" * 70)
    print("TEST 4: LÁ SỐ HOÀN CHỈNH VỚI SAO MỚI")
    print("=" * 70)
    
    try:
        # Sinh ngày 28/3/1994, giờ Mão, Nam
        chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
        
        # Check star count
        star_count = len(chart['all_stars'])
        print(f"  Tổng số sao: {star_count}")
        
        # Check Tuần Triệt info
        if 'tuan_triet' in chart:
            tuan_info = chart['tuan_triet']['tuan']
            triet_info = chart['tuan_triet']['triet']
            print(f"  Tuần tại: {', '.join(tuan_info['names'])}")
            print(f"  Triệt tại: {', '.join(triet_info['names'])}")
        else:
            print("  ✗ Thiếu thông tin Tuần Triệt")
            return False
        
        # Check new stars in all_stars
        new_stars = ['Tuần 1', 'Tuần 2', 'Triệt 1', 'Triệt 2', 
                     'Cô Thần', 'Quả Tú', 'Thái Phụ', 'Phong Các',
                     'Giải Thần', 'Thiên Giải', 'Thiên Y', 'Kiếp Sát']
        
        found = 0
        for star in new_stars:
            if star in chart['all_stars']:
                found += 1
        
        print(f"  Sao mới tìm thấy: {found}/{len(new_stars)}")
        
        # Check positions have tuan/triet flags
        tuan_cung_count = sum(1 for p in chart['positions'].values() if p.get('in_tuan'))
        triet_cung_count = sum(1 for p in chart['positions'].values() if p.get('in_triet'))
        print(f"  Số cung bị Tuần: {tuan_cung_count}")
        print(f"  Số cung bị Triệt: {triet_cung_count}")
        
        if star_count >= 90 and found >= 10:
            print("\n  ✓ PASS: Lá số đầy đủ với các sao mới")
            return True
        else:
            print("\n  ✗ FAIL: Thiếu sao")
            return False
            
    except Exception as e:
        import traceback
        print(f"  ✗ ERROR: {e}")
        traceback.print_exc()
        return False


def test_multiple_years():
    """Test nhiều năm sinh khác nhau"""
    print("\n" + "=" * 70)
    print("TEST 5: NHIỀU NĂM SINH KHÁC NHAU")
    print("=" * 70)
    
    test_years = [
        (15, 1, 1960, 0, 'nam', "1960 - Canh Tý"),
        (20, 6, 1975, 6, 'nu', "1975 - Ất Mão"),
        (28, 3, 1994, 3, 'nam', "1994 - Giáp Tuất"),
        (1, 1, 2000, 0, 'nam', "2000 - Canh Thìn"),
        (15, 8, 2010, 9, 'nu', "2010 - Canh Dần"),
    ]
    
    passed = 0
    for day, month, year, hour, gender, desc in test_years:
        try:
            chart = generate_birth_chart(day, month, year, hour, gender)
            tuan_triet = chart.get('tuan_triet', {})
            tuan_names = tuan_triet.get('tuan', {}).get('names', ['?', '?'])
            triet_names = tuan_triet.get('triet', {}).get('names', ['?', '?'])
            
            print(f"  ✓ {desc}")
            print(f"      Năm: {chart['year_can_chi']['full']}")
            print(f"      Tuần: {', '.join(tuan_names)} | Triệt: {', '.join(triet_names)}")
            print(f"      Tổng sao: {len(chart['all_stars'])}")
            passed += 1
        except Exception as e:
            print(f"  ✗ {desc} - Error: {e}")
    
    print(f"\n  Result: {passed}/{len(test_years)} passed")
    return passed == len(test_years)


def run_all_tests():
    """Chạy tất cả test"""
    print("\n")
    print("*" * 70)
    print("*       TEST SUITE: TUẦN, TRIỆT VÀ CÁC SAO PHỤ MỚI              *")
    print("*" * 70)
    
    results = []
    results.append(("Tính Tuần theo Can Chi", test_tuan_calculation()))
    results.append(("Vị trí Triệt", test_triet_positions()))
    results.append(("Các sao phụ mới", test_additional_stars()))
    results.append(("Lá số hoàn chỉnh", test_full_chart_with_new_stars()))
    results.append(("Nhiều năm sinh", test_multiple_years()))
    
    print("\n")
    print("=" * 70)
    print("KẾT QUẢ TỔNG HỢP")
    print("=" * 70)
    
    passed = sum(1 for _, r in results if r)
    failed = sum(1 for _, r in results if not r)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"  [{status}] {name}")
    
    print("-" * 70)
    print(f"  Total: {passed} passed, {failed} failed")
    print("=" * 70)
    
    return failed == 0


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)

