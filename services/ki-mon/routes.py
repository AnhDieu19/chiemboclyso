"""
Kì Môn Routes

Tách từ: python/services/ki_mon_service.py
"""
from flask import Blueprint, request, jsonify, render_template

ki_mon_bp = Blueprint('ki_mon', __name__)


@ki_mon_bp.route('/ki-mon')
def index():
    """Render trang chủ Kì Môn"""
    return render_template('ki_mon_view.html')


@ki_mon_bp.route('/api/ki-mon/calculate', methods=['POST'])
def calculate():
    """API tính toán Kì Môn"""
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
        
        from logic.ki_mon_engine import KiMonEngine
        engine = KiMonEngine(year, month, day, hour)
        chart_data = engine.get_full_chart()
        
        return jsonify({'success': True, 'data': chart_data})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400
