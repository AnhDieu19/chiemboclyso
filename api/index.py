"""
Vercel Serverless Entrypoint
Self-contained Flask app for Vercel deployment.
All routes inline to avoid cross-file import issues.
"""
import os
import sys

# ── Path Setup ──────────────────────────────────────────────────────────────
_api_dir = os.path.dirname(os.path.abspath(__file__))
_project_root = os.path.dirname(_api_dir)
_python_dir = os.path.normpath(os.path.join(_project_root, 'python'))

for p in [_python_dir, _project_root]:
    if p not in sys.path:
        sys.path.insert(0, p)

# ── Flask App ───────────────────────────────────────────────────────────────
from flask import Flask, jsonify, request, render_template, redirect
from flask_cors import CORS

_templates_dir = os.path.join(_python_dir, 'templates')
_static_dir = os.path.join(_project_root, 'frontend', 'static')

app = Flask(__name__,
            template_folder=_templates_dir,
            static_folder=_static_dir,
            static_url_path='/static')

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'vercel-secret')
CORS(app, resources={r"/api/*": {"origins": "*"}})

# ── Eager import after path setup ───────────────────────────────────────────
from logic.luc_nham_engine import LucNhamEngine
from logic.ki_mon_engine import KiMonEngine


# ── Routes ──────────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return redirect('/luc-nham')


@app.route('/api/info')
def api_info():
    return jsonify({
        'app': 'Chiêm Bốc Lý Số',
        'version': '2.0',
        'endpoints': {
            'luc_nham': '/luc-nham',
            'luc_nham_api': '/api/luc-nham/calculate [POST]',
            'ki_mon': '/ki-mon',
            'ki_mon_api': '/api/ki-mon/calculate [POST]',
        }
    })


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


# Vercel needs the variable named 'app'
