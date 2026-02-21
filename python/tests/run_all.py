"""
Master Test Runner
Executes all test scripts in the tests/ directory
"""
import unittest
import os
import sys

# Setting up path to include parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def run_all_tests():
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result

if __name__ == '__main__':
    print("=== TU VI NAM PHAI - TEST RUNNER ===")
    run_all_tests()
