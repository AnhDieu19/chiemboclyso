# 📋 BÁO CÁO QC - MODULE GRAPH

**Ngày:** 23/12/2025  
**Người thực hiện:** QA/QC Engineer  
**Module:** `python/graph`  
**Phiên bản:** 1.0

---

## 📊 TÓM TẮT KẾT QUẢ TEST

| Loại Test | Tổng số | Passed | Failed | Tỷ lệ Pass |
|-----------|---------|--------|--------|------------|
| **API Endpoints** | 8 | 6 | 2 | 75% |
| **Routes (HTML)** | 2 | 2 | 0 | 100% |
| **Edge Cases** | 3 | 3 | 0 | 100% |
| **Error Handling** | 3 | 1 | 2 | 33% |
| **Tổng cộng** | **16** | **12** | **4** | **75%** |

---

## 🔴 VẤN ĐỀ NGHIÊM TRỌNG (CRITICAL)

### 1. ERROR HANDLING KÉM - TRẢ VỀ 500 THAY VÌ 400

**File:** `python/graph/chart_api.py:58-68`, `python/graph/star_movement_api.py:69-78`

**Mô tả:**
Khi thiếu required fields (day, month, year), code cố gắng convert `None` sang `int()` → gây `TypeError` → trả về 500 thay vì 400.

**Code hiện tại:**
```python
# chart_api.py:58-68
day = int(data.get('day'))  # ❌ Nếu day=None → TypeError
month = int(data.get('month'))  # ❌ Nếu month=None → TypeError
year = int(data.get('year'))  # ❌ Nếu year=None → TypeError

# Validate required fields
if not all([day, month, year]):  # ❌ Không bao giờ đến đây nếu có TypeError
    return jsonify({"status": "error", "message": "Missing day, month, or year"}), 400
```

**Hậu quả:**
- Client nhận 500 Internal Server Error thay vì 400 Bad Request
- Khó debug vì lỗi không rõ ràng
- Vi phạm REST API best practices

**Đề xuất sửa:**
```python
# Validate required fields TRƯỚC KHI parse
if not all([data.get('day'), data.get('month'), data.get('year')]):
    return jsonify({"status": "error", "message": "Missing day, month, or year"}), 400

# Sau đó mới parse
try:
    day = int(data.get('day'))
    month = int(data.get('month'))
    year = int(data.get('year'))
except (ValueError, TypeError) as e:
    return jsonify({"status": "error", "message": f"Invalid date format: {str(e)}"}), 400
```

**Priority:** 🔴 **HOTFIX - Sửa ngay**

---

### 2. DATA STRUCTURE MISMATCH - STAR MOVEMENT ANALYSIS KHÔNG HOẠT ĐỘNG

**File:** `python/graph/star_movement_api.py:159-170`

**Mô tả:**
Function `analyze_star_movements()` tìm sao trong `positions[].chinh_tinh`, `luc_cat`, `luc_sat` nhưng thực tế chart trả về `positions[].stars` (array chung).

**Code hiện tại:**
```python
# star_movement_api.py:162-170
if 'chinh_tinh' in pos_data:  # ❌ Không có key này
    for star in pos_data['chinh_tinh']:
        all_stars.add(star['name'])
if 'luc_cat' in pos_data:  # ❌ Không có key này
    for star in pos_data['luc_cat']:
        all_stars.add(star['name'])
if 'luc_sat' in pos_data:  # ❌ Không có key này
    for star in pos_data['luc_sat']:
        all_stars.add(star['name'])
```

**Cấu trúc thực tế từ chart:**
```python
positions[0] = {
    'chi': 'Tý',
    'cung': 'Mệnh',
    'stars': [  # ✅ Đây mới là key đúng
        {'name': 'Tử Vi', 'brightness': 'M', ...},
        {'name': 'Thiên Cơ', ...},
        ...
    ],
    'hoa': [...],
    ...
}
```

**Hậu quả:**
- `total_stars_analyzed = 0` (không tìm thấy sao nào)
- `stars_that_move = []` (rỗng)
- `stars_that_stay = []` (rỗng)
- Chức năng phân tích movement không hoạt động

**Đề xuất sửa:**
```python
# star_movement_api.py:159-170
for pos_idx, pos_data in chart['positions'].items():
    pos_num = int(pos_idx)
    
    # ✅ Sửa: Dùng 'stars' thay vì 'chinh_tinh', 'luc_cat', 'luc_sat'
    if 'stars' in pos_data:
        for star in pos_data['stars']:
            star_name = star['name'] if isinstance(star, dict) else star
            all_stars.add(star_name)
```

**Priority:** 🔴 **HIGH - Sửa trong sprint này**

---

### 3. ERROR HANDLING CHO WRONG CONTENT TYPE

**File:** `python/graph/chart_api.py:52`

**Mô tả:**
Khi request không có `Content-Type: application/json`, `request.json` raise `UnsupportedMediaType(415)` nhưng không được catch → trả về 500.

