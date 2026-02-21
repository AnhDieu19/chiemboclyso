"""
Thái Ất Thần Số Service - Microservice tính toán Thái Ất

Port: 5015
Endpoints:
  GET  /thai-at                  - Trang chủ
  POST /api/thai-at/calculate    - API tính toán
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'shared'))
from path_setup import setup_service_paths
paths = setup_service_paths()

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(paths['project_root'], '.env'))

from routes import thai_at_bp

# Templates are in python/templates/
_templates_dir = os.path.join(paths['python_dir'], 'templates')


def create_app():
    app = Flask(__name__, template_folder=_templates_dir)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(thai_at_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    print("🔢 Thái Ất Service running on port 5015")
    app.run(debug=True, port=5015, use_reloader=False)
