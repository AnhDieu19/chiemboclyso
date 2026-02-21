# 📊 BA DOCUMENT: PHÂN LOẠI HỒNG NHAN 5 CẤP ĐỘ VÀ XÁC SUẤT

**Mã tính năng:** FEAT-HONG-NHAN-001  
**Ngày tạo:** 22/12/2025  
**Phiên bản:** 1.0  
**Tác giả:** BA Team  
**Trạng thái:** Ready for Development

---

## 1. 📋 TỔNG QUAN

### 1.1 Mô tả tính năng
Phân loại **Hồng Nhan** thành **5 cấp độ** từ rất tốt xuống rất xấu, với:
- **Legend rõ ràng** trong biểu đồ
- **Tính xác suất** cho mỗi loại
- **Filter** để tính xác suất theo điều kiện

### 1.2 Mục tiêu
- Thay thế tên tiếng Anh (VERY_HAPPY, HAPPY...) bằng tên tiếng Việt có ý nghĩa
- Hiển thị xác suất % cho mỗi cấp độ
- Cho phép filter theo năm, bộ sao, giới tính

---

## 2. 🎯 5 CẤP ĐỘ HỒNG NHAN

### 2.1 Mapping từ cũ sang mới

| Level | Tên cũ (Code) | Tên mới (Tiếng Việt) | Mô tả | Màu sắc | Icon |
|-------|---------------|---------------------|-------|---------|------|
| 1 | VERY_HAPPY | **Hồng Nhan Phú Quý** | Rất may mắn, phú quý, hạnh phúc | #4caf50 (Xanh lá) | 👑 |
| 2 | HAPPY | **Hồng Nhan Hạnh Phúc** | May mắn, tình duyên thuận lợi | #8bc34a (Xanh lá nhạt) | 🌸 |
| 3 | NEUTRAL | **Hồng Nhan Bình Thường** | Có lúc vui lúc buồn, đời sống bình thường | #ffeb3b (Vàng) | ⚖️ |
| 4 | TRAGIC | **Hồng Nhan Vất Vả** | Gặp nhiều trắc trở, tình duyên không trọn vẹn | #ff9800 (Cam) | 😔 |
| 5 | VERY_TRAGIC | **Hồng Nhan Bạc Mệnh** | Bạc mệnh, đời lắm gian truân | #f44336 (Đỏ) | 💔 |

### 2.2 Điều kiện phân loại

**Dựa trên `beauty_engine.py` - `classify_beauty_fortune()`:**

| Level | Score Range | Điều kiện |
|-------|-------------|-----------|
| 1 | 8.0 - 10.0 | Lộc Tồn/Hóa Lộc + Quý nhân + Hạnh phúc hôn nhân |
| 2 | 6.5 - 8.0 | Nhiều yếu tố tốt, ít yếu tố xấu |
| 3 | 5.0 - 6.5 | Yếu tố hỗn hợp, cân bằng |
| 4 | 3.0 - 5.0 | Một số yếu tố xấu (Sát tinh, Cô Quả) |
| 5 | 0.0 - 3.0 | Nhiều sát tinh, Cô Thần Quả Tú, Hóa Kỵ |

---

## 3. 📊 TÍNH XÁC SUẤT

### 3.1 Công thức

**Xác suất cơ bản:**
```
P(Level_i) = Số lượng Level_i / Tổng số Hồng Nhan
```

**Xác suất có điều kiện (Filter):**
```
P(Level_i | Filter) = Số lượng Level_i thỏa Filter / Tổng số Hồng Nhan thỏa Filter
```

### 3.2 Ví dụ

**Từ dữ liệu hiện có:**
- Tổng: 3699 Hồng Nhan
- Level 1 (VERY_HAPPY): 155 → **4.2%**
- Level 2 (HAPPY): 949 → **25.7%**
- Level 3 (NEUTRAL): 1197 → **32.4%**
- Level 4 (TRAGIC): 872 → **23.6%**
- Level 5 (VERY_TRAGIC): 526 → **14.2%**

**Với filter "DAO_HONG":**
- Tổng: 2866
- Level 1: 79 → **2.8%**
- Level 2: 599 → **20.9%**
- ...

---

## 4. 🎨 UI/UX SPECIFICATIONS

### 4.1 Legend Component

**Vị trí:** Phía trên hoặc bên cạnh biểu đồ

**Design:**
```
┌─────────────────────────────────────────────────────────┐
│  📊 LEGEND - 5 CẤP ĐỘ HỒNG NHAN                        │
├─────────────────────────────────────────────────────────┤
│  👑 Hồng Nhan Phú Quý        (4.2%)  ████              │
│  🌸 Hồng Nhan Hạnh Phúc      (25.7%) ████████████      │
│  ⚖️  Hồng Nhan Bình Thường   (32.4%) ████████████████  │
│  😔 Hồng Nhan Vất Vả         (23.6%) ███████████       │
│  💔 Hồng Nhan Bạc Mệnh        (14.2%) ███████          │
└─────────────────────────────────────────────────────────┘
```

