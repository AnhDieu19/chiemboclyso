"""
═══════════════════════════════════════════════════════════════════════════════
PHÂN TÍCH: Mối quan hệ cố định giữa 14 Chính Tinh trong các Cung
═══════════════════════════════════════════════════════════════════════════════

MỆNH ĐỀ CHỨNG MINH:
1. Người dữ (Sát-Phá-Tham) lấy vợ/chồng hiền → Phu Thê luôn có sao hiền
2. Người hiền lấy vợ/chồng dữ/ăn chơi
3. Quy luật Âm-Dương cân bằng trong 14 Chính Tinh

NGUYÊN LÝ TOÁN HỌC:
- 14 Chính Tinh chia 2 nhóm: Tử Vi (6 sao) và Thiên Phủ (8 sao)
- Khoảng cách giữa các sao TRONG CÙNG NHÓM là CỐ ĐỊNH (bất biến)
- Thứ tự Cung: Mệnh → Phụ Mẫu → ... → Phu Thê → Huynh Đệ (counter-clockwise)
- Phu Thê luôn ở vị trí Mệnh + 10 ≡ Mệnh − 2 (mod 12)
- Vì vậy, sao "cách Mệnh 2 vị trí" luôn nằm ở Phu Thê

Tác giả: Tử Vi Analysis Engine
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from data.chinh_tinh import CHINH_TINH, TU_VI_GROUP_OFFSET, THIEN_PHU_GROUP_OFFSET
from data.cung_cuc import CUNG_ORDER

# ═══════════════════════════════════════════════════════════════
# CONSTANTS
# ═══════════════════════════════════════════════════════════════
TV_STARS = CHINH_TINH['tu_vi_group']
TP_STARS = CHINH_TINH['thien_phu_group']

# Tính chất cơ bản của 14 Chính Tinh
STAR_NATURE = {
    # Nhóm Tử Vi
    'Tử Vi':     {'nature': 'HIỀN', 'desc': 'Đế tinh, chủ quý, ổn định, hiền'},
    'Thiên Cơ':  {'nature': 'TRUNG', 'desc': 'Mưu trí, linh hoạt, thông minh nhưng bất định'},
    'Thái Dương': {'nature': 'HIỀN', 'desc': 'Quý nhân, rộng lượng, quang minh'},
    'Vũ Khúc':   {'nature': 'DỮ',   'desc': 'Tài tinh, cô khắc, cương trực, nghiêm'},
    'Thiên Đồng': {'nature': 'HIỀN', 'desc': 'Phúc tinh, hiền lành, nhàn nhã'},
    'Liêm Trinh': {'nature': 'DỮ',   'desc': 'Tù tinh, đào hoa, bất trắc, đẹp nhưng dữ'},
    # Nhóm Thiên Phủ  
    'Thiên Phủ':  {'nature': 'HIỀN', 'desc': 'Phúc tinh lớn, hiền hòa, kho tàng'},
    'Thái Âm':   {'nature': 'ĐẸP',  'desc': 'Nhu mì, đẹp, hiền, nữ tính'},
    'Tham Lang':  {'nature': 'DỮ',   'desc': 'Đào hoa, tham, ăn chơi, dục vọng'},
    'Cự Môn':    {'nature': 'DỮ',   'desc': 'Khẩu thiệt, thị phi, ám tinh'},
    'Thiên Tướng': {'nature': 'HIỀN', 'desc': 'Ấn tinh, hiền lành, quý nhân, ổn định'},
    'Thiên Lương': {'nature': 'HIỀN', 'desc': 'Ấm tinh, nhân từ, bậc trưởng bối che chở'},
    'Thất Sát':  {'nature': 'DỮ',   'desc': 'Sát tinh, cương mãnh, quyết đoán, oai phong'},
    'Phá Quân':  {'nature': 'DỮ',   'desc': 'Phá cách, biến động mạnh, tiên phong'},
}


def compute_all_pairs():
    """
    Với mỗi Chính Tinh, tính xem khi sao đó tọa Mệnh thì tất cả các Cung khác có sao gì.
    CHỈ XÉT TRONG CÙNG NHÓM (vì khoảng cách cố định).
    """
    
    print("=" * 90)
    print("BẢNG KHOẢNG CÁCH CỐ ĐỊNH GIỮA 14 CHÍNH TINH")
    print("=" * 90)
    
    # ── Nhóm Thiên Phủ: 8 sao, offset 0,1,2,3,4,5,6,10 ──
    print("\n" + "─" * 90)
    print("NHÓM THIÊN PHỦ — 8 sao (offset thuận chiều từ Thiên Phủ)")
    print("─" * 90)
    
    tp_offsets = dict(zip(TP_STARS, THIEN_PHU_GROUP_OFFSET))
    
    print(f"\n{'Sao':<15} {'Offset':<8} Khoảng cách đến các sao khác")
    print("-" * 90)
    for star, offset in tp_offsets.items():
        distances = []
        for other, other_offset in tp_offsets.items():
            if other == star:
                continue
            d = (other_offset - offset) % 12
            d_min = min(d, 12 - d)
            distances.append(f"{other}({d_min})")
        nature = STAR_NATURE[star]['nature']
        print(f"{star:<15} [{nature:>4}]  {', '.join(distances)}")
    
    # ── Nhóm Tử Vi: 6 sao ──
    print(f"\n{'─' * 90}")
    print("NHÓM TỬ VI — 6 sao (offset nghịch chiều từ Tử Vi)")
    print("─" * 90)
    
    tv_offsets = dict(zip(TV_STARS, TU_VI_GROUP_OFFSET))
    
    print(f"\n{'Sao':<15} {'Offset':<8} Khoảng cách đến các sao khác")
    print("-" * 90)
    for star, offset in tv_offsets.items():
        distances = []
        for other, other_offset in tv_offsets.items():
            if other == star:
                continue
            d = (other_offset - offset) % 12
            d_min = min(d, 12 - d)
            distances.append(f"{other}({d_min})")
        nature = STAR_NATURE[star]['nature']
        print(f"{star:<15} [{nature:>4}]  {', '.join(distances)}")


def analyze_menh_phu_the():
    """
    PHÂN TÍCH CHÍNH: Khi sao X tọa Mệnh → sao nào tọa Phu Thê?
    
    Phu Thê = Mệnh + 10 = Mệnh - 2 (mod 12)
    → Sao cách X đúng 2 vị trí (CW) = sao ở offset (X_offset - 2) trong nhóm
    """
    
    print("\n" + "=" * 90)
    print("CHỨNG MINH: SAO TẠ MỆNH → SAO TẠI PHU THÊ (Cách 2 cung CW)")
    print("=" * 90)
    
    phu_the_idx = CUNG_ORDER.index('Phu Thê')  # = 10
    print(f"\nXác nhận: Phu Thê = cung thứ {phu_the_idx} tính từ Mệnh = Mệnh + {phu_the_idx} ≡ Mệnh − 2 (mod 12)")
    
    # ── Nhóm Thiên Phủ ──
    print(f"\n{'─' * 90}")
    print("CẶP MỆNH ↔ PHU THÊ TRONG NHÓM THIÊN PHỦ (BẤT BIẾN)")
    print("─" * 90)
    
    tp_offsets = dict(zip(TP_STARS, THIEN_PHU_GROUP_OFFSET))
    offset_to_star = {v: k for k, v in tp_offsets.items()}
    
    tp_pairs = []
    for star, offset in tp_offsets.items():
        # Sao tại Phu Thê = sao có offset = (offset - 2) mod 12
        phu_the_offset = (offset - 2) % 12
        phu_the_star = offset_to_star.get(phu_the_offset)
        
        if phu_the_star:
            nature_menh = STAR_NATURE[star]['nature']
            nature_pt = STAR_NATURE[phu_the_star]['nature']
            complement = "✓ ÂM-DƯƠNG" if nature_menh != nature_pt else "= ĐỒNG TÍNH"
            tp_pairs.append((star, phu_the_star, nature_menh, nature_pt, complement))
            print(f"\n  {star:<12} [{nature_menh:>4}] tọa MỆNH")
            print(f"  → {phu_the_star:<12} [{nature_pt:>4}] tọa PHU THÊ  {complement}")
            print(f"     {STAR_NATURE[star]['desc']}")
            print(f"     → lấy: {STAR_NATURE[phu_the_star]['desc']}")
        else:
            print(f"\n  {star:<12} [{STAR_NATURE[star]['nature']:>4}] tọa MỆNH")
            print(f"  → Phu Thê: sao NHÓM TỬ VI (thay đổi tùy lá số)")
    
    # ── Nhóm Tử Vi ──
    print(f"\n{'─' * 90}")
    print("CẶP MỆNH ↔ PHU THÊ TRONG NHÓM TỬ VI (BẤT BIẾN)")
    print("─" * 90)
    
    tv_offsets = dict(zip(TV_STARS, TU_VI_GROUP_OFFSET))
    tv_offset_to_star = {v % 12: k for k, v in tv_offsets.items()}
    
    for star, offset in tv_offsets.items():
        phu_the_offset = (offset - 2) % 12
        phu_the_star = tv_offset_to_star.get(phu_the_offset)
        
        if phu_the_star:
            nature_menh = STAR_NATURE[star]['nature']
            nature_pt = STAR_NATURE[phu_the_star]['nature']
            complement = "✓ ÂM-DƯƠNG" if nature_menh != nature_pt else "= ĐỒNG TÍNH"  
            print(f"\n  {star:<12} [{nature_menh:>4}] tọa MỆNH")
            print(f"  → {phu_the_star:<12} [{nature_pt:>4}] tọa PHU THÊ  {complement}")
            print(f"     {STAR_NATURE[star]['desc']}")
            print(f"     → lấy: {STAR_NATURE[phu_the_star]['desc']}")
        else:
            print(f"\n  {star:<12} [{STAR_NATURE[star]['nature']:>4}] tọa MỆNH")
            print(f"  → Phu Thê: sao NHÓM THIÊN PHỦ (thay đổi tùy lá số)")
    
    return tp_pairs


def analyze_full_cung_layout():
    """
    Khi một sao Nhóm Thiên Phủ tọa Mệnh, tất cả 8 sao nhóm đó phân bố
    vào các cung CỐ ĐỊNH. Hiển thị toàn bộ.
    """
    
    print("\n" + "=" * 90)
    print("BỐ CỤC TOÀN BỘ 12 CUNG — KHI SAO NHÓM THIÊN PHỦ TỌA MỆNH")
    print("=" * 90)
    
    tp_offsets = dict(zip(TP_STARS, THIEN_PHU_GROUP_OFFSET))
    
    for menh_star in TP_STARS:
        menh_offset = tp_offsets[menh_star]
        menh_nature = STAR_NATURE[menh_star]['nature']
        
        print(f"\n{'─' * 70}")
        print(f"★ {menh_star} [{menh_nature}] TỌA MỆNH")
        print(f"{'─' * 70}")
        
        # Tìm sao nhóm TP rơi vào từng cung
        for cung_idx, cung_name in enumerate(CUNG_ORDER):
            # offset cần có để rơi vào cung này
            needed_offset = (menh_offset + cung_idx) % 12
            star_in_cung = None
            for s, o in tp_offsets.items():
                if o == needed_offset:
                    star_in_cung = s
                    break
            
            if star_in_cung:
                nature = STAR_NATURE[star_in_cung]['nature']
                marker = "◀◀◀" if cung_name in ['Mệnh', 'Phu Thê'] else ""
                highlight = "★" if cung_name == 'Mệnh' else ("♥" if cung_name == 'Phu Thê' else " ")
                print(f"  {highlight} {cung_name:<12} → {star_in_cung:<12} [{nature:>4}]  {marker}")
            else:
                print(f"    {cung_name:<12} → (sao nhóm Tử Vi)")


def analyze_beauty_marriage():
    """
    Phân tích: Phụ nữ đẹp (Thái Âm, Tham Lang) và hôn nhân
    """
    
    print("\n" + "=" * 90)
    print("PHÂN TÍCH: ĐẸP ↔ HÔN NHÂN — VỊ TRÍ THÁI ÂM & THAM LANG")
    print("=" * 90)
    
    tp_offsets = dict(zip(TP_STARS, THIEN_PHU_GROUP_OFFSET))
    
    # Khi sao tọa Mệnh → Thái Âm ở đâu? (Thái Âm = đẹp/nhu mì)
    print(f"\n{'─' * 70}")
    print("THÁI ÂM (đẹp, nhu mì) RƠI VÀO CUNG NÀO?")
    print("─" * 70)
    
    tai_am_offset = tp_offsets['Thái Âm']  # = 1
    
    for menh_star in TP_STARS:
        menh_offset = tp_offsets[menh_star]
        # Thái Âm ở cung nào khi menh_star tọa Mệnh?
        tai_am_cung_idx = (tai_am_offset - menh_offset) % 12
        cung_name = CUNG_ORDER[tai_am_cung_idx]
        nature = STAR_NATURE[menh_star]['nature']
        print(f"  {menh_star:<14} [{nature:>4}] Mệnh → Thái Âm [ĐẸP] ở {cung_name}")


def analyze_sat_pha_tham_triad():
    """
    Chứng minh: Sát-Phá-Tham LUÔN nằm ở Tam Hợp Mệnh-Quan-Tài
    """
    
    print("\n" + "=" * 90)
    print("CHỨNG MINH: SÁT – PHÁ – THAM LUÔN TAM HỢP (CÁCH NHAU 4 CUNG)")
    print("=" * 90)
    
    tp_offsets = dict(zip(TP_STARS, THIEN_PHU_GROUP_OFFSET))
    
    sat = tp_offsets['Thất Sát']   # 6
    pha = tp_offsets['Phá Quân']   # 10
    tham = tp_offsets['Tham Lang']  # 2
    
    d_sat_tham = (sat - tham) % 12   # 4
    d_pha_sat = (pha - sat) % 12     # 4
    d_tham_pha = (tham - pha) % 12   # 4
    
    print(f"\n  Offset: Sát={sat}, Phá={pha}, Tham={tham}")
    print(f"  Khoảng cách: Sát→Tham = {d_sat_tham}, Phá→Sát = {d_pha_sat}, Tham→Phá = {d_tham_pha}")
    print(f"  → Ba sao cách nhau đúng 4 cung = TAM HỢP")
    
    print(f"\n  Khi một trong ba tọa Mệnh:")
    print(f"  ┌─────────────────┬────────────────┬────────────────┐")
    print(f"  │    Mệnh (+0)    │  Quan Lộc (+4) │  Tài Bạch (+8) │")
    print(f"  ├─────────────────┼────────────────┼────────────────┤")
    
    for major in ['Thất Sát', 'Phá Quân', 'Tham Lang']:
        major_offset = tp_offsets[major]
        cung_stars = {}
        for s in ['Thất Sát', 'Phá Quân', 'Tham Lang']:
            s_offset = tp_offsets[s]
            cung_idx = (s_offset - major_offset) % 12
            cung_stars[s] = CUNG_ORDER[cung_idx]
        
        quan_star = [s for s, c in cung_stars.items() if c == 'Quan Lộc'][0] if any(c == 'Quan Lộc' for c in cung_stars.values()) else '?'
        tai_star = [s for s, c in cung_stars.items() if c == 'Tài Bạch'][0] if any(c == 'Tài Bạnh' or c == 'Tài Bạch' for c in cung_stars.values()) else '?'
        
        # Fix: find the other two
        others = [s for s in ['Thất Sát', 'Phá Quân', 'Tham Lang'] if s != major]
        o1_cung = (tp_offsets[others[0]] - major_offset) % 12
        o2_cung = (tp_offsets[others[1]] - major_offset) % 12
        
        nature = STAR_NATURE[major]['nature']
        print(f"  │ {major:<13}[{nature}]│ {others[0]:<14} │ {others[1]:<14} │")
    
    print(f"  └─────────────────┴────────────────┴────────────────┘")
    print(f"\n  → Sát-Phá-Tham luôn chiếm Tam Hợp: Mệnh—Quan Lộc—Tài Bạch")
    print(f"  → Cung Phu Thê LUÔN nằm NGOÀI tam hợp này → do sao KHÁC chiếm")


def verify_with_real_charts():
    """
    Kiểm chứng bằng lá số thực: tạo lá số với tất cả 12 vị trí Tử Vi,
    rồi kiểm tra sao tại Mệnh và Phu Thê.
    """
    
    print("\n" + "=" * 90)
    print("KIỂM CHỨNG BẰNG THUẬT TOÁN — TẤT CẢ 12 VỊ TRÍ TỬ VI")
    print("=" * 90)
    
    from stars.chinh_tinh_placer import place_chinh_tinh, calculate_tuvi_position
    
    DIA_CHI = ['Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ','Mùi','Thân','Dậu','Tuất','Hợi']
    
    print(f"\n{'TV Pos':<8} | {'Mệnh Star':<14} → {'Phu Thê Star':<14} | {'Mệnh':>6} → {'PT':>6} | Note")
    print("-" * 90)
    
    # Thử tất cả Mệnh positions khi TV ở từng vị trí
    for tv_pos in range(12):
        all_stars = place_chinh_tinh(tv_pos)
        
        # Tạo reverse map: position → [star_names]
        pos_to_stars = {}
        for star_name, star_pos in all_stars.items():
            if star_pos not in pos_to_stars:
                pos_to_stars[star_pos] = []
            pos_to_stars[star_pos].append(star_name)
        
        # Với mỗi vị trí Mệnh có thể
        for menh_pos in range(12):
            phu_the_pos = (menh_pos + 10) % 12
            
            menh_stars = pos_to_stars.get(menh_pos, [])
            pt_stars = pos_to_stars.get(phu_the_pos, [])
            
            # Chỉ hiển thị khi Mệnh có Chính Tinh
            if menh_stars:
                for ms in menh_stars:
                    pt_display = ', '.join(pt_stars) if pt_stars else '(trống Chính Tinh)'
                    m_nature = STAR_NATURE[ms]['nature']
                    
                    # Check complement
                    pt_natures = [STAR_NATURE[p]['nature'] for p in pt_stars] if pt_stars else []
                    complement = ""
                    if any(n != m_nature for n in pt_natures):
                        complement = "✓ ĐỐI LẬP"
                    elif pt_stars:
                        complement = "  đồng tính"
                    
                    print(f"TV={DIA_CHI[tv_pos]:>3} M={DIA_CHI[menh_pos]:>3} | {ms:<14} → {pt_display:<14} | [{m_nature:>4}] → [{','.join(pt_natures) if pt_natures else '?':>4}] | {complement}")


def summary():
    """Tóm tắt phát hiện"""
    
    print("\n" + "═" * 90)
    print("TÓM TẮT: QUY LUẬT ÂM-DƯƠNG CÂN BẰNG TRONG 14 CHÍNH TINH")
    print("═" * 90)
    
    print("""
