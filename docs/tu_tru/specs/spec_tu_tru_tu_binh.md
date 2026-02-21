# ĐẶC TẢ KỸ THUẬT: DỰ ĐOÁN TỨ TRỤ (TỬ BÌNH) & CÔNG THỨC TÍNH TOÁN

**Ngày cập nhật:** 31/12/2024
**Trạng thái:** Draft/Implementation

---

## 1. TỔNG QUAN HỆ THỐNG
Tứ trụ (Bazi) là bộ môn mệnh lý dựa trên 4 trụ: **Năm - Tháng - Ngày - Giờ** sinh. Khác với Tử Vi dùng Âm lịch, Tứ Trụ dựa vào **Tiết Khí (Dương Lịch)** để xác định thời gian thực của vũ trụ.

---

## 2. CÔNG THỨC TÍNH 4 TRỤ (THE FOUR PILLARS FORMULAS)

### 2.1. Trụ Năm (Year Pillar)
Trong Tứ Trụ, năm bắt đầu từ tiết **Lập Xuân** (thường rơi vào ngày 4/2 hoặc 5/2 Dương lịch), **KHÔNG** phải Mùng 1 Tết Âm Lịch.

*   **Thiên Can Năm:**
    *   Công thức: `(Năm Dương Lịch - 3) % 10`
    *   Quy ước: 0=Quý, 1=Giáp, 2=Ất, 3=Bính, 4=Đinh, 5=Mậu, 6=Kỷ, 7=Canh, 8=Tân, 9=Nhâm.
    *   *Ví dụ:* 1984 - 3 = 1981; 1981 % 10 = 1 (Giáp).

*   **Địa Chi Năm:**
    *   Công thức: `(Năm Dương Lịch - 3) % 12`
    *   Quy ước: 1=Tý, 2=Sửu, ..., 12=Hợi (Hoặc 0=Hợi tùy cách đánh số).
    *   *Lưu ý:* Nếu ngày sinh < Lập Xuân của năm đó, thì vẫn tính là năm trước.
    *   *Ví dụ:* Sinh 01/02/1984 (chưa tới Lập Xuân 04/02) -> Tính là năm 1983 (Quý Hợi).

### 2.2. Trụ Tháng (Month Pillar)
Tháng trong Tứ Trụ cắt theo **12 Tiết Khí**, không phải lịch âm thông thường.

1.  **Xác định Chi Tháng (Lệnh Tháng):**
    *   Tháng Dần (1): Từ Lập Xuân đến Kinh Trập.
    *   Tháng Mão (2): Từ Kinh Trập đến Thanh Minh.
    *   Tháng Thìn (3): Từ Thanh Minh đến Lập Hạ.
    *   Tháng Tỵ (4): Từ Lập Hạ đến Mang Chủng.
    *   Tháng Ngọ (5): Từ Mang Chủng đến Tiểu Thử.
    *   Tháng Mùi (6): Từ Tiểu Thử đến Lập Thu.
    *   Tháng Thân (7): Từ Lập Thu đến Bạch Lộ.
    *   Tháng Dậu (8): Từ Bạch Lộ đến Hàn Lộ.
    *   Tháng Tuất (9): Từ Hàn Lộ đến Lập Đông.
    *   Tháng Hợi (10): Từ Lập Đông đến Đại Tuyết.
    *   Tháng Tý (11): Từ Đại Tuyết đến Tiểu Hàn.
    *   Tháng Sửu (12): Từ Tiểu Hàn đến Lập Xuân năm sau.

2.  **Xác định Can Tháng (Ngũ Dần Độn):**
    Dựa vào **Can Năm** để tìm Can của tháng Dần (tháng khởi đầu), sau đó đếm thuận.
    *   **Giáp / Kỷ** khởi **Bính** (Bính Dần).
    *   **Ất / Canh** khởi **Mậu** (Mậu Dần).
    *   **Bính / Tân** khởi **Canh** (Canh Dần).
    *   **Đinh / Nhâm** khởi **Nhâm** (Nhâm Dần).
    *   **Mậu / Quý** khởi **Giáp** (Giáp Dần).

### 2.3. Trụ Ngày (Day Pillar)
Đây là trụ khó tính nhẩm nhất vì chu kỳ 60 ngày quay vòng liên tục không phụ thuộc năm nhuận/thừa trừ. Cách chính xác nhất là dùng **Julian Day Number (JDN)**.

*   **Bước 1: Tính JDN từ ngày Dương Lịch (dd/mm/yyyy).**
    (Tham khảo thuật toán thiên văn học để đổi ngày Dương -> số JDN)

