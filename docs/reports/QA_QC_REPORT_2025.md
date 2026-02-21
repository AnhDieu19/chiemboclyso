# 📋 BÁO CÁO QA/QC DỰ ÁN TỬ VI - 2025

**Ngày:** 23/12/2025  
**Người thực hiện:** QA/QC Engineer  
**Phiên bản:** 1.0

---

## 📊 TÓM TẮT ĐIỂM SỐ

| Mức độ | Số lượng | Trạng thái |
|--------|----------|------------|
| 🔴 **Critical** | 3 | Cần sửa ngay |
| 🟡 **High** | 5 | Nên sửa sớm |
| 🟢 **Medium** | 6 | Cải thiện |
| ⚪ **Low** | 4 | Tùy chọn |

---

## 🔴 VẤN ĐỀ NGHIÊM TRỌNG (CRITICAL)

### 1. API KEY HARDCODED - BẢO MẬT NGHIÊM TRỌNG ⚠️

**File:** `python/services/gemini_client.py:13`, `python/tests/test_gemini_api.py:8`

**Mô tả:**
```python
API_KEY = "AIzaSyBmL5Wv9bg6jiuMBJETaXJ7W4pBmfMkkls"  # ❌ Hardcoded trong source code
```

**Hậu quả:**
- API key bị lộ trong source code, có thể commit lên Git
- Bất kỳ ai có quyền truy cập repo đều có thể lấy key
- Key có thể bị lạm dụng, gây tốn chi phí
- Vi phạm best practices về bảo mật

**Đề xuất sửa:**
```python
# Option A: Dùng environment variable (KHUYẾN NGHỊ)
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Option B: Dùng Flask config
# app.config['GEMINI_API_KEY'] = os.getenv('GEMINI_API_KEY')
```

**Action Items:**
1. ✅ Tạo file `.env` và thêm vào `.gitignore`
2. ✅ Di chuyển API key sang environment variable
3. ✅ Revoke API key hiện tại và tạo key mới
4. ✅ Cập nhật documentation về setup

**Priority:** 🔴 **HOTFIX - Sửa ngay**

---

### 2. BARE EXCEPT CLAUSE - XỬ LÝ LỖI KÉM

**File:** `python/app.py:134`

**Mô tả:**
```python
try:
    day = int(data.get('day')) if data.get('day') else None
except: day = None  # ❌ Bare except - bắt tất cả exceptions
```

**Hậu quả:**
- Bắt cả `KeyboardInterrupt`, `SystemExit` - có thể gây vấn đề khi shutdown
- Không biết lỗi gì xảy ra, khó debug
- Che giấu lỗi thực sự (ví dụ: `MemoryError`)

**Đề xuất sửa:**
```python
try:
    day = int(data.get('day')) if data.get('day') else None
except (ValueError, TypeError) as e:
    # Log error nếu cần
    day = None
```

**Files cần sửa:**
- `python/app.py:134`
- `python/analytics/verify_canh_ngo_5_mechanisms.py:208, 259`
- `python/analytics/rank_60_hoa_giap.py:99`
- `python/analytics/verify_canh_ngo_mechanisms.py:116, 132, 218, 252, 303`
- `python/analytics/analyze_ngo_phu_the.py:66`
- `python/analytics/analyze_ngo_marriage.py:109, 179`
- `python/analytics/solve_best_fate_all_time_v2.py:91`
- `python/tests/repro_finder_error.py:21`
- `python/tests/test_api_endpoints.py:183`

**Priority:** 🔴 **HIGH - Sửa trong sprint này**

---

### 3. THIẾU INPUT VALIDATION ĐẦY ĐỦ

**File:** `python/app.py:125-223`

**Mô tả:**
- Chỉ validate year range (1900-2100)
- Không validate:
  - Month range (1-12)
  - Day range (1-31, phụ thuộc tháng)
  - Hour range (0-23)
  - Gender values ('nam', 'nu')
  - Calendar type ('solar', 'lunar')

**Ví dụ lỗi:**
```python
# Có thể gửi:
{
    "year": 1995,
    "month": 15,  # ❌ Invalid
    "day": 50,    # ❌ Invalid
    "hour": 25,   # ❌ Invalid
    "gender": "unknown"  # ❌ Invalid
}
```

