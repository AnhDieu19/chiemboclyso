"""
Tu Vi Finder Service - Microservice tìm kiếm ngày giờ sinh

Port: 5012
Endpoints:
  POST /api/v1/finder/solve - Tìm ngày giờ sinh phù hợp
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

from routes import finder_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(finder_bp, url_prefix='/api/v1/finder')
    return app


if __name__ == '__main__':
    app = create_app()
    print("🔍 Tu Vi Finder Service running on port 5012")
    app.run(debug=True, port=5012, use_reloader=False)
