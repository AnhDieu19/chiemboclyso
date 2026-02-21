# ĐẶC TẢ HỆ THỐNG SAO CỬU DIỆU

## 1. Tổng Quan
Hệ thống Cửu Diệu (9 sao chiếu mệnh) là một phần quan trọng trong việc xem hạn hằng năm (Tiểu Hạn/Lưu Niên). Mỗi năm, dựa trên tuổi âm lịch và giới tính, mỗi người sẽ gặp một sao chiếu mệnh khác nhau.
Các sao này luân phiên theo chu kỳ 9 năm.

Danh sách 9 sao:
1. La Hầu (Khẩu thiệt tinh - Xấu)
2. Thổ Tú (Thổ tinh - Trung bình)
3. Thủy Diệu (Thủy tinh - Tốt/Xấu tùy ngũ hành)
4. Thái Bạch (Kim tinh - Rất Xấu)
5. Thái Dương (Nhật tinh - Tốt nam, Xấu nữ)
6. Vân Hán (Hỏa tinh - Trung bình/Xấu)
7. Kế Đô (Hung tinh - Rất Xấu nữ)
8. Thái Âm (Nguyệt tinh - Tốt nữ, Kỵ nam)
9. Mộc Đức (Mộc tinh - Tốt)

## 2. Logic Tính Toán

### 2.1 Input
- **Tuổi Âm Lịch (Lunar Age)**: Tuổi mụ = Năm hiện tại - Năm sinh + 1.
- **Giới Tính (Gender)**: Nam (1) hoặc Nữ (0).

### 2.2 Thuật Toán
Lấy tuổi âm lịch chia cho 9, lấy số dư để xác định sao (tuy nhiên cách phổ biến nhất là tra bảng khởi điểm).

**Cách tính nhanh (dựa trên tuổi mod 9 không chính xác hoàn toàn do chu kỳ, nên dùng bảng tra lookup table):**

Chu kỳ lặp lại là 9 năm.
Ta có thể dùng bảng tra modulo 9 dư bao nhiêu, nhưng thông dụng nhất là danh sách các tuổi khởi điểm.

#### Bảng tra theo số dư (Tuổi chia 9) - NAM MẠNG
*(Lưu ý: Cách này thường phức tạp vì phải trừ đi các mốc. Nên dùng Mapping trực tiếp)*

**Mapping trực tiếp (Logic để Code):**
`Star_Index = (Age - Start_Age) % 9`

Tuy nhiên, đơn giản nhất là dùng mảng cố định cho chu kỳ 9 năm.

Các nhóm tuổi (Tuổi Âm Lịch):

| Sao (Nam) | Sao (Nữ) | Tuổi bắt đầu (và cộng thêm 9) |
|---|---|---|
| La Hầu | Kế Đô | 10, 19, 28, 37, 46, 55, 64, 73, 82, 91 |
| Thổ Tú | Vân Hán | 11, 20, 29, 38, 47, 56, 65, 74, 83, 92 |
| Thủy Diệu | Mộc Đức | 12, 21, 30, 39, 48, 57, 66, 75, 84, 93 |
| Thái Bạch | Thái Âm | 13, 22, 31, 40, 49, 58, 67, 76, 85, 94 |
| Thái Dương | Thổ Tú | 14, 23, 32, 41, 50, 59, 68, 77, 86, 95 |
| Vân Hán | La Hầu | 15, 24, 33, 42, 51, 60, 69, 78, 87, 96 |
| Kế Đô | Thái Dương | 16, 25, 34, 43, 52, 61, 70, 79, 88, 97 |
| Thái Âm | Thái Bạch | 17, 26, 35, 44, 53, 62, 71, 80, 89, 98 |
| Mộc Đức | Thủy Diệu | 18, 27, 36, 45, 54, 63, 72, 81, 90, 99 |

### 2.3 Phân Loại Ngũ Hành & Tính Chất

| Tên Sao | Hán Tự | Ngũ Hành | Tính Chất Chung |
|---|---|---|---|
| **La Hầu** | 羅睺 | Kim | Hung tinh (Nam kỵ, Nữ cũng kỵ). Dễ gặp chuyện thị phi, công quyền, bệnh tai mắt. |
| **Kế Đô** | 計都 | Thổ | Hung tinh (Nữ đại kỵ, Nam cũng kỵ). Dễ bị tai nạn, buồn rầu, hao tài. |
| **Thái Dương** | 太陽 | Hỏa | Cát tinh (Tốt cho Nam, Nữ bình thường). Chủ về danh vọng, tài lộc. |
| **Thái Âm** | 太陰 | Thủy | Cát tinh (Tốt cho Nữ, Nam bình thường). Chủ về tài lộc, tình cảm. |
| **Mộc Đức** | 木德 | Mộc | Cát tinh. Tốt cho học tập, thi cử, mừng vui. Cẩn thận bệnh mắt (nữ). |
| **Vân Hán** | 雲漢 | Hỏa | Trung bình (Hung nhẹ). Dễ nóng nảy, tranh chấp lời nói. Kỵ tháng 2, 8. |
| **Thổ Tú** | 土秀 | Thổ | Trung bình (Hung nhẹ). Dễ bị tiểu nhân, xuất hành không thuận. Kỵ tháng 4, 8. |
| **Thái Bạch** | 太白 | Kim | Hung tinh (Rất xấu). Hao tài tốn của, bệnh tật. "Thái Bạch sạch bách cửa nhà". |
| **Thủy Diệu** | 水曜 | Thủy | Trung bình (Tốt/Xấu). Có tài lộc nhưng dễ bị thị phi, tai nạn nước. Kỵ tháng 4, 8. |

## 3. Cấu Trúc Dữ Liệu Gợi Ý (JSON)

```json
{
  "LaHau": {
    "name": "La Hầu",
    "element": "Kim",
    "type": "Hung",
    "bad_months": [1, 7],
    "description": "Khẩu thiệt tinh, chủ về thị phi, kiện tụng, bệnh tai mắt."
  },
  "KeDo": {
    "name": "Kế Đô",
    "element": "Thổ",
    "type": "Hung",
    "bad_months": [3, 9],
    "description": "Hung tinh, chủ về ám muội, thị phi, đau khổ, hao tài."
  },
  ...
}
```

## 4. Ghi Chú Thực Hiện
- Cần xây dựng hàm `get_cuu_dieu(lunar_age, gender)` trả về object sao tương ứng.
- Hiển thị màu sắc sao dựa trên ngũ hành (Tham chiếu bảng màu `guide_calculation.md` mục 18.2).
