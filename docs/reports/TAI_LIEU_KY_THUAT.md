# TÀI LIỆU KỸ THUẬT DỰ ÁN TỬ VI ĐẨU SỐ (TECHNICAL DOCUMENTATION)

**Ngày cập nhật:** 20/12/2025
**Phiên bản:** 1.0.0
**Ngôn ngữ lập trình:** Python 3.x (Backend), HTML/JS (Frontend)
**Framework:** Flask

---

## 1. TỔNG QUAN HỆ THỐNG
Dự án là một ứng dụng web tính toán và giải đoán lá số Tử Vi Đẩu Số (Nam Phái). Hệ thống được thiết kế theo kiến trúc Modular, tách biệt rõ ràng giữa các tầng dữ liệu (Data), tính toán cốt lõi (Core), logic an sao (Stars Placer) và giao diện người dùng (Presentation).

Mục tiêu chính:
1.  Lập lá số Tử Vi chính xác dựa trên ngày giờ sinh (Dương lịch/Âm lịch).
2.  Cung cấp công cụ tìm ngược giờ sinh (Reverse Lookup) dựa trên đặc điểm và sự kiện cuộc đời.
3.  Tính toán độ miếu hãm, năng lượng ngũ hành và các hạn (Đại vận, Lưu niên).

---

## 2. CẤU TRÚC THƯ MỤC VÀ MÔ ĐUN

Hệ thống mã nguồn được tổ chức trong thư mục `python/` như sau:

### 2.1. Tầng Dữ Liệu (`data/`)
Chứa các hằng số, bảng tra cứu và định nghĩa dữ liệu tĩnh.
*   `__init__.py`: Export các hằng số dùng chung.
*   `can_chi.py`: Định nghĩa 10 Thiên Can, 12 Địa Chi, Ngũ Hành, Nạp Âm.
*   `cung_cuc.py`: Tên 12 Cung chức năng, bảng an Cục (Thủy Nhị Cục, Mộc Tam Cục...).
*   `chinh_tinh.py`: Quy tắc an 14 Chính tinh (Vòng Tử Vi, Vòng Thiên Phủ).
*   `star_brightness.py`: Bảng tra cứu độ sáng của sao (Miếu, Vượng, Đắc, Bình, Hãm) tại 12 cung.
*   `phu_tinh_*.py`: Các nhóm phụ tinh (Lục Sát, Lục Cát, Thái Tuế, Tràng Sinh, Tuần Triệt...).
*   `meanings/*.json`: Hệ thống cơ sở dữ liệu ý nghĩa luận giải chi tiết:
    *   `chinh_tinh.json`: Ý nghĩa 14 chính tinh (bổ sung vị trí đắc hãm 12 cung, nghề nghiệp, tính cách).
    *   `phu_tinh.json`: Ý nghĩa các phụ tinh (bao gồm bộ Thái Tuế: Thái Tuế, Bạch Hổ, Quan Phù).
    *   `dai_van.json`: Luận giải ý nghĩa các Đại Vận (bổ sung Vòng Thái Tuế).
    *   `nhan_tuong.json`: Dữ liệu Nhân Tướng Học (Diện tướng, Thủ tướng, Dâm tướng, Ý nghĩa đeo nhẫn).

### 2.2. Tầng Tính Toán Cốt Lõi (`core/`)
Chịu trách nhiệm xử lý các phép tính toàn học và thiên văn cơ bản.
*   `lunar_converter.py`: Thuật toán chuyển đổi Dương lịch sang Âm lịch (Dựa trên thuật toán Hồ Ngọc Đức), tính ngày Sóc, tiết khí.
*   `can_chi_calc.py`: Tính Can/Chi cho Năm, Tháng, Ngày, Giờ.
*   `cung_menh.py`: Xác định vị trí cung Mệnh, Thân dựa trên Tháng và Giờ sinh.
*   `cuc_calc.py`: Xác định Cục của lá số (Dựa trên Can cung Mệnh và vị trí cung).
*   `fortune_periods.py`: Tính khởi Đại Vận (theo Cục và giới tính/âm dương năm sinh).

