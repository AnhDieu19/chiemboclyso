"""
Data Layer - Star Colors Mapping
Logic quy định màu sắc của sao dựa trên Ngũ Hành
"""

# Mapping Ngũ Hành sang mã màu (CSS classes hoặc Hex)
# Dựa trên yêu cầu của user:
# - Kim (Vàng): color-kim
# - Mộc (Xanh Lá): color-moc
# - Thủy (Đen/Xám): color-thuy
# - Hỏa (Đỏ): color-hoa
# - Thổ (Vàng/Nâu): color-tho (Thường gộp vào Kim nếu là quý tinh, hoặc Nâu)

ELEMENT_COLORS = {
    'Kim': '#f1c40f',    # Vàng (Gold) - Giữ nguyên hoặc chỉnh sáng hơn nếu cần
    'Mộc': '#2ecc71',    # Xanh lá (Emerald)
    'Thủy': '#7f8c8d',   # Xám (Concrete) - User request "Xám"
    'Hỏa': '#e74c3c',    # Đỏ (Alizarin)
    'Thổ': '#d35400',    # Nâu/Cam (Pumpkin)
}

CSS_CLASSES = {
    'Kim': 'star-kim',
    'Mộc': 'star-moc',
    'Thủy': 'star-thuy',
    'Hỏa': 'star-hoa',
    'Thổ': 'star-tho',
}

# Dữ liệu Ngũ Hành cho các sao (Chính Tinh + Phụ Tinh)
# Tổng hợp từ kiến thức Tử Vi Nam Phái
STAR_ELEMENTS = {
    # 1. CHÍNH TINH
    'Tử Vi': 'Thổ',
    'Thiên Cơ': 'Mộc',
    'Thái Dương': 'Hỏa',
    'Vũ Khúc': 'Kim',
    'Thiên Đồng': 'Thủy',
    'Liêm Trinh': 'Hỏa',
    'Thiên Phủ': 'Thổ',
    'Thái Âm': 'Thủy',
    'Tham Lang': 'Thủy', # Đới Mộc
    'Cự Môn': 'Thủy',
    'Thiên Tướng': 'Thủy',
    'Thiên Lương': 'Mộc', # Đới Thổ
    'Thất Sát': 'Kim', # Đới Hỏa
    'Phá Quân': 'Thủy', # Đới Kim

    # 2. LỤC CÁT TINH (Quý Tinh -> Thường Vàng/Thổ/Kim)
    'Văn Xương': 'Kim',
    'Văn Khúc': 'Thủy',
    'Tả Phụ': 'Thổ',
    'Hữu Bật': 'Thổ', 
    'Thiên Khôi': 'Hỏa', # Đới Kim -> Vàng/Đỏ (User: Vàng)
    'Thiên Việt': 'Hỏa', # Đới Kim -> Vàng/Đỏ (User: Vàng)
    
    # 3. LỤC SÁT TINH
    'Kinh Dương': 'Kim',
    'Đà La': 'Kim',
    'Địa Không': 'Hỏa',
    'Địa Kiếp': 'Hỏa',
    'Hỏa Tinh': 'Hỏa',
    'Linh Tinh': 'Hỏa',

    # 4. TỨ HÓA
    'Hóa Lộc': 'Mộc', # (User: Vàng/Xanh - Thường là Mộc, nhưng User nói Vàng nổi bật)
    'Hóa Quyền': 'Mộc', # (User: Vàng)
    'Hóa Khoa': 'Thủy', # (User: Vàng)
    'Hóa Kỵ': 'Thủy',   # (User: Đen/Thủy)

    # 5. VÒNG LỘC TỒN / BÁC SĨ
    'Lộc Tồn': 'Thổ',   # (User: Vàng)
    'Bác Sĩ': 'Thủy',
    'Lục Sĩ': 'Hỏa',
    'Thanh Long': 'Thủy',
    'Tiểu Hao': 'Hỏa',
    'Tướng Quân': 'Mộc',
    'Tàu Thu': 'Kim', # Tàu Thu ??
    'Tàu Thu': 'Kim',
    'Phi Liêm': 'Hỏa',
    'Hỷ Thần': 'Hỏa',
    'Bệnh Phù': 'Thổ',
    'Đại Hao': 'Hỏa', # (User: Đỏ)
    'Phúc Bình': 'Hỏa',
    'Quan Phủ': 'Hỏa',

    # 6. VÒNG THÁI TUẾ
    'Thái Tuế': 'Hỏa',
    'Thiếu Dương': 'Hỏa',
    'Tang Môn': 'Mộc',
    'Thiếu Âm': 'Thủy',
    'Quan Phù': 'Hỏa', # Trùng tên Quan Phủ? (Quan Phù/Quan Phủ phân biệt dấu)
    'Từ Phù': 'Kim',
    'Tuế Phá': 'Hỏa',
    'Long Đức': 'Thủy',
    'Bạch Hổ': 'Kim',
    'Phúc Đức': 'Thổ', # (Vòng Thái Tuế)
    'Điếu Khách': 'Hỏa',
    'Trực Phù': 'Kim',

    # 7. VÒNG TRƯỜNG SINH (Thường ít tô màu riêng, hoặc theo ngũ hành cục)
    'Trường Sinh': 'Thủy',
    'Mộc Dục': 'Thủy',
    'Quan Đới': 'Kim',
    'Lâm Quan': 'Kim',
    'Đế Vượng': 'Kim',
    'Suy': 'Thủy', # Thổ?
    'Bệnh': 'Hỏa', # ?
    'Tử': 'Hỏa',
    'Mộ': 'Thổ',
    'Tuyệt': 'Thổ',
    'Thai': 'Thổ',
    'Dưỡng': 'Mộc',

    # 8. CÁC SAO KHÁC
    'Thiên Mã': 'Hỏa',
    'Thiên Khốc': 'Thủy', # Đới Kim
    'Thiên Hư': 'Thủy',  # Đới Thổ
    'Đào Hoa': 'Mộc', # (User: Đỏ/Hỏa?) -> User nói Hỏa/Thủy đới Hỏa. Let's set Hỏa per user example.
    'Hồng Loan': 'Thủy', # User: Hỏa
    'Thiên Hỹ': 'Thủy', 
    'Thiên Hình': 'Kim', # Đới Hỏa -> Đỏ/Vàng? Thường là Đỏ (Hình phạt)
    'Thiên Riêu': 'Thủy',
    'Thiên Y': 'Thủy',
    'Thiên Giải': 'Hỏa',
    'Địa Giải': 'Thổ',
    'Giải Thần': 'Mộc', # ?
    'Thái Phụ': 'Kim', # Thổ/Kim
    'Phong Cáo': 'Thổ',
    'Thiên Tài': 'Thổ', # Mộc?
    'Thiên Thọ': 'Thổ',
    'Thiên Quan': 'Hỏa', # Vàng/Đỏ (Quý tinh)
    'Thiên Phúc': 'Thổ', # Vàng
    'Phúc Đức (ĐH)': 'Thổ', # (User requested rename)
    'Thiên Trù': 'Thổ',
    'Ân Quang': 'Mộc', # Vàng/Xanh (Quý tinh)
    'Thiên Quý': 'Thổ', # Vàng
    'Tam Thai': 'Thủy', # Thổ/Thủy
    'Bát Tọa': 'Mộc', # Thổ/Mộc
    'Cô Thần': 'Thổ',
    'Quả Tú': 'Thổ',
    'Đẩu Quân': 'Hỏa',
    'Thiên Thường': 'Thổ', # Hung tinh -> Đỏ?
    'Thiên Sứ': 'Thủy', # Hung tinh -> Đen?
    'Kiếp Sát': 'Hỏa',
    'Phá Toái': 'Hỏa', # Kim?
    'Lưu Hà': 'Thủy',
    'Thiên Đức': 'Hỏa', # Vàng (Đức tinh)
    'Nguyệt Đức': 'Hỏa', # Vàng
    'Long Trì': 'Thủy',
    'Phượng Các': 'Thổ', # Mộc/Thổ
    'Hoa Cái': 'Kim',
}