*   **Bước 2: Tính Can Chi Ngày từ JDN.**
    *   **Can Ngày** = `(JDN - 9) % 10` (Kết quả: 0=Giáp, ... 9=Quý - *Cần verify offset cụ thể với ngày mốc*).
        *   *Hiệu chỉnh:* Thường JDN tính từ trưa 12h, nếu tính từ 0h cần điều chỉnh +0.5 hoặc làm tròn.
        *   Công thức thực dụng: Lấy hiệu số ngày từ một mốc chuẩn (VD: 01/01/1900 là Giáp Tuất) chia dư cho 10 (Can) và 12 (Chi).
    *   **Chi Ngày** = `(JDN + 1) % 12` (Quy ước: 0=Tý, 1=Sửu...).

### 2.4. Trụ Giờ (Hour Pillar)

1.  **Xác định Chi Giờ:**
    *   23h-1h: Tý
    *   1h-3h: Sửu
    *   ...
    *   21h-23h: Hợi
    *   *Lưu ý:* Sau 23h được tính là đầu giờ Tý của **ngày hôm sau**.

2.  **Xác định Can Giờ (Ngũ Tý Độn):**
    Dựa vào **Can Ngày** để tìm Can của giờ Tý, sau đó đếm thuận.
    *   **Giáp / Kỷ** khởi **Giáp** (Giáp Tý).
    *   **Ất / Canh** khởi **Bính** (Bính Tý).
    *   **Bính / Tân** khởi **Mậu** (Mậu Tý).
    *   **Đinh / Nhâm** khởi **Canh** (Canh Tý).
    *   **Mậu / Quý** khởi **Nhâm** (Nhâm Tý).

---

## 3. TÍNH TOÁN CÁC THẦN SÁT & VÒNG TRƯỜNG SINH

### 3.1. Vòng Trường Sinh (12 giai đoạn)
Dựa vào **Can Ngày** (Nhật Chủ) so với **Chi** (Năm/Tháng/Ngày/Giờ).
*   Thứ tự: Trường Sinh > Mộc Dục > Quan Đới > Lâm Quan > Đế Vượng > Suy > Bệnh > Tử > Mộ > Tuyệt > Thai > Dưỡng.
*   Cần bảng tra sinh vượng tử tuyệt cho 10 Thiên Can. (Dương sinh Âm tử, Âm sinh Dương tử).

### 3.2. Xác định Thập Thần (10 Gods)
Mối quan hệ khắc/sinh giữa **Can Ngày** và các Can/Chi khác.
*   Sinh ta: Chính Ấn (khác dấu), Thiên Ấn (cùng dấu).
*   Ta sinh: Thực Thần (cùng), Thương Quan (khác).
*   Khắc ta: Chính Quan (khác), Thiên Quan (Sát - cùng).
*   Ta khắc: Chính Tài (khác), Thiên Tài (cùng).
*   Cùng ta: Tỷ Thần (cùng), Kiếp Tài (khác).

---

## 4. DỤNG THẦN (USEFUL GOD)
*   **Bước 1:** Tính độ vượng của Nhật Chủ (Đắc lệnh tháng? Đắc địa? Đắc sinh?).
*   **Bước 2:** Xác định Thân Vượng hay Thân Nhược.
*   **Bước 3:** Chọn Dụng thần để cân bằng:
    *   Thân Vượng: Cần Khắc (Quan/Sát), Xì hơi (Thực/Thương), hoặc Hao (Tài).
    *   Thân Nhược: Cần Sinh (Ấn), Trợ (Tỷ/Kiếp).
    *   (Ngoại cách: Tòng vượng, Tòng nhược - xét riêng).

---

## 5. BẢNG DỮ LIỆU THAM CHIẾU (MASTER TABLES)

### 5.1. Bảng 24 Tiết Khí Dùng Cho Tứ Trụ
*Lưu ý: Ngày bắt đầu có thể xê dịch +/- 1 ngày tùy năm. Cần dùng thư viện thiên văn để tính chính xác.*

