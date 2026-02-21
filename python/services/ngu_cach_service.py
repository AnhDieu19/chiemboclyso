"""
Flask Blueprint cho API Ngũ Cách đặt tên
Tích hợp vào Flask app tuvi-app
"""

from flask import Blueprint, request, jsonify, render_template
from logic.ngu_cach_engine import NguCachEngine, analyze_name
from data.stroke_count import get_all_stroke_data

ngu_cach_bp = Blueprint('ngu_cach', __name__)


@ngu_cach_bp.route('/ngu-cach')
def index():
    """Render trang chủ Ngũ Cách"""
    return render_template('ngu_cach_view.html')


@ngu_cach_bp.route('/api/ngu-cach/calculate', methods=['POST'])
def calculate():
    """
    API tính Ngũ Cách
    
    Request body:
    {
        "ho": "Trần",
        "dem": "Văn",       // optional
        "ten": "Hùng",
        "ho_stroke": 16,    // optional, nếu muốn nhập số nét trực tiếp
        "dem_stroke": 4,    // optional
        "ten_stroke": 12    // optional
    }
    
    Response:
    {
        "success": true,
        "data": {
            "input": {...},
            "ngu_cach": {
                "thien_cach": {...},
                "nhan_cach": {...},
                "dia_cach": {...},
                "ngoai_cach": {...},
                "tong_cach": {...}
            },
            "summary": {...}
        }
    }
    """
    try:
        data = request.json
        
        ho = data.get('ho', '').strip()
        dem = data.get('dem', '').strip() or None
        ten = data.get('ten', '').strip()
        
        # Số nét (optional)
        ho_stroke = data.get('ho_stroke')
        dem_stroke = data.get('dem_stroke')
        ten_stroke = data.get('ten_stroke')
        
        # Validate required fields
        if not ho:
            return jsonify({
                'success': False,
                'error': 'Thiếu họ'
            }), 400
        
        if not ten:
            return jsonify({
                'success': False,
                'error': 'Thiếu tên'
            }), 400
        
        # Tính Ngũ Cách
        result = analyze_name(
            ho=ho,
            dem=dem,
            ten=ten,
            ho_stroke=int(ho_stroke) if ho_stroke else None,
            dem_stroke=int(dem_stroke) if dem_stroke else None,
            ten_stroke=int(ten_stroke) if ten_stroke else None
        )
        
        if not result["success"]:
            return jsonify({
                'success': False,
                'error': 'Không thể tính Ngũ Cách',
                'validation_errors': result["errors"]
            }), 400
        
        return jsonify({
            'success': True,
            'data': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@ngu_cach_bp.route('/api/ngu-cach/stroke-data', methods=['GET'])
def get_stroke_data():
    """
    Lấy dữ liệu số nét để hiển thị gợi ý
    
    Response:
    {
        "success": true,
        "data": {
            "ho": {...},
            "ten_dem": {...},
            "ten": {...}
        }
    }
    """
    try:
        data = get_all_stroke_data()
        return jsonify({
            'success': True,
            'data': data
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@ngu_cach_bp.route('/api/ngu-cach/lookup', methods=['GET'])
def lookup_stroke():
    """
    Tra cứu số nét của một chữ
    
    Query params:
        name: Chữ cần tra cứu
        type: "ho" | "dem" | "ten" | "auto" (default)
    
    Response:
    {
        "success": true,
        "name": "TRẦN",
        "stroke": 16,
        "found": true
    }
    """
    try:
        name = request.args.get('name', '').strip()
        name_type = request.args.get('type', 'auto')
        
        if not name:
            return jsonify({
                'success': False,
                'error': 'Thiếu tên cần tra cứu'
            }), 400
        
        from data.stroke_count import get_stroke_count
        stroke = get_stroke_count(name, name_type)
        
        return jsonify({
            'success': True,
            'name': name.upper(),
            'stroke': stroke,
            'found': stroke is not None
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
