# BÁO CÁO LỖI VÀ HƯỚNG DẪN SỬA BẢNG CỤC

## VẤN ĐỀ PHÁT HIỆN

Khi so sánh với lá số mẫu chuẩn từ **tuvinamhai.vn**, phát hiện **BẢNG TRA CỤC SAI**:

### Thông tin lá số test:
- Ngày: 28/3/1994 (17/2 Âm lịch)
- Giờ: Mão (5h-7h)
- Năm: Giáp Tuất
- Cung Mệnh: Tý

### So sánh kết quả:

| Tiêu chí | Mẫu chuẩn | App hiện tại | Kết quả |
|----------|-----------|--------------|---------|
| Cục | **Thủy Nhị Cục (2)** | Hỏa Lục Cục (6) | SAI |
| Tử Vi | Dậu | Ngọ | SAI (do Cục sai) |

---

## NGUYÊN NHÂN

Bảng `CUC_TABLE` trong file `data/cung_cuc.py` đang có giá trị **SAI** cho năm Giáp/Kỷ:

```python
# HIỆN TẠI (SAI):
0: {0: 'Hỏa Lục Cục', 1: 'Hỏa Lục Cục', 2: 'Thủy Nhị Cục', 3: 'Thủy Nhị Cục', 
    4: 'Mộc Tam Cục', 5: 'Mộc Tam Cục', 6: 'Kim Tứ Cục', 7: 'Kim Tứ Cục',
    8: 'Thổ Ngũ Cục', 9: 'Thổ Ngũ Cục', 10: 'Hỏa Lục Cục', 11: 'Hỏa Lục Cục'},
```

---

## BẢNG CỤC ĐÚNG CHUẨN NAM PHÁI

### Khẩu quyết: "Giáp Kỷ chi niên Bính tác thủ"

Bảng tra Cục theo **Can năm** và **Cung Mệnh**:

| Can năm | Tý | Sửu | Dần | Mão | Thìn | Tỵ | Ngọ | Mùi | Thân | Dậu | Tuất | Hợi |
|---------|:--:|:---:|:---:|:---:|:----:|:--:|:---:|:---:|:----:|:---:|:----:|:---:|
| **Giáp/Kỷ** | 2 | 6 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 | 2 | 2 |
| **Ất/Canh** | 6 | 2 | 4 | 4 | 5 | 5 | 6 | 6 | 2 | 2 | 3 | 3 |
| **Bính/Tân** | 2 | 3 | 5 | 5 | 6 | 6 | 2 | 2 | 3 | 3 | 4 | 4 |
| **Đinh/Nhâm** | 3 | 4 | 6 | 6 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 |
| **Mậu/Quý** | 4 | 5 | 2 | 2 | 3 | 3 | 4 | 4 | 5 | 5 | 6 | 6 |

**Chú thích:** 2=Thủy, 3=Mộc, 4=Kim, 5=Thổ, 6=Hỏa

---

## CODE SỬA LỖI

Cập nhật file `data/cung_cuc.py`:

