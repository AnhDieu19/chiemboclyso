"""
Thái Ất Engine - Core engine tính toán Thái Ất Thần Số

Chức năng:
- Xác định Nguyên (72 năm), Hội, Kỷ
- Tính Tứ Kế (Niên/Nguyệt/Nhật/Thời Cục) theo Tích Niên Thượng Cổ
- An sao chính: Thái Ất, Văn Xương, Kể Thần, Thủy Kích
- An Tam Cơ (Quân/Thần/Dân), Ngũ Phúc, Đại Du
- An Tứ Thần, Thiên Ất, Địa Ất, Trực Phù
- Luận giải cát hung

Tham khảo:
  - Thái Ất Thần Kinh (Nguyễn Bỉnh Khiêm, dịch Nguyễn Ngọc Doãn)
  - Thái Ất Dị Giản Lục (Lê Quý Đôn)
  - Bài viết Thái Ất (Wikipedia tiếng Việt)
"""

from typing import Dict, List, Tuple
from math import floor
from data.thai_at_tables import (
    THAP_LUC_THAN, NGU_NGUYEN, CUU_CUNG_THAI_AT, get_hoi_info,
    THAP_LUC_THAN_NGU_HANH, THAP_CAN_HOA_KHI
)
from core.jie_qi_calculator import get_tiet_khi, jd_from_date
from core.ngu_hanh_engine import NguHanhEngine
from core.palace_converter import LAC_THU_CUNG


