"""
Graph API - Chart Calculation Endpoint
Provides API for calculating birth chart data for the Knowledge Graph
"""

from flask import request, jsonify
from . import graph_bp

# Import chart builder from parent package
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart import generate_birth_chart, generate_birth_chart_lunar


def solar_hour_to_chi_index(h):
    """Convert solar hour (0-23) to Chi Index (0-11, Ty=0)"""
    return ((h + 1) // 2) % 12


@graph_bp.route('/graph/api/chart', methods=['POST'])
def calculate_chart():
    """
    Calculate birth chart and return positions for 12 Cung visualization
    
    Request body:
    {
        "day": 28,
        "month": 3,
        "year": 1994,
        "hour": 6,        // Chi index (0-11) or solar hour (0-23)
        "gender": "nam",  // "nam" or "nu"
        "calendar": "solar",  // "solar" or "lunar"
        "leap_month": false   // Only for lunar calendar
    }
    
    Returns:
    {
        "status": "success",
        "data": {
            "positions": { 0: {...}, 1: {...}, ... 11: {...} },
            "menh_position": 2,
            "than_position": 8,
            "cuc": {"name": "Thuy Nhi Cuc", "number": 2},
            "nap_am": {...},
            ...
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
        
        hour = data.get('hour')  # Can be chi index (0-11) or None
        gender = data.get('gender', 'nam')
        calendar_type = data.get('calendar', 'solar')
        leap_month = data.get('leap_month', False)
        
        # Convert hour if provided
        hour_index = None
        if hour is not None:
            hour_val = int(hour)
            # If hour > 11, assume it's solar hour (0-23), convert to chi index
            if hour_val > 11:
                hour_index = solar_hour_to_chi_index(hour_val)
            else:
                hour_index = hour_val
        else:
            # Default to Ty (0) if no hour provided
            hour_index = 0
        
        # Generate chart based on calendar type
        if calendar_type == 'lunar':
            chart = generate_birth_chart_lunar(day, month, year, hour_index, gender, leap_month)
        else:
            chart = generate_birth_chart(day, month, year, hour_index, gender)
        
        # Extract relevant data for graph visualization
        response_data = {
            "positions": chart.get('positions', {}),
            "menh_position": chart.get('menh_position'),
            "than_position": chart.get('than_position'),
            "menh_name": chart.get('menh_name'),
            "than_name": chart.get('than_name'),
            "cuc": chart.get('cuc'),
            "nap_am": chart.get('nap_am'),
            "cung_map": chart.get('cung_map'),
            "year_can_chi": chart.get('year_can_chi'),
            "lunar_date": chart.get('lunar_date'),
            "tu_hoa": chart.get('tu_hoa'),
            "tuan_triet": chart.get('tuan_triet')
        }
        
        return jsonify({
            "status": "success",
            "data": response_data
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