| Tháng Tứ Trụ | Tiết Khí Đầu (Bắt đầu tháng) | Ngày Dương Lịch (Xấp xỉ) | Kinh Độ Mặt Trời | Tiết Khí Giữa (Giữa tháng) |
|---|---|---|---|---|
| **Dần (1)** | Lập Xuân | 04/02 | 315° | Vũ Thủy |
| **Mão (2)** | Kinh Trập | 06/03 | 345° | Xuân Phân |
| **Thìn (3)** | Thanh Minh | 05/04 | 15° | Cốc Vũ |
| **Tỵ (4)** | Lập Hạ | 06/05 | 45° | Tiểu Mãn |
| **Ngọ (5)** | Mang Chủng | 06/06 | 75° | Hạ Chí |
| **Mùi (6)** | Tiểu Thử | 07/07 | 105° | Đại Thử |
| **Thân (7)** | Lập Thu | 08/08 | 135° | Xử Thử |
| **Dậu (8)** | Bạch Lộ | 08/09 | 165° | Thu Phân |
| **Tuất (9)** | Hàn Lộ | 08/10 | 195° | Sương Giáng |
| **Hợi (10)** | Lập Đông | 07/11 | 225° | Tiểu Tuyết |
| **Tý (11)** | Đại Tuyết | 07/12 | 255° | Đông Chí |
| **Sửu (12)** | Tiểu Hàn | 06/01 | 285° | Đại Hàn |

### 5.2. Bảng Tàng Can (Hidden Stems In Branches)
Dùng để tính định lượng ngũ hành và xác định Thân Vượng/Nhược.

| Địa Chi | Tàng Can Chính (Bản khí) | Tàng Can Phụ (Trung khí) | Tàng Can Phụ (Dư khí) | Ghi chú |
|---|---|---|---|---|
| **Tý (Thủy)** | Quý (100%) | - | - | Thủy vượng |
| **Sửu (Thổ)** | Kỷ (60%) | Quý (20%) | Tân (20%) | Mộ của Kim |
| **Dần (Mộc)** | Giáp (60%) | Bính (20%) | Mậu (20%) | Sinh của Hỏa |
| **Mão (Mộc)** | Ất (100%) | - | - | Mộc vượng |
| **Thìn (Thổ)** | Mậu (60%) | Quý (20%) | Ất (20%) | Mộ của Thủy |
| **Tỵ (Hỏa)** | Bính (60%) | Mậu (20%) | Canh (20%) | Sinh của Kim |
| **Ngọ (Hỏa)** | Đinh (70%) | Kỷ (30%) | - | Hỏa vượng |
| **Mùi (Thổ)** | Kỷ (60%) | Đinh (20%) | Ất (20%) | Mộ của Mộc |
| **Thân (Kim)** | Canh (60%) | Nhâm (20%) | Mậu (20%) | Sinh của Thủy |
| **Dậu (Kim)** | Tân (100%) | - | - | Kim vượng |
| **Tuất (Thổ)** | Mậu (60%) | Tân (20%) | Đinh (20%) | Mộ của Hỏa |
| **Hợi (Thủy)** | Nhâm (60%) | Giáp (40%) | - | Sinh của Mộc |

### 5.3. Bảng Vòng Trường Sinh (Life Cycle)
Tra cứu theo **Can Ngày (Nhật Chủ)** (Hàng ngang) so với **Chi** (Hàng dọc).
*Viết tắt: TS (Trường Sinh), MD (Mộc Dục), QĐ (Quan Đới), LQ (Lâm Quan), ĐV (Đế Vượng), S (Suy), B (Bệnh), T (Tử), M (Mộ), Tu (Tuyệt), Th (Thai), D (Dưỡng).*

| Chi / Nhật Chủ | Giáp | Bính | Mậu | Canh | Nhâm | Ất | Đinh | Kỷ | Tân | Quý |
|---|---|---|---|---|---|---|---|---|---|---|
| **Hợi** | **TS** | Tu | Tu | B | LQ | T | Th | Th | MD | ĐV |
| **Tý** | MD | Th | Th | T | ĐV | B | Tu | Tu | TS | LQ |
| **Sửu** | QĐ | D | D | M | S | S | M | M | D | QĐ |
| **Dần** | LQ | **TS** | **TS** | Tu | B | ĐV | T | T | Th | MD |
| **Mão** | ĐV | MD | MD | Th | T | LQ | B | B | Tu | TS |
| **Thìn** | S | QĐ | QĐ | D | M | M | S | S | QĐ | D |
| **Tỵ** | B | LQ | LQ | **TS** | Tu | Tu | ĐV | ĐV | T | Th |
| **Ngọ** | T | ĐV | ĐV | MD | Th | **TS** | LQ | LQ | B | Tu |
| **Mùi** | M | S | S | QĐ | D | D | QĐ | QĐ | S | M |
| **Thân** | Tu | B | B | LQ | **TS** | Th | T | T | ĐV | MD |
| **Dậu** | Th | T | T | ĐV | MD | Tu | TS | TS | LQ | B |
| **Tuất** | D | M | M | S | QĐ | QĐ | D | D | M | S |

