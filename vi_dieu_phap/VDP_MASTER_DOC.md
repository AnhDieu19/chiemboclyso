# HỒ SƠ DỰ ÁN VI DIỆU PHÁP (KNOWLEDGE GRAPH)

> **Ngày cập nhật:** 01/01/2026
> **Trạng thái:** Stable v3.1 (Clean Architecture + 3-Page Split)
> **Kiến trúc:** Clean Architecture (Domain - UseCase - Infra - Presentation)

## 1. TỔNG QUAN

Dự án **Vi Diệu Pháp (VDP)** là module trực quan hóa hệ thống tâm lý học Phật giáo (Thắng Pháp) dưới dạng Knowledge Graph.

Module được tái xây dựng theo **Clean Architecture** để đảm bảo tính mở rộng và bảo trì, hỗ trợ native 3 chế độ xem riêng biệt.

---

## 2. KIẾN TRÚC HỆ THỐNG (SYSTEM ARCHITECTURE)

Dự án tuân thủ nghiêm ngặt mô hình phân lớp Clean Architecture:

```
vi_dieu_phap/
├── domain/                    # [CORE] Entities & Business Rules
│   └── models.py              # Classes: Node, Link, GrapphData
│
├── infrastructure/            # [DATA LAYER]
│   └── json_repository.py     # Đọc JSON từ `data/`, áp dụng Rules Hierarchy -> Trả về Domain Objects.
│
├── application/               # [LOGIC LAYER] Use Cases
│   └── graph_service.py       # Xử lý logic lọc graph (Structure, Association, Root Cause).
│
└── presentation/              # [INTERFACE LAYER]
    └── web/
        ├── routes.py          # Flask Blueprint & Controllers
        ├── static/            # JS (D3 Core, UI) & CSS
        └── templates/         # HTML Views
```

### 2.1 Luồng Dữ Liệu (Data Flow)

1.  **Request:** User truy cập `/vdp/structure`.
2.  **Controller:** `routes.py` gọi `service.get_structure_graph()`.
3.  **Service:** `GraphService` gọi `repository.get_all_data()`.
4.  **Repository:** `JsonRepository` đọc data gốc, xử lý logic ghép nối cha-con (Rules), trả về danh sách `Node/Link` Objects.
5.  **Service:** Lọc lại các Links thuộc loại `structure` và các Nodes liên quan -> Convert sang Dict.
6.  **Response:** Trả JSON về cho Frontend D3.js render.

---

## 3. FRONTEND MODULES (FE)

Vị trí: `/vi_dieu_phap/presentation/web/static/`

*   **`vdp_core.js`**: Core Engine (D3 Force Simulation). Chịu trách nhiệm render SVG và physics.
*   **`vdp_ui.js`**: Interaction Layer. Chịu trách nhiệm Event, Tooltip, Checkbox.
*   **`vdp_style.css`**: Styling cho toàn bộ module.

### 3.1 Mô Hình Tương Tác (Interaction Model)
Module Frontend hoạt động theo mô hình **Core - UI Separation**:
*   **VDP.Core:**
    *   Quản lý `d3.forceSimulation`.
    *   Lưu trữ dữ liệu gốc: `allLinksData`.
    *   Cung cấp API `getAllLinks()` để các module khác truy xuất dữ liệu gốc nhằm mục đích lọc.
    *   Cung cấp API `getElements()` để truy xuất các DOM elements (circle, line, text).
*   **VDP.UI:**
    *   Khởi tạo Filters checkbox.
    *   Lắng nghe sự kiện change -> gọi `renderDynamicFilters` -> `updateFilters`.
    *   Trong `updateFilters`, gọi `VDP.Core.getAllLinks()` để lấy dữ liệu, sau đó áp dụng logic lọc (ẩn/hiện) và gọi ngược lại `VDP.Core.updateSimulationLinks(visibleLinks)` để cập nhật physics.

### 3.2 Logic Bộ Lọc (Filtering Logic)
Filter hoạt động dựa trên metadata của Node:
1.  **Backend:** Gán thuộc tính `group` chi tiết cho từng Node (ví dụ: "Universals", "Unwholesome" thay vì chỉ "Cetasika").
2.  **UI:** `renderDynamicFilters` quét toàn bộ Nodes để lấy danh sách Groups duy nhất và tạo checkbox tương ứng.
3.  **Logic:** 
    *   Link được hiện khi: (Type Link được chọn) AND (Source Group được chọn) AND (Target Group được chọn).
    *   Node được hiện khi: Group của nó được chọn.

---

## 4. HƯỚNG DẪN SỬ DỤNG API

Module cung cấp các endpoints chuẩn RESTful (ReadOnly):

*   `GET /vdp/api/data` - Lấy toàn bộ dữ liệu (Raw).
*   `GET /vdp/api/data/structure` - Chỉ lấy dữ liệu Cấu Trúc (Cây phân loại).
*   `GET /vdp/api/data/association` - Chỉ lấy dữ liệu Tương Ưng (Tâm - Sở Hữu).
*   `GET /vdp/api/data/root_cause` - Chỉ lấy dữ liệu Nhân Sanh (Tâm - Nhân).

