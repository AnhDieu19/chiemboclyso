"""
Generate Chart Use Case

Orchestrate việc tính toán và gen lá số Tử Vi.
Tách từ: backend/application/use_cases/generate_chart.py
"""


class GenerateChartUseCase:
    """Use case để generate birth chart"""
    
    def execute(self, year: int, month: int, day: int, hour: int, 
                gender: str, calendar_type: str = 'solar', leap_month: bool = False):
        """
        Execute use case
        
        Args:
            year: Năm sinh
            month: Tháng sinh
            day: Ngày sinh
            hour: Giờ sinh (0-23)
            gender: Giới tính ('nam' hoặc 'nữ')
            calendar_type: Loại lịch ('solar' hoặc 'lunar')
            leap_month: Có phải tháng nhuận không
        
        Returns:
            Dict chứa chart, interpretation và tai_menh analysis
        """
        from chart.chart_builder import (
            generate_birth_chart, 
            generate_birth_chart_lunar,
            generate_partial_chart
        )
        from interpretation.chart_analyzer import generate_overall_interpretation
        from analytics.talent_fortune_engine import TalentFortuneAnalyzer
        from presentation.adapters.chart_adapter import adapter_chart_response
        
        # Convert hour to chi index
        hour_index = None
        if hour is not None:
            hour_index = ((hour + 1) // 2) % 12
        
        has_full_data = day is not None and hour_index is not None
        
        # Generate chart based on calendar type
        if not has_full_data:
            chart = generate_partial_chart(year, month, gender)
            interpretation = {'summary': 'Lá số thiếu thông tin.', 'details': ''}
        elif calendar_type == 'lunar':
            chart = generate_birth_chart_lunar(day, month, year, hour_index, gender, leap_month)
            interpretation = generate_overall_interpretation(chart)
        else:
            chart = generate_birth_chart(day, month, year, hour_index, gender)
            interpretation = generate_overall_interpretation(chart)
        
        # Format response
        response_data = adapter_chart_response(chart, interpretation)
        response_data['data']['internal_chart'] = chart
        
        # Tai-Menh analysis if full data
        if has_full_data:
            try:
                analyzer = TalentFortuneAnalyzer(chart)
                tai_menh_result = analyzer.analyze()
                
                from constants import CATEGORY_META, CATEGORY_ADVICE
                
                category = tai_menh_result.get('category', 'Tài Mệnh Cân Bằng')
                meta = CATEGORY_META.get(category, {"icon": "❓", "color": "#7f8c8d"})
                advice_list = CATEGORY_ADVICE.get(category, [])
                
                tai_menh_result['category_icon'] = meta['icon']
                tai_menh_result['category_color'] = meta['color']
                tai_menh_result['advice'] = advice_list
                
                response_data['data']['tai_menh'] = tai_menh_result
            except Exception as e:
                print(f"Warning: Tài-Mệnh analysis failed: {e}")
                response_data['data']['tai_menh'] = None
        
        return response_data
