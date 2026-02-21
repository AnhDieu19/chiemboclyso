"""
Thái Ất Routes

Tách từ: python/services/thai_at_service.py
"""
from flask import Blueprint, request, jsonify, render_template

thai_at_bp = Blueprint('thai_at', __name__)


@thai_at_bp.route('/thai-at')
def index():
    """Render trang chủ Thái Ất"""
    return render_template('thai_at_view.html')


@thai_at_bp.route('/api/thai-at/calculate', methods=['POST'])
def calculate():
    """API tính toán Thái Ất"""
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
        
        from logic.thai_at_engine import ThaiAtEngine
        engine = ThaiAtEngine(year, month, day, hour)
        chart_data = engine.get_full_chart()
        
        return jsonify({'success': True, 'data': chart_data})
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400
