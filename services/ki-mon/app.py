"""
Kì Môn Độn Giáp Service - Microservice tính toán Kì Môn

Port: 5016
Endpoints:
  GET  /ki-mon                  - Trang chủ
  POST /api/ki-mon/calculate    - API tính toán
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

from routes import ki_mon_bp

_templates_dir = os.path.join(paths['python_dir'], 'templates')


def create_app():
    app = Flask(__name__, template_folder=_templates_dir)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(ki_mon_bp)
    return app


if __name__ == '__main__':
    app = create_app()
    print("🏛️ Kì Môn Service running on port 5016")
    app.run(debug=True, port=5016, use_reloader=False)
