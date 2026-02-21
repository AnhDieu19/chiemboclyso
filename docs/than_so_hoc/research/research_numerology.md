# NGHIÊN CỨU & KẾ HOẠCH: THẦN SỐ HỌC PHƯƠNG TÂY (WESTERN NUMEROLOGY)

**Ngày tạo:** 31/12/2024
**Trạng thái:** Draft

---

## 1. TỔNG QUAN
Thần số học (Numerology) phương Tây, chủ yếu dựa trên hệ thống Pythagoras, nghiên cứu ý nghĩa năng lượng của các con số gắn liền với Họ Tên và Ngày Sinh của một người.

### 1.1. Mục tiêu
Xây dựng module Thần Số Học có khả năng:
- Tính toán các chỉ số cốt lõi từ Họ Tên và Ngày Sinh.
- Xuất báo cáo luận giải tính cách, điểm mạnh, điểm yếu, và dự báo vận hạn (Năm/Tháng/Ngày cá nhân).
- Vẽ biểu đồ ngày sinh (Birth Chart) và biểu đồ tên (Name Chart).

---

## 2. CƠ SỞ LÝ THUYẾT & TÍNH TOÁN

### 2.1. Hệ thống quy đổi chữ cái (Pythagorean System)
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|
| A | B | C | D | E | F | G | H | I |
| J | K | L | M | N | O | P | Q | R |
| S | T | U | V | W | X | Y | Z |   |

### 2.2. Các Chỉ Số Cốt Lõi (Core Numbers)

1.  **Số Chủ Đạo / Đường Đời (Life Path Number):**
    - *Công thức:* Cộng tất cả các chữ số trong ngày tháng năm sinh (dd/mm/yyyy) lại cho đến khi còn 1 chữ số (hoặc là các số Master 11, 22, 33).
    - *Ý nghĩa:* Bài học lớn nhất, mục đích sống, thiên hướng tự nhiên.

2.  **Số Sứ Mệnh / Vận Mệnh (Destiny / Expression Number):**
    - *Công thức:* Cộng giá trị của TẤT CẢ các chữ cái trong Họ Tên đầy đủ.
    - *Ý nghĩa:* Năng lực tiềm ẩn, khả năng đạt được mục tiêu.

3.  **Số Linh Hồn (Soul Urge / Heart's Desire Number):**
    - *Công thức:* Cộng giá trị của CÁC NGUYÊN ÂM trong Họ Tên.
    - *Ý nghĩa:* Khao khát thầm kín, động lực bên trong.

4.  **Số Nhân Cách / Tương Tác (Personality Number):**
    - *Công thức:* Cộng giá trị của CÁC PHỤ ÂM trong Họ Tên.
    - *Ý nghĩa:* Cách người khác nhìn nhận bạn, "mặt nạ" xã hội.

5.  **Số Ngày Sinh (Birthday Number):**
    - *Công thức:* Tổng các chữ số ngày sinh.
    - *Ý nghĩa:* Tài năng phụ trợ.

6.  **Số Trưởng Thành (Maturity Number):**
    - *Công thức:* (Life Path + Name Number) rút gọn.
    - *Ý nghĩa:* Xu hướng phát triển sau tuổi 40.

### 2.3. Các Chỉ Số Dự Báo (Forecasting)

1.  **Năm Cá Nhân (Personal Year):**
    - *Công thức:* (Ngày sinh + Tháng sinh + Năm hiện tại) -> rút gọn 1-9.
    - *Ý nghĩa:* Vận hạn, chủ đề của năm đó.

2.  **Tháng Cá Nhân (Personal Month):**
    - *Công thức:* (Năm cá nhân + Tháng hiện tại) -> rút gọn.

3.  **Chu Kỳ 9 Năm (9 Year Cycle):**
    - Sóng phát triển của đời người theo chu kỳ 9 năm.

---

## 3. KẾ HOẠCH PHÁT TRIỂN (IMPLEMENTATION PLAN)

### Giai đoạn 1: Core Engine (Python)
- **Module:** `python/core/numerology_engine.py` (Mới)
- **Chức năng:**
    - Hàm xử lý chuỗi: Chuẩn hóa họ tên, xóa dấu tiếng Việt (để map sang bảng chữ cái tiếng Anh - *Lưu ý: Cần confirm quy tắc xử lý tên tiếng Việt, thường là bỏ dấu rồi tính*).
    - Hàm tính toán: `calculate_life_path`, `calculate_expression`, `calculate_personal_year`...
    - Class `NumerologyProfile`.

### Giai đoạn 2: API & Data
- **API:** Endpoint `/api/numerology/calculate` nhận input (Name, DOB) trả về JSON kq.
- **Data Content:** File JSON chứa nội dung luận giải cho từng con số (1-9, 11, 22, 33) ở từng vị trí (Life Path, Soul Urge...).

### Giai đoạn 3: Frontend (Web/App)
- UI nhập liệu Name - DOB.
- Hiển thị các chỉ số đẹp mắt.
- Vẽ biểu đồ (Grid 3x3).

---

## 4. QUY TẮC MAPPING KÝ TỰ (Notes)
- **Y:**
    - Y là Nguyên âm khi: Đứng riêng (Ly), đi sau phụ âm (Thy), đi cuối âm tiết không có nguyên âm khác (Mary).
    - Y là Phụ âm khi: Đi đầu (Yến), đi cạnh nguyên âm khác đóng vai trò chính (Mai - y dài k có trong này nhưng ví dụ 'Yacht').
    - *Trong tiếng Việt:* Y thường được coi là Nguyễn Âm (Ly, Mỹ, Ý) hoặc Phụ Âm (Yến). Cần logic check kỹ.
