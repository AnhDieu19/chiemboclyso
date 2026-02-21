import sys
import os
import asyncio
"""
Verify specific user chart (Giáp Tuất 1994)
"""
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.lunar_converter import solar_to_lunar
from chart.chart_builder import generate_birth_chart
from services.gemini_client import get_client, MODEL_NAME

def verify_chart():
    print("=== VERIFYING USER CHART (04/12/2025 DL) ===")
    
    # 1. Inputs from Image
    # Image: Ngày 4[15], Tháng 12[10]. Year 2025. Hour Dần (4:18). Gender: Âm Nữ.
    d, m, y = 4, 12, 2025
    hour = 4 # Dần (3-5h)
    gender = 0 # Nữ (in app convention: 1=Nam, 0=Nữ usually? check code)
    # Check chart_builder convention:
    # Nam: 1, Nữ: 0 (Let's verify via check)
    
    # 2. Generate Chart
    # Note: gender in generate_birth_chart might be "Nam"/"Nữ" string or int?
    # Let's check chart_builder.py signature.
    # def generate_birth_chart(day, month, year, hour, gender_input, viewing_year=None):
    # gender_input: "Nam" or "Nữ" (string) usually.
    
    try:
        # Convert Solar to Lunar first to verify "10/15" match
        lunar_date = solar_to_lunar(d, m, y)
        print(f"Input Solar: {d}/{m}/{y}")
        print(f"Converted Lunar: {lunar_date['day']}/{lunar_date['month']}/{lunar_date['year']}")
        # print(f"Can Chi Ngay: {lunar_date['day_can_chi']}, Thang:...
        
        # Expectation from Image: Ngày 15, Tháng 10.
        
        # Generate Full Chart
        chart = generate_birth_chart(d, m, y, hour, "Nữ")
        
        print("\n--- CORE INFO CHECK ---")
        print(f"Mệnh Palace Position: {chart['menh_position']} ({chart['positions'][chart['menh_position']]['cung']})")
        print(f"Thân Palace Position: {chart['than_position']} ({chart['positions'][chart['than_position']]['cung']})")
        print(f"Cục: {chart['cuc']}")
        print(f"Mệnh Chủ: {chart['menh_chu']}")
        print(f"Thân Chủ: {chart['than_chu']}")
        
        print("\n--- MAJOR STARS POSITIONS ---")
        # List major stars to compare with Image
        targets = ['Tử Vi', 'Thiên Phủ', 'Thái Dương', 'Thái Âm', 'Thiên Lương', 'Phá Quân', 'Thất Sát', 'Tham Lang', 'Thiên Cơ', 'Thiên Đồng', 'Vũ Khúc', 'Cự Môn', 'Liêm Trinh', 'Thiên Tướng']
        
        star_map = {s: "Not Found" for s in targets}
        
        for pos_idx, data in chart['positions'].items():
            p_name = data['cung']
            # Check Tuan/Triet
            tt = []
            if data['in_tuan']: tt.append("TUẦN")
            if data['in_triet']: tt.append("TRIỆT")
            tt_str = " + ".join(tt)
            
            # Check stars
            stars = [s['name'] for s in data['stars']]
            
            # Update targets
            for t in targets:
                if t in stars:
                    star_map[t] = f"{p_name} ({pos_idx})"
            
            # Print if contains targets or Tuần/Triệt
            check_list = [t for t in targets if t in stars]
            if check_list or tt:
                print(f"[{p_name}]: {', '.join(check_list)} {tt_str}")
        
        print("\n--- AI INTERPRETATION (Gemini 2.0 Flash) ---")
        # Reuse 'ask_bad_luck' or direct interpretation?
        # Let's format a prompt manually to test the "Realism" system prompt.
        
        msg = (
            f"Tôi là một người dùng thử nghiệm. Hãy luận giải lá số này cho tôi theo phong cách thực chiến mới.\n"
            f"Thông tin: Nữ, sinh 04/12/2025 Dương lịch. Mệnh Thái Âm tại {chart['positions'][chart['menh_position']]['cung']}.\n"
            f"Cục: {chart['cuc']}. Mệnh Chủ: {chart['menh_chu']}.\n"
            f"Sơ lược các cung:\n"
            f"- Mệnh: {', '.join([s['name'] for s in chart['positions'][chart['menh_position']]['stars']])}\n"
            f"- Tài Bạch: {', '.join([s['name'] for s in chart['positions'][(chart['menh_position']+4)%12]['stars']])}\n"
            f"- Quan Lộc: {', '.join([s['name'] for s in chart['positions'][(chart['menh_position']+8)%12]['stars']])}\n"
            f"Hãy cho tôi biết tính cách, điểm mạnh yếu và vận hạn năm 2025."
        )
        
        client = get_client()
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=msg
        )
        print(response.text)

    except Exception as e:
        print(f"Critical Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    verify_chart()
