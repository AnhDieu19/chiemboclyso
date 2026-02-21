# 🕐 QUY LUẬT VẬN ĐỘNG SAO THEO CANH GIỜ

> Phân tích vận động sao lấy **Ngũ Hành + 12 Địa Chi** làm gốc cố định
> Hướng kim đồng hồ = THUẬN (Tý → Sửu → Dần → ... → Hợi)
> 
> Ngày tạo: 23/12/2024

---

## 📍 HỆ QUY CHIẾU CỐ ĐỊNH

### Bàn cờ 12 Cung theo chiều kim đồng hồ:

```
                    NGỌ (6)
                      ↑
        TỴ (5) ←              → MÙI (7)
                      |
       THÌN (4)       |        THÂN (8)
          ↑           |           ↓
                   [TRUNG TÂM]
          ↑           |           ↓
        MÃO (3)       |        DẬU (9)
                      |
        DẦN (2) ←              → TUẤT (10)
                      ↓
          SỬU (1)         HỢI (11)
                TÝ (0)
```

### Quy ước:
- **THUẬN** (↻): Tý(0) → Sửu(1) → Dần(2) → ... → Hợi(11) → Tý(0)
- **NGHỊCH** (↺): Tý(0) → Hợi(11) → Tuất(10) → ... → Sửu(1) → Tý(0)

---

## ⏰ I. SAO BIẾN ĐỘNG THEO GIỜ SINH

### Bảng tổng hợp:

| # | Sao | Vị trí gốc | Hướng | Bước/Giờ | Công thức |
|---|-----|-----------|-------|----------|-----------|
| 1 | **Cung Mệnh** | Dần (2) + Tháng | ↺ NGHỊCH | -1 | `(2 + tháng - 1 - giờ) % 12` |
| 2 | **Cung Thân** | Dần (2) + Tháng | ↻ THUẬN | +1 | `(2 + tháng - 1 + giờ) % 12` |
| 3 | **Văn Xương** | Tuất (10) | ↺ NGHỊCH | -1 | `(10 - giờ) % 12` |
| 4 | **Văn Khúc** | Thìn (4) | ↻ THUẬN | +1 | `(4 + giờ) % 12` |
| 5 | **Địa Không** | Hợi (11) | ↺ NGHỊCH | -1 | `(11 - giờ) % 12` |
| 6 | **Địa Kiếp** | Hợi (11) | ↻ THUẬN | +1 | `(11 + giờ) % 12` |
| 7 | **Hỏa Tinh** | *Theo Chi năm* | Điều kiện* | ±1 | Xem bảng chi tiết |
| 8 | **Linh Tinh** | *Theo Chi năm* | Điều kiện* | ±1 | Ngược Hỏa Tinh |
| 9 | **Thai Phụ** | Ngọ (6) | ↻ THUẬN | +1 | `(6 + giờ) % 12` |
| 10 | **Phong Cáo** | Dần (2) | ↻ THUẬN | +1 | `(2 + giờ) % 12` |
| 11 | **Đẩu Quân** | Dần + Tháng | ↺ NGHỊCH | -1 | `(2 + tháng - 1 - giờ) % 12` |

---

### 1.1 VĂN XƯƠNG - VĂN KHÚC (Đối xứng qua trục Thìn-Tuất)

```
Giờ │ Văn Xương (↺)  │ Văn Khúc (↻)  │ Tổng khoảng cách
────┼────────────────┼────────────────┼──────────────────
 Tý │ Tuất (10)      │ Thìn (4)      │ 6 (đối xứng)
Sửu │ Dậu (9)        │ Tỵ (5)        │ 4
Dần │ Thân (8)       │ Ngọ (6)       │ 2
Mão │ Mùi (7)        │ Mùi (7)       │ 0 (trùng!)
Thìn│ Ngọ (6)        │ Thân (8)      │ 2
 Tỵ │ Tỵ (5)         │ Dậu (9)       │ 4
Ngọ │ Thìn (4)       │ Tuất (10)     │ 6 (đối xứng)
Mùi │ Mão (3)        │ Hợi (11)      │ 8
Thân│ Dần (2)        │ Tý (0)        │ 10
Dậu │ Sửu (1)        │ Sửu (1)       │ 0 (trùng!)
Tuất│ Tý (0)         │ Dần (2)       │ 2
Hợi │ Hợi (11)       │ Mão (3)       │ 4
```

