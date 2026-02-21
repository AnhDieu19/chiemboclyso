"""
Shared Core Module - Re-exports from python/core/

Cung cấp các hàm tính toán cơ bản cho tất cả services
"""
import os
import sys

# Add python/ directory to path for backward compatibility
_python_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'python')
if _python_dir not in sys.path:
    sys.path.insert(0, _python_dir)

from core import *
