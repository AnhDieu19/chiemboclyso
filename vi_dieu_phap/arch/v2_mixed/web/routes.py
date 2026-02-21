from flask import Blueprint, render_template, jsonify
from vi_dieu_phap.repository import VdpRepository
import os

# Define Blueprint with its own static/template folders
# Note: paths are relative to THIS file's location
current_dir = os.path.dirname(os.path.abspath(__file__))

vdp_bp = Blueprint('vdp', __name__,
                   template_folder='templates',
                   static_folder='static',
                   static_url_path='/static') # Serve static at /vdp/static

repo = VdpRepository()

@vdp_bp.route('/')
def index():
    """Landing page with 3 options"""
    return render_template('vdp_index.html')

@vdp_bp.route('/structure')
def structure_view():
    """Structure (Hierarchy) view"""
    return render_template('vdp_structure.html')

@vdp_bp.route('/association')
def association_view():
    """Association (Citta-Cetasika) view"""
    return render_template('vdp_association.html')

@vdp_bp.route('/root-cause')
def root_cause_view():
    """Root Cause view"""
    return render_template('vdp_root_cause.html')

@vdp_bp.route('/api/data')
@vdp_bp.route('/data')
def get_graph_data():
    """Return all graph data (backward compatibility)"""
    return jsonify(repo.get_graph_data())

@vdp_bp.route('/api/data/<relation_type>')
def get_graph_data_filtered(relation_type):
    """Return filtered graph data by relation type"""
    return jsonify(repo.get_graph_data_by_type(relation_type))