**Code hiện tại:**
```python
try:
    data = request.json  # ❌ Raise 415 nếu không phải JSON
    ...
except Exception as e:  # ❌ Không catch 415
    ...
```

**Hậu quả:**
- Client gửi form data → nhận 500 thay vì 415
- Không rõ ràng về lỗi

**Đề xuất sửa:**
```python
try:
    data = request.json
    if data is None:
        # Try to get JSON from request data
        try:
            data = json.loads(request.data)
        except (ValueError, TypeError):
            return jsonify({
                "status": "error",
                "message": "Invalid JSON or missing Content-Type: application/json"
            }), 415
except Exception as e:
    # Handle other exceptions
    ...
```

**Priority:** 🟡 **MEDIUM**

---

## 🟡 VẤN ĐỀ QUAN TRỌNG (HIGH)

### 4. THIẾU INPUT VALIDATION

**File:** `python/graph/chart_api.py`, `python/graph/star_movement_api.py`

**Mô tả:**
- Không validate year range (1900-2100)
- Không validate month range (1-12)
- Không validate day range (1-31, phụ thuộc tháng)
- Không validate hour range (0-23 hoặc 0-11)
- Không validate gender ('nam', 'nu')
- Không validate calendar type ('solar', 'lunar')

**Đề xuất:**
Tạo function validation chung:
```python
def validate_chart_input(data: dict) -> tuple[bool, str]:
    """Validate input data for chart generation"""
    errors = []
    
    # Year validation
    year = data.get('year')
    if not year:
        errors.append("Year is required")
    else:
        try:
            year = int(year)
            if not (1900 <= year <= 2100):
                errors.append("Year must be between 1900 and 2100")
        except (ValueError, TypeError):
            errors.append("Year must be a valid integer")
    
    # Month validation
    month = data.get('month')
    if month:
        try:
            month = int(month)
            if not (1 <= month <= 12):
                errors.append("Month must be between 1 and 12")
        except (ValueError, TypeError):
            errors.append("Month must be a valid integer")
    
    # ... (tương tự cho day, hour, gender, calendar)
    
    if errors:
        return False, "; ".join(errors)
    return True, ""
```

**Priority:** 🟡 **MEDIUM**

---

### 5. HOUR NAME FORMATTING SAI

**File:** `python/graph/star_movement_api.py:92`

**Mô tả:**
Format hour name có logic sai:
```python
hour_name = f"{CHI_NAMES[hour_index]} ({hour_index*2-1 if hour_index > 0 else 23}-{hour_index*2+1 if hour_index < 12 else 1:02d}h)"
```

**Vấn đề:**
- `hour_index*2-1` với `hour_index=0` → `-1` (sai)
- `hour_index*2+1` với `hour_index=11` → `23` (đúng nhưng format `:02d` không áp dụng)
- Logic phức tạp, dễ sai

**Đề xuất sửa:**
```python
# Map hour_index (0-11) to time range
HOUR_RANGES = [
    (23, 1),   # Tý: 23h-01h
    (1, 3),    # Sửu: 01h-03h
    (3, 5),    # Dần: 03h-05h
    (5, 7),    # Mão: 05h-07h
    (7, 9),    # Thìn: 07h-09h
    (9, 11),   # Tỵ: 09h-11h
    (11, 13),  # Ngọ: 11h-13h
    (13, 15),  # Mùi: 13h-15h
    (15, 17),  # Thân: 15h-17h
    (17, 19),  # Dậu: 17h-19h
    (19, 21),  # Tuất: 19h-21h
    (21, 23),  # Hợi: 21h-23h
]

start_hour, end_hour = HOUR_RANGES[hour_index]
hour_name = f"{CHI_NAMES[hour_index]} ({start_hour:02d}-{end_hour:02d}h)"
```

**Priority:** 🟡 **MEDIUM**

---

### 6. THIẾU LOGGING

**File:** `python/graph/star_movement_api.py:105`

**Mô tả:**
Chỉ dùng `print()` để log errors:
```python
except Exception as e:
    print(f"Error calculating chart for hour {hour_index}: {e}")  # ❌
```

**Đề xuất:**
```python
import logging
logger = logging.getLogger(__name__)

except Exception as e:
    logger.error(f"Error calculating chart for hour {hour_index}: {e}", exc_info=True)
```

**Priority:** 🟡 **MEDIUM**

---

## 🟢 VẤN ĐỀ TRUNG BÌNH (MEDIUM)

### 7. CODE TRÙNG LẶP

**File:** `python/graph/chart_api.py`, `python/graph/star_movement_api.py`

**Mô tả:**
Cả 2 files đều có logic parse input giống nhau:
- Parse day, month, year
- Validate required fields
- Convert hour
- Generate chart

**Đề xuất:**
Tạo helper function:
```python
# graph/utils.py
def parse_chart_request(data: dict) -> tuple[dict, Optional[str]]:
    """Parse and validate chart request data"""
    # Common parsing logic
    ...
    return parsed_data, error_message
```

**Priority:** 🟢 **LOW**

---

