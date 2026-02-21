# 📋 BÁO CÁO RÀ SOÁT CODE DỰ ÁN TỬ VI

**Ngày:** 22/12/2025  
**Người thực hiện:** QC Engineer

---

## 🔴 VẤN ĐỀ NGHIÊM TRỌNG (CRITICAL)

### 1. BẢNG CUC_TABLE KHÔNG ĐƯỢC SỬ DỤNG

**File:** `core/cuc_calc.py`, `chart/chart_builder.py`

**Mô tả:**
- Bảng `CUC_TABLE` trong `data/cung_cuc.py` được định nghĩa nhưng **KHÔNG ĐƯỢC DÙNG** trong logic chính
- Hàm `determine_cuc()` trong `core/cuc_calc.py` tính Cục bằng **công thức thuật toán** thay vì tra bảng
- `chart_builder.py` gọi `determine_cuc()`, không phải tra `CUC_TABLE`

**Hậu quả:**
- Việc sửa bảng `CUC_TABLE` không ảnh hưởng đến kết quả thực tế
- Test dùng `CUC_TABLE` để verify có thể cho kết quả sai
- Có 2 nguồn sự thật (source of truth) gây confusion

**Đề xuất sửa:**
```python
# Option A: Sửa determine_cuc() để dùng CUC_TABLE
def determine_cuc(year_can_index: int, menh_chi_index: int) -> dict:
    from data import CUC_TABLE, CUC_TYPE
    cuc_name = CUC_TABLE[year_can_index % 5][menh_chi_index]  # Giảm về 5 cặp
    return {'name': cuc_name, 'number': CUC_TYPE[cuc_name]}

# Option B: Xóa CUC_TABLE, chỉ dùng công thức (hiện tại)
```

---

### 2. BẢNG CUC_TABLE SAI DỮ LIỆU

**File:** `data/cung_cuc.py`

**Mô tả:**
Bảng `CUC_TABLE` có comment mô tả đúng nhưng **data thực tế SAI**:

| Chi | Comment đúng | CUC_TABLE thực tế | Status |
|-----|--------------|-------------------|--------|
| 0 (Tý) | Thủy Nhị Cục | Thủy Nhị Cục | ✅ |
| 1 (Sửu) | **Hỏa Lục Cục** | Thủy Nhị Cục | ❌ SAI |
| 2 (Dần) | **Mộc Tam Cục** | Hỏa Lục Cục | ❌ SAI |
| 3 (Mão) | Mộc Tam Cục | Hỏa Lục Cục | ❌ SAI |
| 4 (Thìn) | **Kim Tứ Cục** | Mộc Tam Cục | ❌ SAI |
| 5 (Tỵ) | Kim Tứ Cục | Mộc Tam Cục | ❌ SAI |
| 6 (Ngọ) | Thổ Ngũ Cục | Thổ Ngũ Cục | ✅ |
| 7 (Mùi) | Thổ Ngũ Cục | Thổ Ngũ Cục | ✅ |
| 8 (Thân) | **Hỏa Lục Cục** | Kim Tứ Cục | ❌ SAI |
| 9 (Dậu) | Hỏa Lục Cục | Kim Tứ Cục | ❌ SAI |
| 10 (Tuất) | **Thủy Nhị Cục** | Hỏa Lục Cục | ❌ SAI |
| 11 (Hợi) | Thủy Nhị Cục | Hỏa Lục Cục | ❌ SAI |

**Đề xuất sửa:** Sửa data trong CUC_TABLE khớp với comment (Bảng chuẩn Nam Phái)

---

## 🟡 VẤN ĐỀ TRUNG BÌNH (MEDIUM)

### 3. CODE TRÙNG LẶP TRONG CHART BUILDER

**File:** `chart/chart_builder.py`

**Mô tả:**
- `generate_birth_chart()` và `generate_birth_chart_lunar()` có ~80% code giống nhau
- Chỉ khác phần xử lý input date

**Đề xuất sửa:**
```python
def _build_chart_internal(lunar: dict, hour_index: int, gender: str, 
                          solar_date: dict = None) -> dict:
    """Hàm nội bộ chung cho cả 2 loại input"""
    # ... logic chung ...

def generate_birth_chart(day, month, year, hour, gender):
    lunar = solar_to_lunar(day, month, year)
    return _build_chart_internal(lunar, hour, gender, {'day': day, 'month': month, 'year': year})

def generate_birth_chart_lunar(lunar_day, lunar_month, lunar_year, hour, gender, leap_month=False):
    lunar = {'day': lunar_day, 'month': lunar_month, 'year': lunar_year, 'leap': leap_month}
    return _build_chart_internal(lunar, hour, gender)
```

