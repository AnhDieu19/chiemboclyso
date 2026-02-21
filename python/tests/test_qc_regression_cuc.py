"""
TASK-QC-HF-01: Regression Test Cục
Test toàn diện 60 test cases (5 nhóm Can x 12 Cung Mệnh)
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.')

from data.cung_cuc import CUC_TABLE

# Tên Cục
CUC_NAMES = {
    2: 'Thủy Nhị Cục',
    3: 'Mộc Tam Cục',
    4: 'Kim Tứ Cục',
    5: 'Thổ Ngũ Cục',
    6: 'Hỏa Lục Cục'
}

# Bảng chuẩn theo tài liệu BA
EXPECTED_CUC = {
    # Giáp/Kỷ (Can 0, 5)
    'Giáp/Kỷ': [2, 6, 3, 3, 4, 4, 5, 5, 6, 6, 2, 2],
    # Ất/Canh (Can 1, 6)
    'Ất/Canh': [6, 2, 4, 4, 5, 5, 6, 6, 2, 2, 3, 3],
    # Bính/Tân (Can 2, 7)
    'Bính/Tân': [2, 3, 5, 5, 6, 6, 2, 2, 3, 3, 4, 4],
    # Đinh/Nhâm (Can 3, 8)
    'Đinh/Nhâm': [3, 4, 6, 6, 2, 2, 3, 3, 4, 4, 5, 5],
    # Mậu/Quý (Can 4, 9)
    'Mậu/Quý': [4, 5, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
}

CHI_NAMES = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
CAN_PAIRS = [
    ('Giáp/Kỷ', 0, 5),
    ('Ất/Canh', 1, 6),
    ('Bính/Tân', 2, 7),
    ('Đinh/Nhâm', 3, 8),
    ('Mậu/Quý', 4, 9),
]

def run_regression_test():
    """Chạy 60 test cases"""
    print("=" * 70)
    print("TASK-QC-HF-01: REGRESSION TEST CỤC - 60 TEST CASES")
    print("=" * 70)
    
    total_passed = 0
    total_failed = 0
    failed_cases = []
    
    for can_pair_name, can1, can2 in CAN_PAIRS:
        print(f"\n📌 Test Can {can_pair_name}:")
        print("-" * 60)
        
        expected_values = EXPECTED_CUC[can_pair_name]
        
        for chi in range(12):
            expected_cuc_num = expected_values[chi]
            expected_cuc_name = CUC_NAMES[expected_cuc_num]
            
            # Test Can 1
            actual1 = CUC_TABLE[can1][chi]
            match1 = actual1 == expected_cuc_name
            
            # Test Can 2 (đối)
            actual2 = CUC_TABLE[can2][chi]
            match2 = actual2 == expected_cuc_name
            
            if match1 and match2:
                print(f"   [PASS] {CHI_NAMES[chi]:4}: {expected_cuc_name}")
                total_passed += 2
            else:
                if not match1:
                    print(f"   [FAIL] Can{can1}+{CHI_NAMES[chi]}: Got '{actual1}', Expected '{expected_cuc_name}'")
                    failed_cases.append(f"Can{can1}+{CHI_NAMES[chi]}")
                    total_failed += 1
                else:
                    total_passed += 1
                    
                if not match2:
                    print(f"   [FAIL] Can{can2}+{CHI_NAMES[chi]}: Got '{actual2}', Expected '{expected_cuc_name}'")
                    failed_cases.append(f"Can{can2}+{CHI_NAMES[chi]}")
                    total_failed += 1
                else:
                    total_passed += 1
    
    # Tổng kết
    print("\n" + "=" * 70)
    print("KẾT QUẢ REGRESSION TEST")
    print("=" * 70)
    print(f"   Passed: {total_passed}/120")
    print(f"   Failed: {total_failed}/120")
    print(f"   Tỷ lệ:  {total_passed/120*100:.1f}%")
    
    if failed_cases:
        print(f"\n   Các cases thất bại:")
        for fc in failed_cases[:10]:
            print(f"      - {fc}")
        if len(failed_cases) > 10:
            print(f"      ... và {len(failed_cases) - 10} cases khác")
    
    print("=" * 70)
    
    if total_failed == 0:
        print("🎉 TẤT CẢ 120 TEST CASES ĐỀU PASSED!")
        print("   Bảng Cục đã đúng chuẩn Tử Vi Nam Phái.")
        return True
    else:
        print("⚠️  CÓ LỖI! Cần kiểm tra lại bảng Cục.")
        return False


if __name__ == '__main__':
    success = run_regression_test()
    sys.exit(0 if success else 1)

