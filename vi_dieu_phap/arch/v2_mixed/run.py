import os
import sys
from flask import Flask, redirect

# Add project root to path to ensure imports work if run directly
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from vi_dieu_phap.web.routes import vdp_bp

def create_standalone_app():
    """
    Creates a standalone Flask application for Vi Dieu Phap.
    This allows developing/testing VDP in isolation from the main Tu Vi App.
    """
    app = Flask(__name__)
    
    # Register VDP Blueprint at root element '/' for standalone convenience
    # But inside the blueprint, routes are relative. 
    # vdp_bp defines '/' as index.
    app.register_blueprint(vdp_bp, url_prefix='/vdp')

    @app.route('/')
    def root():
        return redirect('/vdp/')

    return app

if __name__ == "__main__":
    print("==================================================")
    print("   VI DIỆU PHÁP - STANDALONE MODE")
    print("==================================================")
    print("   Running independently on http://127.0.0.1:5002/vdp/")
    print("==================================================")
    
    app = create_standalone_app()
    app.run(debug=True, port=5002, use_reloader=False)
