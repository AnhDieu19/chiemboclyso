#!/usr/bin/env python
"""
Run Monolith Mode - Chạy tất cả trong 1 process (giống app cũ)

Backward compatible với backend/app.py
Dùng cho development hoặc khi không cần tách services

Usage:
    python run_monolith.py
"""
import os
import sys

# Setup paths giống backend/app.py
project_root = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(project_root, 'backend')
python_dir = os.path.join(project_root, 'python')

sys.path.insert(0, backend_dir)
sys.path.insert(0, python_dir)
sys.path.insert(0, project_root)

# Set mode to monolith
os.environ['GATEWAY_MODE'] = 'monolith'

# Import and run gateway in monolith mode
sys.path.insert(0, os.path.join(project_root, 'services', 'gateway'))
sys.path.insert(0, os.path.join(project_root, 'services', 'shared'))

from app import main
main()