### 2.3. Tầng Logic An Sao (`stars/`)
Chứa các lớp/hàm đặt sao vào các cung cụ thể.
*   `chinh_tinh_placer.py`: An 14 chính tinh.
*   `luc_sat_placer.py`: An Kính Dương, Đà La, Địa Không, Địa Kiếp, Hỏa Tinh, Linh Tinh.
*   `luc_cat_placer.py`: An Tả Phù, Hữu Bật, Văn Xương, Văn Khúc, Thiên Khôi, Thiên Việt.
*   `tuan_triet_placer.py`: Tính vị trí Tuần Trung Vong và Triệt Lộ Không Vong.
*   `tu_hoa_applier.py`: Tính Tứ Hóa (Lộc, Quyền, Khoa, Kỵ) theo Can năm sinh (cho lá số gốc) hoặc Can hạn (cho Lưu niên).
*   `bo_sung_placer.py`: An các tạp tinh và sao nhỏ khác.

### 2.4. Tầng Logic Nghiệp Vụ (`logic/`)
*   `reverse_lookup_engine.py`: Engine tìm kiếm lá số ngược. Bao gồm thuật toán chấm điểm (Scoring), xếp hạng thành công (Success Ranking) và phân tích dòng thời gian (Timeline Analysis).
*   `candidate_finder.py`: Logic cũ (đã được thay thế/bổ trợ bởi engine mới).

### 2.5. Ứng Dụng Chính (`app.py`)
*   Khởi tạo Flask server.
*   Định nghĩa các API endpoints (`/api/generate`, `/api/finder/solve`).
*   Render các trang HTML (`index.html`, `finder.html`).

---

## 2.6. API ENDPOINTS

### `/api/finder/solve` (POST)
Tìm kiếm lá số ngược dựa trên đặc điểm và sự kiện.

**Request Body:**
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

**Response (200 OK):**
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

## 3. QUY TRÌNH THUẬT TOÁN LẬP LÁ SỐ (CHART GENERATION FLOW)

Quy trình lập lá số được thực hiện tuần tự qua các bước sau trong `chart/chart_builder.py` (hoặc tương đương):

### Bước 1: Chuẩn hóa Đầu vào
1.  Người dùng nhập Ngày, Tháng, Năm (Dương lịch hoặc Âm lịch) và Giờ sinh.
2.  Nếu là Dương lịch, gọi `core.lunar_converter.solar_to_lunar` để lấy Ngày/Tháng/Năm Âm lịch.
3.  Xác định Can Chi cho Năm, Tháng, Ngày, Giờ sử dụng `core.can_chi_calc`.

### Bước 2: An Cung Mệnh và Cung Thân
1.  Khởi tại cung Dần là tháng 1.
2.  **Cung Mệnh**: Từ cung Dần, đếm thuận đến tháng sinh, rồi đếm nghịch đến giờ sinh.
3.  **Cung Thân**: Từ cung Dần, đếm thuận đến tháng sinh, rồi đếm thuận tiếp đến giờ sinh.
4.  An tên 12 cung chức năng (Phụ Mẫu, Phúc Đức...) chạy nghịch chiều kim đồng hồ từ cung Mệnh.

### Bước 3: Định Cục (Element Configuration)
1.  Lấy Thiên Can của cung Mệnh (dựa trên Ngũ Hổ Độn: từ Can năm sinh tìm Can tháng Dần, rồi đếm thuận tới cung Mệnh).
2.  Kết hợp Can cung Mệnh và Chi cung Mệnh để tra bảng `data.cung_cuc.CUC_TABLE`.
3.  Kết quả là Cục (ví dụ: Kim Tứ Cục, Hỏa Lục Cục...).

### Bước 4: An Chính Tinh (14 Sao)
1.  **Vòng Tử Vi**: Dựa vào Cục và Ngày sinh.
    *   Công thức: (Ngày sinh + X) / Cục (Chi tiết trong `stars.chinh_tinh_placer`).
