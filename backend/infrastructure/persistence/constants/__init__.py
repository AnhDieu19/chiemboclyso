"""
Data Layer - Init file that exports all constants
Central import point for all data modules
"""

# Can Chi and Nap Am
from .can_chi import THIEN_CAN, DIA_CHI, NGU_HANH, CHI_NGU_HANH, GIO_SINH_RANGE, NAP_AM

# Cung and Cuc
from .cung_cuc import CUNG_ORDER, CUC_TYPE, CUC_TABLE

# Chinh Tinh (14 Main Stars)
from .chinh_tinh import CHINH_TINH, TU_VI_GROUP_OFFSET, TUVI_POSITION, THIEN_PHU_POSITION, THIEN_PHU_GROUP_OFFSET

# Luc Cat Tinh
from .phu_tinh_luc_cat import TA_PHU_BASE, HUU_BAT_BASE, VAN_XUONG_BASE, VAN_KHUC_BASE, THIEN_KHOI_VIET

# Luc Sat Tinh
from .phu_tinh_luc_sat import KINH_DA, HOA_LINH_BASE

# Truong Sinh cycle
from .phu_tinh_truong_sinh import TRUONG_SINH_STARS, TRUONG_SINH_BASE

# Bac Sy ring
from .phu_tinh_bac_sy import LOC_TON_POSITION, BAC_SY_STARS

# Thai Tue ring
from .phu_tinh_thai_tue import THAI_TUE_STARS, TUE_STARS

# Other stars
from .phu_tinh_other import (
    THIEN_MA_POSITION, HONG_LOAN_THIEN_HY, DAO_HOA_POSITION, HOA_CAI_POSITION,
    LONG_NGUYET_DUC, THIEN_QUAN_PHUC, THIEN_THUONG_SU_BASE, PHONG_CAO_POSITION,
    QUOC_AN_POSITION, DUONG_PHU_POSITION, THIEN_THO_TAI, THIEN_DIEU_POSITION,
    THIEN_LA_POSITION, DIA_VONG_POSITION, AN_QUANG_THIEN_QUY, THIEN_HINH_POSITION,
    TAM_THAI_BASE, BAT_TOA_BASE, THIEN_TRU_POSITION, calculate_dia_giai, LN_VAN_TINH
)

# Tu Hoa
from .tu_hoa import TU_HOA_TABLE

# Star Brightness (Miếu Vượng Đắc Hãm)
from .star_brightness import STAR_BRIGHTNESS_TABLE, BRIGHTNESS_LEVELS, get_star_brightness, get_brightness_display

# Tuần Triệt và các sao phụ quan trọng
from .phu_tinh_tuan_triet import (
    TRIET_POSITION, CO_THAN_QUA_TU, THAI_PHU_PHONG_CAC,
    GIAI_THAN_THIEN_GIAI, THIEN_DUC_NGUYET_DUC_YEAR,
    KIEP_SAT_POSITION, PHA_TOAI_POSITION,
    THIEN_VU_POSITION, THIEN_TAI_THO_YEAR, calculate_tuan_position,
    LUU_HA_POSITION
)

# Star Details (Chi tiết sao theo UC-03)
from .star_details import CHINH_TINH_DETAILS, get_star_detail

# Sao bổ sung để đạt >= 114 sao
from .phu_tinh_bo_sung import (
    LONG_TRI_PHUONG_CAC, THIEN_RIEU_POSITION, 
    MENH_CHU_TABLE, THAN_CHU_TABLE, 
    calculate_thien_khong, calculate_dau_quan,
    place_bo_sung_stars, get_menh_chu, get_than_chu
)