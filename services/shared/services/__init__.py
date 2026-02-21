"""
Shared Services Module - Re-exports from python/services/
"""
import os
import sys

_python_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'python')
if _python_dir not in sys.path:
    sys.path.insert(0, _python_dir)

from services import *
