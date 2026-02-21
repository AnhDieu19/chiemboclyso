"""
Analytics Routes - Analytics và visualization endpoints
"""
from flask import Blueprint, request, jsonify

analytics_bp = Blueprint('analytics', __name__)

# Module-level constants (avoid re-creating per request)
CATEGORY_META = {
    "Tài Mệnh Song Toàn": {"icon": "👑", "color": "#f1c40f"},
    "Tài Cao Mệnh Thấp": {"icon": "🎭", "color": "#9b59b6"},
    "Mệnh Cao Tài Thấp": {"icon": "🍀", "color": "#27ae60"},
    "Tài Mệnh Đều Thấp": {"icon": "💪", "color": "#e67e22"},
    "Tài Vượt Mệnh": {"icon": "⚡", "color": "#3498db"},
    "Mệnh Vượt Tài": {"icon": "🌟", "color": "#1abc9c"},
    "Tài Mệnh Cân Bằng": {"icon": "⚖️", "color": "#95a5a6"},
}

CATEGORY_ADVICE = {
    "Tài Mệnh Song Toàn": [
        "Biết trân trọng những gì mình có.",
        "Chia sẻ tài năng và may mắn cho người khác.",
        "Không kiêu ngạo, giữ đức khiêm tốn."
    ],
    "Tài Cao Mệnh Thấp": [
        "Tu dưỡng đạo đức, làm việc thiện để cải mệnh.",
        "Tìm quý nhân phò tá, đừng cố gắng một mình.",
        "Kiên nhẫn, vạn sự khởi đầu nan.",
        "Tránh đầu tư mạo hiểm, giữ ổn định."
    ],
    "Mệnh Cao Tài Thấp": [
        "Trau dồi kỹ năng, học hỏi không ngừng.",
        "Biết ơn và sống tích cực.",
        "Không ỷ lại vào may mắn, phải tự phấn đấu."
    ],
    "Tài Mệnh Đều Thấp": [
        "Không bỏ cuộc, nghịch cảnh rèn luyện người.",
        "Tìm môi trường phù hợp để phát triển.",
        "Tu tâm, hành thiện để tích đức.",
        "Kết giao với người tốt, tránh tiểu nhân."
    ],
    "Tài Vượt Mệnh": [
        "Tìm quý nhân, môi trường tốt để tài năng phát huy.",
        "Kiên nhẫn chờ thời, vận may sẽ đến.",
        "Làm việc thiện để tích phúc đức."
    ],
    "Mệnh Vượt Tài": [
        "Trau dồi kỹ năng để xứng đáng với may mắn.",
        "Biết ơn và chia sẻ với người khác.",
        "Không lãng phí thời gian, may mắn có giới hạn."
    ],
    "Tài Mệnh Cân Bằng": [
        "Cuộc sống ổn định, tiếp tục phát triển.",
        "Cân bằng giữa làm việc và nghỉ ngơi.",
        "Giữ gìn sức khỏe và các mối quan hệ."
    ]
}


@analytics_bp.route('/tai-menh', methods=['POST'])
def analyze_tai_menh():
    """
    Phân tích quan hệ Tài và Mệnh (UC-TAI-MENH-04)
    
    Request:
        {
            "chart": {...}
        }
    
    Response:
        {
            "status": "success",
            "data": {
                "category": "Tài Mệnh Song Toàn",
                "tai_score": 85,
                "menh_score": 90,
                "advice": [...]
            }
        }
    """
    try:
        data = request.json
        
        # Get chart from request or generate from birth info
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
        
        if 'chart' in data:
            chart = data['chart']
        else:
            # Generate chart if birth info provided
            required = ['day', 'month', 'year']
            for field in required:
                if field not in data or data[field] is None:
                    return jsonify({'status': 'error', 'message': f'Missing required field: {field}'}), 400
            try:
                day = int(data['day'])
                month = int(data['month'])
                year = int(data['year'])
                hour = int(data.get('hour', 0))
            except (ValueError, TypeError) as e:
                return jsonify({'status': 'error', 'message': f'Invalid numeric field: {e}'}), 400
            gender = data.get('gender', 'nam')
            
            from chart.chart_builder import generate_birth_chart
            chart = generate_birth_chart(day, month, year, hour, gender)
        
        # Analyze Tai Menh
        from analytics.talent_fortune_engine import TalentFortuneAnalyzer
        analyzer = TalentFortuneAnalyzer(chart)
        result = analyzer.analyze()
        
        # Enrich with metadata
        category = result.get('category', 'Tài Mệnh Cân Bằng')
        meta = CATEGORY_META.get(category, {"icon": "❓", "color": "#7f8c8d"})
        advice_list = CATEGORY_ADVICE.get(category, [])
        
        return jsonify({
            'status': 'success',
            'data': {
                **result,
                'category_icon': meta['icon'],
                'category_color': meta['color'],
                'advice': advice_list
            }
        })
        
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Error in tai-menh analysis")
        return jsonify({
            'status': 'error',
            'message': 'Internal server error'
        }), 500


@analytics_bp.route('/drilldown', methods=['GET'])
def api_drilldown():
    """Drilldown data for analytics dashboard"""
    try:
        gender = request.args.get('gender', 'all')
        year = request.args.get('year')  # str or None
        month = request.args.get('month')  # str or None
        
        # Convert to int if provided
        if year is not None:
            try:
                year = int(year)
            except (ValueError, TypeError):
                return jsonify({'status': 'error', 'message': 'year must be an integer'}), 400
        if month is not None:
            try:
                month = int(month)
            except (ValueError, TypeError):
                return jsonify({'status': 'error', 'message': 'month must be an integer'}), 400
        
        from analytics.visualize_data import get_drilldown_data
        data = get_drilldown_data(year=year, month=month, gender_filter=gender)
        
        return jsonify(data)
        
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Error in drilldown")
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