**Nhận xét:**
- Xương và Khúc **đối xứng qua trục Thìn-Tuất**
- Giờ Mão và giờ Dậu: Xương Khúc **TRÙNG CUNG** (Đồng cung)
- Tổng khoảng cách luôn = 14 (mod 12)

---

### 1.2 ĐỊA KHÔNG - ĐỊA KIẾP (Đối xứng qua Hợi)

```
Giờ │ Địa Không (↺)  │ Địa Kiếp (↻)  │ Ghi chú
────┼────────────────┼────────────────┼─────────────────
 Tý │ Hợi (11)       │ Hợi (11)      │ TRÙNG tại Hợi!
Sửu │ Tuất (10)      │ Tý (0)        │ 
Dần │ Dậu (9)        │ Sửu (1)       │
Mão │ Thân (8)       │ Dần (2)       │
Thìn│ Mùi (7)        │ Mão (3)       │
 Tỵ │ Ngọ (6)        │ Thìn (4)      │
Ngọ │ Tỵ (5)         │ Tỵ (5)        │ TRÙNG tại Tỵ!
Mùi │ Thìn (4)       │ Ngọ (6)       │
Thân│ Mão (3)        │ Mùi (7)       │
Dậu │ Dần (2)        │ Thân (8)      │
Tuất│ Sửu (1)        │ Dậu (9)       │
Hợi │ Tý (0)         │ Tuất (10)     │
```

**Nhận xét:**
- Địa Không và Địa Kiếp **đối xứng qua vị trí Hợi (11)**
- Giờ Tý: Cả hai TRÙNG tại **Hợi** (11)
- Giờ Ngọ: Cả hai TRÙNG tại **Tỵ** (5)

---

### 1.3 HỎA TINH - LINH TINH (Phức tạp nhất)

**Bước 1: Xác định vị trí GỐC theo Chi năm**

| Nhóm Chi năm | Hỏa Tinh gốc | Linh Tinh gốc |
|--------------|--------------|---------------|
| Dần, Ngọ, Tuất | **Sửu (1)** | **Mão (3)** |
| Thân, Tý, Thìn | **Dần (2)** | **Tuất (10)** |
| Tỵ, Dậu, Sửu | **Mão (3)** | **Tuất (10)** |
| Hợi, Mão, Mùi | **Dậu (9)** | **Tuất (10)** |

**Bước 2: Xác định HƯỚNG đi theo Âm/Dương + Giới tính**

| Can năm | Âm/Dương | Giới tính | Hỏa Tinh | Linh Tinh |
|---------|----------|-----------|----------|-----------|
| Giáp, Bính, Mậu, Canh, Nhâm | DƯƠNG | Nam | ↻ THUẬN | ↺ NGHỊCH |
| Giáp, Bính, Mậu, Canh, Nhâm | DƯƠNG | Nữ | ↺ NGHỊCH | ↻ THUẬN |
| Ất, Đinh, Kỷ, Tân, Quý | ÂM | Nam | ↺ NGHỊCH | ↻ THUẬN |
| Ất, Đinh, Kỷ, Tân, Quý | ÂM | Nữ | ↻ THUẬN | ↺ NGHỊCH |

**Ví dụ: Năm Giáp Ngọ (Dương), Nam**
- Chi Ngọ thuộc nhóm "Dần Ngọ Tuất" → Hỏa gốc = Sửu, Linh gốc = Mão
- Dương Nam → Hỏa THUẬN, Linh NGHỊCH
- Giờ Dần (2): Hỏa = (1 + 2) % 12 = **Mão**, Linh = (3 - 2) % 12 = **Sửu**

---

### 1.4 CUNG MỆNH - CUNG THÂN (Đối xứng)

**Công thức:**
```
Cung Mệnh = (2 + tháng - 1 - giờ) % 12
Cung Thân = (2 + tháng - 1 + giờ) % 12
```

**Khẩu quyết:** 
> "Chính nguyệt khởi DẦN, THUẬN tháng, NGHỊCH giờ tìm Mệnh"
> "Chính nguyệt khởi DẦN, THUẬN tháng, THUẬN giờ tìm Thân"

**Bảng Cung Mệnh theo Tháng và Giờ:**

