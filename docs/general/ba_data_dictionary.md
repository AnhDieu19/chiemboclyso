# TỬ VI NAM PHÁI - DATA DICTIONARY

## 📋 Mục Lục

1. [Thiên Can](#1-thiên-can)
2. [Địa Chi](#2-địa-chi)
3. [Ngũ Hành](#3-ngũ-hành)
4. [Ngũ Hành Cục](#4-ngũ-hành-cục)
5. [12 Cung](#5-12-cung)
6. [14 Chính Tinh](#6-14-chính-tinh)
7. [Lục Cát Tinh](#7-lục-cát-tinh)
8. [Lục Sát Tinh](#8-lục-sát-tinh)
9. [Vòng Trường Sinh](#9-vòng-trường-sinh)
10. [Vòng Bác Sỹ](#10-vòng-bác-sỹ)
11. [Vòng Thái Tuế](#11-vòng-thái-tuế)
12. [Tứ Hóa](#12-tứ-hóa)
13. [Độ Sáng Sao](#13-độ-sáng-sao)
14. [Các Sao Khác](#14-các-sao-khác)

---

## 1. THIÊN CAN (10 Can)

| Index | Can | Pinyin | Âm/Dương | Ngũ Hành | Hướng |
|-------|-----|--------|----------|----------|-------|
| 0 | Giáp | Jiǎ | Dương | Mộc | Đông |
| 1 | Ất | Yǐ | Âm | Mộc | Đông |
| 2 | Bính | Bǐng | Dương | Hỏa | Nam |
| 3 | Đinh | Dīng | Âm | Hỏa | Nam |
| 4 | Mậu | Wù | Dương | Thổ | Trung tâm |
| 5 | Kỷ | Jǐ | Âm | Thổ | Trung tâm |
| 6 | Canh | Gēng | Dương | Kim | Tây |
| 7 | Tân | Xīn | Âm | Kim | Tây |
| 8 | Nhâm | Rén | Dương | Thủy | Bắc |
| 9 | Quý | Guǐ | Âm | Thủy | Bắc |

### Mã Code

```python
THIEN_CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", 
             "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]

CAN_AM_DUONG = {
    "Giáp": "Dương", "Ất": "Âm",
    "Bính": "Dương", "Đinh": "Âm",
    "Mậu": "Dương", "Kỷ": "Âm",
    "Canh": "Dương", "Tân": "Âm",
    "Nhâm": "Dương", "Quý": "Âm"
}

CAN_NGU_HANH = {
    "Giáp": "Mộc", "Ất": "Mộc",
    "Bính": "Hỏa", "Đinh": "Hỏa",
    "Mậu": "Thổ", "Kỷ": "Thổ",
    "Canh": "Kim", "Tân": "Kim",
    "Nhâm": "Thủy", "Quý": "Thủy"
}
```

---

## 2. ĐỊA CHI (12 Chi)

| Index | Chi | Pinyin | Âm/Dương | Ngũ Hành | Con giáp | Giờ |
|-------|-----|--------|----------|----------|----------|-----|
| 0 | Tý | Zǐ | Dương | Thủy | Chuột | 23:00-01:00 |
| 1 | Sửu | Chǒu | Âm | Thổ | Trâu | 01:00-03:00 |
| 2 | Dần | Yín | Dương | Mộc | Hổ | 03:00-05:00 |
| 3 | Mão | Mǎo | Âm | Mộc | Mèo | 05:00-07:00 |
| 4 | Thìn | Chén | Dương | Thổ | Rồng | 07:00-09:00 |
| 5 | Tỵ | Sì | Âm | Hỏa | Rắn | 09:00-11:00 |
| 6 | Ngọ | Wǔ | Dương | Hỏa | Ngựa | 11:00-13:00 |
| 7 | Mùi | Wèi | Âm | Thổ | Dê | 13:00-15:00 |
| 8 | Thân | Shēn | Dương | Kim | Khỉ | 15:00-17:00 |
| 9 | Dậu | Yǒu | Âm | Kim | Gà | 17:00-19:00 |
| 10 | Tuất | Xū | Dương | Thổ | Chó | 19:00-21:00 |
| 11 | Hợi | Hài | Âm | Thủy | Lợn | 21:00-23:00 |

### Mã Code

```python
DIA_CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ",
           "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

GIO_SINH_RANGE = {
    0:  {"name": "Tý",   "range": "23:00 - 01:00"},
    1:  {"name": "Sửu",  "range": "01:00 - 03:00"},
    2:  {"name": "Dần",  "range": "03:00 - 05:00"},
    3:  {"name": "Mão",  "range": "05:00 - 07:00"},
    4:  {"name": "Thìn", "range": "07:00 - 09:00"},
    5:  {"name": "Tỵ",   "range": "09:00 - 11:00"},
    6:  {"name": "Ngọ",  "range": "11:00 - 13:00"},
    7:  {"name": "Mùi",  "range": "13:00 - 15:00"},
    8:  {"name": "Thân", "range": "15:00 - 17:00"},
    9:  {"name": "Dậu",  "range": "17:00 - 19:00"},
    10: {"name": "Tuất", "range": "19:00 - 21:00"},
    11: {"name": "Hợi",  "range": "21:00 - 23:00"}
}
```

---

## 3. NGŨ HÀNH

| Hành | Element | Màu sắc | Hướng | Mùa | Tạng |
|------|---------|---------|-------|-----|------|
| Kim | Metal | Trắng, Vàng kim | Tây | Thu | Phổi |
| Mộc | Wood | Xanh lá | Đông | Xuân | Gan |
| Thủy | Water | Đen, Xanh đen | Bắc | Đông | Thận |
| Hỏa | Fire | Đỏ, Tím | Nam | Hạ | Tim |
| Thổ | Earth | Vàng, Nâu | Trung tâm | Tứ quý | Lá lách |

### Quan Hệ Sinh Khắc

```
       TƯƠNG SINH (→)           TƯƠNG KHẮC (⊕)
       
    Kim → Thủy → Mộc           Kim ⊕ Mộc ⊕ Thổ
     ↑              ↓           ↑              ↓
    Thổ ←──── Hỏa ←┘           Hỏa ⊕ Kim ⊕ Mộc
                                       ↑
                               Thủy ⊕ Hỏa
                               Thổ ⊕ Thủy
```

---

## 4. NGŨ HÀNH CỤC

| Cục | Số | Ngũ Hành | Tuổi khởi vận |
|-----|----|---------| --------------|
| Thủy Nhị Cục | 2 | Thủy | 2 tuổi |
| Mộc Tam Cục | 3 | Mộc | 3 tuổi |
| Kim Tứ Cục | 4 | Kim | 4 tuổi |
| Thổ Ngũ Cục | 5 | Thổ | 5 tuổi |
| Hỏa Lục Cục | 6 | Hỏa | 6 tuổi |

### Bảng Tra Cục (Cục Table)

Tra theo **Can năm** và **Cung Mệnh**:

```python
CUC_TABLE = {
    # Can năm: {Cung Mệnh: Cục}
    "Giáp": {"Tý": 4, "Sửu": 4, "Dần": 2, "Mão": 2, "Thìn": 6, "Tỵ": 6,
             "Ngọ": 3, "Mùi": 3, "Thân": 5, "Dậu": 5, "Tuất": 4, "Hợi": 4},
    "Ất": {"Tý": 4, "Sửu": 4, "Dần": 2, "Mão": 2, "Thìn": 6, "Tỵ": 6,
           "Ngọ": 3, "Mùi": 3, "Thân": 5, "Dậu": 5, "Tuất": 4, "Hợi": 4},
    # ... (tiếp tục cho các Can khác)
}
```

---

## 5. 12 CUNG

| STT | Tên Cung | Ý nghĩa | Đại diện |
|-----|----------|---------|----------|
| 1 | Mệnh | Bản thân | Tính cách, ngoại hình, vận mệnh |
| 2 | Phụ Mẫu | Cha mẹ | Quan hệ với cha mẹ, học vấn |
| 3 | Phúc Đức | Phúc phần | Tâm linh, đạo đức, phúc họa |
| 4 | Điền Trạch | Nhà cửa | Bất động sản, gia đình |
| 5 | Quan Lộc | Sự nghiệp | Công việc, chức vụ |
| 6 | Nô Bộc | Bạn bè | Bạn bè, cấp dưới, đồng nghiệp |
| 7 | Thiên Di | Di chuyển | Du lịch, di cư, quý nhân ngoại |
| 8 | Tật Ách | Sức khỏe | Bệnh tật, tai nạn |
| 9 | Tài Bạch | Tài chính | Tiền bạc, thu nhập |
| 10 | Tử Tức | Con cái | Con cái, học trò |
| 11 | Phu Thê | Hôn nhân | Vợ/chồng, đối tác |
| 12 | Huynh Đệ | Anh em | Anh chị em, bạn thân |

### Tam Hợp / Lục Xung

```python
TAM_HOP = [
    ["Thân", "Tý", "Thìn"],   # Thủy Cục
    ["Dần", "Ngọ", "Tuất"],   # Hỏa Cục
    ["Tỵ", "Dậu", "Sửu"],     # Kim Cục
    ["Hợi", "Mão", "Mùi"]     # Mộc Cục
]

LUC_XUNG = [
    ("Tý", "Ngọ"),
    ("Sửu", "Mùi"),
    ("Dần", "Thân"),
    ("Mão", "Dậu"),
    ("Thìn", "Tuất"),
    ("Tỵ", "Hợi")
]
```

---

## 6. 14 CHÍNH TINH

### Nhóm Tử Vi (6 sao)

| STT | Tên | Ngũ Hành | Âm/Dương | Tính chất | Đặc điểm |
|-----|-----|----------|----------|-----------|----------|
| 1 | Tử Vi | Thổ | Âm | Cát | Đế tinh, quyền quý |
| 2 | Thiên Cơ | Mộc | Âm | Cát/Trung | Trí tuệ, mưu kế |
| 3 | Thái Dương | Hỏa | Dương | Cát | Quý nhân, bác ái |
| 4 | Vũ Khúc | Kim | Âm | Cát/Hung | Tài tinh, cương nghị |
| 5 | Thiên Đồng | Thủy | Dương | Cát | Phúc tinh, an nhàn |
| 6 | Liêm Trinh | Hỏa | Âm | Hung/Cát | Quan tinh, đào hoa |

### Nhóm Thiên Phủ (8 sao)

| STT | Tên | Ngũ Hành | Âm/Dương | Tính chất | Đặc điểm |
|-----|-----|----------|----------|-----------|----------|
| 7 | Thiên Phủ | Thổ | Dương | Cát | Tài khố, ổn định |
| 8 | Thái Âm | Thủy | Âm | Cát | Tài tinh, phú quý |
| 9 | Tham Lang | Thủy/Mộc | Dương | Hung/Cát | Đào hoa, ham muốn |
| 10 | Cự Môn | Thủy | Âm | Hung | Ám tinh, thị phi |
| 11 | Thiên Tướng | Thủy | Dương | Cát | Ấn tinh, phụ tá |
| 12 | Thiên Lương | Thổ | Dương | Cát | Ấm tinh, che chở |
| 13 | Thất Sát | Kim | Dương | Hung | Sát tinh, quyết đoán |
| 14 | Phá Quân | Thủy | Âm | Hung | Hao tinh, phá cách |

### Vị Trí An Sao

```python
# Nhóm Tử Vi (từ Tử Vi đếm nghịch)
TU_VI_GROUP_OFFSETS = {
    "Tử Vi": 0,
    "Thiên Cơ": -1,
    "Thái Dương": -3,
    "Vũ Khúc": -4,
    "Thiên Đồng": -5,
    "Liêm Trinh": 4
}

# Nhóm Thiên Phủ (từ Thiên Phủ đếm thuận)
THIEN_PHU_GROUP_OFFSETS = {
    "Thiên Phủ": 0,
    "Thái Âm": 1,
    "Tham Lang": 2,
    "Cự Môn": 3,
    "Thiên Tướng": 4,
    "Thiên Lương": 5,
    "Thất Sát": 6,
    "Phá Quân": 10
}
```

---

## 7. LỤC CÁT TINH (6 sao may)

| STT | Tên | Ngũ Hành | Cách an | Ý nghĩa |
|-----|-----|----------|---------|---------|
| 1 | Tả Phù | Thổ | Theo tháng, từ Thìn thuận | Trợ lý, phụ tá |
| 2 | Hữu Bật | Thủy | Theo tháng, từ Tuất nghịch | Trợ lý, phụ tá |
| 3 | Văn Xương | Kim | Theo giờ, từ Tuất nghịch | Học vấn, văn chương |
| 4 | Văn Khúc | Thủy | Theo giờ, từ Thìn thuận | Tài năng, nghệ thuật |
| 5 | Thiên Khôi | Hỏa | Theo Can năm | Quý nhân, may mắn |
| 6 | Thiên Việt | Hỏa | Theo Can năm | Quý nhân, may mắn |

### Bảng Tra Thiên Khôi/Thiên Việt

```python
THIEN_KHOI_POSITION = {
    "Giáp": "Sửu", "Mậu": "Sửu", "Canh": "Sửu",
    "Ất": "Tý",   "Kỷ": "Tý",
    "Bính": "Hợi", "Đinh": "Hợi",
    "Nhâm": "Mão", "Quý": "Mão",
    "Tân": "Ngọ"
}

THIEN_VIET_POSITION = {
    "Giáp": "Mùi", "Mậu": "Mùi", "Canh": "Mùi",
    "Ất": "Thân", "Kỷ": "Thân",
    "Bính": "Dậu", "Đinh": "Dậu",
    "Nhâm": "Tỵ",  "Quý": "Tỵ",
    "Tân": "Dần"
}
```

---

## 8. LỤC SÁT TINH (6 sao hung)

| STT | Tên | Ngũ Hành | Cách an | Ý nghĩa |
|-----|-----|----------|---------|---------|
| 1 | Kình Dương | Kim | Lộc Tồn + 1 | Hung tinh, tranh đấu |
| 2 | Đà La | Kim | Lộc Tồn - 1 | Hung tinh, cản trở |
| 3 | Hỏa Tinh | Hỏa | Theo Chi năm + giờ | Nóng nảy, bùng nổ |
| 4 | Linh Tinh | Hỏa | Theo Chi năm + giờ | Nóng nảy, thất thường |
| 5 | Địa Không | Hỏa | Theo giờ, từ Hợi thuận | Trống rỗng, mất mát |
| 6 | Địa Kiếp | Hỏa | Theo giờ, từ Hợi nghịch | Cướp đoạt, tai họa |

### Bảng Tra Lộc Tồn (cơ sở để an Kình Dương, Đà La)

```python
LOC_TON_POSITION = {
    "Giáp": "Dần",
    "Ất": "Mão",
    "Bính": "Tỵ",
    "Đinh": "Ngọ",
    "Mậu": "Tỵ",
    "Kỷ": "Ngọ",
    "Canh": "Thân",
    "Tân": "Dậu",
    "Nhâm": "Hợi",
    "Quý": "Tý"
}
```

---

## 9. VÒNG TRƯỜNG SINH (12 sao)

| STT | Tên | Ý nghĩa | Tốt/Xấu |
|-----|-----|---------|---------|
| 1 | Trường Sinh | Sinh sôi, khởi đầu | Tốt |
| 2 | Mộc Dục | Tắm gội, thanh lọc | Xấu |
| 3 | Quan Đới | Đội mũ, thăng tiến | Tốt |
| 4 | Lâm Quan | Ra làm quan | Tốt |
| 5 | Đế Vượng | Vua, cực thịnh | Tốt |
| 6 | Suy | Suy yếu | Xấu |
| 7 | Bệnh | Ốm đau | Xấu |
| 8 | Tử | Chết | Xấu |
| 9 | Mộ | Mai táng | Xấu |
| 10 | Tuyệt | Tuyệt diệt | Xấu |
| 11 | Thai | Mang thai | Trung bình |
| 12 | Dưỡng | Nuôi dưỡng | Trung bình |

### Vị Trí Khởi Trường Sinh

```python
TRUONG_SINH_START = {
    # Cục: {Âm Dương: vị trí khởi}
    2: {"Dương": "Thân", "Âm": "Mão"},   # Thủy Cục
    3: {"Dương": "Hợi", "Âm": "Ngọ"},    # Mộc Cục
    4: {"Dương": "Tỵ", "Âm": "Tý"},      # Kim Cục
    5: {"Dương": "Thân", "Âm": "Mão"},   # Thổ Cục
    6: {"Dương": "Dần", "Âm": "Dậu"}     # Hỏa Cục
}
```

---

## 10. VÒNG BÁC SỸ (12 sao)

| STT | Tên | Tốt/Xấu | Ý nghĩa |
|-----|-----|---------|---------|
| 1 | Bác Sỹ | Tốt | Học vấn, chuyên môn |
| 2 | Lực Sỹ | Tốt | Sức mạnh, quyền uy |
| 3 | Thanh Long | Tốt | May mắn, quý nhân |
| 4 | Tiểu Hao | Xấu | Hao tổn nhỏ |
| 5 | Tướng Quân | Tốt | Quyền lực, lãnh đạo |
| 6 | Tấu Thư | Tốt | Văn thư, thăng tiến |
| 7 | Phi Liêm | Xấu | Thị phi, kiện tụng |
| 8 | Hỉ Thần | Tốt | Vui vẻ, hỉ khánh |
| 9 | Bệnh Phù | Xấu | Bệnh tật |
| 10 | Đại Hao | Xấu | Hao tổn lớn |
| 11 | Phục Binh | Xấu | Tiểu nhân, ẩn họa |
| 12 | Quan Phù | Xấu | Kiện tụng, quan phi |

---

## 11. VÒNG THÁI TUẾ (12 sao)

| STT | Tên | Tốt/Xấu | Ý nghĩa |
|-----|-----|---------|---------|
| 1 | Thái Tuế | Trung | Năm tuổi, chủ đạo |
| 2 | Thiếu Dương | Tốt | Quý nhân nam |
| 3 | Tang Môn | Xấu | Tang chế, buồn |
| 4 | Thiếu Âm | Tốt | Quý nhân nữ |
| 5 | Quan Phù | Xấu | Kiện tụng |
| 6 | Tử Phù | Xấu | Bệnh tật, chết chóc |
| 7 | Tuế Phá | Xấu | Phá tài, phá hoại |
| 8 | Long Đức | Tốt | May mắn, quý nhân |
| 9 | Bạch Hổ | Xấu | Tai nạn, máu |
| 10 | Phúc Đức | Tốt | Phúc lộc |
| 11 | Điếu Khách | Xấu | Tang, chia ly |
| 12 | Trực Phù | Trung | Trung tính |

### Bộ Ba Thái Tuế (Tuế - Hổ - Phù)
*   **Thái Tuế**: Lý trí, bảo thủ, lãnh đạo.
*   **Bạch Hổ**: Ngang ngược, máu lạnh, chiến đấu.
*   **Quan Phù**: Thù dai, kiện tụng.
> "Thuận Thái Tuế thì sống, chống Thái Tuế thì chết."

### So Sánh Tuế - Phá
*   **Thái Tuế (Vòng Nhân)**: Lý trí, hiên ngang, dứt khoát.
*   **Tuế Phá (Vòng Đối Nghịch)**: Cảm xúc, lo âu, lụy tình.

---

## 12. TỨ HÓA

### Bảng Tứ Hóa Nam Phái

| Can | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|-----|---------|-----------|----------|--------|
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

### Ý Nghĩa Tứ Hóa

```python
TU_HOA_MEANING = {
    "Lộc": {
        "keyword": "Tài lộc",
        "meaning": "May mắn, thuận lợi, cơ hội tốt",
        "color": "#4CAF50"  # Xanh lá
    },
    "Quyền": {
        "keyword": "Quyền lực",
        "meaning": "Kiểm soát, thăng tiến, chủ động",
        "color": "#F44336"  # Đỏ
    },
    "Khoa": {
        "keyword": "Danh tiếng",
        "meaning": "Học vấn, uy tín, vinh dự",
        "color": "#9C27B0"  # Tím
    },
    "Kỵ": {
        "keyword": "Trở ngại",
        "meaning": "Khó khăn, cản trở, cần cẩn thận",
        "color": "#212121"  # Đen
    }
}
```

---

## 13. ĐỘ SÁNG SAO

| Độ sáng | Ý nghĩa | Sức mạnh | Màu hiển thị |
|---------|---------|----------|--------------|
| Miếu | Cực tốt, phát huy tối đa | 100% | **Bold + Vàng** |
| Vượng | Rất tốt, sức mạnh mạnh | 80% | **Bold** |
| Đắc | Tốt, có lợi ích | 60% | Normal |
| Bình | Trung bình, không tốt không xấu | 40% | Normal + Nhạt |
| Hãm | Xấu, yếu đuối, bất lợi | 20% | Mờ + Nghiêng |

### Bảng Tra Độ Sáng (Ví dụ: Tử Vi)

```python
TU_VI_BRIGHTNESS = {
    "Tý": "Miếu",
    "Sửu": "Miếu",
    "Dần": "Vượng",
    "Mão": "Đắc",
    "Thìn": "Vượng",
    "Tỵ": "Đắc",
    "Ngọ": "Miếu",
    "Mùi": "Miếu",
    "Thân": "Vượng",
    "Dậu": "Đắc",
    "Tuất": "Vượng",
    "Hợi": "Đắc"
}
```

---

## 14. CÁC SAO KHÁC

### Sao Theo Năm

| Sao | Cách an | Ý nghĩa |
|-----|---------|---------|
| Thiên Mã | Theo Chi năm | Di chuyển, đi xa |
| Thiên Hình | Theo Chi năm | Hình phạt, pháp luật |
| Thiên Riêu | Theo Chi năm | Đào hoa, tà dâm |
| Thiên Hỉ | Theo Chi năm | Vui vẻ, hỉ khánh |
| Hồng Loan | Theo Chi năm | Đào hoa chính, hôn nhân |
| Thiên Khốc | Theo Chi năm | Khóc lóc, buồn |
| Thiên Hư | Theo Chi năm | Hư hao, mất mát |

### Sao Theo Tháng

| Sao | Cách an | Ý nghĩa |
|-----|---------|---------|
| Thiên Đức | Theo tháng | Phúc đức, may mắn |
| Nguyệt Đức | Theo tháng | Phúc đức, quý nhân |

### Sao Theo Ngày

| Sao | Cách an | Ý nghĩa |
|-----|---------|---------|
| Tam Thai | Theo ngày | Học vấn |
| Bát Tọa | Theo ngày | Địa vị |
| Ân Quang | Theo ngày | Ân đức |
| Thiên Quý | Theo ngày | Quý nhân |

---

## 15. DỮ LIỆU NHÂN TƯỚNG (Physiognomy)

Hệ thống bổ sung dữ liệu nhận diện tướng mạo con người song song với lá số:

### 1. Diện Tướng (Gương Mặt)
*   **Mắt**: Thần thái, độ sáng, hình dáng (lá dăm, ướt...).
*   **Tai**: Độ dày, thành quách, rái tai (Phật).
*   **Miệng/Răng**: Độ đều, màu môi, hình dáng răng.
*   **Trán**: Độ cao, rộng, gân trán.
*   **Mũi**: Tài khố, độ cao, hình dáng lỗ mũi.

### 2. Thủ Tướng (Bàn Tay)
*   **Hình dáng**: Độ dày, khe hở ngón tay.
*   **Chỉ tay**: Sinh đạo, Thái dương.
*   **Ý nghĩa ngón đeo nhẫn**:
    *   Ngón Cái: Cha.
    *   Ngón Trỏ: Mẹ.
    *   Ngón Giữa: Bản thân.
    *   Ngón Áp Út: Hôn nhân.
    *   Ngón Út: Bạn bè.

### 3. Dâm Tướng (Nhu Cầu Sinh Lý)
*   Nhận diện qua: Mắt (ướt, lá khoai), Nốt ruồi (quanh miệng, ngực), Dáng đi, Giọng nói.

---

## 📊 TỔNG HỢP SỐ LƯỢNG SAO

| Loại | Số lượng | Ghi chú |
|------|----------|---------|
| Chính Tinh | 14 | Tử Vi + Thiên Phủ group |
| Lục Cát + Lộc Tồn | 7 | Tả Phù, Hữu Bật, Văn Xương, Văn Khúc, Thiên Khôi, Thiên Việt, Lộc Tồn |
| Lục Sát | 6 | Kình Dương, Đà La, Hỏa Tinh, Linh Tinh, Địa Không, Địa Kiếp |
| Vòng Trường Sinh | 12 | Trường Sinh → Dưỡng |
| Vòng Bác Sỹ | 12 | Bác Sỹ → Quan Phù |
| Vòng Thái Tuế | 12 | Thái Tuế → Trực Phù |
| Sao Other | 27 | Thiên Mã, Hồng Loan, Đào Hoa, Thiên La, Địa Võng... |
| Sao Tuần Triệt + Phụ | 23 | Tuần, Triệt, Cô Thần, Quả Tú, Thai Phụ, Phong Các... |
| **Sao Bổ Sung** | **11** | Long Trì, Phượng Các, Thiên Riêu, Thiên Không, Đẩu Quân... |
| **TỔNG CỘNG** | **~117** | ✅ Đạt yêu cầu >= 114 sao |

### Danh Sách Sao Bổ Sung (11 sao mới)

| # | Tên Sao | Theo | Ý nghĩa |
|---|---------|------|---------|
| 1 | Long Trì | Chi năm | Văn chương, thi cử |
| 2 | Phượng Các | Chi năm | Nghệ thuật, tài hoa |
| 3 | Thiên Riêu | Chi năm | Đào hoa phụ |
| 4 | Thiên Không | Giờ | Tư tưởng, triết lý |
| 5 | Đẩu Quân | Giờ + Tháng | Mưu lược, quân sự |
| 6 | Hóa Cái | Chi năm | Nghệ thuật |
| 7 | Thiên Đào | Chi năm | Đào hoa |
| 8 | Thiên Thanh | Chi năm | Thanh cao |
| 9 | Thiên Trụ | Giờ | Cát tinh hỗ trợ |
| 10 | Thiên Trì | Giờ | Cát tinh hỗ trợ |
| 11 | Hàm Trì | Chi năm | Đào hoa phụ |

### Mệnh Chủ và Thân Chủ

| Cung Mệnh | Mệnh Chủ | Chi Năm | Thân Chủ |
|-----------|----------|---------|----------|
| Tý | Tham Lang | Tý | Linh Tinh |
| Sửu | Cự Môn | Sửu | Thiên Tướng |
| Dần | Lộc Tồn | Dần | Thiên Lương |
| Mão | Văn Khúc | Mão | Thiên Đồng |
| Thìn | Liêm Trinh | Thìn | Văn Xương |
| Tỵ | Vũ Khúc | Tỵ | Thiên Cơ |
| Ngọ | Phá Quân | Ngọ | Hỏa Tinh |
| Mùi | Vũ Khúc | Mùi | Thiên Tướng |
| Thân | Liêm Trinh | Thân | Thiên Lương |
| Dậu | Văn Khúc | Dậu | Thiên Đồng |
| Tuất | Lộc Tồn | Tuất | Văn Xương |
| Hợi | Cự Môn | Hợi | Thiên Cơ |

---

*Data Dictionary - Phien ban 1.2 (Cap nhat 20/12/2025)*

---

## 16. DU LIEU FINDER API

### Request Payload

```python
FinderRequest = {
    "year": int,           # Nam sinh (1900-2100)
    "month": int,          # Thang am lich (1-12)
    "day": int,            # Ngay am lich (1-30)
    "gender": str,         # "nam" | "nu"
    "calendar_type": str,  # "lunar" | "solar"
    "known_hour": str,     # "-1" = chua biet, "0"-"11" = gio cu the
    "traits": list,        # Danh sach dac diem ["Thong minh", "Dao hoa", ...]
    "events": list         # Danh sach su kien [{"type": "Ket hon", "year": 2022}]
}
```

### Response Payload

```python
FinderResponse = {
    "success": bool,       # True neu thanh cong
    "status": str,         # "success" | "error"
    "total": int,          # Tong so ung vien
    "candidates": list,    # Top 3 ung vien (sorted by score)
    "all_candidates": list,# Tat ca ung vien
    "top_timeline": list   # Du lieu timeline cho ung vien hang dau
}

Candidate = {
    "date": {
        "day": int,
        "month": int,
        "year": int,
        "hour": int        # 0-11 (Ty - Hoi)
    },
    "gender": str,
    "chart_summary": {
        "menh_at": str,    # Chi cung Menh (e.g. "Ty")
        "menh_chinh_tinh": list  # Danh sach chinh tinh tai cung Menh
    },
    "match_info": {
        "score": float,    # Diem khop (0-100+)
        "details": dict    # Chi tiet ly do khop
    },
    "success_info": {
        "score": float,    # Diem thanh cong (0-100)
        "rank_class": str, # "S", "A", "B", "C"
        "archetype": str   # "So Ty Phu", "Kha Gia", ...
    }
}
```
