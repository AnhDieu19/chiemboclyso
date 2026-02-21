"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    NGŨ HÀNH ENGINE (FIVE ELEMENTS)                           ║
║                    Tương Sinh Tương Khắc Logic                               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Purpose: Calculate Ngũ Hành (Five Elements) relationships and cycles       ║
║  Used by: Thái Ất (Ngũ Nguyên), Kì Môn, general Tử Vi logic                ║
║  Refactored from: analytics/tuvi_knowledge_graph.py                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

NGŨ HÀNH (FIVE ELEMENTS):
==========================
Kim (Metal) - Thủy (Water) - Mộc (Wood) - Hỏa (Fire) - Thổ (Earth)

TƯƠNG SINH (Generating Cycle):
- Kim → Thủy (Metal generates Water)
- Thủy → Mộc (Water nourishes Wood)
- Mộc → Hỏa (Wood feeds Fire)
- Hỏa → Thổ (Fire creates Earth/ash)
- Thổ → Kim (Earth contains Metal)

TƯƠNG KHẮC (Controlling Cycle):
- Kim → Mộc (Metal cuts Wood)
- Mộc → Thổ (Wood depletes Earth)
- Thổ → Thủy (Earth dams Water)
- Thủy → Hỏa (Water extinguishes Fire)
- Hỏa → Kim (Fire melts Metal)
"""

from typing import Dict, List, Tuple

# ═══════════════════════════════════════════════════════════════════════════════
# HẰNG SỐ / CONSTANTS
# ═══════════════════════════════════════════════════════════════════════════════

# 5 Elements
NGU_HANH = ['Kim', 'Thủy', 'Mộc', 'Hỏa', 'Thổ']

# Generating Cycle (Tương Sinh)
NGU_HANH_SINH = {
    'Kim': 'Thủy',   # Metal → Water
    'Thủy': 'Mộc',   # Water → Wood
    'Mộc': 'Hỏa',    # Wood → Fire
    'Hỏa': 'Thổ',    # Fire → Earth
    'Thổ': 'Kim'     # Earth → Metal
}

# Controlling Cycle (Tương Khắc)
NGU_HANH_KHAC = {
    'Kim': 'Mộc',    # Metal → Wood
    'Mộc': 'Thổ',    # Wood → Earth
    'Thổ': 'Thủy',   # Earth → Water
    'Thủy': 'Hỏa',   # Water → Fire
    'Hỏa': 'Kim'     # Fire → Metal
}

# Reverse mappings (who generates me? who controls me?)
NGU_HANH_DUOC_SINH = {v: k for k, v in NGU_HANH_SINH.items()}  # Who generates this element
NGU_HANH_BI_KHAC = {v: k for k, v in NGU_HANH_KHAC.items()}     # Who controls this element

# Index mapping (for cycle calculations)
NGU_HANH_INDEX = {
    'Kim': 0,
    'Thủy': 1,
    'Mộc': 2,
    'Hỏa': 3,
    'Thổ': 4
}

# Reverse index
INDEX_TO_NGU_HANH = {v: k for k, v in NGU_HANH_INDEX.items()}


# ═══════════════════════════════════════════════════════════════════════════════
# CORE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def get_sinh_element(element: str) -> str:
    """
    Lấy hành được sinh ra từ hành này
    
    Args:
        element: Tên hành ('Kim', 'Thủy', 'Mộc', 'Hỏa', 'Thổ')
        
    Returns:
        Hành được sinh (str)
    """
    return NGU_HANH_SINH.get(element, None)


def get_khac_element(element: str) -> str:
    """
    Lấy hành bị khắc bởi hành này
    
    Args:
        element: Tên hành
        
    Returns:
        Hành bị khắc (str)
    """
    return NGU_HANH_KHAC.get(element, None)


def get_parent_element(element: str) -> str:
    """
    Lấy hành sinh ra hành này (hành mẹ)
    
    Args:
        element: Tên hành
        
    Returns:
        Hành mẹ (str)
    """
    return NGU_HANH_DUOC_SINH.get(element, None)


def get_controller_element(element: str) -> str:
    """
    Lấy hành khắc hành này
    
    Args:
        element: Tên hành
        
    Returns:
        Hành khắc (str)
    """
    return NGU_HANH_BI_KHAC.get(element, None)


def check_sinh_relationship(from_element: str, to_element: str) -> bool:
    """
    Kiểm tra xem from_element có sinh to_element không
    
    Args:
        from_element: Hành nguồn
        to_element: Hành đích
        
    Returns:
        True nếu có quan hệ sinh
    """
    return NGU_HANH_SINH.get(from_element) == to_element


def check_khac_relationship(from_element: str, to_element: str) -> bool:
    """
    Kiểm tra xem from_element có khắc to_element không
    
    Args:
        from_element: Hành nguồn
        to_element: Hành đích
        
    Returns:
        True nếu có quan hệ khắc
    """
    return NGU_HANH_KHAC.get(from_element) == to_element


def get_relationship(from_element: str, to_element: str) -> str:
    """
    Xác định quan hệ giữa 2 hành
    
    Args:
        from_element: Hành nguồn
        to_element: Hành đích
        
    Returns:
        'sinh' | 'khac' | 'duoc_sinh' | 'bi_khac' | 'same' | 'neutral'
    """
    if from_element == to_element:
        return 'same'
    
    if check_sinh_relationship(from_element, to_element):
        return 'sinh'  # from sinh to
    
    if check_khac_relationship(from_element, to_element):
        return 'khac'  # from khắc to
    
    if check_sinh_relationship(to_element, from_element):
        return 'duoc_sinh'  # from được sinh bởi to
    
    if check_khac_relationship(to_element, from_element):
        return 'bi_khac'  # from bị khắc bởi to
    
    return 'neutral'


def calculate_distance(from_element: str, to_element: str) -> int:
    """
    Tính khoảng cách giữa 2 hành trong chu kỳ sinh (0-4)
    
    Args:
        from_element: Hành nguồn
        to_element: Hành đích
        
    Returns:
        Khoảng cách (0-4), 1 = sinh trực tiếp, 2 = sinh gián tiếp
    """
    if from_element == to_element:
        return 0
    
    from_idx = NGU_HANH_INDEX[from_element]
    to_idx = NGU_HANH_INDEX[to_element]
    
    # Tính khoảng cách theo chiều kim đồng hồ
    distance = (to_idx - from_idx) % 5
    
    return distance


def get_cycle_path(from_element: str, to_element: str, cycle_type: str = 'sinh') -> List[str]:
    """
    Lấy đường đi trong chu kỳ sinh hoặc khắc
    
    Args:
        from_element: Hành bắt đầu
        to_element: Hành kết thúc
        cycle_type: 'sinh' hoặc 'khac'
        
    Returns:
        List các hành trong đường đi (bao gồm from và to)
    """
    path = [from_element]
    current = from_element
    
    # Giới hạn 5 bước để tránh vòng lặp vô tận
    for _ in range(5):
        if current == to_element and len(path) > 1:
            break
            
        if cycle_type == 'sinh':
            next_element = get_sinh_element(current)
        else:  # khac
            next_element = get_khac_element(current)
            
        if next_element is None:
            break
            
        path.append(next_element)
        current = next_element
        
    return path


def calculate_ngu_nguyen_element(year: int) -> Tuple[str, int]:
    """
    Tính Ngũ Nguyên (Nguyên Hành) cho Thái Ất
    
    Ngũ Nguyên: Mỗi nguyên = 72 năm, 5 nguyên = 360 năm
    - Nguyên 1 (1864-1935): Thượng Nguyên - Hành Kim
    - Nguyên 2 (1936-2007): Trung Nguyên - Hành Thủy  
    - Nguyên 3 (2008-2079): Hạ Nguyên - Hành Mộc
    - Nguyên 4 (2080-2151): Thượng Nguyên - Hành Hỏa
    - Nguyên 5 (2152-2223): Trung Nguyên - Hành Thổ
    
    Args:
        year: Năm dương lịch
        
    Returns:
        (tên_hành, index_nguyên) - VD: ('Thủy', 2)
    """
    # Base year (1864 = bắt đầu chu kỳ 360 năm hiện tại)
    base_year = 1864
    
    # Tính số năm từ base year
    years_since_base = year - base_year
    
    # Mỗi nguyên = 72 năm
    nguyen_index = (years_since_base // 72) % 5
    
    # Thứ tự hành: Kim → Thủy → Mộc → Hỏa → Thổ
    nguyen_elements = ['Kim', 'Thủy', 'Mộc', 'Hỏa', 'Thổ']
    
    return (nguyen_elements[nguyen_index], nguyen_index + 1)


def get_element_properties(element: str) -> Dict:
    """
    Lấy thuộc tính chi tiết của một hành
    
    Args:
        element: Tên hành
        
    Returns:
        Dict chứa thông tin chi tiết
    """
    properties = {
        'Kim': {
            'name': 'Kim',
            'chinese': '金',
            'season': 'Thu',
            'direction': 'Tây',
            'color': 'Trắng',
            'sinh': 'Thủy',
            'khac': 'Mộc',
            'duoc_sinh': 'Thổ',
            'bi_khac': 'Hỏa',
            'characteristics': 'Cứng rắn, quyết đoán, sắc bén'
        },
        'Thủy': {
            'name': 'Thủy',
            'chinese': '水',
            'season': 'Đông',
            'direction': 'Bắc',
            'color': 'Đen',
            'sinh': 'Mộc',
            'khac': 'Hỏa',
            'duoc_sinh': 'Kim',
            'bi_khac': 'Thổ',
            'characteristics': 'Linh hoạt, thông minh, sâu sắc'
        },
        'Mộc': {
            'name': 'Mộc',
            'chinese': '木',
            'season': 'Xuân',
            'direction': 'Đông',
            'color': 'Xanh lá',
            'sinh': 'Hỏa',
            'khac': 'Thổ',
            'duoc_sinh': 'Thủy',
            'bi_khac': 'Kim',
            'characteristics': 'Sinh trưởng, phát triển, nhân từ'
        },
        'Hỏa': {
            'name': 'Hỏa',
            'chinese': '火',
            'season': 'Hạ',
            'direction': 'Nam',
            'color': 'Đỏ',
            'sinh': 'Thổ',
            'khac': 'Kim',
            'duoc_sinh': 'Mộc',
            'bi_khac': 'Thủy',
            'characteristics': 'Nhiệt huyết, năng động, sáng tạo'
        },
        'Thổ': {
            'name': 'Thổ',
            'chinese': '土',
            'season': 'Tứ Mùa',
            'direction': 'Trung',
            'color': 'Vàng',
            'sinh': 'Kim',
            'khac': 'Thủy',
            'duoc_sinh': 'Hỏa',
            'bi_khac': 'Mộc',
            'characteristics': 'Ổn định, bao dung, trung thành'
        }
    }
    
    return properties.get(element, {})


# ═══════════════════════════════════════════════════════════════════════════════
# TESTING
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("=" * 80)
    print("TESTING NGŨ HÀNH ENGINE")
    print("=" * 80)
    
    # Test 1: Quan hệ sinh khắc
    print("\nTest 1: Quan hệ sinh khắc")
    print("-" * 80)
    test_pairs = [
        ('Kim', 'Thủy'),  # Kim sinh Thủy
        ('Thủy', 'Hỏa'),  # Thủy khắc Hỏa
        ('Mộc', 'Hỏa'),   # Mộc sinh Hỏa
        ('Kim', 'Mộc'),   # Kim khắc Mộc
    ]
    
    for from_el, to_el in test_pairs:
        rel = get_relationship(from_el, to_el)
        print(f"{from_el} → {to_el}: {rel}")
    
    # Test 2: Ngũ Nguyên
    print("\nTest 2: Ngũ Nguyên (Thái Ất)")
    print("-" * 80)
    test_years = [1900, 1968, 2000, 2024, 2050]
    
    for year in test_years:
        element, nguyen = calculate_ngu_nguyen_element(year)
        props = get_element_properties(element)
        print(f"Năm {year}: Nguyên {nguyen} - Hành {element} ({props['chinese']}) - {props['season']}")
    
    # Test 3: Cycle path
    print("\nTest 3: Chu kỳ sinh")
    print("-" * 80)
    path = get_cycle_path('Kim', 'Hỏa', 'sinh')
    print(f"Kim → Hỏa (sinh): {' → '.join(path)}")
