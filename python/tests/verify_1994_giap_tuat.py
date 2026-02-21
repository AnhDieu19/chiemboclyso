import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'python'))

from chart.chart_builder import generate_birth_chart_lunar
from data import DIA_CHI

from adapters import adapter_chart_response

def verify_1994():
    print("=== VERIFYING CHART: 1994 Giap Tuat, Month 2, Day 17, Hour Mao, Nam ===")
    
    # Input
    year = 1994
    month = 2
    day = 17
    hour_chi_index = 3 # Tý=0, Sửu=1, Dần=2, Mão=3
    gender = 1 # Nam
    
    # Generate
    raw_chart = generate_birth_chart_lunar(day, month, year, hour_chi_index, gender)
    response = adapter_chart_response(raw_chart)
    chart = response['data']
    
    # Analyze
    basic = chart['basic_info']
    print(f"Basic Keys: {list(basic.keys())}")
    print(f"Basic Info: {basic.get('can_chi_nam')} - {basic.get('nap_am')} - {basic.get('cuc')}")
    
    # Check Menh
    menh_pos_name = "Unknown"
    menh_palace = None
    
    for p in chart['dia_ban']:
        if p['cung_name'] == 'Mệnh':
            menh_pos_name = p['dia_chi']
            menh_palace = p
            break
            
    print(f"Mệnh Palace: {menh_pos_name}")
    
    # Check Stars
    print("\n--- Stars Locations ---")
    tu_vi_pos = 'Unknown'
    thien_phu_pos = 'Unknown'
    
    tuan_locs = []
    triet_locs = []
    
    for i, palace in enumerate(chart['dia_ban']):
        names = [s['name'] for s in palace['chinh_tinh']]
        if 'Tử Vi' in names:
            tu_vi_pos = palace['dia_chi']
            print(f"Tử Vi: {palace['cung_name']} ({palace['dia_chi']})")
        if 'Thiên Phủ' in names:
            thien_phu_pos = palace['dia_chi']
            print(f"Thiên Phủ: {palace['cung_name']} ({palace['dia_chi']})")
        if 'Thiên Lương' in names:
            print(f"Thiên Lương: {palace['cung_name']} ({palace['dia_chi']})")
            
        if palace.get('tuan'):
            tuan_locs.append(palace['dia_chi'])
        if palace.get('triet'):
            triet_locs.append(palace['dia_chi'])
            
    print(f"\nTuần Positions: {tuan_locs}")
    print(f"Triệt Positions: {triet_locs}")
    
    print("\n--- COMPARISON WITH IMAGE ---")
    print(f"Mệnh Image: Tý. Code: {menh_pos_name}")
    print(f"Cục Image: Thủy Nhị Cục. Code: {basic.get('cuc')}")
    print(f"Tử Vi Image: Dậu. Code: {tu_vi_pos}")
    print(f"Thiên Phủ Image: Mùi. Code: {thien_phu_pos}")
    
    # Verify exact match
    pass_menh = menh_pos_name == 'Tý'
    pass_cuc = 'Thủy Nhị Cục' in basic.get('cuc', '')
    pass_tuvi = tu_vi_pos == 'Dậu'
    pass_thienphu = thien_phu_pos == 'Mùi'
    
    # Tuan/Triet logic: Should be Thân/Dậu for both (or close)
    # 1994 Giap Tuat -> Tuan at Than/Dau. Triet at Than/Dau.
    pass_tuan = 'Thân' in tuan_locs and 'Dậu' in tuan_locs
    pass_triet = 'Thân' in triet_locs and 'Dậu' in triet_locs
    
    print(f"\nMatch Results:")
    print(f"Mệnh: {pass_menh}")
    print(f"Cục: {pass_cuc}")
    print(f"Tử Vi: {pass_tuvi}")
    print(f"Thiên Phủ: {pass_thienphu}")
    print(f"Tuần (Thân/Dậu): {pass_tuan}")
    print(f"Triệt (Thân/Dậu): {pass_triet}")

if __name__ == "__main__":
    verify_1994()