---

---

## 6. ĐỊNH NGHĨA BIẾN & ENUM (CODE DEFINITIONS)

Để đảm bảo tính nhất quán khi lập trình (nhất là khi dùng Python/Enum), sử dụng các định nghĩa sau:

### 6.1. Thiên Can (Heavenly Stems) Enum
*   **Value:** 0-9
*   **Attributes:**
    *   `name`: Tên tiếng Việt (Giáp, Ất...)
    *   `element`: Ngũ hành (Mộc, Hỏa...)
    *   `yin_yang`: Âm/Dương (0=Dương, 1=Âm hoặc True/False)

| Index | Name | Element | Yin/Yang |
|---|---|---|---|
| 0 | Giáp (Jia) | Mộc | Dương |
| 1 | Ất (Yi) | Mộc | Âm |
| 2 | Bính (Bing) | Hỏa | Dương |
| 3 | Đinh (Ding) | Hỏa | Âm |
| 4 | Mậu (Wu) | Thổ | Dương |
| 5 | Kỷ (Ji) | Thổ | Âm |
| 6 | Canh (Geng) | Kim | Dương |
| 7 | Tân (Xin) | Kim | Âm |
| 8 | Nhâm (Ren) | Thủy | Dương |
| 9 | Quý (Gui) | Thủy | Âm |

### 6.2. Địa Chi (Earthly Branches) Enum
*   **Value:** 0-11 (Lưu ý: Index 0 thường là Tý, nhưng tháng Tứ Trụ khởi từ Dần (2). Cần cẩn thận offset).
*   **Attributes:**
    *   `name`: Tên (Tý, Sửu...)
    *   `element`: Ngũ hành chính (Bản khí)
    *   `hidden_stems`: List[Stem] (Tàng can)

| Index | Name | Element |
|---|---|---|
| 0 | Tý (Zi) | Thủy |
| 1 | Sửu (Chou) | Thổ |
| 2 | Dần (Yin) | Mộc |
| 3 | Mão (Mao) | Mộc |
| 4 | Thìn (Chen) | Thổ |
| 5 | Tỵ (Si) | Hỏa |
| 6 | Ngọ (Wu) | Hỏa |
| 7 | Mùi (Wei) | Thổ |
| 8 | Thân (Shen) | Kim |
| 9 | Dậu (You) | Kim |
| 10 | Tuất (Xu) | Thổ |
| 11 | Hợi (Hai) | Thủy |

### 6.3. Thập Thần (10 Gods) Mapping
*   **Input:** Nhật Chủ (Day Stem) vs Can Khác (Other Stem).
*   **Logic:** So sánh Sinh/Khắc và cùng/khác dấu.

| Code | Tên | Logic (So với Nhật Chủ) |
|---|---|---|
| **TyKien** | Tỷ Kiên | Cùng hành, Cùng dấu |
| **KiepTai** | Kiếp Tài | Cùng hành, Khác dấu |
| **ThucThan** | Thực Thần | Ta sinh, Cùng dấu |
| **ThuongQuan**| Thương Quan | Ta sinh, Khác dấu |
| **ChinhTai** | Chính Tài | Ta khắc, Khác dấu |
| **ThienTai** | Thiên Tài | Ta khắc, Cùng dấu |
| **ChinhQuan** | Chính Quan | Khắc ta, Khác dấu |
| **ThienQuan** | Thiên Quan (Sát)| Khắc ta, Cùng dấu |
| **ChinhAn** | Chính Ấn | Sinh ta, Khác dấu |
| **ThienAn** | Thiên Ấn (Kiêu)| Sinh ta, Cùng dấu |

---

## 7. PHỤ LỤC: BẢNG TRA CAN CHI THÁNG & GIỜ



### Ngũ Dần Độn (Tìm Tháng Dần đầu năm)
| Can Năm | Giáp/Kỷ | Ất/Canh | Bính/Tân | Đinh/Nhâm | Mậu/Quý |
|---------|---------|---------|----------|-----------|---------|
| Tháng Dần | Bính | Mậu | Canh | Nhâm | Giáp |

### Ngũ Tý Độn (Tìm Giờ Tý đầu ngày)
| Can Ngày | Giáp/Kỷ | Ất/Canh | Bính/Tân | Đinh/Nhâm | Mậu/Quý |
|----------|---------|---------|----------|-----------|---------|
| Giờ Tý | Giáp | Bính | Mậu | Canh | Nhâm |
