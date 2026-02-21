# SAO THIÊN LƯƠNG - KIẾN THỨC TỪ CHUYÊN GIA

## Nguồn Tham Khảo
*   **Video:** [Sao Thiên Lương Trong Khoa Tử Vi](https://www.youtube.com/watch?v=_nDiq1hbwcY&t=175s)
*   **Chuyên gia:** Thầy Lê Quang Lăng (Tử Vi Nam Phái)
*   **Ngày cập nhật:** 27/09/2019

## 1. Tổng Quan
*   **Biệt danh:** "Ấm Tinh" (Ngôi sao che chở, ấm áp), "Phúc Tinh".
*   **Ngũ hành:** Mộc (dương Mộc).
*   **Đặc tính cốt lõi:** Thiện lương, che chở, giải ách, nguyên tắc, người thầy.

## 2. Đặc Điểm Tính Cách & Con Người

### Tâm Tính: "Ấm Áp & Thiện Lương"
*   **Bản chất:** Là sao chủ về sự thiện lương, nhân hậu. Người có Thiên Lương thủ mệnh thường có tâm địa tốt, hay thương người, thích làm việc thiện, giúp đỡ kẻ yếu.
*   **Tâm linh:** Có thiên hướng tìm hiểu về tâm linh, tín ngưỡng, tôn giáo. Thường chăm chỉ đi lễ bái, công quả.
*   **Phong thái:** Mang dáng dấp của một người thầy (giáo viên, cố vấn, quân sư). Thích lý luận, giảng giải, dạy bảo người khác.

### Lối Sống & Ứng Xử
*   **Sự đối lập (Nghịch lý Thiên Lương):**
    *   **Với gia đình nhỏ:** Rất cẩn thận, chi ly, tiết kiệm, chặt chẽ trong chi tiêu sinh hoạt hàng ngày.
    *   **Với xã hội/người thân:** Lại cực kỳ rộng rãi, hào phóng, không toan tính với anh em, bạn bè hoặc các hoạt động xã hội/từ thiện.
*   **Thái độ làm việc:** Chăm chỉ, chịu khó, cần mẫn. Không thích bon chen, tranh giành, đấu đá hay đố kỵ.

### Ngoại Hình
*   **Dáng vẻ:** Thư sinh, nho nhã, hiền lành.
*   **Đặc điểm:** Đôi khi nhìn gầy gò hoặc có nét "già dặn" trước tuổi (do suy nghĩ nhiều hoặc mang phong thái cụ non).

## 3. Cách Cục Đặc Biệt

### Thiên Lương cư Tý: "Phượng Lãm Cao Cương"
*   **Vị trí:** Thiên Lương ở cung Tý (Cung Ngọ xung chiếu thường có Thái Dương).
*   **Hình tượng:** Chim Phượng Hoàng đậu trên ngọn núi cao.
*   **Luận giải:**
    *   Vị trí đắc địa nhất của Thiên Lương.
    *   Chủ về sự thông minh xuất chúng, trí tuệ hơn người.
    *   Thường đạt được địa vị cao trong xã hội, đặc biệt là các lĩnh vực liên quan đến giáo dục, y tế, công tác xã hội hoặc tư vấn chiến lược.
    *   Được người đời nể trọng vì đức độ và tài năng.

## 4. Ứng Dụng Trong Luận Giải (Ghi Chú Kỹ Thuật)

### Keywords nhận diện (Dùng cho AI/Search):
*   `tam_tinh`: ["thiện lương", "hay giúp người", "thích tâm linh", "nguyên tắc"]
*   `nghe_nghiep`: ["giáo viên", "thầy thuốc", "cố vấn", "làm từ thiện", "giám sát"]
*   `uu_diem`: ["thông minh", "nhân hậu", "giải hạn tốt"]
*   `nhuoc_diem`: ["hay lo xa", "khắt khe với người nhà", "dễ bị lợi dụng lòng tốt"]

### Logic kiểm tra (Code Idea):
```python
def check_thien_luong_traits(chart):
    menh = chart.palaces['Mệnh']
    has_thien_luong = any(s.name == 'Thiên Lương' for s in menh.stars)
    
    if has_thien_luong:
        traits = ["thiện lương", "thích lý luận", "có duyên với tôn giáo"]
        
        # Check cách cục Phượng Lãm Cao Cương
        if menh.position == 'Tý': # Tý cung
            traits.append("Phượng Lãm Cao Cương - Thông minh xuất chúng")
            
        return traits
    return []
```
