"""
Meanings Loader - Load interpretation data from JSON files
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional

# Base directory for meanings data
# Path: python/interpretation/meanings/loader.py -> python/data/meanings
DATA_DIR = Path(__file__).parent.parent.parent / "data" / "meanings"


def load_json(filename: str) -> Dict[str, Any]:
    """Load a JSON file from the meanings directory."""
    filepath = DATA_DIR / filename
    if not filepath.exists():
        return {}
    with open(filepath, encoding='utf-8') as f:
        return json.load(f)


# Cache loaded data
_cache: Dict[str, Dict] = {}


def get_chinh_tinh_meanings() -> Dict[str, Any]:
    """Get Chinh Tinh (Main Stars) meanings."""
    if 'chinh_tinh' not in _cache:
        _cache['chinh_tinh'] = load_json('chinh_tinh.json')
    return _cache['chinh_tinh']


def get_phu_tinh_meanings() -> Dict[str, Any]:
    """Get Phu Tinh (Auxiliary Stars) meanings."""
    if 'phu_tinh' not in _cache:
        basic = load_json('phu_tinh.json')
        special = load_json('phu_tinh_special.json')
        _cache['phu_tinh'] = {**basic, **special}
    return _cache['phu_tinh']


def get_than_cu_meanings() -> Dict[str, Any]:
    """Get Than Cu (Body Palace Position) meanings."""
    if 'than_cu' not in _cache:
        _cache['than_cu'] = load_json('than_cu.json')
    return _cache['than_cu']


def get_truong_sinh_meanings() -> Dict[str, Any]:
    """Get Truong Sinh (12 Life Stages) meanings."""
    if 'truong_sinh' not in _cache:
        _cache['truong_sinh'] = load_json('truong_sinh.json')
    return _cache['truong_sinh']


def get_dai_van_meanings() -> Dict[str, Any]:
    """Get Dai Van (Major Fortune Period) meanings."""
    if 'dai_van' not in _cache:
        _cache['dai_van'] = load_json('dai_van.json')
    return _cache['dai_van']


def get_tieu_han_meanings() -> Dict[str, Any]:
    """Get Tieu Han (Annual Fortune) meanings."""
    if 'tieu_han' not in _cache:
        _cache['tieu_han'] = load_json('tieu_han.json')
    return _cache['tieu_han']


def get_star_meaning(star_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for a specific star (Chinh Tinh or Phu Tinh)."""
    chinh_tinh = get_chinh_tinh_meanings()
    if star_name in chinh_tinh:
        return chinh_tinh[star_name]
    
    phu_tinh = get_phu_tinh_meanings()
    if star_name in phu_tinh:
        return phu_tinh[star_name]
    
    return None


def get_star_in_palace_meaning(star_name: str, palace_name: str) -> Optional[str]:
    """Get meaning for a star in a specific palace."""
    meaning = get_star_meaning(star_name)
    if meaning and 'in_palace' in meaning:
        return meaning['in_palace'].get(palace_name)
    return None


def get_than_cu_meaning(palace_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for Than (Body) positioned in a specific palace."""
    than_cu = get_than_cu_meanings()
    return than_cu.get(palace_name)


def get_truong_sinh_in_palace(truong_sinh_name: str, palace_name: str) -> Optional[str]:
    """Get meaning for a Truong Sinh stage in a specific palace."""
    truong_sinh = get_truong_sinh_meanings()
    if truong_sinh_name in truong_sinh:
        return truong_sinh[truong_sinh_name].get('in_palace', {}).get(palace_name)
    return None


def get_dai_van_tam_hop(tam_hop_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for a Tam Hop (Triple Combination) in Dai Van."""
    dai_van = get_dai_van_meanings()
    return dai_van.get('tam_hop', {}).get(tam_hop_name)


def get_dai_van_vong(vong_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for a Vong (Circle) in Dai Van."""
    dai_van = get_dai_van_meanings()
    return dai_van.get('vong', {}).get(vong_name)


def get_tieu_han_star_meaning(star_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for a star in Tieu Han (Annual Fortune)."""
    tieu_han = get_tieu_han_meanings()
    return tieu_han.get('sao_nhap_tieu_han', {}).get(star_name)


def get_nguyet_han_star_meaning(star_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for a star in Nguyet Han (Monthly Fortune)."""
    tieu_han = get_tieu_han_meanings()
    return tieu_han.get('sao_nhap_nguyet_han', {}).get(star_name)


def get_giap_meanings() -> Dict[str, Any]:
    """Get Giap (Flanking Stars) meanings."""
    if 'giap' not in _cache:
        _cache['giap'] = load_json('giap_meanings.json')
    return _cache['giap']


def get_phi_hoa_nam_meanings() -> Dict[str, Any]:
    """Get Phi Hoa Nam (Annual Flying Transformations) meanings."""
    if 'phi_hoa_nam' not in _cache:
        _cache['phi_hoa_nam'] = load_json('phi_hoa_nam.json')
    return _cache['phi_hoa_nam']


def get_giap_meaning(star1: str, star2: str = None) -> Optional[Dict[str, Any]]:
    """Get meaning for a specific Giap (flanking) configuration."""
    giap = get_giap_meanings()
    for key, value in giap.items():
        stars = value.get('stars', [])
        if star1 in stars and (star2 is None or star2 in stars):
            return value
    return None


def get_phi_hoa_in_palace(hoa_type: str, palace_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for Phi Hoa (Flying Transformation) in a specific palace.
    
    Args:
        hoa_type: 'phi_hoa_loc', 'phi_hoa_quyen', 'phi_hoa_khoa', 'phi_hoa_ky'
        palace_name: Name of the palace
    """
    phi_hoa = get_phi_hoa_nam_meanings()
    hoa_data = phi_hoa.get(hoa_type, {})
    return hoa_data.get(palace_name)


def get_luu_tinh_meaning(star_name: str, palace_name: str) -> Optional[Dict[str, Any]]:
    """Get meaning for Luu Tinh (Annual Stars) in a specific palace."""
    phi_hoa = get_phi_hoa_nam_meanings()
    luu_tinh = phi_hoa.get('luu_tinh', {})
    star_data = luu_tinh.get(star_name, {})
    return star_data.get(palace_name)


def clear_cache():
    """Clear the meanings cache."""
    _cache.clear()


# For backward compatibility and easy access
CHINH_TINH_MEANINGS = property(lambda self: get_chinh_tinh_meanings())
PHU_TINH_MEANINGS = property(lambda self: get_phu_tinh_meanings())

