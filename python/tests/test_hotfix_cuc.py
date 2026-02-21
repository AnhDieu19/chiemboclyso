"""
Test script cho HOTFIX Bảng Cục
Chạy: python test_hotfix_cuc.py

Mục đích: Verify bảng CUC_TABLE đã đúng chuẩn Nam Phái
Tham chiếu: HOTFIX_CUC_TABLE.md
"""

import sys
sys.path.insert(0, '.')

from data.cung_cuc import CUC_TABLE

# Bảng chuẩn Nam Phái theo khẩu quyết
# Chú thích: 2=Thủy, 3=Mộc, 4=Kim, 5=Thổ, 6=Hỏa
EXPECTED = {
    # Giáp/Kỷ (0, 5) - "Giáp Kỷ chi niên Bính tác thủ"
    (0, 0): 'Thủy Nhị Cục', (0, 1): 'Hỏa Lục Cục', (0, 2): 'Mộc Tam Cục',
    (0, 3): 'Mộc Tam Cục', (0, 4): 'Kim Tứ Cục', (0, 5): 'Kim Tứ Cục',
    (0, 6): 'Thổ Ngũ Cục', (0, 7): 'Thổ Ngũ Cục', (0, 8): 'Hỏa Lục Cục',
    (0, 9): 'Hỏa Lục Cục', (0, 10): 'Thủy Nhị Cục', (0, 11): 'Thủy Nhị Cục',
    
    # Ất/Canh (1, 6) - "Ất Canh chi niên Mậu tác thủ"
    (1, 0): 'Hỏa Lục Cục', (1, 1): 'Thủy Nhị Cục', (1, 2): 'Kim Tứ Cục',
    (1, 3): 'Kim Tứ Cục', (1, 4): 'Thổ Ngũ Cục', (1, 5): 'Thổ Ngũ Cục',
    (1, 6): 'Hỏa Lục Cục', (1, 7): 'Hỏa Lục Cục', (1, 8): 'Thủy Nhị Cục',
    (1, 9): 'Thủy Nhị Cục', (1, 10): 'Mộc Tam Cục', (1, 11): 'Mộc Tam Cục',
    
    # Bính/Tân (2, 7) - "Bính Tân chi niên Canh tác thủ"
    (2, 0): 'Thủy Nhị Cục', (2, 1): 'Mộc Tam Cục', (2, 2): 'Thổ Ngũ Cục',
    (2, 3): 'Thổ Ngũ Cục', (2, 4): 'Hỏa Lục Cục', (2, 5): 'Hỏa Lục Cục',
    (2, 6): 'Thủy Nhị Cục', (2, 7): 'Thủy Nhị Cục', (2, 8): 'Mộc Tam Cục',
    (2, 9): 'Mộc Tam Cục', (2, 10): 'Kim Tứ Cục', (2, 11): 'Kim Tứ Cục',
    
    # Đinh/Nhâm (3, 8) - "Đinh Nhâm chi niên Nhâm tác thủ"
    (3, 0): 'Mộc Tam Cục', (3, 1): 'Kim Tứ Cục', (3, 2): 'Hỏa Lục Cục',
    (3, 3): 'Hỏa Lục Cục', (3, 4): 'Thủy Nhị Cục', (3, 5): 'Thủy Nhị Cục',
    (3, 6): 'Mộc Tam Cục', (3, 7): 'Mộc Tam Cục', (3, 8): 'Kim Tứ Cục',
    (3, 9): 'Kim Tứ Cục', (3, 10): 'Thổ Ngũ Cục', (3, 11): 'Thổ Ngũ Cục',
    
    # Mậu/Quý (4, 9) - "Mậu Quý chi niên Giáp tác thủ"
    (4, 0): 'Kim Tứ Cục', (4, 1): 'Thổ Ngũ Cục', (4, 2): 'Thủy Nhị Cục',
    (4, 3): 'Thủy Nhị Cục', (4, 4): 'Mộc Tam Cục', (4, 5): 'Mộc Tam Cục',
    (4, 6): 'Kim Tứ Cục', (4, 7): 'Kim Tứ Cục', (4, 8): 'Thổ Ngũ Cục',
    (4, 9): 'Thổ Ngũ Cục', (4, 10): 'Hỏa Lục Cục', (4, 11): 'Hỏa Lục Cục',
}

def test_cuc_table():
    """Test toàn bộ bảng Cục"""
    passed = 0
    failed = 0
    
    chi_names = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 
                 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
    can_names = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 
                 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    
    print("=" * 70)
    print("🧪 TEST HOTFIX BẢNG CỤC - TỬ VI NAM PHÁI")
    print("=" * 70)
    
    # Test từng can chính (0-4)
    for can in range(5):
        print(f"\n📌 Test Can {can_names[can]}/{can_names[can+5]}:")
        for chi in range(12):
            expected = EXPECTED.get((can, chi))
            actual = CUC_TABLE[can][chi]
            
            if actual == expected:
                print(f"   ✅ {chi_names[chi]}: {actual}")
                passed += 1
            else:
                print(f"   ❌ {chi_names[chi]}: Got {actual}, Expected {expected}")
                failed += 1
            
            # Test can đối (5-9) cũng phải giống
            actual_pair = CUC_TABLE[can + 5][chi]
            if actual_pair == expected:
                passed += 1
            else:
                print(f"   ❌ {can_names[can+5]}+{chi_names[chi]}: Got {actual_pair}, Expected {expected}")
                failed += 1
    
    print("\n" + "=" * 70)
    print(f"📊 KẾT QUẢ: {passed} PASSED, {failed} FAILED")
    print("=" * 70)
    
    if failed == 0:
        print("🎉 TẤT CẢ TEST PASSED! Bảng Cục đã đúng chuẩn Nam Phái.")
        return True
    else:
        print("⚠️  CÓ LỖI! Cần kiểm tra lại bảng Cục.")
        return False


def test_quick_verification():
    """Quick test cho lá số mẫu 28/3/1994"""
    print("\n" + "=" * 70)
    print("🔍 QUICK VERIFY: Lá số 28/3/1994, giờ Mão")
    print("=" * 70)
    
    # 28/3/1994 = năm Giáp Tuất, tháng 2 âm, giờ Mão
    # Cung Mệnh tại Tý (index 0)
    # Can năm: Giáp (index 0)
    
    can_index = 0  # Giáp
    chi_menh = 0   # Tý
    
    cuc = CUC_TABLE[can_index][chi_menh]
    expected = 'Thủy Nhị Cục'
    
    if cuc == expected:
        print(f"✅ Cục: {cuc} (Expected: {expected})")
        return True
    else:
        print(f"❌ Cục: {cuc} (Expected: {expected})")
        return False


if __name__ == "__main__":
    test1 = test_cuc_table()
    test2 = test_quick_verification()
    
    if test1 and test2:
        print("\n✅ ALL HOTFIX TESTS PASSED!")
        sys.exit(0)
    else:
        print("\n❌ SOME TESTS FAILED!")
        sys.exit(1)
