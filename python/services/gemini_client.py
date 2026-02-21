"""
Gemini AI Client - Hỏi Thầy Tử Vi AI
Sử dụng Google Gen AI SDK (v1.0+) và Gemini 3.0
"""

from google import genai
from google.genai import types
from typing import Optional
import json
import os

# Configure API - Load from environment variable
API_KEY = os.environ.get('GEMINI_API_KEY')
if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY environment variable is not set. "
        "Please set it in your .env file or environment."
    )
# Use the new model name
MODEL_NAME = "gemini-2.0-flash" 

# System prompt cho thầy tử vi
SYSTEM_PROMPT = """Bạn là một chuyên gia Tử Vi Nam Phái thực chiến, đề cao tính ứng dụng và thực tế.
Phong cách luận giải: Thẳng thắn, đi thẳng vào trọng tâm, không dùng lời lẽ sáo rỗng hay khen ngợi chung chung.
Khi phân tích, hãy tập trung vào:
1. Bản chất thực của các cách cục (chú ý sự phá cách do Tuần/Triệt/Sát tinh).
2. Tâm lý và hành vi thực tế của đương số.
3. Đưa ra lời khuyên cụ thể về sự nghiệp, tài chính (ví dụ: đầu tư, chuyển việc) dựa trên tính chất sao.
Lưu ý: Nếu thấy cách cục tốt nhưng gặp Tuần/Triệt/Kỵ, hãy cảnh báo ngay về sự trắc trở trước khi thành công."""


def get_client():
    """Get Gemini client instance."""
    return genai.Client(api_key=API_KEY)


def format_chart_for_ai(chart_data: dict, interpretation: dict) -> str:
    """Format chart data for AI prompt."""
    basic = interpretation.get('basic_info', {})
    
    chart_text = f"""
=== THÔNG TIN LÁ SỐ ===
- Năm sinh: {basic.get('year_can_chi', '?')}
- Cục: {basic.get('cuc', '?')}
- Cung Mệnh: {basic.get('menh_chi', '?')}
- Cung Thân: {basic.get('than_chi', '?')}
- Bản Mệnh (Nạp Âm): {basic.get('nap_am', '?')}
- Mệnh Chủ: {basic.get('menh_chu', '?')}
- Thân Chủ: {basic.get('than_chu', '?')}

=== TỨ HÓA ===
"""
    tu_hoa = chart_data.get('tu_hoa', {})
    for hoa_name, hoa_info in tu_hoa.items():
        chart_text += f"- {hoa_name}: {hoa_info.get('star', '')} tại cung {hoa_info.get('position', '')}\n"
    
    # Add palace info
    chart_text += "\n=== CÁC CUNG CHÍNH ===\n"
    positions = chart_data.get('positions', {})
    cung_map = chart_data.get('cung_map', {})
    
    important_cung = ['Mệnh', 'Thân', 'Quan Lộc', 'Tài Bạch', 'Phu Thê', 'Tật Ách', 'Phúc Đức', 'Thiên Di']
    for pos, data in positions.items():
        cung_name = data.get('cung', '')
        # Include more palaces for better context
        stars = [s.get('name') if isinstance(s, dict) else s for s in data.get('stars', [])]
        chart_text += f"- {cung_name}: {', '.join(stars)}\n"
    
    return chart_text


def format_system_interpretation(interpretation: dict) -> str:
    """Format system interpretation for comparison."""
    text = "\n=== HỆ THỐNG ĐÃ PHÂN TÍCH ===\n"
    
    menh = interpretation.get('menh_interpretation', {})
    text += f"Cung Mệnh: {menh.get('interpretation', '')}\n"
    text += f"Đánh giá: {menh.get('strength', 'Trung bình')}\n"
    
    if interpretation.get('cach_cuc'):
        text += "\nCách cục phát hiện:\n"
        for cc in interpretation.get('cach_cuc', [])[:3]:
            text += f"- {cc.get('name', '')}: {cc.get('meaning', '')}\n"
    
    text += f"\nTổng quan: {interpretation.get('fortune', '')}\n"
    text += f"Lời khuyên: {interpretation.get('advice', '')}\n"
    
    return text


def ask_master_ai(chart_data: dict, interpretation: dict) -> dict:
    """
    Hỏi thầy AI luận giải lá số.
    Using new SDK generate_content
    """
    try:
        client = get_client()
        
        chart_text = format_chart_for_ai(chart_data, interpretation)
        system_text = format_system_interpretation(interpretation)
        
        prompt = f"""{SYSTEM_PROMPT}

Hãy xem và luận giải lá số tử vi sau:

{chart_text}

{system_text}

Với vai trò thầy tử vi 50 năm kinh nghiệm, hãy:
1. Đưa ra luận giải tổng quan của thầy về lá số này
2. Nhận xét về những điểm mạnh và điểm cần lưu ý
3. Đưa ra lời khuyên cho đương số
4. Nếu thấy hệ thống phân tích chưa đầy đủ, hãy bổ sung thêm"""

        # New SDK call
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )
        
        return {
            'success': True,
            'response': response.text,
            'model': MODEL_NAME
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'response': f"Xin lỗi, thầy không thể xem lá số lúc này. Lỗi: {str(e)}"
        }


def chat_with_master(chart_data: dict, interpretation: dict, user_message: str, history: list = None) -> dict:
    """
    Chat với thầy tử vi về lá số.
    Using new SDK generate_content (chat is managed by history context manually or separate call)
    For simplicity in new SDK, we can just append history to contents or use proper ChatSession if available/preferred.
    Here we'll reconstruct context.
    """
    try:
        client = get_client()
        
        chart_text = format_chart_for_ai(chart_data, interpretation)
        
        # Build contents list for history
        contents = []
        
        # System instructions set as starting context
        contents.append(types.Content(
            role="user",
            parts=[types.Part(text=f"{SYSTEM_PROMPT}\n\nĐây là lá số của tôi:\n{chart_text}")]
        ))
        
        contents.append(types.Content(
            role="model",
            parts=[types.Part(text="Vâng, tôi đã nắm rõ lá số. Xin mời bạn đặt câu hỏi.")]
        ))

        # Append history
        if history:
            for msg in history:
                role = "user" if msg.get('role') == 'user' else "model"
                text = msg.get('parts', [''])[0]
                contents.append(types.Content(
                    role=role,
                    parts=[types.Part(text=text)]
                ))
        
        # Current message
        contents.append(types.Content(
            role="user",
            parts=[types.Part(text=user_message)]
        ))
        
        # Generate response
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=contents
        )
        
        return {
            'success': True,
            'response': response.text,
            'model': MODEL_NAME
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'response': f"Xin lỗi, thầy không thể trả lời lúc này. Lỗi: {str(e)}"
        }
