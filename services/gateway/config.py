"""
Gateway Configuration - Service Registry & Mode Setup
"""
import os

# Gateway mode: 'monolith' (default) or 'proxy'
GATEWAY_MODE = os.environ.get('GATEWAY_MODE', 'monolith')

# Service Registry - tất cả microservices trong hệ thống
SERVICE_REGISTRY = {
    'tuvi-chart': {
        'port': 5011,
        'prefix': '/api/v1/chart',
        'description': 'Tu Vi Chart Generation',
        'icon': '🔮',
        'health_check': '/api/v1/chart/star/Tử Vi',
    },
    'tuvi-finder': {
        'port': 5012,
        'prefix': '/api/v1/finder',
        'description': 'Reverse Birth-Date Finder',
        'icon': '🔍',
        'health_check': '/api/v1/finder/solve',
    },
    'tuvi-analytics': {
        'port': 5013,
        'prefix': '/api/v1/analytics',
        'description': 'Tai Menh Analytics',
        'icon': '📊',
        'health_check': '/api/v1/analytics/drilldown',
    },
    'tuvi-ai': {
        'port': 5014,
        'prefix': '/api/v1/ai',
        'description': 'AI Gemini Integration',
        'icon': '🤖',
        'health_check': '/api/v1/ai/ask',
    },
    'thai-at': {
        'port': 5015,
        'prefix': '/api/thai-at',
        'description': 'Thái Ất Thần Số',
        'icon': '🔢',
        'health_check': '/thai-at',
    },
    'ki-mon': {
        'port': 5016,
        'prefix': '/api/ki-mon',
        'description': 'Kì Môn Độn Giáp',
        'icon': '🏛️',
        'health_check': '/ki-mon',
    },
    'graph': {
        'port': 5017,
        'prefix': '/graph',
        'description': 'Knowledge Graph Visualization',
        'icon': '🌐',
        'health_check': '/knowledge-graph',
    },
    'vi-dieu-phap': {
        'port': 5018,
        'prefix': '/vdp',
        'description': 'Vi Diệu Pháp Knowledge Graph',
        'icon': '📿',
        'health_check': '/vdp/',
    },
    'luc-nham': {
        'port': 5019,
        'prefix': '/api/luc-nham',
        'description': 'Đại Lục Nhâm',
        'icon': '🔯',
        'health_check': '/luc-nham',
    },
}