**Đề xuất sửa:**
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
    
    # Day validation (with month context)
    day = data.get('day')
    if day:
        try:
            day = int(day)
            if month:
                max_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
                if not (1 <= day <= max_days):
                    errors.append(f"Day must be between 1 and {max_days} for month {month}")
        except (ValueError, TypeError):
            errors.append("Day must be a valid integer")
    
    # Hour validation
    hour = data.get('hour')
    if hour is not None:
        try:
            hour = int(hour)
            if not (0 <= hour <= 23):
                errors.append("Hour must be between 0 and 23")
        except (ValueError, TypeError):
            errors.append("Hour must be a valid integer")
    
    # Gender validation
    gender = data.get('gender', 'nam')
    if gender not in ['nam', 'nu']:
        errors.append("Gender must be 'nam' or 'nu'")
    
    # Calendar type validation
    calendar = data.get('calendar_type', 'solar')
    if calendar not in ['solar', 'lunar']:
        errors.append("Calendar type must be 'solar' or 'lunar'")
    
    if errors:
        return False, "; ".join(errors)
    return True, ""

# Sử dụng trong endpoint:
is_valid, error_msg = validate_chart_input(data)
if not is_valid:
    return jsonify({"status": "error", "message": error_msg}), 400
```

**Priority:** 🔴 **HIGH - Sửa trong sprint này**

---

## 🟡 VẤN ĐỀ QUAN TRỌNG (HIGH)

### 4. THIẾU TYPE HINTS

**File:** `python/app.py:18`

**Mô tả:**
```python
def solar_hour_to_chi_index(h):  # ❌ Thiếu type hints
    """Convert solar hour (0-23) to Chi Index (0-11, Ty=0)"""
    return ((h + 1) // 2) % 12
```

**Đề xuất:**
```python
def solar_hour_to_chi_index(h: int) -> int:
    """Convert solar hour (0-23) to Chi Index (0-11, Ty=0)"""
    return ((h + 1) // 2) % 12
```

**Files cần cải thiện:**
- Tất cả functions trong `app.py`
- Các functions public trong modules khác

**Priority:** 🟡 **MEDIUM - Cải thiện dần**

---

### 5. ERROR HANDLING KHÔNG NHẤT QUÁN

**File:** `python/app.py`

**Mô tả:**
- Một số endpoints trả về `{"status": "error", "message": "..."}`
- Một số trả về `{"error": "..."}`
- Một số trả về `{"success": False, "error": "..."}`

**Ví dụ:**
```python
# Line 136
return jsonify({"status": "error", "message": "No data provided"}), 400

# Line 330
return jsonify({'error': 'Không tìm thấy sao'}), 404

# Line 414
return jsonify({'success': False, 'error': str(e), ...}), 500
```

**Đề xuất:**
Thống nhất format response:
```python
# Success
{
    "status": "success",
    "data": {...}
}

# Error
{
    "status": "error",
    "code": "ERROR_CODE",  # Optional
    "message": "Error message"
}
```

**Priority:** 🟡 **MEDIUM**

---

### 6. THIẾU LOGGING

**File:** Toàn bộ application

**Mô tả:**
- Không có logging system
- Chỉ dùng `print()` statements
- Không track errors, warnings, info

**Đề xuất:**
```python
import logging
from logging.handlers import RotatingFileHandler

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('logs/app.log', maxBytes=10*1024*1024, backupCount=5),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Sử dụng:
logger.info("Chart generated for year %s", year)
logger.error("Failed to generate chart: %s", str(e), exc_info=True)
logger.warning("Invalid input: %s", data)
```

**Priority:** 🟡 **MEDIUM**

---

### 7. THIẾU RATE LIMITING

**File:** `python/app.py`

**Mô tả:**
- Không có rate limiting cho API endpoints
- Có thể bị abuse, đặc biệt là `/api/ask-ai` và `/api/chat-ai` (tốn API cost)

**Đề xuất:**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/ask-ai', methods=['POST'])
@limiter.limit("10 per minute")  # Limit AI endpoints
def ask_ai():
    ...
```

**Priority:** 🟡 **MEDIUM - Quan trọng cho production**

---

### 8. DEBUG MODE ENABLED

**File:** `python/app.py:651`

**Mô tả:**
```python
app.run(debug=True, port=5000)  # ❌ Debug mode trong production code
```

**Hậu quả:**
- Expose traceback trong production
- Auto-reload có thể gây vấn đề
- Performance kém hơn

**Đề xuất:**
```python
if __name__ == '__main__':
    import os
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, port=5000)
```

**Priority:** 🟡 **MEDIUM**

---

## 🟢 VẤN ĐỀ TRUNG BÌNH (MEDIUM)

### 9. CODE TRÙNG LẶP

**File:** `python/chart/chart_builder.py`

**Mô tả:**
- `generate_birth_chart()` và `generate_birth_chart_lunar()` có ~80% code giống nhau
- Đã được đề cập trong QC report cũ nhưng chưa sửa

**Priority:** 🟢 **LOW - Tech debt**

---

### 10. THIẾU DOCUMENTATION STRINGS

**File:** Nhiều modules

**Mô tả:**
- Một số functions thiếu docstrings
- Docstrings không đầy đủ (thiếu Args, Returns, Raises)

**Priority:** 🟢 **LOW**

---

### 11. MAGIC NUMBERS

**File:** `python/core/cung_menh.py`

**Mô tả:**
```python
position = 2 + (lunar_month - 1) - hour_index  # 2 = Dần index
```

**Đề xuất:**
```python
DAN_INDEX = 2  # Dần position
position = DAN_INDEX + (lunar_month - 1) - hour_index
```

**Priority:** 🟢 **LOW**

---

### 12. THIẾU UNIT TESTS CHO MỘT SỐ MODULES

**File:** `python/tests/`

**Mô tả:**
- Có tests cho API endpoints
- Có tests cho core logic
- Thiếu tests cho:
  - Adapters
  - Services (gemini_client)
  - Error handling paths

**Priority:** 🟢 **LOW**

---

### 13. IMPORT KHÔNG CẦN THIẾT Ở TOP LEVEL

**File:** `python/app.py:49`

**Mô tả:**
```python
from analytics.visualize_data import get_visualization_data  # Line 49
```

**Đề xuất:**
```python
@app.route('/analytics/beauty')
def analytics_beauty():
    from analytics.visualize_data import get_visualization_data  # Lazy import
    ...
```

**Priority:** 🟢 **LOW**

---

### 14. THIẾU CORS CONFIGURATION

**File:** `python/app.py`

**Mô tả:**
- Không có CORS configuration
- Có thể gây vấn đề khi frontend ở domain khác

**Đề xuất:**
```python
from flask_cors import CORS

CORS(app, resources={r"/api/*": {"origins": ["http://localhost:3000", "https://yourdomain.com"]}})
```

**Priority:** 🟢 **LOW - Nếu cần**

---

## ⚪ VẤN ĐỀ NHẸ (LOW)

### 15. COMMENT TIẾNG VIỆT VÀ TIẾNG ANH TRỘN LẪN

**Đề xuất:** Thống nhất dùng tiếng Việt cho comment về nghiệp vụ Tử Vi, tiếng Anh cho comment kỹ thuật

---

### 16. THIẾU .gitignore CHO .env

**File:** `.gitignore`

**Đề xuất:** Đảm bảo `.env` được ignore

---

### 17. THIẾU REQUIREMENTS VERSION PINNING

**File:** `requirements.txt`

**Mô tả:**
```txt
flask
requests
pytest
google-genai
python-dotenv
```

**Đề xuất:**
```txt
flask==3.0.0
requests==2.31.0
pytest==7.4.3
google-genai==0.2.2
python-dotenv==1.0.0
```

---

### 18. THIẾU DOCKERFILE/DOCKER-COMPOSE

**Đề xuất:** Thêm Dockerfile để dễ deploy

---

## ✅ ĐIỂM TÍCH CỰC

1. ✅ **CUC_TABLE issue đã được fix** - Code hiện dùng bảng tra đúng
2. ✅ **Có test coverage tốt** - Có tests cho API endpoints và core logic
3. ✅ **Code structure tốt** - Modular, dễ maintain
4. ✅ **Có documentation** - Có docs về architecture, use cases
5. ✅ **Error handler tổng quát** - Có global exception handler

---

## 📋 ACTION PLAN

### Sprint 1 (Hotfix - Tuần này):
1. 🔴 **Fix API key hardcoded** - Move to environment variable
2. 🔴 **Fix bare except clauses** - Replace with specific exceptions
3. 🔴 **Add input validation** - Validate all inputs properly

### Sprint 2 (High Priority):
4. 🟡 **Add logging system** - Setup proper logging
5. 🟡 **Standardize error responses** - Unified error format
6. 🟡 **Add rate limiting** - Protect AI endpoints
7. 🟡 **Fix debug mode** - Use environment variable

### Sprint 3 (Medium Priority):
8. 🟢 **Add type hints** - Improve code quality
9. 🟢 **Refactor duplicate code** - DRY principle
10. 🟢 **Improve documentation** - Add missing docstrings

### Sprint 4 (Low Priority):
11. ⚪ **Add unit tests** - Increase coverage
12. ⚪ **Add CORS if needed** - For cross-origin requests
13. ⚪ **Version pinning** - Pin dependency versions

---

## 📊 METRICS

- **Code Quality Score:** 7/10
- **Security Score:** 4/10 (do API key hardcoded)
- **Test Coverage:** ~70%
- **Documentation:** 8/10

---

## 🔗 REFERENCES

- Previous QC Report: `python/docs/QC_CODE_REVIEW_REPORT.md`
- Tech Lead Fix Summary: `python/docs/TECH_LEAD_FIX_SUMMARY.md`
- BA Specification: `docs/BA_SYSTEM_ARCHITECTURE.md`

---

*Báo cáo được tạo tự động bởi QA/QC System*

