# 🛠️ HƯỚNG DẪN IMPLEMENTATION - HỒNG NHAN 5 CẤP ĐỘ

**Dành cho:** Dev Team  
**Thời gian dự kiến:** 3-4 giờ  
**Tham khảo:** BA_HONG_NHAN_5_LEVELS.md

---

## ✅ ĐÃ HOÀN THÀNH

File `beauty_report.html` đã được cập nhật với:
- ✅ 5 cấp độ với tên tiếng Việt
- ✅ Legend component với xác suất
- ✅ Filter panel (Bộ Sao, Năm)
- ✅ Tính xác suất động

---

## 📋 CHECKLIST VERIFICATION

### 1. Verify 5 Cấp Độ

Mở `beauty_report.html` và kiểm tra:

- [ ] Legend hiển thị 5 cấp độ:
  - 👑 Hồng Nhan Phú Quý
  - 🌸 Hồng Nhan Hạnh Phúc
  - ⚖️ Hồng Nhan Bình Thường
  - 😔 Hồng Nhan Vất Vả
  - 💔 Hồng Nhan Bạc Mệnh

- [ ] Màu sắc đúng:
  - Level 1: #4caf50 (Xanh lá)
  - Level 2: #8bc34a (Xanh lá nhạt)
  - Level 3: #ffeb3b (Vàng)
  - Level 4: #ff9800 (Cam)
  - Level 5: #f44336 (Đỏ)

### 2. Verify Xác Suất

- [ ] Legend hiển thị số mẫu và %
- [ ] Tổng % = 100% (hoặc gần 100% do làm tròn)
- [ ] Xác suất cập nhật khi filter thay đổi

**Test:**
```javascript
// Mở Console và chạy:
const data = getFilteredData();
const { probabilities } = calculateProbabilities(data);
console.log(probabilities);
// Tổng phải ≈ 100
```

### 3. Verify Filter

- [ ] Filter "Bộ Sao" hoạt động
- [ ] Filter "Năm" hoạt động (nếu có data)
- [ ] Nút "Áp dụng" cập nhật biểu đồ
- [ ] Nút "Reset" trở về mặc định
- [ ] Filter info hiển thị số mẫu sau filter

---

## 🔧 CẦN BỔ SUNG (Nếu có)

### 1. Thêm Data theo Năm

Nếu có data chi tiết theo năm, cập nhật:

```javascript
// Thêm vào RAW_DATA
RAW_DATA.by_year = {
    "2000": {
        VERY_HAPPY: 20,
        HAPPY: 120,
        NEUTRAL: 150,
        TRAGIC: 80,
        VERY_TRAGIC: 50,
        total: 420
    },
    // ... các năm khác
};

// Cập nhật getFilteredData()
function getFilteredData() {
    // ... existing code ...
    
    if (currentFilter.year !== 'all') {
        const yearData = RAW_DATA.by_year[currentFilter.year];
        if (yearData) {
            data.levels = { ...yearData };
            delete data.levels.total;
            data.total = yearData.total;
        }
    }
    
    return data;
}
```

### 2. Thêm Filter Giới Tính

Nếu có data theo giới tính:

```html
<div class="filter-group">
    <label>Giới tính:</label>
    <select id="filter-gender">
        <option value="all">Tất cả</option>
        <option value="nam">Nam</option>
        <option value="nu">Nữ</option>
    </select>
</div>
```

```javascript
// Thêm vào currentFilter
currentFilter.gender = document.getElementById('filter-gender').value;

// Cập nhật getFilteredData() để filter theo gender
```

### 3. Export Data

Thêm nút export:

```html
<button class="btn btn-secondary" onclick="exportData()">📥 Export CSV</button>
```

```javascript
function exportData() {
    const data = getFilteredData();
    const { probabilities } = calculateProbabilities(data);
    
    let csv = "Cấp Độ,Số Mẫu,Xác Suất (%)\n";
    Object.keys(HONG_NHAN_LEVELS).forEach(key => {
        const level = HONG_NHAN_LEVELS[key];
        const count = data.levels[key] || 0;
        const pct = probabilities[key] || 0;
        csv += `${level.name},${count},${pct.toFixed(2)}\n`;
    });
    
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'hong_nhan_stats.csv';
    a.click();
}
```

---

## 🧪 TEST CASES

### Test 1: Xác Suất Cơ Bản

**Input:** Không filter  
**Expected:**
- Level 1: 155/3699 = 4.19%
- Level 2: 949/3699 = 25.66%
- Level 3: 1197/3699 = 32.36%
- Level 4: 872/3699 = 23.57%
- Level 5: 526/3699 = 14.22%
- **Tổng: 100%**

### Test 2: Filter DAO_HONG

**Input:** Filter = DAO_HONG  
**Expected:**
- Total: 2866
- Level 1: 79/2866 = 2.76%
- Level 2: 599/2866 = 20.88%
- Level 3: 906/2866 = 31.58%
- Level 4: 759/2866 = 26.48%
- Level 5: 523/2866 = 18.25%
- **Tổng: 100%**

### Test 3: Filter VAN_TINH

**Input:** Filter = VAN_TINH  
**Expected:**
- Total: 1002
- Level 1: 129/1002 = 12.87%
- Level 2: 393/1002 = 39.22%
- Level 3: 313/1002 = 31.24%
- Level 4: 157/1002 = 15.67%
- Level 5: 10/1002 = 1.00%
- **Tổng: 100%**

---

## 🐛 DEBUGGING

### Vấn đề: Xác suất không đúng

**Kiểm tra:**
```javascript
// Console
const data = getFilteredData();
console.log('Data:', data);
const { total, probabilities } = calculateProbabilities(data);
console.log('Total:', total);
console.log('Probabilities:', probabilities);

// Verify tổng
const sum = Object.values(probabilities).reduce((a, b) => a + b, 0);
console.log('Sum:', sum); // Phải ≈ 100
```

### Vấn đề: Filter không hoạt động

**Kiểm tra:**
```javascript
// Console
console.log('Current filter:', currentFilter);
const filtered = getFilteredData();
console.log('Filtered data:', filtered);
```

### Vấn đề: Chart không cập nhật

**Kiểm tra:**
- Chart instance có được destroy trước khi tạo mới không?
- Data có đúng format không?
- Console có lỗi JavaScript không?

---

## 📊 PERFORMANCE

**Optimization tips:**
- Cache chart instances nếu không cần destroy
- Debounce filter changes nếu có nhiều filter
- Lazy load data theo năm nếu dataset lớn

---

## ✅ FINAL CHECKLIST

- [ ] 5 cấp độ hiển thị đúng tên tiếng Việt
- [ ] Legend hiển thị icon, màu, số mẫu, %
- [ ] Xác suất tính đúng (tổng ≈ 100%)
- [ ] Filter hoạt động và cập nhật chart
- [ ] Responsive trên mobile
- [ ] Không có lỗi console
- [ ] Tooltip hiển thị đầy đủ thông tin

---

*Guide created: 22/12/2025*



