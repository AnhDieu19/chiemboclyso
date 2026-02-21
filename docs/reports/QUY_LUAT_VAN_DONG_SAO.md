# 📜 QUY LUẬT VẬN ĐỘNG CÁC SAO TỬ VI

> Tài liệu phân tích quy luật vận động của các sao trong Tử Vi Đẩu Số
> 
> Ngày tạo: 23/12/2024

---

## 📊 TỔNG QUAN

Trong Tử Vi Đẩu Số, có hơn **100+ sao** được phân bổ vào **12 cung**. Vị trí của các sao phụ thuộc vào các yếu tố sinh thời khác nhau.

### Các yếu tố ảnh hưởng đến vị trí sao:
| Yếu tố | Ký hiệu | Chu kỳ |
|--------|---------|--------|
| Thiên Can năm sinh | Can | 10 năm |
| Địa Chi năm sinh | Chi | 12 năm |
| Cục | Cục | 5 loại × 6 mức = 30 |
| Ngày âm lịch | Day | 30 ngày |
| Tháng âm lịch | Month | 12 tháng |
| Giờ sinh | Hour | 12 canh giờ |
| Giới tính | Gender | Nam/Nữ |

---

## 🌟 I. CHÍNH TINH (14 SAO CHÍNH)

### 1.1 Nhóm Tử Vi (6 sao)
**Phụ thuộc vào: CỤC + NGÀY ÂM LỊCH**

| Sao | Vị trí tương đối so với Tử Vi |
|-----|------------------------------|
| **Tử Vi** | Sao chủ - tính từ công thức |
| Thiên Cơ | Tử Vi - 1 |
| Thái Dương | Tử Vi - 3 |
| Vũ Khúc | Tử Vi - 4 |
| Thiên Đồng | Tử Vi - 5 |
| Liêm Trinh | Tử Vi - 8 |

**Công thức tính vị trí Tử Vi:**
```
1. Tìm 'a' (0 đến Cục-1) sao cho (Ngày + a) chia hết cho Cục
2. b = (Ngày + a) / Cục
3. Bắt đầu từ Dần (vị trí 2), tiến b bước
4. Nếu 'a' LẺ: lùi 'a' bước
   Nếu 'a' CHẴN: tiến 'a' bước
```

### 1.2 Nhóm Thiên Phủ (8 sao)
**Phụ thuộc vào: VỊ TRÍ TỬ VI (đối xứng)**

| Sao | Vị trí tương đối so với Thiên Phủ |
|-----|----------------------------------|
| **Thiên Phủ** | Đối xứng Tử Vi qua trục Dần-Thân: `(16 - Tử Vi) % 12` |
| Thái Âm | Thiên Phủ + 1 |
| Tham Lang | Thiên Phủ + 2 |
| Cự Môn | Thiên Phủ + 3 |
| Thiên Tướng | Thiên Phủ + 4 |
| Thiên Lương | Thiên Phủ + 5 |
| Thất Sát | Thiên Phủ + 6 |
| Phá Quân | Thiên Phủ + 10 |

### 📈 QUY LUẬT VẬN ĐỘNG CHÍNH TINH

**Chu kỳ**: Phụ thuộc Cục và Ngày → thay đổi theo ngày
- Cùng Cục, khác ngày = khác vị trí
- Khác Cục = hoàn toàn khác pattern

```
Ví dụ với Hỏa Lục Cục:
Ngày 1  → Tử Vi ở Dần
Ngày 6  → Tử Vi ở Mùi
Ngày 12 → Tử Vi ở Dần
Ngày 18 → Tử Vi ở Mùi
...
```

---

## ⭐ II. LỤC CÁT TINH (6 SAO CÁT)

### 2.1 Tả Phù, Hữu Bật
**Phụ thuộc vào: THÁNG ÂM LỊCH**

| Sao | Công thức | Hướng |
|-----|-----------|-------|
| **Tả Phù** | `(Thìn + tháng - 1) % 12` | Thuận từ Thìn |
| **Hữu Bật** | `(Tuất - tháng + 1) % 12` | Nghịch từ Tuất |

**Quy luật**: Đối xứng qua trục Thìn-Tuất
```
Tháng 1: Tả Phù @ Thìn (4), Hữu Bật @ Tuất (10)
Tháng 2: Tả Phù @ Tỵ (5),  Hữu Bật @ Dậu (9)
Tháng 3: Tả Phù @ Ngọ (6), Hữu Bật @ Thân (8)
...
```

