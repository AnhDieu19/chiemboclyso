# THÁI ẤT & KÌ MÔN ĐỘN GIÁP
## Tài liệu nghiên cứu và phát triển tính năng

---

## 1. TỔNG QUAN

### 1.1. Giới thiệu

**Thái Ất Thần Số** (太乙神數) và **Kì Môn Độn Giáp** (奇門遁甲) là hai trong "Tam Thức" (三式) - Ba phương pháp dự đoán cao cấp nhất trong Dịch học Trung Hoa.

**Tam Thức bao gồm:**
1. **Thái Ất** (太乙) - Thiên thời, chiêm tinh, quốc vận
2. **Kì Môn** (奇門) - Không gian, phương vị, binh pháp
3. **Lục Nhâm** (六壬) - Nhân sự, quan hệ, dự đoán sự kiện

### 1.2. So sánh Thái Ất vs Kì Môn vs Huyền Không

| Đặc điểm | Thái Ất (太乙) | Kì Môn (奇門) | Huyền Không (玄空) |
|----------|---------------|--------------|------------------|
| Trọng tâm | Thiên văn, vận quốc | Binh pháp, phương vị | Thời gian, vận khí |
| Chu kỳ | 360 năm | 1800 giờ (75 ngày) | 180 năm |
| Công cụ | 16 Thần, 9 Cung | 8 Môn, 9 Tinh, 8 Thần | 9 Sao, Lạc Thư |
| Ứng dụng | Chính trị, chiến tranh | Quân sự, thương mại | Phong thủy, cá nhân |
| Độ khó | ⭐⭐⭐⭐⭐ Rất cao | ⭐⭐⭐⭐⭐ Rất cao | ⭐⭐⭐⭐ Cao |
| Phổ biến | ⭐⭐ Ít | ⭐⭐⭐ Trung bình | ⭐⭐⭐⭐ Cao |

### 1.3. Mục tiêu Implementation

**Mục tiêu:**
- Tạo 2 nhánh riêng biệt trên `localhost:5000`
- Tích hợp với hệ thống Tử Vi hiện có
- Cung cấp công cụ dự đoán cao cấp cho users

**Phạm vi:**
- **Phase 1**: Thái Ất Cơ Bản (16 Thần, 9 Cung)
- **Phase 2**: Kì Môn Độn Giáp (8 Môn, 9 Tinh, 8 Thần)
- **Phase 3**: Tích hợp & Phân tích đa chiều

---

## 2. THÁI ẤT THẦN SỐ (太乙神數)

### 2.1. Định nghĩa

**Thái Ất Thần Số** là phương pháp chiêm tinh cao cấp nhất, dùng để dự đoán:
- Vận nước (quốc vận)
- Thiên tai địa biến
- Chiến tranh hòa bình
- Vận mệnh cá nhân (hạn chế, phức tạp)

### 2.2. Cấu trúc hệ thống

#### A. Thập Lục Thần (16 Thần)
```
Chủ Tướng (主將):
1. Thái Ất (太乙) - Thần chủ
2. Văn Xương (文昌) - Văn chương
3. Chiêu Dao (招搖) - Chiêu vận
4. Hiên Dư (軒轅) - Đế vương

Đại Tướng (大將):
5. Thiên Phù (天符) - Thiên mệnh
6. Thanh Long (青龍) - Đông phương
7. Tiểu Cát (小吉) - Nhỏ cát
8. Tùng Khuê (從魁) - Tòng tùy

Tiểu Tướng (小將):
9. Thắng Quang (勝光) - Chiến thắng
10. Thái Xung (太冲) - Xung kích
11. Thiên Cương (天罡) - Cương cường
12. Thái Ất (太乙) - Phó
13. Thắng Tiên (勝先) - Tiên phong
14. Tiểu Cát (小吉) - Phó
15. Thái Ất (太乙) - Tam
16. Cửu Thiên (九天) - Cửu trùng
```

#### B. Cửu Cung (9 Cung) - Giống Lạc Thư
```
   4(SE)  9(S)   2(SW)
   3(E)   5      7(W)
   8(NE)  1(N)   6(NW)
```

#### C. Ngũ Nguyên (5 Nguyên) - Chu kỳ 72 năm
```
Giáp Tý Nguyên (甲子元):   1984-2055 (72 năm)
Giáp Tuất Nguyên (甲戌元): 2056-2127
Giáp Thân Nguyên (甲申元): 2128-2199
Giáp Ngọ Nguyên (甲午元):  2200-2271
Giáp Thìn Nguyên (甲辰元): 2272-2343

1 Nguyên = 72 năm
5 Nguyên = 360 năm (1 chu kỳ lớn)
```

### 2.3. Công thức tính toán

#### A. Xác định Nguyên hiện tại
```python
def get_thai_at_nguyen(year):
    """
    Xác định Nguyên (72 năm) dựa vào năm
    
    Chu kỳ 360 năm bắt đầu từ 1984:
    - Giáp Tý Nguyên: 1984-2055 (72 năm)
    - Giáp Thân Nguyên: 2056-2127
    - ...
    """
    base_year = 1984  # Năm bắt đầu chu kỳ mới
    cycle_length = 360  # 5 Nguyên
    nguyen_length = 72   # 1 Nguyên
    
    year_offset = (year - base_year) % cycle_length
    nguyen_index = year_offset // nguyen_length  # 0-4
    
    nguyen_names = [
        "Giáp Tý Nguyên",   # 0: 1984-2055
        "Giáp Tuất Nguyên", # 1: 2056-2127
        "Giáp Thân Nguyên", # 2: 2128-2199
        "Giáp Ngọ Nguyên",  # 3: 2200-2271
        "Giáp Thìn Nguyên"  # 4: 2272-2343
    ]
    
    return nguyen_index, nguyen_names[nguyen_index]
```

#### B. An Thập Lục Thần vào Cửu Cung (Logic Cũ - Tham khảo)
```python
def an_thai_at_than(year, month, day, hour):
    """
    An Thái Ất Thập Lục Thần vào Cửu Cung
    
    Công thức phức tạp, dựa vào:
    1. Nguyên (72 năm)
    2. Hội (6 năm)
    3. Kỷ (4 tháng)
    4. Nhập Kỷ (10 ngày trong 1 Kỷ)
    5. Can Chi của giờ
    """
    
    # 1. Xác định Nguyên
    nguyen_index, nguyen_name = get_thai_at_nguyen(year)
    
    # 2. Xác định Hội (6 năm)
    hui = ((year - 1984) % 72) // 6  # 0-11 (12 Hội trong 1 Nguyên)
    
    # 3. Xác định Kỷ (4 tháng)
    ky = month // 4  # 0-2 (3 Kỷ trong 1 năm)
    
    # 4. Xác định Nhập Kỷ (10 ngày)
    nhap_ky = (day - 1) // 10  # 0-2 (3 Nhập trong 1 Kỷ)
    
    # 5. An Thần vào Cung dựa vào công thức phức tạp
    # (Cần tra bảng hoặc dùng thuật toán chuyên biệt)
    
    return {
        'nguyen': nguyen_name,
        'hoi': hui,
        'ky': ky,
        'nhap_ky': nhap_ky,
        'than_positions': calculate_than_positions(nguyen_index, hoi, ky, nhap_ky, hour)
    }
```

### 4.2. Algorithmic Details (Chi tiết Thuật toán - Cập nhật Mới)

#### 4.2.1. Các Công thức An Sao Thái Ất (Theo Sách Thái Ất & Diễn dịch Hình ảnh)

**1. Thái Ất (Tuế Kể)**
*   **Công thức**: `(Kỷ Dư - 24) / 3`. Rút 3.
*   **Quy luật**:
    *   **Dương Cục**: Khởi Cung 1 (Khảm), đi thuận 8 cung theo Hậu Thiên Bát Quái (1→8→3→4→9→2→7→6→1). Bỏ trung cung 5. **3 năm dời 1 cung**.
    *   **Âm Cục**: Khởi Cung 9 (Ly), đi nghịch.

