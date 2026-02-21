"""
═══════════════════════════════════════════════════════════════════════════
PHÂN TÍCH QUY LUẬT DI CHUYỂN SAO CHÍNH TINH, LỤC CÁT, LỤC SÁT
Kèm theo 12 Thiên Can & 12 Cung Mệnh
═══════════════════════════════════════════════════════════════════════════
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from stars.chinh_tinh_placer import calculate_tuvi_position, calculate_thien_phu_position, place_chinh_tinh
from stars.luc_cat_placer import place_luc_cat, place_ta_huu, place_xuong_khuc, place_khoi_viet
from stars.luc_sat_placer import place_luc_sat, place_kinh_da, place_hoa_linh, place_khong_kiep
from core.cuc_calc import determine_cuc

CHI = ['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']
CAN = ['Giáp','Ất','Bính','Đinh','Mậu','Kỷ','Canh','Tân','Nhâm','Quý']
CUC_NAMES = {2:'Thủy Nhị', 3:'Mộc Tam', 4:'Kim Tứ', 5:'Thổ Ngũ', 6:'Hỏa Lục'}

TV_GROUP = ['Tử Vi','Thiên Cơ','Thái Dương','Vũ Khúc','Thiên Đồng','Liêm Trinh']
TPH_GROUP = ['Thiên Phủ','Thái Âm','Tham Lang','Cự Môn','Thiên Tướng','Thiên Lương','Thất Sát','Phá Quân']

SEPARATOR = '═' * 90

def fmt(pos):
    """Position => Chi name"""
    return CHI[pos % 12]

# ═══════════════════════════════════════════════════════════════════════
# PART 1: CHÍNH TINH - Quy luật theo Cục & Ngày
# ═══════════════════════════════════════════════════════════════════════
def analyze_chinh_tinh():
    print(f"\n{SEPARATOR}")
    print("PHẦN 1: QUY LUẬT DI CHUYỂN 14 CHÍNH TINH")
    print(f"{SEPARATOR}")
    print("\nChính Tinh phụ thuộc: CỤC (2-6) + NGÀY ÂM LỊCH (1-30)")
    print("Cục phụ thuộc: CAN NĂM + CUNG MỆNH")

    # 1A: Bảng Cục theo Can & Cung Mệnh
    print(f"\n{'─'*90}")
    print("1A. BẢNG CỤC THEO CAN NĂM × CUNG MỆNH")
    print(f"{'─'*90}")
    print(f"{'Can':<10}", end='')
    for c in CHI:
        print(f"{c:>6}", end='')
    print()
    print('─' * 82)
    
    for can_idx in range(10):
        print(f"{CAN[can_idx]:<10}", end='')
        for chi_idx in range(12):
            cuc = determine_cuc(can_idx, chi_idx)
            print(f"{cuc['number']:>6}", end='')
        print()
    
    print("\n(Giáp/Kỷ, Ất/Canh, Bính/Tân, Đinh/Nhâm, Mậu/Quý cùng kết quả → chu kỳ 5 Can)")

    # 1B: Vị trí Tử Vi theo Cục × Ngày
    print(f"\n{'─'*90}")
    print("1B. VỊ TRÍ TỬ VI THEO CỤC × NGÀY ÂM LỊCH")
    print(f"{'─'*90}")
    
    for cuc in [2, 3, 4, 5, 6]:
        print(f"\n  ▸ {CUC_NAMES[cuc]} Cục (Cục = {cuc}):")
        print(f"    {'Ngày':>5}", end='')
        for d in range(1, 31):
            print(f"{d:>5}", end='')
        print()
        print(f"    {'Vị trí':>5}", end='')
        
        positions = []
        for d in range(1, 31):
            pos = calculate_tuvi_position(cuc, d)
            positions.append(pos)
            print(f"{fmt(pos):>5}", end='')
        print()
        
        # Tìm chu kỳ
        cycle = None
        for period in range(1, 31):
            if all(positions[i] == positions[(i + period) % len(positions)] 
                   for i in range(min(period, len(positions) - period))):
                if period < len(positions):
                    cycle = period
                    break
        if cycle:
            print(f"    → Chu kỳ lặp: {cycle} ngày")
        
        # Tìm bước nhảy
        steps = [(positions[i+1] - positions[i]) % 12 for i in range(len(positions)-1)]
        unique_steps = set(steps)
        if len(unique_steps) <= 3:
            step_names = [f"+{s}" if s <= 6 else f"-{12-s}" for s in unique_steps]
            print(f"    → Bước nhảy: {', '.join(step_names)}")

    # 1C: Quan hệ Tử Vi - Thiên Phủ (Đối xứng)
    print(f"\n{'─'*90}")
    print("1C. ĐỐI XỨNG TỬ VI ↔ THIÊN PHỦ")
    print(f"{'─'*90}")
    print(f"  Công thức: Thiên Phủ = (16 - Tử Vi) % 12  [Đối xứng qua trục Dần-Thân]")
    print(f"\n  {'Tử Vi':>8} │ {'Thiên Phủ':>10} │ Tổng")
    print(f"  {'─'*8}─┼─{'─'*10}─┼─────")
    for i in range(12):
        tp = calculate_thien_phu_position(i)
        print(f"  {fmt(i):>8} │ {fmt(tp):>10} │ {i+tp}")
    print(f"\n  → Tử Vi + Thiên Phủ luôn ≡ 4 (mod 12) khi vị trí ≤ 4, hoặc = 16")

    # 1D: Offset các sao trong nhóm
    print(f"\n{'─'*90}")
    print("1D. VỊ TRÍ TƯƠNG ĐỐI TRONG MỖI NHÓM")
    print(f"{'─'*90}")
    print(f"\n  Nhóm Tử Vi (nghịch, có bước nhảy):")
    offsets = [0, -2, -3, -4, -5, -8]
    for i, star in enumerate(TV_GROUP):
        print(f"    {star:<12} = Tử Vi {offsets[i]:+d} cung")
    
    print(f"\n  Nhóm Thiên Phủ (thuận, liên tục):")
    offsets_p = [0, 1, 2, 3, 4, 5, 6, 10]
    for i, star in enumerate(TPH_GROUP):
        print(f"    {star:<12} = Thiên Phủ {offsets_p[i]:+d} cung")

    # 1E: Ví dụ cụ thể - Năm Giáp Tuất, Cung Mệnh Tý
    print(f"\n{'─'*90}")
    print("1E. VÍ DỤ: 14 CHÍNH TINH VỚI MỖI CỤC (Ngày 15)")
    print(f"{'─'*90}")
    day = 15
    print(f"  {'Sao':<14}", end='')
    for cuc in [2,3,4,5,6]:
        print(f"{'Cục '+str(cuc):>10}", end='')
    print()
    print('  ' + '─' * 64)
    
    all_results = {}
    for cuc in [2,3,4,5,6]:
        tv_pos = calculate_tuvi_position(cuc, day)
        stars = place_chinh_tinh(tv_pos)
        all_results[cuc] = stars
    
    for star in TV_GROUP + TPH_GROUP:
        print(f"  {star:<14}", end='')
        for cuc in [2,3,4,5,6]:
            pos = all_results[cuc][star]
            print(f"{fmt(pos):>10}", end='')
        print()


# ═══════════════════════════════════════════════════════════════════════
# PART 2: LỤC CÁT - 6 sao Cát Tinh
# ═══════════════════════════════════════════════════════════════════════
def analyze_luc_cat():
    print(f"\n\n{SEPARATOR}")
    print("PHẦN 2: QUY LUẬT DI CHUYỂN LỤC CÁT TINH")
    print(f"{SEPARATOR}")

    # 2A: Tả Phụ - Hữu Bật (theo Tháng)
    print(f"\n{'─'*90}")
    print("2A. TẢ PHÙ & HỮU BẬT (theo THÁNG ÂM LỊCH)")
    print(f"{'─'*90}")
    print(f"  Tả Phụ:  Khởi Thìn(4), thuận +1/tháng  → (4 + tháng - 1) % 12")
    print(f"  Hữu Bật: Khởi Tuất(10), nghịch -1/tháng → (10 - tháng + 1) % 12")
    print(f"\n  {'Tháng':>6} │ {'Tả Phụ':>8} │ {'Hữu Bật':>8} │ Khoảng cách │ Ghi chú")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*12}┼─{'─'*20}")
    
    for m in range(1, 13):
        stars = place_ta_huu(m)
        tp = stars['Tả Phụ']
        hb = stars['Hữu Bật']
        dist = (tp - hb + 12) % 12
        note = "ĐỒNG CUNG!" if tp == hb else ("Đối xứng" if dist == 6 else "")
        print(f"  {m:>6} │ {fmt(tp):>8} │ {fmt(hb):>8} │ {dist:>12} │ {note}")
    
    print(f"\n  → Đối xứng qua trục Thìn-Tuất. Trùng cung tháng 4 (Mùi) & tháng 10 (Sửu)")

    # 2B: Văn Xương - Văn Khúc (theo Giờ)
    print(f"\n{'─'*90}")
    print("2B. VĂN XƯƠNG & VĂN KHÚC (theo GIỜ SINH)")
    print(f"{'─'*90}")
    print(f"  Văn Xương: Khởi Tuất(10), nghịch -1/giờ → (10 - giờ) % 12")
    print(f"  Văn Khúc:  Khởi Thìn(4), thuận +1/giờ  → (4 + giờ) % 12")
    print(f"\n  {'Giờ':>6} │ {'Xương':>8} │ {'Khúc':>8} │ KC │ Ghi chú")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*3}┼─{'─'*20}")
    
    for h in range(12):
        stars = place_xuong_khuc(h)
        vx = stars['Văn Xương']
        vk = stars['Văn Khúc']
        dist = (vx - vk + 12) % 12
        note = "ĐỒNG CUNG!" if vx == vk else ""
        print(f"  {CHI[h]:>6} │ {fmt(vx):>8} │ {fmt(vk):>8} │ {dist:>3} │ {note}")
    
    print(f"\n  → Đối xứng qua trục Thìn-Tuất. Trùng cung giờ Mão & giờ Dậu")

    # 2C: Thiên Khôi - Thiên Việt (theo Can năm)
    print(f"\n{'─'*90}")
    print("2C. THIÊN KHÔI & THIÊN VIỆT (theo CAN NĂM)")
    print(f"{'─'*90}")
    print(f"  Cố định theo Thiên Can → Chu kỳ 10 năm (5 pattern vì 2 Can cùng nhóm)")
    print(f"\n  {'Can':>6} │ {'Khôi':>8} │ {'Việt':>8}")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*8}")
    
    for c in range(10):
        stars = place_khoi_viet(c)
        print(f"  {CAN[c]:>6} │ {fmt(stars['Thiên Khôi']):>8} │ {fmt(stars['Thiên Việt']):>8}")

    print(f"\n  → Nhận xét: Khôi Việt luôn ở các cung 'quý nhân' - không tuân theo công thức tuyến tính")
    print(f"  → Giáp & Canh đối xứng (Sửu↔Mùi, Mùi↔Sửu)")
    print(f"  → Bính≡Mậu, Đinh≡Kỷ (cùng vị trí)")


# ═══════════════════════════════════════════════════════════════════════
# PART 3: LỤC SÁT - 6 sao Sát Tinh
# ═══════════════════════════════════════════════════════════════════════
def analyze_luc_sat():
    print(f"\n\n{SEPARATOR}")
    print("PHẦN 3: QUY LUẬT DI CHUYỂN LỤC SÁT TINH")
    print(f"{SEPARATOR}")

    # 3A: Kinh Dương - Đà La (theo Can năm)
    print(f"\n{'─'*90}")
    print("3A. KÌNH DƯƠNG & ĐÀ LA (theo CAN NĂM, qua LỘC TỒN)")
    print(f"{'─'*90}")
    print(f"  Kinh Dương = Lộc Tồn + 1 cung (thuận)")
    print(f"  Đà La      = Lộc Tồn - 1 cung (nghịch)")
    print(f"\n  {'Can':>6} │ {'Đà La':>8} │ {'[Lộc Tồn]':>10} │ {'Kinh Dương':>10} │ Ghi chú")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*10}─┼─{'─'*10}─┼─{'─'*15}")
    
    # Lộc Tồn positions
    LOC_TON = [2, 3, 5, 6, 5, 6, 8, 9, 11, 0]  # Giáp→Quý
    
    for c in range(10):
        stars = place_kinh_da(c)
        lt = LOC_TON[c]
        print(f"  {CAN[c]:>6} │ {fmt(stars['Đà La']):>8} │ {fmt(lt):>10} │ {fmt(stars['Kinh Dương']):>10} │ Luôn liền kề")

    print(f"\n  → Kình-Lộc-Đà luôn nằm 3 cung liên tiếp (Đà < Lộc < Kình)")
    print(f"  → Lộc Tồn đi theo quy luật Ngũ Hành: Dần→Mão→Tỵ→Ngọ→Tỵ→Ngọ→Thân→Dậu→Hợi→Tý")

    # 3B: Địa Không - Địa Kiếp (theo Giờ)
    print(f"\n{'─'*90}")
    print("3B. ĐỊA KHÔNG & ĐỊA KIẾP (theo GIỜ SINH)")
    print(f"{'─'*90}")
    print(f"  Địa Không: (11 - giờ) % 12  (Nghịch từ Hợi)")
    print(f"  Địa Kiếp:  (11 + giờ) % 12  (Thuận từ Hợi)")
    print(f"\n  {'Giờ':>6} │ {'Đ.Không':>8} │ {'Đ.Kiếp':>8} │ Ghi chú")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*20}")
    
    for h in range(12):
        stars = place_khong_kiep(h)
        dk = stars['Địa Không']
        dj = stars['Địa Kiếp']
        note = "ĐỒNG CUNG!" if dk == dj else ""
        print(f"  {CHI[h]:>6} │ {fmt(dk):>8} │ {fmt(dj):>8} │ {note}")
    
    print(f"\n  → Đối xứng qua Hợi(11). Trùng cung giờ Tý (Hợi) & giờ Ngọ (Tỵ)")

    # 3C: Hỏa Tinh - Linh Tinh
    print(f"\n{'─'*90}")
    print("3C. HỎA TINH & LINH TINH (Chi năm × Giờ × Giới tính)")
    print(f"{'─'*90}")
    print(f"  Phức tạp nhất - phụ thuộc 3 yếu tố:")
    print(f"  1. Nhóm Địa Chi năm → Vị trí gốc")
    print(f"  2. Giờ sinh → Số bước")
    print(f"  3. Âm/Dương × Giới tính → Hướng đi")
    
    chi_groups = [
        ("Dần Ngọ Tuất", [2, 6, 10], "Hỏa gốc=Sửu(1), Linh gốc=Mão(3)"),
        ("Thân Tý Thìn", [8, 0, 4], "Hỏa gốc=Dần(2), Linh gốc=Tuất(10)"),
        ("Tỵ Dậu Sửu",  [5, 9, 1], "Hỏa gốc=Mão(3), Linh gốc=Tuất(10)"),
        ("Hợi Mão Mùi",  [11, 3, 7], "Hỏa gốc=Dậu(9), Linh gốc=Tuất(10)")
    ]
    
    for group_name, chi_indices, desc in chi_groups:
        print(f"\n  ▸ Nhóm {group_name}: {desc}")
        chi_idx = chi_indices[0]  # representative
        
        # Dương Nam (thuận)
        can_duong = 0  # Giáp (dương)
        print(f"    Dương Nam (Hỏa thuận, Linh nghịch):")
        print(f"    {'Giờ':>6}", end='')
        for h in range(12):
            print(f"{CHI[h]:>5}", end='')
        print()
        
        print(f"    {'Hỏa':>6}", end='')
        for h in range(12):
            stars = place_hoa_linh(can_duong, chi_idx, h, 'nam')
            print(f"{fmt(stars['Hỏa Tinh']):>5}", end='')
        print()
        
        print(f"    {'Linh':>6}", end='')
        for h in range(12):
            stars = place_hoa_linh(can_duong, chi_idx, h, 'nam')
            print(f"{fmt(stars['Linh Tinh']):>5}", end='')
        print()

        # Âm Nam (nghịch)
        can_am = 1  # Ất (âm)
        print(f"    Âm Nam (Hỏa nghịch, Linh thuận):")
        print(f"    {'Hỏa':>6}", end='')
        for h in range(12):
            stars = place_hoa_linh(can_am, chi_idx, h, 'nam')
            print(f"{fmt(stars['Hỏa Tinh']):>5}", end='')
        print()
        
        print(f"    {'Linh':>6}", end='')
        for h in range(12):
            stars = place_hoa_linh(can_am, chi_idx, h, 'nam')
            print(f"{fmt(stars['Linh Tinh']):>5}", end='')
        print()


# ═══════════════════════════════════════════════════════════════════════
# PART 4: TỔNG HỢP - Ma trận Can × Cung Mệnh
# ═══════════════════════════════════════════════════════════════════════
def analyze_comprehensive():
    print(f"\n\n{SEPARATOR}")
    print("PHẦN 4: MA TRẬN TỔNG HỢP - 10 CAN × 12 CUNG MỆNH")
    print(f"{SEPARATOR}")
    print("\nVới mỗi tổ hợp (Can, Cung Mệnh) → xác định Cục → ảnh hưởng Chính Tinh")
    print("Đồng thời Can cố định → Kình Đà, Khôi Việt, Tứ Hóa")
    
    # Bảng: Can → sao cố định
    print(f"\n{'─'*90}")
    print("4A. CÁC SAO CỐ ĐỊNH THEO CAN NĂM (chu kỳ 10 năm)")
    print(f"{'─'*90}")
    print(f"  {'Can':>6} │ {'Lộc Tồn':>8} │ {'Kinh Dương':>10} │ {'Đà La':>8} │ {'Khôi':>6} │ {'Việt':>6}")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*10}─┼─{'─'*8}─┼─{'─'*6}─┼─{'─'*6}")
    
    LOC_TON = [2, 3, 5, 6, 5, 6, 8, 9, 11, 0]
    for c in range(10):
        kd = place_kinh_da(c)
        kv = place_khoi_viet(c)
        print(f"  {CAN[c]:>6} │ {fmt(LOC_TON[c]):>8} │ {fmt(kd['Kinh Dương']):>10} │ {fmt(kd['Đà La']):>8} │ {fmt(kv['Thiên Khôi']):>6} │ {fmt(kv['Thiên Việt']):>6}")

    # Bảng: Giờ → sao biến động
    print(f"\n{'─'*90}")
    print("4B. CÁC SAO BIẾN ĐỘNG THEO GIỜ (chu kỳ 12 giờ)")
    print(f"{'─'*90}")
    print(f"  {'Giờ':>6} │ {'V.Xương':>8} │ {'V.Khúc':>8} │ {'Đ.Không':>8} │ {'Đ.Kiếp':>8}")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*8}")
    
    for h in range(12):
        xk = place_xuong_khuc(h)
        dk = place_khong_kiep(h)
        print(f"  {CHI[h]:>6} │ {fmt(xk['Văn Xương']):>8} │ {fmt(xk['Văn Khúc']):>8} │ {fmt(dk['Địa Không']):>8} │ {fmt(dk['Địa Kiếp']):>8}")

    # Bảng: Tháng → sao biến động
    print(f"\n{'─'*90}")
    print("4C. CÁC SAO BIẾN ĐỘNG THEO THÁNG (chu kỳ 12 tháng)")
    print(f"{'─'*90}")
    print(f"  {'Tháng':>6} │ {'Tả Phụ':>8} │ {'Hữu Bật':>8}")
    print(f"  {'─'*6}─┼─{'─'*8}─┼─{'─'*8}")
    
    for m in range(1, 13):
        th = place_ta_huu(m)
        print(f"  {m:>6} │ {fmt(th['Tả Phụ']):>8} │ {fmt(th['Hữu Bật']):>8}")

    # 4D: Full analysis cho case study
    print(f"\n{'─'*90}")
    print("4D. CASE STUDY: NĂM GIÁP TUẤT (1994), NAM, NGÀY 17 ÂM, THÁNG 2")
    print(f"{'─'*90}")
    
    year_can = 0  # Giáp
    year_chi = 10  # Tuất
    month = 2
    day = 17
    gender = 'nam'
    
    # Tính Cung Mệnh cho mỗi giờ
    print(f"\n  Bảng vị trí sao theo 12 giờ sinh:")
    print(f"  {'Giờ':>6} │ {'C.Mệnh':>7} │ {'Cục':>8} │ {'Tử Vi':>7} │ {'T.Phủ':>7} │ {'V.Xương':>8} │ {'V.Khúc':>8} │ {'Đ.Không':>8} │ {'Đ.Kiếp':>8} │ {'K.Dương':>8} │ {'Đà La':>7}")
    print(f"  {'─'*6}─┼─{'─'*7}─┼─{'─'*8}─┼─{'─'*7}─┼─{'─'*7}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*8}─┼─{'─'*7}")
    
    for h in range(12):
        menh = (2 + month - 1 - h + 24) % 12
        cuc_info = determine_cuc(year_can, menh)
        cuc_num = cuc_info['number']
        
        tv_pos = calculate_tuvi_position(cuc_num, day)
        tp_pos = calculate_thien_phu_position(tv_pos)
        
        xk = place_xuong_khuc(h)
        dk = place_khong_kiep(h)
        kd = place_kinh_da(year_can)
        
        print(f"  {CHI[h]:>6} │ {fmt(menh):>7} │ {CUC_NAMES[cuc_num]:>8} │ {fmt(tv_pos):>7} │ {fmt(tp_pos):>7} │ {fmt(xk['Văn Xương']):>8} │ {fmt(xk['Văn Khúc']):>8} │ {fmt(dk['Địa Không']):>8} │ {fmt(dk['Địa Kiếp']):>8} │ {fmt(kd['Kinh Dương']):>8} │ {fmt(kd['Đà La']):>7}")


# ═══════════════════════════════════════════════════════════════════════
# PART 5: QUY LUẬT TỔNG KẾT
# ═══════════════════════════════════════════════════════════════════════
def print_summary():
    print(f"\n\n{SEPARATOR}")
    print("PHẦN 5: TỔNG KẾT QUY LUẬT DI CHUYỂN")
    print(f"{SEPARATOR}")
    
    print("""
