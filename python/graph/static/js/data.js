/**
 * Tu Vi Knowledge Graph - Data
 * Đầy đủ 118+ sao với phân loại Cát (+) / Hung (-) / Trung tính
 */

const TUVI_GRAPH_DATA = {
    // ═══════════════════════════════════════════════════════════════════════════
    // CẤU HÌNH MÀU SẮC CHO TỪNG LỚP
    // ═══════════════════════════════════════════════════════════════════════════
    // ═══════════════════════════════════════════════════════════════════════════
    // NODES - Đầy đủ 118+ sao
    // nature: "cat" (+), "hung" (-), "trung" (neutral)
    // ═══════════════════════════════════════════════════════════════════════════

    nodes: [
        // ─────────────────────────────────────────────────────────────────────
        // NGŨ HÀNH (5)
        // ─────────────────────────────────────────────────────────────────────
        { id: "Kim", type: "ngu_hanh", nature: "trung", size: 40, desc: "Kim - Kim loại, chủ quyết đoán, cứng rắn" },
        { id: "Mộc", type: "ngu_hanh", nature: "trung", size: 40, desc: "Mộc - Cây cối, chủ sinh trưởng, nhân từ" },
        { id: "Thủy", type: "ngu_hanh", nature: "trung", size: 40, desc: "Thủy - Nước, chủ trí tuệ, linh hoạt" },
        { id: "Hỏa", type: "ngu_hanh", nature: "trung", size: 40, desc: "Hỏa - Lửa, chủ nhiệt huyết, lễ nghĩa" },
        { id: "Thổ", type: "ngu_hanh", nature: "trung", size: 40, desc: "Thổ - Đất, chủ ổn định, trung tín" },

        // ─────────────────────────────────────────────────────────────────────
        // THIÊN CAN (10)
        // ─────────────────────────────────────────────────────────────────────
        { id: "Giáp", type: "thien_can", nature: "trung", size: 22, hanh: "Mộc", desc: "Giáp - Dương Mộc" },
        { id: "Ất", type: "thien_can", nature: "trung", size: 22, hanh: "Mộc", desc: "Ất - Âm Mộc" },
        { id: "Bính", type: "thien_can", nature: "trung", size: 22, hanh: "Hỏa", desc: "Bính - Dương Hỏa" },
        { id: "Đinh", type: "thien_can", nature: "trung", size: 22, hanh: "Hỏa", desc: "Đinh - Âm Hỏa" },
        { id: "Mậu", type: "thien_can", nature: "trung", size: 22, hanh: "Thổ", desc: "Mậu - Dương Thổ" },
        { id: "Kỷ", type: "thien_can", nature: "trung", size: 22, hanh: "Thổ", desc: "Kỷ - Âm Thổ" },
        { id: "Canh", type: "thien_can", nature: "trung", size: 22, hanh: "Kim", desc: "Canh - Dương Kim" },
        { id: "Tân", type: "thien_can", nature: "trung", size: 22, hanh: "Kim", desc: "Tân - Âm Kim" },
        { id: "Nhâm", type: "thien_can", nature: "trung", size: 22, hanh: "Thủy", desc: "Nhâm - Dương Thủy" },
        { id: "Quý", type: "thien_can", nature: "trung", size: 22, hanh: "Thủy", desc: "Quý - Âm Thủy" },

        // ─────────────────────────────────────────────────────────────────────
        // ĐỊA CHI (12)
        // ─────────────────────────────────────────────────────────────────────
        { id: "Tý", type: "dia_chi", nature: "trung", size: 24, hanh: "Thủy", desc: "Tý - Chuột, hướng Bắc" },
        { id: "Sửu", type: "dia_chi", nature: "trung", size: 24, hanh: "Thổ", desc: "Sửu - Trâu, Đông Bắc" },
        { id: "Dần", type: "dia_chi", nature: "trung", size: 24, hanh: "Mộc", desc: "Dần - Hổ, hướng Đông" },
        { id: "Mão", type: "dia_chi", nature: "trung", size: 24, hanh: "Mộc", desc: "Mão - Mèo, hướng Đông" },
        { id: "Thìn", type: "dia_chi", nature: "trung", size: 24, hanh: "Thổ", desc: "Thìn - Rồng, Đông Nam" },
        { id: "Tỵ", type: "dia_chi", nature: "trung", size: 24, hanh: "Hỏa", desc: "Tỵ - Rắn, hướng Nam" },
        { id: "Ngọ", type: "dia_chi", nature: "trung", size: 24, hanh: "Hỏa", desc: "Ngọ - Ngựa, hướng Nam" },
        { id: "Mùi", type: "dia_chi", nature: "trung", size: 24, hanh: "Thổ", desc: "Mùi - Dê, Tây Nam" },
        { id: "Thân", type: "dia_chi", nature: "trung", size: 24, hanh: "Kim", desc: "Thân - Khỉ, hướng Tây" },
        { id: "Dậu", type: "dia_chi", nature: "trung", size: 24, hanh: "Kim", desc: "Dậu - Gà, hướng Tây" },
        { id: "Tuất", type: "dia_chi", nature: "trung", size: 24, hanh: "Thổ", desc: "Tuất - Chó, Tây Bắc" },
        { id: "Hợi", type: "dia_chi", nature: "trung", size: 24, hanh: "Thủy", desc: "Hợi - Lợn, hướng Bắc" },

        // ─────────────────────────────────────────────────────────────────────
        // CHÍNH TINH - VÒNG TỬ VI (6) 
        // ─────────────────────────────────────────────────────────────────────
        { id: "Tử Vi", type: "chinh_tinh_tuvi", nature: "cat", size: 32, hanh: "Thổ", desc: "Đế tinh - Sao vua, chủ quyền quý cao sang" },
        { id: "Thiên Cơ", type: "chinh_tinh_tuvi", nature: "cat", size: 28, hanh: "Mộc", desc: "Mưu tinh - Chủ mưu trí, linh hoạt, cơ biến" },
        { id: "Thái Dương", type: "chinh_tinh_tuvi", nature: "cat", size: 28, hanh: "Hỏa", desc: "Phụ tinh - Mặt trời, chủ quang minh chính đại" },
        { id: "Vũ Khúc", type: "chinh_tinh_tuvi", nature: "cat", size: 28, hanh: "Kim", desc: "Tài tinh - Chủ tiền bạc, quyết đoán, cứng rắn" },
        { id: "Thiên Đồng", type: "chinh_tinh_tuvi", nature: "cat", size: 28, hanh: "Thủy", desc: "Phúc tinh - Chủ phúc lộc, an nhàn, trẻ trung" },
        { id: "Liêm Trinh", type: "chinh_tinh_tuvi", nature: "trung", size: 28, hanh: "Hỏa", desc: "Tù tinh - Chủ pháp luật, chính trực, cô đơn" },

        // ─────────────────────────────────────────────────────────────────────
        // CHÍNH TINH - VÒNG THIÊN PHỦ (8)
        // ─────────────────────────────────────────────────────────────────────
        { id: "Thiên Phủ", type: "chinh_tinh_phu", nature: "cat", size: 32, hanh: "Thổ", desc: "Tài khố - Chủ tích trữ, bảo quản tài sản" },
        { id: "Thái Âm", type: "chinh_tinh_phu", nature: "cat", size: 28, hanh: "Thủy", desc: "Mẫu tinh - Mặt trăng, chủ nữ tính, ôn hòa" },
        { id: "Tham Lang", type: "chinh_tinh_phu", nature: "trung", size: 28, hanh: "Thủy", desc: "Đào hoa tinh - Chủ sắc đẹp, ham muốn, đa tài" },
        { id: "Cự Môn", type: "chinh_tinh_phu", nature: "hung", size: 28, hanh: "Thủy", desc: "Ám tinh - Chủ khẩu thiệt thị phi, tranh cãi" },
        { id: "Thiên Tướng", type: "chinh_tinh_phu", nature: "cat", size: 28, hanh: "Thủy", desc: "Ấn tinh - Chủ uy tín, danh dự, quý nhân" },
        { id: "Thiên Lương", type: "chinh_tinh_phu", nature: "cat", size: 28, hanh: "Mộc", desc: "Phúc thọ tinh - Chủ phúc đức, thọ mệnh" },
        { id: "Thất Sát", type: "chinh_tinh_phu", nature: "trung", size: 28, hanh: "Kim", desc: "Sát tinh - Chủ quyền lực, cương quyết, sát khí" },
        { id: "Phá Quân", type: "chinh_tinh_phu", nature: "hung", size: 28, hanh: "Thủy", desc: "Hao tinh - Chủ phá bỏ, đổi mới, mạo hiểm" },

        // ─────────────────────────────────────────────────────────────────────
        // LỤC CÁT TINH (6) - TỐT
        // ─────────────────────────────────────────────────────────────────────
        { id: "Tả Phụ", type: "luc_cat", nature: "cat", size: 24, hanh: "Thổ", desc: "Quý nhân bên trái, chủ giúp đỡ, phò tá" },
        { id: "Hữu Bật", type: "luc_cat", nature: "cat", size: 24, hanh: "Thủy", desc: "Quý nhân bên phải, chủ hỗ trợ, bổ sung" },
        { id: "Văn Xương", type: "luc_cat", nature: "cat", size: 24, hanh: "Kim", desc: "Văn tinh - Chủ văn chương, học vấn, khoa bảng" },
        { id: "Văn Khúc", type: "luc_cat", nature: "cat", size: 24, hanh: "Thủy", desc: "Văn tinh - Chủ nghệ thuật, âm nhạc, tài hoa" },
        // ─────────────────────────────────────────────────────────────────────
        // TẠP TINH QUAN TRỌNG (Chọn lọc)
        // ─────────────────────────────────────────────────────────────────────
        { id: "Lộc Tồn", type: "tap_tinh", nature: "cat", size: 22, hanh: "Thổ", desc: "Đại cát - Chủ tài lộc bền vững" },
        { id: "Thiên Mã", type: "tap_tinh", nature: "cat", size: 20, hanh: "Hỏa", desc: "Cát - Chủ di chuyển, thăng tiến" },
        { id: "Đào Hoa", type: "tap_tinh", nature: "trung", size: 20, hanh: "Thủy", desc: "Trung - Chủ sắc đẹp, nhân duyên" },
        { id: "Hồng Loan", type: "tap_tinh", nature: "cat", size: 20, hanh: "Thủy", desc: "Cát - Chủ hôn nhân, hỷ sự" },
        { id: "Thiên Hỹ", type: "tap_tinh", nature: "cat", size: 20, hanh: "Thủy", desc: "Cát - Chủ vui mừng, thai nghén" },
        { id: "Thiên Khôi", type: "luc_cat", nature: "cat", size: 24, hanh: "Hỏa", desc: "Quý tinh dương - Chủ quý nhân nam giới" },
        { id: "Thiên Việt", type: "luc_cat", nature: "cat", size: 24, hanh: "Hỏa", desc: "Quý tinh âm - Chủ quý nhân nữ giới" },

        // ─────────────────────────────────────────────────────────────────────
        // LỤC SÁT TINH (6) - XẤU
        // ─────────────────────────────────────────────────────────────────────
        { id: "Kinh Dương", type: "luc_sat", nature: "hung", size: 24, hanh: "Kim", desc: "Hung tinh - Chủ xung đột, bạo lực, tai nạn" },
        { id: "Đà La", type: "luc_sat", nature: "hung", size: 24, hanh: "Kim", desc: "Hung tinh - Chủ trì hoãn, cản trở, thị phi" },
        { id: "Hỏa Tinh", type: "luc_sat", nature: "hung", size: 24, hanh: "Hỏa", desc: "Hung tinh - Chủ nóng nảy, tai họa, cháy nổ" },
        { id: "Linh Tinh", type: "luc_sat", nature: "hung", size: 24, hanh: "Hỏa", desc: "Hung tinh - Chủ âm thầm, thất bại, cô độc" },
        { id: "Địa Không", type: "luc_sat", nature: "hung", size: 24, hanh: "Hỏa", desc: "Không vong - Chủ mất mát, phá tán, hư vô" },
        { id: "Địa Kiếp", type: "luc_sat", nature: "hung", size: 24, hanh: "Hỏa", desc: "Kiếp số - Chủ kiếp nạn, cướp đoạt, phá hại" },

        // ─────────────────────────────────────────────────────────────────────
        // TỨ HÓA (4)
        // ─────────────────────────────────────────────────────────────────────
        { id: "Hóa Lộc", type: "tu_hoa", nature: "cat", size: 22, desc: "Chủ tài lộc, may mắn, phát triển" },
        { id: "Hóa Quyền", type: "tu_hoa", nature: "cat", size: 22, desc: "Chủ quyền lực, thăng tiến, thành công" },
        { id: "Hóa Khoa", type: "tu_hoa", nature: "cat", size: 22, desc: "Chủ danh tiếng, học vấn, uy tín" },
        { id: "Hóa Kỵ", type: "tu_hoa", nature: "hung", size: 22, desc: "Chủ cản trở, thị phi, khó khăn" },

        { id: "Tuần", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Tuần Trung Không Vong" },
        { id: "Triệt", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Triệt Lộ Không Vong" },
        { id: "Thiên Hình", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ hình phạt, tù tội" },
        { id: "Thiên Riêu", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ đào hoa xấu, bệnh tình" },
        { id: "Cô Thần", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ cô đơn nam" },
        { id: "Quả Tú", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ cô đơn nữ" },
        { id: "Thiên Không", type: "tap_tinh", nature: "trung", size: 18, desc: "Trung - Chủ không vong, tu hành" },
        { id: "Kiếp Sát", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ tai họa, kiếp nạn" },
        { id: "Phá Toái", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ phá hoại, tan vỡ" },
        { id: "Hoa Cái", type: "tap_tinh", nature: "trung", size: 18, desc: "Trung - Chủ cô độc, tài nghệ" },
        
        // Tạp tinh bổ sung
        { id: "Thiên La", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Lưới trời, cản trở, giam hãm (cố định tại Thìn)" },
        { id: "Địa Võng", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Lưới đất, cản trở, giam hãm (cố định tại Tuất)" },
        { id: "Thiên Thường", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ thương tích, tổn hại" },
        { id: "Thiên Sứ", type: "tap_tinh", nature: "trung", size: 18, desc: "Trung - Sứ giả trời, biến động" },
        { id: "Thiên Đức", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ phúc đức, quý nhân" },
        { id: "Nguyệt Đức", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ phúc đức, quý nhân nữ" },
        { id: "Long Đức", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ phúc lộc, quý nhân" },
        { id: "Thiên Giải", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Giải trừ hung tinh" },
        { id: "Địa Giải", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Giải trừ hung tinh" },
        { id: "Thiên Quan", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ quan lộc" },
        { id: "Thiên Phúc", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ phúc lộc" },
        { id: "Thiên Tài", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ tài năng" },
        { id: "Thiên Thọ", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ thọ mệnh" },
        { id: "Thái Phụ", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ quý nhân phụ trợ" },
        { id: "Phong Cáo", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ thăng quan, phong thưởng" },
        { id: "Ân Quang", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ ân sủng, quý nhân" },
        { id: "Thiên Quý", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ quý nhân, danh tiếng" },
        { id: "Tam Thai", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ văn chương, học vấn" },
        { id: "Bát Tọa", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ văn chương, học vấn" },
        { id: "Thiên Khốc", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ khóc lóc, tang chế" },
        { id: "Thiên Hư", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ hư hao, mất mát" },
        { id: "Thiên Y", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ y học, chữa bệnh" },
        { id: "Phúc Bình", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ tiểu nhân, phục kích" },
        { id: "Quan Phủ", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ quan tụng, kiện cáo" },
        
        // Vòng Trường Sinh (12 sao)
        { id: "Trường Sinh", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Bắt đầu cuộc sống" },
        { id: "Mộc Dục", type: "tap_tinh", nature: "trung", size: 18, desc: "Trung - Tắm gội, đào hoa" },
        { id: "Quan Đới", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Đội mũ, thành đạt" },
        { id: "Lâm Quan", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Làm quan, thăng tiến" },
        { id: "Đế Vượng", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Vượng nhất, cực thịnh" },
        { id: "Suy", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Suy yếu, thoái hóa" },
        { id: "Bệnh", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Bệnh tật, ốm đau" },
        { id: "Tử", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chết, kết thúc" },
        { id: "Mộ", type: "tap_tinh", nature: "trung", size: 18, desc: "Trung - Chôn cất, tích trữ" },
        { id: "Tuyệt", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Tuyệt diệt, hết sạch" },
        { id: "Thai", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Thai nghén, bắt đầu mới" },
        { id: "Dưỡng", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Nuôi dưỡng, chuẩn bị" },
        
        // Vòng Thái Tuế (12 sao)
        { id: "Thái Tuế", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ tinh năm, quan tụng" },
        { id: "Thiếu Dương", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ hỷ khánh, may mắn" },
        { id: "Tang Môn", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ tang chế, buồn rầu" },
        { id: "Thiếu Âm", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ bệnh tật, tiểu nhân" },
        { id: "Quan Phù", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ quan tụng, kiện cáo" },
        { id: "Từ Phù", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ bệnh tật, tử vong" },
        { id: "Tuế Phá", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ phá hại, tổn thất" },
        { id: "Long Đức", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ phúc lộc, quý nhân" },
        { id: "Bạch Hổ", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ tang chế, tai nạn" },
        { id: "Phúc Đức", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ phúc lộc, may mắn" },
        { id: "Điếu Khách", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ tang chế, buồn rầu" },
        { id: "Trực Phù", type: "tap_tinh", nature: "trung", size: 18, desc: "Trung - Chủ biến động" },
        
        // Vòng Bác Sĩ (12 sao)
        { id: "Bác Sĩ", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ thông minh, học vấn" },
        { id: "Lục Sĩ", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ sức mạnh, quyền lực" },
        { id: "Thanh Long", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ hỷ sự, may mắn" },
        { id: "Tiểu Hao", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ hao tài nhỏ" },
        { id: "Tướng Quân", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ xung đột, tranh chấp" },
        { id: "Tàu Thu", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ văn thư, thi cử" },
        { id: "Phi Liêm", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ thị phi, tai tiếng" },
        { id: "Hỷ Thần", type: "tap_tinh", nature: "cat", size: 18, desc: "Cát - Chủ hỷ sự, vui mừng" },
        { id: "Bệnh Phù", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ bệnh tật" },
        { id: "Đại Hao", type: "tap_tinh", nature: "hung", size: 18, desc: "Hung - Chủ hao tài lớn" },

        // 12 CUNG đã được hiển thị trong bàn cờ, không cần node riêng
    ],

    // ═══════════════════════════════════════════════════════════════════════════
    // LINKS - MỐI QUAN HỆ
    // ═══════════════════════════════════════════════════════════════════════════
    links: [
        // Ngũ Hành Tương Sinh
        { source: "Kim", target: "Thủy", relation: "sinh" },
        { source: "Thủy", target: "Mộc", relation: "sinh" },
        { source: "Mộc", target: "Hỏa", relation: "sinh" },
        { source: "Hỏa", target: "Thổ", relation: "sinh" },
        { source: "Thổ", target: "Kim", relation: "sinh" },

        // Ngũ Hành Tương Khắc
        { source: "Kim", target: "Mộc", relation: "khac" },
        { source: "Mộc", target: "Thổ", relation: "khac" },
        { source: "Thổ", target: "Thủy", relation: "khac" },
        { source: "Thủy", target: "Hỏa", relation: "khac" },
        { source: "Hỏa", target: "Kim", relation: "khac" },

        // Thiên Can -> Ngũ Hành
        { source: "Giáp", target: "Mộc", relation: "thuoc" },
        { source: "Ất", target: "Mộc", relation: "thuoc" },
        { source: "Bính", target: "Hỏa", relation: "thuoc" },
        { source: "Đinh", target: "Hỏa", relation: "thuoc" },
        { source: "Mậu", target: "Thổ", relation: "thuoc" },
        { source: "Kỷ", target: "Thổ", relation: "thuoc" },
        { source: "Canh", target: "Kim", relation: "thuoc" },
        { source: "Tân", target: "Kim", relation: "thuoc" },
        { source: "Nhâm", target: "Thủy", relation: "thuoc" },
        { source: "Quý", target: "Thủy", relation: "thuoc" },

        // Địa Chi -> Ngũ Hành
        { source: "Tý", target: "Thủy", relation: "thuoc" },
        { source: "Sửu", target: "Thổ", relation: "thuoc" },
        { source: "Dần", target: "Mộc", relation: "thuoc" },
        { source: "Mão", target: "Mộc", relation: "thuoc" },
        { source: "Thìn", target: "Thổ", relation: "thuoc" },
        { source: "Tỵ", target: "Hỏa", relation: "thuoc" },
        { source: "Ngọ", target: "Hỏa", relation: "thuoc" },
        { source: "Mùi", target: "Thổ", relation: "thuoc" },
        { source: "Thân", target: "Kim", relation: "thuoc" },
        { source: "Dậu", target: "Kim", relation: "thuoc" },
        { source: "Tuất", target: "Thổ", relation: "thuoc" },
        { source: "Hợi", target: "Thủy", relation: "thuoc" },

        // Chính Tinh -> Ngũ Hành
        { source: "Tử Vi", target: "Thổ", relation: "thuoc" },
        { source: "Thiên Cơ", target: "Mộc", relation: "thuoc" },
        { source: "Thái Dương", target: "Hỏa", relation: "thuoc" },
        { source: "Vũ Khúc", target: "Kim", relation: "thuoc" },
        { source: "Thiên Đồng", target: "Thủy", relation: "thuoc" },
        { source: "Liêm Trinh", target: "Hỏa", relation: "thuoc" },
        { source: "Thiên Phủ", target: "Thổ", relation: "thuoc" },
        { source: "Thái Âm", target: "Thủy", relation: "thuoc" },
        { source: "Tham Lang", target: "Thủy", relation: "thuoc" },
        { source: "Cự Môn", target: "Thủy", relation: "thuoc" },
        { source: "Thiên Tướng", target: "Thủy", relation: "thuoc" },
        { source: "Thiên Lương", target: "Mộc", relation: "thuoc" },
        { source: "Thất Sát", target: "Kim", relation: "thuoc" },
        { source: "Phá Quân", target: "Thủy", relation: "thuoc" },

        // Vòng Tử Vi
        { source: "Tử Vi", target: "Thiên Cơ", relation: "vong" },
        { source: "Thiên Cơ", target: "Thái Dương", relation: "vong" },
        { source: "Thái Dương", target: "Vũ Khúc", relation: "vong" },
        { source: "Vũ Khúc", target: "Thiên Đồng", relation: "vong" },
        { source: "Thiên Đồng", target: "Liêm Trinh", relation: "vong" },

        // Vòng Thiên Phủ
        { source: "Thiên Phủ", target: "Thái Âm", relation: "vong" },
        { source: "Thái Âm", target: "Tham Lang", relation: "vong" },
        { source: "Tham Lang", target: "Cự Môn", relation: "vong" },
        { source: "Cự Môn", target: "Thiên Tướng", relation: "vong" },
        { source: "Thiên Tướng", target: "Thiên Lương", relation: "vong" },
        { source: "Thiên Lương", target: "Thất Sát", relation: "vong" },
        { source: "Thất Sát", target: "Phá Quân", relation: "vong" },

        // Đồng hành (cùng nhóm)
        { source: "Tả Phụ", target: "Hữu Bật", relation: "dong_hanh" },
        { source: "Văn Xương", target: "Văn Khúc", relation: "dong_hanh" },
        { source: "Thiên Khôi", target: "Thiên Việt", relation: "dong_hanh" },
        { source: "Kinh Dương", target: "Đà La", relation: "dong_hanh" },
        { source: "Hỏa Tinh", target: "Linh Tinh", relation: "dong_hanh" },
        { source: "Địa Không", target: "Địa Kiếp", relation: "dong_hanh" },
        { source: "Hóa Lộc", target: "Hóa Quyền", relation: "dong_hanh" },
        { source: "Hóa Quyền", target: "Hóa Khoa", relation: "dong_hanh" },
        { source: "Tuần", target: "Triệt", relation: "dong_hanh" },
        { source: "Cô Thần", target: "Quả Tú", relation: "dong_hanh" },

        // Lục Cát Tinh -> Ngũ Hành
        { source: "Tả Phụ", target: "Thổ", relation: "thuoc" },
        { source: "Hữu Bật", target: "Thủy", relation: "thuoc" },
        { source: "Văn Xương", target: "Kim", relation: "thuoc" },
        { source: "Văn Khúc", target: "Thủy", relation: "thuoc" },
        { source: "Thiên Khôi", target: "Hỏa", relation: "thuoc" },
        { source: "Thiên Việt", target: "Hỏa", relation: "thuoc" },

        // Lục Sát Tinh -> Ngũ Hành
        { source: "Kinh Dương", target: "Kim", relation: "thuoc" },
        { source: "Đà La", target: "Kim", relation: "thuoc" },
        { source: "Hỏa Tinh", target: "Hỏa", relation: "thuoc" },
        { source: "Linh Tinh", target: "Hỏa", relation: "thuoc" },
        { source: "Địa Không", target: "Hỏa", relation: "thuoc" },
        { source: "Địa Kiếp", target: "Hỏa", relation: "thuoc" },

        // Tứ Hóa -> Tính chất (Tạm thời nối vào các Hành tiêu biểu hoặc giữ nhóm)
        // Hóa Lộc (Mộc/Thổ), Hóa Quyền (Mộc/Hỏa), Hóa Khoa (Thủy/Mộc), Hóa Kỵ (Thủy)
        { source: "Hóa Lộc", target: "Mộc", relation: "thuoc" },
        { source: "Hóa Quyền", target: "Hỏa", relation: "thuoc" },
        { source: "Hóa Khoa", target: "Thủy", relation: "thuoc" },
        { source: "Hóa Kỵ", target: "Thủy", relation: "thuoc" },

        // Tạp Tinh quan trọng -> Ngũ Hành
        { source: "Lộc Tồn", target: "Thổ", relation: "thuoc" },
        { source: "Thiên Mã", target: "Hỏa", relation: "thuoc" },
        { source: "Đào Hoa", target: "Mộc", relation: "thuoc" },
        { source: "Hồng Loan", target: "Thủy", relation: "thuoc" },
        { source: "Thiên Hỹ", target: "Thủy", relation: "thuoc" },

        { source: "Thiên Hình", target: "Hỏa", relation: "thuoc" }, // Hình (Kim đới Hỏa)
        { source: "Thiên Riêu", target: "Thủy", relation: "thuoc" },
        { source: "Kiếp Sát", target: "Hỏa", relation: "thuoc" },
        { source: "Cô Thần", target: "Thổ", relation: "thuoc" },
        { source: "Quả Tú", target: "Thổ", relation: "thuoc" },
        { source: "Phá Toái", target: "Hỏa", relation: "thuoc" }, // Hỏa đới Kim
        { source: "Hoa Cái", target: "Kim", relation: "thuoc" },

        // Vòng Thái Tuế (đại diện)
        // { source: "Thái Tuế", target: "Hỏa", relation: "thuoc" },
        // { source: "Bạch Hổ", target: "Kim", relation: "thuoc" },
        // { source: "Quan Phù", target: "Hỏa", relation: "thuoc" },
        // { source: "Tang Môn", target: "Mộc", relation: "thuoc" }, // Mộc đới Thổ
        // { source: "Điếu Khách", target: "Hỏa", relation: "thuoc" },

        // Vòng Trường Sinh (đại diện)
        // { source: "Trường Sinh", target: "Thủy", relation: "thuoc" },
        // { source: "Đế Vượng", target: "Kim", relation: "thuoc" },
        // { source: "Mộ", target: "Thổ", relation: "thuoc" },
        // { source: "Tuyệt", target: "Thổ", relation: "thuoc" },

        // Vòng Bác Sĩ (đại diện)
        // { source: "Bác Sĩ", target: "Thủy", relation: "thuoc" },
        // { source: "Lục Sĩ", target: "Hỏa", relation: "thuoc" },
        // { source: "Tướng Quân", target: "Mộc", relation: "thuoc" },
        // { source: "Tiểu Hao", target: "Hỏa", relation: "thuoc" },
        // { source: "Đại Hao", target: "Hỏa", relation: "thuoc" },
    ]
};

// Export for use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = TUVI_GRAPH_DATA;
}
