"""
Knowledge Graph Service - Microservice visualize graph tri thức

Port: 5017
Endpoints:
  GET  /knowledge-graph            - Knowledge graph page
  GET  /star-movement              - Star movement page
  GET  /dataset-movement           - Dataset movement page
  POST /graph/api/chart            - Chart calculation API
  POST /graph/api/star-movement    - Star movement API
  POST /graph/api/dataset-movement - Dataset movement API
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

# Graph module has its own templates and static files
_graph_dir = os.path.join(paths['python_dir'], 'graph')
_templates_dir = os.path.join(_graph_dir, 'templates')
_static_dir = os.path.join(_graph_dir, 'static')


def create_app():
    app = Flask(__name__, 
                template_folder=_templates_dir,
                static_folder=_static_dir,
                static_url_path='/graph/static')
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    CORS(app, resources={r"/api/*": {"origins": "*"}, r"/graph/*": {"origins": "*"}})
    
    # Import and register the graph blueprint from python/graph/
    sys.path.insert(0, paths['python_dir'])
    from graph import graph_bp
    app.register_blueprint(graph_bp)
    
    return app


if __name__ == '__main__':
    app = create_app()
    print("🌐 Knowledge Graph Service running on port 5017")
    app.run(debug=True, port=5017, use_reloader=False)
