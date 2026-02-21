# Tu Vi Chart Service

Microservice cho lập lá số Tử Vi.

## Chạy riêng

```bash
cd services/tuvi-chart
pip install -r requirements.txt
python app.py
# → http://localhost:5011
```

## API Endpoints

| Method | Path | Mô tả |
|--------|------|--------|
| POST | `/api/v1/chart/generate` | Lập lá số Tử Vi |
| GET | `/api/v1/chart/star/<name>` | Tra cứu sao |
| GET | `/api/v1/chart/palace/<name>` | Tra cứu cung |
| POST | `/api/v1/chart/fortune` | Tính vận hạn |

## Dependencies

- `shared/core/` - Tính toán cơ bản
- `shared/chart/` - Chart builder
- `shared/stars/` - Star placers
- `shared/data/` - Lookup tables
- `shared/interpretation/` - Meanings