**2. Thiên Mục (Văn Xương - Chủ Mục)**
*   **Công thức**: `(Kỷ Dư - 18)`.
*   **Khởi điểm**:
    *   Dương Cục: Khởi **Thân** (Cung 2 - Khôn), đi thuận 16 thần.
    *   Âm Cục: Khởi **Dần** (Cung 8 - Cấn), đi xuôi/ngược (tùy sách).
*   **Luật đặc biệt**: "Gặp Kiền Khôn lưu 2 toán" (Ở cung Càn và Khôn thì ở lại 2 nhịp/2 năm).

**3. Địa Mục (Thủy Kích - Khách Mục)**
*   **Quy luật**: Phụ thuộc vào vị trí Kể Thần và Văn Xương. (Logic: Văn Xương tới cung nào thì Thủy Kích giạt phương nào đó... Cần xác định rõ rule).
*   *Tạm thời*: Dùng logic đối xứng hoặc 16 Thần nghịch.

**4. Tam Cơ (3 Nền)**
*   **Quân Cơ (Nền Vua)**:
    *   Công thức: `((Tích Tuế - Offset) % 360) / 30`.
    *   Quy luật: Khởi **Ngọ** (Cung 9), đi thuận 12 cung. **30 năm** dời 1 cung.
*   **Thần Cơ (Nền Quan)**:
    *   Công thức: `((Tích Tuế - Offset) % 360) / 3`.
    *   Quy luật: Khởi **Ngọ**, thuận 12 cung. **3 năm** dời 1 cung.
*   **Dân Cơ (Nền Dân)**:
    *   Công thức: `(Tích Tuế % 12)`.
    *   Quy luật: Khởi **Tuất**, thuận 12 cung. **1 năm** dời 1 cung.

**5. Ngũ Phúc**
*   **Công thức**: `((Tích Tuế + 115) % 225) / 45`.
*   **Quy luật**: Khởi **Cung 1** (Kiền), đi theo chu trình: **1 → 8 → 4 → 2 → 5**. (45 năm dời 1 cung).

**6. Đại Du**
*   **Công thức**: `((Tích Tuế + 34) % 288) / 36`.
*   **Quy luật**: Khởi **Cung 7** (Đoài) hoặc **2** (Khôn) (User ghi "Khôn 7"). Đi thuận 8 cung. **36 năm** dời 1 cung.

**7. Tứ Thần**
*   **Tứ Thần**: Khởi **Cung 1**, đi thuận 12 cung (3 năm/cung).
*   **Thiên Ất (Thần)**: Khởi **Cung 6**.
*   **Địa Ất**: Khởi **Cung 9**.
*   **Trực Phù**: Khởi **Cung 5**.

#### 4.2.2. Logic Tương Tác và Lưới Thái Ất (Theo Hình Ảnh)

**1. Quan hệ Can Chi & Ngũ Hành (Ảnh 0 & 1)**
*   **Tam Hợp (Trine - A U B)**:
    *   Thủy: Thân - Tý - Thìn (Màu Xanh Dương/Lục)
    *   Hỏa: Dần - Ngọ - Tuất (Màu Đỏ)
    *   Mộc: Hợi - Mão - Mùi (Màu Xanh Lá)
    *   Kim: Tỵ - Dậu - Sửu (Màu Vàng/Cam) (Note: Ảnh 2 show Ty-Dau-Suu as Metal/Yellow) => *Điều chỉnh: Tỵ-Dậu-Sửu là Kim cục.*
*   **Nhị Hợp (Lục Hợp)**: Ngọ-Mùi (Nhật-Nguyệt), Tỵ-Thân, Thìn-Dậu, Mão-Tuất, Dần-Hợi, Tý-Sửu.
*   **Lục Hại (A - B)**: Tý-Mùi, Sửu-Ngọ, Dần-Tỵ, Mão-Thìn, Thân-Hợi, Dậu-Tuất.

**2. Lưới Thái Ất Mẫu (Ảnh 4 & 5)**
*   Hệ thống cung dựa trên Lạc Thư (Luo Shu Variations):
    *   **Thìn (9)**: Thái Dương, Dương Tuyệt. (Vị trí 4/9/2 Row 1 Grid)
    *   **Ngọ (2)**: Đại Uy, Khí Rời.
    *   **Mùi (7)**: Thiên Đạo.
    *   **Mão (4)**: Cao Tùng, Khí Tuyệt.
    *   **Trung (5)**.
    *   **Dậu (6)**: Huynh Thái Tộc.
    *   **Dần (3)**: Lã Thân.
    *   **Tý (8)**: Tài Thổ Chủ.
    *   **Hợi (1)**: Tự Đại Nghĩa.
*   *Ghi chú*: Đây là bảng **Thập Lục Thần** (hoặc biến thể) an theo **12 Chi** vào 9 Cung. Cần tra cứu bảng `thai_at_tables.py` để map tên (Vũ Đức, Đại Vũ, Thái Tộc...) vào ID tương ứng.

```python
# Helper Logic Tương Tác Mới
def analyze_inteactions(stars_list):
    interactions = []
    # Check Tam Hợp
    # Check Nhị Hợp
    # Check Xung/Hại
    return interactions
```

#### C. Giải mã ý nghĩa
```python
THAI_AT_MEANINGS = {
    'Thái Ất': {
        'nature': 'cat',
        'meaning': 'Đế tinh, chủ quyền, vận quốc thịnh',
        'fields': ['chính trị', 'lãnh đạo', 'quyền lực']
    },
    'Văn Xương': {
        'nature': 'cat',
        'meaning': 'Văn chương, học vấn, khoa cử',
        'fields': ['giáo dục', 'văn học', 'nghiên cứu']
    },
    'Thanh Long': {
        'nature': 'cat',
        'meaning': 'Quý nhân, thăng quan, may mắn',
        'fields': ['sự nghiệp', 'thăng tiến', 'tài vận']
    },
    # ... 13 Thần còn lại
}
```

### 2.4. Độ phức tạp

**⚠️ Cảnh báo:**
- Thái Ất là hệ thống **CỰC KỲ PHỨC TẠP**, khó hơn cả Kì Môn
- Cần tra bảng Thái Ất chuyên biệt (ít tài liệu công khai)
- Phù hợp cho dự đoán quốc vận, ít dùng cho cá nhân
- **Khuyến nghị**: Implement ở mức cơ bản, không đi sâu vào chi tiết

---

## 3. KÌ MÔN ĐỘN GIÁP (奇門遁甲)

### 3.1. Định nghĩa

**Kì Môn Độn Giáp** là "Vua của các phương pháp dự đoán", được Gia Cát Lượng, Lưu Bá Ôn sử dụng để:
- Dự đoán thắng bại trong chiến tranh
- Chọn phương hướng cát hung
- Xác định thời điểm tốt nhất cho hành động
- Phân tích cục diện hiện tại

### 3.2. Cấu trúc hệ thống

#### A. Tam Kỳ (3 Kỳ)
```
1. Ất (乙) - Nhật Kỳ (日奇) - Mặt trời
2. Bính (丙) - Nguyệt Kỳ (月奇) - Mặt trăng
3. Đinh (丁) - Tinh Kỳ (星奇) - Sao
```

#### B. Bát Môn (8 Cửa)
```
1. Khai Môn (開門) - Mở - Cát
2. Hưu Môn (休門) - Nghỉ - Cát
3. Sinh Môn (生門) - Sinh - Cát
4. Thương Môn (傷門) - Thương - Hung
5. Đỗ Môn (杜門) - Đóng - Trung bình
6. Cảnh Môn (景門) - Cảnh - Cát/Hung
7. Tử Môn (死門) - Chết - Hung
8. Kinh Môn (驚門) - Kinh - Hung
```

#### C. Cửu Tinh (9 Sao) - Khác Huyền Không
```
1. Thiên Bồng (天蓬) - Thủy - Hung
2. Thiên Nhuế (天芮) - Thổ - Hung       ← Bệnh phù tinh
3. Thiên Xung (天衝) - Mộc - Hung/Cát
4. Thiên Phụ (天輔) - Mộc - Cát
5. Thiên Cấm (天禽) - Thổ - Trung bình
6. Thiên Tâm (天心) - Kim - Cát
7. Thiên Trụ (天柱) - Kim - Hung/Cát
8. Thiên Nhậm (天任) - Thổ - Cát       ← Trung hậu tinh
9. Thiên Anh (天英) - Hỏa - Hung/Cát
```

