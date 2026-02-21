
import requests
import json

BASE_URL = "http://localhost:5000"

def test_reverse_lookup():
    print("Testing Reverse Lookup...")
    
    # Case: Find "Canh Ngọ" (1990)
    # Lộc Tồn at Thân (8) -> Year Can = Canh (6)
    # Thái Tuế at Ngọ (6) -> Year Chi = Ngọ (6)
    # Tử Vi at Tỵ (5) (Example, need to check if valid for Canh Ngo)
    # Let's pick a known combo:
    # 1990 (Canh Ngo), Month 1, Day 1, Hour Ty (9-11 -> Tỵ? No, 9-11 is Ty, 09:30 is Ty)
    # Let's just constrain Year.
    
    payload = {
        "stars": {
            "Lộc Tồn": 8,   # Canh -> Thân
            "Thái Tuế": 6   # Ngọ -> Ngọ
        },
        "start_year": 1980,
        "end_year": 2000
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/reverse_lookup", json=payload)
        
        if response.status_code == 200:
            data = response.json()
            results = data.get('results', [])
            count = data.get('count', 0)
            
            print(f"Found {count} results.")
            
            # Check if 1990 is in results
            found_1990 = False
            for r in results:
                if r['lunar']['year'] == 1990:
                    found_1990 = True
                    break
            
            if found_1990:
                print("✅ [PASS] Found 1990 (Canh Ngọ) as expected.")
            else:
                print("❌ [FAIL] 1990 not found in results.")
                if count > 0: print(f"Sample: {results[0]['display']}")
                
        else:
            print(f"❌ [FAIL] API Error: {response.text}")
            
    except Exception as e:
        print(f"❌ [FAIL] Request Failed: {str(e)}")

if __name__ == "__main__":
    test_reverse_lookup()
