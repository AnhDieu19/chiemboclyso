"""Test script - compare chart output with reference (tuvinamphai.vn)"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from chart.chart_builder import generate_birth_chart
from data import DIA_CHI

chart = generate_birth_chart(day=28, month=3, year=1994, hour=3, gender='nam')

print("=" * 60)
print("BASIC INFO")
print("=" * 60)
lunar = chart['lunar_date']
print(f"Lunar: month={lunar['month']}, day={lunar['day']}, year={lunar['year']}")
print(f"Year: {chart['year_can_chi']['full']}")
print(f"Month: {chart['month_can_chi']['full']}")
print(f"Day: {chart['day_can_chi']['full']}")
print(f"Hour: {chart['hour_can_chi']['full']}")
print(f"Menh: {chart['menh_position']} ({DIA_CHI[chart['menh_position']]})")
print(f"Than: {chart['than_position']} ({DIA_CHI[chart['than_position']]})")
print(f"Cuc: {chart['cuc']['name']} (so={chart['cuc']['number']})")
print(f"Nap Am: {chart['nap_am']}")
print(f"Tu Vi pos: {chart['tu_vi_position']} ({DIA_CHI[chart['tu_vi_position']]})")
print(f"Menh Chu: {chart['menh_chu']}")
print(f"Than Chu: {chart['than_chu']}")

print()
print("=" * 60)
print("14 CHINH TINH")
print("=" * 60)
chinh_tinh = chart['chinh_tinh']
for name in sorted(chinh_tinh.keys()):
    pos = chinh_tinh[name]
    print(f"  {name:15s} -> {DIA_CHI[pos]} ({pos})")

print()
print("=" * 60)
print("ALL STARS BY PALACE")
print("=" * 60)

# Reference from tuvinamphai.vn
ref = {
    0: ["Thiên Lương", "Phượng Các", "Giải Thần", "Đẩu Quân", "Tang Môn", "Phúc Bình", "Linh Tinh"],  # Tý - MỆNH
    1: ["Liêm Trinh", "Thất Sát", "Thiếu Âm", "Thiên Khôi", "Đà La", "Hóa Lộc", "Phá Toái", "Quan Phủ"],  # Sửu - PHỤ MẪU
    2: ["Bác Sĩ", "Quan Phù", "Lộc Tồn", "Thiên Diêu", "Thiên Y", "Địa Kiếp", "Long Trì"],  # Dần - PHÚC ĐỨC
    3: ["Nguyệt Đức", "Từ Phù", "Lục Sĩ", "Kinh Dương", "Đào Hoa"],  # Mão - ĐIỀN TRẠCH
    4: ["Thiên Đồng", "Thanh Long", "Tuế Phá", "Thiên Quý", "Thiên La", "Thiên Thọ", "Hỏa Tinh"],  # Thìn - QUAN LỘ
    5: ["Vũ Khúc", "Phá Quân", "Long Đức", "Thiên Thường", "Tiểu Hao", "Hồng Loan", "Tả Phụ", "Bát Tọa", "Phong Cáo", "Thiên Trù", "Hóa Quyền", "Hóa Khoa"],  # Tỵ - NÔ BỘC  
    6: ["Thái Dương", "Bạch Hổ", "Tướng Quân", "Hóa Kỵ", "Kinh Dương"],  # Ngọ - THIÊN DI
    7: ["Thiên Phủ", "Phúc Đức", "Thiên Đức", "Đường Phù", "Thiên Sứ", "Quả Tú", "Tàu Thu", "Văn Khúc", "Văn Xương", "Thiên Việt", "Thiên Quan"],  # Mùi - TẬT ÁCH
    8: ["Thiên Cơ", "Thái Âm", "Thiên Mã", "Điếu Khách", "Phi Liêm", "Địa Không", "Thiên Khốc"],  # Thân - TÀI BẠCH
    9: ["Tử Vi", "Tham Lang", "Hỷ Thần", "Trực Phù", "Thiên Giải", "Lưu Hà", "Tam Thai", "Hữu Bật", "Thái Phụ", "Thiên Phúc"],  # Dậu - TỬ TỨC
    10: ["Cự Môn", "Quốc Ấn", "Hoa Cái", "Bệnh Phù", "Ân Quang", "Thiên Hình", "Thiên Tài", "Thái Tuế"],  # Tuất - PHU THÊ
    11: ["Thiên Tướng", "Thiếu Dương", "Thiên Không", "Cô Thần", "Thiên Hỹ", "Đại Hao", "Kiếp Sát"],  # Hợi - HUYNH ĐỆ
}

cung_names_ref = {
    0: "MỆNH", 1: "PHỤ MẪU", 2: "PHÚC ĐỨC", 3: "ĐIỀN TRẠCH",
    4: "QUAN LỘ", 5: "NÔ BỘC", 6: "THIÊN DI", 7: "TẬT ÁCH",
    8: "TÀI BẠCH", 9: "TỬ TỨC", 10: "PHU THÊ", 11: "HUYNH ĐỆ"
}

all_s = chart.get('all_stars', {})
for i in range(12):
    code_stars = sorted([n for n, p in all_s.items() if p == i])
    ref_stars = sorted(ref.get(i, []))
    
    # Find differences
    code_set = set(code_stars)
    ref_set = set(ref_stars)
    missing = ref_set - code_set  # in ref but not in code
    extra = code_set - ref_set    # in code but not in ref
    
    print(f"\n{DIA_CHI[i]:4s}({i:2d}) - {cung_names_ref.get(i, '?')}")
    print(f"  Code : {code_stars}")
    print(f"  Ref  : {ref_stars}")
    if missing:
        print(f"  MISSING: {sorted(missing)}")
    if extra:
        print(f"  EXTRA  : {sorted(extra)}")
    if not missing and not extra:
        print(f"  ✓ MATCH")