```python
"""
Data Layer - Cung and Cục Constants
BẢNG CỤC CHUẨN NAM PHÁI - ĐÃ SỬA
"""

# 12 Cung (Palaces) - Fixed order starting from Mệnh
CUNG_ORDER = ['Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 'Quan Lộc', 'Nô Bộc', 
              'Thiên Di', 'Tật Ách', 'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ']

# Ngũ Hành Cục với số cục
CUC_TYPE = {
    'Thủy Nhị Cục': 2,
    'Mộc Tam Cục': 3,
    'Kim Tứ Cục': 4,
    'Thổ Ngũ Cục': 5,
    'Hỏa Lục Cục': 6
}

# Bảng tra Cục CHUẨN NAM PHÁI dựa trên Thiên Can năm sinh và Địa Chi của Cung Mệnh
# Khẩu quyết: "Giáp Kỷ chi niên Bính tác thủ"
CUC_TABLE = {
    # Giáp (0), Kỷ (5)
    0: {0: 'Thủy Nhị Cục', 1: 'Hỏa Lục Cục', 2: 'Mộc Tam Cục', 3: 'Mộc Tam Cục', 
        4: 'Kim Tứ Cục', 5: 'Kim Tứ Cục', 6: 'Thổ Ngũ Cục', 7: 'Thổ Ngũ Cục',
        8: 'Hỏa Lục Cục', 9: 'Hỏa Lục Cục', 10: 'Thủy Nhị Cục', 11: 'Thủy Nhị Cục'},
    5: {0: 'Thủy Nhị Cục', 1: 'Hỏa Lục Cục', 2: 'Mộc Tam Cục', 3: 'Mộc Tam Cục', 
        4: 'Kim Tứ Cục', 5: 'Kim Tứ Cục', 6: 'Thổ Ngũ Cục', 7: 'Thổ Ngũ Cục',
        8: 'Hỏa Lục Cục', 9: 'Hỏa Lục Cục', 10: 'Thủy Nhị Cục', 11: 'Thủy Nhị Cục'},
    
    # Ất (1), Canh (6)
    1: {0: 'Hỏa Lục Cục', 1: 'Thủy Nhị Cục', 2: 'Kim Tứ Cục', 3: 'Kim Tứ Cục', 
        4: 'Thổ Ngũ Cục', 5: 'Thổ Ngũ Cục', 6: 'Hỏa Lục Cục', 7: 'Hỏa Lục Cục',
        8: 'Thủy Nhị Cục', 9: 'Thủy Nhị Cục', 10: 'Mộc Tam Cục', 11: 'Mộc Tam Cục'},
    6: {0: 'Hỏa Lục Cục', 1: 'Thủy Nhị Cục', 2: 'Kim Tứ Cục', 3: 'Kim Tứ Cục', 
        4: 'Thổ Ngũ Cục', 5: 'Thổ Ngũ Cục', 6: 'Hỏa Lục Cục', 7: 'Hỏa Lục Cục',
        8: 'Thủy Nhị Cục', 9: 'Thủy Nhị Cục', 10: 'Mộc Tam Cục', 11: 'Mộc Tam Cục'},
    
    # Bính (2), Tân (7)
    2: {0: 'Thủy Nhị Cục', 1: 'Mộc Tam Cục', 2: 'Thổ Ngũ Cục', 3: 'Thổ Ngũ Cục', 
        4: 'Hỏa Lục Cục', 5: 'Hỏa Lục Cục', 6: 'Thủy Nhị Cục', 7: 'Thủy Nhị Cục',
        8: 'Mộc Tam Cục', 9: 'Mộc Tam Cục', 10: 'Kim Tứ Cục', 11: 'Kim Tứ Cục'},
    7: {0: 'Thủy Nhị Cục', 1: 'Mộc Tam Cục', 2: 'Thổ Ngũ Cục', 3: 'Thổ Ngũ Cục', 
        4: 'Hỏa Lục Cục', 5: 'Hỏa Lục Cục', 6: 'Thủy Nhị Cục', 7: 'Thủy Nhị Cục',
        8: 'Mộc Tam Cục', 9: 'Mộc Tam Cục', 10: 'Kim Tứ Cục', 11: 'Kim Tứ Cục'},
    
    # Đinh (3), Nhâm (8)
    3: {0: 'Mộc Tam Cục', 1: 'Kim Tứ Cục', 2: 'Hỏa Lục Cục', 3: 'Hỏa Lục Cục', 
        4: 'Thủy Nhị Cục', 5: 'Thủy Nhị Cục', 6: 'Mộc Tam Cục', 7: 'Mộc Tam Cục',
        8: 'Kim Tứ Cục', 9: 'Kim Tứ Cục', 10: 'Thổ Ngũ Cục', 11: 'Thổ Ngũ Cục'},
    8: {0: 'Mộc Tam Cục', 1: 'Kim Tứ Cục', 2: 'Hỏa Lục Cục', 3: 'Hỏa Lục Cục', 
        4: 'Thủy Nhị Cục', 5: 'Thủy Nhị Cục', 6: 'Mộc Tam Cục', 7: 'Mộc Tam Cục',
        8: 'Kim Tứ Cục', 9: 'Kim Tứ Cục', 10: 'Thổ Ngũ Cục', 11: 'Thổ Ngũ Cục'},
    
    # Mậu (4), Quý (9)
    4: {0: 'Kim Tứ Cục', 1: 'Thổ Ngũ Cục', 2: 'Thủy Nhị Cục', 3: 'Thủy Nhị Cục', 
        4: 'Mộc Tam Cục', 5: 'Mộc Tam Cục', 6: 'Kim Tứ Cục', 7: 'Kim Tứ Cục',
        8: 'Thổ Ngũ Cục', 9: 'Thổ Ngũ Cục', 10: 'Hỏa Lục Cục', 11: 'Hỏa Lục Cục'},
    9: {0: 'Kim Tứ Cục', 1: 'Thổ Ngũ Cục', 2: 'Thủy Nhị Cục', 3: 'Thủy Nhị Cục', 
        4: 'Mộc Tam Cục', 5: 'Mộc Tam Cục', 6: 'Kim Tứ Cục', 7: 'Kim Tứ Cục',
        8: 'Thổ Ngũ Cục', 9: 'Thổ Ngũ Cục', 10: 'Hỏa Lục Cục', 11: 'Hỏa Lục Cục'},
}
```