#### D. Bát Thần (8 Thần)
```
1. Trực Phù (值符) - Thần chủ
2. Đằng Xà (螣蛇) - Rắn lượn
3. Thái Âm (太陰) - Thái âm
4. Lục Hợp (六合) - Hòa hợp
5. Câu Trần (勾陈) - Câu trần
6. Chu Tước (朱雀) - Chu tước
7. Cửu Địa (九地) - Cửu địa
8. Cửu Thiên (九天) - Cửu thiên
```

### 3.3. Công thức tính toán

#### A. Xác định Cục (局) - Quan trọng nhất
```python
def get_ki_mon_cuc(year, month, day, hour, tiet_khi):
    """
    Xác định Cục Kì Môn (1-9)
    
    Dựa vào:
    1. Tiết Khí (24 tiết khí)
    2. Ngày Can Chi
    3. Giờ Can Chi
    4. Âm Dương (Âm Độn/Dương Độn)
    """
    
    # 1. Xác định Âm Độn hay Dương Độn
    # Đông Chí → Hạ Chí: Dương Độn
    # Hạ Chí → Đông Chí: Âm Độn
    la_duong_don = is_between_dong_chi_and_ha_chi(tiet_khi)
    
    # 2. Xác định số Cục dựa vào Tiết Khí + Can Chi ngày
    # Công thức phức tạp, cần tra bảng
    cuc = calculate_cuc_from_tiet_khi_and_day_can(tiet_khi, day_can, la_duong_don)
    
    # 3. Xác định giờ Kì Môn (1-18 giờ trong 1 cục)
    gio_ki_mon = calculate_ki_mon_hour(hour, cuc)
    
    return {
        'cuc': cuc,  # 1-9
        'la_duong_don': la_duong_don,
        'gio_ki_mon': gio_ki_mon,
        'tiet_khi': tiet_khi
    }
```

#### B. An Bát Môn vào Cửu Cung
```python
def an_bat_mon(cuc, gio_ki_mon, la_duong_don):
    """
    An 8 Môn vào 9 Cung theo Cục và Giờ
    
    Quy tắc:
    - Dương Độn: Thuận phi (1→2→3...)
    - Âm Độn: Nghịch phi (9→8→7...)
    """
    
    # Cung bắt đầu phụ thuộc vào Cục
    start_positions = {
        1: 1,  # Cục 1 bắt đầu từ cung Khảm (1)
        2: 8,  # Cục 2 bắt đầu từ cung Cấn (8)
        3: 3,  # Cục 3 bắt đầu từ cung Chấn (3)
        # ... 9 cục
    }
    
    start_pos = start_positions[cuc]
    
    # An 8 Môn theo thứ tự
    mon_order = ['Hưu', 'Sinh', 'Thương', 'Đỗ', 'Cảnh', 'Tử', 'Kinh', 'Khai']
    
    mon_positions = {}
    current_pos = start_pos
    
    for i, mon in enumerate(mon_order):
        if la_duong_don:
            pos = (start_pos + i) % 9
        else:
            pos = (start_pos - i) % 9
        
        mon_positions[mon] = pos
    
    return mon_positions
```

#### C. An Cửu Tinh và Bát Thần
```python
def an_cuu_tinh_bat_than(cuc, gio_ki_mon, la_duong_don):
    """
    An Cửu Tinh và Bát Thần vào Cửu Cung
    
    Phức tạp hơn Bát Môn, cần tra bảng chuyên biệt
    """
    
    # 1. An Trực Phù (Thần chủ) - phụ thuộc vào giờ
    zhi_fu_pos = calculate_zhi_fu_position(gio_ki_mon)
    
    # 2. An 8 Thần còn lại theo thứ tự
    # ...
    
    # 3. An Cửu Tinh
    # ...
    
    return {
        'sao_positions': {...},
        'than_positions': {...}
    }
```

### 3.4. Giải mã ý nghĩa

#### A. Phân tích Cung
```python
def analyze_ki_mon_palace(palace_index, mon, sao, than, tam_ky):
    """
    Phân tích 1 cung trong Kì Môn
    
    Kết hợp:
    - Môn (Cửa)
    - Sao (Tinh)
    - Thần (Thần)
    - Tam Kỳ (nếu có)
    """
    
    # Tính điểm cát hung
    cat_hung_score = 0
    
    # Môn
    if mon in ['Khai', 'Hưu', 'Sinh']:
        cat_hung_score += 2  # Cát
    elif mon in ['Tử', 'Kinh', 'Thương']:
        cat_hung_score -= 2  # Hung
    
    # Sao
    if sao in ['Thiên Nhiệm', 'Thiên Tâm', 'Thiên Phụ']:
        cat_hung_score += 1
    elif sao in ['Thiên Bồng', 'Thiên Anh']:
        cat_hung_score -= 1
    
    # Tam Kỳ
    if tam_ky in ['Ất', 'Bính', 'Đinh']:
        cat_hung_score += 3  # Rất cát
    
    return {
        'score': cat_hung_score,
        'nature': 'cat' if cat_hung_score > 0 else 'hung',
        'meaning': generate_meaning(mon, sao, than, tam_ky)
    }
```

#### B. Ứng dụng thực tế
```python
KI_MON_APPLICATIONS = {
    'Dự đoán thắng bại': {
        'check': ['Thiên Tâm', 'Sinh Môn', 'Trực Phù'],
        'cat': 'Chiến thắng',
        'hung': 'Thất bại'
    },
    'Chọn phương hướng': {
        'cat_directions': ['Cung có Tam Kỳ', 'Sinh Môn', 'Khai Môn'],
        'hung_directions': ['Tử Môn', 'Kinh Môn', 'Thương Môn']
    },
    'Xem thời vận': {
        'good_time': 'Trực Phù + Tam Kỳ + Sinh Môn',
        'bad_time': 'Tử Môn + Hung Tinh'
    }
}
```

### 3.5. Độ phức tạp

**⚠️ Cảnh báo:**
- Kì Môn là hệ thống **CỰC KỲ PHỨC TẠP**
- Cần tra bảng Kì Môn chuyên biệt (có sẵn nhiều nguồn)
- Tính toán Tiết Khí chính xác là quan trọng nhất
- **Khuyến nghị**: Implement đầy đủ vì có giá trị thực tế cao

---

## 4. TÍCH HỢP VỚI HỆ THỐNG HIỆN TẠI

### 4.1. Chi tiết tái sử dụng code - Phân tích từng module

#### A. Core Calendar System (✅ Tái sử dụng 100%)

**Module: `python/core/lunar_converter.py`**

| Hàm hiện có | Chữ ký | Dùng cho | Mức độ tái sử dụng |
|-------------|--------|----------|-------------------|
| `solar_to_lunar()` | `(dd: int, mm: int, yy: int) -> dict` | Chuyển Dương→Âm cho cả 3 hệ | ✅ 100% Direct |
| `jd_from_date()` | `(dd: int, mm: int, yy: int) -> int` | Tính Julius Day (dùng cho Tiết Khí) | ✅ 100% Direct |
| `new_moon()` | `(k: int) -> float` | Tính Sóc (Huyền Không cần) | ✅ 100% Direct |
| `sun_longitude()` | `(jd: float) -> float` | **Quan trọng!** Base cho Tiết Khí | ✅ 80% Cần wrapper |

**Ví dụ sử dụng:**
```python
from core.lunar_converter import solar_to_lunar, sun_longitude, jd_from_date

# 1. Chuyển đổi Âm-Dương (dùng cho cả 3 hệ)
lunar = solar_to_lunar(15, 1, 2024)
# → {'day': 5, 'month': 12, 'year': 2023, 'leap': False}

# 2. Tính Julius Day (cơ sở cho Tiết Khí)
jd = jd_from_date(15, 1, 2024)
# → 2460328

# 3. Tính kinh độ mặt trời (base cho Tiết Khí)
longitude = sun_longitude(jd)
# → 295.234 độ (cần chia cho 15° để ra Tiết Khí index)
```

