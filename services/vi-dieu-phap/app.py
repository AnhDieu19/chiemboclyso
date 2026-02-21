"""
Vi Diệu Pháp Service - Microservice cho Vi Diệu Pháp knowledge graph

Port: 5018
Endpoints:
  GET  /vdp/              - VDP main page
  GET  /vdp/structure     - Structure view
  GET  /vdp/association   - Association view  
  GET  /vdp/root-cause    - Root cause view
  GET  /vdp/api/data      - Full graph data
  GET  /vdp/api/stats     - Statistics
"""
import os
import sys

# Add project root for vi_dieu_phap package
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(project_root, '.env'))

from vi_dieu_phap import vdp_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/vdp/*": {"origins": "*"}})
    app.register_blueprint(vdp_bp, url_prefix='/vdp')
    return app


if __name__ == '__main__':
    app = create_app()
    print("📿 Vi Diệu Pháp Service running on port 5018")
    app.run(debug=True, port=5018, use_reloader=False)
