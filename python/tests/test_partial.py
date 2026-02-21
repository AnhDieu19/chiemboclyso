
import requests
import json
import sys

BASE_URL = "http://localhost:5000"

def test_partial_chart():
    print("Testing Partial Chart Generation...")
    
    # Case 1: Only Year
    payload = {
        "year": 1990,
        "gender": "nam"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/generate", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            chart = data.get('chart', {})
            
            if chart.get('is_partial'):
                print("✅ [PASS] API returned partial chart")
                
                # Verify key stars exist
                stars = chart.get('all_stars', {})
                if 'Thái Tuế' in stars and 'Lộc Tồn' in stars and 'Thiên Mã' in stars:
                    print(f"✅ [PASS] Found Year-based stars: Thái Tuế({stars['Thái Tuế']}), Lộc Tồn({stars['Lộc Tồn']}), Thiên Mã({stars['Thiên Mã']})")
                else: 
                    print("❌ [FAIL] Missing Year-based stars (Thái Tuế, Lộc Tồn or Thiên Mã)")
                    
                # Verify logic is sound (Year 1990 is Canhm)
                # Canh Loc Ton at Than (8)
                # Canh Ngo (Ngo=6) -> Thien Ma at Than (8)
                if stars.get('Lộc Tồn') == 8 and stars.get('Thiên Mã') == 8:
                     print("✅ [PASS] Lộc Tồn and Thiên Mã position correct for Canh Ngọ 1990")
                else:
                     print(f"❌ [FAIL] Lộc Tồn position incorrect: {stars.get('Lộc Tồn')}")
                     
            else:
                print("❌ [FAIL] API did not set is_partial flag")
        else:
            print(f"❌ [FAIL] API Error: {response.text}")
            
    except Exception as e:
        print(f"❌ [FAIL] Request Failed: {str(e)}")
        print("Ensure the server is running!")

if __name__ == "__main__":
    test_partial_chart()
