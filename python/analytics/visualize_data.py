"""
Visualize Beauty Data
Generates an interactive HTML dashboard using Chart.js.
Hỗ trợ đọc từ CSV hoặc JSON meta file.
"""
import csv
import json
import os
import sys


def get_visualization_data_from_json(meta: dict, gender_filter=None) -> dict:
    """
    Tạo dữ liệu visualization từ JSON meta file khi không có CSV.
    Chỉ hiển thị thống kê tổng quan theo năm.
    """
    if not meta or "scan_meta" not in meta:
        return None
    
    scan_meta = meta["scan_meta"]
    total_scanned = meta.get("total_scanned", 0)
    total_beauty = meta.get("total_beauty", 0)
    
    if gender_filter in ['nam', 'nu']:
        total_scanned = total_scanned // 2
        total_beauty = total_beauty // 2
    
    # Tạo dữ liệu line chart từ scan_meta
    years_sorted = sorted([int(y) for y in scan_meta.keys()])
    
    line_beauty_rate = []
    line_beauty_count = []
    
    for y in years_sorted:
        y_str = str(y)
        if y_str in scan_meta:
            m = scan_meta[y_str]
            total = m['total']
            beauty = m['beauty']
            if gender_filter in ['nam', 'nu']:
                total = total // 2
                beauty = beauty // 2
            rate = (beauty / total) * 100 if total > 0 else 0
            line_beauty_rate.append(round(rate, 2))
            line_beauty_count.append(beauty)
        else:
            line_beauty_rate.append(0)
            line_beauty_count.append(0)
    
    # Tạo fake pie data (không có chi tiết fate level từ JSON)
    # 5 Cấp Độ Hồng Nhan (BA Spec)
    fate_labels = {
        "VERY_HAPPY": "Hồng Nhan Phú Quý",
        "HAPPY": "Hồng Nhan Hạnh Phúc",
        "NEUTRAL": "Hồng Nhan Bình Thường",
        "TRAGIC": "Hồng Nhan Vất Vả",
        "VERY_TRAGIC": "Hồng Nhan Bạc Mệnh"
    }
    
    # Ước tính phân bố (từ JSON không có chi tiết, dùng tỷ lệ trung bình)
    # Đây chỉ là placeholder - dữ liệu thực cần từ CSV
    pie_data = [0, 0, total_beauty, 0, 0]  # Tất cả vào NEUTRAL vì không có chi tiết
    
    set_names = {
        "DAO_HONG": "Đào Hồng Hỷ",
        "VAN_TINH": "Văn Xương/Khúc",
        "QUYEN_RU": "Tham/Liêm",
        "PHUC_THIEN": "Phủ/Tướng/Âm"
    }
    beauty_sets = list(set_names.values())
    
    # Bar datasets placeholder
    bar_datasets = [
        {"label": fate_labels["NEUTRAL"], "data": [0, 0, 0, 0], "backgroundColor": "#ffeb3b"}
    ]
    
    return {
        "count": total_beauty,
        "total_scanned": total_scanned,
        "fate_labels": list(fate_labels.values()),
        "beauty_sets": beauty_sets,
        "pie_data": pie_data,
        "bar_datasets": bar_datasets,
        "line_labels": years_sorted,
        "line_lucky": [0] * len(years_sorted),  # Không có chi tiết từ JSON
        "line_tragic": [0] * len(years_sorted),
        "line_beauty_rate": line_beauty_rate,
        "line_beauty_count": line_beauty_count,
        "data_source": "json_meta",
        "note": "Dữ liệu từ JSON meta - chỉ có thống kê tổng quan, không có chi tiết fate level"
    }



