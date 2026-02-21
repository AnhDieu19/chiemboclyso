"""
Data Layer - Vòng Trường Sinh (12 Stars Longevity Cycle) Constants
"""

# Vòng Trường Sinh - 12 sao theo Ngũ Hành Cục và Âm/Dương năm
TRUONG_SINH_STARS = [
    'Trường Sinh', 'Mộc Dục', 'Quan Đới', 'Lâm Quan', 'Đế Vượng', 
    'Suy', 'Bệnh', 'Tử', 'Mộ', 'Tuyệt', 'Thai', 'Dưỡng'
]

# Khởi điểm Trường Sinh theo Cục (Dương Nam/Âm Nữ đi thuận, Âm Nam/Dương Nữ đi nghịch)
TRUONG_SINH_BASE = {
    2: 8,   # Thủy Nhị Cục: khởi Thân
    3: 11,  # Mộc Tam Cục: khởi Hợi
    4: 5,   # Kim Tứ Cục: khởi Tỵ
    5: 8,   # Thổ Ngũ Cục: khởi Thân
    6: 2    # Hỏa Lục Cục: khởi Dần
}
