"""
Reverse Lookup Engine (Level 2)
Implements weighted scoring, broadened scope, and event verification.
"""
from dataclasses import dataclass, field
from typing import List, Dict, Optional
import sys
import os

# Ensure python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core import (
    get_hour_can_chi, determine_cuc, solar_to_lunar
)


from logic.candidate_finder import CandidateFinder
from chart import generate_birth_chart_lunar
from data.finder_rules import get_rule_by_name, FINDER_RULES

# --- DATA STRUCTURES ---

@dataclass
class Star:
    name: str
    type: int = 0  # 1: Chinh tinh, 2: Phu tinh (Simplification)
    characteristics: List[str] = field(default_factory=list)

@dataclass
class Palace:
    position: int # 0-11 (Ty -> Hoi)
    name: str # Menh, Phu Mau...
    stars: List[Star] = field(default_factory=list)
    stem: str = "" # Can
    branch: str = "" # Chi

    def has_star(self, star_name):
        return any(s.name == star_name for s in self.stars)
    
    def has_any_star(self, star_names):
        return any(s.name in star_names for s in self.stars)

@dataclass
class Horoscope:
    birth_date: dict # {day, month, year, hour}
    palaces: Dict[str, Palace] # Keyed by Palace Name (e.g. "Mệnh") or Position Index? 
                               # Better by Name for easy lookup, but Position is unique. 
                               # Let's verify: names can duplicate in rare cases (Than Cu...), but standard 12 names.
    palaces_by_index: Dict[int, Palace]
    
    # Helper to find where a star is
    def find_star_position(self, star_name):
        for p in self.palaces_by_index.values():
            if p.has_star(star_name):
                return p
        return None

# --- ENGINE ---

