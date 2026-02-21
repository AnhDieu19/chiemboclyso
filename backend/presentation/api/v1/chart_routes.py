"""
Chart Routes - API endpoints cho lá số Tử Vi

Xử lý các yêu cầu liên quan đến tính toán và hiển thị lá số
"""
from flask import Blueprint, request, jsonify

chart_bp = Blueprint('chart', __name__)


@chart_bp.route('/generate', methods=['POST'])
def generate():
    """
    Generate birth chart API endpoint (UC-01)
    
    Request:
        {
            "year": 1990,
            "month": 1,
            "day": 1,
            "hour": 12,
            "gender": "nam",
            "calendar_type": "solar",
            "leap_month": false
        }
    
    Response:
        {
            "status": "success",
            "data": {
                "chart": {...},
                "interpretation": {...},
                "tai_menh": {...}
            }
        }
    """
    try:
        data = request.json

        # Validate input
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
            return jsonify({
                "status": "error",
                "message": "Missing required fields (year, month, day)"
            }), 400

        # Validate year type and range
        try:
            year = int(year)
            if not (1900 <= year <= 2100):
                return jsonify({
                    'status': 'error',
                    'message': 'Năm không hợp lệ (1900-2100)'
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'status': 'error',
                'message': 'Năm phải là số nguyên'
            }), 400

        # Validate month
        try:
            month = int(month)
            if not (1 <= month <= 12):
                return jsonify({
                    'status': 'error',
                    'message': 'Tháng không hợp lệ (1-12)'
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'status': 'error',
                'message': 'Tháng phải là số nguyên'
            }), 400

        # Validate day
        try:
            day = int(day)
            if not (1 <= day <= 31):
                return jsonify({
                    'status': 'error',
                    'message': 'Ngày không hợp lệ (1-31)'
                }), 400
        except (ValueError, TypeError):
            return jsonify({
                'status': 'error',
                'message': 'Ngày phải là số nguyên'
            }), 400

        # Validate hour if provided
        if hour is not None:
            try:
                hour = int(hour)
                if not (0 <= hour <= 23):
                    return jsonify({
                        'status': 'error',
                        'message': 'Giờ không hợp lệ (0-23)'
                    }), 400
            except (ValueError, TypeError):
                return jsonify({
                    'status': 'error',
                    'message': 'Giờ phải là số nguyên'
                }), 400

        # Validate gender (accept both 'nu' from frontend and 'nữ')
        if gender not in ['nam', 'nu', 'nữ']:
            return jsonify({
                'status': 'error',
                'message': 'Giới tính không hợp lệ (nam/nu)'
            }), 400
        # Normalize gender: 'nu' -> 'nữ' for internal processing
        if gender == 'nu':
            gender = 'nữ'

        # Validate calendar type
        if calendar_type not in ['solar', 'lunar']:
            return jsonify({
                'status': 'error',
                'message': 'Loại lịch không hợp lệ (solar/lunar)'
            }), 400

        # Validate leap_month type
        if not isinstance(leap_month, bool):
            leap_month = str(leap_month).lower() in ['true', '1', 'yes']
        
        # Import use case
        from application.use_cases.generate_chart import GenerateChartUseCase
        use_case = GenerateChartUseCase()
        
        # Execute use case (year, month, day, hour already validated and converted to int)
        result = use_case.execute(
            year=year,
            month=month,
            day=day,
            hour=hour,
            gender=gender,
            calendar_type=calendar_type,
            leap_month=leap_month
        )
        
        return jsonify(result)

    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': f'Invalid input: {str(e)}'
        }), 400
    except KeyError as e:
        return jsonify({
            'status': 'error',
            'message': f'Missing required field: {str(e)}'
        }), 400
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.exception("Unexpected error in chart generation")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error occurred'
        }), 500


@chart_bp.route('/star/<star_name>', methods=['GET'])
def get_star_info(star_name: str):
    """
    Get detailed information about a specific star (UC-03)
    
    Response:
        {
            "name": "Tử Vi",
            "type": "Chính Tinh",
            "nature": "Cát",
            "meaning": {...}
        }
    """
    try:
        from data.star_details import CHINH_TINH_DETAILS
        from interpretation import STAR_MEANINGS
        
        # Check in Chinh Tinh first
        if star_name in CHINH_TINH_DETAILS:
            return jsonify(CHINH_TINH_DETAILS[star_name])
        
        # Check in Phu Tinh
        if star_name in STAR_MEANINGS:
            phu_tinh = STAR_MEANINGS[star_name]
            return jsonify({
                'name': star_name,
                'type': 'Phụ Tinh',
                'nature': phu_tinh.get('nature', 'Trung'),
                'effect': phu_tinh.get('effect', ''),
                'meaning': {
                    'general': phu_tinh.get('effect', ''),
                }
            })
        
        return jsonify({'status': 'error', 'message': 'Không tìm thấy sao'}), 404
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@chart_bp.route('/palace/<palace_name>', methods=['GET'])
def get_palace_info(palace_name: str):
    """
    Get information about a specific palace
    
    Response:
        {
            "name": "Mệnh",
            "meaning": {...}
        }
    """
    try:
        from interpretation import PALACE_MEANINGS
        
        if palace_name in PALACE_MEANINGS:
            return jsonify(PALACE_MEANINGS[palace_name])
        
        return jsonify({'status': 'error', 'message': 'Không tìm thấy cung'}), 404
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@chart_bp.route('/fortune', methods=['POST'])
def get_fortune():
    """
    Get fortune periods (Đại Hạn, Tiểu Hạn, Lưu Niên) - UC-05
    
    Request:
        {
            "chart": {...},
            "year": 2024
        }
    
    Response:
        {
            "status": "success",
            "data": {
                "dai_han_all": [...],
                "current_dai_han": {...},
                "tieu_han": {...},
                "luu_nien": {...}
            }
        }
    """
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
        
        return jsonify({
            'status': 'success',
            'data': fortune
        })

    except ValueError as e:
        return jsonify({
            'status': 'error',
            'message': f'Invalid input: {str(e)}'
        }), 400
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Unexpected error in fortune calculation")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error occurred'
        }), 500
