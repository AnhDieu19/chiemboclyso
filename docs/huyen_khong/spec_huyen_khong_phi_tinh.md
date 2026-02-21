# HUYỀN KHÔNG PHI TINH - PHÁI LÍ KHÍ
## Tài liệu nghiên cứu và phát triển tính năng

---

## 1. TỔNG QUAN

### 1.1. Định nghĩa
**Huyền Không Phi Tinh** (玄空飛星) là một phương pháp an sao đặc biệt trong Tử Vi Đẩu Số, thuộc phái Lí Khí (理氣派). Phương pháp này dựa trên:
- Nguyên lý Huyền Không Phong Thủy
- Chu kỳ thời gian (Nguyên Vận, Đại Vận)
- Sự chuyển hóa của Ngũ Hành theo không gian và thời gian

### 1.2. Đặc điểm
- **Phi Tinh** (Flying Stars): Các sao "bay" theo quy luật nhất định qua 12 cung
- **Huyền Không**: Nguyên lý không gian - thời gian trong Dịch học
- **Lí Khí**: Thuộc phái nghiên cứu về khí (氣) và lý (理)

### 1.3. Quan hệ với Phái Loan Đầu (峦头派)

**Phái Lí Khí vs Phái Loan Đầu:**

| Đặc điểm | Phái Lí Khí (理氣派) | Phái Loan Đầu (峦头派) |
|----------|---------------------|----------------------|
| Trọng tâm | Thời gian, Khí vận | Không gian, Hình thế |
| Phương pháp | Tính toán theo chu kỳ | Quan sát hình địa lý |
| Ứng dụng | Phi Tinh, Vận Tinh | Địa thế, Cục diện |
| Công cụ | Lạc Thư, Hà Đồ | La Bàn, Bát Quái |

**Tích hợp Lí Khí + Loan Đầu trong Tử Vi:**
- **Lí Khí (Phi Tinh)**: Xác định thời điểm cát흉 → Khi nào tốt/xấu
- **Loan Đầu (12 Cung)**: Xác định không gian cát흉 → Cung nào tốt/xấu
- **Kết hợp**: Phi Tinh bay vào các Cung → Thời gian + Không gian = Dự đoán chính xác

**Ví dụ tích hợp:**
```
Cung Mệnh (Loan Đầu) + Bát Bạch Tinh (Lí Khí) + Năm 2024 (Vận 9)
→ Phân tích: Mệnh cung gặp Bát Bạch (Cát tinh) trong Vận 9
→ Ý nghĩa: Tài vận hanh thông, sự nghiệp thăng tiến
```

### 1.4. Lạc Thư: Tiên Thiên hay Hậu Thiên?

**Huyền Không Phi Tinh sử dụng LẠC THƯ HẬU THIÊN (後天洛書)**

#### So sánh Lạc Thư Tiên Thiên vs Hậu Thiên:

**1. Lạc Thư Tiên Thiên (先天洛書) - Hà Đồ:**
```
Thứ tự: Theo Hà Đồ
   1(N)  6
   8     5(Center)
   3     4
   2(S)  7

Đặc điểm:
- Tĩnh, bất biến
- Nguyên lý vũ trụ ban đầu
- Dùng trong phong thủy cổ truyền
```

**2. Lạc Thư Hậu Thiên (後天洛書) - Dùng trong Phi Tinh:** ✅
```
Thứ tự: Theo Lạc Thư
   4(SE)  9(S)   2(SW)
   3(E)   5      7(W)
   8(NE)  1(N)   6(NW)

Đặc điểm:
- Động, biến đổi theo thời gian
- Nguyên lý hậu thiên vạn vật
- Dùng trong Huyền Không Phi Tinh
- Chu kỳ 180 năm (9 Vận x 20 năm)
```

#### So sánh Lạc Thư các hệ thống:

**A. Lạc Thư Trung Hoa (Hậu Thiên) - Chuẩn quốc tế:**
```
   4  9  2
   3  5  7
   8  1  6

Ánh xạ Bát Quái:
- 1 = Khảm (坎) = Bắc = Thủy
- 2 = Khôn (坤) = Tây Nam = Thổ
- 3 = Chấn (震) = Đông = Mộc
- 4 = Tốn (巽) = Đông Nam = Mộc
- 5 = Trung Cung = Trung tâm = Thổ
- 6 = Càn (乾) = Tây Bắc = Kim
- 7 = Đoài (兌) = Tây = Kim
- 8 = Cấn (艮) = Đông Bắc = Thổ
- 9 = Ly (離) = Nam = Hỏa
```

**B. Lạc Thư Lạc Việt (Nếu có biến thể):**
```
※ Lưu ý: Hệ thống Lạc Việt cần nghiên cứu thêm

Có thể khác biệt:
1. Điểm xuất phát (Bắc vs Đông)
2. Chiều phi tinh (Thuận vs Nghịch)
3. Ánh xạ với 12 Chi (Tý, Sửu...)

Cần xác minh:
- Có tài liệu Lạc Việt chính thống không?
- Có dùng 12 Chi thay 8 Quái không?
- Có điều chỉnh cho múi giờ VN không?
```

