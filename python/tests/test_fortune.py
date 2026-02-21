"""Test Đại Hạn, Tiểu Hạn, Lưu Niên"""
from chart import generate_birth_chart
from core import get_fortune_periods

# Test case: 28/3/1994, Mão, Nam
chart = generate_birth_chart(28, 3, 1994, 3, 'nam')

# Get fortune periods for 2024
periods = get_fortune_periods(chart, 2024)

print("=" * 60)
print("ĐẠI HẠN - TIỂU HẠN - LƯU NIÊN")
print("=" * 60)

print(f"\n📅 Sinh năm: {periods['birth_year']}")
print(f"📅 Năm xem: {periods['current_year']}")
print(f"🎂 Tuổi (mụ): {periods['age']}")

print("\n" + "=" * 60)
print("ĐẠI HẠN (Vận 10 năm)")
print("=" * 60)

for dh in periods['dai_han_all'][:6]:  # Show first 6
    marker = "👉" if periods['current_dai_han'] and dh['position'] == periods['current_dai_han']['position'] else "  "
    print(f"{marker} {dh['start_age']:2}-{dh['end_age']:2} tuổi: {dh['chi']:5} ({dh['direction']})")

print("\n" + "=" * 60)
print("TIỂU HẠN (Vận năm hiện tại)")
print("=" * 60)

th = periods['tieu_han']
print(f"📌 Tuổi {th['age']}: Tiểu Hạn tại cung {th['chi']} ({th['direction']})")

print("\n" + "=" * 60)
print("LƯU NIÊN (Sao năm 2024)")
print("=" * 60)

ln = periods['luu_nien']
print(f"📅 Năm {ln['year']} ({ln['chi_name']})")
print("\nCác sao Lưu Niên chính:")
for star_name, info in list(ln['stars_detail'].items())[:6]:
    print(f"  • {star_name}: {info['chi']}")

print("\n" + "=" * 60)
print("✅ Đại Hạn, Tiểu Hạn, Lưu Niên hoạt động!")