**⚠️ Cần mở rộng:**
```python
# python/core/jie_qi_calculator.py (MỚI - 150 LOC)
def calculate_jie_qi(year: int, month: int, day: int) -> dict:
    """
    Tính Tiết Khí (24 tiết khí) từ kinh độ mặt trời
    
    CÔNG THỨC:
    - 1 Tiết Khí = 15° kinh độ mặt trời
    - Lập Xuân (315°), Vũ Thủy (330°), Kinh Trập (345°)...
    - Index Tiết Khí = (longitude // 15) % 24
    
    Tái sử dụng: sun_longitude() từ lunar_converter.py
    """
    jd = jd_from_date(day, month, year)
    longitude = sun_longitude(jd)
    tiet_khi_index = int(longitude // 15) % 24
    return {
        'index': tiet_khi_index,
        'name': TIET_KHI_NAMES[tiet_khi_index],
        'longitude': longitude
    }

TIET_KHI_NAMES = [
    '小寒', '大寒', '立春', '雨水', '惊蛰', '春分',
    '清明', '谷雨', '立夏', '小满', '芒种', '夏至',
    '小暑', '大暑', '立秋', '处暑', '白露', '秋分',
    '寒露', '霜降', '立冬', '小雪', '大雪', '冬至'
]
```

---

#### B. Can Chi System (✅ Tái sử dụng 100%)

**Module: `python/core/can_chi_calc.py`**

| Hàm hiện có | Chữ ký | Dùng cho | Mức độ tái sử dụng |
|-------------|--------|----------|-------------------|
| `get_year_can_chi()` | `(lunar_year: int) -> dict` | Thái Ất (Nguyên), Kì Môn (Dương/Âm Độn) | ✅ 100% Direct |
| `get_month_can_chi()` | `(month: int, year: int) -> dict` | Kì Môn (Dương Độn phân biệt mùa) | ✅ 100% Direct |
| `get_day_can_chi()` | `(dd: int, mm: int, yy: int) -> dict` | Kì Môn (Cục calculation) | ✅ 100% Direct |
| `get_hour_can_chi()` | `(hour_idx: int, dd: int, mm: int, yy: int) -> dict` | Kì Môn (1-18 giờ Kì Môn) | ✅ 100% Direct |

**Ví dụ sử dụng:**
```python
from core.can_chi_calc import get_year_can_chi, get_month_can_chi

# Thái Ất: Xác định Nguyên (Giáp Tý Nguyên, Giáp Tuất Nguyên...)
year_cc = get_year_can_chi(2024)
# → {'can_index': 0, 'chi_index': 4, 'can': 'Giáp', 'chi': 'Thìn', 'full': 'Giáp Thìn'}

# Kì Môn: Phân biệt Dương Độn (Đông Chí → Hạ Chí) vs Âm Độn
month_cc = get_month_can_chi(1, 2024)
jie_qi_index = calculate_jie_qi(15, 1, 2024)['index']
la_duong_don = 23 >= jie_qi_index >= 0 or jie_qi_index <= 11
# → True (Đông Chí tới Hạ Chí)
```

**Data constants (✅ Tái sử dụng 100%):**
```python
from data.can_chi import THIEN_CAN, DIA_CHI, NGU_HANH, CHI_NGU_HANH

# THIEN_CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
# DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
# CHI_NGU_HANH = {0: 'Thủy', 1: 'Thổ', 2: 'Mộc', 3: 'Mộc', ...}
```

---

#### C. Ngũ Hành Relationships (✅ Tái sử dụng 100%)

**Module: `python/analytics/tuvi_knowledge_graph.py` (extract thành engine)**

| Data hiện có | Dùng cho | Mức độ tái sử dụng |
|-------------|----------|-------------------|
| `NGU_HANH_SINH` | Thái Ất (Thần hợp/xung), Kì Môn (Tinh tương sinh) | ✅ 100% Direct |
| `NGU_HANH_KHAC` | Thái Ất (Thần khắc), Kì Môn (Tinh tương khắc) | ✅ 100% Direct |
| `SAO_NGU_HANH` | Kì Môn (9 Tinh thuộc Ngũ Hành) | 🔄 70% (cần map Cửu Tinh Kì Môn) |
| `CHI_NGU_HANH` | Cả 3 hệ (12 Cung → Ngũ Hành) | ✅ 100% Direct |

**✅ Tạo engine mới (refactor từ tuvi_knowledge_graph.py):**
```python
# python/core/ngu_hanh_engine.py (MỚI - 80 LOC)
class NguHanhEngine:
    """
    Ngũ Hành Tương Sinh Tương Khắc Engine
    Tái sử dụng cho: Tử Vi, Huyền Không, Thái Ất, Kì Môn
    """
    
    NGU_HANH_SINH = {
        'Kim': 'Thủy', 'Thủy': 'Mộc', 'Mộc': 'Hỏa', 'Hỏa': 'Thổ', 'Thổ': 'Kim'
    }
    
    NGU_HANH_KHAC = {
        'Kim': 'Mộc', 'Mộc': 'Thổ', 'Thổ': 'Thủy', 'Thủy': 'Hỏa', 'Hỏa': 'Kim'
    }
    
    @staticmethod
    def get_relation(hanh1: str, hanh2: str) -> str:
        """
        Xác định mối quan hệ giữa 2 Ngũ Hành
        Returns: 'sinh' | 'khac' | 'bi_khac' | 'dong' | 'neutral'
        """
        if hanh1 == hanh2:
            return 'dong'  # Đồng hành
        if NguHanhEngine.NGU_HANH_SINH.get(hanh1) == hanh2:
            return 'sinh'  # hanh1 sinh hanh2
        if NguHanhEngine.NGU_HANH_KHAC.get(hanh1) == hanh2:
            return 'khac'  # hanh1 khắc hanh2
        if NguHanhEngine.NGU_HANH_KHAC.get(hanh2) == hanh1:
            return 'bi_khac'  # hanh1 bị hanh2 khắc
        return 'neutral'
    
    @staticmethod
    def get_chi_ngu_hanh(chi_index: int) -> str:
        """Lấy Ngũ Hành của Địa Chi (12 Cung)"""
        from data.can_chi import CHI_NGU_HANH
        return CHI_NGU_HANH[chi_index]
```

---

#### D. Palace System (🔄 Cần mapping 12 Cung → 9 Cung)

**Module: `python/core/cung_menh.py`**

| Hàm hiện có | Chữ ký | Dùng cho | Mức độ tái sử dụng |
|-------------|--------|----------|-------------------|
| `calculate_cung_menh()` | `(month: int, hour: int) -> int` | Tử Vi (12 Cung) | 🔄 50% Cần wrapper |
| `calculate_cung_than()` | `(month: int, hour: int) -> int` | Tử Vi (12 Cung) | 🔄 50% Cần wrapper |
| `get_cung_info()` | `(position: int) -> dict` | Lấy tên + Ngũ Hành | 🔄 50% Cần wrapper |

**⚠️ Vấn đề mapping:**
- **Tử Vi**: 12 Cung (Địa Chi: Tý, Sửu, Dần...)
- **Huyền Không/Thái Ất/Kì Môn**: 9 Cung (Lạc Thư: 1-9)