┌─────────────────────────────────────────────────────────────────────────────┐
│ TRONG NHÓM THIÊN PHỦ (8 sao) — 6 cặp Mệnh-Phu Thê BẤT BIẾN:           │
│                                                                           │
│   Thất Sát  [DỮ]  Mệnh  →  Thiên Tướng [HIỀN]  Phu Thê   ✓ Đối lập   │
│   Thiên Tướng [HIỀN] Mệnh →  Tham Lang   [DỮ]   Phu Thê   ✓ Đối lập   │
│   Tham Lang [DỮ]  Mệnh  →  Thiên Phủ  [HIỀN]  Phu Thê   ✓ Đối lập   │
│   Thiên Phủ [HIỀN] Mệnh  →  Phá Quân   [DỮ]   Phu Thê   ✓ Đối lập   │
│   Cự Môn   [DỮ]  Mệnh  →  Thái Âm   [ĐẸP]   Phu Thê   ✓ Đối lập   │
│   Thiên Lương [HIỀN] Mệnh →  Cự Môn    [DỮ]   Phu Thê   ✓ Đối lập   │
│                                                                           │
│ → CHUỖI VÒNG: Sát → Tướng → Tham → Phủ → Phá (→ TV nhóm)              │
│                Cự ↔ Âm,  Lương → Cự                                      │
│ → 6/6 cặp đều ĐỐI LẬP tính chất = QUY LUẬT ÂM DƯƠNG CÂN BẰNG          │
├─────────────────────────────────────────────────────────────────────────────┤
│ TRONG NHÓM TỬ VI (6 sao) — 3 cặp BẤT BIẾN:                              │
│                                                                           │
│   Tử Vi    [HIỀN] Mệnh  →  Thiên Cơ   [TRUNG]  Phu Thê                │
│   Thiên Cơ [TRUNG] Mệnh →  Vũ Khúc    [DỮ]    Phu Thê   ✓ Đối lập   │
│   Thái Dương [HIỀN] Mệnh →  Thiên Đồng  [HIỀN]  Phu Thê                │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHỨNG MINH CÁC CÂU NÓI DÂN GIAN:                                        │
│                                                                           │
│ 1. "Vợ dữ lấy chồng hiền":                                               │
│    → Thất Sát Mệnh → Thiên Tướng Phu Thê (LUÔN ĐÚNG)                   │
│    → Phá Quân/Tham Lang Mệnh → các sao khác Phu Thê (chi tiết ở trên)  │
│                                                                           │
│ 2. "Chồng hiền lấy vợ ăn chơi":                                          │
│    → Thiên Tướng Mệnh → Tham Lang Phu Thê (LUÔN ĐÚNG)                   │
│    → Thiên Phủ Mệnh → Phá Quân Phu Thê (LUÔN ĐÚNG)                     │
│                                                                           │
│ 3. "Người thị phi lấy vợ/chồng đẹp":                                     │
│    → Cự Môn Mệnh → Thái Âm Phu Thê (LUÔN ĐÚNG)                         │
│                                                                           │
│ 4. Sát – Phá – Tham LUÔN chiếm Tam Hợp Mệnh–Quan Lộc–Tài Bạch          │
│    → Ba sao dữ gom về sự nghiệp & tài chính                              │
│    → Phu Thê luôn "thoát" ra ngoài, được sao hiền bảo vệ                │
└─────────────────────────────────────────────────────────────────────────────┘
""")


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    compute_all_pairs()
    pairs = analyze_menh_phu_the()
    analyze_full_cung_layout()
    analyze_beauty_marriage()
    analyze_sat_pha_tham_triad()
    verify_with_real_charts()
    summary()
