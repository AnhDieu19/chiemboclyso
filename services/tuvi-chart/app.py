"""
Tu Vi Chart Service - Microservice cho lập lá số Tử Vi

Port: 5011
Endpoints:
  POST /api/v1/chart/generate   - Lập lá số
  GET  /api/v1/chart/star/<name> - Tra cứu sao
  GET  /api/v1/chart/palace/<name> - Tra cứu cung
  POST /api/v1/chart/fortune    - Tính vận hạn
"""
import os
import sys

# Setup paths
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'shared'))
from path_setup import setup_service_paths
setup_service_paths()

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env'))

from routes import chart_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    app.register_blueprint(chart_bp, url_prefix='/api/v1/chart')
    
    return app


if __name__ == '__main__':
    app = create_app()
    print("🔮 Tu Vi Chart Service running on port 5011")
    app.run(debug=True, port=5011, use_reloader=False)
