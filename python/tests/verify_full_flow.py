import sys
import os
import json
sys.path.append(os.path.join(os.getcwd(), 'python'))

from core.lunar_converter import solar_to_lunar
# from chart.chart_builder import build_chart # Function name was wrong
from adapters import adapter_chart_response

def test_full_flow():
    print("=== STARTING END-TO-END VERIFICATION ===")
    
    # 1. Setup Input: Year 1984 (Giap Ty), Month 1, Day 1 (Lunar approximately)
    # Use dict to mock lunar date since that's what build_chart expects mostly (or generate_birth_chart_lunar)
    # Actually build_chart expects "lunar_date" dict in generate_birth_chart but here we are calling build_chart?
    # Wait, build_chart is not exported in chart_builder.py, it calls generate_birth_chart.
    # checking imports: from chart.chart_builder import build_chart -> NameError likely if I don't fix it.
    # Looking at file content: functions are generate_birth_chart, generate_birth_chart_lunar.
    # "build_chart" does not exist in the file content I viewed.
    # I should use generate_birth_chart_lunar.
    
    lunar_date_dict = {'day': 1, 'month': 1, 'year': 1984, 'leap': False}
    solar_date = {"day": 2, "month": 2, "year": 1984} # Dummy
    
    hour_index = 6 # Ngo (11-13h)
    
    # 2. Build Chart
    # Using generate_birth_chart_lunar directly
    from chart.chart_builder import generate_birth_chart_lunar
    print("Building chart for Year Tý, Month 1...")
    chart = generate_birth_chart_lunar(lunar_day=1, lunar_month=1, lunar_year=1984, hour=6, gender=1) 
    
    # 3. Convert to JSON dict
    print("Adapting to JSON...")
    # NOTE: adapter_chart_response returns {status: ..., data: {...}}
    response = adapter_chart_response(chart)
    data = response['data']
    
    # 4. Search for New Stars in the Output
    target_stars = ["Thiên Giải", "Địa Giải", "Giải Thần", "Thiên Đức", "Nguyệt Đức", "Phúc Đức"]
    found_stars = {star: [] for star in target_stars}
    
    # Loop through 12 Palaces (dia_ban)
    for palace in data['dia_ban']:
        palace_name = palace['cung_name']
        
        # Check chinh tinh
        # Check chinh tinh
        for star in palace['chinh_tinh']:
            if star['name'] == 'Thiên Phủ':
                print(f"[CHECK] Thiên Phủ at: {palace_name} ({palace['dia_chi']})")
            
            if star['name'] in target_stars:
                 found_stars[star['name']].append(palace_name)
                 
        # Check phu tinh tot
        for star in palace['phu_tinh_tot']:
             if star['name'] in target_stars:
                 found_stars[star['name']].append(palace_name)
                 
        # Check Tuan/Triet
        if palace.get('tuan'):
            print(f"[CHECK] Tuần at: {palace_name} ({palace['dia_chi']})")
        if palace.get('triet'):
            print(f"[CHECK] Triệt at: {palace_name} ({palace['dia_chi']})")

    print(f"[CHECK] Cục: {data['basic_info']['cuc']}")

    # 5. Report Results
    all_passed = True
    print("\n--- RESULTS ---")
    for star, locations in found_stars.items():
        if locations:
            print(f"[PASS] {star}: Found in {locations}")
        else:
            print(f"[FAIL] {star}: NOT FOUND in chart!")
            all_passed = False
            
    if all_passed:
        print("\n>>> SUCCESS: All new stars are present in the API response structure. <<<")
    else:
        print("\n>>> FAILURE: Some stars are missing. Check star placer or list definitions. <<<")

if __name__ == "__main__":
    test_full_flow()