class ReverseLookupEngine:
    def __init__(self):
        pass

    def generate_candidates(self, year, month, day, gender) -> List[Horoscope]:
        """
        Generate 12 candidates for the given date (12 hours).
        Uses the existing `generate_birth_chart_lunar` from `chart` module.
        """
        candidates = []
        # Loop 0-11 for 12 canh gio
        for hour in range(12):
            try:
                # Real chart generation
                chart_data = generate_birth_chart_lunar(day, month, year, hour, gender, False)
                candidates.append(self._convert_to_horoscope(chart_data))
            except Exception as e:
                continue
        return candidates

    def _convert_to_horoscope(self, chart_data) -> Horoscope:
        """Convert dict output from chart library to Horoscope object"""
        palaces = {}
        palaces_by_index = {}
        
        for pos_idx, p_data in chart_data['positions'].items():
            # Create Star objects
            # Need to identify Main Stars (Type 1)
            # Simple check list
            MAIN_STARS = ["Tử Vi", "Thiên Cơ", "Thái Dương", "Vũ Khúc", "Thiên Đồng", "Liêm Trinh", 
                          "Thiên Phủ", "Thái Âm", "Tham Lang", "Cự Môn", "Thiên Tướng", "Thiên Lương", "Thất Sát", "Phá Quân"]
            
            stars = []
            for s in p_data['stars']:
                star_name = s['name']
                s_type = 1 if star_name in MAIN_STARS else 2
                stars.append(Star(name=star_name, type=s_type))
            
            # Determine logic name (Mệnh, Phụ Mẫu...)
            # Note: chart_data['positions'] might not explicitly list "Mệnh" as a key, 
            # but has 'cung' field with the name.
            cung_name = p_data['cung']
            
            palace = Palace(
                position=pos_idx,
                name=cung_name,
                stars=stars,
                stem="", # Placeholder
                branch=p_data['chi']
            )
            
            palaces[cung_name] = palace
            palaces_by_index[pos_idx] = palace
            
            # Special handling for Body (Thân) - it might double up on a palace
            if p_data.get('is_than'):
                palaces['Thân'] = palace # Alias
            if p_data.get('is_menh'):
                palaces['Mệnh'] = palace # Alias
                
        return Horoscope(
            birth_date={'day': chart_data['lunar_date']['day'], 
                        'month': chart_data['lunar_date']['month'], 
                        'year': chart_data['lunar_date']['year'], 
                        'hour': chart_data['hour']},
            palaces=palaces,
            palaces_by_index=palaces_by_index
        )

    def calculate_score(self, horoscope: Horoscope, user_facts: dict):
        """
        Calculate matching score.
        user_facts: {
             'traits': ['Công nghệ thông tin (IT)', 'Nóng nảy...'],
             'events': [{'year': 2022, 'type': 'Kết hôn'}, ...]
        }
        """
        score = 0
        details = {}

        # 1. TRAITS SCORING
        for trait_name in user_facts.get('traits', []):
            rule = get_rule_by_name(trait_name)
            if not rule:
                continue
                
            trait_score = 0
            matched_reasons = []
            
            # Weighted Scoring
            weight = rule.get('weight', 1.0)
            
            # Check Scope - Support both List (uniform) and Dict (weighted)
            scopes_config = rule.get('scope', [])
            normalized_scopes = {}
            
            if isinstance(scopes_config, list):
                # Legacy: List of strings -> Weight 1.0 for all
                normalized_scopes = {name: 1.0 for name in scopes_config}
            elif isinstance(scopes_config, dict):
                # New: Dict {Name: Weight}
                normalized_scopes = scopes_config
                
            for scope_name, scope_modifier in normalized_scopes.items():
                palace = horoscope.palaces.get(scope_name)
                if not palace: continue
                
                # Apply modifier to base points
                # Base Logic: 10 pts for Positive, 5 for Bonus
                
                # Check Positive Stars
                positive = rule.get('positive_stars', [])
                for star in positive:
                    if palace.has_star(star):
                        pts = 10 * weight * scope_modifier
                        trait_score += pts
                        # Round for display
                        matched_reasons.append(f"{scope_name} có {star} (+{round(pts, 1)})")
                
                # Check Bonus Stars
                bonus = rule.get('positive_stars_bonus', [])
                for star in bonus:
                    if palace.has_star(star):
                        pts = 5 * weight * scope_modifier
                        trait_score += pts
                        matched_reasons.append(f"{scope_name} có {star} (+{round(pts, 1)})")
                
                # Check Negative Stars
                negative = rule.get('negative_stars', [])
                for star in negative:
                    if palace.has_star(star):
                        pts = -5 * weight * scope_modifier
                        trait_score += pts
                        matched_reasons.append(f"{scope_name} có {star} ({round(pts, 1)})")

            
            if trait_score != 0:
                score += trait_score
                details[trait_name] = matched_reasons

        # 2. EVENT CHECKING ("Killer Feature")
        for event in user_facts.get('events', []):
            event_year = event.get('year')
            event_type = event.get('type')
            
            if event_year and event_type:
                event_name_ui = f"{event_type} năm {event_year}"
                evt_score, evt_reasons = self._check_year_event(horoscope, int(event_year), event_type)
                if evt_score > 0:
                    score += evt_score
                    details[event_name_ui] = evt_reasons

        return score, details

    def _check_year_event(self, horoscope, year, event_type):
        """
        Generic Event Checker based on Year.
        Logic:
        1. Determine 'Lưu Thái Tuế' position for the Year (by Chi).
        2. Check relationship with relevant Palace (e.g., Sinh con -> Tu Tuc).
        3. Check relevant Stars in Luu Thai Tue palace.
        """
        score = 0
        reasons = []
        
        # MAPPING RULES
        # Define what to look for based on event type
        # TODO: Move to external config
        EVENT_RULES = {
            'Kết hôn': {
                'target_palace': 'Phu Thê',
                'stars': ['Hồng Loan', 'Đào Hoa', 'Thiên Hỹ', 'Hỷ Thần', 'Lưu Hà'],
                'weight': 1.0
            },
            'Sinh con': {
                'target_palace': 'Tử Tức',
                'stars': ['Thai', 'Long Trì', 'Phượng Các', 'Hồng Loan', 'Thiên Hỹ', 'Mộc Dục'],
                'weight': 1.0
            },
             'Đổi việc': {
                'target_palace': 'Quan Lộc',
                'stars': ['Thiên Mã', 'Lộc Tồn', 'Hóa Lộc', 'Lưu Hà', 'Phá Quân'],
                'weight': 0.8
            },
             'Chuyển nhà': {
                'target_palace': 'Điền Trạch',
                'stars': ['Thiên Mã', 'Lộc Tồn', 'Thiên Đồng', 'Hóa Lộc', 'Hồng Loan'],
                'weight': 0.8
            }
        }
        
        rule = EVENT_RULES.get(event_type)
        if not rule:
            return 0, [] # Unknown event type
            
        target_calace_name = rule['target_palace']
        target_stars = rule['stars']
        
        # 1. Calculate Luu Thai Tue Index (Year Chi)
        # 4 AD = Ty (Rat) -> Index 0? No.
        # Custom mapping: Tý=0, Sửu=1...
        # 1984 (Giáp Tý) -> 0. (1984 - 4) % 12 = 0. Correct.
        year_chi_idx = (year - 4) % 12 
        
        luu_thai_tue_palace = horoscope.palaces_by_index.get(year_chi_idx)
        if not luu_thai_tue_palace:
            return 0, []

        # 2. Check Palace Coincidence (Lưu Thái Tuế nhập cung nào?)
        target_palace = horoscope.palaces.get(target_calace_name)
        
        if target_palace:
            # Nhập Cung (Conjunction)
            if target_palace.position == luu_thai_tue_palace.position:
                pts = 50
                score += pts
                reasons.append(f"Lưu Thái Tuế ({year}) nhập cung {target_calace_name} (+50)")
            
            # Xung Chiếu (Opposition) - 6 steps away
            elif abs(target_palace.position - luu_thai_tue_palace.position) == 6:
                pts = 30
                score += pts
                reasons.append(f"Lưu Thái Tuế ({year}) xung chiếu {target_calace_name} (+30)")
                
            # Tam Hợp (Trine) - 4 steps away
            # pos diff is 4 or 8
            diff = abs(target_palace.position - luu_thai_tue_palace.position)
            if diff == 4 or diff == 8:
                pts = 20
                score += pts
                reasons.append(f"Lưu Thái Tuế ({year}) tam hợp {target_calace_name} (+20)")

        # 3. Check Stars in Luu Thai Tue Palace
        # Find matches
        matches = [s for s in target_stars if luu_thai_tue_palace.has_star(s)]
        if matches:
            stars_str = ", ".join(matches)
            pts = 10 * len(matches)
            score += pts
            reasons.append(f"Năm {year} có sao {stars_str} tại Lưu Thái Tuế (+{pts})")

        return score, reasons

    def rank_candidates(self, candidates_scores):
        """Sort and find top 3"""
        sorted_list = sorted(candidates_scores, key=lambda x: x['match_info']['score'], reverse=True)
        return sorted_list[:3]

    def calculate_success_score(self, horoscope):
        """
        Calculates the 'Success Score' based on new Weighting Matrix.
        Criteria:
        - Weights: Mệnh (40%), Thân (30%), Tài (20%), Quan (20%) -> Total > 100%? 
          Wait, usually sum is 100%. Let's assume normalized weights or just additive points.
          User Prompt: Mệnh (40%), Thân (30%), Tài & Quan (20%). Total 90%? 
          Let's treat them as weights: 0.4, 0.3, 0.15, 0.15.
        
        - Bonus: Miếu/Vượng (+100), Hãm (-50), Hóa Lộc/Quyền/Khoa (+50)
        - Penalty: Tuần/Triệt (-20%), Không Kiếp hãm (-30%)
        """
        # Import brightness checker
        from data.star_brightness import get_star_brightness
        
        # 1. Define Weights
        WEIGHTS = {
            'Mệnh': 0.40,
            'Thân': 0.30,
            'Tài Bạch': 0.15,
            'Quan Lộc': 0.15
        }
        
        # 2. Define Special Stars
        BONUS_STARS = ["Hóa Lộc", "Hóa Quyền", "Hóa Khoa"]
        PENALTY_STARS = ["Tuần", "Triệt"]
        KK_STARS = ["Địa Không", "Địa Kiếp"]
        
        # Helpers for Archetype
        wealth_score = 0
        power_score = 0
        happiness_score = 0
        
        final_score = 0
        
        for palace_name, weight in WEIGHTS.items():
            palace = horoscope.palaces.get(palace_name)
            if not palace: continue
            
            p_score = 0
            
            # A. Calculate Star Points
            # We need to iterate main stars in this palace
            has_chinh_tinh = False
            
            for star in palace.stars:
                if star.type == 1: # Chinh tinh
                    has_chinh_tinh = True
                    # Check Brightness
                    # Assuming star.name is correct
                    # Need Chi Index of the palace to check brightness
                    # Palace has 'branch' string, need to convert to index or use palace.position
                    
                    br_info = get_star_brightness(star.name, palace.position)
                    code = br_info.get('code', 'B')
                    
                    if code in ['M', 'V']:
                        p_score += 100
                    elif code == 'H':
                        p_score -= 50
                    elif code == 'Đ':
                         p_score += 20 # Small bonus for Dac dia
                    
                    # Classify star for Archetype
                    if star.name in ["Vũ Khúc", "Thái Âm", "Thiên Phủ", "Lộc Tồn"]:
                        wealth_score += 1
                        if code in ['M', 'V']: wealth_score += 1
                    
                    if star.name in ["Tử Vi", "Thái Dương", "Thất Sát", "Phá Quân", "Thiên Tướng"]:
                        power_score += 1
                        if code in ['M', 'V']: power_score += 1
                        
                    if star.name in ["Thiên Đồng", "Thiên Lương", "Thiên Cơ"]:
                        happiness_score += 1
            
            # B. Bonus Stars (Tam Hóa)
            for s in BONUS_STARS:
                if palace.has_star(s):
                    p_score += 50
                    if s == "Hóa Lộc": wealth_score += 2
                    if s == "Hóa Quyền": power_score += 2
            
            # C. Penalties (Multipliers)
            # Tuần/Triệt
            is_triet = palace.has_star("Triệt")
            is_tuan = palace.has_star("Tuần")
            
            if is_tuan or is_triet:
                p_score = p_score * 0.8 # -20%
                
            # Không Kiếp Hãm
            # Check brightness of KK if present
            # KK hãm at: Hợi, Tý, Dần, Thân, Dậu... (Simplified check needed)
            # For now, let's assume if existing in map and H => penalty
            # Actually KK is Phu Tinh, brightness logic might be complex or in data.
            # Let's simplify: If KK is present, apply penalty.
            for kk in KK_STARS:
                if palace.has_star(kk):
                    # Check if Hãm? 
                    # Let's assume -30% for now as requested "Gặp Không Kiếp hãm"
                    # We can use get_star_brightness if definitions exist for KK, 
                    # but typically it's only 14 Main Stars in that table.
                    # Hard rule for KK Hãm: Tỵ, Hợi usually Đắc/Hãm specific.
                    # Implementation detail: Just apply flat penalty for now to be safe.
                    p_score = p_score * 0.7 
            
            # Normalize Palace Score to 0-100 range before weighting? 
            # Or just accumulate raw score?
            # User said: "Output: Điểm số trên thang 100".
            # If max raw score per palace (e.g. 2 miếu stars + hoa loc) ~= 250.
            # Let's cap at 100 for normalization.
            p_score = min(100, max(0, p_score))
            
            final_score += p_score * weight

        # Final Cap
        final_score = min(100, round(final_score, 1))
        
        # Archetype Determination
        archetype = "An Nhàn" # Default
        if final_score >= 80:
            if wealth_score >= power_score:
                archetype = "Số Tỷ Phú (Phú Cách)"
            else:
                archetype = "Số Quan Chức (Quý Cách)"
        elif final_score >= 60:
             if wealth_score > power_score:
                archetype = "Khá Giả"
             else:
                archetype = "Có Danh Vọng"
        
        # Badges
        rank_class = "C"
        if final_score >= 90: mr = "S"
        elif final_score >= 80: rank_class = "A"
        elif final_score >= 65: rank_class = "B"
            
        return {
            'score': final_score,
            'rank_class': rank_class,
            'archetype': archetype
        }

    def analyze_timeline(self, horoscope):
        """
        Golden Year Finder: Analyze fortune for ages 20-80.
        Find peaks based on Dai Van (10 years) and Luu Nien (1 year).
        """
        timeline = []
        start_year = horoscope.birth_date['year']
        
        # Determine Cuc (Element) -> Dai Van start age
        # Simplified: defaulting to 2, 3, 4, 5, 6 depending on element
        # We need the element number to calculate Dai Van accurately.
        # But 'horoscope' object doesn't have it explicitly stored yet (TODO).
        # We will estimate or default to standard Luu Thai Tue + Tieu Van scoring for now
        # as a robust fallback for "Fortune Trend".
        
        peak_score = -1
        peak_year = 0
        
        for age in range(20, 81):
            current_year = start_year + age
            
            # Simple Scoring Model for Timeline
            # 1. Luu Thai Tue position check
            year_chi_idx = (current_year - 4) % 12
            ltt_palace = horoscope.palaces_by_index.get(year_chi_idx)
            
            # Base score from the palace quality itself
            # If the palace itself is good (Miếu/Vượng stars) -> Good year background
            daily_bg_score = 50
            if ltt_palace:
                # Check stars in this palace
                from data.star_brightness import get_star_brightness
                for s in ltt_palace.stars:
                    if s.type == 1:
                        br = get_star_brightness(s.name, ltt_palace.position)
                        if br.get('code') in ['M', 'V']: daily_bg_score += 10
                        if br.get('code') == 'H': daily_bg_score -= 5
            
            y_score = daily_bg_score
            
            # 2. Modifiers
            highlight = ""
            if ltt_palace:
                good_stars = ["Hóa Lộc", "Hóa Quyền", "Hóa Khoa", "Lộc Tồn", "Thiên Mã", "Hồng Loan", "Thiên Hỹ"]
                bad_stars = ["Hóa Kỵ", "Thiên Không", "Địa Kiếp", "Địa Không", "Kinh Dương", "Đà La", "Thái Tuế"] 
                # Note: Thai Tue can be good/bad, usually stress.
                
                for s in good_stars:
                    if ltt_palace.has_star(s): 
                        y_score += 10
                        if not highlight: highlight = f"Gặp {s}"
                
                for s in bad_stars:
                    if ltt_palace.has_star(s): 
                        y_score -= 10
                        if not highlight: highlight = f"Gặp {s}"

            # Track Peak
            if y_score > peak_score:
                peak_score = y_score
                peak_year = current_year

            timeline.append({
                'year': current_year,
                'age': age,
                'score': y_score,
                'highlight': highlight
            })
            
        # Add peak annotation
        for t in timeline:
            if t['year'] == peak_year:
                t['is_peak'] = True
                t['highlight'] = f"ĐỈNH CAO: {t['highlight']}" if t['highlight'] else "Đỉnh Cao Sự Nghiệp"
                
        return timeline