┌────────────────────────────────────────────────────────────────────────────────┐
│                    BẢNG TỔNG KẾT QUY LUẬT DI CHUYỂN SAO                       │
├─────────────┬──────────────────┬────────────┬──────────────────────────────────┤
│ Nhóm        │ Sao              │ Phụ thuộc  │ Quy luật                        │
├─────────────┼──────────────────┼────────────┼──────────────────────────────────┤
│ CHÍNH TINH  │ Tử Vi            │ Cục + Ngày │ Thuật toán phức tạp (chia Cục)  │
│ (14 sao)    │ Thiên Cơ         │ ← Tử Vi   │ Tử Vi - 2                       │
│             │ Thái Dương       │ ← Tử Vi   │ Tử Vi - 3                       │
│             │ Vũ Khúc          │ ← Tử Vi   │ Tử Vi - 4                       │
│             │ Thiên Đồng       │ ← Tử Vi   │ Tử Vi - 5                       │
│             │ Liêm Trinh       │ ← Tử Vi   │ Tử Vi - 8                       │
│             │ ──────────────── │ ────────── │ ────────────────────────         │
│             │ Thiên Phủ        │ ← Tử Vi   │ (16 - Tử Vi) % 12 [đối xứng]   │
│             │ Thái Âm          │ ← T.Phủ   │ Thiên Phủ + 1                   │
│             │ Tham Lang        │ ← T.Phủ   │ Thiên Phủ + 2                   │
│             │ Cự Môn           │ ← T.Phủ   │ Thiên Phủ + 3                   │
│             │ Thiên Tướng      │ ← T.Phủ   │ Thiên Phủ + 4                   │
│             │ Thiên Lương      │ ← T.Phủ   │ Thiên Phủ + 5                   │
│             │ Thất Sát         │ ← T.Phủ   │ Thiên Phủ + 6                   │
│             │ Phá Quân         │ ← T.Phủ   │ Thiên Phủ + 10                  │
├─────────────┼──────────────────┼────────────┼──────────────────────────────────┤
│ LỤC CÁT    │ Tả Phụ           │ Tháng      │ Thuận từ Thìn (+1/tháng)        │
│ (6 sao)     │ Hữu Bật          │ Tháng      │ Nghịch từ Tuất (-1/tháng)       │
│             │ Văn Xương         │ Giờ        │ Nghịch từ Tuất (-1/giờ)         │
│             │ Văn Khúc          │ Giờ        │ Thuận từ Thìn (+1/giờ)          │
│             │ Thiên Khôi        │ Can năm    │ Tra bảng (chu kỳ 10 năm)       │
│             │ Thiên Việt        │ Can năm    │ Tra bảng (chu kỳ 10 năm)       │
├─────────────┼──────────────────┼────────────┼──────────────────────────────────┤
│ LỤC SÁT    │ Kinh Dương        │ Can năm    │ Lộc Tồn + 1 (chu kỳ 10 năm)   │
│ (6 sao)     │ Đà La             │ Can năm    │ Lộc Tồn - 1 (chu kỳ 10 năm)   │
│             │ Hỏa Tinh          │ Chi+Giờ+GT │ Gốc theo Chi, bước theo Giờ    │
│             │ Linh Tinh         │ Chi+Giờ+GT │ Ngược chiều Hỏa Tinh           │
│             │ Địa Không         │ Giờ        │ Nghịch từ Hợi (-1/giờ)         │
│             │ Địa Kiếp          │ Giờ        │ Thuận từ Hợi (+1/giờ)          │
└─────────────┴──────────────────┴────────────┴──────────────────────────────────┘

