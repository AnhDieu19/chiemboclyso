"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CỤC & NẠP ÂM CALCULATIONS                                  ║
║                    Tính Cục và Nạp Âm (Mệnh)                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Purpose: Xác định Ngũ Hành Cục và Nạp Âm cho lá số Tử Vi                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

NGŨ HÀNH CỤC:
=============
Cục là đơn vị tính để an sao Tử Vi. Có 5 loại Cục:
┌─────────────────┬─────────┐
│ Tên Cục         │ Số Cục  │
├─────────────────┼─────────┤
│ Thủy Nhị Cục    │ 2       │
│ Mộc Tam Cục     │ 3       │
│ Kim Tứ Cục      │ 4       │
│ Thổ Ngũ Cục     │ 5       │
│ Hỏa Lục Cục     │ 6       │
└─────────────────┴─────────┘

CÁCH XÁC ĐỊNH CỤC:
==================
Dựa vào Can năm sinh và Chi của Cung Mệnh
→ Tra bảng CUC_TABLE[can_group][chi_index]
→ can_group = year_can_index % 5 (vì mỗi nhóm 2 Can dùng chung bảng)

NẠP ÂM (MỆNH):
==============
Nạp Âm là Ngũ Hành của năm sinh theo hệ thống 60 năm Giáp Tý.
Có 30 cặp Nạp Âm, mỗi cặp 2 năm liên tiếp:
- Giáp Tý, Ất Sửu: Hải Trung Kim (Vàng dưới biển)
- Bính Dần, Đinh Mão: Lư Trung Hỏa (Lửa trong lò)
- Mậu Thìn, Kỷ Tỵ: Đại Lâm Mộc (Cây rừng lớn)
...