**Màu sắc:**
- Level 1: `#4caf50` (Xanh lá đậm)
- Level 2: `#8bc34a` (Xanh lá nhạt)
- Level 3: `#ffeb3b` (Vàng)
- Level 4: `#ff9800` (Cam)
- Level 5: `#f44336` (Đỏ)

### 4.2 Filter Panel

**Vị trí:** Phía trên biểu đồ

**Controls:**
- **Năm:** Dropdown (1950-2007) hoặc Range slider
- **Bộ Sao:** Multi-select (DAO_HONG, VAN_TINH, QUYEN_RU, PHUC_THIEN)
- **Giới tính:** Radio (Nam/Nữ/Tất cả)
- **Nút "Áp dụng Filter"**

**Kết quả sau filter:**
- Hiển thị: "Đang xem: 2866 mẫu (DAO_HONG)"
- Cập nhật xác suất theo filter

---

## 5. 📋 TASK CHO DEV

### TASK-DEV-HN-01: Cập nhật HTML Report
**Priority:** HIGH  
**Estimated:** 2 giờ

- [ ] Thêm mapping 5 cấp độ (tên mới, icon, màu)
- [ ] Thêm Legend component
- [ ] Tính và hiển thị xác suất % cho mỗi level
- [ ] Cập nhật labels trong Chart.js

### TASK-DEV-HN-02: Thêm Filter Functionality
**Priority:** MEDIUM  
**Estimated:** 3 giờ

- [ ] Tạo Filter Panel UI
- [ ] Implement filter logic (năm, bộ sao, giới tính)
- [ ] Cập nhật biểu đồ khi filter thay đổi
- [ ] Hiển thị số mẫu sau filter

### TASK-DEV-HN-03: Tính xác suất động
**Priority:** HIGH  
**Estimated:** 2 giờ

- [ ] Function tính xác suất cơ bản
- [ ] Function tính xác suất có điều kiện (filter)
- [ ] Format % (2 chữ số thập phân)
- [ ] Update legend khi filter thay đổi

---

## 6. 🧪 TASK CHO QC

### TASK-QC-HN-01: Verify 5 Levels
**Priority:** HIGH  
**Estimated:** 1 giờ

- [ ] Verify mapping đúng 5 cấp độ
- [ ] Verify màu sắc và icon
- [ ] Verify tên tiếng Việt hiển thị đúng

### TASK-QC-HN-02: Verify Xác suất
**Priority:** HIGH  
**Estimated:** 1 giờ

**Test cases:**

| # | Filter | Expected Total | Level 1 % | Verify |
|---|--------|----------------|-----------|--------|
| 1 | Không filter | 3699 | 4.2% | [ ] |
| 2 | DAO_HONG | 2866 | 2.8% | [ ] |
| 3 | VAN_TINH | 1002 | 12.9% | [ ] |
| 4 | Năm 2000 | 4118 | ? | [ ] |

### TASK-QC-HN-03: Verify Filter
**Priority:** MEDIUM  
**Estimated:** 1 giờ

- [ ] Filter theo năm hoạt động đúng
- [ ] Filter theo bộ sao hoạt động đúng
- [ ] Multiple filters kết hợp đúng
- [ ] Reset filter hoạt động đúng

---

## 7. 📊 DATA STRUCTURE

### 7.1 Input Data Format

```json
{
  "total": 3699,
  "levels": {
    "VERY_HAPPY": 155,
    "HAPPY": 949,
    "NEUTRAL": 1197,
    "TRAGIC": 872,
    "VERY_TRAGIC": 526
  },
  "by_set": {
    "DAO_HONG": {
      "VERY_HAPPY": 79,
      "HAPPY": 599,
      "NEUTRAL": 906,
      "TRAGIC": 759,
      "VERY_TRAGIC": 523
    },
    ...
  },
  "by_year": {
    "2000": {
      "VERY_HAPPY": 20,
      "HAPPY": 120,
      ...
    },
    ...
  }
}
```

### 7.2 Output Format

```json
{
  "filtered_total": 2866,
  "levels": [
    {
      "level": 1,
      "name": "Hồng Nhan Phú Quý",
      "name_en": "VERY_HAPPY",
      "count": 79,
      "percentage": 2.76,
      "color": "#4caf50",
      "icon": "👑"
    },
    ...
  ],
  "probabilities": {
    "VERY_HAPPY": 2.76,
    "HAPPY": 20.88,
    "NEUTRAL": 31.58,
    "TRAGIC": 26.48,
    "VERY_TRAGIC": 18.25
  }
}
```

---

## 8. ✅ ACCEPTANCE CRITERIA

1. ✅ 5 cấp độ hiển thị với tên tiếng Việt
2. ✅ Legend hiển thị đầy đủ icon, tên, màu, %
3. ✅ Xác suất tính đúng (tổng = 100%)
4. ✅ Filter hoạt động và cập nhật xác suất
5. ✅ Biểu đồ cập nhật khi filter thay đổi
6. ✅ Responsive trên mobile

---

*Tài liệu BA tạo: 22/12/2025*  
*Người tạo: BA Team*