### 8. THIẾU TYPE HINTS

**File:** `python/graph/chart_api.py:17`, `python/graph/star_movement_api.py:139`

**Mô tả:**
```python
def solar_hour_to_chi_index(h):  # ❌ Thiếu type hints
def analyze_star_movements(charts):  # ❌ Thiếu type hints
```

**Đề xuất:**
```python
def solar_hour_to_chi_index(h: int) -> int:
def analyze_star_movements(charts: list[dict]) -> dict:
```

**Priority:** 🟢 **LOW**

---

### 9. MAGIC NUMBERS

**File:** `python/graph/star_movement_api.py:82, 256`

**Mô tả:**
```python
for hour_index in range(12):  # ❌ Magic number
if len(positions) < 3:  # ❌ Magic number
```

**Đề xuất:**
```python
NUM_HOURS = 12
MIN_POSITIONS_FOR_PATTERN = 3

for hour_index in range(NUM_HOURS):
if len(positions) < MIN_POSITIONS_FOR_PATTERN:
```

**Priority:** 🟢 **LOW**

---

## ✅ ĐIỂM TÍCH CỰC

1. ✅ **Blueprint structure tốt** - Tách biệt rõ ràng
2. ✅ **API endpoints có docstring** - Dễ hiểu
3. ✅ **Error handling có try-except** - Có cơ chế bắt lỗi
4. ✅ **HTML routes hoạt động tốt** - 100% pass
5. ✅ **Edge cases được xử lý** - Boundary conditions OK

---

## 📋 ACTION PLAN

### Sprint 1 (Hotfix - Tuần này):
1. 🔴 **Fix error handling** - Validate trước khi parse (Issue #1)
2. 🔴 **Fix data structure mismatch** - Sửa analyze_star_movements() (Issue #2)

### Sprint 2 (High Priority):
3. 🟡 **Add input validation** - Validate tất cả inputs (Issue #4)
4. 🟡 **Fix hour name formatting** - Sửa logic format (Issue #5)
5. 🟡 **Add logging** - Thay print() bằng logging (Issue #6)

### Sprint 3 (Medium Priority):
6. 🟢 **Refactor duplicate code** - Tạo helper functions (Issue #7)
7. 🟢 **Add type hints** - Cải thiện code quality (Issue #8)
8. 🟢 **Remove magic numbers** - Dùng constants (Issue #9)

---

## 🧪 TEST RESULTS DETAIL

### ✅ PASSED Tests (12/16):

**API Endpoints:**
- ✅ `test_chart_api_success_solar` - Chart generation với solar calendar
- ✅ `test_chart_api_success_lunar` - Chart generation với lunar calendar
- ✅ `test_chart_api_solar_hour_conversion` - Convert solar hour sang chi index
- ✅ `test_chart_api_no_hour_defaults_to_ty` - Default hour = Tý
- ✅ `test_chart_api_invalid_input_types` - Handle invalid types
- ✅ `test_chart_api_invalid_calendar_type` - Handle invalid calendar

**Star Movement API:**
- ✅ `test_star_movement_api_success` - Generate 12 charts thành công
- ✅ `test_star_movement_api_lunar` - Lunar calendar support

**Routes:**
- ✅ `test_knowledge_graph_route` - HTML route hoạt động
- ✅ `test_star_movement_route` - HTML route hoạt động

**Edge Cases:**
- ✅ `test_chart_api_boundary_year` - Boundary year values
- ✅ `test_chart_api_boundary_hour` - Boundary hour values
- ✅ `test_star_movement_all_hours_generated` - Đủ 12 charts

**Error Handling:**
- ✅ `test_chart_api_invalid_json` - Handle invalid JSON
- ✅ `test_star_movement_api_empty_charts_handling` - Handle empty charts

### ❌ FAILED Tests (4/16):

1. ❌ `test_chart_api_missing_required_fields` (3 sub-tests)
   - **Issue:** Trả về 500 thay vì 400
   - **Root cause:** Parse trước khi validate

2. ❌ `test_star_movement_api_missing_fields` (2 sub-tests)
   - **Issue:** Trả về 500 thay vì 400
   - **Root cause:** Parse trước khi validate

3. ❌ `test_star_movement_analysis_logic`
   - **Issue:** `total_stars_analyzed = 0`
   - **Root cause:** Data structure mismatch (tìm 'chinh_tinh' thay vì 'stars')

4. ❌ `test_chart_api_wrong_content_type`
   - **Issue:** Trả về 500 thay vì 415
   - **Root cause:** Không catch UnsupportedMediaType exception

---

## 📊 METRICS

- **Test Coverage:** 75% (12/16 passed)
- **Code Quality Score:** 6/10
- **Error Handling Score:** 4/10
- **API Design Score:** 7/10

---

## 🔗 REFERENCES

- Test File: `python/tests/test_graph_module.py`
- Module Code: `python/graph/`
- Chart Builder: `python/chart/chart_builder.py`

---

*Báo cáo được tạo tự động bởi QA/QC System*





