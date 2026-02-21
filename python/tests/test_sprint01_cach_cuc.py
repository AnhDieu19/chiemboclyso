"""
Test Cách Cục theo TASK-QC-002 trong Sprint 01
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from chart import generate_birth_chart
from interpretation import detect_cach_cuc, CACH_CUC_LIST

print('=' * 60)
print('TEST CÁCH CỤC ĐẶC BIỆT - SPRINT 01')
print('=' * 60)

# Test 1: Kiểm tra danh sách Cách Cục
print('\n=== DANH SÁCH CÁCH CỤC ĐƯỢC ĐỊNH NGHĨA ===')
print(f'Tổng số Cách Cục: {len(CACH_CUC_LIST)}')
for cach_id, cach in CACH_CUC_LIST.items():
    print(f"  {cach.get('icon', '✨')} {cach['name']} ({cach['rank']})")

# Test 2: Detect với một lá số mẫu
print('\n=== DETECT CÁCH CỤC - Lá số 28/3/1994 giờ Mão ===')
chart = generate_birth_chart(28, 3, 1994, 3, 'nam')
cach_cuc = detect_cach_cuc(chart)

if cach_cuc:
    print(f'Phát hiện {len(cach_cuc)} cách cục:')
    for cc in cach_cuc:
        print(f"\n  {cc.get('icon', '')} {cc['name']} ({cc['rank']})")
        print(f"     {cc['meaning']}")
else:
    print('Không phát hiện cách cục đặc biệt')

# Test 3: Một số lá số khác
test_cases = [
    (15, 6, 1990, 6, 'nam', "15/6/1990 giờ Ngọ"),
    (1, 1, 2000, 0, 'nam', "1/1/2000 giờ Tý"),
    (20, 8, 1985, 9, 'nu', "20/8/1985 giờ Dậu"),
]

print('\n=== DETECT CÁCH CỤC - CÁC LÁ SỐ KHÁC ===')
for day, month, year, hour, gender, desc in test_cases:
    chart = generate_birth_chart(day, month, year, hour, gender)
    cach_cuc = detect_cach_cuc(chart)
    print(f"\n{desc}: {len(cach_cuc)} cách cục")
    for cc in cach_cuc:
        print(f"  - {cc['name']}")

print('\n' + '=' * 60)
print('TEST COMPLETED')
print('=' * 60)