---

### 4. GIÁ TRỊ GIỜ TRONG HTML KHÔNG NHẤT QUÁN

**File:** `templates/index.html`

**Mô tả:**
Dropdown giờ sinh gửi giá trị **giờ 24h** (0, 2, 4, 6...) thay vì **Chi index** (0-11):

```html
<option value="0">Tý (23-01h)</option>    <!-- Value 0 = OK -->
<option value="2">Sửu (01-03h)</option>    <!-- Value 2 ≠ Chi index 1 -->
<option value="12" selected>Ngọ (11-13h)</option>  <!-- Value 12 ≠ Chi index 6 -->
```

**Backend xử lý:**
```python
# app.py
hour_index = solar_hour_to_chi_index(hour_val)  # Chuyển 0-23 → 0-11
```

**Đề xuất sửa:**
```html
<!-- Option A: Gửi trực tiếp Chi index -->
<option value="0">Tý (23-01h)</option>
<option value="1">Sửu (01-03h)</option>
<option value="6">Ngọ (11-13h)</option>  <!-- Chi index trực tiếp -->
```

---

### 5. IMPORT KHÔNG CẦN THIẾT VÀ CÓ THỂ GÂY LỖI

**File:** `app.py`

**Mô tả:**
```python
from analytics.visualize_data import get_visualization_data  # Line 49
```
- Import này có thể fail nếu folder `analytics` không tồn tại
- Nên dùng lazy import

**Đề xuất sửa:**
```python
@app.route('/analytics/beauty')
def analytics_beauty():
    from analytics.visualize_data import get_visualization_data  # Lazy import
    ...
```

---

### 6. EXCEPTION HANDLING THIẾU THÔNG TIN

**File:** `app.py` - Line 80-82

**Mô tả:**
```python
try:
    day = int(data.get('day')) if data.get('day') else None
except: day = None  # Bare except - không biết lỗi gì
```

**Đề xuất sửa:**
```python
try:
    day = int(data.get('day')) if data.get('day') else None
except (ValueError, TypeError):
    day = None
```

---

## 🟢 VẤN ĐỀ NHẸ (LOW)

### 7. MAGIC NUMBERS KHÔNG CÓ CONSTANT

**File:** `core/cung_menh.py`

```python
position = 2 + (lunar_month - 1) - hour_index  # 2 = Dần index
```

**Đề xuất:** 
```python
DAN_INDEX = 2  # Dần position
position = DAN_INDEX + (lunar_month - 1) - hour_index
```

---

### 8. COMMENT TIẾNG VIỆT VÀ TIẾNG ANH TRỘN LẪN

**Đề xuất:** Thống nhất dùng tiếng Việt cho comment về nghiệp vụ Tử Vi, tiếng Anh cho comment kỹ thuật

---

### 9. THIẾU TYPE HINTS Ở MỘT SỐ HÀM

**File:** `app.py`

```python
def solar_hour_to_chi_index(h):  # Thiếu type hint
```

**Đề xuất:**
```python
def solar_hour_to_chi_index(h: int) -> int:
```

---

### 10. POSITIONS DICT DÙNG INDEX THAY VÌ CHI NAME

**File:** `chart/chart_builder.py`

**Mô tả:**
```python
positions = {0: {...}, 1: {...}, ...}  # Dùng số
```

**Đề xuất:** Cân nhắc dùng Chi name làm key cho dễ debug:
```python
positions = {'Tý': {...}, 'Sửu': {...}, ...}
```

---

## 📊 TÓM TẮT

| Mức độ | Số lượng | Cần sửa ngay |
|--------|----------|--------------|
| 🔴 Critical | 2 | ✅ CẦN SỬA NGAY |
| 🟡 Medium | 4 | Nên sửa |
| 🟢 Low | 4 | Tùy chọn |

---

## 🔧 ĐỀ XUẤT HÀNH ĐỘNG

### Ưu tiên 1 (Hotfix):
1. **Sửa bảng CUC_TABLE** hoặc **Xóa bỏ** nếu không dùng
2. **Thống nhất** nguồn sự thật về Cục (Table vs Algorithm)

### Ưu tiên 2 (Sprint tiếp):
3. Refactor chart builder để giảm code trùng lặp
4. Thống nhất format giờ giữa frontend và backend

### Ưu tiên 3 (Tech debt):
5. Thêm type hints
6. Cải thiện error handling
7. Lazy imports

---

*Báo cáo tạo tự động bởi QC System*

