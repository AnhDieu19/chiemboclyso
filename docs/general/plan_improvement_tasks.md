# 📋 DANH SÁCH TASK CẢI TIẾN DỰ ÁN

**Ngày tạo:** 22/12/2025  
**Dựa trên:** PROJECT_ANALYSIS_REPORT.md

---

## 🔴 PHASE 1: ỔN ĐỊNH (Tuần 1-2)

### TASK-P1-01: Hoàn thiện Test Coverage
**Assignee:** QC Team  
**Priority:** HIGH  
**Estimated:** 3 ngày

- [ ] Review 32 test files hiện có
- [ ] Thêm test cho các edge cases
- [ ] Tạo test cho tất cả API endpoints
- [ ] Mục tiêu: 80% code coverage

### TASK-P1-02: Performance Audit
**Assignee:** Dev Team  
**Priority:** HIGH  
**Estimated:** 2 ngày

- [ ] Profile API response time
- [ ] Xác định bottlenecks
- [ ] Optimize database queries (nếu có)
- [ ] Implement caching cho static data

### TASK-P1-03: Security Review
**Assignee:** Dev Team  
**Priority:** HIGH  
**Estimated:** 1 ngày

- [ ] Input validation tất cả endpoints
- [ ] Rate limiting (10 requests/minute/IP)
- [ ] CORS configuration
- [ ] Error message sanitization

---

## 🟡 PHASE 2: UI/UX UPGRADE (Tuần 3-4)

### TASK-P2-01: Responsive Design
**Assignee:** Frontend Dev  
**Priority:** MEDIUM  
**Estimated:** 5 ngày

**Files cần sửa:**
- `templates/index.html`
- `static/css/base.css`
- `static/css/chart.css`

**Checklist:**
- [ ] Mobile layout (< 768px)
- [ ] Tablet layout (768px - 1024px)
- [ ] Desktop layout (> 1024px)
- [ ] Touch-friendly buttons
- [ ] Readable font sizes

### TASK-P2-02: Dark Mode
**Assignee:** Frontend Dev  
**Priority:** LOW  
**Estimated:** 2 ngày

- [ ] CSS variables cho colors
- [ ] Toggle button
- [ ] Save preference to localStorage
- [ ] Smooth transition

### TASK-P2-03: Print/Export PDF
**Assignee:** Dev Team  
**Priority:** MEDIUM  
**Estimated:** 3 ngày

**Đề xuất thư viện:** `weasyprint` hoặc `pdfkit`

- [ ] Tạo template PDF
- [ ] API endpoint `/api/export/pdf`
- [ ] Include chart visualization
- [ ] Include interpretation text

### TASK-P2-04: Improved Chart Visualization
**Assignee:** Frontend Dev  
**Priority:** MEDIUM  
**Estimated:** 5 ngày

**Đề xuất:**
- [ ] SVG-based chart (thay vì table)
- [ ] Hover tooltips cho sao
- [ ] Color coding theo Ngũ Hành
- [ ] Animation khi load
- [ ] Zoom/Pan cho mobile

---

## 🟢 PHASE 3: NEW FEATURES (Tuần 5-8)

### TASK-P3-01: So Sánh Hợp Duyên
**Assignee:** Dev Team  
**Priority:** MEDIUM  
**Estimated:** 5 ngày

**Backend:**
- [ ] Endpoint `/api/compare`
- [ ] Logic tính điểm hợp duyên
- [ ] Phân tích Cung Phu Thê

**Frontend:**
- [ ] Form nhập 2 người
- [ ] Hiển thị kết quả so sánh
- [ ] Chart comparison view

### TASK-P3-02: Chọn Ngày Tốt
**Assignee:** Dev Team  
**Priority:** LOW  
**Estimated:** 5 ngày

**Backend:**
- [ ] Endpoint `/api/good-day`
- [ ] Logic theo mục đích (kết hôn, khai trương, di chuyển...)
- [ ] Tích hợp với lá số người dùng

**Frontend:**
- [ ] Date picker range
- [ ] Filter theo mục đích
- [ ] Calendar view với ngày tốt highlight

### TASK-P3-03: User Accounts + Lưu Lá Số
**Assignee:** Dev Team  
**Priority:** LOW  
**Estimated:** 7 ngày

**Dependencies:** Database upgrade

- [ ] User registration/login
- [ ] Save chart to account
- [ ] Chart history
- [ ] Share via link

---

## ⚙️ INFRASTRUCTURE TASKS

### TASK-INF-01: API Documentation
**Assignee:** Dev Team  
**Priority:** MEDIUM  
**Estimated:** 2 ngày

**Đề xuất:** Swagger/OpenAPI

- [ ] Document tất cả endpoints
- [ ] Request/Response schemas
- [ ] Example requests
- [ ] Host tại `/api/docs`

### TASK-INF-02: Database Migration
**Assignee:** Dev Team  
**Priority:** LOW  
**Estimated:** 3 ngày

**Lý do:** Hiện tại dùng file JSONL, cần scale

- [ ] Chọn DB (SQLite → PostgreSQL)
- [ ] Design schema
- [ ] Migration script
- [ ] Update data layer

### TASK-INF-03: Caching Layer
**Assignee:** Dev Team  
**Priority:** MEDIUM  
**Estimated:** 2 ngày

**Đề xuất:** Redis hoặc in-memory cache

- [ ] Cache chart data (TTL: 1 hour)
- [ ] Cache AI responses (TTL: 24 hours)
- [ ] Invalidation strategy

### TASK-INF-04: Logging & Monitoring
**Assignee:** Dev Team  
**Priority:** MEDIUM  
**Estimated:** 1 ngày

- [ ] Structured logging (JSON format)
- [ ] Request/Response logging
- [ ] Error tracking
- [ ] Performance metrics

---

## 📊 TASK SUMMARY

| Phase | Tasks | Estimated Days | Priority |
|-------|-------|----------------|----------|
| Phase 1 | 3 tasks | 6 days | HIGH |
| Phase 2 | 4 tasks | 15 days | MEDIUM |
| Phase 3 | 3 tasks | 17 days | LOW-MEDIUM |
| Infrastructure | 4 tasks | 8 days | MEDIUM |
| **TOTAL** | **14 tasks** | **46 days** | - |

---

## 🎯 SPRINT PLANNING

### Sprint 1 (Week 1-2): Stabilization
- TASK-P1-01: Test Coverage ✅
- TASK-P1-02: Performance Audit ✅
- TASK-P1-03: Security Review ✅

### Sprint 2 (Week 3-4): UI/UX
- TASK-P2-01: Responsive Design
- TASK-P2-02: Dark Mode
- TASK-INF-01: API Documentation

### Sprint 3 (Week 5-6): Print & Visualization
- TASK-P2-03: Print/Export PDF
- TASK-P2-04: Improved Chart

### Sprint 4 (Week 7-8): New Features
- TASK-P3-01: So Sánh Hợp Duyên
- TASK-INF-03: Caching Layer

### Backlog (Future):
- TASK-P3-02: Chọn Ngày Tốt
- TASK-P3-03: User Accounts
- TASK-INF-02: Database Migration
- TASK-INF-04: Logging & Monitoring

---

## ✅ DEFINITION OF DONE

Mỗi task được coi là DONE khi:
1. ✅ Code đã được review
2. ✅ Unit tests pass
3. ✅ Integration tests pass
4. ✅ Documentation updated
5. ✅ No linting errors
6. ✅ QC sign-off

---

*Task list tạo: 22/12/2025*  
*Người tạo: BA Team*

