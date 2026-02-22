"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ĐẠI LỤC NHÂM ENGINE                                     ║
║             Grand Six Ren Divination - Core Engine                          ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Chức năng:                                                                 ║
║  1. Xoay Thiên Bàn theo Nguyệt Tướng + Giờ chiêm                          ║
║  2. An 12 Thần Tướng (Quý Nhân khởi theo Can ngày)                        ║
║  3. Lập Tứ Khóa (Four Classes) từ Can-Chi Ngày-Giờ                        ║
║  4. Chiết xuất Tam Truyền (Three Transmissions)                            ║
║  5. Xác định Khóa Thể (9 loại)                                            ║
║  6. Luận giải cát hung + quantum correlation                               ║
║  7. Knowledge Graph (Ontology): RDF Reification + Vedic Force Routing      ║
║                                                                              ║
║  Toán học đẳng cấu:                                                         ║
║  12 Thần Tướng × 12 Địa Chi × 12 canh giờ = 1.440 cấu hình               ║
║  ≡ 720 cặp hạt Vệ Đà (Vedic Nuclear Physics)                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from typing import Dict, List, Tuple, Optional
from math import floor

from data.luc_nham_tables import (
    THIEN_CAN, DIA_CHI, THIEN_CAN_HAN, DIA_CHI_HAN,
    LUC_NHAM, THAP_NHI_THAN_TUONG, THAN_TUONG_ORDER,
    DIA_BAN, CAN_NGU_HANH, CAN_AM_DUONG, CAN_KY_CUNG,
    TU_KHOA_INFO, TAM_TRUYEN_INFO, KHOA_THE,
    NGUYET_TUONG, NGUYET_TUONG_TEN,
    QUY_NHAN_KHOI, DONG_VAT_DIA_BAN, NHI_THAP_BAT_TU,
    QUANTUM_VEDIC_ISOMORPHISM,
    get_ngu_hanh_relation, get_relation_score,
    get_than_tuong_by_index, get_dia_chi_ngu_hanh,
)
from core.jie_qi_calculator import get_tiet_khi, jd_from_date
from core.ngu_hanh_engine import NguHanhEngine


