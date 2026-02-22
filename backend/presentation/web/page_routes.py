"""
Page Routes - Web UI endpoints

Serve HTML pages cho người dùng
"""
import os
import logging
from flask import Blueprint, render_template, request, send_from_directory

logger = logging.getLogger(__name__)

web_bp = Blueprint('web', __name__)

# ── Project root for serving static viz apps ──
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))


@web_bp.route('/')
def dashboard():
    """Dashboard — app launcher homepage"""
    try:
        return render_template('dashboard.html')
    except Exception as e:
        logger.exception("Render dashboard failed: %s", e)
        raise


@web_bp.route('/tuvi')
def index():
    """Tu Vi main page (birth chart form)"""
    from data.can_chi import GIO_SINH_RANGE
    try:
        return render_template('index.html', gio_sinh_range=GIO_SINH_RANGE)
    except Exception as e:
        logger.exception("Render index failed: %s", e)
        raise


@web_bp.route('/finder')
def finder_page():
    """Reverse Finder UI"""
    try:
        from data.finder_options import (
            EVENTS, TRAITS, APPEARANCE, PROFESSION, MARITAL_STATUS
        )
        from data.can_chi import DIA_CHI, GIO_SINH_RANGE
        
        formatted_hours = [
            {'id': k, 'name': DIA_CHI.get(k, '?'), 'range': v}
            for k, v in GIO_SINH_RANGE.items()
        ]
        
        options = {
            'events': EVENTS,
            'traits': TRAITS,
            'appearance': APPEARANCE,
            'profession': PROFESSION,
            'marital': MARITAL_STATUS
        }
        
        return render_template('finder.html', options=options, hours=formatted_hours)
    except Exception as e:
        logger.exception("Render finder failed: %s", e)
        raise


@web_bp.route('/analytics/beauty')
def analytics_beauty():
    """Beauty Analytics Dashboard"""
    try:
        from analytics.visualize_data import get_visualization_data
        
        gender = request.args.get('gender', 'all')
        if gender not in ('all', 'nam', 'nu', 'nữ'):
            gender = 'all'
        
        data = get_visualization_data(gender_filter=gender)
        
        if not data:
            return render_template('analytics_beauty.html', 
                                   data={'count': 0, 'total_scanned': 0, 'data_source': 'empty',
                                         'fate_labels': [], 'pie_data': [], 'beauty_sets': [],
                                         'bar_datasets': [], 'line_labels': [], 'line_lucky': [],
                                         'line_tragic': [], 'line_beauty_rate': [], 'line_beauty_count': [],
                                         'note': 'Chưa có dữ liệu. Vui lòng chạy script run_full_scan.py trước.'},
                                   current_gender=gender)
        
        return render_template('analytics_beauty.html', data=data, current_gender=gender)
    except Exception as e:
        logger.exception("Render analytics_beauty failed: %s", e)
        raise


# ─── Static Visualization Apps ───────────────────────────────────
# Serve the standalone HTML/JS/CSS apps from their project-root dirs

_STATIC_VIZ_APPS = {
    'math-viz':      'math_viz',
    'hexagram-viz':  'hexagram_viz',
    'octonion-viz':  'octonion_viz',
    'acupoints-viz': 'acupoints_viz',
}

@web_bp.route('/math-viz/')
@web_bp.route('/hexagram-viz/')
@web_bp.route('/octonion-viz/')
@web_bp.route('/acupoints-viz/')
def viz_app_index():
    """Serve index.html for static visualization apps"""
    # Extract app name from path: /math-viz/ → math-viz
    app_name = request.path.strip('/').split('/')[0]
    dir_name = _STATIC_VIZ_APPS.get(app_name)
    if not dir_name:
        return "Not Found", 404
    app_dir = os.path.join(_PROJECT_ROOT, dir_name)
    return send_from_directory(app_dir, 'index.html')


@web_bp.route('/math-viz/<path:filename>')
@web_bp.route('/hexagram-viz/<path:filename>')
@web_bp.route('/octonion-viz/<path:filename>')
@web_bp.route('/acupoints-viz/<path:filename>')
def viz_app_static(filename):
    """Serve static assets (JS, CSS, data) for visualization apps"""
    app_name = request.path.strip('/').split('/')[0]
    dir_name = _STATIC_VIZ_APPS.get(app_name)
    if not dir_name:
        return "Not Found", 404
    app_dir = os.path.join(_PROJECT_ROOT, dir_name)
    return send_from_directory(app_dir, filename)