### 2.2 Văn Xương, Văn Khúc
**Phụ thuộc vào: GIỜ SINH**

| Sao | Công thức | Hướng |
|-----|-----------|-------|
| **Văn Xương** | `(Tuất - giờ) % 12` | Nghịch từ Tuất |
| **Văn Khúc** | `(Thìn + giờ) % 12` | Thuận từ Thìn |

**Quy luật**: Đối xứng qua trục Thìn-Tuất
```
Giờ Tý (0):  Xương @ Tuất, Khúc @ Thìn
Giờ Sửu (1): Xương @ Dậu,  Khúc @ Tỵ
Giờ Dần (2): Xương @ Thân, Khúc @ Ngọ
...
```

### 2.3 Thiên Khôi, Thiên Việt
**Phụ thuộc vào: THIÊN CAN NĂM SINH**

| Thiên Can | Thiên Khôi | Thiên Việt |
|-----------|------------|------------|
| Giáp | Sửu | Mùi |
| Ất | Tý | Thân |
| Bính, Mậu | Hợi | Dậu |
| Đinh, Kỷ | Dậu | Hợi |
| Canh | Mùi | Sửu |
| Tân | Ngọ | Dần |
| Nhâm | Mão | Tỵ |
| Quý | Mão | Tỵ |

**Quy luật**: Cố định theo Thiên Can → chu kỳ 10 năm

---

## 💀 III. LỤC SÁT TINH (6 SAO SÁT)

### 3.1 Kình Dương, Đà La
**Phụ thuộc vào: THIÊN CAN (qua Lộc Tồn)**

| Thiên Can | Lộc Tồn | Kình Dương | Đà La |
|-----------|---------|------------|-------|
| Giáp | Dần | Mão | Sửu |
| Ất | Mão | Thìn | Dần |
| Bính, Mậu | Tỵ | Ngọ | Thìn |
| Đinh, Kỷ | Ngọ | Mùi | Tỵ |
| Canh | Thân | Dậu | Mùi |
| Tân | Dậu | Tuất | Thân |
| Nhâm | Hợi | Tý | Tuất |
| Quý | Tý | Sửu | Hợi |

**Quy luật**: `Kình Dương = Lộc Tồn + 1`, `Đà La = Lộc Tồn - 1`

### 3.2 Hỏa Tinh, Linh Tinh
**Phụ thuộc vào: ĐỊA CHI + GIỜ + GIỚI TÍNH**

**Vị trí cơ sở theo nhóm Địa Chi:**
| Nhóm Chi năm | Hỏa Tinh base | Linh Tinh base |
|--------------|---------------|----------------|
| Dần, Ngọ, Tuất | Sửu (1) | Mão (3) |
| Thân, Tý, Thìn | Dần (2) | Tuất (10) |
| Tỵ, Dậu, Sửu | Mão (3) | Tuất (10) |
| Hợi, Mão, Mùi | Dậu (9) | Tuất (10) |

**Hướng đi theo Âm/Dương + Giới tính:**
| Năm | Giới tính | Hướng Hỏa | Hướng Linh |
|-----|-----------|-----------|------------|
| Dương | Nam | Thuận | Nghịch |
| Dương | Nữ | Nghịch | Thuận |
| Âm | Nam | Nghịch | Thuận |
| Âm | Nữ | Thuận | Nghịch |

### 3.3 Địa Không, Địa Kiếp
**Phụ thuộc vào: GIỜ SINH**

| Sao | Công thức |
|-----|-----------|
| **Địa Không** | `(11 - giờ) % 12` |
| **Địa Kiếp** | `(11 + giờ) % 12` |

**Quy luật**: Đối xứng qua trục Hợi
```
Giờ Tý (0):  Địa Không @ Hợi (11), Địa Kiếp @ Hợi (11)
Giờ Sửu (1): Địa Không @ Tuất (10), Địa Kiếp @ Tý (0)
Giờ Dần (2): Địa Không @ Dậu (9),  Địa Kiếp @ Sửu (1)
...
```

---

## 🔄 IV. VÒNG TRƯỜNG SINH (12 SAO)

**Phụ thuộc vào: CỤC + THIÊN CAN + GIỚI TÍNH**

### 4.1 Vị trí khởi đầu theo Cục

| Cục | Hành | Trường Sinh bắt đầu |
|-----|------|---------------------|
| Kim | Kim | Tỵ (5) |
| Mộc | Mộc | Hợi (11) |
| Thủy | Thủy | Thân (8) |
| Hỏa | Hỏa | Dần (2) |
| Thổ | Thổ | Thân (8) |

