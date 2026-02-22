"""
Vercel Serverless Entrypoint
Full-platform Flask app for Vercel deployment.
Registers all blueprints + inline routes for complete functionality.
"""
import os
import sys

# ── Path Setup ──────────────────────────────────────────────────────────────
_api_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_api_dir)
_python_dir = os.path.normpath(os.path.join(_project_root, 'python'))
_backend_dir = os.path.normpath(os.path.join(_project_root, 'backend'))

for p in [_python_dir, _backend_dir, _project_root]:
    if p not in sys.path:
        sys.path.insert(0, p)

# ── Flask App ───────────────────────────────────────────────────────────────
from flask import Flask, jsonify, request, render_template, redirect, send_from_directory
from flask_cors import CORS
from jinja2 import ChoiceLoader, FileSystemLoader

_static_dir = os.path.join(_project_root, 'frontend', 'static')

app = Flask(__name__,
            template_folder=os.path.join(_python_dir, 'templates'),
            static_folder=_static_dir,
            static_url_path='/static')

# Multiple template directories: python/templates + frontend/templates
app.jinja_loader = ChoiceLoader([
    FileSystemLoader(os.path.join(_python_dir, 'templates')),
    FileSystemLoader(os.path.join(_project_root, 'frontend', 'templates')),
])

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'vercel-secret')
CORS(app, resources={r"/api/*": {"origins": "*"}, r"/vdp/*": {"origins": "*"}})


# ── Register Blueprints (graceful fallback) ─────────────────────────────────
# Vi Diệu Pháp
try:
    from vi_dieu_phap import vdp_bp
    app.register_blueprint(vdp_bp, url_prefix='/vdp')
except Exception as e:
    print(f"[Vercel] VDP blueprint skipped: {e}")

# Knowledge Graph
try:
    from graph import graph_bp
    app.register_blueprint(graph_bp)
except Exception as e:
    print(f"[Vercel] Graph blueprint skipped: {e}")

# Tu Vi Chart API
try:
    from presentation.api.v1.chart_routes import chart_bp
    app.register_blueprint(chart_bp, url_prefix='/api/v1/chart')
except Exception as e:
    print(f"[Vercel] Chart API blueprint skipped: {e}")

# Tu Vi Finder API
try:
    from presentation.api.v1.finder_routes import finder_bp
    app.register_blueprint(finder_bp, url_prefix='/api/v1/finder')
except Exception as e:
    print(f"[Vercel] Finder API blueprint skipped: {e}")

# Tu Vi Analytics API
try:
    from presentation.api.v1.analytics_routes import analytics_bp
    app.register_blueprint(analytics_bp, url_prefix='/api/v1/analytics')
except Exception as e:
    print(f"[Vercel] Analytics API blueprint skipped: {e}")

# Tu Vi AI API
try:
    from presentation.api.v1.ai_routes import ai_bp
    app.register_blueprint(ai_bp, url_prefix='/api/v1/ai')
except Exception as e:
    print(f"[Vercel] AI API blueprint skipped: {e}")

# Legacy API (/api/generate, /api/finder/solve, /api/ask-ai, etc.)
try:
    from presentation.api.v1.legacy_routes import legacy_bp
    app.register_blueprint(legacy_bp, url_prefix='/api')
except Exception as e:
    print(f"[Vercel] Legacy API blueprint skipped: {e}")


# ── Eager imports for inline routes ─────────────────────────────────────────
from logic.luc_nham_engine import LucNhamEngine
from logic.ki_mon_engine import KiMonEngine
from logic.thai_at_engine import ThaiAtEngine


# ── Homepage ────────────────────────────────────────────────────────────────
@app.route('/')
def home():
    """Landing page with links to all services"""
    return render_template('home.html')


@app.route('/api/info')
def api_info():
    return jsonify({
        'app': 'Chiêm Bốc Lý Số',
        'version': '3.0',
        'services': {
            'tuvi': '/tuvi',
            'finder': '/finder',
            'analytics': '/analytics/beauty',
            'luc_nham': '/luc-nham',
            'ki_mon': '/ki-mon',
            'thai_at': '/thai-at',
            'vdp': '/vdp/',
            'knowledge_graph': '/knowledge-graph',
            'star_movement': '/star-movement',
            'hexagram_viz': '/hexagram-viz/',
            'octonion_viz': '/octonion-viz/',
            'math_viz': '/math-viz/',
            'acupoints_viz': '/acupoints-viz/',
        }
    })


# ── Tu Vi Page Routes ──────────────────────────────────────────────────────
@app.route('/tuvi')
def tuvi_index():
    """Tử Vi Đẩu Số — Main chart page"""
    try:
        from data.can_chi import GIO_SINH_RANGE
        return render_template('index.html', gio_sinh_range=GIO_SINH_RANGE)
    except Exception as e:
        return jsonify({'error': f'Tu Vi page load failed: {e}'}), 500


@app.route('/finder')
def finder_page():
    """Reverse Finder — find birth date from traits"""
    try:
        from data.finder_options import EVENTS, TRAITS, APPEARANCE, PROFESSION, MARITAL_STATUS
        from data.can_chi import DIA_CHI, GIO_SINH_RANGE
        formatted_hours = [
            {'id': k, 'name': DIA_CHI[k] if k < len(DIA_CHI) else '?', 'range': v}
            for k, v in GIO_SINH_RANGE.items()
        ]
        options = {
            'events': EVENTS, 'traits': TRAITS, 'appearance': APPEARANCE,
            'profession': PROFESSION, 'marital': MARITAL_STATUS
        }
        return render_template('finder.html', options=options, hours=formatted_hours)
    except Exception as e:
        return jsonify({'error': f'Finder page load failed: {e}'}), 500


