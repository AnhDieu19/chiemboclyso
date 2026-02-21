# Cơ Sở Toán Học của Ngũ Hành (Wuxing)

## Kết Luận

Theo các nghiên cứu toán học hiện đại, "cơ sở toán học" rõ nhất của ngũ hành là: một **mạng 5 tác nhân (5-agent network)** đặt trên ngũ giác, với hai kiểu liên kết (tương sinh = hợp tác, tương khắc = đối kháng), mô tả bằng **đồ thị + ma trận** (đặc biệt là ma trận tuần hoàn/circulant) và phân tích bằng **giá trị riêng (eigenvalues)** để xét ổn định/cân bằng.

Trong mô hình hóa kiểu này, **tỉ lệ vàng** xuất hiện tự nhiên do đối xứng ngũ giác và điều kiện ổn định có thể cho ra ngưỡng:

```
(a + b) / (c + d) = φ²
```

---

## Facts (Dữ kiện)

1. Ngũ hành thường được mô tả bằng hai chu trình: **tương sinh** và **tương khắc** (hợp tác vs đối kháng)

2. Bài Scientific Reports (Nature) mô hình hóa Wuxing network như 5 tác nhân ở 5 đỉnh ngũ giác:
   - Kề nhau → hợp tác
   - Cách một đỉnh → đối kháng
   - Lập mô hình tuyến tính: `Ẋ = A₅X`
   - Dùng giá trị riêng để xét ổn định
   - Điều kiện biên ổn định: `(a+b)/(c+d) = φ²`

3. Bài Springer (2025) tiếp tục hướng "mạng 5 tác nhân" và nhấn mạnh **eigenstructure analysis** để diễn giải cơ chế phản hồi/cân bằng (trong bối cảnh TCM)

4. Về toán thuần: cấu trúc "đi quanh 5 trạng thái" khớp tự nhiên với nhóm cyclic **Z₅** (cộng modulo 5)

5. Tỉ lệ vàng gắn chặt với ngũ giác đều (đường chéo/cạnh tạo ra φ)

---

## Phân Tích Theo Khung

### 3 Lớp Toán

| Lớp | Mô tả |
|-----|-------|
| Cấu trúc rời rạc | 5 trạng thái + hai kiểu "bước chuyển" (sinh/khắc) |
| Đại số tuyến tính | Mã hóa quan hệ thành ma trận tuần hoàn, dùng phổ (eigenvalues) |
| Động lực học/điều khiển | "Cân bằng" = ổn định, "hài hòa" = trạng thái biên/dao động/hội tụ |

---

## Các Option Mô Hình Hóa

### Option 1: Nhóm Z₅ + Đồ thị (Graph)

Gán 5 hành vào các số `0, 1, 2, 3, 4`:

```
Tương sinh: i ↦ i + 1 (mod 5)  // đi thêm 1
Tương khắc: i ↦ i + 2 (mod 5)  // đi thêm 2
```

**Ưu điểm:** Cực gọn, giải thích "vì sao 5" và hai vòng sinh/khắc rất sạch  
**Nhược điểm:** Chưa nói được "ổn định/cân bằng" định lượng

### Option 2: Ma trận tuần hoàn (Circulant) + Eigenvalues

Gán trọng số:
- Cạnh kề (sinh/hợp tác): trọng số dương `a, b`
- Đường chéo (khắc/đối kháng): trọng số âm `-c, -d`

Động lực tuyến tính:
```
Ẋ = A₅X
```

Dùng **dominant eigenvalue** để kết luận ổn định. Điều kiện biên:
```
(a + b) / (c + d) = φ²
```

**Ưu điểm:** Cho ra điều kiện định lượng  
**Nhược điểm:** Phụ thuộc cách gán trọng số và phương trình động lực

### Option 3: Mạng đa tác nhân (Multi-agent) trong Điều khiển

- "Hợp tác" kéo hệ về đồng thuận/ổn định
- "Đối kháng" tạo xu hướng phân kỳ/dao động
- Công cụ: ma trận đồ thị và phân tích phổ (Laplacian/eigenvalues)

---

## Khuyến Nghị

**MVP tốt nhất cho "cơ sở toán học" theo nghiên cứu hiện đại:**

> Graph 5 đỉnh + Ma trận tuần hoàn + Eigenvalues

(Đúng tinh thần các bài Nature/Springer)

---

## Rủi Ro & Kiểm Thử

| Rủi ro | Cách kiểm |
|--------|-----------|
| Gán ghép: đổi cách gán trọng số → kết luận khác | Công khai đúng A₅, chạy mô phỏng, kiểm tra độ nhạy tham số |
| "Tỉ lệ vàng" bị hiểu sai: xuất hiện tự nhiên do ngũ giác, không "chứng minh" mọi ứng dụng | Tách bạch "toán của mô hình" vs "diễn giải" |