---

## 5. HƯỚNG DẪN BẢO TRÌ

### 5.1 Thay đổi cấu trúc dữ liệu
*   Sửa file JSON trong `vi_dieu_phap/data/json/`.
*   Cập nhật `infrastructure/json_repository.py` nếu thêm trường mới vào Logic.

### 5.2 Thêm view mới
1.  Thêm method `get_new_view_graph()` vào `application/graph_service.py`.
2.  Thêm route `/new-view` và API `/api/data/new-view` vào `presentation/web/routes.py`.
3.  Tạo template mới trong `presentation/web/templates/`.

---

## 6. LỊCH SỬ THAY ĐỔI
*   **v1.0:** Monolithic Script (`graph/`).
*   **v2.0:** Modular Web App (`web/` + `repository.py` cũ).
*   **v3.0:** Clean Architecture Rebuild (Current). Tách biệt Domain, Infra, App Services.

---

## 7. KHẮC PHỤC SỰ CỐ (TROUBLESHOOTING)

Tổng hợp các lỗi thường gặp trong quá trình phát triển và vận hành hệ thống VDP.

### 7.1 Lỗi Dữ Liệu (Data Integrity)
*   **Triệu chứng:** Node không hiện link, hoặc bị gom nhóm sai.
*   **Nguyên nhân:**
    *   Trường `group` trong Master Data (Python) hoặc JSON không khớp với Rules Hierarchy.
    *   Ví dụ: Data ghi `group="Rupa"` nhưng Rules yêu cầu `group="Rupa-Kusala"`.
*   **Giải pháp:** 
    1.  Kiểm tra `rules_hierarchy.json` để xem yêu cầu cha-con.
    2.  Sửa master data (`citta_master.py`...) để match đúng yêu cầu.
    3.  Chạy lại `migrate_to_json.py`.

### 7.2 Lỗi Server Cache/Reload (Backend)
*   **Triệu chứng:** Đã sửa code Python nhưng API vẫn trả về kết quả cũ.
*   **Nguyên nhân:**
    *   Flask Reload đôi khi không bắt được thay đổi trong các module con.
    *   File `__pycache__` cũ gây nhiễu mã bytecode.
    *   Process Python cũ (Zombie process) vẫn đang chạy nền và chiếm port.
*   **Giải pháp:**
    1.  **Dừng Server:** Dùng `Ctrl+C` hoặc `taskkill /F /IM python.exe`.
    2.  **Xóa Cache:** Xóa toàn bộ folder `__pycache__` (nhất là trong `infrastructure/`).
    3.  **Khởi động lại:** Chạy lại `python backend/app.py`.

### 7.3 Lỗi Logic Khởi Tạo (Python Class Init)
*   **Triệu chứng:** Server crash khi khởi động, lỗi `AttributeError` hoặc `IndentationError` tiềm ẩn.
*   **Bài học:**
    *   Luôn **khởi tạo biến List/Dict** trước khi gọi hàm load dữ liệu (`_load_data`).
    *   Tránh gọi `_load_data` ngay dòng đầu của `__init__` nếu method này phụ thuộc vào các biến instance khác.
    *   Cẩn thận với thụt đầu dòng (Indentation) khi copy-paste code sửa lỗi.

### 7.4 Lỗi Đường Dẫn Import (Migration Script)
*   **Triệu chứng:** Chạy script `migrate_to_json.py` bị lỗi `ModuleNotFoundError`.
*   **Nguyên nhân:** Import path sai lệch giữa môi trường chạy script và cấu trúc project (`python.vi_dieu_phap` vs `vi_dieu_phap`).
*   **Giải pháp:**
    *   Sử dụng đường dẫn import chuẩn `vi_dieu_phap...` nếu chạy từ root.
    *   Sử dụng đường dẫn import chuẩn `vi_dieu_phap...` nếu chạy từ root.
    *   Kiểm tra `sys.path.append` trong script nếu cần.

### 7.5 Lỗi Frontend (Undefined Reference)
*   **Triệu chứng:** Bấm checkbox bộ lọc nhưng không có gì thay đổi (Filter không hoạt động). Console báo lỗi `Uncaught ReferenceError` hoặc `undefined`.
*   **Nguyên nhân:**
    *   Module UI gọi hàm từ một biến/module không tồn tại (ví dụ: gọi `VDP.Main.getAllLinks()` trong khi trang con chỉ load `VDP.Core`).
    *   Core Module không expose hàm lấy dữ liệu.
*   **Giải pháp:**
    *   Đảm bảo `VDP.Core` có hàm `getAllLinks()` trả về dữ liệu gốc.
    *   Sửa `vdp_ui.js` để gọi đúng `VDP.Core.getAllLinks()`.