def get_visualization_data(filename="beauty_stats_full.csv", gender_filter=None):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, filename)
    meta_path = os.path.join(base_dir, filename.replace(".csv", "_meta.json"))
    
    # Auto-fallback to sample CSV if full CSV doesn't exist
    if not os.path.exists(filepath) and filename == "beauty_stats_full.csv":
        sample_file = os.path.join(base_dir, "beauty_stats_sample.csv")
        if os.path.exists(sample_file):
            # Use sample CSV for testing
            filepath = sample_file
            meta_path = os.path.join(base_dir, "beauty_stats_sample_meta.json")
    
    # Load Metadata (Total Scanned info)
    meta = {}
    if os.path.exists(meta_path):
        with open(meta_path, 'r', encoding='utf-8') as f:
            meta = json.load(f)
    
    # Nếu không có CSV nhưng có JSON meta, trả về dữ liệu từ JSON
    if not os.path.exists(filepath):
        if meta:
            return get_visualization_data_from_json(meta, gender_filter)
        return None

    # Data Structures for Charts
    fate_levels = ["VERY_HAPPY", "HAPPY", "NEUTRAL", "TRAGIC", "VERY_TRAGIC"]
    beauty_sets = ["DAO_HONG", "VAN_TINH", "QUYEN_RU", "PHUC_THIEN"]
    
    # 1. Pie Chart Data (Global)
    global_dist = {fl: 0 for fl in fate_levels}
    
    # 2. Bar Chart Data (Sets)
    sets_dist = {bs: {fl: 0 for fl in fate_levels} for bs in beauty_sets}
    
    # 3. Line Chart Data (Years) - Sướng/Khổ Ratios
    years_data = {} 

    count = 0
    # Adjust total scanned based on filter?
    current_total_scanned = meta.get("total_scanned", 0)
    if gender_filter in ['nam', 'nu']:
        current_total_scanned = current_total_scanned / 2

    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # FILTER LOGIC
            row_gender = row.get('Gender', 'nu') # Default to nu for old data compatibility
            if gender_filter and gender_filter != 'all' and row_gender != gender_filter:
                continue

            count += 1
            d_cls = row['Detailed_Class']
            year = int(row['Year'])
            
            # Global
            if d_cls in global_dist:
                global_dist[d_cls] += 1
            
            # Sets
            sets_str = row['Beauty_Sets']
            if sets_str:
                for s in sets_str.split(';'):
                    if s in sets_dist:
                        sets_dist[s][d_cls] += 1
            
            # Years
            if year not in years_data:
                years_data[year] = {'count': 0, 'lucky': 0, 'tragic': 0}
            years_data[year]['count'] += 1
            
            if d_cls in ["VERY_HAPPY", "HAPPY"]:
                years_data[year]['lucky'] += 1
            elif d_cls in ["VERY_TRAGIC", "TRAGIC"]:
                years_data[year]['tragic'] += 1

    # Prepare JSON for JS
    years_sorted = sorted(years_data.keys())
    
    # Line 1: Happiness Rate (Lucky vs Tragic within Beauty population)
    line_labels = years_sorted
    line_lucky_data = [round(years_data[y]['lucky']/years_data[y]['count']*100, 1) if years_data[y]['count'] > 0 else 0 for y in years_sorted]
    line_tragic_data = [round(years_data[y]['tragic']/years_data[y]['count']*100, 1) if years_data[y]['count'] > 0 else 0 for y in years_sorted]

    # Line 2: Beauty Distribution Rate (Meta: Beauty / Total Scanned)
    line_beauty_rate = []
    line_beauty_count = []  # Count of beauty found per year
    if "scan_meta" in meta:
        for y in years_sorted:
            y_str = str(y)
            if y_str in meta["scan_meta"]:
                m = meta["scan_meta"][y_str]
                rate = (m['beauty'] / m['total']) * 100 if m['total'] > 0 else 0
                line_beauty_rate.append(round(rate, 2))
                beauty_count = m['beauty']
                if gender_filter in ['nam', 'nu']:
                    beauty_count = beauty_count // 2
                line_beauty_count.append(beauty_count)
            else:
                line_beauty_rate.append(0)
                line_beauty_count.append(years_data[y]['count'] if y in years_data else 0)
    else:
        # Fallback: use years_data count
        line_beauty_count = [years_data[y]['count'] if y in years_data else 0 for y in years_sorted]

    pie_data = [global_dist[fl] for fl in fate_levels]
    
    # Stacked Bar Data
    bar_datasets = []
    colors = {
        "VERY_HAPPY": "#4caf50", # Green
        "HAPPY": "#8bc34a",      # Light Green
        "NEUTRAL": "#ffeb3b",    # Yellow
        "TRAGIC": "#ff9800",     # Orange
        "VERY_TRAGIC": "#f44336" # Red
    }
    
    # Translation keys for sets
    set_names = {
        "DAO_HONG": "Đào Hồng Hỷ",
        "VAN_TINH": "Văn Xương/Khúc",
        "QUYEN_RU": "Tham/Liêm",
        "PHUC_THIEN": "Phủ/Tướng/Âm"
    }
    beauty_set_labels = [set_names.get(bs, bs) for bs in beauty_sets]
    
    # Translation map for Fate Levels - 5 Cấp Độ Hồng Nhan (BA Spec)
    fate_labels = {
        "VERY_HAPPY": "Hồng Nhan Phú Quý",
        "HAPPY": "Hồng Nhan Hạnh Phúc",
        "NEUTRAL": "Hồng Nhan Bình Thường",
        "TRAGIC": "Hồng Nhan Vất Vả",
        "VERY_TRAGIC": "Hồng Nhan Bạc Mệnh"
    }
    
    for fl in fate_levels:
        data = [sets_dist[bs][fl] for bs in beauty_sets]
        bar_datasets.append({
            "label": fate_labels[fl],
            "data": data,
            "backgroundColor": colors[fl]
        })
        
    return {
        "count": count,
        "total_scanned": current_total_scanned,
        "fate_labels": [fate_labels[fl] for fl in fate_levels],
        "beauty_sets": beauty_set_labels,
        "pie_data": pie_data,
        "bar_datasets": bar_datasets,
        "line_labels": line_labels,
        "line_lucky": line_lucky_data,
        "line_tragic": line_tragic_data,
        "line_beauty_rate": line_beauty_rate,
        "line_beauty_count": line_beauty_count,
        "data_source": "csv"  # Mark as CSV data source
    }