---

## Tham Khảo

- Scientific Reports (Nature) - Wuxing network model
- Springer (2025) - Five-agent network eigenstructure analysis  
- MathWorld - Pentagon geometry and golden ratio
- Clemson Math - Cyclic groups Z₅

---

## Ngũ Hành và Thiên Văn Học

### Ngũ Tinh (5 Hành Tinh Cổ Điển)

| Hành | Hành Tinh | Tên Hán | Chu Kỳ Quỹ Đạo | Ghi Chú |
|------|-----------|---------|----------------|---------|
| **Mộc** | Jupiter (Mộc Tinh) | 歲星 Tuế Tinh | ~12 năm | Chu kỳ 12 năm = 12 Chi |
| **Hỏa** | Mars (Hỏa Tinh) | 熒惑 Huỳnh Hoặc | ~2 năm | Màu đỏ = Hỏa |
| **Thổ** | Saturn (Thổ Tinh) | 鎮星 Trấn Tinh | ~30 năm | Ổn định, chậm = Thổ |
| **Kim** | Venus (Kim Tinh) | 太白 Thái Bạch | ~225 ngày | Sáng nhất = Kim |
| **Thủy** | Mercury (Thủy Tinh) | 辰星 Thần Tinh | ~88 ngày | Nhanh nhất = Thủy |

### Chu Kỳ Thiên Văn Quan Trọng

```
Mộc Tinh:  12 năm  → Gốc của 12 Địa Chi
Thổ Tinh:  30 năm  → Một "Đại Hạn" trong Tử Vi
Mộc-Thổ hội: 60 năm → Lục Thập Hoa Giáp (10 Can × 6 = 60 năm)
```

### Công Thức Chu Kỳ

**Hội Mộc-Thổ (Jupiter-Saturn Conjunction):**
```
LCM(12, 30) / GCD(12, 30) ≈ 20 năm (hội gần)
LCM(12, 30) = 60 năm (hội chính xác tại cùng vị trí sao)
```

**Liên hệ với Lục Thập Hoa Giáp:**
- 10 Thiên Can × 12 Địa Chi = 60 tổ hợp
- Mộc Tinh 12 năm × 5 Hành = 60 năm
- Thổ Tinh 30 năm × 2 = 60 năm

### Ngũ Hành - Ngũ Tinh - Ngũ Phương

| Hành | Hành Tinh | Phương | Mùa | Số |
|------|-----------|--------|-----|-----|
| Mộc | Jupiter | Đông | Xuân | 3, 8 |
| Hỏa | Mars | Nam | Hạ | 2, 7 |
| Thổ | Saturn | Trung tâm | Tứ quý | 5, 10 |
| Kim | Venus | Tây | Thu | 4, 9 |
| Thủy | Mercury | Bắc | Đông | 1, 6 |

### Tương Sinh/Tương Khắc theo Chu Kỳ

**Tương Sinh (theo thứ tự chu kỳ tăng dần):**
```
Thủy(88d) → Kim(225d) → Hỏa(2y) → Mộc(12y) → Thổ(30y)
   ↓          ↓          ↓         ↓          ↓
 Nhanh      Sáng      Mạnh      Lớn      Chậm/Ổn định
```

**Chu kỳ trong Z₅:**
- Vị trí i: Thủy=0, Mộc=1, Hỏa=2, Thổ=3, Kim=4
- Sinh: `i → (i+1) mod 5`
- Khắc: `i → (i+2) mod 5`

---

## Quy Luật Số Học Trong Đông Phương Học

### Các Con Số Nền Tảng

| Số | Ý Nghĩa | Nguồn Gốc | Hệ Số |
|----|---------|-----------|-------|
| **5** | Ngũ Hành | 5 hành tinh khả kiến | Cơ số 5 |
| **7** | Thất Diệu (7 sao) | 5 hành tinh + Mặt Trời + Mặt Trăng | Thất phân |
| **9** | Cửu Cung | Lạc Thư, 9 cung Huyền Không | Hệ 9 |
| **10** | Thập Can | Thiên Can | Thập phân |
| **12** | Thập Nhị Chi | Mộc Tinh chu kỳ 12 năm | Cơ số 12 |
| **60** | Lục Thập Hoa Giáp | LCM(10, 12) = 60 | Chu kỳ lớn |

### Hệ Thất Phân (Base-7)

**7 Diệu (Thất Tinh):**
```
Nhật (Mặt Trời) → Chủ Nhật
Nguyệt (Mặt Trăng) → Thứ Hai
Hỏa (Mars) → Thứ Ba
Thủy (Mercury) → Thứ Tư
Mộc (Jupiter) → Thứ Năm
Kim (Venus) → Thứ Sáu
Thổ (Saturn) → Thứ Bảy
```

