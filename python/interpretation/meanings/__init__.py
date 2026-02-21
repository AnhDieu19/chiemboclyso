"""
Interpretation Layer - Meanings Init
Supports both legacy Python dicts and new JSON-based data
"""

from .chinh_tinh_meanings import CHINH_TINH_MEANINGS
from .palace_meanings import PALACE_MEANINGS
from .phu_tinh_meanings import PHU_TINH_MEANINGS

# New JSON-based loader for detailed meanings
from .loader import (
    get_chinh_tinh_meanings,
    get_phu_tinh_meanings,
    get_than_cu_meanings,
    get_truong_sinh_meanings,
    get_dai_van_meanings,
    get_tieu_han_meanings,
    get_star_meaning,
    get_star_in_palace_meaning,
    get_than_cu_meaning,
    get_truong_sinh_in_palace,
    get_dai_van_tam_hop,
    get_dai_van_vong,
    get_tieu_han_star_meaning,
    get_nguyet_han_star_meaning,
    # New: Giap and Phi Hoa
    get_giap_meanings,
    get_phi_hoa_nam_meanings,
    get_giap_meaning,
    get_phi_hoa_in_palace,
    get_luu_tinh_meaning,
)

STAR_MEANINGS = {**CHINH_TINH_MEANINGS, **PHU_TINH_MEANINGS}