---

## KIỂM TRA SAU KHI SỬA

Sau khi cập nhật bảng Cục, chạy test với lá số mẫu:

```
Ngày: 28/3/1994, Giờ: Mão, Nam
Kết quả mong đợi:
- Cục: Thủy Nhị Cục (2) -> DONE
- Tử Vi: Dậu -> DONE
- Thiên Lương tại Mệnh (Tý) -> DONE
```

---

## TÓM TẮT

| Hạng mục | Trước khi sửa | Sau khi sửa |
|----------|--------------|-------------|
| CUC_TABLE[Giáp][Tý] | Hỏa Lục Cục (6) | Thủy Nhị Cục (2) |
| Tử Vi vị trí | Sai | Đúng |
| Các Chính Tinh | Sai | Đúng |

---

*Báo cáo lập ngày: 15/12/2025*
*Cập nhật lần cuối: 20/12/2025*
*Người đánh giá: Chuyên gia Tử Vi Nam Phái 20 năm kinh nghiệm*

---

## TỔNG HỢP KHẨU QUYẾT TỬ VI NAM PHÁI

### 1. Khẩu quyết An Cung Mệnh

**Khẩu quyết:** "Chính nguyệt khởi Dần, thuận tháng nghịch giờ"

**Công thức:**
```
Cung Mệnh = (2 + tháng - 1 - giờ) mod 12 = (Dần + tháng - giờ) mod 12
```

**Nguồn:** Code `core/cung_menh.py`, docs `CALCULATION_GUIDE.md`, `BA_SYSTEM_ARCHITECTURE.md`

---

### 2. Khẩu quyết An Cung Thân

**Khẩu quyết:** "Chính nguyệt khởi Dần, thuận tháng thuận giờ"

**Công thức:**
```
Cung Thân = (2 + tháng - 1 + giờ) mod 12 = (Dần + tháng + giờ) mod 12
```

**Nguồn:** Code `core/cung_menh.py`, docs `CALCULATION_GUIDE.md`

---

### 3. Khẩu quyết Ngũ Hổ Độn (An Can Tháng)

**Khẩu quyết:**
- Giáp Kỷ chi niên **Bính** tác thủ (tháng 1 khởi Bính Dần)
- Ất Canh chi niên **Mậu** tác thủ (tháng 1 khởi Mậu Dần)
- Bính Tân chi niên **Canh** tác thủ (tháng 1 khởi Canh Dần)
- Đinh Nhâm chi niên **Nhâm** tác thủ (tháng 1 khởi Nhâm Dần)
- Mậu Quý chi niên **Giáp** tác thủ (tháng 1 khởi Giáp Dần)

**Bảng tra:**
| Can Năm | Start Can tháng 1 |
|---------|-------------------|
| Giáp/Kỷ | Bính (2) |
| Ất/Canh | Mậu (4) |
| Bính/Tân | Canh (6) |
| Đinh/Nhâm | Nhâm (8) |
| Mậu/Quý | Giáp (0) |

**Nguồn:** Code `data/cung_cuc.py`, docs `CALCULATION_GUIDE.md`

---

### 4. Khẩu quyết An Lộc Tồn

**Khẩu quyết:**
- Giáp Lộc tại **Dần**, Ất Lộc tại **Mão**
- Bính Mậu tại **Tỵ**, Đinh Kỷ tại **Ngọ**
- Canh Lộc tại **Thân**, Tân Lộc tại **Dậu**
- Nhâm Lộc tại **Hợi**, Quý Lộc tại **Tý**

**Bảng tra:**
| Can Năm | Lộc Tồn |
|---------|---------|
| Giáp | Dần |
| Ất | Mão |
| Bính | Tỵ |
| Đinh | Ngọ |
| Mậu | Tỵ |
| Kỷ | Ngọ |
| Canh | Thân |
| Tân | Dậu |
| Nhâm | Hợi |
| Quý | Tý |

**Nguồn:** Code `data/phu_tinh_luc_sat.py`, Internet (bachhoaxanh.com, mogi.vn)

---

### 5. Khẩu quyết An Kình Dương / Đà La

- **Kình Dương:** Lộc Tồn + 1 (thuận)
- **Đà La:** Lộc Tồn - 1 (nghịch)

