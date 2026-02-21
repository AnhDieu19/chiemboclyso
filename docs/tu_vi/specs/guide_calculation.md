# TỬ VI ĐẨU SỐ - HƯỚNG DẪN TÍNH TOÁN
## Comprehensive Calculation Guide

---

## Mục Lục

1. [Tổng Quan Thuật Toán](#1-tổng-quan-thuật-toán)
2. [Chuyển Đổi Âm Dương Lịch](#2-chuyển-đổi-âm-dương-lịch)
3. [Tính Can Chi](#3-tính-can-chi)
4. [Xác Định Cung Mệnh và Cung Thân](#4-xác-định-cung-mệnh-và-cung-thân)
5. [Xác Định Cục](#5-xác-định-cục)
6. [An Tử Vi và Chính Tinh](#6-an-tử-vi-và-chính-tinh)
7. [An Phụ Tinh](#7-an-phụ-tinh)
8. [Áp Dụng Tứ Hóa](#8-áp-dụng-tứ-hóa)
9. [Luận Giải Lá Số](#9-luận-giải-lá-số)

---

## 1. Tổng Quan Thuật Toán

### 1.1 Quy Trình Lập Lá Số

```
[Ngày Dương lịch] → [Chuyển Âm lịch] → [Tính Can Chi] → [Xác định Cung Mệnh]
                                                              ↓
[Hiển thị lá số] ← [Luận giải] ← [An các sao] ← [Xác định Cục]
```

### 1.2 Các Bước Chính

| Step | Tên | Mô tả |
|------|-----|-------|
| 1 | Solar → Lunar | Chuyển ngày Dương lịch sang Âm lịch |
| 2 | Can Chi | Tính Can Chi năm, tháng, ngày, giờ |
| 3 | Cung Mệnh | Tính vị trí Cung Mệnh và Cung Thân |
| 4 | Cục | Xác định Ngũ Hành Cục (2-6) |
| 5 | Tử Vi | An sao Tử Vi dựa trên Cục và ngày sinh |
| 6 | Chính Tinh | An 14 Chính Tinh theo Tử Vi |
| 7 | Phụ Tinh | An 75+ Phụ Tinh theo các quy tắc |
| 8 | Tứ Hóa | Áp dụng Hóa Lộc, Quyền, Khoa, Kỵ |
| 9 | Luận giải | Phân tích và giải đoán lá số |

---

## 2. Chuyển Đổi Âm Dương Lịch

### 2.1 Julius Day Number

**Công thức:**
```
a = (14 - month) / 12
y = year + 4800 - a
m = month + 12 * a - 3
JD = day + (153*m + 2)/5 + 365*y + y/4 - y/100 + y/400 - 32045
```

**Giải thích:**
- `a`: Điều chỉnh nếu tháng 1 hoặc 2 (coi như tháng 13, 14 năm trước)
- `y`: Năm điều chỉnh, cộng 4800 để tránh số âm
- `m`: Tháng điều chỉnh (bắt đầu từ tháng 3 = 0)
- Các hệ số 153, 365, 32045 là hằng số lịch Gregorian

### 2.2 Điểm Sóc (New Moon)

**Công thức Jean Meeus:**
```
T = k / 1236.85
JD = 2415020.75933 + 29.53058868*k + corrections
```

**Trong đó:**
- `k`: Số thứ tự Trăng mới từ mốc (6/1/1900)
- `29.53058868`: Chu kỳ Sóc trung bình (ngày)
- `corrections`: Hiệu chỉnh thiên văn dựa trên M, M', F

### 2.3 Xác Định Tháng Âm Lịch

**Quy trình:**
1. Tìm tháng 11 Âm lịch (chứa Đông Chí)
2. Đếm số tháng từ tháng 11 đến tháng hiện tại
3. Kiểm tra năm có tháng nhuận không
4. Điều chỉnh số tháng nếu có nhuận

**Tháng nhuận:** Xảy ra khi từ tháng 11 năm trước đến tháng 11 năm sau > 365 ngày (có 13 Sóc)

---

## 3. Tính Can Chi

### 3.1 Can Chi Năm

**Công thức:**
```
Can = (năm + 6) mod 10
Chi = (năm + 8) mod 12
```

**Bảng 10 Thiên Can:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-------|---|---|---|---|---|---|---|---|---|---|
| Can | Giáp | Ất | Bính | Đinh | Mậu | Kỷ | Canh | Tân | Nhâm | Quý |

**Bảng 12 Địa Chi:**
| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|-------|---|---|---|---|---|---|---|---|---|---|----|----|
| Chi | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |

### 3.2 Can Chi Tháng (Ngũ Hổ Độn)

**Công thức:**
```
Chi tháng = (tháng + 1) mod 12  (tháng 1 = Dần)
Can tháng = (start_can[Can năm] + tháng - 1) mod 10
```

**Bảng Start Can:**
| Can Năm | Giáp/Kỷ | Ất/Canh | Bính/Tân | Đinh/Nhâm | Mậu/Quý |
|---------|---------|---------|----------|-----------|---------|
| Start Can tháng 1 | Bính (2) | Mậu (4) | Canh (6) | Nhâm (8) | Giáp (0) |

### 3.3 Can Chi Ngày

**Công thức:**
```
JD = Julius Day của ngày Dương lịch
Can = (JD + 9) mod 10
Chi = (JD + 1) mod 12
```

### 3.4 Can Chi Giờ (Ngũ Thử Độn)

**Công thức:**
```
Chi giờ = hour_index (0-11, từ Tý đến Hợi)
Can giờ = (Can ngày * 2 + Chi giờ) mod 10
```

**Bảng 12 Canh Giờ:**
| Index | Chi | Giờ |
|-------|-----|-----|
| 0 | Tý | 23:00 - 01:00 |
| 1 | Sửu | 01:00 - 03:00 |
| 2 | Dần | 03:00 - 05:00 |
| 3 | Mão | 05:00 - 07:00 |
| ... | ... | ... |

---

## 4. Xác Định Cung Mệnh và Cung Thân

### 4.1 Công Thức Cung Mệnh

**Khẩu quyết:** "Chính nguyệt khởi Dần, thuận tháng nghịch giờ"

```
Cung Mệnh = (2 + tháng - 1 - giờ) mod 12
         = (Dần + tháng - giờ) mod 12
```

### 4.2 Công Thức Cung Thân

**Khẩu quyết:** "Chính nguyệt khởi Dần, thuận tháng thuận giờ"

```
Cung Thân = (2 + tháng - 1 + giờ) mod 12
         = (Dần + tháng + giờ) mod 12
```

### 4.3 Ví Dụ

| Tháng | Giờ | Cung Mệnh | Cung Thân |
|-------|-----|-----------|-----------|
| 1 | Tý (0) | (2+0-0)=2 → Dần | (2+0+0)=2 → Dần |
| 2 | Mão (3) | (2+1-3)=0 → Tý | (2+1+3)=6 → Ngọ |
| 3 | Ngọ (6) | (2+2-6)=-2 → Tuất | (2+2+6)=10 → Tuất |

---

## 5. Xác Định Cục

### 5.1 Ngũ Hành Cục

| Cục | Số | Hành |
|-----|----|----- |
| Thủy Nhị Cục | 2 | Thủy |
| Mộc Tam Cục | 3 | Mộc |
| Kim Tứ Cục | 4 | Kim |
| Thổ Ngũ Cục | 5 | Thổ |
| Hỏa Lục Cục | 6 | Hỏa |

### 5.2 Bảng Tra Cục (trích)

Tra theo **Can năm** (hàng) và **Chi Cung Mệnh** (cột):

| | Tý | Sửu | Dần | Mão | Thìn | Tỵ |
|---|---|---|---|---|---|---|
| **Giáp/Ất** | Kim 4 | Kim 4 | Thủy 2 | Thủy 2 | Hỏa 6 | Hỏa 6 |
| **Bính/Đinh** | Thủy 2 | Thủy 2 | Hỏa 6 | Hỏa 6 | Thổ 5 | Thổ 5 |
| **Mậu/Kỷ** | Hỏa 6 | Hỏa 6 | Thổ 5 | Thổ 5 | Mộc 3 | Mộc 3 |
| ... | ... | ... | ... | ... | ... | ... |

---

## 6. An Tử Vi và Chính Tinh

### 6.1 Công Thức An Tử Vi

**Bảng TUVI_POSITION[Cục][Ngày Âm lịch]:**

Mỗi Cục có một bảng riêng, tra theo ngày Âm lịch để tìm vị trí Tử Vi.

```
tu_vi_position = TUVI_POSITION[cuc_number][lunar_day]
```

### 6.2 An 14 Chính Tinh

| Nhóm Tử Vi | Sao | Vị trí |
|------------|-----|--------|
| Tử Vi | Tử Vi | Gốc |
| | Thiên Cơ | Tử Vi - 1 |
| | Thái Dương | Tử Vi - 3 |
| | Vũ Khúc | Tử Vi - 4 |
| | Thiên Đồng | Tử Vi - 5 |
| | Liêm Trinh | Tử Vi + 4 |

| Nhóm Thiên Phủ | Sao | Vị trí |
|----------------|-----|--------|
| Thiên Phủ | Thiên Phủ | Đối xứng với Tử Vi qua trục Dần-Thân |
| | Thái Âm | Thiên Phủ + 1 |
| | Tham Lang | Thiên Phủ + 2 |
| | Cự Môn | Thiên Phủ + 3 |
| | Thiên Tướng | Thiên Phủ + 4 |
| | Thiên Lương | Thiên Phủ + 5 |
| | Thất Sát | Thiên Phủ + 6 |
| | Phá Quân | Thiên Phủ + 10 |

---

## 7. An Phụ Tinh

### 7.1 Lục Cát Tinh

| Sao | Cách An |
|-----|---------|
| Tả Phù | Theo tháng, khởi từ Thìn |
| Hữu Bật | Theo tháng, khởi từ Tuất |
| Văn Xương | Theo giờ, khởi từ Tuất đếm nghịch |
| Văn Khúc | Theo giờ, khởi từ Thìn đếm thuận |
| Thiên Khôi | Theo Can năm, tra bảng |
| Thiên Việt | Theo Can năm, tra bảng |

### 7.2 Lục Sát Tinh

| Sao | Cách An |
|-----|---------|
| Kình Dương | Lộc Tồn + 1 |
| Đà La | Lộc Tồn - 1 |
| Hỏa Tinh | Theo Chi năm và giờ |
| Linh Tinh | Theo Chi năm và giờ |
| Địa Không | Theo giờ, khởi từ Hợi đếm thuận |
| Địa Kiếp | Theo giờ, khởi từ Hợi đếm nghịch |

### 7.3 Vòng Trường Sinh (12 sao)

```
Trường Sinh → Mộc Dục → Quan Đới → Lâm Quan → Đế Vượng → Suy
     ↓                                                    ↓
   Dưỡng ← Thai ← Tuyệt ← Mộ ← Tử ← Bệnh
```

- Khởi từ Trường Sinh theo Cục và Âm/Dương năm
- Thuận hành (nam Dương, nữ Âm) hoặc nghịch hành

### 7.4 Vòng Bác Sỹ (12 sao)

```
Bác Sỹ → Lực Sỹ → Thanh Long → Tiểu Hao → Tướng Quân → Tấu Thư
   ↓                                                       ↓
Quan Phù ← Phục Binh ← Đại Hao ← Bệnh Phù ← Hỉ Thần ← Phi Liêm
```

- Khởi từ Lộc Tồn, đếm thuận

### 7.5 Vòng Thái Tuế (12 sao)

```
Thái Tuế → Thiếu Dương → Tang Môn → Thiếu Âm → Quan Phù → Tử Phù
    ↓                                                        ↓
Trực Phù ← Điếu Khách ← Phúc Đức ← Bạch Hổ ← Long Đức ← Tuế Phá
```

- Khởi từ Chi năm
295: 
296: ### 7.6 Các Sao Đã Hiệu Chỉnh (Verified Nam Phái)
297: 
298: Dựa trên kết quả kiểm thử với lá số mẫu (1994, 2025):
299: 
300: | Sao | Công Thức / Quy Tắc |
301: |-----|---------------------|
302: | **Phượng Các** | Khởi Tuất, nghịch hành theo Chi năm |
303: | **Giải Thần** | An theo Phượng Các (đồng cung) |
304: | **Thiên Khốc** | Khởi Ngọ, nghịch hành theo Chi năm |
305: | **Thiên Hư** | Khởi Ngọ, thuận hành theo Chi năm |
306: | **Thiên Diêu** | Theo Tháng: Tháng 1 tại Sửu, thuận hành |
307: | **Thiên Y** | Theo Tháng: Tháng 1 tại Sửu, thuận hành (đồng cung Diêu) |
308: | **Thiên Tài** | Cung Mệnh + Chi năm |
309: | **Thiên Thọ** | Cung Thân + Chi năm |
310: | **Thiên Đức** | (Chi năm - 3) |
311: | **Nguyệt Đức** | (Chi năm + 5) |
312: | **Lưu Hà** | Theo Can năm (Giáp→Dậu, Ất→Tuất...) |
313: | **LN.Văn Tinh** | Theo Can năm (Giáp→Tỵ, Ất→Ngọ...) |
314: 
315: ### 7.7 Các Sao Lưu Niên (Annual Stars)
316: 
317: Tính theo năm xem hạn (Viewing Year):
318: 
319: | Sao Lưu | Công Thức |
320: |---------|-----------|
321: | **Lưu Thái Tuế** | Tại cung có Chi = Chi năm xem |
322: | **Lưu Lộc Tồn** | Theo Can năm xem |
323: | **Lưu Kình/Đà** | Trước/Sau Lưu Lộc Tồn |
324: | **Lưu Thiên Mã** | Theo Tam Hợp Chi năm xem (DầnNgọTuất→Thân...) |
325: | **Lưu Khốc/Hư** | Khởi Ngọ, nghịch/thuận theo Chi năm xem |
326: | **Lưu Tứ Hóa** | Theo Can năm xem (Giáp: Liêm Phá Vũ Dương...) |

### 7.6 Các Sao Đã Hiệu Chỉnh (Verified Nam Phái)

Dựa trên kết quả kiểm thử với lá số mẫu (1994, 2025):

| Sao | Công Thức / Quy Tắc |
|-----|---------------------|
| **Phượng Các** | Khởi Tuất, nghịch hành theo Chi năm |
| **Giải Thần** | An theo Phượng Các (đồng cung) |
| **Thiên Khốc** | Khởi Ngọ, nghịch hành theo Chi năm |
| **Thiên Hư** | Khởi Ngọ, thuận hành theo Chi năm |
| **Thiên Diêu** | Theo Tháng: Tháng 1 tại Sửu, thuận hành |
| **Thiên Y** | Theo Tháng: Tháng 1 tại Sửu, thuận hành (đồng cung Diêu) |
| **Thiên Tài** | Cung Mệnh + Chi năm |
| **Thiên Thọ** | Cung Thân + Chi năm |
| **Thiên Đức** | (Chi năm - 3) |
| **Nguyệt Đức** | (Chi năm + 5) |
| **Lưu Hà** | Theo Can năm (Giáp→Dậu, Ất→Tuất...) |
| **LN.Văn Tinh** | Theo Can năm (Giáp→Tỵ, Ất→Ngọ...) |

### 7.7 Các Sao Lưu Niên (Annual Stars)

Tính theo năm xem hạn (Viewing Year):

| Sao Lưu | Công Thức |
|---------|-----------|
| **Lưu Thái Tuế** | Tại cung có Chi = Chi năm xem |
| **Lưu Lộc Tồn** | Theo Can năm xem |
| **Lưu Kình/Đà** | Trước/Sau Lưu Lộc Tồn |
| **Lưu Thiên Mã** | Theo Tam Hợp Chi năm xem (DầnNgọTuất→Thân...) |
| **Lưu Khốc/Hư** | Khởi Ngọ, nghịch/thuận theo Chi năm xem |
| **Lưu Tứ Hóa** | Theo Can năm xem (Giáp: Liêm Phá Vũ Dương...) |

---

## 8. Áp Dụng Tứ Hóa

### 8.1 Bảng Tứ Hóa (Code Reference)
**Code Reference:** `python/stars/tu_hoa_applier.py`

| Can Năm | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|---------|---------|-----------|----------|--------|
| Giáp | Liêm Trinh | Phá Quân | Vũ Khúc | Thái Dương |
| Ất | Thiên Cơ | Thiên Lương | Tử Vi | Thái Âm |
| Bính | Thiên Đồng | Thiên Cơ | Văn Xương | Liêm Trinh |
| Đinh | Thái Âm | Thiên Đồng | Thiên Cơ | Cự Môn |
| Mậu | Tham Lang | Thái Âm | Hữu Bật | Thiên Cơ |
| Kỷ | Vũ Khúc | Tham Lang | Thiên Lương | Văn Khúc |
| Canh | Thái Dương | Vũ Khúc | Thái Âm | Thiên Đồng |
| Tân | Cự Môn | Thái Dương | Văn Khúc | Văn Xương |
| Nhâm | Thiên Lương | Tử Vi | Tả Phù | Vũ Khúc |
| Quý | Phá Quân | Cự Môn | Thái Âm | Tham Lang |

### 8.2 Ý Nghĩa Tứ Hóa

| Hóa | Ý nghĩa |
|-----|---------|
| Hóa Lộc | Tài lộc, may mắn, cơ hội |
| Hóa Quyền | Quyền lực, kiểm soát, thăng tiến |
| Hóa Khoa | Danh tiếng, học vấn, uy tín |
| Hóa Kỵ | Trở ngại, khó khăn, cần cẩn thận |

### 7.8 An Tuần - Triệt
**Code Reference:** `python/stars/tuan_triet_placer.py`

#### 7.8.1 Triệt (Triệt Lộ Không Vong)
- **Nguyên lý:** Dựa trên Can Năm.
- **Công thức Code:** `(8 - (Can % 5) * 2) % 12`
- **Ví dụ:** Giáp (0) -> Thân (8).

#### 7.8.2 Tuần (Tuần Trung Không Vong)
- **Nguyên lý:** Dựa trên "Nhà Giáp" của năm sinh (Vòng 10 năm).
- **Công thức Code:** `(Chi - Can + 10) % 12`

---

## 9. Luận Giải Lá Số

### 9.1 Phân Tích Cung Mệnh

1. Xem Chính Tinh tọa thủ
2. Đánh giá Phụ Tinh cát/sát
3. Kiểm tra Tứ Hóa ảnh hưởng
4. Xét tương quan với Cung Thân

### 9.2 Đánh Giá Cách Cục

| Cách Cục | Điều Kiện |
|----------|-----------|
| Tử Phủ Vũ Tướng | Tử Vi + Thiên Phủ/Vũ Khúc/Thiên Tướng |
| Sát Phá Liêm Tham | Thất Sát + Phá Quân + Liêm Trinh + Tham Lang |
| Nhật Nguyệt Tịnh Minh | Thái Dương + Thái Âm ở vị trí miếu vượng |
| Song Lộc | Lộc Tồn + Hóa Lộc cùng cung |
| Lộc Mã Giao Trì | Lộc Tồn + Thiên Mã |

### 9.3 Xét 12 Cung

| Cung | Đại diện |
|------|----------|
| Mệnh | Bản thân, tính cách |
| Phụ Mẫu | Cha mẹ, học vấn |
| Phúc Đức | Phúc phần, tâm linh |
| Điền Trạch | Nhà cửa, bất động sản |
| Quan Lộc | Sự nghiệp, công việc |
| Nô Bộc | Bạn bè, cấp dưới |
| Thiên Di | Du lịch, quý nhân ngoại |
| Tật Ách | Sức khỏe, bệnh tật |
| Tài Bạch | Tiền bạc, tài chính |
| Tử Tức | Con cái |
| Phu Thê | Hôn nhân |
| Huynh Đệ | Anh chị em |

---

## Phụ Lục: File Code Reference

| File | Chuc nang |
|------|-----------|
| `core/lunar_converter.py` | Chuyen doi Am Duong lich |
| `core/can_chi_calc.py` | Tinh Can Chi |
| `core/cung_menh.py` | Tinh Cung Menh/Than |
| `core/cuc_calc.py` | Xac dinh Cuc, Nap Am |
| `stars/chinh_tinh_placer.py` | An 14 Chinh Tinh |
| `stars/luc_cat_placer.py` | An Luc Cat Tinh |
| `stars/luc_sat_placer.py` | An Luc Sat Tinh |
| `stars/truong_sinh_placer.py` | An Vong Truong Sinh |
| `stars/bac_sy_placer.py` | An Vong Bac Sy |
| `stars/thai_tue_placer.py` | An Vong Thai Tue |
| `stars/tu_hoa_applier.py` | Ap dung Tu Hoa |
| `chart/chart_builder.py` | Lap la so hoan chinh |
| `interpretation/chart_analyzer.py` | Luan giai la so |
| `logic/reverse_lookup_engine.py` | Tim gio sinh nguoc (Finder Tool) |

---

---

## 16. BỔ SUNG NGUYÊN TẮC & CÔNG THỨC (20/12/2025)

Dựa trên tài liệu tổng hợp các khẩu quyết và nguyên lý cốt lõi:

### 16.1 Nguyên Tắc Cốt Lõi
**Công thức:** `Tính Chất = Ngũ Hành + Hóa Khí`
- Ví dụ: Thiên Phủ (Dương Thổ) + Lệnh Tinh = Quản lý, bao bọc.
- Ví dụ: Tử Vi (Âm Thổ) + Tôn Quý = Phúc thọ, quyền lực.

### 16.2 Quy Tắc An Sao & Vị Trí Cung
1.  **Cung An Thân theo Giờ:**
    - Giờ Dần (3h-5h): Thân cư Quan Lộc.
    - Giờ Mão (5h-7h): Thân cư Thiên Di.
2.  **Đổi Ngày Giờ Tý:**
    - Từ 23:00 được tính là giờ Tý của ngày hôm sau.
3.  **Ngũ Hành 12 Cung:**
    - Mộc: Dần, Mão
    - Hỏa: Tỵ, Ngọ
    - Kim: Thân, Dậu
    - Thủy: Hợi, Tý
    - Thổ: Thìn, Tuất, Sửu, Mùi (Tứ Mộ)

### 16.3 Công Thức An Phụ Tinh (Chi Tiết)
1.  **Tả Phù - Hữu Bật:**
    - Tả Phù: Khởi Thìn, đi thuận theo tháng.
    - Hữu Bật: Khởi Tuất, đi nghịch theo tháng.
    - *Đồng cung:* Tại Sửu (tháng 10), Tại Mùi (tháng 4).
2.  **Văn Xương - Văn Khúc:**
    - Văn Xương: Khởi Tuất, đi nghịch theo giờ.
    - Văn Khúc: Khởi Thìn, đi thuận theo giờ.
3.  **Ân Quang - Thiên Quý:**
    - Ân Quang: Từ cung Xương, đếm thuận theo ngày (lùi 1 cung).
    - Thiên Quý: Từ cung Khúc, đếm nghịch theo ngày (lùi 1 cung).
4.  **Giải Thần:**
    - Khởi Tuất (năm Tý), đi nghịch đến năm sinh.
5.  **Thiên Giải - Địa Giải:**
    - Thiên Giải: Khởi Thân, thuận theo tháng.
    - Địa Giải: Khởi Mùi, thuận theo tháng.
6.  **Phục Binh:**
    - Đi theo vòng Lộc Tồn (Vị trí thứ 11).
    - Dương Nam/Âm Nữ: Thuận.
    - Âm Nam/Dương Nữ: Nghịch.

### 16.4 Sao Lưu (Theo Năm)
1.  **Lưu Thái Tuế:** Theo Chi năm hiện tại (Năm Mão tại cung Mão).
2.  **Lưu Tang Môn:** Đối cung với Lưu Bạch Hổ, hoặc cách Lưu Thái Tuế theo chiều thuận/nghịch (Quy tắc: Tiền Tuế hậu Tang).
    - *Chính xác:* Tang Môn cố định ở vị trí cách Thái Tuế +2 cung (Thái Tuế -> Thiếu Dương -> Tang Môn). Vậy Lưu Tang Môn cũng cách Lưu Thái Tuế 2 cung.
3.  **Lưu Thiên Mã:** Theo Tam Hợp Chi năm hiện tại (Dần Ngọ Tuất -> Thân).
4.  **Lưu Lộc Tồn:** Theo Can năm hiện tại. (Kèm Lưu Kình Dương, Lưu Đà La).

### 16.5 Quy Luật Phối Hợp & Đối Trọng
1.  **Đối Cung:**
    - Thiên Phủ <> Thất Sát.
    - Thiên Tướng <> Phá Quân.
    - Phục Binh <> Tướng Quân.
2.  **Nhị Hợp:**
    - Thái Dương <> Thiên Phủ.
    - Thái Âm <> Vũ Khúc.
    - Tham Lang <> Thiên Đồng.
    - Thiên Lương <> Thất Sát.
3.  **Tuần - Triệt:**
    - Triệt (Kim): Phá bỏ, kìm hãm. Vị trí theo Can (Giáp Kỷ -> Thân Dậu...).
    - Tuần (Mộc): Bao bọc, bó buộc. Vị trí theo dư của Can Chi năm (vòng 10 năm).

### 16.6 Hình Dáng & Sự Kiện
- **Tử Vi:** Mặt vuông, lưng dày. Gặp Triệt mập, gặp Tuần cao.
- **Hạn Sinh Tử:** Trẻ sợ Thất Sát, Trung niên sợ Phá Quân, Già sợ Tham Lang.

---

## 17. KẾ HOẠCH KIỂM TRA CÔNG THỨC (VERIFICATION PLAN)

### Mục tiêu
Đảm bảo toàn bộ công thức trên được phản ánh đúng trong Source Code (`python/`).

### Checklist Kiểm Tra
1.  [ ] **Kiểm tra Tuần/Triệt:** Xác thực nguyên lý Ngũ Hành (Triệt=Kim, Tuần=Mộc) có ảnh hưởng đến luận giải không.
2.  [ ] **Verification Phụ Tinh:**
    - [ ] Ân Quang / Thiên Quý (Check offset ngày).
    - [ ] Giải Thần (Check logic khởi Tuất).
    - [ ] Thiên Giải / Địa Giải.
3.  [ ] **Verification Sao Lưu:**
    - [ ] Lưu Tang Môn (Vị trí tương đối vs Lưu Thái Tuế).
    - [ ] Lưu Lộc Tồn (Theo Can năm xem hạn).
4.  [ ] **Unit Tests:** Tạo file `tests/verify_formulas_2025.py` để chạy các case cụ thể (Ngày Giờ đổi Tý, Ân Quang Thiên Quý).

---
*Tài liệu được cập nhật lần cuối: 28/12/2025*

---

## 18. CÁC CẬP NHẬT CÔNG THỨC & LOGIC (28/12/2025)

### 18.1 Tính Tiểu Hạn (Minor Age Cycle)
**Code Reference:** `python/core/fortune_periods.py`

Tiểu Hạn là hạn của 1 năm, chu kỳ 12 năm lặp lại vị trí (nhưng khác Thiên Can Lưu Niên).

**1. Xác Định Cung Khởi Tiểu Hạn:**
Dựa trên **Tam Hợp Chi Năm Sinh** (Tam Hợp Cục):
- **Dần - Ngọ - Tuất**: Khởi tại **Thìn**.
- **Thân - Tý - Thìn**: Khởi tại **Tuất**.
- **Tỵ - Dậu - Sửu**: Khởi tại **Mùi**.
- **Hợi - Mão - Mùi**: Khởi tại **Sửu**.

*(Khẩu quyết: Dần Ngọ Tuất khởi Thìn, Thân Tý Thìn khởi Tuất, Tỵ Dậu Sửu khởi Mùi, Hợi Mão Mùi khởi Sửu)*

**2. Chiều Đếm (Direction):**
- **Nam (Dương/Âm)**: Luôn đi **Thuận**.
- **Nữ (Dương/Âm)**: Luôn đi **Nghịch**.
*(Khác với Đại Hạn tính theo Âm Dương Năm Sinh, Tiểu Hạn chỉ tính theo Giới Tính)*

**3. Công Thức:**
- `Start Position = Lookup(Year_Chi)`
- `Offset = Age - 1` (Tuổi Mụ)
- `Tiểu Hạn = (Start + Direction * Offset) % 12`

### 18.2 Hệ Thống Màu Sắc Ngũ Hành (Star Colors)
**Code Reference:** `python/data/star_colors.py`

Mỗi sao được gán một màu sắc cố định dựa trên Ngũ Hành của nó để hiển thị trực quan:

| Ngũ Hành | Màu Sắc | Mã Màu (Hex) | Ví dụ |
|---|---|---|---|
| **Kim** | Vàng Sáng / Trắng | `#f1c40f` | Vũ Khúc, Thất Sát |
| **Mộc** | Xanh Lá | `#2ecc71` | Thiên Cơ, Thiên Lương |
| **Thủy** | Xám / Đen / Xanh Dương | `#7f8c8d` | Thiên Đồng, Thái Âm |
| **Hỏa** | Đỏ / Tím | `#e74c3c` | Thái Dương, Liêm Trinh |
| **Thổ** | Nâu / Cam Đất | `#d35400` | Thiên Phủ, Tử Vi |

### 18.3 Phân Loại Sao (Star Nature)
**Code Reference:** `python/data/star_nature.py`

Chuẩn hóa lại phân loại Cát/Hung tinh cho hiển thị:
- **Chính Tinh (14 sao)**: Được hiển thị riêng ở giữa cung, size lớn (16px).
- **Vòng Trường Sinh**: Hiển thị riêng biệt ở góc cung.
- **Phụ Tinh Tốt (Cát)**: Hiển thị cột bên trái, màu xanh lá cây đậm.
- **Phụ Tinh Xấu (Sát/Hung)**: Hiển thị cột bên phải, màu đỏ đậm.
    - *Lưu ý*: Các sao như **Điếu Khách**, **Phi Liêm**, **Phục Binh** được xếp vào nhóm Hung Tinh.

```
