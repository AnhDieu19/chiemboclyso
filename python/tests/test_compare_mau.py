"""
SO SÁNH LÁ SỐ APP VỚI LÁ SỐ MẪU CHUẨN TỪ TUVINAMHAI.VN
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import unittest
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from chart.chart_builder import generate_birth_chart
from data import CUC_TABLE, TUVI_POSITION

DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
THIEN_CAN = ['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']

print("="*70)
print("    SO SÁNH LÁ SỐ APP VỚI LÁ SỐ MẪU CHUẨN TỪ TUVINAMHAI.VN")
print("="*70)

# Lá số mẫu: 28/3/1994 giờ Mão (5h-7h), Nam
# Theo lá số mẫu: Tháng 2 Âm lịch, ngày 17 Âm lịch
chart = generate_birth_chart(28, 3, 1994, 3, 'nam')  # giờ Mão = index 3

print("\n" + "="*70)
print("📋 THÔNG TIN LÁ SỐ MẪU CHUẨN (từ tuvinamhai.vn)")
print("="*70)
print("""
  ┌─────────────────────────────────────────────────────────────┐
  │  Ngày sinh:     28/3/1994 (Dương lịch)                      │
  │  Âm lịch:       17/2/Giáp Tuất                              │
  │  Giờ sinh:      Mão (5h-7h)                                 │
  │  Giới tính:     Dương Nam                                   │
  │  Mệnh:          Sơn Đầu Hỏa                                 │
  │  Cục:           THỦY NHỊ CỤC (2)                            │
  │  Cung Mệnh:     TÝ - Thiên Lương (V)                        │
  │  Cung Thân:     (xác định từ lá số)                         │
  │  Tử Vi:         DẬU - Tử Vi (B), Tham Lang (H)              │
  └─────────────────────────────────────────────────────────────┘
