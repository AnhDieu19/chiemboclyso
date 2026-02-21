import unittest
import sys
import os
import json

# Add parent dir to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

class TestAPIContract(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_chart_generate_v1_success(self):
        """Test happy path for chart generation"""
        payload = {
            "year": 1995,
            "month": 6,
            "day": 15,
            "hour": 14,
            "gender": "nam",
            "calendar_type": "solar"
        }
        response = self.client.post('/api/v1/chart/generate', 
                                    data=json.dumps(payload),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check Root Keys
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        
        # Check Data Keys
        resp_data = data['data']
        self.assertIn('basic_info', resp_data)
        self.assertIn('dia_ban', resp_data)
        
        # Check Dia Ban Array
        self.assertIsInstance(resp_data['dia_ban'], list)
        self.assertEqual(len(resp_data['dia_ban']), 12)
        
        # Check items in Dia Ban
        first_palace = resp_data['dia_ban'][0]
        self.assertIn('dia_chi', first_palace)
        self.assertIn('chinh_tinh', first_palace)
        self.assertIn('phu_tinh_tot', first_palace)

    def test_chart_generate_v1_error(self):
        """Test error handling (invalid year)"""
        payload = {
            "year": 1800, # Invalid < 1900
            "month": 1,
            "day": 1,
            "hour": 1
        }
        response = self.client.post('/api/v1/chart/generate', 
                                    data=json.dumps(payload),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
        self.assertIn('message', data)

    def test_finder_solve_v1(self):
        """Test finder response structure"""
        payload = {
            "year": 1990,
            "month": 1,
            "traits": ["hien_lanh"]
        }
        response = self.client.post('/api/v1/finder/solve',
                                    data=json.dumps(payload),
                                    content_type='application/json')
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        self.assertEqual(data['status'], 'success')
        self.assertIn('candidates', data)
        self.assertIn('data', data)

if __name__ == '__main__':
    unittest.main()
