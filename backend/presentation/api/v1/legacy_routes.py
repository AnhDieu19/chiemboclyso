"""
Legacy Routes - Backward compatibility với API cũ

Giữ các endpoint cũ để không làm hỏng frontend hiện tại
"""
from flask import Blueprint, request, jsonify

legacy_bp = Blueprint('legacy', __name__)


@legacy_bp.route('/generate', methods=['POST'])
def generate_legacy():
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/chart/generate
    """
    from presentation.api.v1.chart_routes import generate
    return generate()


@legacy_bp.route('/tai-menh', methods=['POST'])
def tai_menh_legacy():
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/analytics/tai-menh
    """
    from presentation.api.v1.analytics_routes import analyze_tai_menh
    return analyze_tai_menh()


@legacy_bp.route('/finder/solve', methods=['POST'])
def finder_solve_legacy():
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/finder/solve
    """
    from presentation.api.v1.finder_routes import solve
    return solve()


@legacy_bp.route('/ask-ai', methods=['POST'])
def ask_ai_legacy():
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/ai/ask
    """
    from presentation.api.v1.ai_routes import ask_ai
    return ask_ai()


@legacy_bp.route('/chat-ai', methods=['POST'])
def chat_ai_legacy():
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/ai/chat
    """
    from presentation.api.v1.ai_routes import chat_ai
    return chat_ai()


@legacy_bp.route('/fortune', methods=['POST'])
def fortune_legacy():
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/chart/fortune
    """
    from presentation.api.v1.chart_routes import get_fortune
    return get_fortune()


@legacy_bp.route('/star/<star_name>')
def star_info_legacy(star_name):
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/chart/star/<star_name>
    """
    from presentation.api.v1.chart_routes import get_star_info
    return get_star_info(star_name)


@legacy_bp.route('/palace/<palace_name>')
def palace_info_legacy(palace_name):
    """
    Legacy endpoint - redirect to v1
    Alias cho /api/v1/chart/palace/<palace_name>
    """
    from presentation.api.v1.chart_routes import get_palace_info
    return get_palace_info(palace_name)