╔════════════════════════════════════════════════════════════════════════════════╗
║                         QUY LUẬT ĐỐI XỨNG                                  ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  1. Tả Phụ ↔ Hữu Bật    : Đối xứng qua trục Thìn-Tuất (theo tháng)       ║
║  2. Văn Xương ↔ Văn Khúc : Đối xứng qua trục Thìn-Tuất (theo giờ)        ║
║  3. Địa Không ↔ Địa Kiếp : Đối xứng qua Hợi (theo giờ)                   ║
║  4. Tử Vi ↔ Thiên Phủ    : Đối xứng qua trục Dần-Thân (theo Cục+Ngày)    ║
║  5. Kinh Dương ↔ Đà La   : Đối xứng qua Lộc Tồn (±1 cung)               ║
║  6. Hỏa Tinh ↔ Linh Tinh : Đối xứng hướng đi (thuận↔nghịch)             ║
║  7. Cung Mệnh ↔ Cung Thân: Đối xứng qua điểm gốc (Dần+tháng)           ║
╚════════════════════════════════════════════════════════════════════════════════╝

╔════════════════════════════════════════════════════════════════════════════════╗
║                    ĐIỂM ĐẶC BIỆT - ĐỒNG CUNG                              ║
╠════════════════════════════════════════════════════════════════════════════════╣
║  • Xương Khúc đồng cung: Giờ Mão (tại Mùi) & Giờ Dậu (tại Sửu)          ║
║  • Không Kiếp đồng cung: Giờ Tý (tại Hợi) & Giờ Ngọ (tại Tỵ)            ║
║  • Tả Hữu đồng cung:    Tháng 4 (tại Mùi) & Tháng 10 (tại Sửu)          ║
║  • Mệnh Thân đồng cung:  Giờ Tý                                           ║
╚════════════════════════════════════════════════════════════════════════════════╝
""")


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("=" * 90)
    print("  PHÂN TÍCH QUY LUẬT DI CHUYỂN SAO - CHÍNH TINH, LỤC CÁT, LỤC SÁT")
    print("  Kèm 10 Thiên Can × 12 Cung Mệnh")
    print("=" * 90)
    
    analyze_chinh_tinh()
    analyze_luc_cat()
    analyze_luc_sat()
    analyze_comprehensive()
    print_summary()
