"""Test Tiết Khí Calculator"""
from core.tiet_khi_calculator import (
    calculate_tiet_khi, 
    get_duong_am_don_status,
    format_tiet_khi_info
)

# Test dates
test_dates = [
    (22, 12, 2024, "Đông Chí 2024"),
    (4, 2, 2024, "Lập Xuân 2024"),
    (21, 6, 2024, "Hạ Chí 2024"),
    (15, 1, 2024, "Giữa tháng 1/2024"),
]

print("=" * 80)
print("TESTING TIẾT KHÍ CALCULATOR")
print("=" * 80)

for day, month, year, description in test_dates:
    print(f"\n{description} ({day}/{month}/{year}):")
    print("-" * 80)
    
    tiet_khi = calculate_tiet_khi(year, month, day)
    print(format_tiet_khi_info(tiet_khi))
    print()
