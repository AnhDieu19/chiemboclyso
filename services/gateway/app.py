"""
API Gateway - Entry point duy nhất cho Tu Vi Platform

Port: 5001 (giữ nguyên port gốc để backward compatible)

Chế độ hoạt động:
1. MONOLITH mode: Load tất cả blueprints trực tiếp (như app cũ)
2. PROXY mode: Forward requests đến các microservices

Mặc định: MONOLITH mode (development)
Set GATEWAY_MODE=proxy để chuyển sang proxy mode
"""
import os
import sys

# Setup paths
_gateway_dir = os.path.dirname(os.path.abspath(__file__))
_services_dir = os.path.dirname(_gateway_dir)
_project_root = os.path.dirname(_services_dir)

sys.path.insert(0, os.path.join(_services_dir, 'shared'))
from path_setup import setup_service_paths
paths = setup_service_paths()

from flask import Flask, redirect
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(os.path.join(_project_root, '.env'))

from config import SERVICE_REGISTRY, GATEWAY_MODE


def create_app():
    """Application Factory"""
    app = Flask(__name__,
                template_folder=os.path.join(_project_root, 'frontend', 'templates'),
                static_folder=os.path.join(_project_root, 'frontend', 'static'))
    
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}, r"/vdp/*": {"origins": "*"}})
    
    if GATEWAY_MODE == 'monolith':
        register_monolith_blueprints(app)
    else:
        register_proxy_routes(app)
    
    # Common routes
    @app.route('/graph')
    def redirect_graph():
        return redirect('/vdp/')
    
    return app


def register_monolith_blueprints(app):
    """
    Monolith mode: Load trực tiếp tất cả blueprints.
    Giống hệt backend/app.py cũ - fully backward compatible.
    """
    # Tu Vi Chart
    from presentation.api.v1.chart_routes import chart_bp
    app.register_blueprint(chart_bp, url_prefix='/api/v1/chart')
    
    # Tu Vi Finder
    from presentation.api.v1.finder_routes import finder_bp
    app.register_blueprint(finder_bp, url_prefix='/api/v1/finder')
    
    # Tu Vi Analytics
    from presentation.api.v1.analytics_routes import analytics_bp
    app.register_blueprint(analytics_bp, url_prefix='/api/v1/analytics')
    
    # Tu Vi AI
    from presentation.api.v1.ai_routes import ai_bp
    app.register_blueprint(ai_bp, url_prefix='/api/v1/ai')
    
    # VDP
    from vi_dieu_phap import vdp_bp
    app.register_blueprint(vdp_bp, url_prefix='/vdp')
    
    # Graph
    from graph import graph_bp
    app.register_blueprint(graph_bp)
    
    # Web pages
    from presentation.web.page_routes import web_bp
    app.register_blueprint(web_bp)
    
    # Legacy
    from presentation.api.v1.legacy_routes import legacy_bp
    app.register_blueprint(legacy_bp, url_prefix='/api')
    
    # Thai At & Ki Mon & Luc Nham
    from services.thai_at_service import thai_at_bp
    from services.ki_mon_service import ki_mon_bp
    app.register_blueprint(thai_at_bp)
    app.register_blueprint(ki_mon_bp)
    
    # Luc Nham
    import importlib.util
    _luc_nham_routes = os.path.join(_services_dir, 'luc-nham', 'routes.py')
    spec = importlib.util.spec_from_file_location('luc_nham_routes', _luc_nham_routes)
    luc_nham_mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(luc_nham_mod)
    app.register_blueprint(luc_nham_mod.luc_nham_bp)
    
    # Error handlers
    from presentation.api.middleware.error_handler import register_error_handlers
    register_error_handlers(app)
    
    print("  Mode: MONOLITH (all blueprints loaded in-process)")


def register_proxy_routes(app):
    """
    Proxy mode: Forward requests to individual microservices.
    Each service runs on its own port.
    """
    import requests as http_requests
    from flask import request, Response
    
    def proxy_request(service_name, path):
        """Forward request to a microservice"""
        service = SERVICE_REGISTRY.get(service_name)
        if not service:
            return Response(f'Service {service_name} not found', status=503)
        
        target_url = f"http://localhost:{service['port']}{path}"
        
        try:
            resp = http_requests.request(
                method=request.method,
                url=target_url,
                headers={k: v for k, v in request.headers if k != 'Host'},
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False,
                timeout=30
            )
            
            excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
            headers = [(name, value) for name, value in resp.raw.headers.items()
                       if name.lower() not in excluded_headers]
            
            return Response(resp.content, resp.status_code, headers)
        except http_requests.exceptions.ConnectionError:
            return Response(
                f'Service {service_name} unavailable (port {service["port"]})', 
                status=503
            )
    
    # Route patterns to services
    @app.route('/api/v1/chart/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_chart(path):
        return proxy_request('tuvi-chart', f'/api/v1/chart/{path}')
    
    @app.route('/api/v1/finder/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_finder(path):
        return proxy_request('tuvi-finder', f'/api/v1/finder/{path}')
    
    @app.route('/api/v1/analytics/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_analytics(path):
        return proxy_request('tuvi-analytics', f'/api/v1/analytics/{path}')
    
    @app.route('/api/v1/ai/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_ai(path):
        return proxy_request('tuvi-ai', f'/api/v1/ai/{path}')
    
    @app.route('/thai-at', defaults={'path': ''})
    @app.route('/api/thai-at/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_thai_at(path):
        if path:
            return proxy_request('thai-at', f'/api/thai-at/{path}')
        return proxy_request('thai-at', '/thai-at')
    
    @app.route('/ki-mon', defaults={'path': ''})
    @app.route('/api/ki-mon/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_ki_mon(path):
        if path:
            return proxy_request('ki-mon', f'/api/ki-mon/{path}')
        return proxy_request('ki-mon', '/ki-mon')
    
    @app.route('/luc-nham', defaults={'path': ''})
    @app.route('/api/luc-nham/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_luc_nham(path):
        if path:
            return proxy_request('luc-nham', f'/api/luc-nham/{path}')
        return proxy_request('luc-nham', '/luc-nham')
    
    @app.route('/knowledge-graph')
    @app.route('/star-movement')
    @app.route('/dataset-movement')
    @app.route('/graph/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_graph(path=''):
        if path:
            return proxy_request('graph', f'/graph/api/{path}')
        return proxy_request('graph', request.path)
    
    @app.route('/vdp/', defaults={'path': ''})
    @app.route('/vdp/<path:path>')
    def proxy_vdp(path):
        return proxy_request('vi-dieu-phap', f'/vdp/{path}')
    
    # Legacy API proxy
    @app.route('/api/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def proxy_legacy(path):
        return proxy_request('tuvi-chart', f'/api/{path}')
    
    # Web pages - served by gateway itself
    from presentation.web.page_routes import web_bp
    app.register_blueprint(web_bp)
    
    print(f"  Mode: PROXY (forwarding to {len(SERVICE_REGISTRY)} services)")


def main():
    """Main entry point"""
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')
    
    app = create_app()
    
    print("=" * 60)
    print("     TỬ VI ĐẨU SỐ - MICROSERVICES PLATFORM")
    print("=" * 60)
    print(f"\n  Server: http://localhost:5001")
    print(f"  Gateway Mode: {GATEWAY_MODE.upper()}")
    print(f"\n  Services:")
    for name, info in SERVICE_REGISTRY.items():
        print(f"    {info.get('icon', '📦')} {name:20s} → port {info['port']}")
    print("=" * 60)
    
    app.run(debug=True, port=5001, use_reloader=False)


if __name__ == '__main__':
    main()
