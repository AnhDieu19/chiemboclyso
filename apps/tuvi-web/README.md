# Tu Vi Web - Main Web Application

Ứng dụng web chính của hệ thống Tử Vi.

## Nguồn gốc
- Templates: `frontend/templates/`
- Static files: `frontend/static/`
- Served qua: API Gateway (port 5001) hoặc các service riêng

## Trang chính
- `index.html` - Trang chủ, lập lá số Tử Vi
- `finder.html` - Tra cứu ngược (reverse lookup)
- `analytics_beauty.html` - Phân tích tài mệnh
- `graph.html` - Đồ thị sao

## Cấu trúc
```
templates/
├── index.html              # Trang chủ
├── finder.html             # Tra cứu ngược
├── analytics_beauty.html   # Phân tích tài mệnh
├── graph.html              # Đồ thị
├── pages/                  # Sub-pages
├── components/             # Reusable components
└── reverse_lookup_snippet.html

static/
├── css/                    # Stylesheets
├── js/                     # JavaScript
├── assets/                 # Fonts, icons
└── images/                 # Images
```

## Chạy
```bash
# Qua monolith gateway
python run_monolith.py

# Hoặc microservice mode  
python run_all.py
```

Truy cập: http://localhost:5001