```
       │ Tháng 1│ Tháng 2│ Tháng 3│ ... │ Tháng 12
───────┼────────┼────────┼────────┼─────┼──────────
Giờ Tý │ Dần(2) │ Mão(3) │Thìn(4) │ ... │ Sửu(1)
Giờ Sửu│ Sửu(1) │ Dần(2) │ Mão(3) │ ... │ Tý(0)
Giờ Dần│ Tý(0)  │ Sửu(1) │ Dần(2) │ ... │ Hợi(11)
Giờ Mão│ Hợi(11)│ Tý(0)  │ Sửu(1) │ ... │ Tuất(10)
   ...
Giờ Hợi│ Mão(3) │Thìn(4) │ Tỵ(5)  │ ... │ Dần(2)
```

**Nhận xét:**
- Mệnh và Thân **đối xứng qua vị trí gốc** (Dần + tháng - 1)
- Tổng vị trí Mệnh + Thân = `2 × (2 + tháng - 1)` (mod 12)
- Khi giờ = 0 (Tý): Mệnh = Thân (trùng nhau)
- Khi giờ = 6 (Ngọ): Mệnh và Thân cách nhau 12 vị trí = **đối xứng**

---

## 📅 II. SAO BIẾN ĐỘNG THEO THÁNG

| # | Sao | Vị trí gốc | Hướng | Bước/Tháng | Công thức |
|---|-----|-----------|-------|------------|-----------|
| 1 | **Tả Phù** | Thìn (4) | ↻ THUẬN | +1 | `(4 + tháng - 1) % 12` |
| 2 | **Hữu Bật** | Tuất (10) | ↺ NGHỊCH | -1 | `(10 - tháng + 1) % 12` |
| 3 | **Thiên Hình** | Dậu (9) | ↻ THUẬN | +1 | `(9 + tháng - 1) % 12` |
| 4 | **Thiên Y** | Sửu (1) | ↻ THUẬN | +1 | `(1 + tháng - 1) % 12` |
| 5 | **Thiên Giải** | Thân (8) | ↻ THUẬN | +1 | `(8 + tháng - 1) % 12` |
| 6 | **Địa Giải** | Mùi (7) | ↻ THUẬN | +1 | `(7 + tháng - 1) % 12` |

### Bảng Tả Phù - Hữu Bật (Đối xứng qua trục Thìn-Tuất)

```
Tháng │ Tả Phù (↻)    │ Hữu Bật (↺)   │ Khoảng cách
──────┼───────────────┼───────────────┼─────────────
   1  │ Thìn (4)      │ Tuất (10)     │ 6 (đối xứng)
   2  │ Tỵ (5)        │ Dậu (9)       │ 4
   3  │ Ngọ (6)       │ Thân (8)      │ 2
   4  │ Mùi (7)       │ Mùi (7)       │ 0 (TRÙNG!)
   5  │ Thân (8)      │ Ngọ (6)       │ 2
   6  │ Dậu (9)       │ Tỵ (5)        │ 4
   7  │ Tuất (10)     │ Thìn (4)      │ 6 (đối xứng)
   8  │ Hợi (11)      │ Mão (3)       │ 8
   9  │ Tý (0)        │ Dần (2)       │ 2
  10  │ Sửu (1)       │ Sửu (1)       │ 0 (TRÙNG!)
  11  │ Dần (2)       │ Tý (0)        │ 2
  12  │ Mão (3)       │ Hợi (11)      │ 8
```

**Nhận xét:**
- Tả Hữu **đối xứng qua trục Thìn-Tuất**
- Tháng 4 và Tháng 10: Tả Hữu **ĐỒNG CUNG**

---

## 📆 III. SAO BIẾN ĐỘNG THEO NGÀY

### 14 Chính Tinh (Phụ thuộc Ngày + Cục)

**Cục** được xác định bởi: Can năm + Cung Mệnh

| Cục | Giá trị | Ngày tương ứng |
|-----|---------|----------------|
| Thủy Nhị Cục | 2 | Ngày 2, 4, 6, ... |
| Mộc Tam Cục | 3 | Ngày 3, 6, 9, ... |
| Kim Tứ Cục | 4 | Ngày 4, 8, 12, ... |
| Thổ Ngũ Cục | 5 | Ngày 5, 10, 15, ... |
| Hỏa Lục Cục | 6 | Ngày 6, 12, 18, ... |

