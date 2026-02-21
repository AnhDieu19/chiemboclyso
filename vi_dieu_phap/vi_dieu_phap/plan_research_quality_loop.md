# KẾ HOẠCH NGHIÊN CỨU & QUY TRÌNH "VÒNG LẶP CHẤT LƯỢNG" (QUALITY LOOP)
**Module:** Vi Diệu Pháp (Abhidhamma)
**Mục tiêu:** Đạt điểm chất lượng 10/10 cho dữ liệu & kiến thức.

---

## 1. QUY TRÌNH VÒNG LẶP (THE LOOP WORKFLOW)

Quy trình sẽ được lặp lại liên tục cho đến khi đạt điểm tuyệt đối.

1.  **Phase 1: Research & Expand** (Nghiên cứu & Mở rộng)
    *   Dựa trên checklist, xác định thông tin còn thiếu.
    *   Tìm kiếm (Search) hoặc trích xuất từ "Kho tri thức" (Knowledge Base).
    *   Cập nhật vào tài liệu `research_vi_dieu_phap.md`.

2.  **Phase 2: Audit & Scoring** (Kiểm tra & Chấm điểm)
    *   So sánh nội dung hiện tại với "Tiêu chuẩn 10/10".
    *   Chấm điểm từng hạng mục.
    *   Liệt kê các điểm khuyết (Gaps).

3.  **Phase 3: Decision** (Quyết định)
    *   Nếu điểm < 10: Quay lại Phase 1 (Auto-search bổ sung).
    *   Nếu điểm = 10: Đóng băng tài liệu nghiên cứu, chuyển sang giai đoạn Specs/Dev.

---

## 2. TIÊU CHUẨN CHẤT LƯỢNG 10/10 (CHECKLIST)

Để một đơn vị kiến thức (ví dụ: 1 Tâm hoặc 1 Sở hữu tâm) đạt chuẩn, cần phải có đủ các trường thông tin sau:

| STT | Tiêu chí | Trọng số | Yêu cầu chi tiết |
|-----|----------|----------|------------------|
| 1 | **Định danh** | 1.0 | Tên Tiếng Việt chuẩn, Tên Pāli gốc, Mã định danh (ID). |
| 2 | **Phân loại** | 1.0 | Thuộc nhóm nào (Vực, Căn, Giống)? Cấu trúc phân cấp rõ ràng. |
| 3 | **Định nghĩa** | 1.0 | Giải thích khái niệm ngắn gọn, dễ hiểu. |
| 4 | **Tứ Ý Nghĩa** | 2.0 | 4 khía cạnh thực tính pháp: <br>- Trạng thái (Lakkhana)<br>- Phận sự (Rasa)<br>- Biểu hiện (Paccupatthana)<br>- Nhân cần (Padatthana) |
| 5 | **Tương quan (Hiệp lực)** | 2.0 | **Quan trọng nhất cho App:**<br>- Tâm này đi kèm bao nhiêu/những Sở hữu tâm nào?<br>- Sở hữu tâm này phối hợp với những Tâm nào? |
| 6 | **Chi pháp thực hành** | 1.0 | Ứng dụng trong thiền như thế nào? (Đối trị gì? Nuôi dưỡng gì?) |
| 7 | **Dữ liệu cấu trúc** | 2.0 | Có thể chuyển đổi sang JSON/Database schema ngay lập tức không? |

**Tổng điểm: 10.0**

---

## 3. ĐÁNH GIÁ VÒNG 1 (CURRENT STATUS)

**Tài liệu:** `docs/vi_dieu_phap/research/research_vi_dieu_phap.md`

| Tiêu chí | Điểm chấm | Nhận xét (Gaps) |
|----------|-----------|-----------------|
| 1. Định danh | 0.8 / 1.0 | Đã có tên Việt/Pāli, thiếu ID hệ thống. |
| 2. Phân loại | 1.0 / 1.0 | Phân loại tốt (89 tâm, 52 sở hữu). |
| 3. Định nghĩa | 0.5 / 1.0 | Chỉ liệt kê tên, chưa có định nghĩa chi tiết từng mục. |
| 4. Tứ Ý Nghĩa| **0.0 / 2.0** | **Hoàn toàn thiếu.** Chưa có Trạng thái, Phận sự... |
| 5. Tương quan| **0.0 / 2.0** | **Hoàn toàn thiếu.** Chưa biết Tâm nào đi với Sở hữu nào. |
| 6. Thực hành | 0.2 / 1.0 | Sơ sài, chỉ nhắc đến Chi thiền. |
| 7. Cấu trúc | 0.5 / 2.0 | Dạng list văn bản, chưa phải dạng bảng/schema để code. |

**TỔNG ĐIỂM: 3.0 / 10**

---

## 4. KẾ HOẠCH HÀNH ĐỘNG (NEXT STEPS)

### Loop 1: Bổ sung Tứ Ý Nghĩa & Định nghĩa
*   **Mục tiêu:** Tìm kiếm thông tin về "Lakkhana Rasa Paccupatthana Padatthana" của 52 Sở Hữu và các nhóm Tâm chính.
*   **Action:** Cập nhật file Research.

### Loop 2: Xây dựng Ma trận Tương Quan (Matrix)
*   **Mục tiêu:** Xác định quy luật phối hợp (Tâm nào - Sở hữu nào).
*   **Action:** Tạo bảng Matrix hoặc danh sách Hiệp lực.

### Loop 3: Chuyển đổi Schema
*   **Mục tiêu:** Viết lại dưới dạng cấu trúc dữ liệu cho Dev.
