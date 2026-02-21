"""
Data Layer - Chính Tinh (14 Main Stars) Constants
"""

# 14 Chính Tinh (Main Stars)
CHINH_TINH = {
    # Vòng Tử Vi (đi ngược)
    'tu_vi_group': ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh'],
    # Vòng Thiên Phủ (đi thuận)
    'thien_phu_group': ['Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 'Thất Sát', 'Phá Quân']
}

# Khoảng cách của các sao trong vòng Tử Vi so với Tử Vi (đi ngược chiều kim đồng hồ)
TU_VI_GROUP_OFFSET = [0, -1, -3, -4, -5, -8]  # Tử, Cơ, (gap), Dương, Vũ, Đồng, (gap, gap), Liêm

# Khoảng cách của các sao trong vòng Thiên Phủ so với Thiên Phủ (đi thuận chiều kim đồng hồ)
# Phủ, Âm, Tham, Cự, Tướng, Lương, Sát, (gap, gap, gap), Phá
THIEN_PHU_GROUP_OFFSET = [0, 1, 2, 3, 4, 5, 6, 10]

# ═══════════════════════════════════════════════════════════════════════════════
# BẢNG TRA VỊ TRÍ TỬ VI - CHUẨN NAM PHÁI (FIXED)
# ═══════════════════════════════════════════════════════════════════════════════
# Công thức chính xác (from hocvienlyso.org):
# 1. Tìm 'a' (0 đến Cục-1) sao cho (Ngày + a) chia hết cho Cục
# 2. b = (Ngày + a) / Cục
# 3. Khởi từ Dần (index 2), đếm thuận b bước
# 4. Nếu 'a' Lẻ: lùi 'a' bước. Nếu 'a' Chẵn: tiến 'a' bước
#
# FIX DATE: 21/12/2025
# ═══════════════════════════════════════════════════════════════════════════════

def _calc_tuvi(cuc, day):
    """Helper to calculate Tu Vi position using Nam Phai formula"""
    remainder = day % cuc
    if remainder == 0:
        a = 0
    else:
        a = cuc - remainder
    b = (day + a) // cuc
    anchor = (2 + b - 1) % 12  # Dần = 2, đếm b bước
    if a % 2 == 1:  # Lẻ: lùi
        return (anchor - a + 12) % 12
    else:  # Chẵn: tiến
        return (anchor + a) % 12

# Generate tables programmatically using correct formula
TUVI_POSITION = {
    2: {d: _calc_tuvi(2, d) for d in range(1, 31)},  # Thủy Nhị Cục
    3: {d: _calc_tuvi(3, d) for d in range(1, 31)},  # Mộc Tam Cục
    4: {d: _calc_tuvi(4, d) for d in range(1, 31)},  # Kim Tứ Cục
    5: {d: _calc_tuvi(5, d) for d in range(1, 31)},  # Thổ Ngũ Cục
    6: {d: _calc_tuvi(6, d) for d in range(1, 31)},  # Hỏa Lục Cục
}

# Verify key test case: Day 13, Mộc 3 Cục -> Expected: 8 (Thân)
# _calc_tuvi(3, 13) = 8 ✓

# Bảng tra vị trí Thiên Phủ dựa trên vị trí Tử Vi
# Thiên Phủ đối xứng với Tử Vi qua trục Dần(2)-Thân(8)
# Formula: (2 + 8 - tuvi_pos) % 12 = (10 - tuvi_pos) % 12
# Or simplified: (16 - tuvi_pos) % 12
THIEN_PHU_POSITION = {
    0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 11, 6: 10, 7: 9, 8: 8, 9: 7, 10: 6, 11: 5
}
