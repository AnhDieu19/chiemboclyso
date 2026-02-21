from flask import Blueprint, render_template, jsonify
from vi_dieu_phap.application.graph_service import GraphService
import os
import traceback


def create_vdp_blueprint(service: GraphService):
    vdp_bp = Blueprint('vdp', __name__,
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='/static')

    # --- Error wrapper ---
    def safe_json(func):
        """Wrap API handlers with error handling."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                traceback.print_exc()
                return jsonify({'error': str(e), 'type': type(e).__name__}), 500
        wrapper.__name__ = func.__name__
        return wrapper

    # --- Page Routes ---
    @vdp_bp.route('/')
    def index():
        return render_template('vdp_index.html')

    @vdp_bp.route('/structure')
    def structure_view():
        return render_template('vdp_structure.html')

    @vdp_bp.route('/association')
    def association_view():
        return render_template('vdp_association.html')

    @vdp_bp.route('/root-cause')
    def root_cause_view():
        return render_template('vdp_root_cause.html')

    # --- API Routes ---
    @vdp_bp.route('/api/data')
    @safe_json
    def get_all_data():
        return jsonify(service.get_full_data())

    @vdp_bp.route('/api/data/structure')
    @safe_json
    def get_structure_data():
        return jsonify(service.get_structure_graph())

    @vdp_bp.route('/api/data/association')
    @safe_json
    def get_association_data():
        return jsonify(service.get_association_graph())

    @vdp_bp.route('/api/data/root_cause')
    @safe_json
    def get_root_cause_data():
        return jsonify(service.get_root_cause_graph())

    @vdp_bp.route('/api/stats')
    @safe_json
    def get_stats():
        return jsonify(service.get_stats())

    return vdp_bp
