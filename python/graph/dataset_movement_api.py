"""
Dataset Star Movement Analysis API
Analyze star movement patterns across the entire dataset (tuvi_data_1960_2005.jsonl)
"""

from flask import request, jsonify
from . import graph_bp
import json
import os
from collections import defaultdict, Counter

CHI_NAMES = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']


@graph_bp.route('/graph/api/dataset-movement', methods=['POST'])
def analyze_dataset_movement():
    """
    Analyze star movement patterns across entire dataset
    
    Request body:
    {
        "sample_size": 1000,  // Optional, default all records
        "year_range": [1960, 2005],  // Optional filter
        "gender": "nam"  // Optional filter: "nam", "nu", or null for both
    }
    
    Returns:
    {
        "status": "success",
        "data": {
            "total_records_analyzed": 8785,
            "star_movement_patterns": {
                "Tử Vi": {
                    "movement_type": "fixed",
                    "positions": [0, 0, 0, ...],  // 12 positions for 12 hours
                    "unique_positions": 1,
                    "pattern_description": "Cố định tại vị trí 1"
                },
                ...
            },
            "movement_statistics": {
                "total_unique_stars": 45,
                "always_fixed_stars": ["Tử Vi", "Thiên Phủ", ...],
                "always_moving_stars": ["Lộc Tồn", ...],
                "pattern_distribution": {
                    "fixed": 15,
                    "sequential_forward": 8,
                    "skip_pattern": 3,
                    ...
                }
            }
        }
    }
    """
    try:
        data = request.json or {}
        sample_size = data.get('sample_size', None)
        year_range = data.get('year_range', None)
        gender_filter = data.get('gender', None)
        
        # Load dataset - Using full dataset with 490,896 records (1950-2005)
        dataset_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'analytics',
            'tai_menh_full_1950_2005.jsonl'
        )
        
        if not os.path.exists(dataset_path):
            return jsonify({
                "status": "error",
                "message": f"Dataset not found: {dataset_path}"
            }), 404
        
        # Analyze dataset
        result = analyze_star_patterns_from_file(
            dataset_path,
            sample_size=sample_size,
            year_range=year_range,
            gender_filter=gender_filter
        )
        
        return jsonify({
            "status": "success",
            "data": result
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


def analyze_star_patterns_from_file(file_path, sample_size=None, year_range=None, gender_filter=None):
    """
    Analyze star movement patterns from JSONL file
    """
    # Track star positions across all records
    # Structure: {star_name: {hour_id: [list of positions]}}
    star_positions_by_hour = defaultdict(lambda: defaultdict(list))
    
    # Track which palace each star appears in
    star_palace_appearances = defaultdict(lambda: defaultdict(int))
    
    records_processed = 0
    records_filtered = 0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f):
            if sample_size and records_processed >= sample_size:
                break
            
            try:
                record = json.loads(line)
                
                # New format: year, month, day, hour_chi, gender at root level
                year = record.get('year', 0)
                gender = record.get('gender', '')
                hour_chi = record.get('hour_chi', '')
                
                # Map hour_chi to hour_id (0-11)
                try:
                    hour_id = CHI_NAMES.index(hour_chi)
                except ValueError:
                    hour_id = 0
                
                # Apply filters
                if year_range and not (year_range[0] <= year <= year_range[1]):
                    continue
                
                if gender_filter and gender != gender_filter:
                    continue
                
                records_filtered += 1
                
                palaces = record.get('palaces', {})
                
                # Map palace names to positions (Địa Chi)
                # Need to find Mệnh palace position first
                menh_position = None
                for palace_name, palace_data in palaces.items():
                    if palace_name == 'Mệnh':
                        # In new format, we need to calculate position
                        # For now, use palace index as position
                        palace_names = ['Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 
                                       'Quan Lộc', 'Nô Bộc', 'Thiên Di', 'Tật Ách', 
                                       'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ']
                        try:
                            menh_position = palace_names.index('Mệnh')
                        except:
                            menh_position = 0
                        break
                
                if menh_position is None:
                    continue
                
                # Extract star positions for this record  
                palace_names = ['Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 
                               'Quan Lộc', 'Nô Bộc', 'Thiên Di', 'Tật Ách', 
                               'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ']
                
                for palace_name, palace_data in palaces.items():
                    try:
                        position = palace_names.index(palace_name)
                    except ValueError:
                        continue
                    
                    # New format: chinh, phu_tot, phu_xau, tu_hoa
                    all_stars = []
                    
                    # Chính tinh
                    if 'chinh' in palace_data and isinstance(palace_data['chinh'], list):
                        all_stars.extend(palace_data['chinh'])
                    
                    # Phụ tinh tốt
                    if 'phu_tot' in palace_data and isinstance(palace_data['phu_tot'], list):
                        all_stars.extend(palace_data['phu_tot'])
                    
                    # Phụ tinh xấu
                    if 'phu_xau' in palace_data and isinstance(palace_data['phu_xau'], list):
                        all_stars.extend(palace_data['phu_xau'])
                    
                    # Tứ hóa
                    if 'tu_hoa' in palace_data and isinstance(palace_data['tu_hoa'], list):
                        for hoa_info in palace_data['tu_hoa']:
                            if isinstance(hoa_info, dict):
                                hoa_name = hoa_info.get('hoa', '')
                                star_name = hoa_info.get('star', '')
                                if hoa_name:
                                    all_stars.append(hoa_name)
                    
                    # Track positions
                    for star_name in all_stars:
                        if star_name and isinstance(star_name, str):
                            star_positions_by_hour[star_name][hour_id].append(position)
                            star_palace_appearances[star_name][palace_name] += 1
                
                records_processed += 1
                
            except json.JSONDecodeError:
                print(f"Error parsing line {line_num + 1}")
                continue
            except Exception as e:
                print(f"Error processing record {line_num + 1}: {e}")
                import traceback
                traceback.print_exc()
                continue
    
    # Analyze patterns for each star
    star_movement_patterns = {}
    
    for star_name, hour_positions in star_positions_by_hour.items():
        # Get most common position for each hour
        positions_by_hour = []
        for hour_id in range(12):
            if hour_id in hour_positions:
                pos_list = hour_positions[hour_id]
                if pos_list:
                    # Use most common position
                    most_common_pos = Counter(pos_list).most_common(1)[0][0]
                    positions_by_hour.append(most_common_pos)
                else:
                    positions_by_hour.append(None)
            else:
                positions_by_hour.append(None)
        
        # Remove None values for analysis
        valid_positions = [p for p in positions_by_hour if p is not None]
        
        if not valid_positions:
            continue
        
        unique_positions = list(set(valid_positions))
        
        # Determine movement type
        if len(unique_positions) == 1:
            movement_type = "fixed"
            pattern_desc = f"Cố định tại vị trí {unique_positions[0]} ({CHI_NAMES[unique_positions[0]]})"
        else:
            # Detect movement pattern
            pattern_type = detect_movement_pattern(valid_positions)
            movement_type = "moving"
            pattern_desc = describe_pattern(pattern_type, unique_positions)
        
        star_movement_patterns[star_name] = {
            "movement_type": movement_type,
            "positions": positions_by_hour,
            "unique_positions": len(unique_positions),
            "unique_position_list": unique_positions,
            "pattern_description": pattern_desc,
            "total_appearances": sum(len(pos_list) for pos_list in hour_positions.values()),
            "most_common_palace": max(star_palace_appearances[star_name].items(), key=lambda x: x[1])[0] if star_palace_appearances[star_name] else None
        }
    
    # Calculate statistics
    always_fixed_stars = [star for star, info in star_movement_patterns.items() if info['movement_type'] == 'fixed']
    always_moving_stars = [star for star, info in star_movement_patterns.items() if info['movement_type'] == 'moving']
    
    pattern_distribution = defaultdict(int)
    for star_info in star_movement_patterns.values():
        pattern_distribution[star_info['movement_type']] += 1
    
    return {
        "total_records_analyzed": records_processed,
        "records_after_filter": records_filtered,
        "star_movement_patterns": star_movement_patterns,
        "movement_statistics": {
            "total_unique_stars": len(star_movement_patterns),
            "always_fixed_stars": always_fixed_stars,
            "always_moving_stars": always_moving_stars,
            "fixed_star_count": len(always_fixed_stars),
            "moving_star_count": len(always_moving_stars),
            "pattern_distribution": dict(pattern_distribution)
        }
    }


def detect_movement_pattern(positions):
    """Detect movement pattern from position sequence"""
    if len(positions) < 3:
        return "insufficient_data"
    
    # Calculate differences
    diffs = []
    for i in range(1, len(positions)):
        diff = (positions[i] - positions[i-1]) % 12
        diffs.append(diff)
    
    # Check for consistent pattern
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
    
    return "irregular"


def describe_pattern(pattern_type, positions):
    """Create human-readable pattern description"""
    pos_names = [CHI_NAMES[p] for p in positions]
    
    if pattern_type == "sequential_forward":
        return f"Di chuyển tuần tự thuận ({', '.join(pos_names[:3])}...)"
    elif pattern_type == "sequential_backward":
        return f"Di chuyển tuần tự nghịch ({', '.join(pos_names[:3])}...)"
    elif pattern_type == "skip_1_forward":
        return f"Nhảy cách 1 vị trí thuận ({', '.join(pos_names[:3])}...)"
    elif pattern_type == "skip_1_backward":
        return f"Nhảy cách 1 vị trí nghịch ({', '.join(pos_names[:3])}...)"
    elif pattern_type.startswith("regular_shift"):
        return f"Di chuyển đều đặn ({', '.join(pos_names[:3])}...)"
    else:
        return f"Di chuyển không đều ({len(positions)} vị trí khác nhau)"
