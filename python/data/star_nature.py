"""
STAR NATURE CLASSIFICATION
Phân loại Cát Tinh (Good) và Hung Tinh (Bad) để hiển thị phân tách.
"""

# Các sao Xấu (Hung Tinh, Sát Tinh, Bại Tinh)
BAD_STARS = {
    # 1. Lục Sát
    'Kinh Dương', 'Đà La', 'Địa Không', 'Địa Kiếp', 'Hỏa Tinh', 'Linh Tinh',
    
    # 2. Vòng Thái Tuế (Các sao xấu)
    'Thái Tuế', 'Tang Môn', 'Bạch Hổ', 'Điếu Khách', 'Quan Phù', 'Tuế Phá',
    
    # 3. Vòng Lộc Tồn (Các sao xấu)
    'Tiểu Hao', 'Đại Hao', 'Bệnh Phù', 'Từ Phù', 'Phúc Bình', 'Phi Liêm', 
    
    # 4. Sao xấu khác (Hình, Riêu, Không, Kiếp...)
    'Thiên Hình', 'Thiên Riêu', 'Kiếp Sát', 'Đà La', 'Thiên Không',
    'Thiên Khốc', 'Thiên Hư', 'Thiên Thường', 'Thiên Sứ',
    'Cô Thần', 'Quả Tú', 'Phá Toái', 'Lưu Hà', 'Âm Sát',
    'Trực Phù',
    # Lưu sao xấu
    'L.Thái Tuế', 'L.Kinh Dương', 'L.Đà La', 'L.Bạch Hổ', 'L.Tang Môn', 'L.Khốc', 'L.Hư'
}

# Các sao Tốt (Cát Tinh, Quý Tinh) - Dùng để tham chiếu nếu cần
# Thực tế logic sẽ là: Nếu trong Bad -> Bad, ngược lại là Good (trừ Chính Tinh)
GOOD_STARS = {
    # Lục Cát
    'Tả Phụ', 'Hữu Bật', 'Văn Xương', 'Văn Khúc', 'Thiên Khôi', 'Thiên Việt',
    
    # Tứ Hóa
    'Hóa Lộc', 'Hóa Quyền', 'Hóa Khoa', # Hóa Kỵ thường coi là xấu, nhưng tuỳ context
    
    # Khác
    'Lộc Tồn', 'Thiên Mã', 'Thiên Quan', 'Thiên Phúc', 'Thiên Thọ', 'Thiên Tài',
    'Ân Quang', 'Thiên Quý', 'Tam Thai', 'Bát Tọa', 'Phong Cáo', 'Quốc Ấn', 'Đường Phù',
    'Thiên Hỹ', 'Hỷ Thần', 'Thiên Trù', 'Đào Hoa', 'Hồng Loan', 
    'Long Trì', 'Phượng Các', 'Thiên Giải', 'Địa Giải', 'Giải Thần',
    'Thiên Đức', 'Nguyệt Đức', 'Phúc Đức', 'Long Đức', 'Thiếu Dương', 'Thiếu Âm',
    'Thanh Long', 'Lực Sĩ', 'Tướng Quân', # Tướng Quân lưỡng tính, tạm cho tốt
    'Tràng Sinh', 'Mộc Dục', 'Quan Đới', 'Lâm Quan', 'Đế Vượng', 'Thai', 'Dưỡng'
}

# Hóa Kỵ là trường hợp đặc biệt, thường xếp vào Hung tinh
BAD_STARS.add('Hóa Kỵ')

def classify_star(star_name: str) -> str:
    """
    Phân loại sao: 'good', 'bad', hoặc 'neutral'
    """
    if star_name in BAD_STARS:
        return 'bad'
    # Check if star starts with L. (Lưu) and base name is bad
    if star_name.startswith('L.') and star_name[2:] in BAD_STARS:
        return 'bad'
        
    return 'good'
