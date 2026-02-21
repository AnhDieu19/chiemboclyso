"""
Analytics Definitions
Define sets of stars for Beauty, Lucky (Sướng), and Tragic (Khổ) criteria.
Reference: Design Proposal
"""

# 1. Nhóm Sao Nhan Sắc (Beauty Archetypes)
BEAUTY_STARS = {
    "DAO_HONG": {"Đào Hoa", "Hồng Loan", "Thiên Hỹ"},
    "VAN_TINH": {"Văn Xương", "Văn Khúc"},
    "PHUC_THIEN": {"Thiên Phủ", "Thiên Tướng"}, # Cần check thêm miếu vượng trong logic
    "QUYEN_RU": {"Tham Lang", "Liêm Trinh"}, # Cần check đi cùng Đào/Hồng
    "THAI_AM": {"Thái Âm"} # Da trắng, khuôn trăng đầy đặn
}

# 2. Nhóm Sao May Mắn (Lucky - Sướng)
LUCKY_STARS = {
    "QUI_TINH": {"Thiên Khôi", "Thiên Việt", "Tả Phụ", "Hữu Bật", "Văn Xương", "Văn Khúc", "Hóa Khoa"},
    "TAI_TINH": {"Hóa Lộc", "Lộc Tồn", "Vũ Khúc"}, 
    "QUYEN_TINH": {"Hóa Quyền", "Tử Vi", "Thiên Phủ"}
}

# 3. Nhóm Sao Bạc Mệnh (Tragic - Khổ)
TRAGIC_STARS = {
    "KHONG_KIEP": {"Địa Không", "Địa Kiếp"},
    "AM_TINH": {"Hóa Kỵ", "Đà La", "Thiên Hình", "Cô Thần", "Quả Tú"},
    "SAC_DUC": {"Thiên Riêu", "Thai", "Mộc Dục"},
    "SAT_TINH_HANG_NANG": {"Kinh Dương", "Hỏa Tinh", "Linh Tinh", "Kiếp Sát"}
}
