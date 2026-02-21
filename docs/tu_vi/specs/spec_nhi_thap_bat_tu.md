# ĐẶC TẢ HỆ THỐNG NHỊ THẬP BÁT TÚ

## 1. Tổng Quan
Nhị Thập Bát Tú là 28 chòm sao nằm trên bầu trời theo cách chia của thiên văn học cổ đại Á Đông.
Hệ thống này được ứng dụng để xem ngày tốt xấu (Nhật Cầm) và xem hạn năm (Niên Cầm).

## 2. Danh Sách 28 Sao
Chia làm 4 nhóm (Tứ Tượng), mỗi nhóm 7 sao:

| Nhóm | Phương | Tên Sao (Việt) | Tên Sao (Hán) | Hành | Vật Tượng |
|---|---|---|---|---|---|
| **Thanh Long** | Đông | Giác, Cang, Đê, Phòng, Tâm, Vĩ, Cơ | 角, 亢, 氐, 房, 心, 尾, 箕 | Mộc, Kim, Thổ, Nhật, Nguyệt, Hỏa, Thủy | Giao, Long, Lạc, Thố, Hồ, Hổ, Báo |
| **Huyền Vũ** | Bắc | Đẩu, Ngưu, Nữ, Hư, Nguy, Thất, Bích | 斗, 牛, 女, 虛, 危, 室, 壁 | Mộc, Kim, Thổ, Nhật, Nguyệt, Hỏa, Thủy | Giải, Ngưu, Bức, Thử, Yến, Trư, Du |
| **Bạch Hổ** | Tây | Khuê, Lâu, Vị, Mão, Tất, Chủy, Sâm | 奎, 婁, 胃, 昴, 畢, 觜, 參 | Mộc, Kim, Thổ, Nhật, Nguyệt, Hỏa, Thủy | Lang, Cẩu, Trĩ, Kê, Ô, Hầu, Viên |
| **Chu Tước** | Nam | Tĩnh, Quỷ, Liễu, Tinh, Trương, Dực, Chấn | 井, 鬼, 柳, 星, 張, 翼, 軫 | Mộc, Kim, Thổ, Nhật, Nguyệt, Hỏa, Thủy | Hãn, Dương, Chương, Mã, Lộc, Xà, Dẫn |

## 3. Logic Tính Toán

### 3.1 Nhị Thập Bát Tú Ngày (Nhật Cầm)
Chu kỳ 28 ngày lặp lại liên tục, không phụ thuộc vào tháng nhuận hay năm nhuận.
Cần một ngày mốc (Epoch) để tính toán.

**Công thức:**
`Index = (JulianDay - OFFSET) % 28`

**Thứ tự vòng sao:**
1.Giác → 2.Cang → ... → 7.Cơ → 8.Đẩu → ... → 28.Chấn → quay lại 1.Giác.

**Mốc tham chiếu (Reference Date):**
- Ngày **01/01/1995** (Dương lịch) là ngày **Hư** (Sao thứ 11).
- Hoặc check lịch vạn niên hiện tại để lấy mốc gần nhất.
- Ví dụ kiểm chứng: Ngày 22/12/2023 là ngày **Thất** (Sao thứ 13 - Thất Hỏa Trư).

### 3.2 Nhị Thập Bát Tú Năm (Niên Cầm)
Mỗi năm có một sao quản hạ.
Cách tính:
- Các sao an theo thứ tự các ngày trong tuần của ngày 1 tháng Giêng (Dương Lịch hoặc Âm Lịch tùy phái - *Cần confirm User, mặc định theo Lịch Vạn Sự phổ thông là an theo thứ tự tuần hoàn 28 năm*).

**Cách tính phổ biến (Vòng 28 năm):**
Năm 1994: Giác
Năm 1995: Cang
...
Cứ thế đếm thuận.

## 4. Bảng Tra Cát Hung (Tóm tắt)

| Sao | Tính Chất | Việc Nên Làm | Việc Kỵ |
|---|---|---|---|
| **Giác** | Tốt | Hôn thú, tạo tác | Chôn cất |
| **Cang** | Xấu | (Hung tinh) | Cưới hỏi, khởi công |
| **Đê** | Xấu | (Hung tinh) | Động thổ, xuất hành |
| **Phòng** | Tốt | Xây dựng, cưới hỏi | (Ít kỵ) |
| **Tâm** | Xấu | (Hung tinh) | Cưới hỏi, tranh chấp |
| **Vĩ** | Tốt | Mọi việc tốt | (Ít kỵ) |
| **Cơ** | Tốt | Tốt cho văn chương | Động thổ nhẹ |
| *... (Bổ sung chi tiết khi implement data)* | ... | ... | ... |

## 5. Implementation Notes
- Xây dựng Enum `Star28` chứa 28 sao.
- Hàm `get_daily_star28(julian_day)`: Tính sao theo ngày.
- Hàm `get_yearly_star28(year)`: Tính sao theo năm.
- Dữ liệu chi tiết về Cát/Hung sẽ được lưu trong file JSON/Dict.