**C. Công thức chuyển đổi Hà Đồ → Lạc Thư (Theo Viên Như):**

Tham khảo: [Nghiên Cứu Lịch Sử - Công thức tính Hà Đồ thành Lạc Thư](https://nghiencuulichsu.com/2019/02/13/cong-thuc-tinh-ha-do-thanh-lac-thu/)

```python
"""
Hà Đồ (河圖) = Bản thể vũ trụ (Tiên Thiên Bát Quái)
Lạc Thư (洛書) = Thế giới hiện tượng (Hậu Thiên Bát Quái)

Công thức: 1→4→3→2→1 (theo tương tác Âm-Dương)
"""

# 1. Tương tác Tung ↔ Hữu (xoay 180°)
Tung 1 (Càn-Khôn, Dương) ↔ Hữu 4 (Tốn-Cấn, Âm)
→ Hữu 4: Khôn-Càn (Âm)

# 2. Tương tác Hữu ↔ Tả (xoay 360°)
Hữu 4 (Tốn-Cấn, Âm) ↔ Tả 3 (Đoài-Chấn, Dương)
→ Tả 3: Cấn-Tốn (Dương)

# 3. Tương tác Tả ↔ Hoành (xoay 90°)
Tả 3 (Đoài-Chấn, Dương) ↔ Hoành 2 (Khảm-Ly, Âm)
→ Hoành 2: Chấn-Đoài (Âm)

# 4. Tương tác Hoành ↔ Tung (xoay 90°)
Hoành 2 (Khảm-Ly, Âm) ↔ Tung 1 (Càn-Khôn, Dương)
→ Tung 1: Khảm-Ly (Dương)

# Kết quả Lạc Thư:
#   4  9  2
#   3  5  7
#   8  1  6

# Lý số:
- Tung (Dương): Lấy số Dương 2-7 từ Hà Đồ
- Hoành (Âm): Lấy số Âm 4-9 từ Hà Đồ
- Trung tâm: 5 (10 đã hòa vào các cặp đối diện)
```

**Ý nghĩa:**
- **Hà Đồ**: Bản thể, không gian, tĩnh, "thể viên nhi dụng phương" (體圓而用方)
- **Lạc Thư**: Hiện tượng, thời gian, động, "thể phương nhi dụng viên" (體方而用圓)
- **Huyền Không Phi Tinh** dùng Lạc Thư vì có yếu tố **thời gian** (Vận 20 năm, Lưu Niên hàng năm)
- **Tử Vi Đẩu Số** dùng 12 Cung cố định, không dùng Lạc Thư (không có khái niệm phi tinh theo thời gian)

**⚠️ Lưu ý:**
```
Công thức Viên Như chứng minh Lạc Thư không phải "tùy tiện sắp xếp"
mà là kết quả tương tác Âm-Dương giữa các trục.

Tuy nhiên, đây là nghiên cứu lịch sử, chưa có consensus học thuật.
Cần xem như tài liệu tham khảo, không phải chân lý tuyệt đối.
```

---

## 2. CÁC LOẠI SAO HUYỀN KHÔNG PHI TINH

### 2.1. Cửu Tinh (九星 - 9 Sao chính)
Dựa trên Lạc Thư và Hà Đồ:

| STT | Tên sao | Ngũ Hành | Ý nghĩa | Cát/흉 |
|-----|---------|----------|---------|--------|
| 1 | Nhất Bạch (一白) | Thủy | Tham Lang | Cát |
| 2 | Nhị Hắc (二黑) | Thổ | Cự Môn | Hung |
| 3 | Tam Bích (三碧) | Mộc | Lộc Tồn | Hung |
| 4 | Tứ Lục (四綠) | Mộc | Văn Khúc | Cát |
| 5 | Ngũ Hoàng (五黃) | Thổ | Liêm Trinh | Hung |
| 6 | Lục Bạch (六白) | Kim | Vũ Khúc | Cát |
| 7 | Thất Xích (七赤) | Kim | Phá Quân | Hung |
| 8 | Bát Bạch (八白) | Thổ | Tả Phù | Cát |
| 9 | Cửu Tử (九紫) | Hỏa | Hữu Bật | Cát |

### 2.2. Đặc tính các sao
- **Cát tinh**: 1, 4, 6, 8, 9
- **Hung tinh**: 2, 3, 5, 7
- **Ngũ Hoàng (5)**: Hung tinh mạnh nhất, tượng trưng tai họa

---

## 3. NGUYÊN LÝ AN SAO

### 3.1. Nguyên Vận (元運)
Chu kỳ 180 năm chia thành 3 Nguyên, mỗi Nguyên 60 năm:
- **Thượng Nguyên** (上元): Vận 1-2-3 (1864-1923)
- **Trung Nguyên** (中元): Vận 4-5-6 (1924-1983)
- **Hạ Nguyên** (下元): Vận 7-8-9 (1984-2043)

### 3.2. Đại Vận (大運)
Mỗi Vận kéo dài 20 năm:
- Vận 1: 1864-1883
- Vận 2: 1884-1903
- Vận 3: 1904-1923
- Vận 4: 1924-1943
- Vận 5: 1944-1963
- Vận 6: 1964-1983
- Vận 7: 1984-2003
- **Vận 8**: 2004-2023
- **Vận 9**: 2024-2043 ← Hiện tại

### 3.2bis. Lưu Niên, Lưu Nguyệt, Lưu Nhật, Lưu Thì

**Các tầng Phi Tinh theo thời gian:**

#### A. Lưu Niên (流年 - Yearly Flying Stars)
```python
def get_yearly_star(base_year=2024):
    """
    Lưu Niên: Phi tinh theo năm
    Công thức: (Năm hiện tại - Năm gốc) mod 9 + 1
    """
    base_star = 9  # Vận 9 (2024-2043)
    current_year = datetime.now().year
    offset = (current_year - base_year) % 9
    yearly_star = (base_star + offset - 1) % 9 + 1
    return yearly_star

# Ví dụ:
# 2024 → Sao 9 (Vận 9)
# 2025 → Sao 1 (9+1=10, 10%9=1)
# 2026 → Sao 2
# ...
```

#### B. Lưu Nguyệt (流月 - Monthly Flying Stars)
```python
def get_monthly_star(year, month):
    """
    Lưu Nguyệt: Phi tinh theo tháng
    
    Công thức dựa theo Tiết Khí:
    - Tháng 1 (Dần): Lập Xuân → Kinh Trập
    - Tháng 2 (Mão): Kinh Trập → Thanh Minh
    - ...
    
    Lưu Nguyệt Tinh = (Lưu Niên Tinh + Tháng - 1) mod 9
    """
    yearly_star = get_yearly_star(year)
    
    # Tháng 1 = Dần, Tháng 2 = Mão, ...
    # Cần convert từ tháng dương lịch sang tháng Can Chi
    lunar_month = convert_to_lunar_month(year, month)
    
    monthly_star = (yearly_star + lunar_month - 1) % 9
    if monthly_star == 0:
        monthly_star = 9
    
    return monthly_star
```

#### C. Lưu Nhật (流日 - Daily Flying Stars) ⚠️ Phức tạp
```python
def get_daily_star(year, month, day):
    """
    Lưu Nhật: Phi tinh theo ngày
    
    Cực kỳ phức tạp, cần:
    1. Tính Can Chi của ngày (Giáp Tý, Ất Sửu...)
    2. Xác định Tiết Khí
    3. Phi tinh từ Lưu Nguyệt
    
    Công thức:
    - Ngày 1 của tháng = Lưu Nguyệt Tinh
    - Các ngày sau: Phi theo thứ tự Lạc Thư
    
    ⚠️ Warning: 
    - Rất phức tạp, dễ sai
    - Ít được dùng trong thực tế
    - Khuyến nghị: Không implement giai đoạn đầu
    """
    monthly_star = get_monthly_star(year, month)
    
    # Simplified version (có thể không chính xác 100%)
    day_offset = day % 9
    daily_star = (monthly_star + day_offset - 1) % 9
    if daily_star == 0:
        daily_star = 9
    
    return daily_star
```

#### D. Lưu Thì (流时 - Hourly Flying Stars) ⚠️⚠️ Cực phức tạp
```python
def get_hourly_star(year, month, day, hour):
    """
    Lưu Thì: Phi tinh theo giờ (12 Giờ Thần)
    
    Cực kỳ phức tạp:
    - Cần Can Chi chính xác của ngày
    - Phi từ Lưu Nhật Tinh
    - Dựa vào 12 Địa Chi (Tý, Sửu, Dần...)
    
    ⚠️⚠️ Extreme Warning:
    - Độ chính xác thấp nếu không có công thức chuẩn
    - Rất ít sách viết về Lưu Thì
    - Khuyến nghị: KHÔNG implement
    """
    daily_star = get_daily_star(year, month, day)
    
    # Hour: 0-23 → Chi: 0-11 (Tý-Hợi)
    chi_index = (hour // 2) % 12
    
    hourly_star = (daily_star + chi_index) % 9
    if hourly_star == 0:
        hourly_star = 9
    
    return hourly_star
```

#### Khuyến nghị Implementation:
```python
# Phase 1: ✅ Implement
- Vận Tinh (20 năm)
- Lưu Niên (hàng năm)

# Phase 2: ⚠️ Optional
- Lưu Nguyệt (hàng tháng)

# Phase 3: ❌ Không khuyến nghị
- Lưu Nhật (quá phức tạp, ít dùng)
- Lưu Thì (cực phức tạp, gần như không dùng)
```

### 3.3. Quy luật phi tinh
```
Số Vận hiện tại → Vị trí trung tâm
└─→ Các sao khác bay theo thứ tự Lạc Thư
    Thuận phi (順飛): 1→2→3→4→5→6→7→8→9→1
    Nghịch phi (逆飛): 9→8→7→6→5→4→3→2→1→9
```

---

## 4. CÁCH TÍNH VÀ AN SAO

### 4.0. Tận dụng code Tử Vi hiện có

**✅ Các hàm có thể tái sử dụng:**

```python
# Từ python/core/calendar_converter.py
from core.calendar_converter import CalendarConverter

# 1. Chuyển đổi lịch Âm-Dương
converter = CalendarConverter()
lunar_date = converter.solar_to_lunar(2024, 1, 15)
# → Trả về: (lunar_year, lunar_month, lunar_day, is_leap)

# 2. Tính Can Chi của năm, tháng, ngày
from core.can_chi import calculate_can_chi
can_chi_data = calculate_can_chi(2024, 1, 15, 12)
# → Trả về: {
#     'year_can': 'Giáp', 'year_chi': 'Thìn',
#     'month_can': 'Bính', 'month_chi': 'Dần',
#     'day_can': 'Nhân', 'day_chi': 'Tý',
#     'hour_chi': 'Ngọ'
# }

# 3. Tính vị trí 12 cung
from logic.cung_calculator import CungCalculator
cung_calc = CungCalculator(lunar_month, hour_chi_index)
menh_cung = cung_calc.calculate_cung_positions()
# → Trả về: {'Menh': 0, 'Phu_The': 1, 'Phuc_Duc': 2, ...}

# 4. Ngũ Hành tương sinh/tương khắc
from logic.ngu_hanh_engine import NguHanhEngine
relation = NguHanhEngine.get_relation('Mộc', 'Thổ')
# → Trả về: 'khac' hoặc 'sinh' hoặc 'neutral'

# 5. Ánh xạ tên sao (có dấu ↔ không dấu)
from graph.static.js.star_mapping import STAR_NAME_MAP
normalized = normalize_star_name('Thái Âm')
# → Trả về: 'thai_am'
```

**❌ Các hàm cần viết mới:**

```python
# 1. Xác định Vận (20 năm)
def get_current_yun(year):
    """Chưa có trong Tử Vi, cần viết mới"""
    pass

# 2. Ánh xạ Lạc Thư → 12 Cung
def map_luo_shu_to_12_cung():
    """
    Huyền Không: 9 số Lạc Thư → 12 Cung
    Tử Vi: 12 Cung cố định
    → Cần xác định logic ánh xạ
    """
    pass

# 3. Thuật toán phi tinh (thuận/nghịch)
def fly_stars_algorithm(center_star, direction='forward'):
    """
    Lạc Thư phi tinh theo thứ tự 1→2→3...→9
    Khác với Tử Vi (không có khái niệm này)
    """
    pass

# 4. Tính Lưu Niên, Lưu Nguyệt (nếu implement)
def get_yearly_star(base_year, current_year):
    """Phi tinh hàng năm, chưa có trong Tử Vi"""
    pass
```

**📊 Ước lượng:**
- **Code tái sử dụng**: ~70% (calendar, can chi, cung, ngũ hành)
- **Code mới**: ~30% (vận, phi tinh, lạc thư mapping)
- **Thời gian tiết kiệm**: ~40% nhờ tận dụng core Tử Vi

**⚠️ Lưu ý:**
```python
# Tử Vi có 12 Cung cố định:
CHI_NAMES = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 
             'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

# Huyền Không có 9 Sao + 8 Quái:
FLYING_STARS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
BA_QUAT = ['Khảm', 'Khôn', 'Chấn', 'Tốn', 'Càn', 'Đoài', 'Cấn', 'Ly']

# → Cần mapping 9 sao vào 12 cung (có 3 cung trùng)
```

### 4.1. Xác định Vận hiện tại
```python
def get_current_yun(year):
    """
    Xác định Vận dựa vào năm
    2024-2043: Vận 9
    """
    if 1864 <= year <= 1883: return 1
    elif 1884 <= year <= 1903: return 2
    elif 1904 <= year <= 1923: return 3
    elif 1924 <= year <= 1943: return 4
    elif 1944 <= year <= 1963: return 5
    elif 1964 <= year <= 1983: return 6
    elif 1984 <= year <= 2003: return 7
    elif 2004 <= year <= 2023: return 8
    elif 2024 <= year <= 2043: return 9
    else: return None
```

### 4.2. Thứ tự phi tinh theo Lạc Thư
```
Cung vị trí theo Lạc Thư:
   4  9  2
   3  5  7
   8  1  6
```

Ánh xạ sang 12 cung Tử Vi:
```
Dần(4) - Mão(9) - Thìn(2)
Sửu(3) - [5]    - Tỵ(7)
Tý(8)  - Hợi(1) - Ngọ(6)
```

### 4.3. Algorithm an sao cơ bản
```python
def an_huyen_khong_phi_tinh(year, month, day, hour, menh_cung_position):
    """
    An Huyền Không Phi Tinh vào 12 cung
    
    Input:
        - year: Năm sinh
        - month: Tháng sinh
        - day: Ngày sinh
        - hour: Giờ sinh
        - menh_cung_position: Vị trí cung Mệnh (0-11)
    
    Output:
        - Dictionary: {cung_position: [list_of_stars]}
    """
    
    # 1. Xác định Vận hiện tại
    yun = get_current_yun(year)
    
    # 2. Xác định sao trung tâm (Vận Tinh)
    center_star = yun
    
    # 3. An sao theo Lạc Thư (thuận phi hoặc nghịch phi)
    # Dựa vào Âm/Dương của năm và Mệnh cung
    is_yang_year = is_yang_year(year)
    
    # 4. Phi tinh từ trung tâm ra 8 cung
    star_positions = fly_stars(center_star, is_yang_year)
    
    # 5. Tính sao Thái Tuế (流年飛星)
    yearly_stars = fly_yearly_stars(year, star_positions)
    
    # 6. Tính sao Tháng (流月飛星)
    monthly_stars = fly_monthly_stars(month, star_positions)
    
    return {
        'base_stars': star_positions,
        'yearly_stars': yearly_stars,
        'monthly_stars': monthly_stars
    }
```

### 4.4. Thuận phi vs Nghịch phi
```python
def fly_stars(center_star, is_yang):
    """
    Phi tinh từ trung tâm theo Lạc Thư
    
    Thuận phi (Yang): 1→2→3→4→5→6→7→8→9
    Nghịch phi (Âm): 9→8→7→6→5→4→3→2→1
    """
    luo_shu_positions = [
        (1, 'Hợi'),  # Khảm - Bắc
        (2, 'Thìn'), # Khôn - Tây Nam
        (3, 'Sửu'),  # Chấn - Đông
        (4, 'Dần'),  # Tốn - Đông Nam
        (5, None),   # Trung tâm - không có cung
        (6, 'Ngọ'),  # Càn - Tây Bắc
        (7, 'Tỵ'),   # Đoài - Tây
        (8, 'Tý'),   # Cấn - Đông Bắc
        (9, 'Mão')   # Ly - Nam
    ]
    
    result = {}
    
    for i, (pos, cung_name) in enumerate(luo_shu_positions):
        if pos == 5:
            continue  # Skip center
            
        if is_yang:
            star_number = (center_star + i - 1) % 9 + 1
        else:
            star_number = (center_star - i + 1) % 9
            if star_number == 0:
                star_number = 9
        
        result[cung_name] = star_number
    
    return result
```

---

## 5. TƯƠNG SINH TƯƠNG KHẮC

### 5.1. Quan hệ Ngũ Hành giữa các sao
```
Sinh (Cát):
- Thủy sinh Mộc: 1 + 3,4
- Mộc sinh Hỏa: 3,4 + 9
- Hỏa sinh Thổ: 9 + 2,5,8
- Thổ sinh Kim: 2,5,8 + 6,7
- Kim sinh Thủy: 6,7 + 1

Khắc (Hung):
- Kim khắc Mộc: 6,7 khắc 3,4
- Mộc khắc Thổ: 3,4 khắc 2,5,8
- Thổ khắc Thủy: 2,5,8 khắc 1
- Thủy khắc Hỏa: 1 khắc 9
- Hỏa khắc Kim: 9 khắc 6,7
```

### 5.2. Tổ hợp đặc biệt
- **1-4 Đồng cung**: Văn Xương Văn Khúc hội, Cát về văn chương
- **2-5 Đồng cung**: Bệnh Phù hội, Hung về bệnh tật
- **6-7 Đồng cung**: Kim Kim tranh đấu, hung về quan tai
- **8-9 Đồng cung**: Tài vượng, Cát về tài lộc

---

## 6. THIẾT KẾ HỆ THỐNG

### 6.1. Data Model
```python
class HuyenKhongPhiTinh:
    """
    Model lưu trữ thông tin Huyền Không Phi Tinh
    """
    star_number: int  # 1-9
    star_name: str    # Nhất Bạch, Nhị Hắc, ...
    ngu_hanh: str     # Thủy, Mộc, Hỏa, Thổ, Kim
    nature: str       # cat/hung
    position: int     # 0-11 (12 cung)
    star_type: str    # base/yearly/monthly/daily/hourly
```

### 6.2. API Endpoints
```python
# 1. Calculate Huyền Không Phi Tinh
POST /api/huyen-khong/calculate
Body: {
    "year": 1994,
    "month": 3,
    "day": 28,
    "hour": 0,  # Giờ Tý
    "gender": "nam",
    "calendar": "solar"
}

Response: {
    "status": "success",
    "data": {
        "yun": 8,  # Vận 8 (năm 1994)
        "base_stars": {
            "0": [{"star": 8, "name": "Bát Bạch", "ngu_hanh": "Thổ"}],
            "1": [{"star": 3, "name": "Tam Bích", "ngu_hanh": "Mộc"}],
            ...
        },
        "yearly_stars": {...},
        "monthly_stars": {...},
        "combinations": [
            {
                "position": 0,
                "stars": [8, 9],
                "meaning": "Tài vượng - Cát về tài lộc"
            }
        ]
    }
}
```

### 6.3. Frontend Components
```javascript
// components/HuyenKhongPanel.js
class HuyenKhongPanel {
    constructor() {
        this.baseStars = null;
        this.yearlyStars = null;
        this.monthlyStars = null;
    }
    
    // Render Phi Tinh lên 12 cung
    renderStars(chartData) {
        // Hiển thị các sao Phi Tinh trên visualization
    }
    
    // Toggle hiển thị các loại sao
    toggleStarLayer(layerType) {
        // base, yearly, monthly, daily, hourly
    }
    
    // Phân tích tổ hợp
    analyzeCombinations() {
        // Phân tích các tổ hợp đặc biệt
    }
}
```

---

## 7. UI/UX DESIGN

### 7.1. Layout mới - Separate Page
```
┌────────────────────────────────────────────────────────┐
│ HUYỀN KHÔNG PHI TINH                   [Về Tử Vi Chính]│
├────────────────────────────────────────────────────────┤
│ Nhập thông tin:                                        │
│ Năm: [____] Tháng: [__] Ngày: [__] Giờ: [__:__]      │
│ Giới tính: ○ Nam  ○ Nữ   Lịch: ○ Dương  ○ Âm         │
│                                     [Tính Phi Tinh]    │
├────────────────────────────────────────────────────────┤
│ Học phái: ⦿ Đàm Dưỡng Ngô  ○ Thẩm Thị                │
│                                                        │
│ Các tầng Phi Tinh:                                     │
│ ☑ Vận Tinh (20 năm)        ☑ Lưu Niên (1 năm)         │
│ ☑ Lưu Nguyệt (1 tháng)     ☐ Lưu Nhật (1 ngày) ⚠️     │
│ ☐ Lưu Thì (2 giờ) ⚠️⚠️                                 │
│                                                        │
│ ⚠️ Cảnh báo: Lưu Nhật và Lưu Thì có độ phức tạp cao   │
├────────────────────────────────────────────────────────┤
│                  12 CUNG PHI TINH                      │
│                                                        │
│  ┌──────┬──────┬──────┬──────┐                        │
│  │ Tỵ   │ Ngọ  │ Mùi  │ Thân │  Mỗi cung hiển thị:   │
│  │ [7]  │ [6]  │ [2]  │ [4]  │  • Tên cung           │
│  ├──────┼──────┼──────┼──────┤  • Số sao (1-9)       │
│  │ Thìn │      │      │ Dậu  │  • Màu Cát/Hung       │
│  │ [8]  │ TRUNG│      │ [9]  │  • Icon Ngũ Hành      │
│  ├──────┤      │      ├──────┤  • Lưu Niên (nếu có)  │
│  │ Mão  │      │      │ Tuất │  • Lưu Nguyệt         │
│  │ [3]  │      │      │ [5]  │  • Tổ hợp đặc biệt    │
│  ├──────┼──────┼──────┼──────┤                        │
│  │ Dần  │ Sửu  │ Tý   │ Hợi  │                        │
│  │ [1]  │ [6]  │ [7]  │ [8]  │                        │
│  └──────┴──────┴──────┴──────┘                        │
│                                                        │
├────────────────────────────────────────────────────────┤
│ PHÂN TÍCH TỔ HỢP:                                      │
│ • Cung Mệnh (Dần): Sao 1 (Nhất Bạch - Thủy) - CÁT     │
│   → Tài lộc hanh thông, trí tuệ sáng suốt             │
│                                                        │
│ • Cung Thân: Sao 2+5 (Nhị Hắc + Ngũ Hoàng) - HUNG     │
│   → ⚠️ Bệnh Phù hội, cẩn thận về sức khỏe             │
└────────────────────────────────────────────────────────┘
```

### 7.2. Color Scheme
```css
/* Cát tinh (1, 4, 6, 8, 9) */
.phi-tinh-cat {
    background: linear-gradient(135deg, #4CAF50 0%, #81C784 100%);
    color: white;
}

/* Hung tinh (2, 3, 5, 7) */
.phi-tinh-hung {
    background: linear-gradient(135deg, #F44336 0%, #E57373 100%);
    color: white;
}

/* Ngũ Hoàng - Hung tinh mạnh nhất */
.phi-tinh-ngu-hoang {
    background: linear-gradient(135deg, #000000 0%, #424242 100%);
    color: #FFEB3B;
    font-weight: bold;
}
```

### 7.3. Star Display
```html
<div class="phi-tinh-badge phi-tinh-cat">
    <span class="star-number">8</span>
    <span class="star-name">Bát Bạch</span>
    <span class="ngu-hanh-icon">⛰️</span> <!-- Thổ -->
</div>
```

---

## 8. IMPLEMENTATION PLAN

### Phase 1: Backend Core Logic (Week 1-2)
- [ ] Create `python/logic/huyen_khong_engine.py`
  - [ ] Implement Vận calculation (20-year cycles)
  - [ ] Implement Lạc Thư to 12 Cung mapping
  - [ ] Implement fly_stars algorithm (Thuận/Nghịch phi)
  - [ ] Support both schools: Đàm Dưỡng Ngô & Thẩm Thị
- [ ] Create `python/logic/huyen_khong_liu_calculator.py`
  - [ ] Lưu Niên (yearly) calculation
  - [ ] Lưu Nguyệt (monthly) calculation
  - [ ] Lưu Nhật (daily) calculation with Can Chi
  - [ ] Lưu Thì (hourly) calculation with 12 Giờ Thần
- [ ] Unit tests for all calculations

### Phase 2: Backend API (Week 2)
- [ ] Create `python/graph/blueprints/huyen_khong_bp.py`
- [ ] Create model `HuyenKhongPhiTinh` in `python/core/models.py`
- [ ] API endpoint `POST /api/huyen-khong/calculate`
  - [ ] Input: birth date, gender, school selection
  - [ ] Output: Vận, 5 layers of stars, combinations
- [ ] Integration tests with existing calendar_converter

### Phase 3: Frontend New Page (Week 3-4)
- [ ] Create new route `/huyen-khong` in `app.py`
- [ ] Create `python/graph/templates/huyen_khong.html`
  - [ ] Birth date/time input form
  - [ ] School selection toggle (Đàm Dưỡng Ngô / Thẩm Thị)
  - [ ] Time layer checkboxes (5 layers)
  - [ ] Warning messages for Lưu Nhật/Lưu Thì
- [ ] Create `python/graph/static/js/huyen_khong.js`
  - [ ] Form submission handler
  - [ ] API call to `/api/huyen-khong/calculate`
  - [ ] Render 12 Cung grid with flying stars
  - [ ] Color-coding by Cát/Hung
  - [ ] Layer toggle functionality

### Phase 4: Visualization & Analysis (Week 4-5)
- [ ] CSS styling for Phi Tinh badges
  - [ ] Cát tinh: Green gradient
  - [ ] Hung tinh: Red gradient
  - [ ] Ngũ Hoàng: Black/yellow warning style
- [ ] Ngũ Hành icons (Thủy/Mộc/Hỏa/Thổ/Kim)
- [ ] Special combination detection
  - [ ] 1-4 Văn Xương Văn Khúc
  - [ ] 2-5 Bệnh Phù
  - [ ] 6-7 Kim Kim tranh đấu
  - [ ] 8-9 Tài vượng
- [ ] Interpretation panel with analysis text

### Phase 5: Testing & Documentation (Week 5-6)
- [ ] E2E tests for full user flow
- [ ] Test both schools produce correct results
- [ ] Test all 5 time layers
- [ ] Performance optimization
- [ ] Write user guide documentation
- [ ] Add help tooltips in UI

**Tổng thời gian ước tính: 6-7 tuần**

---

## 9. TÀI LIỆU THAM KHẢO

### 9.1. Lý thuyết
- Huyền Không Đại Quái (玄空大卦)
- Phi Tinh Đẩu Số (飛星斗數)
- Lạc Thư Cửu Tinh (洛書九星)

### 9.2. Công thức
```
Vận Tinh = ((Year - 1864) / 20) + 1
Thuận Phi: Dương Nam / Âm Nữ
Nghịch Phi: Âm Nam / Dương Nữ
```

### 9.3. Test Cases
```python
# Test case 1: Năm 1994, Nam, Dương lịch
assert get_current_yun(1994) == 8
assert is_yang_year(1994) == True  # Giáp Tuất - Dương Mộc

# Test case 2: Năm 2024, Nữ, Dương lịch
assert get_current_yun(2024) == 9
assert is_yang_year(2024) == True  # Giáp Thìn - Dương Mộc

# Test case 3: Phi tinh sequence
center = 8
yang = True
result = fly_stars(center, yang)
# Expected: 8 ở trung tâm, các sao bay thuận
```

---

## 10. NOTES & CONSIDERATIONS

### 10.1. Phương pháp học phái

**✅ QUYẾT ĐỊNH: Implement cả 2 phái với switch toggle**

#### A. Đàm Dưỡng Ngô (沈氏) - Phương pháp phổ biến:
- Phi tinh dựa vào Âm Dương của năm sinh
- Nam Dương/Nữ Âm: Thuận phi (順飛)
- Nam Âm/Nữ Dương: Nghịch phi (逆飛)
- Xuất phát từ cung Trung tâm (5)

#### B. Thẩm Thị (沈氏玄空) - Phương pháp Hồng Kông:
- Phi tinh dựa vào hướng ngồi của nhà (坐向)
- Phức tạp hơn, cần La Bàn xác định
- Xuất phát từ cung Sơn Tinh/Hướng Tinh
- Kết hợp với Đại Vận (20 năm)

**Implementation:**
```python
class HuyenKhongSchool(Enum):
    DAM_DUONG_NGO = "dam_duong_ngo"  # Default
    THAM_THI = "tham_thi"

# User có thể switch giữa 2 phái trong UI
```

### 10.2. Separate View - Trang riêng

**✅ QUYẾT ĐỊNH: Tạo route mới `/huyen-khong` độc lập**

**Lý do:**
- Không làm rối UI trang chính
- Dễ focus vào Phi Tinh analysis
- Performance tốt hơn (lazy load)
- Có thể mở song song 2 tab để so sánh

**Route structure:**
```
http://localhost:5000/           → Tử Vi truyền thống (hiện tại)
http://localhost:5000/huyen-khong → Huyền Không Phi Tinh (mới)
```

**Navigation:**
```html
<!-- Thêm link vào navbar -->
<nav>
  <a href="/">Tử Vi Chính</a>
  <a href="/huyen-khong">Huyền Không Phi Tinh</a>
</nav>
```

### 10.3. Lưu Nhật & Lưu Thì - Bao gồm đầy đủ

**✅ QUYẾT ĐỊNH: Implement đầy đủ 5 tầng**

| Tầng | Tên | Chu kỳ | Độ phức tạp | Status |
|------|-----|--------|-------------|--------|
| 1 | Vận Tinh | 20 năm | ⭐ Easy | ✅ Phase 1 |
| 2 | Lưu Niên | 1 năm | ⭐⭐ Medium | ✅ Phase 1 |
| 3 | Lưu Nguyệt | 1 tháng | ⭐⭐⭐ Medium | ✅ Phase 2 |
| 4 | Lưu Nhật | 1 ngày | ⭐⭐⭐⭐ Hard | ✅ Phase 3 |
| 5 | Lưu Thì | 2 giờ | ⭐⭐⭐⭐⭐ Very Hard | ✅ Phase 3 |

**Warning system:**
```javascript
// UI sẽ hiển thị cảnh báo khi enable Lưu Nhật/Lưu Thì
if (enableLuuNhat || enableLuuThi) {
    showWarning(
        "⚠️ Lưu Nhật và Lưu Thì có độ phức tạp cao, " +
        "có thể có sai số. Chỉ dùng tham khảo."
    );
}
```

### 10.4. Integration với hệ thống hiện tại
- Không conflict với logic an sao hiện tại
- Có thể hiển thị song song: Sao truyền thống + Phi Tinh
- Cần toggle để chuyển đổi giữa các chế độ

### 10.4. Integration với hệ thống hiện tại
- Không conflict với logic an sao hiện tại
- Trang riêng `/huyen-khong` không ảnh hưởng trang chính
- Có thể mở 2 tab song song để so sánh

### 10.5. Performance
- Cache Vận calculation theo năm
- Pre-compute Lạc Thư mapping
- Lazy load Phi Tinh khi user click "Hiển thị Phi Tinh"

---

## 11. NEXT STEPS

1. **Nghiên cứu thêm:**
   - Tìm tài liệu chính xác về phái Lí Khí
   - Consult với chuyên gia (nếu có)
   - So sánh với các phần mềm Tử Vi khác

2. **Prototype:**
   - Build quick prototype để verify logic
   - Test với các trường hợp cụ thể
   - Get feedback từ users

3. **Development:**
   - Follow implementation plan
   - Regular testing & validation
   - Iterative improvement

---

## 12. RESOLVED DECISIONS

### ✅ 1. Phương pháp Phi Tinh:
**Quyết định:** Implement cả 2 phái với toggle switch
- Default: Đàm Dưỡng Ngô (phổ biến, dễ dùng)
- Option: Thẩm Thị (chuyên sâu hơn)
- User có thể chuyển đổi trong UI

### ✅ 2. Lưu Nhật và Lưu Thì:
**Quyết định:** CÓ - Implement đầy đủ 5 tầng
- Vận Tinh, Lưu Niên, Lưu Nguyệt: Bắt buộc
- Lưu Nhật, Lưu Thì: Optional với warning ⚠️
- Giúp người dùng tự quyết định độ chi tiết

### ✅ 3. Kết hợp với sao truyền thống:
**Quyết định:** KHÔNG trong giai đoạn 1
- Tách biệt hoàn toàn để tránh confusion
- Có thể làm feature tích hợp sau (Phase 7+)

### ✅ 4. UI hiển thị:
**Quyết định:** Separate view - Trang riêng `/huyen-khong`
- Không overlay trên trang chính
- Route độc lập: `localhost:5000/huyen-khong`
- Lý do: Clear hơn, performance tốt hơn

### ✅ 5. Export/Save:
**Quyết định:** CÓ - Giai đoạn sau (Phase 6)
- Export PNG (screenshot)
- Export PDF (formatted report)
- Save to database (user history)
- Share link (generate shareable URL)

## 13. FUTURE ENHANCEMENTS (Phase 7+)

1. **Tích hợp sao truyền thống + Phi Tinh**
   - Combined view showing both systems
   - Cross-reference analysis

2. **Lưu lịch sử tra cứu**
   - User account system
   - Save favorite charts
   - Compare multiple charts

3. **Mobile responsive design**
   - Touch-optimized UI
   - Swipe to switch layers

4. **Advanced interpretations**
   - AI-powered analysis
   - Personalized recommendations
   - Life event predictions

5. **Multi-language support**
   - English interface
   - Traditional Chinese option

---

**Document Version:** 2.0  
**Last Updated:** 2024-12-24  
**Author:** AI Assistant  
**Status:** Ready for Implementation
