"""
Lục Nhâm Routes for Vercel deployment
(Copied from services/luc-nham/routes.py, adapted for unified app)
"""
from flask import Blueprint, request, jsonify, render_template

luc_nham_bp = Blueprint('luc_nham', __name__)


@luc_nham_bp.route('/luc-nham')
def index():
    """Render trang chủ Lục Nhâm"""
    return render_template('luc_nham_view.html')


@luc_nham_bp.route('/api/luc-nham/calculate', methods=['POST'])
def calculate():
    """API tính toán Lục Nhâm"""
    try:
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400

        year_val = data.get('year')
        month_val = data.get('month')
        day_val = data.get('day')

        if year_val is None or month_val is None or day_val is None:
            return jsonify({'success': False, 'error': 'Missing required fields: year, month, day'}), 400

        try:
            year = int(year_val)
            month = int(month_val)
            day = int(day_val)
            hour = int(data.get('hour', 0))
        except (ValueError, TypeError) as e:
            return jsonify({'success': False, 'error': f'Invalid numeric input: {e}'}), 400

        from logic.luc_nham_engine import LucNhamEngine
        engine = LucNhamEngine(year, month, day, hour)
        chart_data = engine.get_full_chart()

        return jsonify({'success': True, 'data': chart_data})

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400