**Quan hệ toán học:**
- 7 ngày/tuần = 7 thiên thể khả kiến bằng mắt thường
- Trong Z₇: `i → (i+1) mod 7` cho vòng tuần hoàn

### Hệ Cửu Phân (Base-9) - Lạc Thư

```
┌───┬───┬───┐
│ 4 │ 9 │ 2 │  (Magic Square 3x3)
├───┼───┼───┤
│ 3 │ 5 │ 7 │  Tổng mỗi hàng/cột/chéo = 15
├───┼───┼───┤
│ 8 │ 1 │ 6 │  Trung tâm = 5 (Ngũ Hoàng)
└───┴───┴───┘
```

**Tính chất toán học:**
- Magic constant = n(n² + 1)/2 = 3(9+1)/2 = 15
- 9 cung = 8 hướng + 1 trung tâm
- Phi Tinh vận động: `cung_mới = (cung_cũ + bước) mod 9` (với 0 → 9)

### Hệ Thập Phân (Base-10) - Thiên Can

```
Giáp(0) Ất(1) → Mộc
Bính(2) Đinh(3) → Hỏa
Mậu(4) Kỷ(5) → Thổ
Canh(6) Tân(7) → Kim
Nhâm(8) Quý(9) → Thủy
```

**Công thức:**
```python
can_index = (year - 4) % 10
hanh = ["Mộc", "Mộc", "Hỏa", "Hỏa", "Thổ", "Thổ", "Kim", "Kim", "Thủy", "Thủy"][can_index]
```

### Hệ Thập Nhị Phân (Base-12) - Địa Chi

**12 Địa Chi = 12 năm Mộc Tinh:**
```
Tý(0)=Thủy  Sửu(1)=Thổ  Dần(2)=Mộc  Mão(3)=Mộc
Thìn(4)=Thổ  Tỵ(5)=Hỏa  Ngọ(6)=Hỏa  Mùi(7)=Thổ
Thân(8)=Kim  Dậu(9)=Kim  Tuất(10)=Thổ Hợi(11)=Thủy
```

**Công thức:**
```python
chi_index = (year - 4) % 12
```

### Hệ Nhị Phân (Base-2) - Âm Dương

**Nền tảng cơ bản nhất:**
```
0 = Âm (--) 
1 = Dương (─)
```

**64 Quẻ Dịch = 2⁶ = 64 tổ hợp:**
- Mỗi quẻ = 6 hào
- Mỗi hào = Âm hoặc Dương
- Tổng: 2 × 2 × 2 × 2 × 2 × 2 = 64

### Quan Hệ Giữa Các Hệ Số

```
Nhị phân (2) → Âm/Dương
    ↓
Ngũ phân (5) → Ngũ Hành
    ↓
Thất phân (7) → Thất Diệu (tuần)
    ↓
Cửu phân (9) → Cửu Cung Lạc Thư
    ↓
Thập phân (10) → Thiên Can
    ↓
Thập nhị phân (12) → Địa Chi
    ↓
Lục thập (60) → Can Chi = LCM(10, 12)
```

**Công thức tổng hợp:**
```
60 = LCM(10, 12) = 10 × 12 / GCD(10, 12) = 120 / 2 = 60
360 = 60 × 6 = Một "Đại Vận" hoặc số độ trong vòng tròn
```

### Số 100 và Bách Nhị Thập Phân

**100 trong hệ thống:**
- 100 năm ≈ 3 chu kỳ Thổ Tinh (30 × 3 = 90 năm)
- 100 = 10 × 10 = Thiên Can × Thiên Can
- 120 năm = 2 Lục Thập Hoa Giáp = "Thượng Thọ"

**Số 108:**
- 108 = 12 × 9 = Địa Chi × Cửu Cung
- 108 hạt chuỗi Phật
- 108 = 1 × 2 × 2 × 3 × 3 × 3 (tích các số đầu tiên)

---

## Bảng Chuyển Đổi Giữa Các Hệ Số

### Các Số Quan Trọng Trong Nhiều Hệ

| Decimal (10) | Binary (2) | Octal (8) | Hex (16) | Base-5 | Base-7 | Base-9 | Base-12 |
|--------------|------------|-----------|----------|--------|--------|--------|---------|
| 5 | 101 | 5 | 5 | 10 | 5 | 5 | 5 |
| 7 | 111 | 7 | 7 | 12 | 10 | 7 | 7 |
| 9 | 1001 | 11 | 9 | 14 | 12 | 10 | 9 |
| 10 | 1010 | 12 | A | 20 | 13 | 11 | A |
| 12 | 1100 | 14 | C | 22 | 15 | 13 | 10 |
| 60 | 111100 | 74 | 3C | 220 | 114 | 66 | 50 |
| 64 | 1000000 | 100 | 40 | 224 | 121 | 71 | 54 |
| **100** | 1100100 | 144 | 64 | 400 | **202** | 121 | 84 |
| 108 | 1101100 | 154 | 6C | 413 | 213 | 130 | 90 |
| 120 | 1111000 | 170 | 78 | 440 | 231 | 143 | A0 |
| 360 | 101101000 | 550 | 168 | 2420 | 1023 | 440 | 260 |

