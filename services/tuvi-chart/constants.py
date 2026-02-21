"""
Constants for Tu Vi Chart Service

Extracted from analytics_routes.py for shared use
"""

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