2.  **Vòng Thiên Phủ**: Vị trí Thiên Phủ đối xứng với Tử Vi qua trục Dần - Thân.
3.  An các sao còn lại trong 2 vòng dựa vào vị trí Tử Vi và Thiên Phủ.

### Bước 5: An Phụ Tinh và Tứ Hóa
1.  An Tuần (dựa trên Can Chi năm) và Triệt (dựa trên Can năm).
2.  An Lục Sát Tinh, Lục Cát Tinh, Vòng Thái Tuế, Vòng Tràng Sinh, Vòng Bác Sỹ.
3.  An Tứ Hóa theo Can của Năm sinh.
4.  Tra cứu độ sáng (Miếu/Hãm) cho tất cả các sao từ `data.star_brightness`.

### Bước 6: Tính Đại Vận và Lưu Niên
1.  **Đại Vận (10 năm)**: Khởi từ cung Mệnh.
    *   Dương Nam/Âm Nữ: Đi thuận.
    *   Âm Nam/Dương Nữ: Đi nghịch.
    *   Số bắt đầu chính là số Cục (Ví dụ Thủy Nhị Cục bắt đầu từ 2 tuổi).
2.  **Lưu Niên (Tiểu Vận/Lưu Thái Tuế)**: Tính vị trí của năm xem hạn trên lá số.

---

## 4. CHI TIẾT THUẬT TOÁN TÍNH ĐIỂM "CÁCH CỤC" (SUCCESS SCORE)

Tính năng này nằm trong `logic.reverse_lookup_engine`. Mục chiêu là định lượng chất lượng lá số trên thang điểm 100.

**Công thức tổng quát:**
`Điểm = Tổng(Trọng số Cung * Điểm Cung)`

**Trọng số Cung:**
*   Mệnh: 40%
*   Thân: 30%
*   Tài Bạch: 15%
*   Quan Lộc: 15%

**Cách tính điểm thành phần trong một cung:**
1.  **Chính Tinh**:
    *   Miếu địa: +10 điểm
    *   Vượng địa: +8 điểm
    *   Đắc địa: +5 điểm
    *   Bình hòa: +2 điểm
    *   Hãm địa: -5 điểm
2.  **Phụ Tinh (Bonus)**:
    *   Hóa Lộc, Hóa Quyền, Hóa Khoa: Điểm cộng lớn (gọi là Tam Hóa Liên Châu hoặc Khoa Quyền Lộc).
    *   Lộc Tồn: Cộng điểm tài lộc.
    *   Khôi, Việt, Tả, Hữu: Cộng điểm quý nhân.
3.  **Sát Tinh (Penalty)**:
    *   Địa Không, Địa Kiếp (Hãm): Trừ điểm nặng (nhân hệ số phạt 0.7).
    *   Kình Dương, Đà La (Hãm): Trừ điểm.
4.  **Tuần/Triệt**:
    *   Nếu cung bị Tuần/Triệt: Tổng điểm cung giảm 20% (nhân 0.8).

**Phân loại (Ranking Class):**
*   Điểm >= 80: Số Tỷ Phú / Đại Quý Cách (Hạng S)
*   Điểm >= 65: Số Quan Chức / Khá Giả (Hạng A)
*   Điểm >= 50: Bình Thường (Hạng B)
*   Điểm < 50: Vất Vả (Hạng C)

---

## 5. BẢO MẬT VÀ KIỂM THỬ
*   Mã nguồn không chứa các hard-coded credentials.
*   Dữ liệu đầu vào từ người dùng (Năm, Tháng, Ngày, Giờ) được validate kiểu dữ liệu (integer) trước khi xử lý.
*   Hệ thống có cơ chế try-catch tại các endpoint API để tránh crash server khi gặp lỗi tính toán logic.

---
**Tài liệu này dùng cho mục đích Audit kỹ thuật. Vui lòng không sao chép hoặc phát tán ra ngoài dự án.**
