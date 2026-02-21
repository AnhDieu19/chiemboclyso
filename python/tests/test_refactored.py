"""
Comprehensive Star Verification Test
Verifies all 89+ stars are correctly defined and placed
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chart import generate_birth_chart
from data import (
    CHINH_TINH, TRUONG_SINH_STARS, BAC_SY_STARS, THAI_TUE_STARS,
    THIEN_CAN, DIA_CHI, TU_HOA_TABLE
)
from interpretation import STAR_MEANINGS, PALACE_MEANINGS

print("=" * 70)
print("      COMPREHENSIVE STAR VERIFICATION TEST")
print("=" * 70)

# Test case
chart = generate_birth_chart(28, 3, 1994, 3, 'nam')

# Count stars
all_stars = chart['all_stars']
total_stars = len(all_stars)
print(f"\n📊 Total unique stars: {total_stars}")

# Verify by category
categories = {
    '14 Chính Tinh': ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh',
                      'Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 
                      'Thất Sát', 'Phá Quân'],
    '6 Cát Tinh': ['Tả Phụ', 'Hữu Bật', 'Văn Xương', 'Văn Khúc', 'Thiên Khôi', 'Thiên Việt'],
    '6 Sát Tinh': ['Kinh Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh', 'Địa Không', 'Địa Kiếp'],
    '12 Trường Sinh': TRUONG_SINH_STARS,
    '12 Bác Sĩ Vòng': BAC_SY_STARS,
    '12 Thái Tuế Vòng': THAI_TUE_STARS,
    'Lộc Tồn & Thiên Mã': ['Lộc Tồn', 'Thiên Mã'],
    'Đào Hoa Group': ['Hồng Loan', 'Thiên Hỹ', 'Đào Hoa', 'Hoa Cái'],
    'Other Stars': ['Thiên Quan', 'Thiên Phúc', 'Thiên Thường', 'Thiên Sứ', 'Phong Cáo',
                    'Quốc Ấn', 'Đường Phù', 'Thiên Thọ', 'Thiên Tài', 'Thiên Diêu',
                    'Thiên La', 'Địa Võng', 'Ân Quang', 'Thiên Quý', 'Thiên Hình',
                    'Tam Thai', 'Bát Tọa', 'Thiên Trù', 'Thiên Khốc', 'Thiên Hư']
}

print("\n📋 Star Category Verification:")
print("-" * 70)

missing_stars = []
for category, expected_stars in categories.items():
    found = [s for s in expected_stars if s in all_stars]
    missing = [s for s in expected_stars if s not in all_stars]
    status = "✓" if len(missing) == 0 else "⚠"
    print(f"  {status} {category}: {len(found)}/{len(expected_stars)}")
    if missing:
        print(f"      Missing: {', '.join(missing)}")
        missing_stars.extend(missing)

# Verify Tứ Hóa
print("\n📋 Tứ Hóa Verification:")
print("-" * 70)
tu_hoa = chart['tu_hoa']
hoa_names = ['Hóa Lộc', 'Hóa Quyền', 'Hóa Khoa', 'Hóa Kỵ']
for hoa in hoa_names:
    if hoa in tu_hoa:
        print(f"  ✓ {hoa}: {tu_hoa[hoa]['star']}")
    else:
        print(f"  ✗ {hoa}: MISSING")

# Verify star meanings
print("\n📋 Star Meanings Verification:")
print("-" * 70)
stars_with_meanings = [s for s in all_stars if s in STAR_MEANINGS]
stars_without_meanings = [s for s in all_stars if s not in STAR_MEANINGS]
print(f"  Stars with meanings: {len(stars_with_meanings)}/{total_stars}")
if stars_without_meanings[:10]:
    print(f"  Stars without meanings (first 10): {', '.join(stars_without_meanings[:10])}...")

# Verify palace meanings
print("\n📋 Palace Meanings Verification:")
print("-" * 70)
from data import CUNG_ORDER
for cung in CUNG_ORDER:
    status = "✓" if cung in PALACE_MEANINGS else "✗"
    print(f"  {status} {cung}")

# Star distribution by palace
print("\n📋 Star Distribution by Palace:")
print("-" * 70)
for i in range(12):
    pos = chart['positions'][i]
    star_count = len(pos['stars'])
    print(f"  {pos['chi']:4} ({pos['cung']:10}): {star_count:2} stars")

# Summary
print("\n" + "=" * 70)
if len(missing_stars) == 0:
    print("🎉 ALL STAR CATEGORIES VERIFIED!")
else:
    print(f"⚠ {len(missing_stars)} stars missing: {', '.join(missing_stars)}")
print("=" * 70)
