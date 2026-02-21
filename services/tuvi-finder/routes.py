"""
Finder Routes - Reverse finder API endpoints

Tách từ: backend/presentation/api/v1/finder_routes.py
"""
from flask import Blueprint, request, jsonify

finder_bp = Blueprint('finder', __name__)


@finder_bp.route('/solve', methods=['POST'])
def solve():
    """Find date candidates based on traits (UC-06)"""
    try:
        data = request.json
        if not data:
            return jsonify({'status': 'error', 'message': 'No data provided'}), 400
        
        if 'year' not in data or data['year'] is None:
            return jsonify({'status': 'error', 'message': 'Missing required field: year'}), 400
        
        try:
            year = int(data['year'])
            month = int(data.get('month', 1))
            day = int(data.get('day', 1))
        except (ValueError, TypeError) as e:
            return jsonify({'status': 'error', 'message': f'Invalid numeric field: {e}'}), 400
        
        gender = data.get('gender', 'nam')
        traits = data.get('traits', [])
        events = data.get('events', [])
        calendar_type = data.get('calendar_type', 'lunar')
        
        facts = {'traits': traits, 'events': events}
        
        from logic.reverse_lookup_engine import ReverseLookupEngine
        from core.lunar_converter import solar_to_lunar
        
        engine = ReverseLookupEngine()
        
        final_year, final_month, final_day = year, month, day
        
        if calendar_type == 'solar':
            lunar_date = solar_to_lunar(day, month, year)
            final_year = lunar_date['year']
            final_month = lunar_date['month']
            final_day = lunar_date['day']
        
        candidates_result = []
        daily_candidates = engine.generate_candidates(final_year, final_month, final_day, gender)
        if daily_candidates:
            for horo in daily_candidates:
                score, details = engine.calculate_score(horo, facts)
                success_data = engine.calculate_success_score(horo)
                
                candidates_result.append({
                    'date': horo.birth_date,
                    'gender': gender,
                    'chart_summary': {
                        'menh_at': horo.palaces['Mệnh'].branch,
                        'menh_chinh_tinh': [s.name for s in horo.palaces['Mệnh'].stars if s.type == 1]
                    },
                    'match_info': {'score': score, 'details': details},
                    'success_info': success_data,
                    'horoscope_ref': horo
                })
        
        ranked_results = engine.rank_candidates(candidates_result)
        
        timeline_data = []
        if ranked_results:
            top_1 = ranked_results[0]
            if 'horoscope_ref' in top_1:
                timeline_data = engine.analyze_timeline(top_1['horoscope_ref'])
            
            for c in candidates_result:
                c.pop('horoscope_ref', None)
            for c in ranked_results:
                c.pop('horoscope_ref', None)
        
        return jsonify({
            'success': True,
            'status': 'success',
            'total': len(candidates_result),
            'candidates': ranked_results,
            'all_candidates': candidates_result,
            'top_timeline': timeline_data
        })
        
    except Exception as e:
        import logging
        logging.getLogger(__name__).exception("Error in finder solve")
        return jsonify({'status': 'error', 'message': 'Internal server error'}), 500