### Các "Số Vuông" Trong Mỗi Hệ

**Số vuông hoàn hảo (perfect squares) đặc biệt:**

| Hệ | Số Vuông | Decimal | Ý Nghĩa |
|----|----------|---------|---------|
| Base-2 | 100 = 2² | 4 | Tứ Tượng |
| Base-5 | 100 = 5² | 25 | - |
| Base-7 | 100 = 7² | **49** | Thất Thất = 49 ngày (7 tuần) |
| Base-9 | 100 = 9² | 81 | Cửu Cửu = 81 nạn |
| Base-10 | 100 = 10² | 100 | Bách (trăm) |
| Base-12 | 100 = 12² | 144 | Đại Tá (gross) |

### Mối Liên Hệ Đặc Biệt

**100 (Decimal) trong các hệ:**
```
100₁₀ = 1100100₂   (Binary: 7 bit)
100₁₀ = 144₈       (Octal: 1×64 + 4×8 + 4)
100₁₀ = 64₁₆       (Hex: 6×16 + 4)
100₁₀ = 400₅       (Base-5: 4×25 = 100)
100₁₀ = 202₇       (Base-7: 2×49 + 0×7 + 2)
100₁₀ = 121₉       (Base-9: 1×81 + 2×9 + 1)
100₁₀ = 84₁₂       (Base-12: 8×12 + 4)
```

**Số 49 (Thất Thất):**
```
49₁₀ = 100₇        (7² - số vuông trong base-7)
49₁₀ = 110001₂     (Binary)
49₁₀ = 31₁₆        (Hex)
49 ngày = 7 tuần   (Thất Thất - 49 ngày Tang/Kỵ)
```

**Số 81 (Cửu Cửu):**
```
81₁₀ = 100₉        (9² - số vuông trong base-9)
81₁₀ = 1010001₂    (Binary)
81₁₀ = 51₁₆        (Hex)
81 = 3⁴            (Lũy thừa 4 của 3)
81 nạn Đường Tăng
```

### Công Thức Chuyển Đổi

**Từ Decimal sang Base-N:**
```python
def to_base_n(num, base):
    if num == 0:
        return "0"
    digits = []
    while num:
        digits.append(str(num % base))
        num //= base
    return ''.join(reversed(digits))
```

**Ví dụ: 100 → Base-7:**
```
100 ÷ 7 = 14 dư 2
14 ÷ 7 = 2 dư 0  
2 ÷ 7 = 0 dư 2
→ 100₁₀ = 202₇
Kiểm tra: 2×49 + 0×7 + 2 = 98 + 0 + 2 = 100
```

### Bảng Nhân Trong Base-7 (Thất Tinh)

```
× | 1  2  3  4  5  6
--+------------------
1 | 1  2  3  4  5  6
2 | 2  4  6  11 13 15
3 | 3  6  12 15 21 24
4 | 4  11 15 22 26 33
5 | 5  13 21 26 34 42
6 | 6  15 24 33 42 51
```

*Lưu ý: 11₇ = 8₁₀, 12₇ = 9₁₀, v.v.*

### Ứng Dụng Trong Đông Phương Học

| Khái Niệm | Công Thức | Hệ Số Liên Quan |
|-----------|-----------|-----------------|
| Lục Thập Hoa Giáp | LCM(10, 12) | Base-10, Base-12 |
| 7 ngày/tuần | 7 Diệu | Base-7 |
| 9 Cung Lạc Thư | 3×3 magic square | Base-9 |
| 64 Quẻ Dịch | 2⁶ = 64 | Base-2 |
| 12 Địa Chi | 12 năm Mộc Tinh | Base-12 |
| 360 độ | 60 × 6 | Base-60 (Lục Thập) |

### Số Đặc Biệt và Ước Số

```
60 = 2² × 3 × 5     (highly composite: 12 ước số)
360 = 2³ × 3² × 5   (24 ước số - nhiều nhất trong phạm vi)
12 = 2² × 3         (6 ước số)
10 = 2 × 5          (4 ước số)
```

**Vì sao dùng 60 và 360?**
- 60 chia hết cho: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60
- 360 chia hết cho: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36, 40, 45, 60, 72, 90, 120, 180, 360
- Thuận tiện cho việc chia đều vòng tròn và chu kỳ
