"""
Tu Vi Analytics Service - Microservice phân tích Tài Mệnh

Port: 5013
Endpoints:
  POST /api/v1/analytics/tai-menh  - Phân tích Tài Mệnh
  GET  /api/v1/analytics/drilldown - Drilldown data
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'shared'))
from path_setup import setup_service_paths
setup_service_paths()

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), '.env'))

from routes import analytics_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(analytics_bp, url_prefix='/api/v1/analytics')
    return app


if __name__ == '__main__':
    app = create_app()
    print("📊 Tu Vi Analytics Service running on port 5013")
    app.run(debug=True, port=5013, use_reloader=False)