### 4.2 Hướng đi theo Âm/Dương + Giới tính

| Can năm | Giới tính | Hướng |
|---------|-----------|-------|
| Dương (Giáp,Bính,Mậu,Canh,Nhâm) | Nam | Thuận |
| Dương | Nữ | Nghịch |
| Âm (Ất,Đinh,Kỷ,Tân,Quý) | Nam | Nghịch |
| Âm | Nữ | Thuận |

### 4.3 Thứ tự 12 sao
```
Trường Sinh → Mộc Dục → Quan Đới → Lâm Quan → Đế Vượng → Suy 
→ Bệnh → Tử → Mộ → Tuyệt → Thai → Dưỡng
```

---

## 🎯 V. VÒNG THÁI TUẾ (12 SAO)

**Phụ thuộc vào: ĐỊA CHI NĂM SINH**

### Quy luật đơn giản:
- **Thái Tuế** luôn ở vị trí **Địa Chi năm sinh**
- Các sao khác đi thuận từ Thái Tuế

### Thứ tự 12 sao
```
Thái Tuế → Thiếu Dương → Tang Môn → Thiếu Âm → Quan Phù → Tử Phù 
→ Tuế Phá → Long Đức → Bạch Hổ → Phúc Đức → Điếu Khách → Trực Phù
```

**Ví dụ**: Năm Ngọ → Thái Tuế @ Ngọ, Thiếu Dương @ Mùi, Tang Môn @ Thân...

---

## 📚 VI. VÒNG BÁC SỸ (12 SAO)

**Phụ thuộc vào: LỘC TỒN + THIÊN CAN + GIỚI TÍNH**

- **Bắt đầu**: Từ vị trí Lộc Tồn
- **Hướng**: Theo Âm/Dương + Giới tính (như Trường Sinh)

### Thứ tự 12 sao
```
Bác Sỹ → Lực Sỹ → Thanh Long → Tiểu Hao → Tướng Quân → Tấu Thư 
→ Phi Liêm → Hỷ Thần → Bệnh Phù → Đại Hao → Phục Binh → Quan Phủ
```

---

## ⚡ VII. TỨ HÓA

**Phụ thuộc vào: THIÊN CAN NĂM SINH**

| Thiên Can | Hóa Lộc | Hóa Quyền | Hóa Khoa | Hóa Kỵ |
|-----------|---------|-----------|----------|--------|
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

**Quy luật**: Cố định theo Thiên Can → chu kỳ 10 năm

---

## 🎲 VIII. CÁC SAO KHÁC (TẠP TINH)

### 8.1 Sao theo Địa Chi năm (chu kỳ 12 năm)

| Sao | Công thức |
|-----|-----------|
| **Thiên Mã** | Tam Hợp Xung: Dần→Thân, Thân→Dần, Tỵ→Hợi, Hợi→Tỵ |
| **Hồng Loan** | Bảng tra theo Chi |
| **Thiên Hỷ** | Đối xứng Hồng Loan |
| **Đào Hoa** | Tam Hợp tra bảng |
| **Hoa Cái** | Tra bảng theo Chi |

### 8.2 Sao theo Tháng (chu kỳ 12 tháng)

| Sao | Công thức |
|-----|-----------|
| **Long Đức** | `(Tỵ + tháng - 1) % 12` |
| **Nguyệt Đức** | `(Tỵ + tháng - 1) % 12` hoặc tra bảng |
| **Thiên Hình** | `(Dậu + tháng - 1) % 12` |
| **Thiên Giải** | `(Thân + tháng - 1) % 12` |

### 8.3 Sao cố định

| Sao | Vị trí |
|-----|--------|
| **Thiên La** | Thìn (4) - luôn cố định |
| **Địa Võng** | Tuất (10) - luôn cố định |

---

## 📊 IX. BẢNG TỔNG HỢP CHU KỲ VẬN ĐỘNG