class ThaiAtEngine:
    """
    Engine tính toán Thái Ất Thần Số
    
    Công thức chính dựa trên Tích Niên (累積年) từ Thượng Cổ Giáp Tý.
    Mốc Thượng Cổ: Giáp Tý đời Thiên Hoàng, cách CN 10.153.917 năm.
    
    Tứ Kế:
    - Niên Cục: Tích Niên % 3600 dư → % 360 dư → % 72 dư
    - Nguyệt Cục: (EPOCH + năm_trước) * 12 + 2 + tháng, rồi % 360 % 72
    - Nhật Cục: Sau Đông Chí, tìm ngày Giáp Tý gần nhất, tích ngày % 360 % 72
    - Thời Cục: Từ ngày Giáp Tý/Giáp Ngọ gần nhất, tích giờ % 360 % 72
    """
    
    # Mốc Thượng Cổ Giáp Tý (Thiên Hoàng) cách CN 10.153.917 năm
    THAI_AT_EPOCH = 10153917
    
    # Mốc Trung Cổ Giáp Dần cách Thượng Cổ 10.141.310 năm
    TRUNG_CO_OFFSET = 10141310
    
    # Số doanh sai khi dùng mốc Trung Cổ cho sao xuất phát từ Thượng Cổ
    DOANH_SAI = 250
    
    CYCLE_LENGTH = 360   # 1 Kỷ = 360 năm (5 Nguyên)
    NGUYEN_LENGTH = 72   # 1 Nguyên = 72 năm
    HOI_LENGTH = 6       # 1 Hội = 6 năm
    
    def __init__(self, year: int, month: int, day: int, hour: int = 0):
        """
        Khởi tạo Thái Ất Engine
        
        Args:
            year: Năm dương lịch (e.g. 2024)
            month: Tháng dương lịch (1-12)
            day: Ngày dương lịch (1-31)
            hour: Giờ dương lịch (0-23)
        """
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        
        # Tính các thông số cơ bản theo công thức Tích Niên
        self._calculate_base()
    
    def _calculate_base(self):
        """
        Tính Tứ Kế (Niên Cục, Nguyệt Cục, Nhật Cục, Thời Cục) theo Tích Niên Thượng Cổ.
        
        Công thức theo Sách Thái Ất & Wikipedia:
        - Niên Cục: (Tích Niên % 3600) dư % 360 dư % 72
        - Nguyệt Cục: ((EPOCH + năm_trước)*12 + 2 + tháng) % 360 % 72
        - Nhật Cục: Từ Giáp Tý đầu tiên sau Đông Chí, tích ngày % 360 % 72
        - Thời Cục: Giáp Tý/Giáp Ngọ gần nhất, tích giờ % 360 % 72
        
        Xác định cục Âm/Dương:
        - Đông Chí → Hạ Chí: Dương Cục
        - Hạ Chí → Đông Chí: Âm Cục
        """
        # === 1. TÍCH NIÊN (累積年) ===
        # Theo Thái Ất Thần Kinh: Thượng Cổ Giáp Tý đến năm xem
        self.tich_nien = self.year + self.THAI_AT_EPOCH
        
        # === 2. NIÊN CỤC ===
        # Ref: "Tích niên chia 3.600, phần dư chia 360, phần dư chia 72"
        # VD: 2014 → Tích niên = 10155931 → %3600 = 331 → %360 = 331 → %72 = 43
        nien_du = self.tich_nien % 3600
        nien_du = nien_du % 360
        self.nien_cuc = nien_du % 72
        if self.nien_cuc == 0:
            self.nien_cuc = 72
        
        # === 3. VÒNG KỶ DƯ (周紀餘) ===
        # Sách: "Lấy số 118 làm vòng Kỷ Dư" (tức tích niên % 360 tại mốc Tân Dậu 1441)
        # Nhưng Kỷ Dư thay đổi theo năm: Kỷ Dư = Tích Niên % 360
        self.vong_ky_du = self.tich_nien % 360
        if self.vong_ky_du == 0:
            self.vong_ky_du = 360
        
        # === 4. XÁC ĐỊNH DƯƠNG CỤC / ÂM CỤC ===
        # Đông Chí → trước Hạ Chí: Dương Cục
        # Hạ Chí → trước Đông Chí: Âm Cục
        tiet_khi_info = get_tiet_khi(self.day, self.month, self.year)
        self.tiet_khi = tiet_khi_info
        tk_idx = tiet_khi_info['index']
        # Dương Cục: từ Đông Chí (23) qua Tiểu Hàn (0) đến trước Hạ Chí (11)
        self.is_duong_cuc = (tk_idx >= 23) or (tk_idx < 11)
        
        # === 5. NGUYỆT CỤC ===
        # Ref: (EPOCH + năm_trước) * 12 + Thiên Chính(1) + Địa Chính(1) + tháng_xem
        # Thiên Chính + Địa Chính = 2 (vì dùng lịch kiến Dần)
        tich_thang = (self.THAI_AT_EPOCH + (self.year - 1)) * 12 + 2 + self.month
        self.nguyet_cuc = (tich_thang % 360) % 72
        if self.nguyet_cuc == 0:
            self.nguyet_cuc = 72
        
        # === 6. NHẬT CỤC ===
        # Theo Thái Ất Thần Kinh:
        # "Sau tiết Đông chí, tìm ngày Giáp Tý đầu tiên gần nhất sau Đông chí
        #  năm trước, lấy đó làm gốc đếm trở đi, tích cho đến ngày xem"
        # Sử dụng Can Chi ngày: Giáp Tý có sexagenary cycle = 0
        # JD % 60 - offset cho ra sexagenary day index (Giáp Tý = 0)
        jd_current = int(jd_from_date(self.day, self.month, self.year))
        
        # Xác định ngày Đông Chí năm trước (khoảng 22/12)
        jd_dong_chi_prev = int(jd_from_date(22, 12, self.year - 1))
        
        # Tìm ngày Giáp Tý đầu tiên >= ngày Đông Chí năm trước
        # Can Chi ngày: (JD + 49) % 60 → 0 = Giáp Tý
        # Tìm JD sao cho (JD + 49) % 60 = 0
        can_chi_dong_chi = (jd_dong_chi_prev + 49) % 60
        days_to_giap_ty = (60 - can_chi_dong_chi) % 60
        jd_giap_ty_base = jd_dong_chi_prev + days_to_giap_ty
        
        # Tích ngày từ Giáp Tý đến ngày xem (inclusive)
        tich_ngay = jd_current - jd_giap_ty_base + 1
        if tich_ngay <= 0:
            tich_ngay += 360  # Safety: nếu ngày xem trước Giáp Tý
        
        self.nhat_cuc = (tich_ngay % 360) % 72
        if self.nhat_cuc == 0:
            self.nhat_cuc = 72
        
        # === 7. THỜI CỤC ===
        # "Sau Đông chí ngày Giáp Tý hoặc Giáp Ngọ, nửa đêm giờ Giáp Tý,
        #  khởi dùng Dương cục 1... Sau Hạ chí, Âm cục."
        # Tìm ngày Giáp Tý (CC=0) hoặc Giáp Ngọ (CC=6) gần nhất trước ngày xem
        can_chi_today = (jd_current + 49) % 60
        # Giáp Tý = 0, Giáp Ngọ = 6 (trong 60 ngày: 0, 6, 12... offset 30 cho Ngọ)
        # Thực ra Giáp Ngọ = index 6 trong bảng 60 Hoa Giáp
        days_since_giap_ty_or_ngo = can_chi_today % 30  # Giáp Tý=0, Giáp Ngọ=30 (mod 30=0)
        jd_giap_base = jd_current - days_since_giap_ty_or_ngo
        
        # Tính giờ Can Chi (0=Tý, 1=Sửu, ...)
        hour_chi = (self.hour + 1) // 2  # Convert 24h to 12 chi index
        
        # Tích giờ = (ngày từ Giáp Tý/Ngọ) * 12 + giờ_chi + 1
        tich_gio = days_since_giap_ty_or_ngo * 12 + hour_chi + 1
        
        self.thoi_cuc = (tich_gio % 360) % 72
        if self.thoi_cuc == 0:
            self.thoi_cuc = 72

        # === 8. NGUYÊN INDEX & HỘI INDEX ===
        # Nguyên (0-4): mỗi Nguyên 72 năm, trong vòng 360 năm
        cycle_360 = self.tich_nien % 360
        self.nguyen_index = (cycle_360 - 1) // 72 if cycle_360 > 0 else 4
        
        # Hội (0-11): mỗi Hội 6 năm, trong 1 Nguyên 72 năm
        self.hoi_index = (self.nien_cuc - 1) // 6
        self.year_in_hoi = (self.nien_cuc - 1) % 6
        
        # Kỷ (0-2): 3 phần trong 1 năm (mỗi 4 tháng)
        self.ky_index = (self.month - 1) // 4
    
    def get_nguyen(self) -> Dict:
        """Lấy thông tin Nguyên hiện tại"""
        return {
            'index': self.nguyen_index,
            **NGU_NGUYEN[self.nguyen_index]
        }
    
    def get_hoi(self) -> Dict:
        """Lấy thông tin Hội hiện tại"""
        info = get_hoi_info(self.hoi_index)
        return {
            'index': self.hoi_index,
            'year_in_hoi': self.year_in_hoi,
            **info
        }
    
    def get_ky(self) -> Dict:
        """Lấy thông tin Kỷ hiện tại"""
        KY_NAMES = ['Thượng Kỷ', 'Trung Kỷ', 'Hạ Kỷ']
        return {
            'index': self.ky_index,
            'name': KY_NAMES[self.ky_index],
            'months': f"Tháng {self.ky_index * 4 + 1}-{self.ky_index * 4 + 4}"
        }
    
    def calculate_than_positions(self) -> Dict[int, List[Dict]]:
        """
        An sao Thái Ất vào Cửu Cung - Theo Sách Thái Ất & Thái Ất Thần Kinh
        
        Các sao chính:
        1. Thái Ất (Tuế Kể): (Kỷ Dư - 24) / 3. 3 năm 1 cung. Khởi Kiền (1).
        2. Văn Xương (Thiên Mục): Kỷ Dư - 18. Vòng 16 Thần. Kiền Khôn lưu 2 toán.
        3. Kể Thần: Kỷ Dư % 12. Khởi Dần ngược.
        4. Thủy Kích (Địa Mục): Kể Thần → khởi Cấn → Văn Xương = Thủy Kích.
        5. Ngũ Phúc: (Tích + 115) % 225 / 45. Path: 1→8→4→2→5.
        6. Đại Du: (Tích + 34) % 288 / 36. Khởi 7.
        7. Tam Cơ: Quân (30 năm), Thần (3 năm), Dân (1 năm).
        8. Tứ Thần, Thiên Ất, Địa Ất, Trực Phù: 3 năm/cung.
        """
        positions = {i: [] for i in range(1, 10)}  # 9 Cung
        
        tich_nien = self.tich_nien
        vong_ky_du = self.vong_ky_du
        
        # === HELPER: Di chuyển trên vòng 8 cung (bỏ trung cung 5) ===
        # Thứ tự Hậu Thiên: 1→8→3→4→9→2→7→6
        RING_8 = [1, 8, 3, 4, 9, 2, 7, 6]
        
        def move_ring_8(start_palace, steps, is_forward=True):
            """Di chuyển trên vòng 8 cung, bỏ trung cung 5"""
            if start_palace not in RING_8:
                start_palace = 1
            idx = RING_8.index(start_palace)
            if is_forward:
                new_idx = (idx + steps) % 8
            else:
                new_idx = (idx - steps) % 8
            return RING_8[new_idx]
        
        # === 12 Cung (Địa Chi) → 9 Cung mapping ===
        # Ngọ→9, Mùi→2, Thân→2, Dậu→7, Tuất→6, Hợi→6, Tý→1, Sửu→8, Dần→8, Mão→3, Thìn→4, Tỵ→9
        CHI_TO_9 = [1, 8, 8, 3, 4, 9, 9, 2, 2, 7, 6, 6]  # index 0=Tý ... 11=Hợi
        
        # ================================================================
        # 1. THÁI ẤT (TUẾ KỂ) - Sách mục 14
        # "Vòng Kỷ Dư trên, lấy 24 mà trừ; rồi lấy 3 rút"
        # Dương cục: khởi Kiền (1), chuyển xuôi 8 cung. 3 năm 1 cung.
        # Âm cục: khởi Tấn (?), chuyển ngược.
        # ================================================================
        val_thai_at = vong_ky_du
        while val_thai_at > 24:
            val_thai_at -= 24
        steps_thai_at = (val_thai_at - 1) // 3  # 3 năm 1 cung
        
        if self.is_duong_cuc:
            pos_thai_at = move_ring_8(1, steps_thai_at, is_forward=True)
        else:
            pos_thai_at = move_ring_8(9, steps_thai_at, is_forward=False)
        
        # ================================================================
        # 2. VĂN XƯƠNG (THIÊN MỤC) - Sách mục 15
        # "Dùng Vòng Kỷ Dư. Lấy 18 trừ mãi. Số dư khởi Thân Vũ Đức
        #  chuyển xuôi 16 Thần. Gặp Kiền Khôn thì lưu 2 toán."
        # 16 Thần (thuận): Thân→Dậu→Tuất→Kiền→Hợi→Tý→Sửu→Cấn→
        #                   Dần→Mão→Thìn→Tốn→Tỵ→Ngọ→Mùi→Khôn
        # Tại Kiền và Khôn: lưu 2 toán (ở lại 2 nhịp)
        # Chu kỳ: 16 thần + 2 lưu (Kiền+Khôn) = 18 năm → khớp "trừ 18"!
        # ================================================================
        RING_16_NAMES = [
            'Thân', 'Dậu', 'Tuất', 'Kiền', 'Hợi', 'Tý', 'Sửu', 'Cấn',
            'Dần', 'Mão', 'Thìn', 'Tốn', 'Tỵ', 'Ngọ', 'Mùi', 'Khôn'
        ]
        MAP_16_TO_9 = {
            'Thân': 2, 'Dậu': 7, 'Tuất': 6, 'Kiền': 6, 'Hợi': 6, 'Tý': 1,
            'Sửu': 8, 'Cấn': 8, 'Dần': 8, 'Mão': 3, 'Thìn': 4, 'Tốn': 4,
            'Tỵ': 9, 'Ngọ': 9, 'Mùi': 2, 'Khôn': 2
        }
        SPECIAL_NODES = {'Kiền', 'Khôn'}  # Lưu 2 toán
        
        # Dương Cục: khởi Thân, đi thuận. Âm Cục: khởi Dần, đi xuôi (hoặc ngược tùy sách)
        if self.is_duong_cuc:
            start_idx_vc = 0   # Thân
            direction_vc = 1   # Thuận
        else:
            start_idx_vc = 8   # Dần
            direction_vc = 1   # Xuôi (sách Ref: "Âm cục khởi Dần Lữ Thân đi xuôi")
        
        # Số bước: "Lấy 18 trừ mãi" → sim_steps = Kỷ Dư % 18
        sim_steps = vong_ky_du % 18
        if sim_steps == 0:
            sim_steps = 18  # Đủ 1 vòng
        
        # Simulation vòng 16 thần với rule Kiền/Khôn lưu 2 toán
        current_idx_vc = start_idx_vc
        special_time = 0  # Đếm thời gian ở node đặc biệt
        
        for step in range(sim_steps):
            curr_name = RING_16_NAMES[current_idx_vc]
            if curr_name in SPECIAL_NODES:
                if special_time < 1:
                    # Lưu lại (ở 2 toán = 2 năm tại node này)
                    special_time += 1
                else:
                    # Đã ở đủ 2 toán, dời đi
                    special_time = 0
                    current_idx_vc = (current_idx_vc + direction_vc) % 16
            else:
                current_idx_vc = (current_idx_vc + direction_vc) % 16
        
        pos_van_xuong = MAP_16_TO_9[RING_16_NAMES[current_idx_vc]]
        self._van_xuong_chi_name = RING_16_NAMES[current_idx_vc]
        
        # ================================================================
        # 3. KỂ THẦN (計神) - Sách mục 16
        # "Vòng Kỷ Dư lấy 12 trừ. Số dư khởi Dần chuyển ngược 12 thần
        #  (Dần→Sửu→Tý→Hợi→Tuất→Dậu→Thân→Mùi→Ngọ→Tỵ→Thìn→Mão)"
        # Âm cục: khởi Thân chuyển ngược
        # ================================================================
        ke_du = vong_ky_du % 12
        if ke_du == 0:
            ke_du = 12
        
        # 12 Địa Chi: Tý(0), Sửu(1), Dần(2), Mão(3), Thìn(4), Tỵ(5),
        #             Ngọ(6), Mùi(7), Thân(8), Dậu(9), Tuất(10), Hợi(11)
        DIA_CHI_NAMES = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ',
                         'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
        
        if self.is_duong_cuc:
            # Khởi Dần (index 2), đi nghịch (giảm)
            ke_chi_idx = (2 - (ke_du - 1)) % 12
        else:
            # Khởi Thân (index 8), đi nghịch
            ke_chi_idx = (8 - (ke_du - 1)) % 12
        
        self._ke_than_chi = DIA_CHI_NAMES[ke_chi_idx]
        pos_ke_than = CHI_TO_9[ke_chi_idx]
        
        # ================================================================
        # 4. THỦY KÍCH (ĐỊA MỤC) - Sách mục 17
        # "Dùng năm nay, Kể Thần ở cung nào. Từ đó khởi Cấn Hòa Đức.
        #  Thấy Văn Xương tới cung nào đó là Thủy Kích"
        # Logic: Từ vị trí Kể Thần, đếm (khởi Cấn) cho đến gặp cung 
        #        mà Văn Xương đang ở → đó là cung Thủy Kích.
        # Cách implementation: Tìm offset từ Kể Thần đến Văn Xương 
        #                      trên Ring 16, đặt Thủy Kích ở đó.
        # ================================================================
        # Đơn giản hóa: Thủy Kích ở vị trí Văn Xương nhìn từ Kể Thần qua Cấn
        # Nếu Kể Thần và Văn Xương cùng cung → Thủy Kích cũng ở đó
        if pos_ke_than == pos_van_xuong:
            pos_thuy_kich = pos_ke_than
        else:
            # Đi từ Kể Thần theo 16 Thần, tìm Văn Xương
            # Khi tìm thấy, cung đó chính là Thủy Kích
            pos_thuy_kich = pos_van_xuong  # Simplified: Thủy Kích ≈ Văn Xương
            # Logic nâng cao: offset qua Cấn
            ke_in_ring = None
            vc_in_ring = None
            for i, name in enumerate(RING_16_NAMES):
                if DIA_CHI_NAMES[ke_chi_idx] == name or \
                   (name == 'Cấn' and ke_chi_idx in [1, 2]):  # Sửu, Dần ≈ Cấn
                    ke_in_ring = i
                if name == self._van_xuong_chi_name:
                    vc_in_ring = i
            
            if ke_in_ring is not None and vc_in_ring is not None:
                # Đếm bước từ Kể Thần đến Văn Xương
                offset = (vc_in_ring - ke_in_ring) % 16
                # Áp dụng offset từ Cấn (index 7 trong ring_16)
                target_idx = (7 + offset) % 16
                pos_thuy_kich = MAP_16_TO_9[RING_16_NAMES[target_idx]]
        
        # ================================================================
        # 5. NGŨ PHÚC - Sách mục 8
        # "Tuế tích thêm 115, lấy 225 khử, thừa lấy 45 trừ"
        # Path: 1(Kiền) → 8(Cấn) → 4(Tốn) → 2(Khôn) → 5(Trung)
        # 45 năm dời 1 cung
        # ================================================================
        val_ngu_phuc = (tich_nien + 115) % 225
        step_ngu_phuc = val_ngu_phuc // 45
        PATH_NGU_PHUC = [1, 8, 4, 2, 5]  # Kiền → Cấn → Tốn → Khôn → Trung
        pos_ngu_phuc = PATH_NGU_PHUC[step_ngu_phuc % 5]
        
        # ================================================================
        # 6. ĐẠI DU - Sách mục 9
        # "Tuế tích thêm 34, lấy 288 trừ, còn lại chia 36 rút"
        # 8 cung (bỏ trung cung 5): 7→8→9→1→2→3→4→6 thuận
        # 36 năm dời 1 cung
        # ================================================================
        val_dai_du = (tich_nien + 34) % 288
        step_dai_du = val_dai_du // 36
        RING_DAI_DU = [7, 8, 9, 1, 2, 3, 4, 6]
        pos_dai_du = RING_DAI_DU[step_dai_du % 8]
        
        # ================================================================
        # 7. TAM CƠ (Quân Cơ / Thần Cơ / Dân Cơ) - Sách mục 7
        # Tất cả dùng Tích Niên + Doanh Sai (250), chia 360, lấy dư.
        # Quân Cơ: Khởi Ngọ, 30 năm 1 cung, thuận 12 cung.
        # Thần Cơ: Khởi Ngọ, 3 năm 1 cung, chia 36 rồi chia 3.
        # Dân Cơ: Khởi Tuất, 1 năm 1 cung.
        # ================================================================
        # Ring 12 cung khởi Ngọ: Ngọ(9), Mùi(2), Thân(2), Dậu(7),
        #                         Tuất(6), Hợi(6), Tý(1), Sửu(8),
        #                         Dần(8), Mão(3), Thìn(4), Tỵ(9)
        RING_12_NGO = [9, 2, 2, 7, 6, 6, 1, 8, 8, 3, 4, 9]
        
        val_tam_co = (tich_nien + self.DOANH_SAI) % 360
        
        # Quân Cơ: dư chia 30
        step_quan_co = val_tam_co // 30
        pos_quan_co = RING_12_NGO[step_quan_co % 12]
        
        # Thần Cơ: dư chia 36 rồi chia 3 (sách mục 26: "lấy 360 trừ, lại lấy 36 trừ, dư lấy 3 rút")
        val_than_co = val_tam_co % 36
        step_than_co = val_than_co // 3
        pos_than_co = RING_12_NGO[step_than_co % 12]
        
        # Dân Cơ: Khởi Tuất (index 4 trong ring_12 từ Ngọ), 1 năm 1 cung
        # Ring từ Tuất: Tuất(6), Hợi(6), Tý(1), Sửu(8), Dần(8), Mão(3),
        #               Thìn(4), Tỵ(9), Ngọ(9), Mùi(2), Thân(2), Dậu(7)
        RING_12_TUAT = RING_12_NGO[4:] + RING_12_NGO[:4]
        step_dan_co = (tich_nien + self.DOANH_SAI) % 12
        pos_dan_co = RING_12_TUAT[step_dan_co % 12]
        
        # ================================================================
        # 8. TỨ THẦN, THIÊN ẤT, ĐỊA ẤT, TRỰC PHÙ - Sách mục 10
        # "Giáp Tý thượng nguyên, lấy 360 trừ, lại trừ 36, dư chia 3.
        #  Tứ Thần khởi 1, Thiên Ất khởi 6, Trực Phù khởi 5, Địa Ất khởi 9.
        #  3 năm 1 cung, thuận hành."
        # ================================================================
        val_tu_than = (tich_nien % 360) % 36
        step_tu_than = val_tu_than // 3
        
        # Ring 12 cung thuận (Tý→Sửu→Dần→...) mapped to 9
        RING_12_TY = CHI_TO_9  # [1, 8, 8, 3, 4, 9, 9, 2, 2, 7, 6, 6]
        
        # Tứ Thần: khởi Cung 1 (Tý=0)
        pos_tu_than = RING_12_TY[step_tu_than % 12]
        
        # Thiên Ất: khởi Cung 6 (Tuất=10 trong Địa Chi → CHI_TO_9[10]=6)
        pos_thien_at = RING_12_TY[(10 + step_tu_than) % 12]
        
        # Trực Phù: khởi Cung 5 → dùng vòng 9 cung thay vì 12
        # Sách: "Trực Phù khởi cung 5". 
        # Vòng 9 cung: 5→6→7→8→9→1→2→3→4
        RING_9 = [5, 6, 7, 8, 9, 1, 2, 3, 4]
        pos_truc_phu = RING_9[step_tu_than % 9]
        
        # Địa Ất: khởi Cung 9 (Ngọ=6 trong Địa Chi) 
        pos_dia_at = RING_12_TY[(6 + step_tu_than) % 12]
        
        # ================================================================
        # MAP VỊ TRÍ CHO TẤT CẢ 16 THẦN
        # ================================================================
        STAR_POSITIONS = {
            'Thái Ất': pos_thai_at,
            'Văn Xương': pos_van_xuong,
            'Kể Thần': pos_ke_than,
            'Thủy Kích': pos_thuy_kich,
            'Ngũ Phúc': pos_ngu_phuc,
            'Đại Du': pos_dai_du,
            'Quân Cơ': pos_quan_co,
            'Thần Cơ': pos_than_co,
            'Dân Cơ': pos_dan_co,
            'Tứ Thần': pos_tu_than,
            'Thiên Ất': pos_thien_at,
            'Địa Ất': pos_dia_at,
            'Trực Phù': pos_truc_phu,
        }
        
        # Sao phụ: Chủ/Khách Đại Tướng/Tham Tướng, Tiểu Du
        # Chủ Đại Tướng: Từ Văn Xương tính toán (Sách mục 18)
        # "Lấy số cung Văn Xương, đếm xuôi đến sau Ất, đủ 10 bỏ 10, dùng linh"
        chu_dai_cung_val = pos_van_xuong
        # Đơn giản: Chủ Đại = (Văn Xương cung + offset) mod 9
        pos_chu_dai = ((chu_dai_cung_val * 3) % 10) or 10
        pos_chu_dai = pos_chu_dai if pos_chu_dai <= 9 else pos_chu_dai % 9
        if pos_chu_dai == 0:
            pos_chu_dai = 9
        STAR_POSITIONS['Chủ Đại Tướng'] = pos_chu_dai
        
        # Chủ Tham Tướng: số Đại Tướng * 3 mod 10 (Sách mục 19)
        pos_chu_tham = ((pos_chu_dai * 3) % 10)
        if pos_chu_tham == 0:
            pos_chu_tham = 10
        pos_chu_tham = pos_chu_tham if pos_chu_tham <= 9 else pos_chu_tham % 9
        if pos_chu_tham == 0:
            pos_chu_tham = 9
        STAR_POSITIONS['Chủ Tham Tướng'] = pos_chu_tham
        
        # Khách Đại Tướng: Từ Thủy Kích
        kdt_val = pos_thuy_kich
        pos_khach_dai = ((kdt_val * 3) % 10) or 10
        pos_khach_dai = pos_khach_dai if pos_khach_dai <= 9 else pos_khach_dai % 9
        if pos_khach_dai == 0:
            pos_khach_dai = 9
        STAR_POSITIONS['Khách Đại Tướng'] = pos_khach_dai
        
        pos_khach_tham = ((pos_khach_dai * 3) % 10) or 10
        pos_khach_tham = pos_khach_tham if pos_khach_tham <= 9 else pos_khach_tham % 9
        if pos_khach_tham == 0:
            pos_khach_tham = 9
        STAR_POSITIONS['Khách Tham Tướng'] = pos_khach_tham
        
        # Tiểu Du: placeholder
        pos_tieu_du = move_ring_8(pos_thai_at, self.nien_cuc % 8)
        STAR_POSITIONS['Tiểu Du'] = pos_tieu_du
        
        # Map star names → positions dict
        for than_id, than_info in THAP_LUC_THAN.items():
            name = than_info['name']
            pos = STAR_POSITIONS.get(name, None)
            
            if pos is None:
                # Fallback cho sao chưa xác định
                offset = (than_id + self.nien_cuc) % 9
                if offset == 0:
                    offset = 9
                pos = offset
            
            positions[pos].append({'id': than_id, **than_info})
        
        return positions
    
    def analyze_palace(self, palace_idx: int) -> Dict:
        """
        Phân tích 1 cung
        
        Args:
            palace_idx: 1-9
            
        Returns:
            Dict với điểm số, ý nghĩa
        """
        than_positions = self.calculate_than_positions()
        thans = than_positions.get(palace_idx, [])
        
        if not thans:
            return {
                'palace': palace_idx,
                'palace_info': CUU_CUNG_THAI_AT[palace_idx],
                'thans': [],
                'score': 0,
                'nature': 'neutral',
                'meaning': 'Cung trống, không có Thần'
            }
        
        # Tính tổng điểm
        total_score = sum(t.get('score', 0) for t in thans)
        
        # Xác định tính chất
        if total_score >= 10:
            nature = 'dai_cat'
            meaning = 'Đại cát, rất tốt lành'
        elif total_score >= 5:
            nature = 'cat'
            meaning = 'Cát lành, thuận lợi'
        elif total_score >= 0:
            nature = 'trung'
            meaning = 'Trung bình, bình thường'
        elif total_score >= -5:
            nature = 'hung'
            meaning = 'Hung, không thuận'
        else:
            nature = 'dai_hung'
            meaning = 'Đại hung, rất xấu'
        
        # Thu thập các lĩnh vực
        fields = []
        for t in thans:
            fields.extend(t.get('fields', []))
        
        return {
            'palace': palace_idx,
            'palace_info': CUU_CUNG_THAI_AT[palace_idx],
            'thans': thans,
            'score': total_score,
            'nature': nature,
            'meaning': meaning,
            'fields': list(set(fields))
        }
    
    def get_full_chart(self) -> Dict:
        """
        Lấy toàn bộ lá số Thái Ất
        
        Returns:
            Dict với tất cả thông tin
        """
        than_positions = self.calculate_than_positions()
        
        palaces = {}
        for i in range(1, 10):
            palaces[i] = self.analyze_palace(i)
        
        return {
            'input': {
                'year': self.year,
                'month': self.month,
                'day': self.day,
                'hour': self.hour
            },
            'cuc_info': {
                'nien_cuc': self.nien_cuc,
                'nguyet_cuc': self.nguyet_cuc,
                'nhat_cuc': self.nhat_cuc,
                'thoi_cuc': self.thoi_cuc
            },
            'nguyen': self.get_nguyen(),
            'hoi': self.get_hoi(),
            'ky': self.get_ky(),
            'palaces': palaces,
            'summary': self._generate_summary(palaces)
        }
    
    def _generate_summary(self, palaces: Dict) -> Dict:
        """Tạo tổng kết"""
        cat_palaces = []
        hung_palaces = []
        
        for idx, p in palaces.items():
            if p['nature'] in ['cat', 'dai_cat']:
                cat_palaces.append(idx)
            elif p['nature'] in ['hung', 'dai_hung']:
                hung_palaces.append(idx)
        
        total_score = sum(p['score'] for p in palaces.values())
        
        return {
            'cat_palaces': cat_palaces,
            'hung_palaces': hung_palaces,
            'total_score': total_score,
            'overall': 'cat' if total_score > 0 else ('hung' if total_score < 0 else 'neutral')
        }


# Test
if __name__ == '__main__':
    # Test với ngày 24/12/2024
    engine = ThaiAtEngine(2024, 12, 24, 10)
    
    print("=== THÁI ẤT THẦN SỐ ===")
    print(f"Ngày: {engine.day}/{engine.month}/{engine.year}")
    print()
    
    print("--- Nguyên ---")
    nguyen = engine.get_nguyen()
    print(f"  {nguyen['name']} ({nguyen['han']})")
    
    print("\n--- Hội ---")
    hoi = engine.get_hoi()
    print(f"  {hoi['name']} - Năm thứ {hoi['year_in_hoi'] + 1}/6")
    
    print("\n--- Kỷ ---")
    ky = engine.get_ky()
    print(f"  {ky['name']} ({ky['months']})")
    
    print("\n--- Phân tích Cung ---")
    for i in range(1, 10):
        analysis = engine.analyze_palace(i)
        thans = [t['name'] for t in analysis['thans']]
        print(f"  Cung {i}: {', '.join(thans) if thans else 'Trống'} → {analysis['nature']}")
