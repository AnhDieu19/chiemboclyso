"""
AI Routes - Gemini AI integration endpoints
"""
from flask import Blueprint, request, jsonify

ai_bp = Blueprint('ai', __name__)


@ai_bp.route('/ask', methods=['POST'])
def ask_ai():
    """
    Hỏi Thầy AI luận giải lá số (UC-07)
    
    Request:
        {
            "chart": {...},
            "interpretation": {...}
        }
    
    Response:
        {
            "success": true,
            "response": "Luận giải từ AI...",
            "model": "gemini-pro"
        }
    """
    try:
        from services.gemini_client import ask_master_ai
        
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        chart = data.get('chart', {})
        interpretation = data.get('interpretation', {})
        
        if not chart:
            return jsonify({'success': False, 'error': 'Cần cung cấp dữ liệu lá số'}), 400
        
        result = ask_master_ai(chart, interpretation)

        return jsonify(result)

    except ValueError as e:
        return jsonify({
            'success': False,
            'error': 'Invalid input',
            'response': f'Dữ liệu không hợp lệ: {str(e)}'
        }), 400
    except (ConnectionError, OSError) as e:
        return jsonify({
            'success': False,
            'error': 'Connection failed',
            'response': 'Không thể kết nối với AI. Vui lòng thử lại sau.'
        }), 503
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Unexpected error in AI ask endpoint")
        return jsonify({
            'success': False,
            'error': 'Internal error',
            'response': 'Đã xảy ra lỗi. Vui lòng thử lại sau.'
        }), 500


@ai_bp.route('/chat', methods=['POST'])
def chat_ai():
    """
    Chat với Thầy Tử Vi AI (UC-08)
    
    Request:
        {
            "chart": {...},
            "interpretation": {...},
            "message": "Câu hỏi của người dùng",
            "history": [...]
        }
    
    Response:
        {
            "success": true,
            "response": "Câu trả lời từ AI..."
        }
    """
    try:
        from services.gemini_client import chat_with_master
        
        data = request.json
        if not data:
            return jsonify({'success': False, 'error': 'No data provided'}), 400
        
        chart = data.get('chart', {})
        interpretation = data.get('interpretation', {})
        message = data.get('message', '')
        history = data.get('history', [])
        
        if not chart:
            return jsonify({'success': False, 'error': 'Cần cung cấp dữ liệu lá số'}), 400
        
        if not message:
            return jsonify({'success': False, 'error': 'Cần cung cấp câu hỏi'}), 400
        
        result = chat_with_master(chart, interpretation, message, history)

        return jsonify(result)

    except ValueError as e:
        return jsonify({
            'success': False,
            'error': 'Invalid input',
            'response': f'Dữ liệu không hợp lệ: {str(e)}'
        }), 400
    except (ConnectionError, OSError) as e:
        return jsonify({
            'success': False,
            'error': 'Connection failed',
            'response': 'Không thể kết nối với AI. Vui lòng thử lại sau.'
        }), 503
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Unexpected error in AI chat endpoint")
        return jsonify({
            'success': False,
            'error': 'Internal error',
            'response': 'Đã xảy ra lỗi. Vui lòng thử lại sau.'
        }), 500
