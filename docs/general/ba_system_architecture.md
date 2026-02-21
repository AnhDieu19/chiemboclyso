# TỬ VI NAM PHÁI - TÀI LIỆU PHÂN TÍCH HỆ THỐNG (BA Document)

## 📋 Thông Tin Tài Liệu

| Thông tin | Chi tiết |
|-----------|----------|
| Dự án | Ứng dụng Tử Vi Đẩu Số - Nam Phái |
| Phiên bản | 1.0 |
| Ngày tạo | 15/12/2025 |
| Tác giả | Business Analyst |

---

## 📑 MỤC LỤC

1. [Tổng Quan Dự Án](#1-tổng-quan-dự-án)
2. [Phạm Vi Hệ Thống](#2-phạm-vi-hệ-thống)
3. [Các Bên Liên Quan](#3-các-bên-liên-quan)
4. [Yêu Cầu Nghiệp Vụ](#4-yêu-cầu-nghiệp-vụ)
5. [Kiến Trúc Hệ Thống](#5-kiến-trúc-hệ-thống)
6. [Module Chức Năng](#6-module-chức-năng)
7. [Mô Hình Dữ Liệu](#7-mô-hình-dữ-liệu)
8. [User Stories & Use Cases](#8-user-stories--use-cases)
9. [API Specification](#9-api-specification)
10. [Business Rules](#10-business-rules)
11. [Roadmap Phát Triển](#11-roadmap-phát-triển)

---

## 1. TỔNG QUAN DỰ ÁN

### 1.1 Giới Thiệu

**Tử Vi Đẩu Số Nam Phái** là một ứng dụng web giúp người dùng lập và luận giải lá số Tử Vi theo trường phái Nam Phái (còn gọi là phái Miền Nam hoặc phái cổ điển Việt Nam).

### 1.2 Mục Tiêu

| # | Mục tiêu | Mô tả |
|---|----------|-------|
| 1 | **Chính xác** | Tính toán lá số Tử Vi chính xác theo thuật toán Nam Phái |
| 2 | **Dễ sử dụng** | Giao diện thân thiện, hỗ trợ cả người mới bắt đầu |
| 3 | **Giáo dục** | Cung cấp giải thích chi tiết để học viên hiểu rõ |
| 4 | **Toàn diện** | Hỗ trợ đầy đủ 110+ sao và các vòng phụ tinh |
| 5 | **Hiện đại** | Thiết kế responsive, hoạt động trên mọi thiết bị |

### 1.3 Đặc Điểm Nam Phái

| Tiêu chí | Nam Phái | Bắc Phái |
|----------|----------|----------|
| Tứ Hóa | Theo bảng cổ điển VN | Theo bảng Đài Loan |
| An Hóa Khoa | Vũ Khúc (năm Giáp) | Thiên Phủ |
| An Thiên Mã | Theo Chi năm | Theo Chi tháng |
| Đại Vận | 10 năm/Đại vận | Tùy phái |
| Tiểu Vận | Theo Chi năm | Theo Chi tháng |

---

## 2. PHẠM VI HỆ THỐNG

### 2.1 Trong Phạm Vi (In Scope)

```
┌─────────────────────────────────────────────────────────────────┐
│                    PHẠM VI HỆ THỐNG                              │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Module Lập Lá Số                                            │
│     • Chuyển đổi Dương lịch ↔ Âm lịch                           │
│     • Tính Can Chi (năm, tháng, ngày, giờ)                      │
│     • Xác định Cung Mệnh, Cung Thân                             │
│     • Xác định Cục (Thủy/Mộc/Kim/Thổ/Hỏa)                      │
│     • An 14 Chính Tinh                                          │
│     • An 75+ Phụ Tinh                                           │
│     • Áp dụng Tứ Hóa                                            │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Module Luận Giải                                            │
│     • Phân tích 12 Cung                                         │
│     • Đánh giá Cách Cục                                         │
│     • Ý nghĩa từng sao                                          │
│     • Ý nghĩa Miếu/Vượng/Đắc/Bình/Hãm                          │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Module Đại/Tiểu Vận                                         │
│     • Tính Đại Vận 10 năm                                       │
│     • Tính Tiểu Vận hàng năm                                    │
│     • Tính Lưu Niên, Lưu Nguyệt, Lưu Nhật                      │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Giao Diện Người Dùng                                        │
│     • Form nhập thông tin sinh                                   │
│     • Hiển thị lá số 12 cung                                    │
│     • Popup chi tiết từng sao                                   │
│     • Bản in PDF                                                │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Ngoài Phạm Vi (Out of Scope) - Phase 1

- ❌ Lưu trữ lá số (Database)
- ❌ Hệ thống tài khoản người dùng
- ❌ So sánh lá số (Hợp hôn)
- ❌ Dự đoán AI/ML
- ❌ Tích hợp thanh toán

---

## 3. CÁC BÊN LIÊN QUAN

### 3.1 Stakeholders

```
                    ┌─────────────────┐
                    │   Product Owner │
                    │    (Quyết định) │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   End Users   │   │  Developers   │   │   Experts     │
│ (Người dùng)  │   │  (Kỹ thuật)   │   │ (Chuyên gia)  │
└───────────────┘   └───────────────┘   └───────────────┘
```

### 3.2 Đối Tượng Người Dùng

| Persona | Mô tả | Nhu cầu chính |
|---------|-------|---------------|
| **Người mới học** | Người bắt đầu tìm hiểu Tử Vi | Giải thích dễ hiểu, UI đơn giản |
| **Người có kinh nghiệm** | Biết căn bản Tử Vi | Tính năng nâng cao, chi tiết |
| **Chuyên gia** | Thầy Tử Vi, nghiên cứu | Độ chính xác tuyệt đối, tùy biến |

---

## 4. YÊU CẦU NGHIỆP VỤ

### 4.1 Yêu Cầu Chức Năng (Functional Requirements)

#### FR-01: Nhập Thông Tin Sinh

| ID | Yêu cầu | Priority |
|----|---------|----------|
| FR-01.1 | Nhập ngày/tháng/năm Dương lịch | Must |
| FR-01.2 | Nhập ngày/tháng/năm Âm lịch | Must |
| FR-01.3 | Chọn giờ sinh (12 canh giờ) | Must |
| FR-01.4 | Chọn giới tính (Nam/Nữ) | Must |
| FR-01.5 | Đánh dấu tháng nhuận (nếu có) | Should |

#### FR-02: Lập Lá Số

| ID | Yêu cầu | Priority |
|----|---------|----------|
| FR-02.1 | Chuyển đổi Dương ↔ Âm lịch chính xác | Must |
| FR-02.2 | Tính Can Chi đúng theo Nam Phái | Must |
| FR-02.3 | Xác định Cung Mệnh, Thân chính xác | Must |
| FR-02.4 | An đủ 14 Chính Tinh | Must |
| FR-02.5 | An đủ 75+ Phụ Tinh | Must |
| FR-02.6 | Áp dụng Tứ Hóa theo Nam Phái | Must |
| FR-02.7 | Tính độ sáng sao (Miếu/Vượng/Đắc/Hãm) | Should |

#### FR-03: Hiển Thị Lá Số

| ID | Yêu cầu | Priority |
|----|---------|----------|
| FR-03.1 | Hiển thị 12 cung theo bố cục truyền thống | Must |
| FR-03.2 | Hiển thị đầy đủ các sao trong mỗi cung | Must |
| FR-03.3 | Phân biệt Chính Tinh và Phụ Tinh | Should |
| FR-03.4 | Hiển thị màu sắc theo Tứ Hóa | Should |
| FR-03.5 | Responsive trên mọi thiết bị | Should |

#### FR-04: Luận Giải

| ID | Yêu cầu | Priority |
|----|---------|----------|
| FR-04.1 | Giải thích ý nghĩa từng Cung | Must |
| FR-04.2 | Giải thích ý nghĩa từng Sao | Must |
| FR-04.3 | Phân tích Cách Cục đặc biệt | Should |
| FR-04.4 | Tổng hợp luận giải tổng quan | Should |

### 4.2 Yêu Cầu Phi Chức Năng (Non-Functional Requirements)

| ID | Loại | Yêu cầu |
|----|------|---------|
| NFR-01 | Performance | Thời gian lập lá số < 2 giây |
| NFR-02 | Usability | UI/UX thân thiện, không cần hướng dẫn |
| NFR-03 | Compatibility | Hỗ trợ Chrome, Firefox, Safari, Edge |
| NFR-04 | Responsiveness | Hiển thị tốt trên Mobile (320px+) |
| NFR-05 | Accuracy | Độ chính xác 100% theo Nam Phái |
| NFR-06 | Availability | Uptime 99.5% |

---

## 5. KIẾN TRÚC HỆ THỐNG

### 5.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           PRESENTATION LAYER                             │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     Web Frontend (HTML/CSS/JS)                   │   │
│  │  • Input Form  • Chart Display  • Interpretation Panel          │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    │ HTTP/REST API
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                           APPLICATION LAYER                              │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     Flask Backend (Python)                       │   │
│  │  • API Endpoints  • Request Handling  • Response Formatting     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                            BUSINESS LAYER                                │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │  Core Module │ │ Stars Module │ │ Chart Module │ │ Interp Module│   │
│  │  • Calendar  │ │ • Chinh Tinh │ │ • Builder    │ │ • Analyzer   │   │
│  │  • Can Chi   │ │ • Phu Tinh   │ │ • Validator  │ │ • Meanings   │   │
│  │  • Cuc/Menh  │ │ • Tu Hoa     │ │              │ │ • Patterns   │   │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                             DATA LAYER                                   │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                   Static Data (Python Dicts)                     │   │
│  │  • Can Chi Data  • Star Positions  • Cuc Tables  • Meanings     │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Component Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              PYTHON BACKEND                              │
│                                                                          │
│  ┌────────────────────────────────────────────────────────────────┐    │
│  │                          app.py (Flask)                         │    │
│  │    /api/generate   /api/star/<name>   /api/palace/<name>       │    │
│  └───────────────────────────────┬────────────────────────────────┘    │
│                                  │                                      │
│         ┌────────────────────────┼────────────────────────┐            │
│         │                        │                        │            │
│         ▼                        ▼                        ▼            │
│  ┌─────────────┐          ┌─────────────┐          ┌─────────────┐    │
│  │   core/     │          │   stars/    │          │ interpret/  │    │
│  ├─────────────┤          ├─────────────┤          ├─────────────┤    │
│  │lunar_convert│          │chinh_tinh   │          │analyzer     │    │
│  │can_chi_calc │          │luc_cat      │          │meanings/    │    │
│  │cung_menh    │          │luc_sat      │          │patterns     │    │
│  │cuc_calc     │          │truong_sinh  │          │             │    │
│  │fortune_peri │          │bac_sy       │          │             │    │
│  └─────────────┘          │thai_tue     │          └─────────────┘    │
│         │                 │tu_hoa       │                 │            │
│         │                 │other_stars  │                 │            │
│         │                 └─────────────┘                 │            │
│         │                        │                        │            │
│         └────────────────────────┼────────────────────────┘            │
│                                  │                                      │
│                                  ▼                                      │
│                          ┌─────────────┐                               │
│                          │   chart/    │                               │
│                          ├─────────────┤                               │
│                          │chart_builder│                               │
│                          └─────────────┘                               │
│                                  │                                      │
│                                  ▼                                      │
│                          ┌─────────────┐                               │
│                          │    data/    │                               │
│                          ├─────────────┤                               │
│                          │can_chi      │                               │
│                          │chinh_tinh   │                               │
│                          │cung_cuc     │                               │
│                          │phu_tinh_*   │                               │
│                          │star_bright  │                               │
│                          │tu_hoa       │                               │
│                          └─────────────┘                               │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. MODULE CHỨC NĂNG

### 6.1 Tổng Quan Modules

```
tuvi-app/
├── python/
│   ├── app.py                    # Flask main application
│   │
│   ├── core/                     # 🧮 Core Calculations
│   │   ├── lunar_converter.py    # Dương→Âm lịch
│   │   ├── can_chi_calc.py       # Tính Can Chi
│   │   ├── cung_menh.py          # Cung Mệnh/Thân
│   │   ├── cuc_calc.py           # Xác định Cục
│   │   └── fortune_periods.py    # Đại/Tiểu Vận
│   │
│   ├── data/                     # 📊 Static Data
│   │   ├── can_chi.py            # Thiên Can, Địa Chi
│   │   ├── chinh_tinh.py         # 14 Chính Tinh positions
│   │   ├── cung_cuc.py           # Bảng tra Cục
│   │   ├── phu_tinh_*.py         # Phụ Tinh data (6 files)
│   │   ├── star_brightness.py    # Độ sáng sao
│   │   └── tu_hoa.py             # Bảng Tứ Hóa
│   │
│   ├── stars/                    # ⭐ Star Placement
│   │   ├── chinh_tinh_placer.py  # An 14 Chính Tinh
│   │   ├── luc_cat_placer.py     # An Lục Cát
│   │   ├── luc_sat_placer.py     # An Lục Sát
│   │   ├── truong_sinh_placer.py # Vòng Trường Sinh
│   │   ├── bac_sy_placer.py      # Vòng Bác Sỹ
│   │   ├── thai_tue_placer.py    # Vòng Thái Tuế
│   │   ├── tu_hoa_applier.py     # Áp dụng Tứ Hóa
│   │   └── other_stars_placer.py # Các sao khác
│   │
│   ├── chart/                    # 📋 Chart Building
│   │   └── chart_builder.py      # Tổng hợp lá số
│   │
│   └── interpretation/           # 💡 Interpretation
│       ├── chart_analyzer.py     # Phân tích lá số
│       ├── patterns.py           # Cách Cục đặc biệt
│       └── meanings/             # Ý nghĩa
│           ├── chinh_tinh_meanings.py
│           ├── palace_meanings.py
│           └── phu_tinh_meanings.py
│
└── docs/                         # 📚 Documentation
```

### 6.2 Chi Tiết Từng Module

#### 6.2.1 Core Module - Tính Toán Cơ Bản

| File | Chức năng | Input | Output |
|------|-----------|-------|--------|
| `lunar_converter.py` | Chuyển đổi Âm Dương | (day, month, year) | LunarDate object |
| `can_chi_calc.py` | Tính Can Chi | LunarDate | CanChi object |
| `cung_menh.py` | Tính Cung Mệnh/Thân | (month, hour) | (menh_index, than_index) |
| `cuc_calc.py` | Xác định Cục | (can_nam, menh_cung) | Cuc number (2-6) |
| `fortune_periods.py` | Tính Đại/Tiểu Vận | Chart object | Fortune periods |

#### 6.2.2 Stars Module - An Sao

| File | Số sao | Phương pháp |
|------|--------|-------------|
| `chinh_tinh_placer.py` | 14 | Theo vị trí Tử Vi |
| `luc_cat_placer.py` | 6 | Theo tháng/giờ/can năm |
| `luc_sat_placer.py` | 6 | Theo Lộc Tồn/giờ/chi năm |
| `truong_sinh_placer.py` | 12 | Theo Cục + Âm/Dương |
| `bac_sy_placer.py` | 12 | Từ Lộc Tồn |
| `thai_tue_placer.py` | 12 | Theo Chi năm |
| `tu_hoa_applier.py` | 4 | Theo Can năm |
| `other_stars_placer.py` | 40+ | Các quy tắc khác |

#### 6.2.3 Interpretation Module - Luận Giải

| Component | Mô tả |
|-----------|-------|
| `chart_analyzer.py` | Phân tích tổng thể lá số |
| `patterns.py` | Nhận diện Cách Cục đặc biệt |
| `meanings/` | Ý nghĩa chi tiết từng sao và cung |

---

## 7. MÔ HÌNH DỮ LIỆU

### 7.1 Core Data Structures

```python
# Thông tin ngày sinh
BirthInfo = {
    "solar_date": {
        "day": int,
        "month": int,
        "year": int
    },
    "lunar_date": {
        "day": int,
        "month": int,
        "year": int,
        "is_leap_month": bool
    },
    "hour": int,              # 0-11 (Tý đến Hợi)
    "gender": str             # "nam" | "nu"
}

# Can Chi đầy đủ
CanChi = {
    "year": {
        "can": str,           # "Giáp", "Ất", ...
        "chi": str,           # "Tý", "Sửu", ...
        "can_index": int,     # 0-9
        "chi_index": int      # 0-11
    },
    "month": {...},
    "day": {...},
    "hour": {...}
}

# Thông tin 1 Cung
Palace = {
    "index": int,             # 0-11 (Tý đến Hợi)
    "name": str,              # "Mệnh", "Phụ Mẫu", ...
    "chi": str,               # Địa chi của cung
    "stars": [                # Danh sách sao
        {
            "name": str,
            "type": str,      # "chinh_tinh" | "phu_tinh"
            "brightness": str, # "Miếu" | "Vượng" | "Đắc" | "Bình" | "Hãm"
            "tu_hoa": str     # "Lộc" | "Quyền" | "Khoa" | "Kỵ" | null
        }
    ],
    "is_than_cung": bool      # True nếu là cung Thân
}

# Lá số hoàn chỉnh
BirthChart = {
    "birth_info": BirthInfo,
    "can_chi": CanChi,
    "cuc": {
        "name": str,          # "Thủy Nhị Cục", ...
        "number": int,        # 2-6
        "element": str        # "Thủy", "Mộc", ...
    },
    "menh_cung": int,         # Index cung Mệnh
    "than_cung": int,         # Index cung Thân
    "nap_am": str,            # Nạp Âm năm sinh
    "palaces": [Palace] * 12, # 12 cung
    "dai_van": [...],         # Đại vận
    "tieu_van": [...]         # Tiểu vận
}
```

### 7.2 Entity Relationship

```
┌───────────────┐       ┌───────────────┐       ┌───────────────┐
│  BirthInfo    │──────▶│  BirthChart   │◀──────│    Palace     │
│               │   1:1 │               │  1:12 │               │
│  - solar_date │       │  - cuc        │       │  - index      │
│  - lunar_date │       │  - menh_cung  │       │  - name       │
│  - hour       │       │  - than_cung  │       │  - chi        │
│  - gender     │       │  - nap_am     │       │  - is_than    │
└───────────────┘       └───────────────┘       └───────┬───────┘
                                                        │
                                                   1:N  │
                                                        ▼
                                                ┌───────────────┐
                                                │     Star      │
                                                │               │
                                                │  - name       │
                                                │  - type       │
                                                │  - brightness │
                                                │  - tu_hoa     │
                                                └───────────────┘
```

---

## 8. USER STORIES & USE CASES

### 8.1 User Stories

#### Epic 1: Lập Lá Số

| ID | User Story | Priority |
|----|------------|----------|
| US-1.1 | Là người dùng, tôi muốn nhập ngày sinh Dương lịch để hệ thống tự động chuyển đổi sang Âm lịch | Must |
| US-1.2 | Là người dùng, tôi muốn chọn giờ sinh từ dropdown để không cần nhớ tên canh giờ | Must |
| US-1.3 | Là người dùng, tôi muốn thấy lá số đầy đủ 12 cung với tất cả các sao | Must |
| US-1.4 | Là người dùng, tôi muốn phân biệt được Chính Tinh và Phụ Tinh qua màu sắc | Should |

#### Epic 2: Xem Chi Tiết

| ID | User Story | Priority |
|----|------------|----------|
| US-2.1 | Là người dùng, tôi muốn click vào sao để xem ý nghĩa chi tiết | Must |
| US-2.2 | Là người dùng, tôi muốn xem giải thích từng cung | Must |
| US-2.3 | Là người dùng, tôi muốn biết sao nào Miếu/Vượng/Hãm | Should |
| US-2.4 | Là người dùng, tôi muốn thấy highlight sao Hóa Lộc/Quyền/Khoa/Kỵ | Should |

#### Epic 3: Đại Tiểu Vận

| ID | User Story | Priority |
|----|------------|----------|
| US-3.1 | Là người dùng, tôi muốn xem Đại Vận của từng giai đoạn 10 năm | Should |
| US-3.2 | Là người dùng, tôi muốn xem Tiểu Vận của năm hiện tại | Should |
| US-3.3 | Là người dùng, tôi muốn xem Lưu Niên Tứ Hóa | Could |

### 8.2 Use Case Diagram

```
                         ┌────────────────────────────────────────┐
                         │          Tử Vi Nam Phái App            │
                         │                                        │
                         │  ┌─────────────────────────────────┐  │
                         │  │         UC-01                    │  │
    ┌─────────┐          │  │    Lập Lá Số Mới                │  │
    │  User   │──────────┼─▶│  • Nhập ngày sinh               │  │
    │(Người   │          │  │  • Chọn giờ sinh                │  │
    │ dùng)   │          │  │  • Chọn giới tính               │  │
    └─────────┘          │  └─────────────────────────────────┘  │
         │               │                                        │
         │               │  ┌─────────────────────────────────┐  │
         │               │  │         UC-02                    │  │
         ├───────────────┼─▶│    Xem Lá Số                    │  │
         │               │  │  • Hiển thị 12 cung             │  │
         │               │  │  • Xem chi tiết sao             │  │
         │               │  │  • Xem Cách Cục                 │  │
         │               │  └─────────────────────────────────┘  │
         │               │                                        │
         │               │  ┌─────────────────────────────────┐  │
         │               │  │         UC-03                    │  │
         ├───────────────┼─▶│    Xem Luận Giải                │  │
         │               │  │  • Ý nghĩa tổng quan            │  │
         │               │  │  • Phân tích từng cung          │  │
         │               │  │  • Nhận xét Cách Cục            │  │
         │               │  └─────────────────────────────────┘  │
         │               │                                        │
         │               │  ┌─────────────────────────────────┐  │
         │               │  │         UC-04                    │  │
         └───────────────┼─▶│    Xem Đại/Tiểu Vận             │  │
                         │  │  • Đại Vận 10 năm               │  │
                         │  │  • Tiểu Vận năm                 │  │
                         │  │  • Lưu Niên                     │  │
                         │  └─────────────────────────────────┘  │
                         │                                        │
                         └────────────────────────────────────────┘
```

---

## 9. API SPECIFICATION

### 9.1 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Trang chu - Form nhap thong tin |
| GET | `/finder` | Trang tim gio sinh nguoc (Reverse Lookup) |
| POST | `/api/generate` | Tao la so moi |
| POST | `/api/finder/solve` | Tim gio sinh dua tren dac diem |
| GET | `/api/star/{name}` | Lay thong tin sao |
| GET | `/api/palace/{name}` | Lay thong tin cung |

### 9.2 POST /api/generate

**Request:**
```json
{
    "day": 15,
    "month": 12,
    "year": 1990,
    "hour": 6,
    "gender": "nam",
    "is_lunar": false,
    "leap_month": false
}
```

**Response Success (200):**
```json
{
    "chart": {
        "birth_info": {...},
        "can_chi": {...},
        "cuc": {
            "name": "Mộc Tam Cục",
            "number": 3,
            "element": "Mộc"
        },
        "menh_cung": 2,
        "than_cung": 8,
        "palaces": [...]
    },
    "interpretation": {
        "overall": "...",
        "palaces": {...}
    },
    "dia_chi": ["Tý", "Sửu", ...],
    "gio_sinh_range": {...}
}
```

**Response Error (400/500):**
```json
{
    "error": "Ngày không hợp lệ (1-31)"
}
```

### 9.3 GET /api/star/{star_name}

**Response:**
```json
{
    "name": "Tử Vi",
    "type": "chinh_tinh",
    "element": "Thổ",
    "nature": "Cát tinh",
    "meaning": "Sao đế vương, chủ quyền quý...",
    "keywords": ["quyền lực", "cao quý", "lãnh đạo"]
}
```

### 9.4 POST /api/finder/solve

**Request:**
```json
{
    "year": 1994,
    "month": 3,
    "day": 15,
    "gender": "nam",
    "calendar_type": "lunar",
    "known_hour": "-1",
    "traits": ["Thong minh, sac sao", "Cong nghe thong tin (IT)"],
    "events": [{"type": "Ket hon", "year": 2022}]
}
```

**Response Success (200):**
```json
{
    "success": true,
    "status": "success",
    "total": 12,
    "candidates": [...],
    "all_candidates": [...],
    "top_timeline": [...]
}
```

**Luu y:** Frontend kiem tra `result.success` (boolean) de xac nhan thanh cong.

---

## 10. BUSINESS RULES

### 10.1 Quy Tắc Tính Toán
**Reference:** Chi tiết công thức xem tại `CALCULATION_GUIDE.md`.

| ID | Rule | Description |
|----|------|-------------|
| BR-01 | Chuyển đổi lịch | Sử dụng thuật toán Jean Meeus cho độ chính xác cao |
| BR-02 | Tháng nhuận | Tháng nhuận tính như tháng đứng trước |
| BR-03 | Giờ Tý (23h-1h) | Giờ Tý đầu (23h-24h) vẫn thuộc ngày hôm trước |
| BR-04 | Cung Mệnh | Khẩu quyết: "Chính nguyệt khởi Dần, thuận tháng nghịch giờ" |
| BR-05 | Cung Thân | Khẩu quyết: "Chính nguyệt khởi Dần, thuận tháng thuận giờ" |

### 10.2 Quy Tắc An Sao Nam Phái

| ID | Rule | Description |
|----|------|-------------|
| BR-10 | Tứ Hóa | Theo bảng Tứ Hóa cổ điển Việt Nam |
| BR-11 | Thiên Mã | An theo Chi năm (không phải Chi tháng) |
| BR-12 | Hóa Khoa Giáp | Năm Giáp: Vũ Khúc hóa Khoa (không phải Thiên Phủ) |
| BR-13 | Âm Dương | Nam sinh năm Dương đi thuận, năm Âm đi nghịch |
| BR-14 | Đại Vận | Mỗi Đại Vận 10 năm, khởi từ Cung Mệnh |

### 10.3 Quy Tắc Hiển Thị

| ID | Rule | Description |
|----|------|-------------|
| BR-20 | Thứ tự sao | Chính Tinh hiển thị trước Phụ Tinh |
| BR-21 | Màu Tứ Hóa | Lộc=Xanh, Quyền=Đỏ, Khoa=Tím, Kỵ=Đen |
| BR-22 | Độ sáng | Miếu/Vượng=Bold, Đắc/Bình=Normal, Hãm=Mờ |

---

## 11. ROADMAP PHÁT TRIỂN

### Phase 1: MVP (Hiện tại) ✅

```
[████████████████████████████████████████] 100%
```

- ✅ Lập lá số cơ bản
- ✅ An 14 Chính Tinh
- ✅ An 75+ Phụ Tinh
- ✅ Áp dụng Tứ Hóa
- ✅ Hiển thị 12 cung
- ✅ Luận giải cơ bản

### Phase 2: Enhanced (Q1 2026)

```
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0%
```

- ⬜ Đại Vận / Tiểu Vận
- ⬜ Lưu Niên Tứ Hóa
- ⬜ So sánh Lá số (Hợp hôn)
- ⬜ Export PDF
- ⬜ UI/UX Enhancement

### Phase 3: Premium (Q2 2026)

```
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0%
```

- ⬜ User Authentication
- ⬜ Lưu trữ lá số (Database)
- ⬜ Lịch sử tra cứu
- ⬜ Mobile App (React Native)

### Phase 4: Enterprise (Q3-Q4 2026)

```
[░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 0%
```

- ⬜ AI-powered predictions
- ⬜ Multi-language support
- ⬜ API for third-party
- ⬜ White-label solution

---

## 📎 PHỤ LỤC

### A. Danh Sách 14 Chính Tinh

| # | Tên | Ngũ Hành | Tính Chất |
|---|-----|----------|-----------|
| 1 | Tử Vi | Thổ | Đế tinh |
| 2 | Thiên Cơ | Mộc | Trí tuệ |
| 3 | Thái Dương | Hỏa | Quý nhân |
| 4 | Vũ Khúc | Kim | Tài tinh |
| 5 | Thiên Đồng | Thủy | Phúc tinh |
| 6 | Liêm Trinh | Hỏa | Quan tinh |
| 7 | Thiên Phủ | Thổ | Tài khố |
| 8 | Thái Âm | Thủy | Tài tinh |
| 9 | Tham Lang | Thủy/Mộc | Đào hoa |
| 10 | Cự Môn | Thủy | Ám tinh |
| 11 | Thiên Tướng | Thủy | Ấn tinh |
| 12 | Thiên Lương | Thổ | Ấm tinh |
| 13 | Thất Sát | Kim | Sát tinh |
| 14 | Phá Quân | Thủy | Hao tinh |

### B. Danh Sách 12 Cung

| # | Cung | Chi | Đại diện |
|---|------|-----|----------|
| 1 | Mệnh | (tùy lá số) | Bản thân |
| 2 | Phụ Mẫu | Mệnh+1 | Cha mẹ |
| 3 | Phúc Đức | Mệnh+2 | Phúc phần |
| 4 | Điền Trạch | Mệnh+3 | Nhà cửa |
| 5 | Quan Lộc | Mệnh+4 | Sự nghiệp |
| 6 | Nô Bộc | Mệnh+5 | Bạn bè |
| 7 | Thiên Di | Mệnh+6 | Di chuyển |
| 8 | Tật Ách | Mệnh+7 | Sức khỏe |
| 9 | Tài Bạch | Mệnh+8 | Tài chính |
| 10 | Tử Tức | Mệnh+9 | Con cái |
| 11 | Phu Thê | Mệnh+10 | Hôn nhân |
| 12 | Huynh Đệ | Mệnh+11 | Anh em |

### C. Bảng Tứ Hóa Nam Phái

| Can | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|-----|---------|-----------|----------|--------|
| Giáp | Liêm Trinh | Phá Quân | **Vũ Khúc** | Thái Dương |
| Ất | Thiên Cơ | Thiên Lương | Tử Vi | Thái Âm |
| Bính | Thiên Đồng | Thiên Cơ | Văn Xương | Liêm Trinh |
| Đinh | Thái Âm | Thiên Đồng | Thiên Cơ | Cự Môn |
| Mậu | Tham Lang | Thái Âm | Hữu Bật | Thiên Cơ |
| Kỷ | Vũ Khúc | Tham Lang | Thiên Lương | Văn Khúc |
| Canh | Thái Dương | Vũ Khúc | Thái Âm | Thiên Đồng |
| Tân | Cự Môn | Thái Dương | Văn Khúc | Văn Xương |
| Nhâm | Thiên Lương | Tử Vi | Tả Phù | Vũ Khúc |
| Quý | Phá Quân | Cự Môn | Thái Âm | Tham Lang |

---

*Tài liệu được tạo bởi Business Analyst - Phiên bản 1.0*