Ý NGHĨA:
========
- CỤC: Quyết định vị trí an Tử Vi, ảnh hưởng cách tính các sao
- NẠP ÂM: Xác định bản mệnh Ngũ Hành của người (Kim/Mộc/Thủy/Hỏa/Thổ)
"""

from data import NAP_AM


# ═══════════════════════════════════════════════════════════════════════════════
# XÁC ĐỊNH CỤC
# Tra bảng dựa trên Can năm và Chi Cung Mệnh
# ═══════════════════════════════════════════════════════════════════════════════

def get_ngu_hanh_nap_am(can_index: int, chi_index: int) -> int:
    """
    Tính Ngũ Hành Nạp Âm theo công thức toán học (không tra bảng)
    Returns: 1=Kim, 2=Thủy, 3=Hỏa, 4=Thổ, 5=Mộc
    """
    # 1. Trị số Can: Giáp/Ất=1, Bính/Đinh=2, Mậu/Kỷ=3, Canh/Tân=4, Nhâm/Quý=5
    val_can = (can_index // 2) + 1
    
    # 2. Trị số Chi: 
    # Tý/Sửu/Ngọ/Mùi = 0
    # Dần/Mão/Thân/Dậu = 1
    # Thìn/Tỵ/Tuất/Hợi = 2
    # Lookup pattern: 0,0,1,1,2,2, 0,0,1,1,2,2
    lookup_chi = [0, 0, 1, 1, 2, 2, 0, 0, 1, 1, 2, 2]
    val_chi = lookup_chi[chi_index]
    
    # 3. Tính tổng
    total = val_can + val_chi
    if total > 5:
        total -= 5
        
    return total


def _determine_cuc_algorithmic(year_can_index: int, menh_chi_index: int) -> dict:
    """
    Tính Cục bằng thuật toán (dùng để verify với bảng, không dùng trong production)
    
    Thuật toán:
    1. Tìm Can của tháng Dần (Tháng 1) từ Can Năm.
    2. Đếm thuận từ cung Dần đến Cung Mệnh để tìm Can của Mệnh.
    3. Tính Ngũ Hành Nạp Âm của (Can Mệnh, Chi Mệnh).
    4. Ngũ Hành đó chính là Hành của Cục.
    5. Map Hành -> Cục (Thủy 2, Mộc 3, Kim 4, Thổ 5, Hỏa 6).
    """
    
    # 1. Tìm Can tháng Dần (Tháng 1)
    # Công thức: (CanNăm % 5 * 2 + 2) % 10
    # Giáp(0) -> 2(Bính). Kỷ(5) -> 2(Bính).
    can_start = (year_can_index % 5 * 2 + 2) % 10
    
    # 2. Tìm Can Cung Mệnh
    # Mệnh cách Dần bao nhiêu cung?
    # Dần là index 2.
    # Offset = (menh_chi - 2) (có thể âm, % 12 sẽ xử lý nhưng Can loop 10)
    # Cách đếm: Từ Dần(2) đếm thuận.
    # Số bước = (menh_chi_index - 2 + 12) % 12
    steps = (menh_chi_index - 2 + 12) % 12
    can_menh = (can_start + steps) % 10
    
    # 3. Tính Ngũ Hành Nạp Âm (Mệnh)
    element_id = get_ngu_hanh_nap_am(can_menh, menh_chi_index)
    
    # 4. Map Element to Cuc
    # 1=Kim(4), 2=Thủy(2), 3=Hỏa(6), 4=Thổ(5), 5=Mộc(3)
    ELEMENT_TO_CUC = {
        1: {'name': 'Kim Tứ Cục', 'number': 4},
        2: {'name': 'Thủy Nhị Cục', 'number': 2},
        3: {'name': 'Hỏa Lục Cục', 'number': 6},
        4: {'name': 'Thổ Ngũ Cục', 'number': 5},
        5: {'name': 'Mộc Tam Cục', 'number': 3}
    }
    
    cuc_info = ELEMENT_TO_CUC.get(element_id, {'name': 'Unknown', 'number': 2})
    
    return cuc_info


def determine_cuc(year_can_index: int, menh_chi_index: int) -> dict:
    """
    Xác định Ngũ Hành Cục bằng tra bảng CUC_TABLE (chuẩn Nam Phái)
    
    Args:
        year_can_index: Index Thiên Can năm sinh (0-9)
        menh_chi_index: Index Địa Chi Cung Mệnh (0-11)
        
    Returns:
        dict với 'name' và 'number' của Cục
        
    Note:
        - Dùng bảng tra CUC_TABLE làm source of truth
        - Algorithm được giữ lại để verify (không dùng trong production)
    """
    from data import CUC_TABLE, CUC_TYPE
    
    # Giảm Can về 5 nhóm (0-4) vì mỗi nhóm có 2 Can cùng bảng
    # Giáp(0)/Kỷ(5) -> 0, Ất(1)/Canh(6) -> 1, Bính(2)/Tân(7) -> 2, 
    # Đinh(3)/Nhâm(8) -> 3, Mậu(4)/Quý(9) -> 4
    can_group = year_can_index % 5
    
    # Tra bảng
    cuc_name = CUC_TABLE[can_group][menh_chi_index]
    
    # Lấy số cục
    cuc_number = CUC_TYPE.get(cuc_name, 2)  # Default 2 (Thủy Nhị Cục) nếu không tìm thấy
    
    return {
        'name': cuc_name,
        'number': cuc_number
    }


# ═══════════════════════════════════════════════════════════════════════════════
# XÁC ĐỊNH NẠP ÂM (MỆNH)
# Tra bảng 60 Giáp Tý theo Can và Chi năm sinh
# ═══════════════════════════════════════════════════════════════════════════════

def get_nap_am(can_index: int, chi_index: int) -> str:
    """
    Xác định Ngũ Hành Nạp Âm (Mệnh) theo năm sinh
    
    NẠP ÂM: Là hệ thống Ngũ Hành theo 60 năm Giáp Tý, mỗi cặp Can Chi
    có một Nạp Âm riêng.
    
    Args:
        can_index: Index Thiên Can năm sinh (0-9)
        chi_index: Index Địa Chi năm sinh (0-11)
        
    Returns:
        Tên Nạp Âm (ví dụ: "Sơn Đầu Hỏa", "Hải Trung Kim")
    """
    return NAP_AM.get((can_index, chi_index), "Không xác định")
