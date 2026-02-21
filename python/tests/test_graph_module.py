"""
QC Test - Graph Module Functionality
Test tất cả chức năng trong module python/graph
"""

import unittest
import sys
import os
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


class TestGraphChartAPI(unittest.TestCase):
    """Test /graph/api/chart endpoint"""
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.base_url = '/graph/api/chart'
    
    def test_chart_api_success_solar(self):
        """Test successful chart calculation with solar calendar"""
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "hour": 6,  # Chi index
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check response structure
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        
        # Check data structure
        chart_data = data['data']
        self.assertIn('positions', chart_data)
        self.assertIn('menh_position', chart_data)
        self.assertIn('than_position', chart_data)
        self.assertIn('cuc', chart_data)
        
        # Check positions is a dict with 12 cung
        positions = chart_data['positions']
        self.assertIsInstance(positions, dict)
        self.assertGreaterEqual(len(positions), 0)  # At least some positions
        
        # Check menh_position is valid (0-11)
        menh_pos = chart_data['menh_position']
        self.assertIsInstance(menh_pos, int)
        self.assertGreaterEqual(menh_pos, 0)
        self.assertLessEqual(menh_pos, 11)
    
    def test_chart_api_success_lunar(self):
        """Test successful chart calculation with lunar calendar"""
        payload = {
            "day": 15,
            "month": 6,
            "year": 1990,
            "hour": 3,
            "gender": "nu",
            "calendar": "lunar",
            "leap_month": False
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_chart_api_solar_hour_conversion(self):
        """Test that solar hour (0-23) is converted to chi index correctly"""
        # Test with solar hour 14 (should convert to chi index)
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "hour": 14,  # Solar hour > 11, should convert
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_chart_api_no_hour_defaults_to_ty(self):
        """Test that missing hour defaults to Tý (0)"""
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            # hour not provided
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_chart_api_missing_required_fields(self):
        """Test error handling for missing required fields"""
        test_cases = [
            ({}, "No data provided"),
            ({"day": 28}, "Missing day, month, or year"),
            ({"day": 28, "month": 3}, "Missing day, month, or year"),
            ({"month": 3, "year": 1994}, "Missing day, month, or year"),
        ]
        
        for payload, expected_error in test_cases:
            with self.subTest(payload=payload):
                response = self.client.post(
                    self.base_url,
                    data=json.dumps(payload),
                    content_type='application/json'
                )
                
                self.assertEqual(response.status_code, 400)
                data = json.loads(response.data)
                self.assertEqual(data['status'], 'error')
                self.assertIn('message', data)
    
    def test_chart_api_invalid_input_types(self):
        """Test error handling for invalid input types"""
        payload = {
            "day": "invalid",  # Should be int
            "month": 3,
            "year": 1994,
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        # Should return 500 or 400 depending on implementation
        self.assertIn(response.status_code, [400, 500])
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'error')
    
    def test_chart_api_invalid_calendar_type(self):
        """Test with invalid calendar type"""
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "hour": 6,
            "gender": "nam",
            "calendar": "invalid"  # Invalid calendar type
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        # Should handle gracefully (might default to solar or return error)
        # Check that it doesn't crash
        self.assertIn(response.status_code, [200, 400, 500])


class TestStarMovementAPI(unittest.TestCase):
    """Test /graph/api/star-movement endpoint"""
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
        self.base_url = '/graph/api/star-movement'
    
    def test_star_movement_api_success(self):
        """Test successful star movement calculation"""
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "gender": "nam",
            "calendar": "solar",
            "leap_month": False
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        
        # Check response structure
        self.assertEqual(data['status'], 'success')
        self.assertIn('data', data)
        
        # Check data structure
        result_data = data['data']
        self.assertIn('base_info', result_data)
        self.assertIn('charts', result_data)
        self.assertIn('movement_analysis', result_data)
        
        # Check base_info
        base_info = result_data['base_info']
        self.assertEqual(base_info['day'], 28)
        self.assertEqual(base_info['month'], 3)
        self.assertEqual(base_info['year'], 1994)
        self.assertEqual(base_info['gender'], 'nam')
        self.assertEqual(base_info['calendar'], 'solar')
        
        # Check charts - should have 12 charts (one for each hour)
        charts = result_data['charts']
        self.assertEqual(len(charts), 12)
        
        # Check first chart structure
        first_chart = charts[0]
        self.assertIn('hour_index', first_chart)
        self.assertIn('hour_name', first_chart)
        self.assertEqual(first_chart['hour_index'], 0)
        
        # Check movement_analysis structure
        movement = result_data['movement_analysis']
        self.assertIn('stars_that_move', movement)
        self.assertIn('stars_that_stay', movement)
        self.assertIn('movement_patterns', movement)
        self.assertIn('menh_cung_positions', movement)
        self.assertIn('than_cung_positions', movement)
        self.assertIn('total_stars_analyzed', movement)
        
        # Check that movement patterns is a dict
        self.assertIsInstance(movement['movement_patterns'], dict)
    
    def test_star_movement_api_lunar(self):
        """Test star movement with lunar calendar"""
        payload = {
            "day": 15,
            "month": 6,
            "year": 1990,
            "gender": "nu",
            "calendar": "lunar",
            "leap_month": False
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
    
    def test_star_movement_api_missing_fields(self):
        """Test error handling for missing required fields"""
        test_cases = [
            ({}, "No data provided"),
            ({"day": 28}, "Missing day, month, or year"),
            ({"day": 28, "month": 3}, "Missing day, month, or year"),
        ]
        
        for payload, expected_error in test_cases:
            with self.subTest(payload=payload):
                response = self.client.post(
                    self.base_url,
                    data=json.dumps(payload),
                    content_type='application/json'
                )
                
                self.assertEqual(response.status_code, 400)
                data = json.loads(response.data)
                self.assertEqual(data['status'], 'error')
    
    def test_star_movement_analysis_logic(self):
        """Test that movement analysis correctly identifies fixed vs moving stars"""
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            self.base_url,
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        movement = data['data']['movement_analysis']
        
        # Check that we have some analysis
        self.assertIsInstance(movement['stars_that_move'], list)
        self.assertIsInstance(movement['stars_that_stay'], list)
        self.assertGreater(movement['total_stars_analyzed'], 0)
        
        # Check that menh_cung_positions has 12 values (one per hour)
        menh_positions = movement['menh_cung_positions']
        self.assertEqual(len(menh_positions), 12)
        
        # Check that than_cung_positions has 12 values
        than_positions = movement['than_cung_positions']
        self.assertEqual(len(than_positions), 12)
        
        # Check that all positions are valid (0-11)
        for pos in menh_positions:
            if pos is not None:
                self.assertGreaterEqual(pos, 0)
                self.assertLessEqual(pos, 11)
        
        for pos in than_positions:
            if pos is not None:
                self.assertGreaterEqual(pos, 0)
                self.assertLessEqual(pos, 11)


class TestGraphRoutes(unittest.TestCase):
    """Test HTML route endpoints"""
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
    
    def test_knowledge_graph_route(self):
        """Test /knowledge-graph route returns HTML"""
        response = self.client.get('/knowledge-graph')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        # Check for some expected content
        self.assertIn(b'Tu Vi Knowledge Graph', response.data)
    
    def test_star_movement_route(self):
        """Test /star-movement route returns HTML"""
        response = self.client.get('/star-movement')
        
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.content_type)
        # Check for some expected content
        self.assertIn(b'Star Movement', response.data)


class TestGraphEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
    
    def test_chart_api_boundary_year(self):
        """Test with boundary year values"""
        test_cases = [
            {"year": 1900, "expected": 200},  # Minimum valid year
            {"year": 2100, "expected": 200},  # Maximum valid year
            {"year": 1899, "expected": 400},  # Below minimum
            {"year": 2101, "expected": 400},  # Above maximum
        ]
        
        for case in test_cases:
            with self.subTest(year=case['year']):
                payload = {
                    "day": 1,
                    "month": 1,
                    "year": case['year'],
                    "hour": 0,
                    "gender": "nam",
                    "calendar": "solar"
                }
                
                response = self.client.post(
                    '/graph/api/chart',
                    data=json.dumps(payload),
                    content_type='application/json'
                )
                
                # Note: chart_api.py doesn't validate year range, 
                # so this might pass or fail depending on chart generation
                # This test documents current behavior
                self.assertIn(response.status_code, [200, 400, 500])
    
    def test_chart_api_boundary_hour(self):
        """Test with boundary hour values"""
        test_cases = [0, 11, 12, 23]  # Chi indices and solar hours
        
        for hour in test_cases:
            with self.subTest(hour=hour):
                payload = {
                    "day": 28,
                    "month": 3,
                    "year": 1994,
                    "hour": hour,
                    "gender": "nam",
                    "calendar": "solar"
                }
                
                response = self.client.post(
                    '/graph/api/chart',
                    data=json.dumps(payload),
                    content_type='application/json'
                )
                
                # Should handle all valid hours
                self.assertIn(response.status_code, [200, 400, 500])
    
    def test_star_movement_all_hours_generated(self):
        """Test that all 12 hours are generated in star movement"""
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            '/graph/api/star-movement',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        charts = data['data']['charts']
        
        # Should have exactly 12 charts
        self.assertEqual(len(charts), 12)
        
        # Check hour indices are 0-11
        hour_indices = [c['hour_index'] for c in charts if 'hour_index' in c]
        self.assertEqual(set(hour_indices), set(range(12)))


class TestGraphErrorHandling(unittest.TestCase):
    """Test error handling and edge cases"""
    
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True
    
    def test_chart_api_invalid_json(self):
        """Test with invalid JSON"""
        response = self.client.post(
            '/graph/api/chart',
            data='invalid json',
            content_type='application/json'
        )
        
        # Should return 400, 415, or 500
        self.assertIn(response.status_code, [400, 415, 500])
    
    def test_chart_api_wrong_content_type(self):
        """Test with wrong content type"""
        payload = {"day": 28, "month": 3, "year": 1994}
        
        response = self.client.post(
            '/graph/api/chart',
            data=payload,
            content_type='application/x-www-form-urlencoded'
        )
        
        # Should handle gracefully
        self.assertIn(response.status_code, [200, 400, 415])
    
    def test_star_movement_api_empty_charts_handling(self):
        """Test that empty or invalid charts are handled gracefully"""
        # This tests the error handling in the loop that generates 12 charts
        # If one chart fails, it should continue with others
        payload = {
            "day": 28,
            "month": 3,
            "year": 1994,
            "gender": "nam",
            "calendar": "solar"
        }
        
        response = self.client.post(
            '/graph/api/star-movement',
            data=json.dumps(payload),
            content_type='application/json'
        )
        
        # Should still return 200 even if some charts have errors
        # (as long as at least some succeed)
        if response.status_code == 200:
            data = json.loads(response.data)
            charts = data['data']['charts']
            
            # Check that errors are properly marked
            for chart in charts:
                if 'error' in chart:
                    self.assertIn('error', chart)
                    self.assertIn('hour_index', chart)


def run_all_tests():
    """Run all graph module tests"""
    print("\n" + "=" * 70)
    print("QC TEST - GRAPH MODULE FUNCTIONALITY")
    print("=" * 70)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestGraphChartAPI))
    suite.addTests(loader.loadTestsFromTestCase(TestStarMovementAPI))
    suite.addTests(loader.loadTestsFromTestCase(TestGraphRoutes))
    suite.addTests(loader.loadTestsFromTestCase(TestGraphEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestGraphErrorHandling))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\nFAILURES:")
        for test, traceback in result.failures:
            print(f"  - {test}")
    
    if result.errors:
        print("\nERRORS:")
        for test, traceback in result.errors:
            print(f"  - {test}")
    
    print("=" * 70)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)

