import requests
import json

url = 'http://localhost:5000/graph/api/dataset-movement'
payload = {
    'sample_size': 100,
    'year_range': [1950, 1951],
    'gender': 'nam'
}

print("Testing API endpoint...")
print(f"URL: {url}")
print(f"Payload: {json.dumps(payload, indent=2)}")
print("\n" + "="*60)

try:
    response = requests.post(url, json=payload, timeout=30)
    result = response.json()
    
    print(f"Status Code: {response.status_code}")
    print(f"Result Status: {result.get('status')}")
    
    if result.get('status') == 'success':
        data = result.get('data', {})
        print(f"\nRecords analyzed: {data.get('total_records_analyzed', 0)}")
        
        stats = data.get('movement_statistics', {})
        print(f"\nMovement Statistics:")
        print(f"  Total unique stars: {stats.get('total_unique_stars', 0)}")
        print(f"  Fixed stars: {stats.get('fixed_star_count', 0)}")
        print(f"  Moving stars: {stats.get('moving_star_count', 0)}")
        
        # Show sample star patterns
        patterns = data.get('star_movement_patterns', {})
        print(f"\nSample star patterns (first 5):")
        for i, (star_name, info) in enumerate(list(patterns.items())[:5]):
            print(f"  {i+1}. {star_name}: {info.get('movement_type')} - {info.get('pattern_description')}")
    else:
        print(f"Error: {result.get('message')}")
        
except Exception as e:
    print(f"Exception: {e}")