@app.route('/analytics/beauty')
def analytics_beauty():
    """Beauty Analytics Dashboard"""
    try:
        from analytics.visualize_data import get_visualization_data
        gender = request.args.get('gender', 'all')
        if gender not in ('all', 'nam', 'nu', 'nữ'):
            gender = 'all'
        try:
            data = get_visualization_data(gender_filter=gender)
        except Exception:
            data = None
        if not data:
            data = {
                'count': 0, 'total_scanned': 0, 'data_source': 'empty',
                'fate_labels': [], 'pie_data': [], 'beauty_sets': [],
                'bar_datasets': [], 'line_labels': [], 'line_lucky': [],
                'line_tragic': [], 'line_beauty_rate': [], 'line_beauty_count': [],
                'note': 'Chưa có dữ liệu. Vui lòng chạy script trước.'
            }
        return render_template('analytics_beauty.html', data=data, current_gender=gender)
    except Exception as e:
        return jsonify({'error': f'Analytics page load failed: {e}'}), 500


# ── Lục Nhâm Routes ────────────────────────────────────────────────────────
@app.route('/luc-nham')
def luc_nham_index():
    """Render trang chủ Lục Nhâm"""
    return render_template('luc_nham_view.html')


@app.route('/api/luc-nham/calculate', methods=['POST'])
def luc_nham_calculate():
    """API tính toán Lục Nhâm"""
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400

        year_val = data.get('year')
        month_val = data.get('month')
        day_val = data.get('day')

        if year_val is None or month_val is None or day_val is None:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: year, month, day'
            }), 400

        try:
            year = int(year_val)
            month = int(month_val)
            day = int(day_val)
            hour = int(data.get('hour', 0))
        except (ValueError, TypeError) as e:
            return jsonify({
                'success': False,
                'error': f'Invalid numeric input: {e}'
            }), 400

        engine = LucNhamEngine(year, month, day, hour)
        chart_data = engine.get_full_chart()

        return jsonify({'success': True, 'data': chart_data})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


# ── Kì Môn Routes ──────────────────────────────────────────────────────────
@app.route('/ki-mon')
def ki_mon_index():
    """Render trang chủ Kì Môn Độn Giáp"""
    return render_template('ki_mon_view.html')


@app.route('/api/ki-mon/calculate', methods=['POST'])
def ki_mon_calculate():
    """API tính toán Kì Môn Độn Giáp"""
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400

        year_val = data.get('year')
        month_val = data.get('month')
        day_val = data.get('day')

        if year_val is None or month_val is None or day_val is None:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: year, month, day'
            }), 400

        try:
            year = int(year_val)
            month = int(month_val)
            day = int(day_val)
            hour = int(data.get('hour', 0))
        except (ValueError, TypeError) as e:
            return jsonify({
                'success': False,
                'error': f'Invalid numeric input: {e}'
            }), 400

        engine = KiMonEngine(year, month, day, hour)
        chart_data = engine.get_full_chart()

        return jsonify({'success': True, 'data': chart_data})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


# ── Thái Ất Routes ──────────────────────────────────────────────────────────
@app.route('/thai-at')
def thai_at_index():
    """Render trang chủ Thái Ất"""
    return render_template('thai_at_view.html')


@app.route('/api/thai-at/calculate', methods=['POST'])
def thai_at_calculate():
    """API tính toán Thái Ất"""
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400

        year_val = data.get('year')
        month_val = data.get('month')
        day_val = data.get('day')

        if year_val is None or month_val is None or day_val is None:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: year, month, day'
            }), 400

        try:
            year = int(year_val)
            month = int(month_val)
            day = int(day_val)
            hour = int(data.get('hour', 0))
        except (ValueError, TypeError) as e:
            return jsonify({
                'success': False,
                'error': f'Invalid numeric input: {e}'
            }), 400

        engine = ThaiAtEngine(year, month, day, hour)
        chart_data = engine.get_full_chart()

        return jsonify({'success': True, 'data': chart_data})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400


# ── Static Visualization Apps ───────────────────────────────────────────────
def _register_viz_routes(flask_app):
    """Register routes for pure-static visualization apps."""
    viz_apps = {
        'hexagram-viz': 'hexagram_viz',
        'acupoints-viz': 'acupoints_viz',
        'math-viz': 'math_viz',
        'octonion-viz': 'octonion_viz',
    }
    for url_slug, dir_name in viz_apps.items():
        dir_path = os.path.join(_project_root, dir_name)
        ep_base = url_slug.replace('-', '_')

        def _make_redirect(slug):
            def handler():
                return redirect(f'/{slug}/')
            return handler

        def _make_index(dp):
            def handler():
                return send_from_directory(dp, 'index.html')
            return handler

        def _make_file(dp):
            def handler(filename):
                return send_from_directory(dp, filename)
            return handler

        flask_app.add_url_rule(
            f'/{url_slug}', endpoint=f'{ep_base}_redir',
            view_func=_make_redirect(url_slug))
        flask_app.add_url_rule(
            f'/{url_slug}/', endpoint=f'{ep_base}_index',
            view_func=_make_index(dir_path))
        flask_app.add_url_rule(
            f'/{url_slug}/<path:filename>', endpoint=f'{ep_base}_file',
            view_func=_make_file(dir_path))


_register_viz_routes(app)


# Vercel needs the variable named 'app'