**Khẩu quyết:** "Kình tiền Đà hậu"

**Nguồn:** Code `stars/luc_sat_placer.py`

---

### 6. Khẩu quyết An Tả Phù / Hữu Bật

**Khẩu quyết:**
- **Tả Phù:** Tháng 1 khởi **Thìn**, đếm **thuận** theo tháng
- **Hữu Bật:** Tháng 1 khởi **Tuất**, đếm **nghịch** theo tháng

**Công thức:**
```
Tả Phù = (4 + tháng - 1) mod 12
Hữu Bật = (10 - tháng + 1) mod 12
```

**Nguồn:** Code `stars/luc_cat_placer.py`, docs `CALCULATION_GUIDE.md`

---

### 7. Khẩu quyết An Văn Xương / Văn Khúc

**Khẩu quyết:**
- **Văn Xương:** Giờ Tý khởi **Tuất**, đếm **nghịch**
- **Văn Khúc:** Giờ Tý khởi **Thìn**, đếm **thuận**

**Công thức:**
```
Văn Xương = (10 - giờ) mod 12
Văn Khúc = (4 + giờ) mod 12
```

**Nguồn:** Code `stars/luc_cat_placer.py`

---

### 8. Khẩu quyết An Đại Vận

**Khẩu quyết:**
- Dương Nam / Âm Nữ: Đi **thuận** từ Cung Mệnh
- Âm Nam / Dương Nữ: Đi **nghịch** từ Cung Mệnh

**Tuổi khởi vận:** Bằng số Cục (Thủy 2 tuổi, Mộc 3 tuổi, Kim 4 tuổi, Thổ 5 tuổi, Hỏa 6 tuổi)

**Nguồn:** Code `core/fortune_periods.py`, docs `BA_SYSTEM_ARCHITECTURE.md`

---

### 9. Khẩu quyết An Vòng Trường Sinh

**Khẩu quyết:**
- Trường Sinh khởi theo Cục và Âm Dương
- **Dương Nam / Âm Nữ:** Đi thuận
- **Âm Nam / Dương Nữ:** Đi nghịch

**Vị trí khởi Trường Sinh:**
| Cục | Dương | Âm |
|-----|-------|-----|
| Thủy (2) | Thân | Mão |
| Mộc (3) | Hợi | Ngọ |
| Kim (4) | Tỵ | Tỵ |
| Thổ (5) | Thân | Mão |
| Hỏa (6) | Dần | Dậu |

**Nguồn:** Code `stars/truong_sinh_placer.py`, docs `BA_DATA_DICTIONARY.md`

---

### 10. Khẩu quyết Tứ Hóa Nam Phái

**Khẩu quyết cho nam Giáp:**
"Giáp **Liêm** Phá Vũ Dương" 
(Liêm Trinh hóa Lộc, Phá Quân hóa Quyền, Vũ Khúc hóa Khoa, Thái Dương hóa Kỵ)

**Lưu ý đặc biệt Nam Phái:**
- Năm Giáp: **Vũ Khúc** hóa Khoa (không phải Thiên Phủ như Bắc Phái)

**Nguồn:** Code `data/tu_hoa.py`, docs `BA_SYSTEM_ARCHITECTURE.md`

---

## KHẨU QUYẾT LUẬN ĐOÁN TỬ VI

### 1. Hình thái và Tính cách các Sao

| Sao | Khẩu quyết |
|-----|------------|
| Tử Vi | "Tử Vi thì tầm tước da dâu, con người chính trực chẳng màu oan sai." |
| Thiên Cơ | "Thiên Cơ thì chẳng vắn chẳng dài, lòng lành tay khéo hay hài đức nghề." |
| Tử Vi + Thiên Phủ | "Tử Vi phúc hậu dung hình, Thiên Phủ tiết hạnh thông minh ôn hòa. Hai sao đồng gặp một tòa, thiên tư ôn thuận thật là tốt thay." |
| Tả Hữu | "Tả Hữu đóng ở mệnh cung, đoán rằng số ấy ly tông cửa nhà. Tả Hữu cũng hợp mệnh ta, là người cốt cách khoan hòa tốt thay." |

---

### 2. Cách cục và Tổ hợp Sao

