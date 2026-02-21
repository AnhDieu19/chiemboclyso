"""
Candidate Finder: Core logic to iterate through dates and filter charts.
"""
from chart import generate_birth_chart, generate_birth_chart_lunar
from logic.trait_mapper import TraitMapper
from data import DIA_CHI, THIEN_CAN
import itertools

class CandidateFinder:
    def __init__(self):
        self.mapper = TraitMapper()

    def find_candidates(self, constraints):
        """
        Find candidates based on constraints.
        constraints: {
            'year': int (required),
            'month': int (optional),
            'day': int (optional),
            'hour': int (optional),
            'gender': 'nam'/'nu' (required),
            'traits': [list of strings]
        }
        """
        candidates = []
        
        year = constraints.get('year')
        gender = constraints.get('gender', 'nam')
        start_month = constraints.get('month') or 1
        end_month = constraints.get('month') or 12
        
        start_day = constraints.get('day') or 1
        end_day = constraints.get('day') or 30 # Simple loop
        
        start_hour = constraints.get('hour') # 0-11 (12 canh gio)
        hour_range = range(0, 12) if start_hour is None else [start_hour]
        
        # 1. Iterate through time (Lunar Calendar approximation)
        # Note: We loop lunar directly for simplicity as Tu Vi uses Lunar.
        # Converting Solar to Lunar for iteration is harder without a specific library, 
        # so for now assume input is Lunar or we iterate logical combinations.
        
        for m in range(start_month, end_month + 1):
            for d in range(start_day, end_day + 1): # Max 30
                 for h in hour_range:
                    try:
                        # Generate basic chart info
                        # We don't need full generation for filtering if we optimize, 
                        # but for MVP lets generate full structure
                        chart = generate_birth_chart_lunar(d, m, year, h, gender, False) # Assume no leap month for MVP simplicity
                        
                        # 2. Check criteria
                        match_info = self.check_criteria(chart, constraints.get('traits', []))
                        
                        if match_info['score'] > 0 or not constraints.get('traits'):
                            # Add to candidates
                            candidates.append({
                                'date': {'day': d, 'month': m, 'year': year, 'hour': h},
                                'gender': gender,
                                'chart_summary': self.summarize_chart(chart),
                                'match_info': match_info
                            })
                            
                    except Exception as e:
                        continue # Invalid date or error
        
        return candidates

    def check_criteria(self, chart, traits):
        """
        Check if chart satisfies traits.
        Returns score and details.
        """
        score = 0
        details = {}
        
        for trait in traits:
            criteria_list = self.mapper.get_criteria(trait)
            # Logic: If trait implies (A or B or C), and chart has A, then Match.
            trait_match = False
            matched_stars = []
            
            for criterion in criteria_list:
                cung_name = criterion.get('cung')
                sao_name = criterion.get('sao')
                
                # Find palace
                palace = next((p for p in chart['positions'].values() if p['cung'] == cung_name), None)
                if palace:
                    # Check star presence
                    star_names = [s['name'] for s in palace['stars']]
                    if sao_name in star_names:
                        trait_match = True
                        matched_stars.append(f"{cung_name} có {sao_name}")
            
            if trait_match:
                score += 1
                details[trait] = matched_stars
        
        return {'score': score, 'details': details}

    def summarize_chart(self, chart):
        """Extract key info for display table"""
        # Get Menh, Than, Quan, Tai...
        menh = next((p for p in chart['positions'].values() if p.get('is_menh', False)), None)
        if not menh: # Fallback or safety
             menh = next((p for p in chart['positions'].values() if p.get('cung') == 'Mệnh'), None)
        
        if not menh:
            return {'menh_at': '?', 'menh_chinh_tinh': []}

        return {
            'menh_at': menh['chi'],
            'menh_chinh_tinh': [s['name'] for s in menh['stars'] if s.get('type') == 1 or s.get('is_chinh_tinh', False)] # logic check type needed
        }
