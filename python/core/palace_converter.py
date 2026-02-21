"""
Palace Converter - Chuyển đổi 12 Cung (Địa Chi) ↔ 9 Cung (Lạc Thư)

Dùng cho: Huyền Không, Thái Ất, Kì Môn
"""

from typing import Dict, Tuple

# 12 Địa Chi
DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 
           'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

# 9 Cung Lạc Thư với Bát Quái
LAC_THU_CUNG = {
    1: {'name': 'Khảm', 'han': '坎', 'direction': 'Bắc', 'ngu_hanh': 'Thủy'},
    2: {'name': 'Khôn', 'han': '坤', 'direction': 'Tây Nam', 'ngu_hanh': 'Thổ'},
    3: {'name': 'Chấn', 'han': '震', 'direction': 'Đông', 'ngu_hanh': 'Mộc'},
    4: {'name': 'Tốn', 'han': '巽', 'direction': 'Đông Nam', 'ngu_hanh': 'Mộc'},
    5: {'name': 'Trung Cung', 'han': '中宮', 'direction': 'Trung Tâm', 'ngu_hanh': 'Thổ'},
    6: {'name': 'Càn', 'han': '乾', 'direction': 'Tây Bắc', 'ngu_hanh': 'Kim'},
    7: {'name': 'Đoài', 'han': '兌', 'direction': 'Tây', 'ngu_hanh': 'Kim'},
    8: {'name': 'Cấn', 'han': '艮', 'direction': 'Đông Bắc', 'ngu_hanh': 'Thổ'},
    9: {'name': 'Ly', 'han': '離', 'direction': 'Nam', 'ngu_hanh': 'Hỏa'},
}

# Ánh xạ 12 Cung (Địa Chi index) → 9 Cung (Lạc Thư)
# Quy tắc dựa trên phương vị
PALACE_12_TO_9 = {
    0: 1,   # Tý → Khảm (Bắc)
    1: 8,   # Sửu → Cấn (Đông Bắc)
    2: 3,   # Dần → Chấn (Đông)
    3: 3,   # Mão → Chấn (Đông)
    4: 4,   # Thìn → Tốn (Đông Nam)
    5: 9,   # Tỵ → Ly (Nam)
    6: 9,   # Ngọ → Ly (Nam)
    7: 2,   # Mùi → Khôn (Tây Nam)
    8: 7,   # Thân → Đoài (Tây)
    9: 7,   # Dậu → Đoài (Tây)
    10: 6,  # Tuất → Càn (Tây Bắc)
    11: 1,  # Hợi → Khảm (Bắc)
}

# Layout Lạc Thư (3x3 grid)
# Đọc từ trên xuống, trái sang phải
LAC_THU_LAYOUT = [
    [4, 9, 2],  # Row 0: Tốn, Ly, Khôn
    [3, 5, 7],  # Row 1: Chấn, Trung, Đoài
    [8, 1, 6],  # Row 2: Cấn, Khảm, Càn
]


def convert_12_to_9(chi_index: int) -> int:
    """
    Chuyển đổi từ 12 Cung (Địa Chi) sang 9 Cung (Lạc Thư)
    
    Args:
        chi_index: 0-11 (Tý=0, Sửu=1, ...)
        
    Returns:
        1-9 (Lạc Thư cung index)
    """
    return PALACE_12_TO_9.get(chi_index, 5)


def get_9_palace_info(palace_idx: int) -> Dict:
    """
    Lấy thông tin đầy đủ của 9 Cung
    
    Args:
        palace_idx: 1-9
        
    Returns:
        Dict với name, han, direction, ngu_hanh
    """
    return LAC_THU_CUNG.get(palace_idx, LAC_THU_CUNG[5])


def get_palace_position(palace_idx: int) -> Tuple[int, int]:
    """
    Lấy vị trí (row, col) của cung trong layout 3x3
    
    Args:
        palace_idx: 1-9
        
    Returns:
        (row, col) với row, col trong [0, 1, 2]
    """
    for row in range(3):
        for col in range(3):
            if LAC_THU_LAYOUT[row][col] == palace_idx:
                return (row, col)
    return (1, 1)  # Default: Trung Cung


def get_adjacent_palaces(palace_idx: int) -> Dict[str, int]:
    """
    Lấy các cung liền kề
    
    Args:
        palace_idx: 1-9
        
    Returns:
        Dict với direction: palace_idx
    """
    row, col = get_palace_position(palace_idx)
    adjacent = {}
    
    directions = [
        ('Bắc', -1, 0),
        ('Nam', 1, 0),
        ('Đông', 0, 1),
        ('Tây', 0, -1),
        ('Đông Bắc', -1, 1),
        ('Đông Nam', 1, 1),
        ('Tây Bắc', -1, -1),
        ('Tây Nam', 1, -1),
    ]
    
    for dir_name, dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            adjacent[dir_name] = LAC_THU_LAYOUT[new_row][new_col]
    
    return adjacent


def get_opposite_palace(palace_idx: int) -> int:
    """
    Lấy cung đối diện (xung)
    
    Quy tắc: 1↔9, 2↔8, 3↔7, 4↔6, 5 tự xung
    """
    opposites = {1: 9, 9: 1, 2: 8, 8: 2, 3: 7, 7: 3, 4: 6, 6: 4, 5: 5}
    return opposites.get(palace_idx, 5)


def phi_thuong(start_palace: int, steps: int, is_duong: bool = True) -> int:
    """
    Phi cung theo thứ tự Lạc Thư
    
    Dương Độn: Thuận phi (1→2→3→4→5→6→7→8→9→1...)
    Âm Độn: Nghịch phi (9→8→7→6→5→4→3→2→1→9...)
    
    Args:
        start_palace: Cung bắt đầu (1-9)
        steps: Số bước di chuyển
        is_duong: True = thuận, False = nghịch
        
    Returns:
        Cung đích (1-9)
    """
    if is_duong:
        return ((start_palace - 1 + steps) % 9) + 1
    else:
        return ((start_palace - 1 - steps) % 9) + 1


def get_lac_thu_as_grid() -> list:
    """
    Trả về Lạc Thư layout dưới dạng 2D array
    với thông tin đầy đủ mỗi cung
    """
    grid = []
    for row in LAC_THU_LAYOUT:
        grid_row = []
        for palace_idx in row:
            info = get_9_palace_info(palace_idx)
            info['index'] = palace_idx
            grid_row.append(info)
        grid.append(grid_row)
    return grid


# Test
if __name__ == '__main__':
    # Test convert
    for i in range(12):
        p9 = convert_12_to_9(i)
        info = get_9_palace_info(p9)
        print(f"{DIA_CHI[i]} (Địa Chi {i}) → Cung {p9} ({info['name']})")
    
    print("\n--- Lạc Thư Layout ---")
    grid = get_lac_thu_as_grid()
    for row in grid:
        print([f"{c['index']}:{c['name']}" for c in row])
    
    print("\n--- Phi Thuận từ Cung 1, 5 bước ---")
    print(f"Dương Độn: {phi_thuong(1, 5, True)}")
    print(f"Âm Độn: {phi_thuong(1, 5, False)}")
