# Microservices Architecture - Tu Vi Platform

## Tổng quan kiến trúc

```
tuvi-app/
├── services/                         # Tất cả microservices
│   ├── shared/                       # Shared library (core, data, stars, chart, interpretation)
│   │   ├── core/                     # → python/core/
│   │   ├── data/                     # → python/data/
│   │   ├── stars/                    # → python/stars/
│   │   ├── chart/                    # → python/chart/
│   │   └── interpretation/           # → python/interpretation/
│   │
│   ├── gateway/                      # API Gateway - Entry point duy nhất
│   │   ├── app.py                    # Flask app + reverse proxy
│   │   ├── config.py                 # Service registry
│   │   └── requirements.txt
│   │
│   ├── tuvi-chart/                   # Service: Tử Vi lá số
│   │   ├── app.py                    # Standalone Flask app (port 5011)
│   │   ├── routes.py                 # API endpoints
│   │   ├── use_cases.py              # Business logic
│   │   └── requirements.txt
│   │
│   ├── tuvi-finder/                  # Service: Reverse finder
│   │   ├── app.py                    # Standalone Flask app (port 5012)
│   │   ├── routes.py
│   │   └── requirements.txt
│   │
│   ├── tuvi-analytics/               # Service: Analytics / Tai Menh
│   │   ├── app.py                    # Standalone Flask app (port 5013)
│   │   ├── routes.py
│   │   └── requirements.txt
│   │
│   ├── tuvi-ai/                      # Service: AI Gemini integration
│   │   ├── app.py                    # Standalone Flask app (port 5014)
│   │   ├── routes.py
│   │   └── requirements.txt
│   │
│   ├── thai-at/                      # Service: Thái Ất Thần Số
│   │   ├── app.py                    # Standalone Flask app (port 5015)
│   │   ├── routes.py
│   │   └── requirements.txt
│   │
│   ├── ki-mon/                       # Service: Kì Môn Độn Giáp
│   │   ├── app.py                    # Standalone Flask app (port 5016)
│   │   ├── routes.py
│   │   └── requirements.txt
│   │
│   ├── graph/                        # Service: Knowledge Graph
│   │   ├── app.py                    # Standalone Flask app (port 5017)
│   │   ├── routes.py
│   │   ├── templates/                # Own templates
│   │   ├── static/                   # Own static files
│   │   └── requirements.txt
│   │
│   └── vi-dieu-phap/                 # Service: Vi Diệu Pháp (self-contained)
│       ├── app.py                    # Standalone Flask app (port 5018)
│       ├── domain/
│       ├── application/
│       ├── infrastructure/
│       ├── presentation/
│       ├── data/
│       └── requirements.txt
│
├── apps/                             # Frontend applications
│   ├── tuvi-web/                     # Main Tu Vi web frontend
│   │   ├── templates/
│   │   └── static/
│   ├── hexagram-viz/                 # Hexagram visualization
│   ├── acupoints-viz/                # Acupoints visualization
│   ├── math-viz/                     # Math visualization
│   └── octonion-viz/                 # Octonion visualization
│
├── docs/                             # Documentation (unchanged)
├── archive/                          # Archive (unchanged)
├── docker-compose.yml                # Docker orchestration
├── run_all.py                        # Script chạy tất cả services
└── run_monolith.py                   # Script chạy monolith mode (backward compatible)
```

## Service Registry

| Service | Port | URL Prefix | Mô tả |
|---------|------|------------|--------|
| Gateway | 5001 | `/` | API Gateway + Static files |
| Tu Vi Chart | 5011 | `/api/v1/chart` | Lập lá số Tử Vi |
| Tu Vi Finder | 5012 | `/api/v1/finder` | Tìm ngày giờ sinh |
| Tu Vi Analytics | 5013 | `/api/v1/analytics` | Phân tích Tài Mệnh |
| Tu Vi AI | 5014 | `/api/v1/ai` | AI luận giải |
| Thái Ất | 5015 | `/api/thai-at` | Thái Ất Thần Số |
| Kì Môn | 5016 | `/api/ki-mon` | Kì Môn Độn Giáp |
| Graph | 5017 | `/graph` | Knowledge Graph |
| Vi Diệu Pháp | 5018 | `/vdp` | Vi Diệu Pháp |

## Chế độ chạy

### 1. Microservice Mode (production)
```bash
python run_all.py              # Chạy tất cả services
python run_all.py --services tuvi-chart,tuvi-ai  # Chạy một số services
docker-compose up              # Chạy bằng Docker
```

### 2. Monolith Mode (development / backward compatible)
```bash
python run_monolith.py         # Chạy tất cả trong 1 process như cũ
```

### 3. Single Service Mode (development / testing)
```bash
cd services/tuvi-chart && python app.py   # Chạy 1 service riêng
```

## Shared Library

Tất cả services dùng chung `services/shared/` package:
```bash
cd services/tuvi-chart
pip install -e ../shared       # Install shared lib dạng editable
```

## Nguyên tắc thiết kế

1. **Mỗi service là 1 Flask app độc lập** - có thể chạy riêng, test riêng, deploy riêng
2. **Shared library** chứa code dùng chung (core, data, stars, chart)
3. **Gateway** là entry point duy nhất - forward requests đến service tương ứng
4. **Backward compatible** - `run_monolith.py` chạy giống hệt app cũ
5. **Easy to add/remove** - Thêm/xóa service chỉ cần thêm/xóa folder + cập nhật gateway