```
┌─────────────────┬────────────────────────────────────────────────────────────┐
│ CHU KỲ          │ CÁC SAO THAY ĐỔI                                           │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ 60 NĂM          │ Nạp Âm (nguyên tố năm sinh)                                │
│ (Lục Thập Hoa   │ Kết hợp Can + Chi tạo pattern lớn                          │
│  Giáp)          │                                                            │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ 12 NĂM          │ Vòng Thái Tuế (12 sao), Thiên Mã, Hồng Loan, Thiên Hỷ,    │
│ (Địa Chi)       │ Đào Hoa, Hoa Cái, Cô Thần, Quả Tú, Thiên Khốc, Thiên Hư   │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ 10 NĂM          │ Lộc Tồn, Kình Dương, Đà La, Thiên Khôi, Thiên Việt,       │
│ (Thiên Can)     │ Vòng Bác Sỹ (12 sao), Tứ Hóa, Tuần, Triệt,                │
│                 │ Thiên Quan, Thiên Phúc                                     │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ THEO NGÀY       │ 14 Chính Tinh (phụ thuộc Cục + Ngày)                       │
│                 │ Ân Quang, Thiên Quý, Tam Thai, Bát Tọa                     │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ THEO THÁNG      │ Tả Phù, Hữu Bật, Long Đức, Nguyệt Đức, Thiên Hình,        │
│                 │ Thiên Giải, Địa Giải                                       │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ THEO GIỜ        │ Văn Xương, Văn Khúc, Địa Không, Địa Kiếp,                  │
│                 │ Thai Phụ, Phong Cáo, Hỏa Tinh*, Linh Tinh*                 │
│                 │ (*kết hợp với Chi năm + Giới tính)                         │
├─────────────────┼────────────────────────────────────────────────────────────┤
│ CỐ ĐỊNH         │ Thiên La (Thìn), Địa Võng (Tuất)                          │
└─────────────────┴────────────────────────────────────────────────────────────┘
```

---

## 🔮 X. QUY LUẬT VẬN ĐỘNG THEO THỜI GIAN

### 10.1 Khi thay đổi GIỜ SINH
- **Thay đổi nhiều nhất**: Văn Xương, Văn Khúc, Địa Không, Địa Kiếp, Hỏa Tinh, Linh Tinh
- **Không đổi**: 14 Chính Tinh, Lục Cát (trừ Xương/Khúc), các sao theo năm

### 10.2 Khi thay đổi NGÀY SINH
- **Thay đổi nhiều nhất**: 14 Chính Tinh (vì phụ thuộc Ngày + Cục)
- **Không đổi**: Tất cả sao theo Năm, Tháng, Giờ

### 10.3 Khi thay đổi THÁNG SINH
- **Thay đổi**: Tả Phù, Hữu Bật, Long/Nguyệt Đức, Thiên Hình
- **Có thể đổi Cục** → 14 Chính Tinh cũng đổi
- **Không đổi**: Các sao theo Năm, Giờ

### 10.4 Khi thay đổi NĂM SINH
- **Thay đổi hầu hết**: Can thay đổi các sao Lộc Tồn, Bác Sỹ ring, Tứ Hóa...
- **Chi thay đổi**: Thái Tuế ring, Hồng Loan, Đào Hoa...
- **Có thể đổi Cục** → 14 Chính Tinh thay đổi

---

## 💡 XI. ỨNG DỤNG TRONG PLAYBACK

Khi xem vận động sao theo thời gian:

### Chế độ THEO GIỜ
- Quan sát: Xương, Khúc, Không, Kiếp, Hỏa, Linh di chuyển
- 14 Chính Tinh giữ nguyên

### Chế độ THEO NGÀY  
- Quan sát: 14 Chính Tinh di chuyển (theo pattern của Cục)
- Các sao theo giờ, năm giữ nguyên

### Chế độ THEO THÁNG
- Quan sát: Tả Phù, Hữu Bật đối xứng di chuyển
- 14 Chính Tinh có thể đổi nếu Cục đổi

### Chế độ THEO NĂM
- Quan sát pattern lớn: Can đổi → nhóm sao Can đổi
- Chi đổi → nhóm sao Chi đổi
- Pattern 60 năm (Hoa Giáp) rõ ràng nhất

---

## 📝 KẾT LUẬN

1. **14 Chính Tinh** là nhóm phức tạp nhất - phụ thuộc Cục + Ngày
2. **Vòng Trường Sinh, Bác Sỹ** phụ thuộc Giới tính → Nam/Nữ khác pattern
3. **Hỏa Tinh, Linh Tinh** là sao phức tạp - phụ thuộc 3 yếu tố: Chi + Giờ + Giới tính
4. **Pattern 10 năm** (Thiên Can) ảnh hưởng nhiều sao quan trọng
5. **Pattern 12 năm** (Địa Chi) ảnh hưởng Thái Tuế và các sao phụ

---

*Tài liệu được tạo tự động từ phân tích mã nguồn Tu Vi App*
