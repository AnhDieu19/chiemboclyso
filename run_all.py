#!/usr/bin/env python
"""
Run All Services - Khởi chạy toàn bộ microservices

Usage:
    python run_all.py                           # Chạy tất cả services
    python run_all.py --services tuvi-chart,tuvi-ai  # Chạy một số
    python run_all.py --exclude graph,vi-dieu-phap   # Loại bỏ một số
    python run_all.py --list                    # Liệt kê services
"""
import os
import sys
import time
import signal
import argparse
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
SERVICES_DIR = PROJECT_ROOT / 'services'

# Service definitions: name -> {dir, port, description, icon}
SERVICES = {
    'gateway':       {'port': 5001, 'icon': '🚪', 'desc': 'API Gateway'},
    'tuvi-chart':    {'port': 5011, 'icon': '🔮', 'desc': 'Tu Vi Chart'},
    'tuvi-finder':   {'port': 5012, 'icon': '🔍', 'desc': 'Reverse Finder'},
    'tuvi-analytics':{'port': 5013, 'icon': '📊', 'desc': 'Analytics'},
    'tuvi-ai':       {'port': 5014, 'icon': '🤖', 'desc': 'AI Gemini'},
    'thai-at':       {'port': 5015, 'icon': '🔢', 'desc': 'Thái Ất'},
    'ki-mon':        {'port': 5016, 'icon': '🏛️', 'desc': 'Kì Môn'},
    'graph':         {'port': 5017, 'icon': '🌐', 'desc': 'Knowledge Graph'},
    'vi-dieu-phap':  {'port': 5018, 'icon': '📿', 'desc': 'Vi Diệu Pháp'},
    'luc-nham':      {'port': 5019, 'icon': '🔯', 'desc': 'Đại Lục Nhâm'},
}

processes = []


def start_service(name, info):
    """Start a single microservice as subprocess"""
    service_dir = SERVICES_DIR / name
    app_file = service_dir / 'app.py'
    
    if not app_file.exists():
        print(f"  ⚠ {name}: app.py not found at {app_file}")
        return None
    
    env = os.environ.copy()
    env['PYTHONUNBUFFERED'] = '1'
    env['PYTHONIOENCODING'] = 'utf-8'
    
    proc = subprocess.Popen(
        [sys.executable, str(app_file)],
        cwd=str(service_dir),
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        encoding='utf-8',
        errors='replace'
    )
    
    print(f"  {info['icon']} {name:20s} → port {info['port']} (PID {proc.pid})")
    return proc


def stop_all():
    """Stop all running services"""
    print("\n\nStopping all services...")
    for name, proc in processes:
        if proc and proc.poll() is None:
            proc.terminate()
            print(f"  Stopped {name} (PID {proc.pid})")
    
    # Wait for clean shutdown
    for name, proc in processes:
        if proc:
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                print(f"  Force killed {name}")


def signal_handler(signum, frame):
    stop_all()
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description='Run Tu Vi microservices')
    parser.add_argument('--services', type=str, help='Comma-separated list of services to run')
    parser.add_argument('--exclude', type=str, help='Comma-separated list of services to exclude')
    parser.add_argument('--list', action='store_true', help='List available services')
    parser.add_argument('--no-gateway', action='store_true', help='Skip gateway (run services only)')
    args = parser.parse_args()
    
    if args.list:
        print("Available services:")
        for name, info in SERVICES.items():
            print(f"  {info['icon']} {name:20s} port {info['port']:5d}  {info['desc']}")
        return
    
    # Determine which services to run
    if args.services:
        selected = [s.strip() for s in args.services.split(',')]
        # Always include gateway unless --no-gateway
        if not args.no_gateway and 'gateway' not in selected:
            selected.insert(0, 'gateway')
    else:
        selected = list(SERVICES.keys())
    
    if args.exclude:
        excluded = [s.strip() for s in args.exclude.split(',')]
        selected = [s for s in selected if s not in excluded]
    
    if args.no_gateway:
        selected = [s for s in selected if s != 'gateway']
    
    # Setup signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    
    print("=" * 60)
    print("     TỬ VI ĐẨU SỐ - MICROSERVICES LAUNCHER")
    print("=" * 60)
    print(f"\nStarting {len(selected)} services...\n")
    
    # Start services (gateway last so others are ready)
    gateway_info = None
    for name in selected:
        if name == 'gateway':
            gateway_info = SERVICES[name]
            continue
        if name in SERVICES:
            proc = start_service(name, SERVICES[name])
            if proc:
                processes.append((name, proc))
    
    # Small delay for services to start
    if gateway_info:
        time.sleep(1)
        proc = start_service('gateway', gateway_info)
        if proc:
            processes.append(('gateway', proc))
    
    print(f"\n{'='*60}")
    print(f"  All services started!")
    if gateway_info:
        print(f"  Gateway: http://localhost:5001")
    print(f"  Press Ctrl+C to stop all services")
    print(f"{'='*60}\n")
    
    # Wait for processes
    try:
        while True:
            for name, proc in processes:
                if proc.poll() is not None:
                    print(f"  ⚠ Service {name} exited with code {proc.returncode}")
            time.sleep(2)
    except KeyboardInterrupt:
        stop_all()


if __name__ == '__main__':
    main()
