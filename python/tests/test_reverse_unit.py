
import unittest
import json
import sys
import os

# Add python dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app

class TestReverseLookup(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_reverse_lookup_canh_ngo(self):
        print("\nTesting Reverse Lookup (Canh Ngọ)...")
        payload = {
            "stars": {
                "Lộc Tồn": 8,   # Canh -> Thân
                "Thái Tuế": 6   # Ngọ -> Ngọ
            },
            "start_year": 1980,
            "end_year": 2000
        }
        
        response = self.app.post('/api/reverse_lookup', 
                               data=json.dumps(payload),
                               content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        results = data.get('results', [])
        print(f"Found {len(results)} results.")
        
        found_1990 = any(r['lunar']['year'] == 1990 for r in results)
        
        if found_1990:
            print("✅ [PASS] Found 1990 (Canh Ngọ)")
        else:
            print("❌ [FAIL] 1990 not found")
            
        self.assertTrue(found_1990)

if __name__ == '__main__':
    unittest.main()
