"""
ĐẠI LỤC NHÂM - BẢNG DỮ LIỆU
Dữ liệu lớn (JSON) được tải từ python/data/json/
Code chỉ giữ lại các mảng nhỏ, mapping và hàm tiện ích
"""

import json
import os
from typing import Dict, List, Tuple, Optional

# ═══════════════════════════════════════════════════════════════════════════════
# LOAD JSON DATA
# ═══════════════════════════════════════════════════════════════════════════════

_JSON_DIR = os.path.join(os.path.dirname(__file__), 'json')


def _load_json(filename: str) -> dict:
    filepath = os.path.join(_JSON_DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


# ═══════════════════════════════════════════════════════════════════════════════
# THIÊN CAN & ĐỊA CHI
# ═══════════════════════════════════════════════════════════════════════════════

THIEN_CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']

THIEN_CAN_HAN = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
DIA_CHI_HAN = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']

# ═══════════════════════════════════════════════════════════════════════════════
# LỤC NHÂM - 6 TỔ HỢP NHÂM
# ═══════════════════════════════════════════════════════════════════════════════

LUC_NHAM = [
    {'can': 8, 'chi': 8,  'name': 'Nhâm Thân', 'han': '壬申',
     'giai_doan': 'Trưởng Sinh', 'y_nghia': 'Khởi đầu sinh trưởng, năng lượng manh nha'},
    {'can': 8, 'chi': 6,  'name': 'Nhâm Ngọ', 'han': '壬午',
     'giai_doan': 'Đế Vượng', 'y_nghia': 'Đỉnh cao cực thịnh, toàn lực phát huy'},
    {'can': 8, 'chi': 4,  'name': 'Nhâm Thìn', 'han': '壬辰',
     'giai_doan': 'Mộ Khố', 'y_nghia': 'Thu gom tinh hoa, tàng trữ năng lượng'},
    {'can': 8, 'chi': 2,  'name': 'Nhâm Dần', 'han': '壬寅',
     'giai_doan': 'Bệnh Suy', 'y_nghia': 'Suy giảm dần, cần bảo toàn lực lượng'},
    {'can': 8, 'chi': 0,  'name': 'Nhâm Tý', 'han': '壬子',
     'giai_doan': 'Lâm Quan', 'y_nghia': 'Vào vị trí quyền lực, nắm thực quyền'},
    {'can': 8, 'chi': 10, 'name': 'Nhâm Tuất', 'han': '壬戌',
     'giai_doan': 'Tuyệt Tàn', 'y_nghia': 'Chu kỳ kết thúc, chuẩn bị tái sinh'},
]

# ═══════════════════════════════════════════════════════════════════════════════
# THẬP NHỊ THẦN TƯỚNG (loaded from JSON)
# ═══════════════════════════════════════════════════════════════════════════════

THAP_NHI_THAN_TUONG: Dict = _load_json('luc_nham_than_tuong.json')

THAN_TUONG_ORDER = [
    'Quý Nhân', 'Đằng Xà', 'Chu Tước', 'Lục Hợp', 'Câu Trận', 'Thanh Long',
    'Thiên Không', 'Bạch Hổ', 'Thái Thường', 'Huyền Vũ', 'Thái Âm', 'Thiên Hậu',
]

# ═══════════════════════════════════════════════════════════════════════════════
# BÀN THỨC - ĐỊA BÀN (12 Cung cố định)
# ═══════════════════════════════════════════════════════════════════════════════

DIA_BAN = {
    0:  {'chi': 'Tý',   'han': '子', 'huong': 'Bắc',       'ngu_hanh': 'Thủy'},
    1:  {'chi': 'Sửu',  'han': '丑', 'huong': 'Đông Bắc',  'ngu_hanh': 'Thổ'},
    2:  {'chi': 'Dần',  'han': '寅', 'huong': 'Đông Bắc',  'ngu_hanh': 'Mộc'},
    3:  {'chi': 'Mão',  'han': '卯', 'huong': 'Đông',      'ngu_hanh': 'Mộc'},
    4:  {'chi': 'Thìn', 'han': '辰', 'huong': 'Đông Nam',  'ngu_hanh': 'Thổ'},
    5:  {'chi': 'Tỵ',   'han': '巳', 'huong': 'Đông Nam',  'ngu_hanh': 'Hỏa'},
    6:  {'chi': 'Ngọ',  'han': '午', 'huong': 'Nam',       'ngu_hanh': 'Hỏa'},
    7:  {'chi': 'Mùi',  'han': '未', 'huong': 'Tây Nam',   'ngu_hanh': 'Thổ'},
    8:  {'chi': 'Thân', 'han': '申', 'huong': 'Tây Nam',   'ngu_hanh': 'Kim'},
    9:  {'chi': 'Dậu',  'han': '酉', 'huong': 'Tây',       'ngu_hanh': 'Kim'},
    10: {'chi': 'Tuất', 'han': '戌', 'huong': 'Tây Bắc',   'ngu_hanh': 'Thổ'},
    11: {'chi': 'Hợi',  'han': '亥', 'huong': 'Tây Bắc',   'ngu_hanh': 'Thủy'},
}

# ═══════════════════════════════════════════════════════════════════════════════
# NGŨ HÀNH CỦA THIÊN CAN & ÂM DƯƠNG
# ═══════════════════════════════════════════════════════════════════════════════

CAN_NGU_HANH = {
    0: 'Mộc', 1: 'Mộc', 2: 'Hỏa', 3: 'Hỏa', 4: 'Thổ',
    5: 'Thổ', 6: 'Kim', 7: 'Kim', 8: 'Thủy', 9: 'Thủy',
}

CAN_AM_DUONG = {
    0: 'Dương', 1: 'Âm', 2: 'Dương', 3: 'Âm', 4: 'Dương',
    5: 'Âm', 6: 'Dương', 7: 'Âm', 8: 'Dương', 9: 'Âm',
}

# ═══════════════════════════════════════════════════════════════════════════════
# TỨ KHÓA & TAM TRUYỀN INFO
# ═══════════════════════════════════════════════════════════════════════════════

TU_KHOA_INFO = {
    1: {'ten': 'Khóa 1 - Can Ngày', 'han': '第一課',
        'vai_tro': 'Bản chất nội tại', 'mo_ta': 'Nguyên nhân sâu xa của sự việc, bản chất căn gốc',
        'chien_luoc': 'Phân tích nền tảng, gốc rễ vấn đề'},
    2: {'ten': 'Khóa 2 - Chi Ngày', 'han': '第二課',
        'vai_tro': 'Hoàn cảnh khách quan', 'mo_ta': 'Sự kiên định, các yếu tố bên ngoài ràng buộc',
        'chien_luoc': 'Đánh giá môi trường và rào cản'},
    3: {'ten': 'Khóa 3 - Can Giờ', 'han': '第三課',
        'vai_tro': 'Động lực kích hoạt', 'mo_ta': 'Tác nhân bùng phát hiện tại, yếu tố thời cơ',
        'chien_luoc': 'Nắm bắt hay trì hoãn tùy mạnh yếu'},
    4: {'ten': 'Khóa 4 - Chi Giờ', 'han': '第四課',
        'vai_tro': 'Định hướng tương lai', 'mo_ta': 'Xu hướng phát triển trong tương lai gần',
        'chien_luoc': 'Dự đoán kết quả và điều chỉnh'},
}

TAM_TRUYEN_INFO = {
    'so_truyen': {
        'ten': 'Sơ Truyền', 'han': '初傳', 'vai_tro': 'Điểm bùng phát',
        'mo_ta': 'Thời điểm sự kiện manh nha, bước ra từ bóng tối xác suất',
        'quantum_analog': 'Sụp đổ hàm sóng (Wave Function Collapse)'},
    'trung_truyen': {
        'ten': 'Trung Truyền', 'han': '中傳', 'vai_tro': 'Chuyển hóa',
        'mo_ta': 'Quá trình diễn tiến, năng lượng biến đổi dạng thức',
        'quantum_analog': 'Tiến hóa đơn nhất (Unitary Evolution)'},
    'mat_truyen': {
        'ten': 'Mạt Truyền', 'han': '末傳', 'vai_tro': 'Kết cục',
        'mo_ta': 'Kết thúc chu kỳ nhân quả, hiện thực hóa hoàn toàn',
        'quantum_analog': 'Trạng thái riêng (Eigenstate)'},
}

# ═══════════════════════════════════════════════════════════════════════════════
# CAN KÝ CUNG & NGUYỆT TƯỚNG
# ═══════════════════════════════════════════════════════════════════════════════

CAN_KY_CUNG = {
    0: 2, 1: 4, 2: 5, 3: 6, 4: 5,
    5: 6, 6: 8, 7: 9, 8: 11, 9: 0,
}

NGUYET_TUONG = {
    0: 11, 1: 10, 2: 9, 3: 8, 4: 7, 5: 6,
    6: 5, 7: 4, 8: 3, 9: 2, 10: 1, 11: 0,
}

NGUYET_TUONG_TEN = {
    0: 'Thần Hậu', 1: 'Đại Cát', 2: 'Công Tào', 3: 'Thái Xung',
    4: 'Thiên Cương', 5: 'Thái Ất', 6: 'Thắng Quang', 7: 'Tiểu Cát',
    8: 'Truyền Tống', 9: 'Tòng Khôi', 10: 'Hà Khôi', 11: 'Đăng Minh',
}

# ═══════════════════════════════════════════════════════════════════════════════
# QUÝ NHÂN KHỞI
# ═══════════════════════════════════════════════════════════════════════════════

QUY_NHAN_KHOI = {
    0: (1, 7), 1: (0, 8), 2: (11, 9), 3: (11, 9), 4: (1, 7),
    5: (0, 8), 6: (7, 1), 7: (6, 2), 8: (5, 3), 9: (5, 3),
}

# ═══════════════════════════════════════════════════════════════════════════════
# NGŨ HÀNH TƯƠNG SINH TƯƠNG KHẮC
# ═══════════════════════════════════════════════════════════════════════════════

NGU_HANH_SINH = {
    'Kim': 'Thủy', 'Thủy': 'Mộc', 'Mộc': 'Hỏa', 'Hỏa': 'Thổ', 'Thổ': 'Kim',
}
NGU_HANH_KHAC = {
    'Kim': 'Mộc', 'Mộc': 'Thổ', 'Thổ': 'Thủy', 'Thủy': 'Hỏa', 'Hỏa': 'Kim',
}

# ═══════════════════════════════════════════════════════════════════════════════
# DỮ LIỆU TỪ JSON (Động vật, 28 Tú, Quantum/Vedic, Khóa Thể)
# ═══════════════════════════════════════════════════════════════════════════════

_extra = _load_json('luc_nham_extra.json')

# Chuyển key string -> int cho dong_vat
DONG_VAT_DIA_BAN: Dict[int, List[str]] = {
    int(k): v for k, v in _extra['dong_vat_dia_ban'].items()
}

QUANTUM_VEDIC_ISOMORPHISM: Dict = _extra['quantum_vedic_isomorphism']
KHOA_THE: Dict = _extra['khoa_the']

NHI_THAP_BAT_TU: Dict = _load_json('luc_nham_nhi_thap_bat_tu.json')

# ═══════════════════════════════════════════════════════════════════════════════
# HÀM TIỆN ÍCH
# ═══════════════════════════════════════════════════════════════════════════════

def get_ngu_hanh_relation(hanh_a: str, hanh_b: str) -> str:
    """Xác định quan hệ Ngũ Hành: 'sinh', 'bi_sinh', 'khac', 'bi_khac', 'hoa'"""
    if hanh_a == hanh_b:
        return 'hoa'
    if NGU_HANH_SINH.get(hanh_a) == hanh_b:
        return 'sinh'
    if NGU_HANH_SINH.get(hanh_b) == hanh_a:
        return 'bi_sinh'
    if NGU_HANH_KHAC.get(hanh_a) == hanh_b:
        return 'khac'
    if NGU_HANH_KHAC.get(hanh_b) == hanh_a:
        return 'bi_khac'
    return 'hoa'


def get_relation_score(relation: str) -> int:
    """Chuyển quan hệ Ngũ Hành thành điểm số"""
    scores = {'sinh': 3, 'bi_sinh': 2, 'hoa': 1, 'bi_khac': -2, 'khac': -3}
    return scores.get(relation, 0)


def get_than_tuong_by_index(idx: int) -> str:
    """Lấy tên Thần Tướng theo index 0-11"""
    return THAN_TUONG_ORDER[idx % 12]


def get_dia_chi_ngu_hanh(chi_idx: int) -> str:
    """Lấy Ngũ Hành của Địa Chi"""
    return DIA_BAN[chi_idx % 12]['ngu_hanh']
