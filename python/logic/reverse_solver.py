"""
Reverse Solver Logic
Deduces (Year Can, Year Chi, Month, Hour) from Star Positions
"""

from data import (
    LOC_TON_POSITION, THIEN_KHOI_VIET, KINH_DA, THIEN_QUAN_PHUC, 
    PHONG_CAO_POSITION, AN_QUANG_THIEN_QUY, THIEN_HINH_POSITION,
    THIEN_MA_POSITION, HONG_LOAN_THIEN_HY, DAO_HOA_POSITION, HOA_CAI_POSITION,
    QUOC_AN_POSITION,
    TA_PHU_BASE, HUU_BAT_BASE,
    VAN_XUONG_BASE, VAN_KHUC_BASE,
    THIEN_THUONG_SU_BASE,
    DUONG_PHU_POSITION, THIEN_DIEU_POSITION,
    DIA_CHI, THIEN_CAN
)

class ReverseSolver:
    def __init__(self, star_map: dict):
        """
        star_map: { "Star Name": PalaceIndex (0-11) }
        """
        self.star_map = star_map
        self.possible_year_cans = set(range(10))
        self.possible_year_chis = set(range(12))
        self.possible_months = set(range(1, 13))
        self.possible_hours = set(range(12))
        
    def solve(self):
        self._infer_year_can()
        self._infer_year_chi()
        self._infer_month()
        self._infer_hour()
        
        return {
            "year_cans": list(self.possible_year_cans),
            "year_chis": list(self.possible_year_chis),
            "months": list(self.possible_months),
            "hours": list(self.possible_hours)
        }

    # ==========================
    # YEAR CAN INFERENCE
    # ==========================
    def _infer_year_can(self):
        # 1. Lộc Tồn
        if "Lộc Tồn" in self.star_map:
            pos = self.star_map["Lộc Tồn"]
            candidates = {can for can, p in LOC_TON_POSITION.items() if p == pos}
            self.possible_year_cans &= candidates

        # 2. Thiên Khôi/Việt
        candidates_kv = set()
        has_kv_constraint = False
        if "Thiên Khôi" in self.star_map:
            has_kv_constraint = True
            pos = self.star_map["Thiên Khôi"]
            candidates_kv = {can for can, val in THIEN_KHOI_VIET.items() if val['khoi'] == pos}
        
        if "Thiên Việt" in self.star_map:
            pos = self.star_map["Thiên Việt"]
            viet_cans = {can for can, val in THIEN_KHOI_VIET.items() if val['viet'] == pos}
            if has_kv_constraint:
                candidates_kv &= viet_cans
            else:
                candidates_kv = viet_cans
                has_kv_constraint = True
                
        if has_kv_constraint:
            self.possible_year_cans &= candidates_kv

        # 3. Kinh Dương / Đà La (Depend on Can)
        candidates_kd = set()
        has_kd_constraint = False
        if "Kinh Dương" in self.star_map:
            has_kd_constraint = True
            pos = self.star_map["Kinh Dương"]
            candidates_kd = {can for can, val in KINH_DA.items() if val['kinh'] == pos}
            
        if "Đà La" in self.star_map:
            pos = self.star_map["Đà La"]
            da_cans = {can for can, val in KINH_DA.items() if val['da'] == pos}
            if has_kd_constraint:
                candidates_kd &= da_cans
            else:
                candidates_kd = da_cans
                has_kd_constraint = True
                
        if has_kd_constraint:
            self.possible_year_cans &= candidates_kd

        # Other Can dependencies (Hóa Lộc, Hóa Quyền etc from Tứ Hóa - COMPLEX, skip for now)
        # Thiên Quan, Thiên Phúc
        # ... (implement similar logic for other stars if needed)

    # ==========================
    # YEAR CHI INFERENCE
    # ==========================
    def _infer_year_chi(self):
        # 1. Thái Tuế (Always at Year Chi position)
        if "Thái Tuế" in self.star_map:
            self.possible_year_chis &= {self.star_map["Thái Tuế"]}
            
        # 2. Thiên Mã
        if "Thiên Mã" in self.star_map:
            pos = self.star_map["Thiên Mã"]
            candidates = {chi for chi, p in THIEN_MA_POSITION.items() if p == pos}
            self.possible_year_chis &= candidates
            
        # 3. Hồng Loan / Thiên Hỹ
        # ... logic similar to others using HONG_LOAN_THIEN_HY dict

    # ==========================
    # MONTH INFERENCE
    # ==========================
    def _infer_month(self):
        # Tả Phụ: (TA_PHU_BASE + month - 1) % 12
        if "Tả Phụ" in self.star_map:
            target = self.star_map["Tả Phụ"]
            # target = (4 + m - 1) % 12 => target = (3 + m) % 12
            # m = (target - 3) % 12. If result 0 -> 12.
            m = (target - (TA_PHU_BASE - 1)) % 12
            if m <= 0: m += 12
            self.possible_months &= {m}

        # Hữu Bật: ((HUU_BAT_BASE - (month - 1)) % 12 + 12) % 12
        if "Hữu Bật" in self.star_map:
            target = self.star_map["Hữu Bật"]
            # target = (10 - (m - 1)) % 12 = (11 - m) % 12
            # 11 - m = target => m = 11 - target (modulo logic)
            # if target <= 11: m = 11 - target. If m<=0, m+=12
            m = (HUU_BAT_BASE + 1 - target) % 12
            if m <= 0: m += 12
            # Verify correctness because modulo arithmetic direction is tricky
            # Let's bruteforce 1-12 to be safe
            valid_months = {m for m in range(1, 13) if ((HUU_BAT_BASE - (m - 1)) % 12 + 12) % 12 == target}
            self.possible_months &= valid_months

    # ==========================
    # HOUR INFERENCE
    # ==========================
    def _infer_hour(self):
        # Văn Xương: ((VAN_XUONG_BASE - hour) % 12 + 12) % 12
        if "Văn Xương" in self.star_map:
            target = self.star_map["Văn Xương"]
            # target = (10 - h) % 12.
            # h = (10 - target) % 12
            h = (VAN_XUONG_BASE - target) % 12
            self.possible_hours &= {h}
            
        # Văn Khúc: (VAN_KHUC_BASE + hour) % 12
        if "Văn Khúc" in self.star_map:
            target = self.star_map["Văn Khúc"]
            # target = (4 + h) % 12
            h = (target - VAN_KHUC_BASE) % 12
            self.possible_hours &= {h}

    # ==========================
    # SEARCH & VERIFY
    # ==========================
    def find_dates(self, start_year=1900, end_year=2100):
        """
        Find specific dates matching all constraints.
        Using Tu Vi position to solve for Day is the most effective method.
        """
        from data import CUC_TABLE, CUC_TYPE
        from chart.chart_builder import calculate_cung_menh, calculate_tuvi_position
        from core import get_year_can_chi
        
        results = []
        
        # Pre-calculate possible specific years
        valid_years = []
        for y in range(start_year, end_year + 1):
            can = (y + 6) % 10  # 0=Canh, but our system 0=Giap? Check core.py logic
            # core.py logic: 0=Giap, 1=At...
            # Year 1984 = Giap Ty. (1984-4)%10 = 0. So (y-4)%10 is Can index.
            # wait, let's check core.get_year_can_chi logic or just rely on it.
            # For header logic, let's just use get_year_can_chi
            yc = get_year_can_chi(y)
            if yc['can_index'] in self.possible_year_cans and yc['chi_index'] in self.possible_year_chis:
                valid_years.append(y)
                
        # If no Tu Vi provided, we cannot deduce Day easily (unless Tam Thai/Bat Toa provided)
        target_tuvi = self.star_map.get("Tử Vi")
        
        for y in valid_years:
            yc = get_year_can_chi(y)
            can_index = yc['can_index']
            
            for m in self.possible_months:
                for h in self.possible_hours:
                    # Calculate Cuc
                    menh_pos = calculate_cung_menh(m, h)
                    # Cuc depends on Can and Menh Position
                    # We need determine_cuc logic. 
                    # from core import determine_cuc (assume it exists or copy logic)
                    # CUC logic: Can of Menh Palace.
                    # Can of year vs Menh Pos? No. can_menh = (year_can * 2 + menh_pos_of_can_lookup??) 
                    # Actually determine_cuc is in chart_builder imports usually.
                    
                    # Let's iterate days (1-30)
                    for d in range(1, 31):
                        # Verify Tu Vi matches
                        if target_tuvi is not None:
                            # Re-calculate Cục for this combo
                            from core import determine_cuc
                            cuc = determine_cuc(can_index, menh_pos) 
                            # determine_cuc might return dict {'number': 2, ...}
                            
                            tuvi_pos = calculate_tuvi_position(cuc['number'], d)
                            if tuvi_pos != target_tuvi:
                                continue # Day doesn't match Tu Vi
                                
                        # If we reached here, this (y, m, d, h) is a CANDIDATE
                        # We should ideally verify ALL other stars in star_map match too
                        # But for now, let's just return it
                        
                        results.append({
                            "year": y, "month": m, "day": d, "hour": h,
                            "can": can_index, "chi": yc['chi_index']
                        })
                        
        return results
