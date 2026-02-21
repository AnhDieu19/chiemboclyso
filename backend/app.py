"""
Flask Main Application - Refactored Clean Architecture Version

Entry point cho Tu Vi application với kiến trúc modular
"""
import os
import sys
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add backend to path
backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

# Add python directory to path (for chart, interpretation, analytics modules)
python_dir = os.path.join(os.path.dirname(backend_dir), 'python')
sys.path.insert(0, python_dir)

# Add project root path (for vi_dieu_phap module at root)
project_root = os.path.dirname(backend_dir)
sys.path.insert(0, project_root)

from config import config
from dependencies import setup_dependencies


def create_app(config_name='development'):
    """
    Application Factory Pattern
    
    Args:
        config_name: Tên configuration ('development', 'production', 'default')
    
    Returns:
        Flask app instance
    """
    app = Flask(__name__,
                template_folder='../frontend/templates',
                static_folder='../frontend/static')
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Enable CORS for all API routes
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # Setup dependencies
    setup_dependencies()
    
    # Register blueprints FIRST (before error handlers)
    register_blueprints(app)
    
    # Register error handlers AFTER blueprints
    from presentation.api.middleware.error_handler import register_error_handlers
    register_error_handlers(app)
    
    return app


def register_blueprints(app):
    """
    Đăng ký tất cả blueprints
    """
    # API v1 routes
    from presentation.api.v1.chart_routes import chart_bp
    from presentation.api.v1.finder_routes import finder_bp
    from presentation.api.v1.analytics_routes import analytics_bp
    from presentation.api.v1.ai_routes import ai_bp
    
    # NEW: Modular VDP Blueprint (Import from Master Package)
    from vi_dieu_phap import vdp_bp
    
    # Web routes
    from presentation.web.page_routes import web_bp
    
    # Knowledge Graph Blueprint (star movement, dataset movement, etc.)
    from graph import graph_bp
    
    # Register with prefixes
    app.register_blueprint(chart_bp, url_prefix='/api/v1/chart')
    app.register_blueprint(finder_bp, url_prefix='/api/v1/finder')
    app.register_blueprint(analytics_bp, url_prefix='/api/v1/analytics')
    app.register_blueprint(ai_bp, url_prefix='/api/v1/ai')
    
    # Mount VDP at /vdp (Web) and /vdp/api (Data)
    app.register_blueprint(vdp_bp, url_prefix='/vdp')
    
    # Mount Graph module (knowledge graph, star movement)
    app.register_blueprint(graph_bp)
    
    app.register_blueprint(web_bp)
    
    # Legacy API support (backward compatibility)
    from presentation.api.v1.legacy_routes import legacy_bp
    app.register_blueprint(legacy_bp, url_prefix='/api')
    
    # Thai At & Ki Mon blueprints
    from services.thai_at_service import thai_at_bp
    from services.ki_mon_service import ki_mon_bp
    app.register_blueprint(thai_at_bp)
    app.register_blueprint(ki_mon_bp)
    
    # Redirect /graph to /vdp/ (Alias)
    @app.route('/graph')
    def redirect_graph():
        from flask import redirect
        return redirect('/vdp/')


def main():
    """
    Main entry point
    """
    # Setup UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    
    # Create app
    app = create_app('development')
    
    # Print startup info
    print("=" * 60)
    print("     TỬ VI ĐẨU SỐ - CLEAN ARCHITECTURE VERSION 2.0")
    print("=" * 60)
    print("\n🌐 Server đang chạy tại: http://localhost:5001")
    print("   Nhấn Ctrl+C để dừng server")
    print("\nKiến trúc mới:")
    print("   📦 Domain Layer         - Business logic thuần túy")
    print("   📦 Application Layer    - Use cases và workflows")
    print("   📦 Infrastructure Layer - External services và data")
    print("   📦 Presentation Layer   - API routes và controllers")
    print("=" * 60)
    
    # Run app
    # Switch to 5001 to avoid port 5000 hang issues
    # Run app without reloader to avoid Google Drive file watch issues
    app.run(debug=True, port=5001, use_reloader=False)


if __name__ == '__main__':
    main()