class LucNhamEngine:
    """
    Engine tính toán Đại Lục Nhâm

    Bàn thức Thiên Viên Địa Phương:
    - Địa bàn (vuông, cố định): 12 Cung cố định theo Địa Chi
    - Thiên bàn (tròn, xoay): Xoay theo Nguyệt Tướng + Giờ chiêm
    - 12 Thần Tướng: An theo Can ngày và ban ngày/đêm
    
    Input: Năm, Tháng, Ngày, Giờ (dương lịch)
    Output: Tứ Khóa, Tam Truyền, Thần Tướng, Bàn Thức hoàn chỉnh
    
    Tổng cấu hình: 1.440 (đẳng cấu với 720 cặp hạt Vệ Đà)
    """

    def __init__(self, year: int, month: int, day: int, hour: int = 0):
        """
        Khởi tạo Đại Lục Nhâm Engine

        Args:
            year: Năm dương lịch
            month: Tháng (1-12)
            day: Ngày (1-31)
            hour: Giờ (0-23)
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour

        # === Bước 1: Tính Can Chi Ngày ===
        self._calc_can_chi_day()

        # === Bước 2: Tính Can Chi Giờ ===
        self._calc_can_chi_hour()

        # === Bước 3: Tính Tiết Khí → Nguyệt Tướng ===
        self._calc_nguyet_tuong()

        # === Bước 4: Xoay Thiên Bàn ===
        self._rotate_thien_ban()

        # === Bước 5: An 12 Thần Tướng ===
        self._place_than_tuong()

        # === Bước 6: Lập Tứ Khóa ===
        self._calc_tu_khoa()

        # === Bước 7: Chiết xuất Tam Truyền ===
        self._calc_tam_truyen()

        # === Bước 8: Xác định Khóa Thể ===
        self._determine_khoa_the()

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 1: CAN CHI NGÀY
    # ═══════════════════════════════════════════════════════════════════════════

    def _calc_can_chi_day(self):
        """Tính Can Chi ngày từ Julius Day"""
        try:
            jd = jd_from_date(self.day, self.month, self.year)
            self.can_ngay = int((jd + 9) % 10)
            self.chi_ngay = int((jd + 1) % 12)
        except Exception:
            # Fallback: Dùng công thức Zeller đơn giản
            a = (14 - self.month) // 12
            y = self.year + 4800 - a
            m = self.month + 12 * a - 3
            jdn = self.day + (153 * m + 2) // 5 + 365 * y + y // 4 - y // 100 + y // 400 - 32045
            self.can_ngay = (jdn + 9) % 10
            self.chi_ngay = (jdn + 1) % 12

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 2: CAN CHI GIỜ
    # ═══════════════════════════════════════════════════════════════════════════

    def _calc_can_chi_hour(self):
        """
        Tính Can Chi giờ
        Chi giờ: (hour + 1) // 2 % 12
        Can giờ: (Can ngày * 2 + Chi giờ) % 10
        """
        self.chi_gio = ((self.hour + 1) // 2) % 12
        self.can_gio = (self.can_ngay * 2 + self.chi_gio) % 10

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 3: NGUYỆT TƯỚNG
    # ═══════════════════════════════════════════════════════════════════════════

    def _calc_nguyet_tuong(self):
        """
        Tính Nguyệt Tướng dựa trên Tiết Khí
        Nguyệt Tướng = Địa Chi đối diện Mặt Trời
        """
        try:
            tiet_khi_info = get_tiet_khi(self.day, self.month, self.year)
            tiet_idx = tiet_khi_info['index']
            # Chuyển 24 tiết khí thành 12 Nguyệt Tướng (mỗi Nguyệt Tướng 2 tiết)
            nguyet_idx = (tiet_idx // 2) % 12
        except Exception:
            # Fallback: Ước tính từ tháng
            nguyet_idx = (self.month - 1) % 12

        self.nguyet_tuong_idx = NGUYET_TUONG.get(nguyet_idx, 0)
        self.nguyet_tuong_ten = NGUYET_TUONG_TEN.get(self.nguyet_tuong_idx, 'Thần Hậu')

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 4: XOAY THIÊN BÀN
    # Thiên bàn xoay bằng cách đặt Nguyệt Tướng lên cung Giờ chiêm
    # ═══════════════════════════════════════════════════════════════════════════

    def _rotate_thien_ban(self):
        """
        Xoay Thiên Bàn: đặt Nguyệt Tướng lên cung Giờ chiêm

        Công thức: offset = Nguyệt Tướng - Chi Giờ
        Thiên bàn[địa_bàn_i] = (địa_bàn_i + offset) % 12
        """
        offset = (self.nguyet_tuong_idx - self.chi_gio) % 12

        # thien_ban[dia_ban_pos] → thiên_chi chiếm vị trí dia_ban_pos
        self.thien_ban = {}
        for dia_pos in range(12):
            thien_chi = (dia_pos + offset) % 12
            self.thien_ban[dia_pos] = thien_chi

        # Reverse map: thien_chi → dia_ban_pos
        self.thien_to_dia = {}
        for dia_pos, thien_chi in self.thien_ban.items():
            self.thien_to_dia[thien_chi] = dia_pos

        self.thien_ban_offset = offset

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 5: AN 12 THẦN TƯỚNG
    # Quý Nhân khởi từ cung theo Can ngày + ban ngày/đêm
    # Sau đó các Thần Tướng còn lại lần lượt thuận/nghịch
    # ═══════════════════════════════════════════════════════════════════════════

    def _place_than_tuong(self):
        """
        An 12 Thần Tướng vào các Cung

        1. Xác định Quý Nhân vị trí theo Can ngày
        2. Ban ngày (6h-18h) → Quý Nhân ban ngày, thuận
        3. Ban đêm (18h-6h) → Quý Nhân ban đêm, nghịch
        4. Các Thần Tướng khác lần lượt từ Quý Nhân
        """
        is_day = 6 <= self.hour < 18
        qn_day, qn_night = QUY_NHAN_KHOI.get(self.can_ngay, (1, 7))

        qn_pos = qn_day if is_day else qn_night
        direction = 1 if is_day else -1  # Thuận: +1, Nghịch: -1

        # An Thần Tướng
        self.than_tuong_map = {}  # dia_chi_idx → tên Thần Tướng
        for i, than_name in enumerate(THAN_TUONG_ORDER):
            pos = (qn_pos + direction * i) % 12
            self.than_tuong_map[pos] = than_name

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 6: TỨ KHÓA (Four Classes)
    #
    # Khóa 1: Thượng thần của Can Ngày (Thiên bàn chi trên cung Can ký gửi)
    # Khóa 2: Thượng thần của Chi Ngày (Thiên bàn chi trên cung Chi Ngày)
    # Khóa 3: Thượng thần của Can Giờ (Thiên bàn chi trên cung Can ký gửi)
    # Khóa 4: Thượng thần của Chi Giờ (Thiên bàn chi trên cung Chi Giờ)
    # ═══════════════════════════════════════════════════════════════════════════

    def _calc_tu_khoa(self):
        """
        Lập Tứ Khóa

        Mỗi Khóa gồm: hạ thần (gốc) + thượng thần (Thiên bàn chi đè lên)
        """
        # Can Ngày → Cung ký gửi
        can_ngay_cung = CAN_KY_CUNG.get(self.can_ngay, 0)

        # Can Giờ → Cung ký gửi
        can_gio_cung = CAN_KY_CUNG.get(self.can_gio, 0)

        def _get_thuong_than(ha_than_chi: int) -> int:
            """Lấy Thượng thần trên Thiên bàn tại cung ha_than_chi"""
            return self.thien_ban.get(ha_than_chi, 0)

        self.tu_khoa = []

        # Khóa 1: Can Ngày
        ha1 = can_ngay_cung
        thuong1 = _get_thuong_than(ha1)
        self.tu_khoa.append({
            'khoa': 1,
            'ha_than': ha1,
            'thuong_than': thuong1,
            'ha_ten': DIA_CHI[ha1],
            'thuong_ten': DIA_CHI[thuong1],
            'info': TU_KHOA_INFO[1],
            'ngu_hanh_ha': get_dia_chi_ngu_hanh(ha1),
            'ngu_hanh_thuong': get_dia_chi_ngu_hanh(thuong1),
        })

        # Khóa 2: Chi Ngày
        ha2 = self.chi_ngay
        thuong2 = _get_thuong_than(ha2)
        self.tu_khoa.append({
            'khoa': 2,
            'ha_than': ha2,
            'thuong_than': thuong2,
            'ha_ten': DIA_CHI[ha2],
            'thuong_ten': DIA_CHI[thuong2],
            'info': TU_KHOA_INFO[2],
            'ngu_hanh_ha': get_dia_chi_ngu_hanh(ha2),
            'ngu_hanh_thuong': get_dia_chi_ngu_hanh(thuong2),
        })

        # Khóa 3: Can Giờ
        ha3 = can_gio_cung
        thuong3 = _get_thuong_than(ha3)
        self.tu_khoa.append({
            'khoa': 3,
            'ha_than': ha3,
            'thuong_than': thuong3,
            'ha_ten': DIA_CHI[ha3],
            'thuong_ten': DIA_CHI[thuong3],
            'info': TU_KHOA_INFO[3],
            'ngu_hanh_ha': get_dia_chi_ngu_hanh(ha3),
            'ngu_hanh_thuong': get_dia_chi_ngu_hanh(thuong3),
        })

        # Khóa 4: Chi Giờ
        ha4 = self.chi_gio
        thuong4 = _get_thuong_than(ha4)
        self.tu_khoa.append({
            'khoa': 4,
            'ha_than': ha4,
            'thuong_than': thuong4,
            'ha_ten': DIA_CHI[ha4],
            'thuong_ten': DIA_CHI[thuong4],
            'info': TU_KHOA_INFO[4],
            'ngu_hanh_ha': get_dia_chi_ngu_hanh(ha4),
            'ngu_hanh_thuong': get_dia_chi_ngu_hanh(thuong4),
        })

        # Tính điểm từng Khóa
        for k in self.tu_khoa:
            rel = get_ngu_hanh_relation(k['ngu_hanh_thuong'], k['ngu_hanh_ha'])
            k['quan_he'] = rel
            k['diem'] = get_relation_score(rel)

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 7: TAM TRUYỀN (Three Transmissions)
    #
    # Sơ Truyền: Lấy từ Khóa có Thượng thần khắc Hạ thần
    #   - Nếu nhiều khóa khắc → lấy khóa có khắc lực mạnh nhất
    #   - Nếu không khóa nào khắc → dùng phương pháp Biệt Trách
    # Trung Truyền: Thượng thần trên cung Sơ Truyền
    # Mạt Truyền: Thượng thần trên cung Trung Truyền
    # ═══════════════════════════════════════════════════════════════════════════

    def _calc_tam_truyen(self):
        """
        Chiết xuất Tam Truyền từ Tứ Khóa

        Nguyên tắc: Thượng khắc Hạ (Tặc) → lấy Tặc,
        nếu không có Tặc → Hạ khắc Thượng (Khắc)
        nếu không có gì → Biệt Trách (dùng Can Ngày liên quan)
        """
        # Tìm Sơ Truyền
        so_truyen_chi = None

        # Ưu tiên 1: Thượng khắc Hạ (Tặc khóa)
        tac_khoas = []
        for k in self.tu_khoa:
            hanh_thuong = k['ngu_hanh_thuong']
            hanh_ha = k['ngu_hanh_ha']
            from data.luc_nham_tables import NGU_HANH_KHAC
            if NGU_HANH_KHAC.get(hanh_thuong) == hanh_ha:
                tac_khoas.append(k)

        if tac_khoas:
            # Nếu nhiều Tặc khóa → Lấy khóa cuối (Khóa 4 > 3 > 2 > 1)
            if len(tac_khoas) == 1:
                so_truyen_chi = tac_khoas[0]['thuong_than']
            else:
                so_truyen_chi = tac_khoas[-1]['thuong_than']
        else:
            # Ưu tiên 2: Hạ khắc Thượng (Khắc khóa)
            khac_khoas = []
            for k in self.tu_khoa:
                hanh_thuong = k['ngu_hanh_thuong']
                hanh_ha = k['ngu_hanh_ha']
                if NGU_HANH_KHAC.get(hanh_ha) == hanh_thuong:
                    khac_khoas.append(k)

            if khac_khoas:
                so_truyen_chi = khac_khoas[-1]['thuong_than']
            else:
                # Biệt Trách: Dùng Thượng thần Khóa 1
                so_truyen_chi = self.tu_khoa[0]['thuong_than']

        # Trung Truyền: Thiên bàn chi trên cung Sơ Truyền
        trung_truyen_chi = self.thien_ban.get(so_truyen_chi, 0)

        # Mạt Truyền: Thiên bàn chi trên cung Trung Truyền
        mat_truyen_chi = self.thien_ban.get(trung_truyen_chi, 0)

        self.tam_truyen = {
            'so_truyen': {
                'chi': so_truyen_chi,
                'ten': DIA_CHI[so_truyen_chi],
                'han': DIA_CHI_HAN[so_truyen_chi],
                'ngu_hanh': get_dia_chi_ngu_hanh(so_truyen_chi),
                'than_tuong': self.than_tuong_map.get(so_truyen_chi, ''),
                'info': TAM_TRUYEN_INFO['so_truyen'],
            },
            'trung_truyen': {
                'chi': trung_truyen_chi,
                'ten': DIA_CHI[trung_truyen_chi],
                'han': DIA_CHI_HAN[trung_truyen_chi],
                'ngu_hanh': get_dia_chi_ngu_hanh(trung_truyen_chi),
                'than_tuong': self.than_tuong_map.get(trung_truyen_chi, ''),
                'info': TAM_TRUYEN_INFO['trung_truyen'],
            },
            'mat_truyen': {
                'chi': mat_truyen_chi,
                'ten': DIA_CHI[mat_truyen_chi],
                'han': DIA_CHI_HAN[mat_truyen_chi],
                'ngu_hanh': get_dia_chi_ngu_hanh(mat_truyen_chi),
                'than_tuong': self.than_tuong_map.get(mat_truyen_chi, ''),
                'info': TAM_TRUYEN_INFO['mat_truyen'],
            },
        }

    # ═══════════════════════════════════════════════════════════════════════════
    # BƯỚC 8: KHÓA THỂ
    # ═══════════════════════════════════════════════════════════════════════════

    def _determine_khoa_the(self):
        """
        Xác định loại Khóa Thể dựa trên đặc điểm Tứ Khóa
        """
        # Kiểm tra Phục Ngâm (Thiên = Địa)
        if self.thien_ban_offset == 0:
            self.khoa_the = KHOA_THE['phuc_ngam']
            return

        # Kiểm tra Phản Ngâm (Thiên xung Địa, offset = 6)
        if self.thien_ban_offset == 6:
            self.khoa_the = KHOA_THE['phan_ngam']
            return

        # Phân tích Tứ Khóa
        diem_tong = sum(k['diem'] for k in self.tu_khoa)
        khac_count = sum(1 for k in self.tu_khoa if k['quan_he'] in ('khac', 'bi_khac'))
        sinh_count = sum(1 for k in self.tu_khoa if k['quan_he'] in ('sinh', 'bi_sinh'))

        # Tất cả sinh
        if sinh_count == 4:
            self.khoa_the = KHOA_THE['duoc_do']
            return

        # Tất cả khắc
        if khac_count == 4:
            self.khoa_the = KHOA_THE['thiep_kinh']
            return

        # Trùng thẩm (2 khóa giống nhau)
        thuong_list = [k['thuong_than'] for k in self.tu_khoa]
        if len(set(thuong_list)) < 4:
            self.khoa_the = KHOA_THE['trung_thiem']
            return

        # Can Ngày mạnh, khóa khác yếu
        if self.tu_khoa[0]['diem'] > 0 and diem_tong <= 0:
            self.khoa_the = KHOA_THE['tri_nhat']
            return

        # Can Giờ khắc Can Ngày mạnh
        if self.tu_khoa[2]['diem'] < 0 and self.tu_khoa[0]['diem'] > 0:
            self.khoa_the = KHOA_THE['phat_dung']
            return

        # Cân bằng hoàn hảo
        if abs(diem_tong) <= 1 and khac_count == sinh_count:
            self.khoa_the = KHOA_THE['bat_bi']
            return

        # Default: Nguyên Thủ (thuận sinh)
        if diem_tong > 0:
            self.khoa_the = KHOA_THE['nguyen_thu']
        else:
            self.khoa_the = KHOA_THE['thiep_kinh']

    # ═══════════════════════════════════════════════════════════════════════════
    # LUẬN GIẢI
    # ═══════════════════════════════════════════════════════════════════════════

    def _analyze_strategy(self) -> Dict:
        """
        Phân tích chiến lược hành động dựa trên Tứ Khóa

        Logic:
        - Can Ngày mạnh + Can Giờ yếu → Nền tảng tốt nhưng thiếu động lực → Trì hoãn
        - Can Ngày yếu + Can Giờ mạnh → Nền tảng yếu nhưng cơ hội đến → Chớp thời cơ
        - Cả hai mạnh → Đại cát, hành động mạnh mẽ
        - Cả hai yếu → Không nên hành động
        """
        k1_diem = self.tu_khoa[0]['diem']  # Can Ngày
        k3_diem = self.tu_khoa[2]['diem']  # Can Giờ

        if k1_diem > 0 and k3_diem > 0:
            return {
                'chien_luoc': 'Hành động mạnh mẽ',
                'icon': '⚡',
                'mo_ta': 'Nền tảng vững chắc + Động lực mạnh. Thời cơ vàng để quyết định lớn.',
                'muc_do': 'Đại Cát',
            }
        elif k1_diem > 0 and k3_diem <= 0:
            return {
                'chien_luoc': 'Trì hoãn, chờ thời',
                'icon': '⏳',
                'mo_ta': 'Nền tảng tốt nhưng thiếu động lực kích hoạt. Chuẩn bị và chờ đợi cơ hội.',
                'muc_do': 'Cát (chờ)',
            }
        elif k1_diem <= 0 and k3_diem > 0:
            return {
                'chien_luoc': 'Chớp thời cơ ngay',
                'icon': '🎯',
                'mo_ta': ('Nền tảng yếu nhưng cửa sổ thời cơ đang mở. '
                          'Phải hành động ngay trước khi cơ hội qua đi!'),
                'muc_do': 'Cát (gấp)',
            }
        else:
            return {
                'chien_luoc': 'Không nên hành động',
                'icon': '🛑',
                'mo_ta': 'Cả nền tảng lẫn động lực đều yếu. An phận thủ thường, chờ chu kỳ mới.',
                'muc_do': 'Hung',
            }

    def _analyze_ban_thuc(self) -> List[Dict]:
        """
        Phân tích bàn thức 12 cung (Thiên bàn + Địa bàn + Thần Tướng)
        """
        cung_analysis = []
        for dia_pos in range(12):
            thien_chi = self.thien_ban[dia_pos]
            dia_info = DIA_BAN[dia_pos]
            than_tuong_name = self.than_tuong_map.get(dia_pos, '')
            than_tuong_info = THAP_NHI_THAN_TUONG.get(than_tuong_name, {})

            # Ngũ Hành
            hanh_dia = dia_info['ngu_hanh']
            hanh_thien = get_dia_chi_ngu_hanh(thien_chi)
            relation = get_ngu_hanh_relation(hanh_thien, hanh_dia)
            score = get_relation_score(relation)

            # Thần Tướng bonus
            than_score = 0
            if than_tuong_info:
                tc = than_tuong_info.get('tinh_chat', 'trung')
                if tc == 'đại_cát':
                    than_score = 4
                elif tc == 'cát':
                    than_score = 2
                elif tc == 'hung':
                    than_score = -2
                elif tc == 'đại_hung':
                    than_score = -4

            total_score = score + than_score

            # Tính chất tổng hợp
            if total_score >= 4:
                nature = 'đại_cát'
            elif total_score >= 2:
                nature = 'cát'
            elif total_score >= -1:
                nature = 'trung'
            elif total_score >= -3:
                nature = 'hung'
            else:
                nature = 'đại_hung'

            # Động vật
            dong_vat = DONG_VAT_DIA_BAN.get(dia_pos, [])

            cung_analysis.append({
                'dia_pos': dia_pos,
                'dia_chi': dia_info['chi'],
                'dia_han': dia_info['han'],
                'huong': dia_info['huong'],
                'thien_chi': DIA_CHI[thien_chi],
                'thien_han': DIA_CHI_HAN[thien_chi],
                'thien_chi_idx': thien_chi,
                'than_tuong': than_tuong_name,
                'than_tuong_han': than_tuong_info.get('han', ''),
                'than_tuong_info': than_tuong_info,
                'hanh_dia': hanh_dia,
                'hanh_thien': hanh_thien,
                'quan_he': relation,
                'score': total_score,
                'nature': nature,
                'dong_vat': dong_vat,
                'nguyet_tuong_ten': NGUYET_TUONG_TEN.get(thien_chi, ''),
            })

        return cung_analysis

    def _get_nhi_thap_bat_tu_summary(self) -> Dict:
        """Lấy tóm tắt Nhị Thập Bát Tú"""
        return NHI_THAP_BAT_TU

    def _analyze_quantum_detail(self) -> Dict:
        """
        Phân tích chi tiết mối liên hệ Lục Nhâm ↔ Vật lý Lượng tử ↔ Vệ Đà
        dựa trên bàn thức thực tế đã tính.

        Returns:
            Dict chứa phân tích lượng tử động (dynamic) dựa trên chart cụ thể
        """
        # --- 1. Entropy & Superposition ---
        # Đếm số trạng thái unique trên bàn thức
        unique_thien = len(set(self.thien_ban.values()))
        unique_hanh = set()
        for pos in range(12):
            thien_chi = self.thien_ban[pos]
            unique_hanh.add(get_dia_chi_ngu_hanh(thien_chi))

        # Entropy Shannon: -Σ p_i × log2(p_i)
        from collections import Counter
        import math
        hanh_counts = Counter()
        for pos in range(12):
            hanh_counts[get_dia_chi_ngu_hanh(self.thien_ban[pos])] += 1

        entropy = 0.0
        for count in hanh_counts.values():
            p = count / 12
            if p > 0:
                entropy -= p * math.log2(p)

        max_entropy = math.log2(5)  # 5 Hành
        coherence = 1.0 - (entropy / max_entropy) if max_entropy > 0 else 0

        # --- 2. Entanglement: Tương quan đôi giữa Tứ Khóa ---
        entanglement_pairs = []
        for i in range(len(self.tu_khoa)):
            for j in range(i + 1, len(self.tu_khoa)):
                ki = self.tu_khoa[i]
                kj = self.tu_khoa[j]
                # Tương quan = cùng hành hoặc sinh/khắc
                rel_ij = get_ngu_hanh_relation(ki['ngu_hanh_thuong'], kj['ngu_hanh_thuong'])
                correlation = 1.0 if rel_ij == 'hoa' else (
                    0.7 if rel_ij in ('sinh', 'bi_sinh') else (
                    -0.7 if rel_ij in ('khac', 'bi_khac') else 0
                ))
                entanglement_pairs.append({
                    'pair': f"K{ki['khoa']}↔K{kj['khoa']}",
                    'khoa_a': f"K{ki['khoa']} ({ki['thuong_ten']})",
                    'khoa_b': f"K{kj['khoa']} ({kj['thuong_ten']})",
                    'hanh_a': ki['ngu_hanh_thuong'],
                    'hanh_b': kj['ngu_hanh_thuong'],
                    'relation': rel_ij,
                    'correlation': correlation,
                    'bell_state': self._get_bell_state(correlation),
                })

        # Avg entanglement
        avg_entanglement = sum(abs(p['correlation']) for p in entanglement_pairs) / max(len(entanglement_pairs), 1)

        # --- 3. Decoherence Timeline: Tam Truyền pathway ---
        tam_truyen_path = []
        stages = [
            ('so_truyen', 'Sơ Truyền', 'Superposition → Collapse', 'Brahma (Tạo)'),
            ('trung_truyen', 'Trung Truyền', 'Unitary Evolution', 'Vishnu (Duy trì)'),
            ('mat_truyen', 'Mạt Truyền', 'Eigenstate', 'Shiva (Hủy/Tái sinh)'),
        ]
        for key, name, quantum_phase, vedic_deity in stages:
            tt = self.tam_truyen[key]
            hanh = tt['ngu_hanh']
            tt_than = tt['than_tuong']
            # Quantum state description
            than_info = THAP_NHI_THAN_TUONG.get(tt_than, {})
            qv_map = QUANTUM_VEDIC_ISOMORPHISM.get('than_tuong_quantum', {}).get(tt_than, {})

            tam_truyen_path.append({
                'stage': name,
                'chi': tt['ten'],
                'han': tt['han'],
                'ngu_hanh': hanh,
                'than_tuong': tt_than,
                'quantum_phase': quantum_phase,
                'vedic_deity': vedic_deity,
                'particle': qv_map.get('particle', ''),
                'vedic_entity': qv_map.get('vedic', ''),
                'interpretation': tt['info']['mo_ta'],
            })

        # --- 4. Symmetry Breaking ---
        # Phân tích đối xứng bị phá vỡ khi "chiêm"
        offset = self.thien_ban_offset
        symmetry_type = 'Phục Ngâm (Đồng nhất)' if offset == 0 else (
            'Phản Ngâm (Nghịch đảo)' if offset == 6 else (
            f'Xoay φ = {offset}×30° = {offset * 30}°'
        ))

        # --- 5. Thần Tướng as Quantum Fields ---
        than_tuong_fields = []
        for pos, name in self.than_tuong_map.items():
            info = THAP_NHI_THAN_TUONG.get(name, {})
            qv = QUANTUM_VEDIC_ISOMORPHISM.get('than_tuong_quantum', {}).get(name, {})
            dia_chi = DIA_CHI[pos]
            thien_chi = DIA_CHI[self.thien_ban[pos]]
            than_tuong_fields.append({
                'ten': name,
                'han': info.get('han', ''),
                'cung': dia_chi,
                'thien': thien_chi,
                'ngu_hanh': info.get('ngu_hanh', ''),
                'tinh_chat': info.get('tinh_chat', 'trung'),
                'particle': qv.get('particle', '—'),
                'vedic': qv.get('vedic', '—'),
                'role': qv.get('role', ''),
            })

        # --- 6. Ngũ Hành distribution as Quantum Field Configuration ---
        ngu_hanh_dist = {}
        ngu_hanh_qmap = QUANTUM_VEDIC_ISOMORPHISM.get('ngu_hanh_quantum', {})
        for hanh, count in hanh_counts.items():
            qinfo = ngu_hanh_qmap.get(hanh, {})
            ngu_hanh_dist[hanh] = {
                'count': count,
                'percentage': round(count / 12 * 100, 1),
                'force': qinfo.get('force', ''),
                'boson': qinfo.get('boson', ''),
                'vedic': qinfo.get('vedic_element', ''),
                'coupling': qinfo.get('coupling', ''),
            }

        return {
            'superposition': {
                'total_states': 1440,
                'collapsed_to': 1,
                'unique_thien_chi': unique_thien,
                'unique_hanh': len(unique_hanh),
                'entropy': round(entropy, 3),
                'max_entropy': round(max_entropy, 3),
                'coherence': round(coherence, 3),
                'coherence_pct': round(coherence * 100, 1),
                'interpretation': self._interpret_coherence(coherence),
            },
            'entanglement': {
                'pairs': entanglement_pairs,
                'avg_entanglement': round(avg_entanglement, 3),
                'max_entangled_pair': max(entanglement_pairs, key=lambda x: abs(x['correlation']))['pair'] if entanglement_pairs else '',
                'interpretation': self._interpret_entanglement(avg_entanglement),
            },
            'decoherence_timeline': tam_truyen_path,
            'symmetry': {
                'offset': offset,
                'angle': offset * 30,
                'type': symmetry_type,
                'group': f'Z₁₂ rotation by {offset}',
                'broken': offset not in (0, 6),
            },
            'than_tuong_fields': than_tuong_fields,
            'ngu_hanh_distribution': ngu_hanh_dist,
        }

    @staticmethod
    def _get_bell_state(correlation: float) -> str:
        """Map correlation to Bell state type"""
        if correlation >= 0.9:
            return '|Φ⁺⟩ (maximally entangled, same)'
        elif correlation >= 0.5:
            return '|Φ⁺⟩ (partially entangled, cooperative)'
        elif correlation <= -0.5:
            return '|Ψ⁻⟩ (anti-correlated, antagonistic)'
        else:
            return '|sep⟩ (weakly coupled)'

    @staticmethod
    def _interpret_coherence(coherence: float) -> str:
        if coherence >= 0.7:
            return 'Năng lượng tập trung cao — bàn thức bị chi phối bởi 1-2 Hành, tạo xu hướng rõ ràng mạnh mẽ'
        elif coherence >= 0.4:
            return 'Năng lượng phân bố khá đều — tình huống nhiều mặt, cần phân tích đa chiều'
        else:
            return 'Năng lượng phân tán đều — trạng thái cân bằng động, nhiều khả năng mở'

    @staticmethod
    def _interpret_entanglement(avg: float) -> str:
        if avg >= 0.7:
            return 'Tứ Khóa tương quan mạnh — các yếu tố khóa chặt vào nhau, thay đổi một ảnh hưởng tất cả'
        elif avg >= 0.4:
            return 'Tứ Khóa tương quan trung bình — có sự liên kết nhưng còn độ tự do'
        else:
            return 'Tứ Khóa ít tương quan — các yếu tố khá độc lập, dễ tách biệt xử lý'

    @staticmethod
    def _get_quantum_vedic_map(than_tuong_name: str) -> Dict:
        """Lấy quantum-vedic mapping cho một Thần Tướng"""
        return QUANTUM_VEDIC_ISOMORPHISM.get(
            'than_tuong_quantum', {}
        ).get(than_tuong_name, {})

    # ═══════════════════════════════════════════════════════════════════════════
    # KNOWLEDGE GRAPH — ONTOLOGY (RDF/OWL/LPG)
    # ═══════════════════════════════════════════════════════════════════════════

    def build_knowledge_graph(self) -> Dict:
        """
        Xây dựng Knowledge Graph theo thiết kế Bản Thể Luận (Ontology).

        Tích hợp:
        - Entity Classes: HeavenlyStem, EarthlyBranch, SiKe_Anchor,
          SanChuan_Transmission, VedicDeva_Particle, etc.
        - RDF Reification: Interaction_Event cho trạng thái song song Cát/Hung
        - Algorithm 2: CASE WHEN operational_strategy (Tứ Khóa)
        - Algorithm 3: Vedic Force Routing (Tam Truyền)

        Returns:
            Dict chứa toàn bộ Knowledge Graph data
        """
        from logic.luc_nham_ontology import KnowledgeGraphBuilder
        builder = KnowledgeGraphBuilder(self)
        return builder.build()

    # ═══════════════════════════════════════════════════════════════════════════
    # OUTPUT CHÍNH
    # ═══════════════════════════════════════════════════════════════════════════

    def get_full_chart(self) -> Dict:
        """
        Xuất toàn bộ bàn thức Đại Lục Nhâm

        Returns:
            Dict chứa tất cả thông tin bàn thức:
            - input_info: Thông tin đầu vào
            - can_chi_info: Can Chi Ngày + Giờ
            - nguyet_tuong: Nguyệt Tướng
            - thien_ban: 12 cung Thiên bàn
            - than_tuong: 12 Thần Tướng phân bố
            - tu_khoa: Tứ Khóa
            - tam_truyen: Tam Truyền
            - khoa_the: Loại Khóa Thể
            - ban_thuc: Phân tích 12 cung
            - chien_luoc: Chiến lược hành động
            - quantum_vedic: Liên hệ Vật lý lượng tử & Vệ Đà
            - knowledge_graph: Đồ Thị Tri Thức (Ontology)
            - luc_nham_info: 6 tổ hợp Nhâm
        """
        ban_thuc = self._analyze_ban_thuc()
        chien_luoc = self._analyze_strategy()

        # Tìm hướng tốt nhất và xấu nhất
        sorted_cung = sorted(ban_thuc, key=lambda x: x['score'], reverse=True)
        best = sorted_cung[0]
        worst = sorted_cung[-1]

        return {
            'input_info': {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'hour': self.hour,
            },
            'can_chi_info': {
                'can_ngay': THIEN_CAN[self.can_ngay],
                'can_ngay_han': THIEN_CAN_HAN[self.can_ngay],
                'chi_ngay': DIA_CHI[self.chi_ngay],
                'chi_ngay_han': DIA_CHI_HAN[self.chi_ngay],
                'can_gio': THIEN_CAN[self.can_gio],
                'can_gio_han': THIEN_CAN_HAN[self.can_gio],
                'chi_gio': DIA_CHI[self.chi_gio],
                'chi_gio_han': DIA_CHI_HAN[self.chi_gio],
                'ngu_hanh_can_ngay': CAN_NGU_HANH[self.can_ngay],
                'ngu_hanh_can_gio': CAN_NGU_HANH[self.can_gio],
                'full_ngay': f"{THIEN_CAN[self.can_ngay]} {DIA_CHI[self.chi_ngay]}",
                'full_gio': f"{THIEN_CAN[self.can_gio]} {DIA_CHI[self.chi_gio]}",
            },
            'nguyet_tuong': {
                'chi': self.nguyet_tuong_idx,
                'ten': self.nguyet_tuong_ten,
                'dia_chi': DIA_CHI[self.nguyet_tuong_idx],
            },
            'thien_ban': {
                str(k): {
                    'dia_chi': DIA_CHI[k],
                    'thien_chi': DIA_CHI[v],
                    'thien_han': DIA_CHI_HAN[v],
                    'nguyet_tuong_ten': NGUYET_TUONG_TEN.get(v, ''),
                } for k, v in self.thien_ban.items()
            },
            'than_tuong': {
                DIA_CHI[k]: {
                    'ten': v,
                    'han': THAP_NHI_THAN_TUONG.get(v, {}).get('han', ''),
                    'ngu_hanh': THAP_NHI_THAN_TUONG.get(v, {}).get('ngu_hanh', ''),
                    'tinh_chat': THAP_NHI_THAN_TUONG.get(v, {}).get('tinh_chat', ''),
                    'y_nghia': THAP_NHI_THAN_TUONG.get(v, {}).get('y_nghia', ''),
                } for k, v in self.than_tuong_map.items()
            },
            'tu_khoa': [
                {
                    'khoa': k['khoa'],
                    'thuong_ten': k['thuong_ten'],
                    'ha_ten': k['ha_ten'],
                    'quan_he': k['quan_he'],
                    'diem': k['diem'],
                    'ngu_hanh_thuong': k['ngu_hanh_thuong'],
                    'ngu_hanh_ha': k['ngu_hanh_ha'],
                    'vai_tro': k['info']['vai_tro'],
                    'mo_ta': k['info']['mo_ta'],
                    'chien_luoc': k['info']['chien_luoc'],
                } for k in self.tu_khoa
            ],
            'tam_truyen': {
                key: {
                    'ten': val['ten'],
                    'han': val['han'],
                    'ngu_hanh': val['ngu_hanh'],
                    'than_tuong': val['than_tuong'],
                    'vai_tro': val['info']['vai_tro'],
                    'mo_ta': val['info']['mo_ta'],
                    'quantum_analog': val['info']['quantum_analog'],
                } for key, val in self.tam_truyen.items()
            },
            'khoa_the': {
                'ten': self.khoa_the['ten'],
                'han': self.khoa_the['han'],
                'y_nghia': self.khoa_the['y_nghia'],
                'tinh_chat': self.khoa_the['tinh_chat'],
            },
            'ban_thuc': {
                str(c['dia_pos']): {
                    'dia_chi': c['dia_chi'],
                    'dia_han': c['dia_han'],
                    'huong': c['huong'],
                    'thien_chi': c['thien_chi'],
                    'thien_han': c['thien_han'],
                    'than_tuong': c['than_tuong'],
                    'than_tuong_han': c['than_tuong_han'],
                    'hanh_dia': c['hanh_dia'],
                    'hanh_thien': c['hanh_thien'],
                    'quan_he': c['quan_he'],
                    'score': c['score'],
                    'nature': c['nature'],
                    'dong_vat': c['dong_vat'],
                    'nguyet_tuong_ten': c['nguyet_tuong_ten'],
                    'than_tuong_y_nghia': c.get('than_tuong_info', {}).get('y_nghia', ''),
                    'than_tuong_tinh_chat': c.get('than_tuong_info', {}).get('tinh_chat', ''),
                } for c in ban_thuc
            },
            'best_direction': {
                'huong': best['huong'],
                'dia_chi': best['dia_chi'],
                'score': best['score'],
                'than_tuong': best['than_tuong'],
                'reason': f"{best['than_tuong']} ({best.get('than_tuong_info', {}).get('y_nghia', '')})"
                         f" - {best['hanh_thien']} {best['quan_he']} {best['hanh_dia']}",
            },
            'worst_direction': {
                'huong': worst['huong'],
                'dia_chi': worst['dia_chi'],
                'score': worst['score'],
                'than_tuong': worst['than_tuong'],
                'reason': f"{worst['than_tuong']} ({worst.get('than_tuong_info', {}).get('y_nghia', '')})"
                         f" - {worst['hanh_thien']} {worst['quan_he']} {worst['hanh_dia']}",
            },
            'chien_luoc': chien_luoc,
            'luc_nham_info': LUC_NHAM,
            'quantum_vedic': QUANTUM_VEDIC_ISOMORPHISM,
            'quantum_analysis': self._analyze_quantum_detail(),
            'knowledge_graph': self.build_knowledge_graph(),
        }