**✅ Giải pháp: Tạo converter mới**
```python
# python/core/palace_converter.py (MỚI - 120 LOC)

# Ánh xạ 12 Cung (Địa Chi) → 9 Cung (Lạc Thư)
# Quy tắc: 3 Địa Chi gộp thành 1 Lạc Thư cung
PALACE_12_TO_9 = {
    # Lạc Thư 1 (Khảm - Bắc - Thủy)
    0: 1,   # Tý → Cung 1
    11: 1,  # Hợi → Cung 1
    
    # Lạc Thư 2 (Khôn - Tây Nam - Thổ)
    1: 2,   # Sửu → Cung 2
    7: 2,   # Mùi → Cung 2
    
    # Lạc Thư 3 (Chấn - Đông - Mộc)
    2: 3,   # Dần → Cung 3
    3: 3,   # Mão → Cung 3
    
    # Lạc Thư 4 (Tốn - Đông Nam - Mộc)
    4: 4,   # Thìn → Cung 4
    
    # Lạc Thư 5 (Trung Cung - Thổ) - không tồn tại trong Địa Chi
    # → Dùng Thìn hoặc Tuất làm proxy
    
    # Lạc Thư 6 (Càn - Tây Bắc - Kim)
    8: 6,   # Thân → Cung 6
    9: 6,   # Dậu → Cung 6
    10: 6,  # Tuất → Cung 6
    
    # Lạc Thư 7 (Đoài - Tây - Kim)
    # → Không ánh xạ trực tiếp, dùng Thân/Dậu
    
    # Lạc Thư 8 (Cấn - Đông Bắc - Thổ)
    # → Không ánh xạ trực tiếp
    
    # Lạc Thư 9 (Ly - Nam - Hỏa)
    5: 9,   # Tỵ → Cung 9
    6: 9,   # Ngọ → Cung 9
}

def convert_12_to_9_palace(chi_index: int) -> int:
    """
    Chuyển đổi từ 12 Cung (Địa Chi) sang 9 Cung (Lạc Thư)
    
    Args:
        chi_index: 0-11 (Tý→Hợi)
        
    Returns:
        1-9 (Lạc Thư cung)
    """
    return PALACE_12_TO_9.get(chi_index, 5)  # Default: Trung Cung

def get_9_palace_ngu_hanh(palace_idx: int) -> str:
    """Lấy Ngũ Hành của 9 Cung Lạc Thư"""
    LAC_THU_NGU_HANH = {
        1: 'Thủy',  # Khảm
        2: 'Thổ',   # Khôn
        3: 'Mộc',   # Chấn
        4: 'Mộc',   # Tốn
        5: 'Thổ',   # Trung Cung
        6: 'Kim',   # Càn
        7: 'Kim',   # Đoài
        8: 'Thổ',   # Cấn
        9: 'Hỏa'    # Ly
    }
    return LAC_THU_NGU_HANH[palace_idx]
```

---

#### E. Frontend Visualization (🔄 50% cần adapt)

**Module: `python/graph/static/js/cung_grid.js`**

| Component hiện có | Dùng cho | Mức độ tái sử dụng |
|-------------------|----------|-------------------|
| `renderCungGrid()` | Render 12 ô cung | 🔄 60% (cần thay đổi layout 3x3) |
| `anSaoVaoCung()` | Đặt sao vào cung | ✅ 80% (logic giữ nguyên) |
| CSS classes `.cung-cell` | Styling cung | ✅ 90% (thêm class `.palace-9`) |
| Ngũ Hành colors | Kim/Mộc/Thủy/Hỏa/Thổ | ✅ 100% Direct |

**⚠️ Cần tạo component mới:**
```javascript
// python/graph/static/js/palace_9_grid.js (MỚI - 300 LOC)

/**
 * Render 9 Cung Lạc Thư (3x3 grid)
 * Layout:
 *   4 (Tốn) | 9 (Ly)  | 2 (Khôn)
 *   --------|---------|----------
 *   3 (Chấn)| 5 (Trung)| 7 (Đoài)
 *   --------|---------|----------
 *   8 (Cấn) | 1 (Khảm)| 6 (Càn)
 */
function renderPalace9Grid(chartData) {
    const PALACE_LAYOUT = [
        [4, 9, 2],  // Top row
        [3, 5, 7],  // Middle row
        [8, 1, 6]   // Bottom row
    ];
    
    // Tái sử dụng: Ngũ Hành colors từ graph.css
    // Tái sử dụng: anSaoVaoCung() logic
    // Thay đổi: 3x3 grid thay vì 12 boxes
}
```

---

#### F. API Blueprint Pattern (✅ 90% tái sử dụng)

**Module: `python/app.py` (Flask routes)**

| Pattern hiện có | Dùng cho | Mức độ tái sử dụng |
|-----------------|----------|-------------------|
| `@app.route('/api/tuvi/calculate')` | Tử Vi calculation | ✅ 90% (copy pattern) |
| Request validation | Input validation | ✅ 100% (reuse schema) |
| Error handling | Try-except wrapper | ✅ 100% Direct |
| JSON response format | Standardized response | ✅ 100% Direct |

**✅ Tạo blueprint mới (theo pattern hiện có):**
```python
# python/services/thai_at_service.py (MỚI - 200 LOC)
# python/services/qi_men_service.py (MỚI - 300 LOC)

from flask import Blueprint, request, jsonify
from core.can_chi_calc import get_year_can_chi
from core.jie_qi_calculator import calculate_jie_qi  # MỚI
from core.ngu_hanh_engine import NguHanhEngine       # MỚI (refactor)

thai_at_bp = Blueprint('thai_at', __name__)

@thai_at_bp.route('/api/thai-at/calculate', methods=['POST'])
def calculate_thai_at():
    """
    Tái sử dụng:
    - Request validation pattern
    - solar_to_lunar()
    - get_year_can_chi()
    - JSON response format
    
    Mới:
    - get_thai_at_nguyen()
    - calculate_hui_ji()
    - an_thai_at_than()
    """
    data = request.get_json()
    # ... validation (reuse existing pattern)
    lunar = solar_to_lunar(data['day'], data['month'], data['year'])
    year_cc = get_year_can_chi(lunar['year'])
    
    # MỚI: Thái Ất calculation
    nguyen = get_thai_at_nguyen(year_cc['can_index'], year_cc['chi_index'])
    hoi = calculate_hoi(lunar['month'])
    ky = calculate_ky(lunar['day'])
    
    return jsonify({
        'success': True,
        'data': {
            'nguyen': nguyen,
            'hoi': hoi,
            'ky': ky,
            # ...
        }
    })
```

---

### 4.2. Tổng hợp phần trăm tái sử dụng

| Layer | Module | LOC hiện có | LOC mới | % Reuse | Ghi chú |
|-------|--------|-------------|---------|---------|---------|
| **Core** | lunar_converter.py | 386 | 0 | 100% | Direct reuse |
| | can_chi_calc.py | 345 | 0 | 100% | Direct reuse |
| | jie_qi_calculator.py | 0 | 150 | 0% | **MỚI - Critical!** |
| | ngu_hanh_engine.py | 0 | 80 | 0% | Refactor từ analytics |
| | palace_converter.py | 0 | 120 | 0% | **MỚI - 12→9 Cung** |
| | cung_menh.py | 144 | 0 | 50% | Cần wrapper |
| **Logic** | thai_at_engine.py | 0 | 400 | 0% | **MỚI - Thái Ất** |
| | qi_men_engine.py | 0 | 600 | 0% | **MỚI - Kì Môn** |
| **Services** | thai_at_service.py | 0 | 200 | 90% | Blueprint pattern |
| | qi_men_service.py | 0 | 300 | 90% | Blueprint pattern |
| **Frontend** | palace_9_grid.js | 0 | 300 | 60% | Adapt từ cung_grid.js |
| | thai_at_view.js | 0 | 200 | 70% | Adapt từ graph_main.js |
| | qi_men_view.js | 0 | 250 | 70% | Adapt từ graph_main.js |
| **Data** | thai_at_tables.py | 0 | 500 | 0% | **MỚI - Lookup tables** |
| | qi_men_tables.py | 0 | 800 | 0% | **MỚI - Lookup tables** |
| | **TỔNG** | **875** | **3900** | **18%** | Core: 875 LOC reused |

**📊 Phân tích chi tiết:**

- **Backend Core (875 LOC tái sử dụng):**
  - ✅ Calendar system: 100% reuse (731 LOC)
  - ✅ Can Chi system: 100% reuse (345 LOC)
  - ✅ Data constants: 100% reuse (CHI_NGU_HANH, THIEN_CAN...)
  - 🔄 Cung system: 50% reuse (cần wrapper 12→9)

- **Backend Logic (2000 LOC mới):**
  - ❌ Tiết Khí calculator: 150 LOC (**critical path**)
  - ❌ Ngũ Hành engine: 80 LOC (refactor từ analytics)
  - ❌ Palace converter: 120 LOC (12→9 mapping)
  - ❌ Thái Ất engine: 400 LOC
  - ❌ Kì Môn engine: 600 LOC
  - ❌ Lookup tables: 1300 LOC (digitize từ sách)

