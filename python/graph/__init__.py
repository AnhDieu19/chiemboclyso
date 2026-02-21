"""
Tu Vi Knowledge Graph - Flask Blueprint
Module rieng cho Knowledge Graph visualization
"""

from flask import Blueprint, render_template

# Tao Blueprint
graph_bp = Blueprint(
    'graph', 
    __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/graph/static'
)

@graph_bp.route('/knowledge-graph')
def knowledge_graph():
    """Tu Vi Knowledge Graph - Interactive Visualization"""
    return render_template('knowledge_graph.html')

@graph_bp.route('/star-movement')
def star_movement():
    """Tu Vi Star Movement - Analyze star patterns across 12 hours"""
    return render_template('star_movement.html')

@graph_bp.route('/dataset-movement')
def dataset_movement():
    """Dataset Star Movement - Analyze patterns across entire dataset"""
    return render_template('dataset_movement.html')

# Import API routes
from . import chart_api
from . import star_movement_api
from . import dataset_movement_api
