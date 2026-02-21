"""
Tu Vi AI Service - Microservice tích hợp Gemini AI

Port: 5014
Endpoints:
  POST /api/v1/ai/ask  - Hỏi AI luận giải
  POST /api/v1/ai/chat - Chat với AI
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

from routes import ai_bp


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['GEMINI_API_KEY'] = os.environ.get('GEMINI_API_KEY', '')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.register_blueprint(ai_bp, url_prefix='/api/v1/ai')
    return app


if __name__ == '__main__':
    app = create_app()
    print("🤖 Tu Vi AI Service running on port 5014")
    app.run(debug=True, port=5014, use_reloader=False)