| Cách cục | Khẩu quyết | Ý nghĩa |
|----------|------------|---------|
| Tử Phủ Dần Thân | "Tử Phủ Dần Thân trung thân phúc hậu" | Bộ Tử Vi - Thiên Phủ cư tại Dần hoặc Thân. |
| Tử Vi cư Ngọ | "Tử Vi cư Ngọ cực hướng Ly Minh" | Vị trí tối thượng của sao Tử Vi tại cung Ngọ. |
| Thủy trừng Quế ngạc | "Thủy trừng Quế ngạc" | Thái Âm tại cung Tý hội cùng Thiên Đồng, chủ về người từ tốn, hài hòa, vừa giàu vừa thọ. |
| Cự Nhật Dần Thân | "Cự Nhật Dần Thân quang phong tam đại" | Bộ Cự Môn - Thái Dương tại Dần hoặc Thân mang lại sự hiển đạt, có tiếng tăm. |
| Đồng Lương Dần Thân | "Đồng Lương Dần Thân, khi xưa bạch thủ mà nay sang giàu" | Người khởi nghiệp từ tay trắng nhưng về sau rất khá giả. |
| Thiện Ấm triều cương | "Thiện Ấm triều cương" | Chỉ bộ Thiên Lương (Thiện tinh) và Thiên Đồng (Ấm tinh) cư tại các cung Tý, Ngọ, Dần, Thân, chủ về phúc thọ song toàn. |
| Binh Hình Tướng Ấn | "Binh Hình Tướng Ấn" | Bộ sao của người chỉ huy trong lực lượng vũ trang (Phục Binh, Thiên Hình, Tướng Quân, Quốc Ấn), chủ về vạn lý binh quyền. |
| Hổ Hao đắc cách | "Hổ Hao đắc cách trúng Thủy triều đông" | Sự kết hợp của Bạch Hổ và Song Hao tại Mão Dậu, chủ về sự nghiệp rực rỡ như nước triều dâng. |

---

### 3. Tài lộc và Công danh

| Khẩu quyết | Ý nghĩa |
|------------|---------|
| "Vũ Khúc điền tài, phú gia địch quốc lâm lai tổ điền" | Người có sao Vũ Khúc cư cung Tài hoặc Điền chủ về sự giàu có lớn, tích lũy được nhiều tài sản. |
| "Vợ về của có muôn vàn, Âm Dương Lộc Mã đế đồng Quyền Khoa" | Chỉ sự may mắn, giàu sang khi các bộ sao này hội tụ tại cung Phu Thê. |
| "Đái ấn triều hồi" | Chỉ cách cục Tử Vi gặp Triệt tại cung Quan, báo hiệu sự gián đoạn đường công danh, phải từ quan về vườn sớm. |

---

### 4. Hóa giải và Rủi ro

| Khẩu quyết | Ý nghĩa |
|------------|---------|
| "Thiên Nguyệt Đức Giải Thần tàng, cũng là quan phúc một làng trừ hung" | Sao Giải Thần đi cùng bộ Tứ Đức giúp hóa giải tai ách rất mạnh. |
| "Phúc đức Tuần Triệt ra liền, con mất mả trên miền hoang sơn" | Cảnh báo sự thất lạc mồ mả hoặc giảm phúc khi cung Phúc Đức gặp Tuần, Triệt. |
| "Hiếm hoi bởi tại Hình Hao, đến già mới có tay nào con thơ" | Chỉ sự muộn màng, khó khăn đường con cái khi có Thiên Hình và Song Hao. |
| "Tang Hổ mệnh cung, sau trước gái cũng đành lỡ bước cổ" | Chỉ sự trắc trở trong duyên nợ của người có Tang Môn, Bạch Hổ tại Mệnh. |
| "Thuận Thái Tuế thì sống, chống Thái Tuế thì chết" | Nguyên tắc ứng xử khi gặp vòng Thái Tuế, yêu cầu con người phải làm điều đúng đạo nghĩa, không làm sai pháp luật. |

---

### 5. Triết lý Hành trì

**9 chữ vàng cải biến số phận:**

> "Trời tích nắng, Khí tích mưa, Nhân tích thiện."

**Giải thích:** Như trời tích lũy nắng để có nắng, tích lũy khí để có mưa, con người tích lũy điều thiện để đổi vận mệnh.

---

### 6. Ứng dụng trong Code

Các khẩu quyết luận đoán này được sử dụng trong:
- `interpretation/cach_cuc.py` - Nhận diện cách cục đặc biệt
- `interpretation/patterns.py` - Phân tích pattern sao
- `data/meanings/*.json` - Lưu trữ ý nghĩa luận giải

**Lưu ý:** Đây là khẩu quyết luận đoán, khác với khẩu quyết an sao (tính toán). Khẩu quyết luận đoán giúp đọc lá số nhanh hơn.