**Thuật toán Tử Vi:**
```
1. Tìm 'a' (0 đến Cục-1) sao cho (Ngày + a) chia hết cho Cục
2. b = (Ngày + a) / Cục
3. Tử Vi = Dần + b (thuận)
4. Nếu a LẺ: Tử Vi -= a (lùi)
   Nếu a CHẴN: Tử Vi += a (tiến)
```

**Các sao khác phụ thuộc Ngày:**
- **Ân Quang** = Văn Xương + Ngày (thuận)
- **Thiên Quý** = Văn Khúc + Ngày (thuận)
- **Tam Thai** = Tả Phù + Ngày (thuận)
- **Bát Tọa** = Hữu Bật + Ngày (thuận)

---

## 🗓️ IV. SAO CỐ ĐỊNH THEO NĂM

### 4.1 Theo Thiên Can (Chu kỳ 10 năm)

| Can | Lộc Tồn | Kình Dương | Đà La | Thiên Khôi | Thiên Việt |
|-----|---------|------------|-------|------------|------------|
| Giáp | Dần | Mão | Sửu | Sửu | Mùi |
| Ất | Mão | Thìn | Dần | Tý | Thân |
| Bính | Tỵ | Ngọ | Thìn | Hợi | Dậu |
| Đinh | Ngọ | Mùi | Tỵ | Dậu | Hợi |
| Mậu | Tỵ | Ngọ | Thìn | Hợi | Dậu |
| Kỷ | Ngọ | Mùi | Tỵ | Dậu | Hợi |
| Canh | Thân | Dậu | Mùi | Mùi | Sửu |
| Tân | Dậu | Tuất | Thân | Ngọ | Dần |
| Nhâm | Hợi | Tý | Tuất | Mão | Tỵ |
| Quý | Tý | Sửu | Hợi | Mão | Tỵ |

### 4.2 Theo Địa Chi (Chu kỳ 12 năm)

**Vòng Thái Tuế** (12 sao, bắt đầu từ Chi năm, đi thuận):
```
Thái Tuế → Thiếu Dương → Tang Môn → Thiếu Âm → Quan Phù → Tử Phù 
→ Tuế Phá → Long Đức → Bạch Hổ → Phúc Đức → Điếu Khách → Trực Phù
```

**Các sao cố định:**
| Sao | Công thức | Ghi chú |
|-----|-----------|---------|
| Thiên La | Cố định tại **Thìn (4)** | Không di chuyển |
| Địa Võng | Cố định tại **Tuất (10)** | Không di chuyển |
| Thái Tuế | = Chi năm | Chu kỳ 12 |

---

## 🌙 V. THÁNG NHUẬN (Leap Month)

### Xử lý hiện tại trong code:

```python
def generate_birth_chart_lunar(..., leap_month=False):
    # leap_month được lưu trữ nhưng KHÔNG ảnh hưởng tính toán
    lunar = {'day': day, 'month': month, 'year': year, 'leap': leap_month}
```

### Quy tắc tháng nhuận:

| Trường hợp | Xử lý | Ghi chú |
|------------|-------|---------|
| Sinh TRƯỚC 15 tháng nhuận | Dùng tháng TRƯỚC | Ví dụ: Nhuận 4 → dùng tháng 4 |
| Sinh SAU 15 tháng nhuận | Dùng tháng SAU | Ví dụ: Nhuận 4 → dùng tháng 5 |
| **Hiện tại code** | Dùng tháng gốc | Chưa phân biệt trước/sau 15 |

### Ngoại lệ cần lưu ý:

1. **Năm nhuận dương lịch** (366 ngày): Không ảnh hưởng Tử Vi (dùng âm lịch)
2. **Tháng nhuận âm lịch**: Cần xác định ngày để tính đúng
3. **Năm có 13 tháng**: Một số phái cho rằng ảnh hưởng Cục

---

## 📊 VI. BẢNG TỔNG HỢP VẬN ĐỘNG

