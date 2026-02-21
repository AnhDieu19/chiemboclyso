"""
Test script: Tao la so va luan giai
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart.chart_builder import generate_birth_chart
from interpretation.meanings import get_star_meaning, get_star_in_palace_meaning, get_than_cu_meaning

# Case tu URL: 28-3-1994, gio Mao, Duong Nam
chart = generate_birth_chart(28, 3, 1994, 4, 'Nam')  # gio 4 = Mao

print('=== LA SO TU VI ===')
print('Ngay: 28-3-1994, Gio: Mao, Duong Nam')
print()

# Thong tin co ban
lunar = chart.get('lunar_date', {})
print('--- THONG TIN CO BAN ---')
print(f"Ngay Am: {lunar.get('day')}/{lunar.get('month')}/{lunar.get('year')}")
cuc = chart.get('cuc', {})
print('Cuc:', cuc.get('name', ''))
print()

# Hien thi tat ca cung
positions = chart.get('positions', {})
print('--- CAC CUNG ---')
for pos_id, pos_data in positions.items():
    cung = pos_data.get('cung', '')
    stars = pos_data.get('stars', [])
    star_names = [s.get('name') if isinstance(s, dict) else s for s in stars[:5]]
    has_than = ' (Than)' if pos_data.get('has_than') else ''
    print(f"{cung}{has_than}: {star_names}")

# Tim cung Menh va luan giai
print()
print('--- LUAN GIAI CUNG MENH ---')
for pos_id, pos_data in positions.items():
    cung_name = pos_data.get('cung', '')
    if 'Mệnh' in cung_name or 'Menh' in cung_name:
        stars = pos_data.get('stars', [])
        for star in stars:
            star_name = star.get('name') if isinstance(star, dict) else star
            meaning = get_star_meaning(star_name)
            if meaning:
                print()
                print(f"SAO {star_name.upper()}:")
                print(f"  Ban chat: {meaning.get('nature', '')}")
                if meaning.get('positive'):
                    print(f"  Tich cuc: {meaning.get('positive', '')}")
                if meaning.get('negative'):
                    print(f"  Tieu cuc: {meaning.get('negative', '')}")
                if meaning.get('detailed'):
                    detail = meaning.get('detailed', '')[:300]
                    print(f"  Luan giai: {detail}...")
        break

# Tim va luan giai Than cu
print()
print('--- LUAN GIAI THAN CU ---')
for pos_id, pos_data in positions.items():
    if pos_data.get('has_than'):
        than_cung = pos_data.get('cung', '')
        print(f"Than cu cung: {than_cung}")
        than_meaning = get_than_cu_meaning(than_cung)
        if than_meaning:
            print(f"  Dac diem: {than_meaning.get('personality', '')}")
            if than_meaning.get('description'):
                desc = than_meaning.get('description', '')[:300]
                print(f"  Mo ta: {desc}...")
            if than_meaning.get('career'):
                print(f"  Nghe nghiep: {than_meaning.get('career', [])}")
        break