# Override User Preferences
USER_COLOR_OVERRIDES = {
    # Quý tinh -> Vàng
    'Thiên Khôi': 'Kim',
    'Thiên Việt': 'Kim',
    'Hóa Lộc': 'Kim',
    'Hóa Quyền': 'Kim',
    'Hóa Khoa': 'Kim',
    'Lộc Tồn': 'Kim',
    'Ân Quang': 'Kim',
    'Thiên Quý': 'Kim',
    'Thiên Quan': 'Kim',
    'Thiên Phúc': 'Kim',
    'Thiên Đức': 'Kim',
    'Nguyệt Đức': 'Kim',
    'Long Đức': 'Kim',
    'Phúc Đức': 'Kim',
    
    # Sát tinh/Hung tinh -> Đỏ (Hỏa)
    'Thiên Hình': 'Hỏa',
    'Kiếp Sát': 'Hỏa',
    'Địa Không': 'Hỏa',
    'Địa Kiếp': 'Hỏa',
    'Hỏa Tinh': 'Hỏa',
    'Linh Tinh': 'Hỏa',
    'Thiên Thường': 'Hỏa',
    
    # Đào hoa -> Đỏ
    'Đào Hoa': 'Hỏa',
    'Hồng Loan': 'Hỏa',
    
    # Ám tinh -> Đen (Thủy)
    'Hóa Kỵ': 'Thủy',
    'Thiên Riêu': 'Thủy',
    'Đà La': 'Thủy', # (Kim đới Thủy -> Đen cho tối?) -> User không specify Đà La. Keep default Kim or override? 
                     # Kinh Dương (Kim - Vàng/Trắng), Đà La (Kim - Xám/Đen?). Let's keep element base first.
}

def get_star_element(star_name: str) -> str:
    """Lấy ngũ hành của sao"""
    # Xử lý tên sao có thể có tiền tố/hậu tố
    # Ví dụ: "L.Thái Tuế", "Triệt 1"...
    clean_name = star_name
    
    # Logic override màu theo user preferences (ưu tiên trước)
    if clean_name in USER_COLOR_OVERRIDES:
        return {'Kim': 'Thổ', 'Hỏa': 'Hỏa', 'Thủy': 'Thủy', 'Mộc': 'Mộc', 'Thổ': 'Thổ'}[USER_COLOR_OVERRIDES[clean_name]] # Hacky mapping back to element if needed, or just return Color Code directly?
    
    # Fallback to dictionary
    return STAR_ELEMENTS.get(clean_name, 'Unknown')

def get_star_color(star_name: str) -> dict:
    """
    Lấy thông tin màu sắc cho sao
    Returns: { 'code': '#hex', 'class': 'css-class', 'element': 'Element' }
    """
    clean_name = star_name.replace('L.', '') # Handle Luu sao if needed
    
    # 1. Determine Effective Element (Ngũ hành hiển thị)
    if clean_name in USER_COLOR_OVERRIDES:
        eff_element = USER_COLOR_OVERRIDES[clean_name]
    else:
        eff_element = STAR_ELEMENTS.get(clean_name, 'Kim') # Default to Kim if unknown? Or Thủy?
    
    # 2. Map to Color
    return {
        'code': ELEMENT_COLORS.get(eff_element, '#7f8c8d'),
        'class': CSS_CLASSES.get(eff_element, 'star-unknown'),
        'element': eff_element
    }
