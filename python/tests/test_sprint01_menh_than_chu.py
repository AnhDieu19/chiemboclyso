"""
Test Mệnh Chủ và Thân Chủ theo TASK-QC-001 trong Sprint 01
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from data.phu_tinh_bo_sung import MENH_CHU_TABLE, THAN_CHU_TABLE
from data import DIA_CHI

print('=' * 60)
print('TEST MỆNH CHỦ VÀ THÂN CHỦ - SPRINT 01')
print('=' * 60)

# Expected values from TASK_SPRINT_01.md
expected_menh = {
    0: 'Tham Lang',   # Tý
    1: 'Cự Môn',      # Sửu
    2: 'Lộc Tồn',     # Dần
    3: 'Văn Khúc',    # Mão
    4: 'Liêm Trinh',  # Thìn
    5: 'Vũ Khúc',     # Tỵ
    6: 'Phá Quân',    # Ngọ
    7: 'Vũ Khúc',     # Mùi
    8: 'Liêm Trinh',  # Thân
    9: 'Văn Khúc',    # Dậu
    10: 'Lộc Tồn',    # Tuất
    11: 'Cự Môn',     # Hợi
}

expected_than = {
    0: 'Linh Tinh',    # Tý
    1: 'Thiên Tướng',  # Sửu
    2: 'Thiên Lương',  # Dần
    3: 'Thiên Đồng',   # Mão
    4: 'Văn Xương',    # Thìn
    5: 'Thiên Cơ',     # Tỵ
    6: 'Hỏa Tinh',     # Ngọ
    7: 'Thiên Tướng',  # Mùi
    8: 'Thiên Lương',  # Thân
    9: 'Thiên Đồng',   # Dậu
    10: 'Văn Xương',   # Tuất
    11: 'Thiên Cơ',    # Hợi
}

print('\n=== TEST MỆNH CHỦ (theo Cung Mệnh) ===')
menh_passed = 0
for i in range(12):
    actual = MENH_CHU_TABLE.get(i, 'N/A')
    exp = expected_menh[i]
    if actual == exp:
        print(f'  ✅ Cung {DIA_CHI[i]}: {actual}')
        menh_passed += 1
    else:
        print(f'  ❌ Cung {DIA_CHI[i]}: Got {actual}, Expected {exp}')

print(f'\n  Result: {menh_passed}/12 passed')

print('\n=== TEST THÂN CHỦ (theo Chi năm) ===')
than_passed = 0
for i in range(12):
    actual = THAN_CHU_TABLE.get(i, 'N/A')
    exp = expected_than[i]
    if actual == exp:
        print(f'  ✅ Chi {DIA_CHI[i]}: {actual}')
        than_passed += 1
    else:
        print(f'  ❌ Chi {DIA_CHI[i]}: Got {actual}, Expected {exp}')

print(f'\n  Result: {than_passed}/12 passed')

print('\n' + '=' * 60)
if menh_passed == 12 and than_passed == 12:
    print('✅ ALL TESTS PASSED!')
else:
    print(f'⚠️  {menh_passed + than_passed}/24 tests passed')
print('=' * 60)


