"""
Chart Routes - API endpoints cho lá số Tử Vi

Tách từ: backend/presentation/api/v1/chart_routes.py
"""
from flask import Blueprint, request, jsonify

chart_bp = Blueprint('chart', __name__)


@chart_bp.route('/generate', methods=['POST'])
def generate():
    """
    Generate birth chart API endpoint (UC-01)
    
    Request:
        {
            "year": 1990, "month": 1, "day": 1, "hour": 12,
            "gender": "nam", "calendar_type": "solar", "leap_month": false
        }
    """
    try:
        data = request.json
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400

        year = data.get('year')
        month = data.get('month')
        day = data.get('day')
        hour = data.get('hour')
        gender = data.get('gender', 'nam')
        calendar_type = data.get('calendar_type', 'solar')
        leap_month = data.get('leap_month', False)

        # Validate required fields
        if not all([year, month, day]):
            return jsonify({"status": "error", "message": "Missing required fields (year, month, day)"}), 400

        # Validate types and ranges
        try:
            year = int(year)
            if not (1900 <= year <= 2100):
                return jsonify({'status': 'error', 'message': 'Năm không hợp lệ (1900-2100)'}), 400
        except (ValueError, TypeError):
            return jsonify({'status': 'error', 'message': 'Năm phải là số nguyên'}), 400

        try:
            month = int(month)
            if not (1 <= month <= 12):
                return jsonify({'status': 'error', 'message': 'Tháng không hợp lệ (1-12)'}), 400
        except (ValueError, TypeError):
            return jsonify({'status': 'error', 'message': 'Tháng phải là số nguyên'}), 400

        try:
            day = int(day)
            if not (1 <= day <= 31):
                return jsonify({'status': 'error', 'message': 'Ngày không hợp lệ (1-31)'}), 400
        except (ValueError, TypeError):
            return jsonify({'status': 'error', 'message': 'Ngày phải là số nguyên'}), 400

        if hour is not None:
            try:
                hour = int(hour)
                if not (0 <= hour <= 23):
                    return jsonify({'status': 'error', 'message': 'Giờ không hợp lệ (0-23)'}), 400
            except (ValueError, TypeError):
                return jsonify({'status': 'error', 'message': 'Giờ phải là số nguyên'}), 400

        # Normalize gender
        if gender not in ['nam', 'nu', 'nữ']:
            return jsonify({'status': 'error', 'message': 'Giới tính không hợp lệ (nam/nu)'}), 400
        if gender == 'nu':
            gender = 'nữ'

        if calendar_type not in ['solar', 'lunar']:
            return jsonify({'status': 'error', 'message': 'Loại lịch không hợp lệ (solar/lunar)'}), 400

        if not isinstance(leap_month, bool):
            leap_month = str(leap_month).lower() in ['true', '1', 'yes']

        # Execute use case
        from use_cases import GenerateChartUseCase
        use_case = GenerateChartUseCase()
        result = use_case.execute(
            year=year, month=month, day=day, hour=hour,
            gender=gender, calendar_type=calendar_type, leap_month=leap_month
        )
        
        return jsonify(result)

    except ValueError as e:
        return jsonify({'status': 'error', 'message': f'Invalid input: {str(e)}'}), 400
    except KeyError as e:
        return jsonify({'status': 'error', 'message': f'Missing required field: {str(e)}'}), 400
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Unexpected error in chart generation")
        return jsonify({'status': 'error', 'message': 'Internal server error occurred'}), 500


@chart_bp.route('/star/<star_name>', methods=['GET'])
def get_star_info(star_name: str):
    """Get detailed information about a specific star (UC-03)"""
    try:
        from data.star_details import CHINH_TINH_DETAILS
        from interpretation import STAR_MEANINGS
        
        if star_name in CHINH_TINH_DETAILS:
            return jsonify(CHINH_TINH_DETAILS[star_name])
        
        if star_name in STAR_MEANINGS:
            phu_tinh = STAR_MEANINGS[star_name]
            return jsonify({
                'name': star_name,
                'type': 'Phụ Tinh',
                'nature': phu_tinh.get('nature', 'Trung'),
                'effect': phu_tinh.get('effect', ''),
                'meaning': {'general': phu_tinh.get('effect', '')}
            })
        
        return jsonify({'status': 'error', 'message': 'Không tìm thấy sao'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@chart_bp.route('/palace/<palace_name>', methods=['GET'])
def get_palace_info(palace_name: str):
    """Get information about a specific palace"""
    try:
        from interpretation import PALACE_MEANINGS
        
        if palace_name in PALACE_MEANINGS:
            return jsonify(PALACE_MEANINGS[palace_name])
        
        return jsonify({'status': 'error', 'message': 'Không tìm thấy cung'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@chart_bp.route('/fortune', methods=['POST'])
def get_fortune():
    """Get fortune periods - Đại Hạn, Tiểu Hạn, Lưu Niên (UC-05)"""
    try:
        data = request.json
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
        
        chart = data.get('chart', {})
        from datetime import datetime
        year = int(data.get('year', datetime.now().year))
        
        if not chart:
            return jsonify({'status': 'error', 'message': 'Cần cung cấp dữ liệu lá số'}), 400
        
        from core import get_fortune_periods
        fortune = get_fortune_periods(chart, year)
        
        return jsonify({'status': 'success', 'data': fortune})

    except ValueError as e:
        return jsonify({'status': 'error', 'message': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Unexpected error in fortune calculation")
        return jsonify({'status': 'error', 'message': 'Internal server error occurred'}), 500
