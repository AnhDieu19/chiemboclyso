"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    PALACE CONVERTER (12 → 9 CUNG)                            ║
║                    Chuyển đổi 12 Cung Tử Vi sang 9 Cung Lạc Thư             ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Purpose: Convert 12-palace Tử Vi system to 9-palace Lạc Thư (Thái Ất/Kì Môn) ║
║  Dependencies: None (standalone converter)                                   ║
║  Output: Palace index mapping (0-11 → 0-8)                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝

HỆ THỐNG 12 CUNG TỬ VI:
========================
0. Mệnh (Life Palace)
1. Phụ Mẫu (Parents)
2. Phúc Đức (Fortune & Virtue)
3. Điền Trạch (Property)
4. Quan Lộc (Career)
5. Nô Bộc (Servants/Friends)
6. Thiên Di (Travel/Migration)
7. Tật Ách (Health/Illness)
8. Tài Bạch (Wealth)
9. Tử Tức (Children)
10. Phu Thê (Spouse)
11. Huynh Đệ (Siblings)

HỆ THỐNG 9 CUNG LẠC THƯ:
=========================
Sắp xếp theo ma phương 3x3 (Lạc Thư Magic Square):

    SE(4)  S(9)  SW(2)
    E(3)   C(5)  W(7)
    NE(8)  N(1)  NW(6)

Index mapping (0-8):
0. Càn (Tây Bắc) - NW(6)
1. Khảm (Bắc) - N(1)
2. Cấn (Đông Bắc) - NE(8)
3. Chấn (Đông) - E(3)
4. Tốn (Đông Nam) - SE(4)
5. Li (Nam) - S(9)
6. Khôn (Tây Nam) - SW(2)
7. Đoài (Tây) - W(7)
8. Trung Cung (Trung tâm) - C(5)

CHIẾN LƯỢC MAPPING:
===================
Không có mapping 1-1 hoàn hảo giữa 12 cung và 9 cung.
Sử dụng mapping theo tương quan ý nghĩa:

12 Cung → 9 Cung (theo Bát Quái):
- Mệnh (0) → Li/Nam (5) - Cung trung tâm mệnh
- Phụ Mẫu (1) → Cấn/ĐB (2) - Cung phụ mẫu/cao vọng
- Phúc Đức (2) → Càn/TB (0) - Cung phúc đức/trí tuệ
- Điền Trạch (3) → Khôn/TN (6) - Cung tài sản/đất đai
- Quan Lộc (4) → Li/Nam (5) - Cung sự nghiệp (overlap với Mệnh)
- Nô Bộc (5) → Đoài/Tây (7) - Cung quan hệ
- Thiên Di (6) → Chấn/Đông (3) - Cung vận động/thay đổi
- Tật Ách (7) → Khảm/Bắc (1) - Cung sức khỏe
- Tài Bạch (8) → Tốn/ĐN (4) - Cung tài lộc
- Tử Tức (9) → Khôn/TN (6) - Cung con cái (overlap với Điền Trạch)
- Phu Thê (10) → Đoài/Tây (7) - Cung hôn nhân (overlap với Nô Bộc)
- Huynh Đệ (11) → Cấn/ĐB (2) - Cung anh em (overlap với Phụ Mẫu)
"""

from typing import Dict, List, Tuple

# ═══════════════════════════════════════════════════════════════════════════════
# HẰNG SỐ / CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

# 12 Cung Tử Vi
TUVI_12_PALACES = [
    'Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 
    'Quan Lộc', 'Nô Bộc', 'Thiên Di', 'Tật Ách',
    'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ'
]

# 9 Cung Lạc Thư (Bát Quái + Trung Cung)
LAC_THU_9_PALACES = [
    'Càn',      # 0 - Tây Bắc (☰)
    'Khảm',     # 1 - Bắc (☵)
    'Cấn',      # 2 - Đông Bắc (☶)
    'Chấn',     # 3 - Đông (☳)
    'Tốn',      # 4 - Đông Nam (☴)
    'Li',       # 5 - Nam (☲)
    'Khôn',     # 6 - Tây Nam (☷)
    'Đoài',     # 7 - Tây (☱)
    'Trung'     # 8 - Trung Cung
]

# Mapping: 12 Cung Tử Vi → 9 Cung Lạc Thư
TUVI_TO_LAC_THU = {
    0: 5,   # Mệnh → Li (Nam) - Cung chủ
    1: 2,   # Phụ Mẫu → Cấn (Đông Bắc) - Cung cao vọng
    2: 0,   # Phúc Đức → Càn (Tây Bắc) - Cung phúc đức
    3: 6,   # Điền Trạch → Khôn (Tây Nam) - Cung đất đai
    4: 5,   # Quan Lộc → Li (Nam) - Cung sự nghiệp
    5: 7,   # Nô Bộc → Đoài (Tây) - Cung quan hệ
    6: 3,   # Thiên Di → Chấn (Đông) - Cung vận động
    7: 1,   # Tật Ách → Khảm (Bắc) - Cung sức khỏe
    8: 4,   # Tài Bạch → Tốn (Đông Nam) - Cung tài lộc
    9: 6,   # Tử Tức → Khôn (Tây Nam) - Cung con cái
    10: 7,  # Phu Thê → Đoài (Tây) - Cung hôn nhân
    11: 2   # Huynh Đệ → Cấn (Đông Bắc) - Cung anh em
}

# Reverse mapping: 9 Cung Lạc Thư → Danh sách các cung Tử Vi tương ứng
LAC_THU_TO_TUVI = {
    0: [2],        # Càn ← Phúc Đức
    1: [7],        # Khảm ← Tật Ách
    2: [1, 11],    # Cấn ← Phụ Mẫu, Huynh Đệ
    3: [6],        # Chấn ← Thiên Di
    4: [8],        # Tốn ← Tài Bạch
    5: [0, 4],     # Li ← Mệnh, Quan Lộc
    6: [3, 9],     # Khôn ← Điền Trạch, Tử Tức
    7: [5, 10],    # Đoài ← Nô Bộc, Phu Thê
    8: []          # Trung Cung (không mapping trực tiếp)
}

# Lạc Thư directions
LAC_THU_DIRECTIONS = {
    0: 'Tây Bắc',   # Càn
    1: 'Bắc',       # Khảm
    2: 'Đông Bắc',  # Cấn
    3: 'Đông',      # Chấn
    4: 'Đông Nam',  # Tốn
    5: 'Nam',       # Li
    6: 'Tây Nam',   # Khôn
    7: 'Tây',       # Đoài
    8: 'Trung'      # Trung Cung
}

# Ngũ Hành của 9 Cung
LAC_THU_NGU_HANH = {
    0: 'Kim',    # Càn
    1: 'Thủy',   # Khảm
    2: 'Thổ',    # Cấn
    3: 'Mộc',    # Chấn
    4: 'Mộc',    # Tốn
    5: 'Hỏa',    # Li
    6: 'Thổ',    # Khôn
    7: 'Kim',    # Đoài
    8: 'Thổ'     # Trung Cung
}


# ═══════════════════════════════════════════════════════════════════════════════
# CORE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def convert_tuvi_to_lac_thu(tuvi_palace_index: int) -> int:
    """
    Chuyển đổi index cung Tử Vi (0-11) sang index cung Lạc Thư (0-8)
    
    Args:
        tuvi_palace_index: Index cung Tử Vi (0-11)
        
    Returns:
        Index cung Lạc Thư (0-8)
    """
    if not 0 <= tuvi_palace_index <= 11:
        raise ValueError(f"Invalid Tử Vi palace index: {tuvi_palace_index}. Must be 0-11.")
    
    return TUVI_TO_LAC_THU[tuvi_palace_index]


def get_tuvi_palaces_from_lac_thu(lac_thu_index: int) -> List[int]:
    """
    Lấy danh sách các cung Tử Vi tương ứng với cung Lạc Thư
    
    Args:
        lac_thu_index: Index cung Lạc Thư (0-8)
        
    Returns:
        List các index cung Tử Vi (có thể có nhiều cung map vào 1 cung Lạc Thư)
    """
    if not 0 <= lac_thu_index <= 8:
        raise ValueError(f"Invalid Lạc Thư palace index: {lac_thu_index}. Must be 0-8.")
    
    return LAC_THU_TO_TUVI.get(lac_thu_index, [])


def get_lac_thu_palace_name(index: int) -> str:
    """
    Lấy tên cung Lạc Thư từ index
    
    Args:
        index: Index cung Lạc Thư (0-8)
        
    Returns:
        Tên cung (Càn, Khảm, Cấn, Chấn, Tốn, Li, Khôn, Đoài, Trung)
    """
    if not 0 <= index <= 8:
        raise ValueError(f"Invalid index: {index}. Must be 0-8.")
    
    return LAC_THU_9_PALACES[index]


def get_tuvi_palace_name(index: int) -> str:
    """
    Lấy tên cung Tử Vi từ index
    
    Args:
        index: Index cung Tử Vi (0-11)
        
    Returns:
        Tên cung
    """
    if not 0 <= index <= 11:
        raise ValueError(f"Invalid index: {index}. Must be 0-11.")
    
    return TUVI_12_PALACES[index]


def get_lac_thu_palace_info(index: int) -> Dict:
    """
    Lấy thông tin chi tiết của cung Lạc Thư
    
    Args:
        index: Index cung Lạc Thư (0-8)
        
    Returns:
        Dict chứa thông tin: name, direction, element, tuvi_palaces
    """
    if not 0 <= index <= 8:
        raise ValueError(f"Invalid index: {index}. Must be 0-8.")
    
    return {
        'index': index,
        'name': LAC_THU_9_PALACES[index],
        'direction': LAC_THU_DIRECTIONS[index],
        'element': LAC_THU_NGU_HANH[index],
        'tuvi_palaces': [get_tuvi_palace_name(i) for i in get_tuvi_palaces_from_lac_thu(index)]
    }


def convert_tuvi_chart_to_lac_thu(tuvi_chart_data: Dict) -> Dict:
    """
    Chuyển đổi toàn bộ lá số Tử Vi (12 cung) sang Lạc Thư (9 cung)
    
    Chiến lược:
    - Map mỗi cung Tử Vi sang cung Lạc Thư tương ứng
    - Merge data nếu nhiều cung Tử Vi map vào 1 cung Lạc Thư
    
    Args:
        tuvi_chart_data: Dict với key là index cung Tử Vi (0-11)
                         Value là data của cung đó (stars, meaning, etc.)
        
    Returns:
        Dict với key là index cung Lạc Thư (0-8)
        Value là merged data từ các cung Tử Vi
    """
    lac_thu_chart = {}
    
    # Khởi tạo 9 cung Lạc Thư
    for i in range(9):
        lac_thu_chart[i] = {
            'palace_name': LAC_THU_9_PALACES[i],
            'direction': LAC_THU_DIRECTIONS[i],
            'element': LAC_THU_NGU_HANH[i],
            'tuvi_sources': [],  # Các cung Tử Vi nguồn
            'merged_data': []    # Data từ các cung Tử Vi
        }
    
    # Map data từ 12 cung Tử Vi
    for tuvi_idx, tuvi_data in tuvi_chart_data.items():
        if not 0 <= tuvi_idx <= 11:
            continue
            
        lac_thu_idx = convert_tuvi_to_lac_thu(tuvi_idx)
        
        lac_thu_chart[lac_thu_idx]['tuvi_sources'].append({
            'index': tuvi_idx,
            'name': TUVI_12_PALACES[tuvi_idx]
        })
        
        lac_thu_chart[lac_thu_idx]['merged_data'].append(tuvi_data)
    
    return lac_thu_chart


def get_lac_thu_grid_position(index: int) -> Tuple[int, int]:
    """
    Lấy vị trí (row, col) của cung Lạc Thư trong lưới 3x3
    
    Grid layout:
        [2][0][4]  (row 0)
        [3][8][7]  (row 1)
        [1][6][5]  (row 2)
    
    Args:
        index: Index cung Lạc Thư (0-8)
        
    Returns:
        (row, col) tuple (0-indexed)
    """
    # Ma phương Lạc Thư 3x3
    grid = [
        [2, 0, 4],  # Row 0: Cấn, Càn, Tốn
        [3, 8, 7],  # Row 1: Chấn, Trung, Đoài
        [1, 6, 5]   # Row 2: Khảm, Khôn, Li
    ]
    
    for row in range(3):
        for col in range(3):
            if grid[row][col] == index:
                return (row, col)
    
    return (None, None)


# ═══════════════════════════════════════════════════════════════════════════════
# TESTING
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 80)
    print("TESTING PALACE CONVERTER (12 → 9 CUNG)")
    print("=" * 80)
    
    # Test 1: Individual palace conversion
    print("\nTest 1: Chuyển đổi từng cung")
    print("-" * 80)
    
    for tuvi_idx in range(12):
        lac_thu_idx = convert_tuvi_to_lac_thu(tuvi_idx)
        tuvi_name = get_tuvi_palace_name(tuvi_idx)
        lac_thu_name = get_lac_thu_palace_name(lac_thu_idx)
        direction = LAC_THU_DIRECTIONS[lac_thu_idx]
        element = LAC_THU_NGU_HANH[lac_thu_idx]
        
        print(f"{tuvi_idx:2d}. {tuvi_name:12s} → {lac_thu_idx}. {lac_thu_name:6s} ({direction:10s}) - {element}")
    
    # Test 2: Reverse mapping
    print("\nTest 2: Reverse mapping (Lạc Thư → Tử Vi)")
    print("-" * 80)
    
    for lac_thu_idx in range(9):
        info = get_lac_thu_palace_info(lac_thu_idx)
        print(f"{lac_thu_idx}. {info['name']:6s} ({info['direction']:10s}) - {info['element']}")
        print(f"   ← Cung Tử Vi: {', '.join(info['tuvi_palaces']) if info['tuvi_palaces'] else 'Không có'}")
    
    # Test 3: Grid positions
    print("\nTest 3: Vị trí trong lưới 3x3")
    print("-" * 80)
    print("\nLạc Thư Magic Square:")
    
    grid = [
        [2, 0, 4],
        [3, 8, 7],
        [1, 6, 5]
    ]
    
    for row in grid:
        for idx in row:
            name = LAC_THU_9_PALACES[idx]
            print(f"{name:6s}", end=" ")
        print()