### Phân loại theo tần suất thay đổi:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TẦN SUẤT THAY ĐỔI CÁC SAO                               │
├──────────────┬──────────────────────────────────────────────────────────────┤
│ CỐ ĐỊNH      │ Thiên La, Địa Võng                                          │
│ (0 lần/đời)  │                                                              │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ THEO NĂM    │ • Thiên Can (10 năm): Lộc Tồn, Kình Đà, Khôi Việt, Tứ Hóa   │
│ (1 lần/năm) │ • Địa Chi (12 năm): Thái Tuế ring, Đào Hoa, Hồng Loan...    │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ THEO THÁNG  │ Tả Phù, Hữu Bật, Thiên Hình, Thiên Y, Thiên Giải, Địa Giải  │
│ (12 lần/năm)│                                                              │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ THEO NGÀY   │ 14 Chính Tinh (qua Cục), Ân Quang, Thiên Quý, Tam Thai,     │
│ (30 lần/th) │ Bát Tọa                                                       │
├──────────────┼──────────────────────────────────────────────────────────────┤
│ THEO GIỜ    │ Văn Xương/Khúc, Địa Không/Kiếp, Hỏa/Linh Tinh,              │
│ (12 lần/ng) │ Thai Phụ, Phong Cáo, Đẩu Quân, Cung Mệnh/Thân               │
└──────────────┴──────────────────────────────────────────────────────────────┘
```

---

## 🔄 VII. MÔ HÌNH VẬN ĐỘNG THEO CANH GIỜ

### Giả sử cố định: Năm, Tháng, Ngày. Chỉ thay đổi GIỜ:

```
Giờ Tý (0)   Giờ Sửu (1)   Giờ Dần (2)   ...   Giờ Hợi (11)
    ↓            ↓             ↓                    ↓
┌────────────────────────────────────────────────────────────┐
│ SAO THUẬN (+1/giờ):                                        │
│   Văn Khúc:    4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 0 → 1 → 2 → 3 │
│   Địa Kiếp:   11 → 0 → 1 → 2 → 3 → 4 →  5 →  6 → 7 → 8 → 9 →10 │
│   Thai Phụ:    6 → 7 → 8 → 9 →10 →11 →  0 →  1 → 2 → 3 → 4 → 5 │
│   Phong Cáo:   2 → 3 → 4 → 5 → 6 → 7 →  8 →  9 →10 →11 → 0 → 1 │
│   Cung Thân:   * → * → * (phụ thuộc tháng)                 │
├────────────────────────────────────────────────────────────┤
│ SAO NGHỊCH (-1/giờ):                                       │
│   Văn Xương:  10 → 9 → 8 → 7 → 6 → 5 →  4 →  3 → 2 → 1 → 0 →11 │
│   Địa Không:  11 →10 → 9 → 8 → 7 → 6 →  5 →  4 → 3 → 2 → 1 → 0 │
│   Cung Mệnh:   * → * → * (phụ thuộc tháng)                 │
├────────────────────────────────────────────────────────────┤
│ SAO ĐIỀU KIỆN (Hỏa/Linh):                                  │
│   Dương Nam:  Hỏa thuận, Linh nghịch                       │
│   Dương Nữ:   Hỏa nghịch, Linh thuận                       │
│   Âm Nam:     Hỏa nghịch, Linh thuận                       │
│   Âm Nữ:      Hỏa thuận, Linh nghịch                       │
└────────────────────────────────────────────────────────────┘
```

---

## 🎯 VIII. KẾT LUẬN

### Quy luật chung:

1. **Đối xứng**: Hầu hết sao đi theo cặp đối xứng
   - Văn Xương ↔ Văn Khúc (qua Thìn-Tuất)
   - Địa Không ↔ Địa Kiếp (qua Hợi)
   - Tả Phù ↔ Hữu Bật (qua Thìn-Tuất)
   - Cung Mệnh ↔ Cung Thân (qua điểm gốc)

2. **Bước nhảy cố định**: Mỗi đơn vị thời gian = 1 cung

3. **Hướng đi**: 
   - Thuận (kim đồng hồ) = +1
   - Nghịch (ngược kim đồng hồ) = -1

4. **Điểm trùng**: Các cặp sao thường trùng nhau tại 2 vị trí trong chu kỳ

5. **Yếu tố phức tạp**: 
   - Hỏa/Linh: Phụ thuộc 3 yếu tố (Chi năm + Giờ + Giới tính)
   - Chính tinh: Phụ thuộc Cục + Ngày (không đơn giản theo giờ)

---

*Tài liệu được tạo từ phân tích mã nguồn Tu Vi App*
