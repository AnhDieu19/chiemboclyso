# TỬ VI NAM PHÁI - TÀI LIỆU DỰ ÁN

## Tổng Quan

Thư mục này chứa tất cả các tài liệu Business Analysis (BA) và hướng dẫn kỹ thuật cho dự án **Ứng dụng Tử Vi Đẩu Số Nam Phái**.

**File quản lý chính:** [DOCS_MASTER.md](./DOCS_MASTER.md)

---

## Danh Sách Tài Liệu Chính

| # | Tài liệu | Mô tả | Đối tượng |
|---|----------|-------|-----------| 
| 1 | [PROJECT_ANALYSIS_REPORT.md](./PROJECT_ANALYSIS_REPORT.md) | Báo cáo phân tích dự án v2.0 | PM, Dev, BA |
| 2 | [BA_SYSTEM_ARCHITECTURE.md](./BA_SYSTEM_ARCHITECTURE.md) | Kiến trúc hệ thống | PM, Dev, BA |
| 3 | [BA_USE_CASES.md](./BA_USE_CASES.md) | Chi tiết Use Cases | BA, Dev, QA |
| 4 | [BA_DATA_DICTIONARY.md](./BA_DATA_DICTIONARY.md) | Từ điển dữ liệu Tử Vi | Dev, Content |
| 5 | [BA_UI_SPECIFICATIONS.md](./BA_UI_SPECIFICATIONS.md) | Đặc tả UI/UX | Designer, Frontend |
| 6 | [CALCULATION_GUIDE.md](./CALCULATION_GUIDE.md) | Hướng dẫn tính toán | Dev |
| 7 | [THAI_AT_KI_MON_SPEC.md](./THAI_AT_KI_MON_SPEC.md) | Đặc tả Thái Ất/Kì Môn | Dev |
| 8 | [NGU_HANH_MATH_BASIS.md](./NGU_HANH_MATH_BASIS.md) | Cơ sở toán học Ngũ Hành | Dev |

---

## Tính Năng Hệ Thống (v2.0)

### Core Features
- Lập lá số Tử Vi (~117 sao)
- Luận giải 12 cung
- 15 cách cục đặc biệt
- Đại Hạn, Tiểu Hạn, Lưu Niên
- Tứ Hóa (Lộc, Quyền, Khoa, Kỵ)

### Advanced Features
- Reverse Finder (tìm ngày sinh từ đặc điểm)
- AI Integration (Gemini)
- Knowledge Graph với D3.js
- Analytics Dashboard

### Modules Mới (12/2024)
- Thái Ất Thần Số (16 Thần, 9 Cung)
- Kì Môn Độn Giáp (8 Môn, 9 Tinh)
- Ngũ Hành Engine (dùng chung)
- Knowledge Graph (12 Cung Grid)

---

## Thống Kê Dự Án

| Metric | Giá trị |
|--------|---------|
| Số lượng sao | ~117 sao |
| Số cung | 12 cung |
| Số Use Cases | 8+ UC |
| Số API Endpoints | 20+ |
| Số Business Rules | 30+ |
| Test files | 34 files |

---

## Công Nghệ Sử Dụng

```
Frontend:   HTML5, CSS3, JavaScript, D3.js
Backend:    Python 3.x, Flask
API:        RESTful JSON
Design:     Responsive, Mobile-First
AI:         Google Gemini API
```

---

## Trạng Thái Phát Triển

```
Phase 1 (MVP):          [====================] 100%
Phase 2 (Knowledge):    [==================  ]  90%
Phase 3 (Thái Ất):      [================    ]  80%
Phase 4 (Kì Môn):       [========            ]  40%
Phase 5 (Huyền Không):  [                    ]   0%
```

---

## Liên Kết Thư Mục

| Folder | Mô tả |
|--------|-------|
| `/python/core/` | Modules tính toán cơ bản |
| `/python/data/` | Dữ liệu tĩnh (constants) |
| `/python/stars/` | Modules an sao |
| `/python/chart/` | Module xây dựng lá số |
| `/python/graph/` | Module Knowledge Graph |
| `/python/logic/` | Modules AI (Thái Ất, Kì Môn) |
| `/python/services/` | External services (Gemini) |
| `/python/interpretation/` | Modules luận giải |
| `/python/UML/` | UML diagrams (.drawio) |

---

## Quick Start

### Chạy Server Development

```bash
cd python
python app.py
```

Server sẽ chạy tại: `http://localhost:5000`

### Các Trang Chính
- Tử Vi: `http://localhost:5000/`
- Finder: `http://localhost:5000/finder`
- Knowledge Graph: `http://localhost:5000/knowledge-graph`
- Thái Ất: `http://localhost:5000/thai-at`
- Kì Môn: `http://localhost:5000/ki-mon`

### API Test

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"day": 15, "month": 12, "year": 1990, "hour": 6, "gender": "nam"}'
```

---

## Changelog

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 15/12/2024 | Initial BA documentation |
| 2.0 | 25/12/2024 | Added Thái Ất, Kì Môn, Knowledge Graph, Ngũ Hành Engine |

---

*Cập nhật lần cuối: 25/12/2024*
