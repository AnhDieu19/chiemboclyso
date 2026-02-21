"""
╔══════════════════════════════════════════════════════════════════════════════╗
║               CUNG MỆNH & CUNG THÂN CALCULATIONS                             ║
║               Tính Cung Mệnh và Cung Thân                                    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Purpose: Xác định vị trí Cung Mệnh và Cung Thân trên lá số Tử Vi           ║
╚══════════════════════════════════════════════════════════════════════════════╝

ĐỊNH NGHĨA:
===========
- CUNG MỆNH: Cung khởi đầu, đại diện cho bản mệnh, tính cách, số phận tổng quát
- CUNG THÂN: Cung đối chiếu, ảnh hưởng đến vận mệnh nửa đời sau

CÔNG THỨC AN CUNG MỆNH:
=======================
Khẩu quyết: "Chính nguyệt khởi Dần thuận hành tý, nghịch hành giờ sinh"
1. Bắt đầu từ cung Dần (index 2)
2. Thuận theo tháng: đếm tiến (tháng - 1) cung
3. Nghịch theo giờ: đếm lùi (giờ) cung

Công thức: Cung Mệnh = (2 + tháng - 1 - giờ) mod 12

CÔNG THỨC AN CUNG THÂN:
=======================
Khẩu quyết: "Chính nguyệt khởi Dần thuận hành tý, thuận hành giờ sinh"
1. Bắt đầu từ cung Dần (index 2)
2. Thuận theo tháng: đếm tiến (tháng - 1) cung
3. Thuận theo giờ: đếm tiến (giờ) cung

Công thức: Cung Thân = (2 + tháng - 1 + giờ) mod 12

VÍ DỤ:
======
Sinh tháng 2 Âm lịch, giờ Mão (index 3):
- Cung Mệnh = (2 + 2 - 1 - 3) mod 12 = 0 (Tý)
- Cung Thân = (2 + 2 - 1 + 3) mod 12 = 6 (Ngọ)
"""

from data import DIA_CHI


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH CUNG MỆNH
# Công thức: (2 + tháng - 1 - giờ) mod 12
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_cung_menh(lunar_month: int, hour_index: int) -> int:
    """
    Tính vị trí Cung Mệnh
    
    KHẨU QUYẾT:
    "Chính nguyệt khởi Dần, thuận đếm theo tháng, nghịch đếm theo giờ"
    
    CÔNG THỨC:
    Cung Mệnh = (Dần + tháng - 1 - giờ) mod 12
              = (2 + lunar_month - 1 - hour_index) mod 12
    
    BẢNG VÍ DỤ (Tháng 1):
    ┌─────────┬──────────────────┐
    │ Giờ     │ Cung Mệnh        │
    ├─────────┼──────────────────┤
    │ Tý (0)  │ (2+0-0)=2 → Dần  │
    │ Sửu (1) │ (2+0-1)=1 → Sửu  │
    │ Dần (2) │ (2+0-2)=0 → Tý   │
    │ Mão (3) │ (2+0-3)=11→ Hợi  │
    │ ...     │ ...              │
    └─────────┴──────────────────┘
    
    Args:
        lunar_month: Tháng Âm lịch sinh (1-12)
        hour_index: Index giờ sinh Chi (0-11), Tý=0, Sửu=1...
        
    Returns:
        Index Địa Chi của Cung Mệnh (0-11)
    """
    # Bước 1: Khởi từ Dần (2), cộng (tháng-1), trừ giờ
    position = 2 + (lunar_month - 1) - hour_index
    
    # Bước 2: Chuẩn hóa về khoảng 0-11 (xử lý số âm)
    position = ((position % 12) + 12) % 12
    
    return position


# ═══════════════════════════════════════════════════════════════════════════════
# TÍNH CUNG THÂN
# Công thức: (2 + tháng - 1 + giờ) mod 12
# ═══════════════════════════════════════════════════════════════════════════════

def calculate_cung_than(lunar_month: int, hour_index: int) -> int:
    """
    Tính vị trí Cung Thân
    
    KHẨU QUYẾT:
    "Chính nguyệt khởi Dần, thuận đếm theo tháng, thuận đếm theo giờ"
    
    CÔNG THỨC:
    Cung Thân = (Dần + tháng - 1 + giờ) mod 12
              = (2 + lunar_month - 1 + hour_index) mod 12
    
    Ý NGHĨA CUNG THÂN:
    - Nếu Mệnh Thân đồng cung: Một đời may mắn, tốt
    - Nếu Mệnh Thân xung chiếu: Cần cân bằng hai mặt
    
    Args:
        lunar_month: Tháng Âm lịch sinh (1-12)
        hour_index: Index giờ sinh Chi (0-11)
        
    Returns:
        Index Địa Chi của Cung Thân (0-11)
    """
    # Khởi từ Dần (2), cộng (tháng-1), cộng giờ
    position = 2 + (lunar_month - 1) + hour_index
    
    # Chuẩn hóa về khoảng 0-11
    return position % 12


# ═══════════════════════════════════════════════════════════════════════════════
# LẤY THÔNG TIN CUNG MỆNH VÀ THÂN
# ═══════════════════════════════════════════════════════════════════════════════

def get_cung_info(menh_position: int, than_position: int) -> dict:
    """
    Lấy thông tin đầy đủ về Cung Mệnh và Cung Thân
    
    Args:
        menh_position: Index vị trí Cung Mệnh (0-11)
        than_position: Index vị trí Cung Thân (0-11)
        
    Returns:
        dict chứa:
        - menh_position: Index Cung Mệnh
        - menh_name: Tên Địa Chi của Cung Mệnh
        - than_position: Index Cung Thân
        - than_name: Tên Địa Chi của Cung Thân
    """
    return {
        'menh_position': menh_position,
        'menh_name': DIA_CHI[menh_position],
        'than_position': than_position,
        'than_name': DIA_CHI[than_position]
    }
