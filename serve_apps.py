"""
Serve all static frontend apps.
Mỗi app static sẽ được serve trên một port riêng.
"""
import os
import sys
import subprocess
import signal
import argparse

# Cấu hình các static apps
STATIC_APPS = {
    'hexagram-viz': {
        'dir': 'hexagram_viz',
        'port': 8081,
        'description': '🔮 Quẻ Dịch Visualization'
    },
    'acupoints-viz': {
        'dir': 'acupoints_viz',
        'port': 8082,
        'description': '📍 Huyệt Đạo 3D'
    },
    'math-viz': {
        'dir': 'math_viz',
        'port': 8083,
        'description': '📐 Toán Lý Số'
    },
    'octonion-viz': {
        'dir': 'octonion_viz',
        'port': 8084,
        'description': '🎱 Bát Nguyên Số'
    }
}

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
processes = []


def start_app(name, config):
    """Start a static app HTTP server."""
    app_dir = os.path.join(PROJECT_ROOT, config['dir'])
    if not os.path.exists(app_dir):
        print(f"  ⚠️  Skipping {name}: directory not found ({config['dir']})")
        return None
    
    port = config['port']
    print(f"  {config['description']}: http://localhost:{port}")
    
    proc = subprocess.Popen(
        [sys.executable, '-m', 'http.server', str(port)],
        cwd=app_dir,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return proc


def shutdown(signum=None, frame=None):
    """Shutdown all app servers."""
    print("\n🛑 Shutting down all frontend apps...")
    for proc in processes:
        if proc and proc.poll() is None:
            proc.terminate()
    for proc in processes:
        if proc and proc.poll() is None:
            proc.wait(timeout=5)
    print("✅ All frontend apps stopped.")
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(description='Serve Tu Vi frontend apps')
    parser.add_argument('--apps', nargs='+', choices=list(STATIC_APPS.keys()),
                        help='Only serve specific apps')
    parser.add_argument('--list', action='store_true',
                        help='List available apps')
    args = parser.parse_args()
    
    if args.list:
        print("📱 Available Frontend Apps:")
        for name, config in STATIC_APPS.items():
            print(f"  {config['description']} ({name}) → port {config['port']}")
        return
    
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)
    
    apps_to_serve = args.apps or list(STATIC_APPS.keys())
    
    print("=" * 50)
    print("📱 Tu Vi Frontend Apps")
    print("=" * 50)
    
    for name in apps_to_serve:
        config = STATIC_APPS[name]
        proc = start_app(name, config)
        if proc:
            processes.append(proc)
    
    print("=" * 50)
    print(f"🚀 {len(processes)} frontend apps running")
    print("   Press Ctrl+C to stop all")
    print("=" * 50)
    
    try:
        for proc in processes:
            proc.wait()
    except KeyboardInterrupt:
        shutdown()


if __name__ == '__main__':
    main()