- **Frontend (750 LOC - 65% pattern reuse):**
  - 🔄 9 Cung grid: 300 LOC (adapt từ cung_grid.js)
  - 🔄 View components: 450 LOC (adapt từ graph_main.js)
  - ✅ CSS colors: 100% reuse (Ngũ Hành colors)

- **Services (500 LOC - 90% pattern reuse):**
  - 🔄 Blueprint structure: Copy từ app.py
  - 🔄 Request validation: Reuse schema
  - 🔄 Error handling: Reuse wrapper

**⚠️ Lưu ý quan trọng:**
1. **Tiết Khí calculator** (150 LOC) là **critical path** cho Kì Môn
2. **Palace converter** (120 LOC) ảnh hưởng cả 3 hệ thống
3. **Lookup tables** (1300 LOC) tốn effort digitize từ sách
4. Frontend cần redesign layout 3x3 thay vì 4x3

**🎯 Revised Effort Estimate:**

| Phase | Original | Revised | Lý do |
|-------|----------|---------|-------|
| Thái Ất | 4-5 tuần | 5-6 tuần | +1w cho Palace converter + Tables |
| Kì Môn | 6-8 tuần | 8-10 tuần | +2w cho Tiết Khí + Complex tables |
| Tích hợp | 2-3 tuần | 2-3 tuần | Pattern reuse giúp giữ đúng estimate |
| **Tổng** | **12-16 tuần** | **15-19 tuần** | +3-4 tuần (realistic)

### 4.3. Dependencies Graph

```
[Core Layer - 100% Reusable]
    lunar_converter.py (386 LOC)
    can_chi_calc.py (345 LOC)
    data/can_chi.py (THIEN_CAN, DIA_CHI, CHI_NGU_HANH)
            ↓
    ┌───────┴────────┐
    ↓                ↓
[New Core - Phase 0]   [Refactor - Phase 0.5]
jie_qi_calculator.py   ngu_hanh_engine.py (80 LOC)
(150 LOC - CRITICAL)   palace_converter.py (120 LOC)
    ↓                        ↓
    └────────┬───────────────┘
             ↓
    ┌────────┴─────────┐
    ↓                  ↓
[Thái Ất - Phase 1]   [Kì Môn - Phase 2]
thai_at_engine.py     qi_men_engine.py
(400 LOC)             (600 LOC)
thai_at_tables.py     qi_men_tables.py
(500 LOC)             (800 LOC)
thai_at_service.py    qi_men_service.py
(200 LOC)             (300 LOC)
    ↓                  ↓
    └────────┬─────────┘
             ↓
    [Integration - Phase 3]
    /tri-thuc route
    Combined view
```

**Critical Path:** `tiet_khi_calculator.py` → `ki_mon_engine.py` (Kì Môn không thể bắt đầu trước khi Tiết Khí xong)

---

### 4.4. Revised Effort Estimate (Based on Detailed Analysis)

**Phase 0: Foundation (2 tuần - NEW)**
- Week 1: `jie_qi_calculator.py` (150 LOC) + Unit tests
  - Implement `sun_longitude()` wrapper
  - 24 Tiết Khí mapping
  - Validation với skyfield library
- Week 2: `ngu_hanh_engine.py` (80 LOC) + `palace_converter.py` (120 LOC)
  - Refactor Ngũ Hành logic từ analytics
  - Implement 12→9 Cung converter
  - Unit tests cho tất cả conversions

**Phase 1: Thái Ất (5-6 tuần)**
- Week 1-2: Research + Lookup tables (500 LOC)
  - Digitize 16 Thần từ sách
  - Nguyên/Hội/Kỳ calculation
- Week 3-4: Engine implementation (400 LOC)
  - `thai_at_engine.py`
  - An Thần vào 9 Cung
- Week 5: API + Frontend (200 + 200 LOC)
  - Blueprint route
  - 9 Cung grid view
- Week 6: Testing + Documentation

**Phase 2: Kì Môn (8-10 tuần)**
- Week 1-3: Research + Lookup tables (800 LOC)
  - Digitize Cục table (9 cục x 2 Dương/Âm)
  - 8 Môn + 9 Tinh + 8 Thần + 3 Kỳ positions
- Week 4-6: Engine implementation (600 LOC)
  - `qi_men_engine.py`
  - Complex Cục calculation (depends on Tiết Khí)
  - An Môn/Tinh/Thần/Kỳ vào 9 Cung
- Week 7-8: API + Frontend (300 + 250 LOC)
  - Blueprint route
  - Enhanced 9 Cung grid (nhiều layers)
- Week 9-10: Testing + Expert validation

**Phase 3: Integration (2-3 tuần)**
- Week 1: `/tri-thuc` route
  - Combined Tam Thức view
  - Switch between systems
- Week 2: Cross-system analysis
  - Compare Tử Vi + Huyền Không + Thái Ất + Kì Môn
- Week 3: Documentation + User guide

**Total: 17-21 tuần (4-5 tháng)**

| Phase | LOC New | LOC Reused | % Reuse | Duration |
|-------|---------|------------|---------|----------|
| Phase 0 | 350 | 731 | 68% | 2w |
| Phase 1 | 1100 | 731 | 40% | 5-6w |
| Phase 2 | 1950 | 731+350 | 36% | 8-10w |
| Phase 3 | 500 | 2600 | 84% | 2-3w |
| **Total** | **3900** | **875** | **18%** | **17-21w** |

---

## 5. THIẾT KẾ HỆ THỐNG

### 5.1. Architecture

```
┌─────────────────────────────────────────┐
│         localhost:5000                  │
├─────────────────────────────────────────┤
│ /                → Tử Vi truyền thống   │
│ /huyen-khong     → Huyền Không Phi Tinh │
│ /thai-at         → Thái Ất Thần Số      │ ← MỚI
│ /qi-men          → Kì Môn Độn Giáp      │ ← MỚI
│ /tri-thuc        → Tích hợp Tam Thức    │ ← PHASE 3
└─────────────────────────────────────────┘
```

### 5.2. Data Models

```python
# python/core/models.py

class ThaiAtChart:
    nguyen: str           # Giáp Tý Nguyên, ...
    hoi: int              # 0-11
    ky: int               # 0-2
    nhap_ky: int          # 0-2
    than_positions: Dict  # {than_name: palace_index}
    interpretations: List # Giải nghĩa

class QiMenChart:
    cuc: int              # 1-9
    la_duong_don: bool    # True=Dương Độn, False=Âm Độn
    tiet_khi: str         # Tiết Khí
    gio_ki_mon: int       # 1-18
    men_positions: Dict   # {men_name: palace_index}
    tinh_positions: Dict  # {tinh_name: palace_index}
    than_positions: Dict  # {than_name: palace_index}
    san_qi_positions: Dict # {qi_name: palace_index}
    interpretations: List  # Giải nghĩa
```

### 5.3. API Endpoints

```python
# Thái Ất
POST /api/thai-at/calculate
Body: {
    "year": 2024,
    "month": 12,
    "day": 24,
    "hour": 14,
    "purpose": "personal"  # personal/country/event
}

Response: {
    "status": "success",
    "data": {
        "nguyen": "Giáp Tý Nguyên",
        "hui": 6,
        "ji": 2,
        "than_positions": {
            "0": ["Thái Ất", "Văn Xương"],
            "1": ["Thanh Long"],
            ...
        },
        "interpretations": [...]
    }
}

# Kì Môn
POST /api/qi-men/calculate
Body: {
    "year": 2024,
    "month": 12,
    "day": 24,
    "hour": 14,
    "question": "business",  # business/travel/health/battle
    "location": {
        "lat": 10.8231,
        "lng": 106.6297
    }  # Optional - để tính hướng
}

Response: {
    "status": "success",
    "data": {
        "cuc": 5,
        "is_yang_dun": false,
        "jie_qi": "Đông Chí",
        "men_positions": {...},
        "tinh_positions": {...},
        "than_positions": {...},
        "san_qi_positions": {...},
        "best_direction": "Đông Nam",  # Phương hướng tốt nhất
        "best_time": "14:00-16:00",     # Thời gian tốt nhất
        "interpretations": [...]
    }
}
```

