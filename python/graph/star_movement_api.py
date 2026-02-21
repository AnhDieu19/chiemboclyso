"""
Star Movement API - Calculate star positions across all 12 hours (Canh Gio)
Provides data for analyzing movement patterns of star circles (Vong Sao)
"""

from flask import request, jsonify
from . import graph_bp

# Import chart builder from parent package
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart import generate_birth_chart, generate_birth_chart_lunar
from core.fortune_periods import calculate_luu_nien, calculate_luu_nien_tu_hoa


CHI_NAMES = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

HOUR_RANGES = [
    (23, 1),   # Tý: 23h-01h
    (1, 3),    # Sửu: 01h-03h
    (3, 5),    # Dần: 03h-05h
    (5, 7),    # Mão: 05h-07h
    (7, 9),    # Thìn: 07h-09h
    (9, 11),   # Tỵ: 09h-11h
    (11, 13),  # Ngọ: 11h-13h
    (13, 15),  # Mùi: 13h-15h
    (15, 17),  # Thân: 15h-17h
    (17, 19),  # Dậu: 17h-19h
    (19, 21),  # Tuất: 19h-21h
    (21, 23),  # Hợi: 21h-23h
]


@graph_bp.route('/graph/api/star-movement', methods=['POST'])
def calculate_star_movement():
    """
    Calculate birth charts for all 12 hours (canh gio) to analyze star movement patterns
    
    Request body:
    {
        "day": 28,
        "month": 3,
        "year": 1994,
        "gender": "nam",
        "calendar": "solar",
        "leap_month": false
    }
    
    Returns:
    {
        "status": "success",
        "data": {
            "base_info": {
                "day": 28, "month": 3, "year": 1994,
                "gender": "nam", "calendar": "solar"
            },
            "charts": [
                {
                    "hour_index": 0,
                    "hour_name": "Tý (23-01h)",
                    "positions": {...},
                    "menh_position": 2,
                    "than_position": 8,
                    ...
                },
                ... (12 charts total)
            ],
            "movement_analysis": {
                "stars_that_move": [...],
                "stars_that_stay": [...],
                "movement_patterns": {...}
            }
        }
    }
    """
    try:
        # Handle JSON parsing with proper error handling
        try:
            data = request.json
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": "Invalid JSON or missing Content-Type: application/json"
            }), 415
        
        if not data:
            return jsonify({"status": "error", "message": "No data provided"}), 400
        
        # Validate required fields BEFORE parsing
        if not all([data.get('day'), data.get('month'), data.get('year')]):
            return jsonify({"status": "error", "message": "Missing day, month, or year"}), 400
        
        # Parse inputs with error handling
        try:
            day = int(data.get('day'))
            month = int(data.get('month'))
            year = int(data.get('year'))
        except (ValueError, TypeError) as e:
            return jsonify({"status": "error", "message": f"Invalid date format: {str(e)}"}), 400
        
        gender = data.get('gender', 'nam')
        calendar_type = data.get('calendar', 'solar')
        leap_month = data.get('leap_month', False)
        viewing_year = data.get('viewing_year', year)  # Default to birth year
        try:
            viewing_year = int(viewing_year)
        except (ValueError, TypeError):
            viewing_year = year
        
        # Calculate Lưu Niên stars (same for all 12 hours - depends only on viewing year)
        luu_nien_data = calculate_luu_nien(viewing_year)
        
        # Generate charts for all 12 hours
        charts = []
        for hour_index in range(12):
            try:
                if calendar_type == 'lunar':
                    chart = generate_birth_chart_lunar(day, month, year, hour_index, gender, leap_month)
                else:
                    chart = generate_birth_chart(day, month, year, hour_index, gender)
                
                start_hour, end_hour = HOUR_RANGES[hour_index]
                
                # Extract essential data
                chart_data = {
                    "hour_index": hour_index,
                    "hour_name": f"{CHI_NAMES[hour_index]} ({start_hour:02d}-{end_hour:02d}h)",
                    "positions": chart.get('positions', {}),
                    "menh_position": chart.get('menh_position'),
                    "than_position": chart.get('than_position'),
                    "menh_name": chart.get('menh_name'),
                    "than_name": chart.get('than_name'),
                    "cuc": chart.get('cuc'),
                    "nap_am": chart.get('nap_am'),
                    "cung_map": chart.get('cung_map'),
                }
                
                # Inject Lưu Niên stars into positions
                if luu_nien_data and luu_nien_data.get('stars'):
                    for star_name, pos in luu_nien_data['stars'].items():
                        # positions keys can be int or str depending on source
                        pos_key = pos if pos in chart_data['positions'] else str(pos)
                        if pos_key in chart_data['positions']:
                            if 'luu_nien' not in chart_data['positions'][pos_key]:
                                chart_data['positions'][pos_key]['luu_nien'] = []
                            chart_data['positions'][pos_key]['luu_nien'].append({
                                'name': star_name,
                                'display': 'L.' + star_name.replace('Lưu ', '')
                            })
                
                # Inject Lưu Niên Tứ Hóa
                all_stars = chart.get('all_stars', {})
                if all_stars:
                    luu_tu_hoa = calculate_luu_nien_tu_hoa(viewing_year, all_stars)
                    for hoa_name in ['Lưu Hóa Lộc', 'Lưu Hóa Quyền', 'Lưu Hóa Khoa', 'Lưu Hóa Kỵ']:
                        if hoa_name in luu_tu_hoa:
                            hoa_info = luu_tu_hoa[hoa_name]
                            hoa_pos = hoa_info['position']
                            pos_key = hoa_pos if hoa_pos in chart_data['positions'] else str(hoa_pos)
                            if pos_key in chart_data['positions']:
                                if 'luu_hoa' not in chart_data['positions'][pos_key]:
                                    chart_data['positions'][pos_key]['luu_hoa'] = []
                                chart_data['positions'][pos_key]['luu_hoa'].append({
                                    'name': hoa_name,
                                    'display': 'L.' + hoa_name.replace('Lưu ', ''),
                                    'star': hoa_info['star']
                                })
                
                charts.append(chart_data)
            except Exception as e:
                print(f"Error calculating chart for hour {hour_index}: {e}")
                charts.append({
                    "hour_index": hour_index,
                    "error": str(e)
                })
        
        # Analyze movement patterns
        movement_analysis = analyze_star_movements(charts)
        
        return jsonify({
            "status": "success",
            "data": {
                "base_info": {
                    "day": day,
                    "month": month,
                    "year": year,
                    "gender": gender,
                    "calendar": calendar_type,
                    "leap_month": leap_month,
                    "viewing_year": viewing_year
                },
                "luu_nien_info": {
                    "year": luu_nien_data.get('year'),
                    "chi_name": luu_nien_data.get('chi_name'),
                    "total_stars": len(luu_nien_data.get('stars', {}))
                },
                "charts": charts,
                "movement_analysis": movement_analysis
            }
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


def analyze_star_movements(charts):
    """
    Analyze which stars move and which stay fixed across 12 hours
    
    Returns:
    {
        "stars_that_move": [...],
        "stars_that_stay": [...],
        "movement_patterns": {
            "Menh Cung": {"type": "fixed", "positions": [...]},
            "Than Cung": {"type": "moves", "positions": [...], "pattern": "shifts_by_1"},
            ...
        }
    }
    """
    if not charts or len(charts) < 2:
        return {}
    
    # Get all unique stars across all charts
    # Note: Chart structure uses 'stars' array, not separate 'chinh_tinh', 'luc_cat', 'luc_sat'
    all_stars = set()
    for chart in charts:
        if 'positions' in chart:
            for pos_idx, pos_data in chart['positions'].items():
                # Use 'stars' array which contains all stars at this position
                if 'stars' in pos_data:
                    for star in pos_data['stars']:
                        # Handle both dict format {'name': '...'} and string format
                        star_name = star['name'] if isinstance(star, dict) else star
                        all_stars.add(star_name)
    
    # Track positions of each star across 12 hours
    star_positions = {star: [] for star in all_stars}
    
    for chart in charts:
        if 'positions' not in chart:
            continue
        
        # Reset for this hour
        hour_star_positions = {star: None for star in all_stars}
        
        # Find where each star is in this chart
        for pos_idx, pos_data in chart['positions'].items():
            pos_num = int(pos_idx)
            
            # Use 'stars' array which contains all stars at this position
            if 'stars' in pos_data:
                for star in pos_data['stars']:
                    # Handle both dict format {'name': '...'} and string format
                    star_name = star['name'] if isinstance(star, dict) else star
                    if star_name in hour_star_positions:
                        hour_star_positions[star_name] = pos_num
        
        # Append to tracking
        for star, pos in hour_star_positions.items():
            star_positions[star].append(pos)
    
    # Analyze patterns
    movement_patterns = {}
    stars_that_move = []
    stars_that_stay = []
    
    for star, positions in star_positions.items():
        # Remove None values
        valid_positions = [p for p in positions if p is not None]
        
        if not valid_positions:
            continue
        
        # Check if star stays in same position
        unique_positions = set(valid_positions)
        
        if len(unique_positions) == 1:
            # Star doesn't move
            stars_that_stay.append(star)
            movement_patterns[star] = {
                "type": "fixed",
                "position": valid_positions[0]
            }
        else:
            # Star moves
            stars_that_move.append(star)
            
            # Detect pattern (sequential shift, jump pattern, etc)
            pattern_type = detect_movement_pattern(valid_positions)
            
            movement_patterns[star] = {
                "type": "moves",
                "positions": valid_positions,
                "unique_positions": list(unique_positions),
                "pattern": pattern_type
            }
    
    # Also track Menh Cung and Than Cung positions
    menh_positions = [c.get('menh_position') for c in charts if 'menh_position' in c]
    than_positions = [c.get('than_position') for c in charts if 'than_position' in c]
    
    # Sort for consistent display
    stars_that_move.sort()
    stars_that_stay.sort()
    
    return {
        "stars_that_move": stars_that_move,
        "stars_that_stay": stars_that_stay,
        "movement_patterns": movement_patterns,
        "menh_cung_positions": menh_positions,
        "than_cung_positions": than_positions,
        "total_stars_analyzed": len(all_stars)
    }


def detect_movement_pattern(positions):
    """
    Detect the type of movement pattern
    - "sequential": moves 1 position each hour
    - "skip_1": skips 1 position each hour (moves by 2)
    - "alternating": alternates between positions
    - "irregular": no clear pattern
    """
    if len(positions) < 3:
        return "insufficient_data"
    
    # Calculate differences between consecutive positions
    diffs = []
    for i in range(1, len(positions)):
        diff = (positions[i] - positions[i-1]) % 12
        diffs.append(diff)
    
    # Check if all differences are the same
    if len(set(diffs)) == 1:
        diff_value = diffs[0]
        if diff_value == 1:
            return "sequential_forward"
        elif diff_value == 11:
            return "sequential_backward"
        elif diff_value == 2:
            return "skip_1_forward"
        elif diff_value == 10:
            return "skip_1_backward"
        else:
            return f"regular_shift_by_{diff_value}"
    
    # Check for alternating pattern
    if len(set(diffs)) == 2:
        return "alternating"
    
    return "irregular"