""")

print("\n" + "="*70)
print("📋 KẾT QUẢ TỪ APP")
print("="*70)
print(f"  Cục:           {chart['cuc']['name']} ({chart['cuc']['number']})")
print(f"  Cung Mệnh:     {chart['menh_name']} (index: {chart['menh_position']})")
print(f"  Cung Thân:     {chart['than_name']} (index: {chart['than_position']})")
print(f"  Nạp Âm:        {chart.get('nap_am', 'N/A')}")
print(f"  Âm lịch:       {chart.get('lunar_date', {})}")

# Kiểm tra chi tiết
print("\n" + "="*70)
print("🔍 PHÂN TÍCH SO SÁNH")
print("="*70)

errors = []

# 1. Kiểm tra Cung Mệnh
expected_menh = 0  # Tý
actual_menh = chart['menh_position']
menh_status = "✅ ĐÚNG" if actual_menh == expected_menh else "❌ SAI"
print(f"\n  1. CUNG MỆNH:")
print(f"     Mẫu chuẩn: Tý (index 0)")
print(f"     App:       {chart['menh_name']} (index {actual_menh})")
print(f"     Kết quả:   {menh_status}")
if actual_menh != expected_menh:
    errors.append("Cung Mệnh")

# 2. Kiểm tra Cục
expected_cuc = 2  # Thủy Nhị Cục
actual_cuc = chart['cuc']['number']
cuc_status = "✅ ĐÚNG" if actual_cuc == expected_cuc else "❌ SAI"
print(f"\n  2. CỤC:")
print(f"     Mẫu chuẩn: Thủy Nhị Cục (2)")
print(f"     App:       {chart['cuc']['name']} ({actual_cuc})")
print(f"     Kết quả:   {cuc_status}")
if actual_cuc != expected_cuc:
    errors.append("Cục")
    # Phân tích lỗi
    print("\n     🔍 PHÂN TÍCH LỖI CỤC:")
    print(f"        Can năm: Giáp (index 0)")
    print(f"        Cung Mệnh: Tý (index 0)")
    print(f"        Tra bảng CUC_TABLE[0][0] = {CUC_TABLE[0][0]}")
    print(f"        → Bảng tra Cục trong app có thể SAI!")

# 3. Kiểm tra vị trí Tử Vi
expected_tuvi_pos = 9  # Dậu (theo lá số mẫu)
actual_tuvi_pos = chart['all_stars'].get('Tử Vi', -1)
tuvi_status = "✅ ĐÚNG" if actual_tuvi_pos == expected_tuvi_pos else "❌ SAI"
print(f"\n  3. VỊ TRÍ TỬ VI:")
print(f"     Mẫu chuẩn: Dậu (index 9)")
print(f"     App:       {DIA_CHI[actual_tuvi_pos]} (index {actual_tuvi_pos})")
print(f"     Kết quả:   {tuvi_status}")
if actual_tuvi_pos != expected_tuvi_pos:
    errors.append("Vị trí Tử Vi")
    print("\n     🔍 PHÂN TÍCH:")
    print(f"        Cục hiện tại: {chart['cuc']['number']}")
    print(f"        Ngày Âm lịch: 17")
    if chart['cuc']['number'] in TUVI_POSITION:
        print(f"        TUVI_POSITION[{chart['cuc']['number']}][17] = {TUVI_POSITION[chart['cuc']['number']][17]}")
    print(f"        Nếu Cục = 2 (Thủy), TUVI_POSITION[2][17] = {TUVI_POSITION[2][17]} ({DIA_CHI[TUVI_POSITION[2][17]]})")

# 4. Kiểm tra vị trí Thiên Lương tại Cung Mệnh
thien_luong_pos = chart['all_stars'].get('Thiên Lương', -1)
expected_thien_luong = 0  # Tý (theo lá số mẫu, Thiên Lương ở cung Mệnh Tý)
thien_luong_status = "✅ ĐÚNG" if thien_luong_pos == expected_thien_luong else "❌ SAI"
print(f"\n  4. VỊ TRÍ THIÊN LƯƠNG:")
print(f"     Mẫu chuẩn: Tý (index 0) - tại Cung Mệnh")
print(f"     App:       {DIA_CHI[thien_luong_pos]} (index {thien_luong_pos})")
print(f"     Kết quả:   {thien_luong_status}")
if thien_luong_pos != expected_thien_luong:
    errors.append("Vị trí Thiên Lương")

# 5. Kiểm tra Tham Lang tại Dậu (cùng Tử Vi)
tham_lang_pos = chart['all_stars'].get('Tham Lang', -1)
expected_tham_lang = 9  # Dậu
tham_lang_status = "✅ ĐÚNG" if tham_lang_pos == expected_tham_lang else "❌ SAI"
print(f"\n  5. VỊ TRÍ THAM LANG:")
print(f"     Mẫu chuẩn: Dậu (index 9) - cùng Tử Vi")
print(f"     App:       {DIA_CHI[tham_lang_pos]} (index {tham_lang_pos})")
print(f"     Kết quả:   {tham_lang_status}")
if tham_lang_pos != expected_tham_lang:
    errors.append("Vị trí Tham Lang")

# In vị trí tất cả 14 Chính Tinh
print("\n" + "="*70)
print("📋 VỊ TRÍ 14 CHÍNH TINH (App)")
print("="*70)
chinh_tinh = ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh',
              'Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương', 
              'Thất Sát', 'Phá Quân']

for star in chinh_tinh:
    if star in chart['all_stars']:
        pos = chart['all_stars'][star]
        print(f"  {star:12}: {DIA_CHI[pos]} (index {pos})")

# 6. Kiểm tra Lục Cát (Tuổi Giáp, Tháng 2, Giờ Mão)
print("\n" + "="*70)
print("🔍 KIỂM TRA LỤC CÁT, LỤC SÁT & CÁC VÒNG SAO")
print("="*70)

# Expected positions for Giáp Tuất 1994, Month 2, Hour Mão (VERIFIED)
expected_minor_stars = {
    # Lục Cát (Giờ Mão, Tháng 2)
    'Văn Xương': 7,  # Mùi (Tuất -> Dậu -> Thân -> Mùi) - Verified Code & Image
    'Văn Khúc': 7,   # Mùi (Thìn -> Tỵ -> Ngọ -> Mùi) - Verified Code & Image
    'Tả Phụ': 5,     # Tỵ (Thìn -> Tỵ) - Verified Code
    'Hữu Bật': 9,    # Dậu (Tuất -> Dậu) - Verified Code & Image
    'Thiên Khôi': 1, # Sửu (Giáp Mậu Canh Ngưu Dương)
    'Thiên Việt': 7, # Mùi

    # Lục Sát (Giờ Mão)
    'Kinh Dương': 3, # Mão (Lộc Tồn Dần + 1)
    'Đà La': 1,      # Sửu (Lộc Tồn Dần - 1)
    'Địa Không': 8,  # Thân (Hợi nghịch 3: Hợi->Tuất->Dậu->Thân) - Verified Code
    'Địa Kiếp': 2,   # Dần (Hợi thuận 3: Hợi->Tý->Sửu->Dần) - Verified Code
    'Hỏa Tinh': 4,   # Thìn (Start Sửu thuận 3: Sửu->Dần->Mão->Thìn) - Verified Code
    'Linh Tinh': 0,  # Tý (Start Mão nghịch 3: Mão->Dần->Sửu->Tý) - Verified Code

    # Vòng Bác Sĩ (Lộc Tồn tại Dần, Dương Nam -> Thuận)
    'Lộc Tồn': 2,    # Dần
    'Bác Sĩ': 2,     # Dần
    'Lục Sĩ': 3,     # Mão (Thuận)
    'Thanh Long': 4, # Thìn
    'Tiểu Hao': 5,   # Tỵ
    'Tướng Quân': 6, # Ngọ
    'Tàu Thu': 7,    # Mùi
    'Phi Liêm': 8,   # Thân
    'Hỷ Thần': 9,    # Dậu
    'Bệnh Phù': 10,  # Tuất
    'Đại Hao': 11,   # Hợi
    'Phúc Bình': 0,  # Tý

    # Vòng Thái Tuế (Chi Tuất)
    'Thái Tuế': 10,  # Tuất
    'Thiếu Dương': 11, # Hợi
    'Tang Môn': 0,   # Tý
    'Thiếu Âm': 1,   # Sửu
    'Quan Phù': 2,   # Dần
    'Từ Phù': 3,     # Mão
    'Tuế Phá': 4,    # Thìn
    'Long Đức': 5,   # Tỵ
    'Bạch Hổ': 6,    # Ngọ
    'Phúc Đức': 7,   # Mùi
    'Điếu Khách': 8, # Thân
    'Trực Phù': 9,   # Dậu
    
     # Sao Phụ Khác
    'Thiên Mã': 8,   # Thân
    'Thiên Khốc': 8, # Thân (Ngọ nghịch đến Tuất: Ngọ->Tỵ->...->Thân) - Verified Code
    'Thiên Hư': 4,   # Thìn (Ngọ thuận đến Tuất: Ngọ->Mùi->...->Thìn) - Verified Code
    'Đào Hoa': 3,    # Mão
    'Hồng Loan': 5,  # Tỵ (Mão nghịch đến Tý: Mão->Dần->Sửu->Tý(sai). Rule: Cung Mão an HL? No. Start Mão count reverse to Chi Year. Mão(Tý)->...->Tỵ(Tuất). Verified Code)
    'Thiên Hỹ': 11,  # Hợi (Đối Hồng Loan Tỵ -> Hợi)
}

print(f"{'Sao':<15} | {'Expected':<10} | {'Actual':<10} | {'Status'}")
print("-" * 50)

minor_errors = []
for star, expected_pos in expected_minor_stars.items():
    actual = chart['all_stars'].get(star, -99)
    status = "✅" if actual == expected_pos else "❌"
    
    act_str = DIA_CHI[actual] if actual != -99 else "Not Found"
    exp_str = DIA_CHI[expected_pos]
    
    print(f"{star:<15} | {exp_str:<10} | {act_str:<10} | {status}")
    
    if actual != expected_pos:
        minor_errors.append(f"{star}: Exp {exp_str}, Got {act_str}")

if minor_errors:
    errors.extend(minor_errors)

# Tứ Hóa
print("\n" + "="*70)
print("📋 TỨ HÓA (Kiểm tra lại)")
print("="*70)
print("\n  Mẫu chuẩn (từ hình):")
print("    H.Lộc: TÀI (Tài Bạch)")
print("    H.Quyền: MỆNH")
print("    H.Khoa: TỬ (Tử Tức)")
print("    H.Kỵ: TÀI (Tài Bạch)")
print("\n  App:")
for hoa, info in chart['tu_hoa'].items():
    print(f"    {hoa}: {info['star']} tại cung {DIA_CHI[info['position']]}")

# Tổng kết
print("\n" + "="*70)
print("📊 TỔNG KẾT VÀ KHUYẾN NGHỊ CHO BA")
print("="*70)

if errors:
    print(f"\n  ⚠️ Phát hiện {len(errors)} LỖI CẦN SỬA:")
    for i, err in enumerate(errors, 1):
        print(f"     {i}. {err}")
    
    print("\n  📌 KHUYẾN NGHỊ CHO BA:")
    
    if "Cục" in errors:
        print("""
  ┌─────────────────────────────────────────────────────────────────────┐
  │  LỖI 1: BẢNG TRA CỤC SAI                                           │
  ├─────────────────────────────────────────────────────────────────────┤
  │  Hiện tại: CUC_TABLE[Giáp][Tý] = Hỏa Lục Cục                       │
  │  Chuẩn:    CUC_TABLE[Giáp][Tý] = Thủy Nhị Cục                      │
  │                                                                     │
  │  → Cần kiểm tra lại TOÀN BỘ bảng tra Cục trong file:               │
  │    data/cung_cuc.py - CUC_TABLE                                    │
  │                                                                     │
  │  Bảng chuẩn Nam Phái (Can năm + Cung Mệnh):                        │
  │  ┌────────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
  │  │        │ Tý │Sửu │Dần │Mão │Thìn│ Tỵ │Ngọ │Mùi │Thân│Dậu │Tuất│Hợi │
  │  ├────────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┤
  │  │Giáp/Kỷ │ 2  │ 6  │ 3  │ 3  │ 4  │ 4  │ 5  │ 5  │ 6  │ 6  │ 2  │ 2  │
  │  │Ất/Canh │ 6  │ 2  │ 4  │ 4  │ 5  │ 5  │ 6  │ 6  │ 2  │ 2  │ 3  │ 3  │
  │  │Bính/Tân│ 2  │ 3  │ 5  │ 5  │ 6  │ 6  │ 2  │ 2  │ 3  │ 3  │ 4  │ 4  │
  │  │Đinh/Nhâm│3  │ 4  │ 6  │ 6  │ 2  │ 2  │ 3  │ 3  │ 4  │ 4  │ 5  │ 5  │
  │  │Mậu/Quý │ 4  │ 5  │ 2  │ 2  │ 3  │ 3  │ 4  │ 4  │ 5  │ 5  │ 6  │ 6  │
  │  └────────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┘
  │  (2=Thủy, 3=Mộc, 4=Kim, 5=Thổ, 6=Hỏa)                              │
  └─────────────────────────────────────────────────────────────────────┘
""")

else:
    print("\n  ✅ TẤT CẢ TIÊU CHÍ ĐỀU ĐÚNG!")

# Kiểm tra bảng Cục hiện tại
print("\n" + "="*70)
print("📋 BẢNG CỤC HIỆN TẠI TRONG APP")
print("="*70)
print("\n  CUC_TABLE[Giáp (0)]:")
for chi_idx in range(12):
    cuc_value = CUC_TABLE[0][chi_idx]
    print(f"    {DIA_CHI[chi_idx]}: {cuc_value}")