---

## 6. UI/UX DESIGN

### 6.1. Thái Ất - Layout

```
┌────────────────────────────────────────────────────────┐
│ THÁI ẤT THẦN SỐ (太乙神數)         [Về Tử Vi Chính]    │
├────────────────────────────────────────────────────────┤
│ Nhập thông tin:                                        │
│ Năm: [____] Tháng: [__] Ngày: [__] Giờ: [__:__]      │
│ Mục đích: ○ Cá nhân  ○ Quốc gia  ○ Sự kiện           │
│                                     [Tính Thái Ất]     │
├────────────────────────────────────────────────────────┤
│ KẾT QUẢ:                                               │
│ • Nguyên: Giáp Tý Nguyên (1984-2055)                  │
│ • Hội: Thứ 7/12                                        │
│ • Kỷ: Thứ 3/3                                          │
│                                                        │
│              CỬU CUNG THẬP LỤC THẦN                    │
│  ┌──────────┬──────────┬──────────┬──────────┐        │
│  │ Tỵ       │ Ngọ      │ Mùi      │ Thân     │        │
│  │ Hiên Dư  │ Thái Ất  │ Văn      │ Chiêu    │        │
│  │          │          │ Xương    │ Dao      │        │
│  ├──────────┼──────────┼──────────┼──────────┤        │
│  │ Thìn     │          │          │ Dậu      │        │
│  │ Thiên    │   TRUNG  │          │ Thanh    │        │
│  │ Phù      │   TÂM    │          │ Long     │        │
│  ├──────────┤          │          ├──────────┤        │
│  │ Mão      │          │          │ Tuất     │        │
│  │ Tùng     │          │          │ Thắng    │        │
│  │ Khuê     │          │          │ Quang    │        │
│  ├──────────┼──────────┼──────────┼──────────┤        │
│  │ Dần      │ Sửu      │ Tý       │ Hợi      │        │
│  │ Thái     │ Cửu      │ Thiên    │ Tiểu     │        │
│  │ Xung     │ Thiên    │ Cương    │ Cát      │        │
│  └──────────┴──────────┴──────────┴──────────┘        │
│                                                        │
├────────────────────────────────────────────────────────┤
│ GIẢI NGHĨA:                                            │
│ • Cung Mệnh gặp Thái Ất: Vận đạo tốt, có quý nhân     │
│ • Văn Xương tại Mùi: Văn chương thông suốt            │
│ • Thanh Long tại Dậu: Tài vận hanh thông              │
│ • ⚠️ Cảnh báo: Hệ thống Thái Ất phức tạp, cần chuyên  │
│   gia xác nhận kết quả                                │
└────────────────────────────────────────────────────────┘
```

### 6.2. Kì Môn - Layout

```
┌────────────────────────────────────────────────────────┐
│ KÌ MÔN ĐỘN GIÁP (奇門遁甲)         [Về Tử Vi Chính]    │
├────────────────────────────────────────────────────────┤
│ Nhập thông tin:                                        │
│ Năm: [____] Tháng: [__] Ngày: [__] Giờ: [__:__]      │
│ Câu hỏi về: ○ Kinh doanh  ○ Sức khỏe  ○ Du lịch      │
│ Vị trí (tùy chọn): Lat [_____] Lng [_____]            │
│                                     [Khởi Cục]         │
├────────────────────────────────────────────────────────┤
│ THÔNG TIN CỤC:                                         │
│ • Cục: 5 (Âm Độn Ngũ Cục)                             │
│ • Tiết Khí: Đông Chí                                   │
│ • Giờ Kì Môn: 7/18                                     │
│                                                        │
│ ⭐ PHƯƠNG HƯỚNG TỐT NHẤT: Đông Nam (Cung Tốn)         │
│ ⏰ THỜI ĐIỂM TỐT NHẤT: 14:00 - 16:00 (Giờ Mùi)        │
│                                                        │
│              CỬU CUNG KÌ MÔN                           │
│  ┌──────────┬──────────┬──────────┬──────────┐        │
│  │ Tỵ (離)  │ Ngọ (坤)  │ Mùi (兌) │ Thân     │        │
│  │ 門: Sinh │ 門: Hưu  │ 門: Kinh │ 門: Tử   │        │
│  │ 星: Thiên│ 星: Thiên│ 星: Thiên│ 星: Thiên│        │
│  │     Anh  │     Nhiệm│     Trụ  │     Bồng │        │
│  │ 神: Chu  │ 神: Thái │ 神: Trực │ 神: Cửu  │        │
│  │     Tước │     Âm   │     Phù  │     Thiên│        │
│  │ 奇: Bính │          │          │          │        │
│  ├──────────┼──────────┼──────────┼──────────┤        │
│  │ Thìn     │          │          │ Dậu      │        │
│  │ 門: Thương│  TRUNG   │          │ 門: Khai │        │
│  │ 星: Thiên│   TÂM    │          │ 星: Thiên│        │
│  │     Xung │          │          │     Tâm  │        │
│  │ 神: Đằng │          │          │ 神: Lục  │        │
│  │     Xà   │          │          │     Hợp  │        │
│  │ 奇: Đinh │          │          │ 奇: Ất   │        │
│  ├──────────┤          │          ├──────────┤        │
│  │ Mão      │          │          │ Tuất     │        │
│  │ 門: Cảnh │          │          │ 門: Đỗ   │        │
│  │ ...      │          │          │ ...      │        │
│  └──────────┴──────────┴──────────┴──────────┘        │
│                                                        │
├────────────────────────────────────────────────────────┤
│ PHÂN TÍCH:                                             │
│ • Cung Dậu (Đoài): Khai Môn + Thiên Tâm + Ất Kỳ      │
│   → Cực cát! Tốt cho kinh doanh, đàm phán, di chuyển │
│                                                        │
│ • Cung Ngọ (Khôn): Hưu Môn + Thiên Nhiệm + Thái Âm   │
│   → Cát. Tốt cho nghỉ ngơi, suy nghĩ, kế hoạch       │
│                                                        │
│ • Cung Thân: Tử Môn + Thiên Bồng                      │
│   → ⚠️ Hung! Tránh phương hướng này                   │
└────────────────────────────────────────────────────────┘
```

---

## 7. IMPLEMENTATION PLAN

### Phase 1: Backend - Thái Ất (Week 1-5)

**Week 1-2: Core Logic**
- [ ] Create `python/logic/thai_at_engine.py`
  - [ ] Implement `get_thai_at_nguyen()`
  - [ ] Implement `calculate_hoi_ky()`
  - [ ] Implement `an_thai_at_than()` (tra bảng)
- [ ] Create lookup tables in `python/data/thai_at_tables.json`
  - [ ] 16 Thần positions
  - [ ] Nguyên cycles
  - [ ] Hội/Kỳ mappings
- [ ] Unit tests

**Week 3: API**
- [ ] Create `python/graph/blueprints/thai_at_bp.py`
- [ ] Endpoint `POST /api/thai-at/calculate`
- [ ] Create model `ThaiAtChart`
- [ ] Integration tests

**Week 4-5: Frontend**
- [ ] Route `/thai-at` in `app.py`
- [ ] Template `templates/thai_at.html`
- [ ] JavaScript `static/js/thai_at.js`
- [ ] CSS styling

### Phase 2: Backend - Kì Môn (Week 6-13)

**Week 6-8: Core Logic (Phức tạp nhất)**
- [ ] Create `python/logic/jie_qi_calculator.py` ⭐ QUAN TRỌNG
  - [ ] Calculate 24 Tiết Khí chính xác
  - [ ] Integrate với CalendarConverter
- [ ] Create `python/logic/qi_men_engine.py`
  - [ ] Implement `get_qi_men_cuc()`
  - [ ] Implement `an_bat_mon()`
  - [ ] Implement `an_cuu_tinh_bat_than()`
  - [ ] Implement `an_tam_ky()`
- [ ] Create lookup tables in `python/data/ki_mon_tables.json`
  - [ ] Cục mappings (Tiết Khí → Cục)
  - [ ] Bát Môn positions
  - [ ] Cửu Tinh, Bát Thần positions
