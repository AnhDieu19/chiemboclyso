# KẾ HOẠCH & CHECKLIST "VÒNG LẶP CHẤT LƯỢNG" - TỨ TRỤ (TU TRU SPEC)
**Module:** Tứ Trụ Tử Bình (Tu Tru / Bazi)
**Mục tiêu:** Đạt điểm chất lượng 10/10 cho đặc tả kỹ thuật, phục vụ trực tiếp cho việc Lập trình (Ready-to-code).

---

## 1. TIÊU CHUẨN ĐÁNH GIÁ 10/10 (CHECKLIST)

Một đặc tả "Ready-to-code" cần đạt được các tiêu chuẩn sau:

| STT | Tiêu chí | Trọng số | Yêu cầu chi tiết |
|-----|----------|----------|------------------|
| 1 | **Master Data Tables** | 3.0 | **Bảng dữ liệu hằng số (Constants):**<br>- 24 Tiết Khí (độ số, ngày chuẩn).<br>- Tàng Can (Hidden Stems) của 12 Chi.<br>- Sinh/Vượng/Mộ (Vòng Trường Sinh).<br>- Ngũ hành sinh khắc. |
| 2 | **Definitions for Code** | 2.0 | **Định nghĩa biến (Variables):**<br>- Định nghĩa rõ input/output cho từng khái niệm (Thân vượng, Nhật chủ...).<br>- Kiểu dữ liệu (Enum, Int, String). |
| 3 | **Thuật toán (Logic)** | 3.0 | **Pseudo-code hoặc Logic Flow:**<br>- Xử lý điểm biên (Edge cases): Sinh đúng giờ giao tiết, sinh sớm/muộn.<br>- Ngũ Dần/Ngũ Tý độn.<br>- Logic tính Thần Sát. |
| 4 | **Test Cases** | 2.0 | **Bộ dữ liệu kiểm thử:**<br>- Ít nhất 3 ví dụ lá số chuẩn (Input đầy đủ -> Output 4 trụ đúng). |

**Tổng điểm: 10.0**

---

## 2. ĐÁNH GIÁ VÒNG 1 (CURRENT STATUS)

**Tài liệu:** `docs/tu_tru/specs/spec_tu_tru_tu_binh.md`

| Tiêu chí | Điểm chấm | Nhận xét (Gaps) |
|----------|-----------|-----------------|
| 1. Master Tables | 1.0 / 3.0 | Đã có bảng Ngũ Dần/Ngũ Tý. **Thiếu:** Bảng Tàng Can, Bảng Tiết Khí chi tiết (độ số), Vòng Trường Sinh. |
| 2. Definitions | 1.0 / 2.0 | Mô tả văn bản tốt, nhưng chưa map sang biến/enum cho dev. |
| 3. Logic | 2.5 / 3.0 | Đã có công thức tính JDN, Năm, Tháng. Tương đối ổn. |
| 4. Test Cases | 0.0 / 2.0 | **Chưa có ví dụ mẫu** để verify công thức. |

**TỔNG ĐIỂM: 4.5 / 10**

---

## 3. KẾ HOẠCH VÒNG LẶP (EXECUTION PLAN)

### Loop 1: Bổ sung Master Data (Target: 4.5 -> 7.5)
*   **Nhiệm vụ:**
    *   Thêm bảng **24 Tiết Khí** (Mốc thời gian, Góc mặt trời).
    *   Thêm bảng **Địa Chi Tàng Can** (quan trọng nhất để tính Thân vượng).
    *   Thêm bảng **Vòng Trường Sinh** (Sinh, Vượng, Mộ...).

### Loop 2: Định nghĩa Code & Logic chi tiết (Target: 7.5 -> 9.0)
*   **Nhiệm vụ:**
    *   Định nghĩa Enum (Can, Chi, WuXing).
    *   Làm rõ logic tính "Độ vượng" (Mức độ 1-100 hay Thang đo?).

### Loop 3: Test Cases & Review (Target: 9.0 -> 10.0)
*   **Nhiệm vụ:**
    *   Thêm section "Ví dụ minh họa" (Case Study thực tế).
    *   Rà soát lần cuối toàn bộ logic.
