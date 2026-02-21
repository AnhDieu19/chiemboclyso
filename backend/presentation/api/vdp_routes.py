"""
Vi Dieu Phap API Routes
Provides data for the Knowledge Graph
"""
from flask import Blueprint, jsonify
from vi_dieu_phap.repository import VdpRepository

vdp_bp = Blueprint('vdp', __name__)
repo = VdpRepository()

@vdp_bp.route('/data')
def get_graph_data():
    """
    Returns graph data from the JSON Repository.
    """
    # Reload data if needed (for dev) or just return
    # repo._load_data() 
    
    return jsonify(repo.get_graph_data())