- [ ] Unit tests (comprehensive!)

**Week 9-10: Analysis Engine**
- [ ] Create `python/logic/qi_men_analyzer.py`
  - [ ] Analyze palace (Môn + Tinh + Thần + Tam Kỳ)
  - [ ] Calculate Cát/Hung score
  - [ ] Generate interpretations
  - [ ] Find best direction/time
- [ ] Integration with NguHanhEngine

**Week 11: API**
- [ ] Create `python/graph/blueprints/qi_men_bp.py`
- [ ] Endpoint `POST /api/qi-men/calculate`
- [ ] Create model `QiMenChart`
- [ ] Integration tests

**Week 12-13: Frontend**
- [ ] Route `/qi-men` in `app.py`
- [ ] Template `templates/qi_men.html`
- [ ] JavaScript `static/js/qi_men.js`
  - [ ] Complex grid rendering
  - [ ] Show Môn/Tinh/Thần/Kỳ layers
  - [ ] Highlight best direction
- [ ] CSS styling (color-code Cát/Hung)

### Phase 3: Integration - Tam Thức (Week 14-16)

**Week 14-15: Combined Analysis**
- [ ] Route `/tri-thuc` (Tam Thức dashboard)
- [ ] Show 3 systems side-by-side:
  - Thái Ất (Thiên)
  - Kì Môn (Địa)
  - (Lục Nhâm - optional, Phase 4)
- [ ] Cross-reference analysis
- [ ] Export reports

**Week 16: Testing & Documentation**
- [ ] E2E tests all 3 routes
- [ ] Performance optimization
- [ ] User documentation
- [ ] Help tooltips

**Tổng thời gian: 16 tuần (4 tháng)**

---

## 8. THÁCH THỨC & GIẢI PHÁP

### 8.1. Thách thức

| Thách thức | Mức độ | Giải pháp |
|------------|--------|-----------|
| Thiếu tài liệu chính thống | ⭐⭐⭐⭐⭐ | Research nhiều nguồn, consult chuyên gia |
| Tính toán Tiết Khí phức tạp | ⭐⭐⭐⭐⭐ | Dùng thư viện chính xác (astronomia) |
| Tra bảng Thái Ất/Kì Môn | ⭐⭐⭐⭐ | Digitize lookup tables từ sách |
| Giải nghĩa đa nghĩa | ⭐⭐⭐⭐ | AI-powered interpretation |
| Performance (nhiều tính toán) | ⭐⭐⭐ | Caching, lazy loading |

### 8.2. Giải pháp ưu tiên

**1. Tính toán Tiết Khí - Quan trọng nhất cho Kì Môn:**
```python
# Dùng thư viện chính xác
from skyfield.api import load, Topos
from skyfield import almanac

def calculate_jie_qi_accurate(year, month, day):
    """
    Tính Tiết Khí chính xác đến giây
    Dựa vào vị trí Mặt Trời trên hoàng đạo
    """
    ts = load.timescale()
    t0 = ts.utc(year, 1, 1)
    t1 = ts.utc(year, 12, 31)
    
    eph = load('de421.bsp')
    sun = eph['sun']
    
    # Tính 24 Tiết Khí
    jie_qi_angles = range(0, 360, 15)  # 15° mỗi tiết
    
    # ... chi tiết implementation
```

**2. Digitize Lookup Tables:**
```json
// python/data/qi_men_tables.json
{
  "cuc_mapping": {
    "dong_chi": {
      "day_gan": {
        "giap": {"duong_don": 1, "am_don": 9},
        "at": {"duong_don": 8, "am_don": 2},
        ...
      }
    },
    ...
  },
  "men_positions": {
    "cuc_1": {
      "duong_don": [1, 8, 3, 4, 9, 2, 7, 6],
      "am_don": [9, 2, 7, 6, 1, 8, 3, 4]
    },
    ...
  }
}
```

---

## 9. REFERENCES & RESOURCES

### 9.1. Sách tham khảo

**Thái Ất:**
- 《太乙神數》- Triệu Quán Ẩn
- 《太乙金鏡式經》- Vương Vĩ
- 《太乙照神經》- Tác giả không rõ

**Kì Môn:**
- 《奇門遁甲統宗》- Trương Chí Thuận (Kinh điển)
- 《奇門遁甲秘笈大全》- Lưu Bá Ôn
- 《神奇之門》- Trương Chí Xuân (Hiện đại, dễ hiểu)

### 9.2. Online Resources

- [Qimen Dunjia Calculator](https://www.fengshuicalculator.com/qimen/)
- [Chinese Metaphysics Forum](https://www.chinesemetaphysics.net/)
- [Tiết Khí Calculator](https://ytliu0.github.io/ChineseCalendar/)

### 9.3. Consult Experts

**Khuyến nghị:**
- Tìm chuyên gia Kì Môn để review công thức
- Validate kết quả với các phần mềm có sẵn
- Test với các case study lịch sử

---

## 10. RISKS & MITIGATION

### 10.1. Technical Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Sai công thức Tiết Khí | High | Critical | Dùng thư viện thiên văn chính xác |
| Lookup tables sai | High | High | Validate với nhiều nguồn |
| Performance chậm | Medium | Medium | Caching, optimize algorithms |
| Thiếu chuyên gia review | High | High | Consult online communities |

### 10.2. User Experience Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Quá phức tạp cho user | High | High | Simplify UI, provide examples |
| Kết quả khó hiểu | High | Medium | Rich interpretations, tooltips |
| Mất niềm tin nếu sai | Medium | Critical | Disclaimer, accuracy warnings |

---

## 11. SUCCESS METRICS

### 11.1. Technical Metrics
- [ ] Accuracy: >95% so với phần mềm chuyên nghiệp
- [ ] Performance: <2s cho mỗi calculation
- [ ] Test coverage: >80%
- [ ] Uptime: >99%

### 11.2. User Metrics
- [ ] User adoption: >100 users/month
- [ ] User satisfaction: >4.0/5.0
- [ ] Return rate: >30%
- [ ] Export/share: >20% của users

---

## 12. NEXT STEPS

### 12.1. Immediate Actions (This Week)

1. **Research Phase:**
   - [ ] Collect Thái Ất & Kì Môn reference books
   - [ ] Study existing online calculators
   - [ ] Document all formulas & lookup tables

2. **Technical Prep:**
   - [ ] Install skyfield library for Tiết Khí
   - [ ] Setup data folder for lookup tables
   - [ ] Create stub files for new modules

3. **Validation Prep:**
   - [ ] Find Kì Môn experts to consult
   - [ ] Prepare test cases from historical events
   - [ ] Setup comparison with existing tools

### 12.2. Phase 1 Kickoff (Next Week)

- [ ] Start `thai_at_engine.py` implementation
- [ ] Create `ThaiAtChart` model
- [ ] Begin frontend mockups

---

## 13. COMPARISON WITH OTHER FEATURES

| Feature | Complexity | Development Time | User Value | Priority |
|---------|-----------|------------------|------------|----------|
| Huyền Không Phi Tinh | ⭐⭐⭐⭐ | 6-7 weeks | ⭐⭐⭐⭐ High | ✅ Done |
| Thái Ất Thần Số | ⭐⭐⭐⭐⭐ | 5 weeks | ⭐⭐⭐ Medium | 🟡 Next |
| Kì Môn Độn Giáp | ⭐⭐⭐⭐⭐ | 8 weeks | ⭐⭐⭐⭐⭐ Very High | 🟢 Priority |
| Tích hợp Tam Thức | ⭐⭐⭐ | 3 weeks | ⭐⭐⭐⭐ High | 🔵 Phase 3 |

**Recommendation:**
- Implement Kì Môn trước Thái Ất (higher user value)
- Thái Ất có thể làm simplified version
- Focus effort on Tiết Khí calculation (critical for Kì Môn)

---

**Document Version:** 1.0  
**Last Updated:** 2024-12-24  
**Author:** AI Assistant (BA)  
**Status:** Draft - Ready for Review  
**Estimated Total Effort:** 16 weeks (4 months)  
**Recommendation:** Proceed with Kì Môn implementation first