def get_drilldown_data(year=None, month=None, gender_filter='all', filename="beauty_stats_full.csv"):
    """
    Fetch data for drill-down charts.
    - No args: Returns stats by Year (1950-2007)
    - Year: Returns stats by Month (1-12) for that Year
    - Year + Month: Returns stats by Day (1-31) for that Month
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, filename)
    
    if not os.path.exists(filepath):
        return {}

    # Result structure: { label: { lucky: 0, tragic: 0, total: 0 } }
    results = {}
    
    # Determine level
    level = 'year' # Default
    if year is not None:
        level = 'month'
    if year is not None and month is not None:
        level = 'day'

    with open(filepath, mode='r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 1. Filter Check
            r_year = int(row['Year'])
            r_month = int(row['Month'])
            r_day = int(row['Day'])
            r_gender = row.get('Gender', 'nu')

            if gender_filter and gender_filter != 'all' and r_gender != gender_filter:
                continue
            
            if year is not None and r_year != int(year):
                continue
            if month is not None and r_month != int(month):
                continue

            # 2. Key Determination
            key = r_year
            if level == 'month':
                key = r_month
            elif level == 'day':
                key = r_day
            
            if key not in results:
                results[key] = {'lucky': 0, 'tragic': 0, 'total': 0}

            # 3. Aggregation
            d_cls = row['Detailed_Class']
            results[key]['total'] += 1
            
            if d_cls in ["VERY_HAPPY", "HAPPY"]:
                results[key]['lucky'] += 1
            elif d_cls in ["VERY_TRAGIC", "TRAGIC"]:
                results[key]['tragic'] += 1

    # Format for Chart.js
    sorted_keys = sorted(results.keys())
    
    labels = sorted_keys
    lucky_data = []
    tragic_data = []
    
    for k in sorted_keys:
        total = results[k]['total']
        if total > 0:
            lucky_data.append(round(results[k]['lucky'] / total * 100, 1))
            tragic_data.append(round(results[k]['tragic'] / total * 100, 1))
        else:
            lucky_data.append(0)
            tragic_data.append(0)
            
    return {
        "level": level,
        "labels": labels,
        "lucky": lucky_data,
        "tragic": tragic_data,
        "meta": {"year": year, "month": month}
    }


def generate_report(filename="beauty_stats_1950_2007.csv", output_file="beauty_report.html"):
    data = get_visualization_data(filename)
    if not data: return

    out_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), output_file)

    # HTML Template
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Báo Cáo Thống Kê Hồng Nhan (1950-2007)</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: 'Segoe UI', sans-serif; background: #f4f6f9; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); margin-bottom: 20px; }}
        h1, h2 {{ color: #333; }}
        .row {{ display: flex; gap: 20px; flex-wrap: wrap; }}
        .col {{ flex: 1; min-width: 300px; }}
        .stat-box {{ text-align: center; padding: 15px; border-radius: 5px; color: white; }}
        .bg-primary {{ background: #2196F3; }}
        .bg-success {{ background: #4CAF50; }}
        .bg-danger {{ background: #F44336; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Báo Cáo Phân Tích "Hồng Nhan" (1950 - 2007)</h1>
        <p>Tổng mẫu phân tích: <b>{data['count']}</b> lá số có nhan sắc.</p>
        
        <div class="row">
            <div class="col card">
                <h2>1. Phân Bố Sướng/Khổ (Toàn bộ)</h2>
                <canvas id="pieChart"></canvas>
            </div>
            <div class="col card">
                <h2>2. Tương Quan Theo Bộ Sao</h2>
                <canvas id="barChart"></canvas>
            </div>
        </div>

        <div class="card">
            <h2>3. Xu Hướng Theo Thời Gian (1950 - 2007)</h2>
            <p>So sánh tỷ lệ % Sướng (Xanh) vs Khổ (Đỏ) qua các năm.</p>
            <canvas id="lineChart" height="100"></canvas>
        </div>
    </div>

    <script>
        // Pie Chart
        const ctxPie = document.getElementById('pieChart').getContext('2d');
        new Chart(ctxPie, {{
            type: 'doughnut',
            data: {{
                labels: {json.dumps(data['fate_labels'])},
                datasets: [{{
                    data: {json.dumps(data['pie_data'])},
                    backgroundColor: ['#4caf50', '#8bc34a', '#ffeb3b', '#ff9800', '#f44336']
                }}]
            }}
        }});

        // Stacked Bar Chart
        const ctxBar = document.getElementById('barChart').getContext('2d');
        new Chart(ctxBar, {{
            type: 'bar',
            data: {{
                labels: {json.dumps(data['beauty_sets'])},
                datasets: {json.dumps(data['bar_datasets'])}
            }},
            options: {{
                scales: {{ x: {{ stacked: true }}, y: {{ stacked: true }} }}
            }}
        }});

        // Line Chart
        const ctxLine = document.getElementById('lineChart').getContext('2d');
        new Chart(ctxLine, {{
            type: 'line',
            data: {{
                labels: {json.dumps(data['line_labels'])},
                datasets: [
                    {{
                        label: 'Tỷ lệ Sướng (%)',
                        data: {json.dumps(data['line_lucky'])},
                        borderColor: '#4caf50',
                        tension: 0.3
                    }},
                    {{
                        label: 'Tỷ lệ Khổ (%)',
                        data: {json.dumps(data['line_tragic'])},
                        borderColor: '#f44336',
                        tension: 0.3
                    }}
                ]
            }}
        }});
    </script>
</body>
</html>
    """
    
    with open(out_path, "w", encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Report generated: {os.path.abspath(out_path)}")

if __name__ == "__main__":
    generate_report()
