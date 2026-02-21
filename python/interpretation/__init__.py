"""
Interpretation Layer - Init file
"""

from .meanings import STAR_MEANINGS, PALACE_MEANINGS, CHINH_TINH_MEANINGS, PHU_TINH_MEANINGS
from .chart_analyzer import generate_overall_interpretation, interpret_palace_detailed
from .patterns import detect_patterns, summarize_patterns, CACH_CUC_DEFINITIONS
from .cach_cuc import (
    detect_cach_cuc, generate_cach_cuc_interpretation, 
    get_cach_cuc_for_display, CACH_CUC_LIST
)
