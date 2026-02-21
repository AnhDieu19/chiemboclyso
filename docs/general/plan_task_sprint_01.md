# 📋 SPRINT 01 - TASK ASSIGNMENT

## 📅 Thông Tin Sprint

| Thông tin | Chi tiết |
|-----------|----------|
| Sprint | 01 |
| Ngày bắt đầu | 16/12/2025 |
| Ngày kết thúc | 23/12/2025 |
| Mục tiêu | Bổ sung Mệnh Chủ/Thân Chủ + Tăng cường luận giải Cách Cục |

---

# 🧑‍💻 TASK CHO DEVELOPER

## TASK-DEV-001: Hiển thị Mệnh Chủ và Thân Chủ trên lá số

### Mô tả
Bổ sung hiển thị **Mệnh Chủ** và **Thân Chủ** một cách rõ ràng trên giao diện lá số.

### Yêu cầu chi tiết

#### 1. Backend (Python)

**File cần chỉnh sửa:** `chart/chart_builder.py`

Mệnh Chủ và Thân Chủ đã được tính toán trong code (xem `data/phu_tinh_bo_sung.py`):

```python
# Đã có sẵn - kiểm tra output:
'menh_chu': menh_than_chu['menh_chu'],  # VD: "Tham Lang"
'than_chu': menh_than_chu['than_chu']   # VD: "Linh Tinh"
```

**Bảng Mệnh Chủ** (theo Cung Mệnh):

| Cung Mệnh | Mệnh Chủ |
|-----------|----------|
| Tý | Tham Lang |
| Sửu | Cự Môn |
| Dần | Lộc Tồn |
| Mão | Văn Khúc |
| Thìn | Liêm Trinh |
| Tỵ | Vũ Khúc |
| Ngọ | Phá Quân |
| Mùi | Vũ Khúc |
| Thân | Liêm Trinh |
| Dậu | Văn Khúc |
| Tuất | Lộc Tồn |
| Hợi | Cự Môn |

**Bảng Thân Chủ** (theo Chi năm sinh):

| Chi Năm | Thân Chủ |
|---------|----------|
| Tý | Linh Tinh |
| Sửu | Thiên Tướng |
| Dần | Thiên Lương |
| Mão | Thiên Đồng |
| Thìn | Văn Xương |
| Tỵ | Thiên Cơ |
| Ngọ | Hỏa Tinh |
| Mùi | Thiên Tướng |
| Thân | Thiên Lương |
| Dậu | Thiên Đồng |
| Tuất | Văn Xương |
| Hợi | Thiên Cơ |

#### 2. Frontend (HTML/JS)

**File cần chỉnh sửa:** `templates/index.html`

**Vị trí hiển thị:** Trong phần thông tin trung tâm của lá số

**UI Design:**

```
┌─────────────────────────────────────────┐
│           THÔNG TIN TRUNG TÂM           │
├─────────────────────────────────────────┤
│  Họ tên: _______________                │
│  Năm sinh: Quý Dậu (1993)              │
│  Cục: Mộc Tam Cục                       │
│  Nạp Âm: Kiếm Phong Kim                │
│                                         │
│  ┌─────────────┬─────────────┐         │
│  │  MỆNH CHỦ   │  THÂN CHỦ   │         │
│  │  ★ Tham Lang │  ★ Linh Tinh│         │
│  └─────────────┴─────────────┘         │
│                                         │
│  Cung Mệnh: Dần                        │
│  Cung Thân: Thân                       │
└─────────────────────────────────────────┘
```

**CSS cần thêm:**

```css
.menh-than-chu-container {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 15px 0;
    padding: 10px;
    background: linear-gradient(135deg, rgba(196, 30, 58, 0.1), rgba(212, 175, 55, 0.1));
    border-radius: 8px;
}

.menh-chu-box, .than-chu-box {
    text-align: center;
    padding: 10px 20px;
    border-radius: 6px;
    min-width: 120px;
}

.menh-chu-box {
    background: rgba(196, 30, 58, 0.15);
    border: 2px solid var(--primary-red);
}

.than-chu-box {
    background: rgba(212, 175, 55, 0.15);
    border: 2px solid var(--primary-gold);
}

.menh-chu-label, .than-chu-label {
    font-size: 12px;
    font-weight: 600;
    text-transform: uppercase;
    opacity: 0.8;
}

.menh-chu-star, .than-chu-star {
    font-size: 16px;
    font-weight: 700;
    margin-top: 5px;
}

.menh-chu-star::before, .than-chu-star::before {
    content: "★ ";
    color: var(--primary-gold);
}
```

**JavaScript cần thêm:**

```javascript
// Trong hàm displayChart(data):
function renderMenhThanChu(data) {
    const container = document.getElementById('menh-than-chu');
    if (!container) return;
    
    container.innerHTML = `
        <div class="menh-than-chu-container">
            <div class="menh-chu-box">
                <div class="menh-chu-label">Mệnh Chủ</div>
                <div class="menh-chu-star">${data.menh_chu || 'N/A'}</div>
            </div>
            <div class="than-chu-box">
                <div class="than-chu-label">Thân Chủ</div>
                <div class="than-chu-star">${data.than_chu || 'N/A'}</div>
            </div>
        </div>
    `;
}
```

### Acceptance Criteria

- [ ] Mệnh Chủ hiển thị đúng theo Cung Mệnh
- [ ] Thân Chủ hiển thị đúng theo Chi năm sinh
- [ ] UI nổi bật, dễ nhìn trong phần trung tâm lá số
- [ ] Responsive trên mobile
- [ ] Có tooltip giải thích ý nghĩa khi hover

### Priority: **HIGH**
### Story Points: **3**

---

## TASK-DEV-002: Tăng cường luận giải Cách Cục đặc biệt

### Mô tả
Bổ sung logic nhận diện và luận giải chi tiết các **Cách Cục đặc biệt** trong Tử Vi.

### Yêu cầu chi tiết

#### 1. Tạo file mới: `interpretation/cach_cuc.py`

```python
"""
Cách Cục Đặc Biệt trong Tử Vi Nam Phái
Nhận diện và luận giải các cách cục quan trọng
"""

# ═══════════════════════════════════════════════════════════════════
# DANH SÁCH CÁCH CỤC ĐẶC BIỆT
# ═══════════════════════════════════════════════════════════════════

CACH_CUC_LIST = {
    # ═══════════════════════════════════════════════════════════════
    # CÁCH CỤC CÁT (TỐT)
    # ═══════════════════════════════════════════════════════════════
    
    "tu_phu_vu_tuong": {
        "name": "Tử Phủ Vũ Tướng",
        "stars": ["Tử Vi", "Thiên Phủ", "Vũ Khúc", "Thiên Tướng"],
        "condition": "any_2_same_cung",  # Ít nhất 2 sao cùng cung hoặc tam hợp
        "rank": "Đại Cát",
        "meaning": "Cách cục quý hiển, chủ quyền cao chức trọng, phú quý song toàn.",
        "detail": """
            Đây là cách cục của những người có tư chất lãnh đạo, uy quyền.
            - Tử Vi là Đế tinh, Thiên Phủ là Tài khố
            - Vũ Khúc chủ tài lộc, Thiên Tướng chủ ấn tín
            - Bốn sao này hội tụ tạo nên cách cục phú quý bậc nhất
            
            Biểu hiện:
            - Sự nghiệp hanh thông, dễ thăng tiến
            - Tài chính ổn định, có của để dành
            - Được quý nhân phù trợ
            - Có uy tín trong xã hội
        """,
        "advice": "Nên phát huy tố chất lãnh đạo, đừng kiêu ngạo."
    },
    
    "sat_pha_liem_tham": {
        "name": "Sát Phá Liêm Tham",
        "stars": ["Thất Sát", "Phá Quân", "Liêm Trinh", "Tham Lang"],
        "condition": "any_2_same_cung",
        "rank": "Đại Cát (nếu đắc địa)",
        "meaning": "Cách cục của người có chí lớn, dám nghĩ dám làm, thành công lớn sau gian nan.",
        "detail": """
            Đây là cách cục mạnh mẽ, quyết đoán:
            - Thất Sát: Sát tinh, chủ quyết đoán
            - Phá Quân: Hao tinh, chủ thay đổi
            - Liêm Trinh: Quan tinh, chủ pháp luật
            - Tham Lang: Đào hoa, chủ ham muốn
            
            Biểu hiện:
            - Cuộc đời nhiều biến động
            - Thành công sau nhiều thử thách
            - Có tài kinh doanh, đầu tư
            - Dám mạo hiểm, dám chấp nhận rủi ro
        """,
        "advice": "Cần kiên nhẫn, tránh nóng vội. Thành công đến muộn nhưng bền vững."
    },
    
    "nhat_nguyet_tinh_minh": {
        "name": "Nhật Nguyệt Tịnh Minh",
        "stars": ["Thái Dương", "Thái Âm"],
        "condition": "both_mieu_vuong",  # Cả hai đều Miếu hoặc Vượng
        "rank": "Đại Cát",
        "meaning": "Cách cục sáng sủa, văn võ song toàn, đời người thuận lợi.",
        "detail": """
            Thái Dương và Thái Âm đều ở vị trí tốt:
            - Thái Dương Miếu/Vượng: Sáng sủa, quý nhân nhiều
            - Thái Âm Miếu/Vượng: Tài lộc, phúc đức
            
            Điều kiện:
            - Thái Dương tốt ở: Mão, Thìn, Tỵ, Ngọ
            - Thái Âm tốt ở: Dậu, Tuất, Hợi, Tý
            
            Biểu hiện:
            - Đời người sáng sủa, ít gian nan
            - Có cả tài và đức
            - Được nhiều người kính trọng
            - Gia đình hạnh phúc
        """,
        "advice": "Phát huy điểm mạnh, giúp đỡ người khác."
    },
    
    "song_loc": {
        "name": "Song Lộc",
        "stars": ["Lộc Tồn", "Hóa Lộc"],
        "condition": "same_cung",  # Cùng cung
        "rank": "Đại Cát",
        "meaning": "Hai Lộc hội tụ, tài lộc dồi dào, suốt đời không thiếu tiền.",
        "detail": """
            Lộc Tồn và Hóa Lộc cùng cung:
            - Lộc Tồn: Chính Lộc, tài sản ổn định
            - Hóa Lộc: Hóa tinh, cơ hội kiếm tiền
            
            Biểu hiện:
            - Tài chính dồi dào
            - Nhiều nguồn thu nhập
            - Đầu tư có lời
            - Không lo về tiền bạc
        """,
        "advice": "Biết chia sẻ, làm từ thiện để tích đức."
    },
    
    "loc_ma_giao_tri": {
        "name": "Lộc Mã Giao Trì",
        "stars": ["Lộc Tồn", "Thiên Mã"],
        "condition": "same_cung_or_opposite",  # Cùng cung hoặc đối xung
        "rank": "Cát",
        "meaning": "Lộc và Mã gặp nhau, tài lộc đến từ xa, kinh doanh xuất nhập khẩu tốt.",
        "detail": """
            Lộc Tồn gặp Thiên Mã:
            - Lộc Tồn: Tài lộc
            - Thiên Mã: Di chuyển, đi xa
            
            Biểu hiện:
            - Kiếm tiền từ xa
            - Kinh doanh liên quan đến vận chuyển
            - Xuất nhập khẩu có lời
            - Hay đi công tác xa
        """,
        "advice": "Nên tìm cơ hội ở xa hoặc làm việc liên quan đến di chuyển."
    },
    
    "ta_huu_giap_menh": {
        "name": "Tả Hữu Giáp Mệnh",
        "stars": ["Tả Phù", "Hữu Bật"],
        "condition": "flank_menh",  # Hai bên Cung Mệnh
        "rank": "Cát",
        "meaning": "Tả Phù Hữu Bật kẹp Mệnh, có nhiều quý nhân phò tá.",
        "detail": """
            Tả Phù và Hữu Bật ở hai bên Cung Mệnh:
            - Được nhiều người giúp đỡ
            - Có cấp dưới trung thành
            - Công việc thuận lợi
            
            Biểu hiện:
            - Nhiều bạn bè tốt
            - Cấp dưới tận tâm
            - Được sếp tin tưởng
            - Ít phải tự mình làm hết
        """,
        "advice": "Biết trọng dụng người khác, đừng tự mình ôm hết việc."
    },
    
    "xuong_khuc_giap_menh": {
        "name": "Xương Khúc Giáp Mệnh",
        "stars": ["Văn Xương", "Văn Khúc"],
        "condition": "flank_menh",
        "rank": "Cát",
        "meaning": "Văn Xương Văn Khúc kẹp Mệnh, thông minh tài hoa, học hành giỏi.",
        "detail": """
            Hai sao văn tinh kẹp Mệnh:
            - Văn Xương: Học vấn, văn chương
            - Văn Khúc: Tài năng, nghệ thuật
            
            Biểu hiện:
            - Thông minh, học giỏi
            - Có tài văn chương
            - Nghệ thuật, sáng tạo
            - Dễ đỗ đạt, thăng tiến
        """,
        "advice": "Phát huy trí tuệ, theo đuổi con đường học vấn."
    },
    
    "khoi_viet_giap_menh": {
        "name": "Khôi Việt Giáp Mệnh",
        "stars": ["Thiên Khôi", "Thiên Việt"],
        "condition": "flank_menh",
        "rank": "Cát",
        "meaning": "Quý nhân lưỡng bên, đời đi đến đâu cũng gặp may, có người giúp.",
        "detail": """
            Thiên Khôi và Thiên Việt kẹp Mệnh:
            - Thiên Khôi: Quý nhân nam
            - Thiên Việt: Quý nhân nữ
            
            Biểu hiện:
            - Gặp quý nhân ở mọi nơi
            - Khi khó khăn có người giúp
            - Thi cử, phỏng vấn dễ đậu
            - Cuộc sống thuận lợi
        """,
        "advice": "Khi thành công nhớ giúp lại người khác."
    },
    
    # ═══════════════════════════════════════════════════════════════
    # CÁCH CỤC HUNG (XẤU)
    # ═══════════════════════════════════════════════════════════════
    
    "kinh_da_giap_menh": {
        "name": "Kình Đà Giáp Mệnh",
        "stars": ["Kình Dương", "Đà La"],
        "condition": "flank_menh",
        "rank": "Hung",
        "meaning": "Hung tinh kẹp Mệnh, đời nhiều gian nan, hay gặp tiểu nhân.",
        "detail": """
            Kình Dương và Đà La kẹp Mệnh:
            - Kình Dương: Tranh đấu, xung đột
            - Đà La: Cản trở, trì hoãn
            
            Biểu hiện:
            - Cuộc sống nhiều trắc trở
            - Hay gặp tiểu nhân
            - Công việc bị cản trở
            - Dễ xảy ra xung đột
        """,
        "advice": "Cần nhẫn nhịn, tránh đối đầu trực tiếp. Tìm cách hóa giải."
    },
    
    "hoa_linh_giap_menh": {
        "name": "Hỏa Linh Giáp Mệnh",
        "stars": ["Hỏa Tinh", "Linh Tinh"],
        "condition": "flank_menh",
        "rank": "Hung",
        "meaning": "Hai sao nóng nảy kẹp Mệnh, tính cách dễ nổi nóng, hay gặp tai nạn.",
        "detail": """
            Hỏa Tinh và Linh Tinh kẹp Mệnh:
            - Hỏa Tinh: Nóng nảy, bùng nổ
            - Linh Tinh: Thất thường, hay thay đổi
            
            Biểu hiện:
            - Tính tình nóng nảy
            - Dễ gây xung đột
            - Hay gặp tai nạn nhỏ
            - Công việc không ổn định
        """,
        "advice": "Học cách kiềm chế cảm xúc, tập thiền định."
    },
    
    "khong_kiep_giap_menh": {
        "name": "Không Kiếp Giáp Mệnh",
        "stars": ["Địa Không", "Địa Kiếp"],
        "condition": "flank_menh",
        "rank": "Hung",
        "meaning": "Hai sao hao tán kẹp Mệnh, tài chính hay thất thoát, cuộc sống nhiều biến động.",
        "detail": """
            Địa Không và Địa Kiếp kẹp Mệnh:
            - Địa Không: Trống rỗng, mất mát
            - Địa Kiếp: Cướp đoạt, tai họa
            
            Biểu hiện:
            - Tài chính thất thường
            - Hay mất tiền bất ngờ
            - Cuộc sống nhiều biến động
            - Có thể hợp với nghệ thuật, tôn giáo
        """,
        "advice": "Đừng đầu tư mạo hiểm, tìm công việc ổn định hoặc theo đuổi nghệ thuật, tâm linh."
    },
    
    "menh_vo_chinh_dieu": {
        "name": "Mệnh Vô Chính Diệu",
        "stars": [],
        "condition": "no_chinh_tinh_in_menh",  # Không có Chính Tinh trong Cung Mệnh
        "rank": "Trung tính",
        "meaning": "Cung Mệnh không có Chính Tinh, phải xem cung đối diện và tam hợp.",
        "detail": """
            Cung Mệnh không có Chính Tinh nào tọa thủ:
            - Phải nhìn cung đối diện (Thiên Di)
            - Xem cung Tam Hợp chiếu
            - Phụ tinh đóng vai trò quan trọng hơn
            
            Biểu hiện:
            - Tính cách không rõ ràng
            - Dễ bị ảnh hưởng bởi hoàn cảnh
            - Linh hoạt, dễ thích ứng
        """,
        "advice": "Chú ý đến phụ tinh và cung đối diện để hiểu rõ hơn về bản thân."
    },
}

# ═══════════════════════════════════════════════════════════════════
# HÀM NHẬN DIỆN CÁCH CỤC
# ═══════════════════════════════════════════════════════════════════

def detect_cach_cuc(chart_data: dict) -> list:
    """
    Nhận diện các cách cục đặc biệt trong lá số
    
    Args:
        chart_data: Dữ liệu lá số từ chart_builder
        
    Returns:
        list các cách cục được phát hiện
    """
    detected = []
    positions = chart_data.get('positions', {})
    menh_position = chart_data.get('menh_position', 0)
    all_stars = chart_data.get('all_stars', {})
    
    # Lấy danh sách sao trong Cung Mệnh
    menh_stars = get_stars_in_palace(positions, menh_position)
    
    # Lấy danh sách sao ở hai bên Cung Mệnh
    left_position = (menh_position - 1 + 12) % 12
    right_position = (menh_position + 1) % 12
    left_stars = get_stars_in_palace(positions, left_position)
    right_stars = get_stars_in_palace(positions, right_position)
    
    # Kiểm tra từng cách cục
    for cach_cuc_id, cach_cuc in CACH_CUC_LIST.items():
        if check_cach_cuc_condition(cach_cuc, chart_data, menh_stars, 
                                     left_stars, right_stars, positions):
            detected.append({
                'id': cach_cuc_id,
                **cach_cuc
            })
    
    return detected


def get_stars_in_palace(positions: dict, palace_index: int) -> list:
    """Lấy danh sách sao trong một cung"""
    palace = positions.get(palace_index, {})
    stars = palace.get('stars', [])
    return [s['name'] if isinstance(s, dict) else s for s in stars]


def check_cach_cuc_condition(cach_cuc: dict, chart_data: dict,
                              menh_stars: list, left_stars: list, 
                              right_stars: list, positions: dict) -> bool:
    """Kiểm tra điều kiện của một cách cục"""
    condition = cach_cuc.get('condition', '')
    stars = cach_cuc.get('stars', [])
    
    if condition == 'flank_menh':
        # Kiểm tra hai sao có kẹp Mệnh không
        if len(stars) == 2:
            return (stars[0] in left_stars and stars[1] in right_stars) or \
                   (stars[1] in left_stars and stars[0] in right_stars)
    
    elif condition == 'same_cung':
        # Kiểm tra các sao có cùng cung không
        for i in range(12):
            palace_stars = get_stars_in_palace(positions, i)
            if all(star in palace_stars for star in stars):
                return True
    
    elif condition == 'any_2_same_cung':
        # Kiểm tra ít nhất 2 sao cùng cung
        for i in range(12):
            palace_stars = get_stars_in_palace(positions, i)
            count = sum(1 for star in stars if star in palace_stars)
            if count >= 2:
                return True
    
    elif condition == 'no_chinh_tinh_in_menh':
        # Kiểm tra Cung Mệnh không có Chính Tinh
        chinh_tinh = ['Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 
                      'Thiên Đồng', 'Liêm Trinh', 'Thiên Phủ', 'Thái Âm',
                      'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương',
                      'Thất Sát', 'Phá Quân']
        return not any(star in menh_stars for star in chinh_tinh)
    
    elif condition == 'both_mieu_vuong':
        # Kiểm tra cả hai sao đều Miếu hoặc Vượng
        # Cần logic phức tạp hơn - bỏ qua tạm
        return False
    
    return False


def generate_cach_cuc_interpretation(detected_cach_cuc: list) -> str:
    """
    Tạo luận giải từ các cách cục được phát hiện
    
    Returns:
        str: Văn bản luận giải
    """
    if not detected_cach_cuc:
        return "Lá số không có cách cục đặc biệt nổi bật."
    
    lines = ["## 🌟 CÁCH CỤC ĐẶC BIỆT\n"]
    
    # Phân loại cách cục
    cat_cuc = [c for c in detected_cach_cuc if 'Cát' in c.get('rank', '')]
    hung_cuc = [c for c in detected_cach_cuc if 'Hung' in c.get('rank', '')]
    
    if cat_cuc:
        lines.append("### ✨ Cách Cục Cát (Tốt)\n")
        for cuc in cat_cuc:
            lines.append(f"**{cuc['name']}** ({cuc['rank']})\n")
            lines.append(f"_{cuc['meaning']}_\n")
            lines.append(f"\n{cuc['detail'].strip()}\n")
            lines.append(f"\n💡 **Lời khuyên:** {cuc['advice']}\n")
            lines.append("\n---\n")
    
    if hung_cuc:
        lines.append("### ⚠️ Cách Cục Cần Lưu Ý\n")
        for cuc in hung_cuc:
            lines.append(f"**{cuc['name']}** ({cuc['rank']})\n")
            lines.append(f"_{cuc['meaning']}_\n")
            lines.append(f"\n{cuc['detail'].strip()}\n")
            lines.append(f"\n💡 **Cách hóa giải:** {cuc['advice']}\n")
            lines.append("\n---\n")
    
    return "\n".join(lines)
```

#### 2. Cập nhật `interpretation/__init__.py`

```python
from .cach_cuc import detect_cach_cuc, generate_cach_cuc_interpretation, CACH_CUC_LIST
```

#### 3. Cập nhật `chart/chart_builder.py`

Thêm vào return của `generate_birth_chart()`:

```python
from interpretation import detect_cach_cuc

# Trong hàm generate_birth_chart, thêm:
cach_cuc = detect_cach_cuc(chart_data)

return {
    # ... existing fields ...
    'cach_cuc': cach_cuc,
}
```

#### 4. Cập nhật Frontend

Thêm section hiển thị Cách Cục trong panel luận giải:

```html
<div class="cach-cuc-section" id="cach-cuc-panel">
    <h3>🌟 Cách Cục Đặc Biệt</h3>
    <div id="cach-cuc-content"></div>
</div>
```

### Danh sách Cách Cục cần implement

| # | Cách Cục | Loại | Priority |
|---|----------|------|----------|
| 1 | Tử Phủ Vũ Tướng | Cát | HIGH |
| 2 | Sát Phá Liêm Tham | Cát | HIGH |
| 3 | Nhật Nguyệt Tịnh Minh | Cát | HIGH |
| 4 | Song Lộc | Cát | HIGH |
| 5 | Lộc Mã Giao Trì | Cát | MEDIUM |
| 6 | Tả Hữu Giáp Mệnh | Cát | MEDIUM |
| 7 | Xương Khúc Giáp Mệnh | Cát | MEDIUM |
| 8 | Khôi Việt Giáp Mệnh | Cát | MEDIUM |
| 9 | Kình Đà Giáp Mệnh | Hung | HIGH |
| 10 | Hỏa Linh Giáp Mệnh | Hung | MEDIUM |
| 11 | Không Kiếp Giáp Mệnh | Hung | MEDIUM |
| 12 | Mệnh Vô Chính Diệu | Trung tính | LOW |

### Acceptance Criteria

- [ ] Nhận diện đúng >= 10 cách cục
- [ ] Luận giải chi tiết cho từng cách cục
- [ ] Hiển thị cách cục trong panel luận giải
- [ ] Phân loại rõ Cát/Hung
- [ ] Có lời khuyên cho mỗi cách cục

### Priority: **HIGH**
### Story Points: **8**

---

# 🧪 TASK CHO QC (Quality Control)

## TASK-QC-001: Test Mệnh Chủ và Thân Chủ

### Test Cases

| TC ID | Mô tả | Input | Expected Output |
|-------|-------|-------|-----------------|
| TC-MC-001 | Mệnh ở Tý | Cung Mệnh = Tý | Mệnh Chủ = Tham Lang |
| TC-MC-002 | Mệnh ở Sửu | Cung Mệnh = Sửu | Mệnh Chủ = Cự Môn |
| TC-MC-003 | Mệnh ở Dần | Cung Mệnh = Dần | Mệnh Chủ = Lộc Tồn |
| TC-MC-004 | Mệnh ở Mão | Cung Mệnh = Mão | Mệnh Chủ = Văn Khúc |
| TC-MC-005 | Mệnh ở Thìn | Cung Mệnh = Thìn | Mệnh Chủ = Liêm Trinh |
| TC-MC-006 | Mệnh ở Tỵ | Cung Mệnh = Tỵ | Mệnh Chủ = Vũ Khúc |
| TC-MC-007 | Mệnh ở Ngọ | Cung Mệnh = Ngọ | Mệnh Chủ = Phá Quân |
| TC-MC-008 | Mệnh ở Mùi | Cung Mệnh = Mùi | Mệnh Chủ = Vũ Khúc |
| TC-MC-009 | Mệnh ở Thân | Cung Mệnh = Thân | Mệnh Chủ = Liêm Trinh |
| TC-MC-010 | Mệnh ở Dậu | Cung Mệnh = Dậu | Mệnh Chủ = Văn Khúc |
| TC-MC-011 | Mệnh ở Tuất | Cung Mệnh = Tuất | Mệnh Chủ = Lộc Tồn |
| TC-MC-012 | Mệnh ở Hợi | Cung Mệnh = Hợi | Mệnh Chủ = Cự Môn |

| TC ID | Mô tả | Input | Expected Output |
|-------|-------|-------|-----------------|
| TC-TC-001 | Năm Tý | Chi năm = Tý | Thân Chủ = Linh Tinh |
| TC-TC-002 | Năm Sửu | Chi năm = Sửu | Thân Chủ = Thiên Tướng |
| TC-TC-003 | Năm Dần | Chi năm = Dần | Thân Chủ = Thiên Lương |
| TC-TC-004 | Năm Mão | Chi năm = Mão | Thân Chủ = Thiên Đồng |
| TC-TC-005 | Năm Thìn | Chi năm = Thìn | Thân Chủ = Văn Xương |
| TC-TC-006 | Năm Tỵ | Chi năm = Tỵ | Thân Chủ = Thiên Cơ |
| TC-TC-007 | Năm Ngọ | Chi năm = Ngọ | Thân Chủ = Hỏa Tinh |
| TC-TC-008 | Năm Mùi | Chi năm = Mùi | Thân Chủ = Thiên Tướng |
| TC-TC-009 | Năm Thân | Chi năm = Thân | Thân Chủ = Thiên Lương |
| TC-TC-010 | Năm Dậu | Chi năm = Dậu | Thân Chủ = Thiên Đồng |
| TC-TC-011 | Năm Tuất | Chi năm = Tuất | Thân Chủ = Văn Xương |
| TC-TC-012 | Năm Hợi | Chi năm = Hợi | Thân Chủ = Thiên Cơ |

### UI Test Cases

| TC ID | Mô tả | Expected |
|-------|-------|----------|
| TC-UI-001 | Hiển thị Mệnh Chủ | Có box riêng, nổi bật |
| TC-UI-002 | Hiển thị Thân Chủ | Có box riêng, nổi bật |
| TC-UI-003 | Vị trí hiển thị | Trong phần trung tâm lá số |
| TC-UI-004 | Responsive Mobile | Hiển thị đúng trên 320px |
| TC-UI-005 | Hover tooltip | Có giải thích khi hover |

### Priority: **HIGH**
### Deadline: 20/12/2025

---

## TASK-QC-002: Test Cách Cục Đặc Biệt

### Test Cases - Cách Cục Cát

| TC ID | Cách Cục | Input (Ví dụ) | Expected |
|-------|----------|---------------|----------|
| TC-CC-001 | Tử Phủ Vũ Tướng | Tử Vi + Thiên Phủ cùng cung | Phát hiện cách cục |
| TC-CC-002 | Song Lộc | Lộc Tồn + Hóa Lộc cùng cung | Phát hiện cách cục |
| TC-CC-003 | Tả Hữu Giáp Mệnh | Tả Phù trái Mệnh, Hữu Bật phải Mệnh | Phát hiện cách cục |
| TC-CC-004 | Xương Khúc Giáp Mệnh | Văn Xương trái, Văn Khúc phải Mệnh | Phát hiện cách cục |
| TC-CC-005 | Khôi Việt Giáp Mệnh | Thiên Khôi + Thiên Việt kẹp Mệnh | Phát hiện cách cục |

### Test Cases - Cách Cục Hung

| TC ID | Cách Cục | Input (Ví dụ) | Expected |
|-------|----------|---------------|----------|
| TC-CC-006 | Kình Đà Giáp Mệnh | Kình Dương + Đà La kẹp Mệnh | Phát hiện cách cục |
| TC-CC-007 | Hỏa Linh Giáp Mệnh | Hỏa Tinh + Linh Tinh kẹp Mệnh | Phát hiện cách cục |
| TC-CC-008 | Không Kiếp Giáp Mệnh | Địa Không + Địa Kiếp kẹp Mệnh | Phát hiện cách cục |

### Test Cases - Luận Giải

| TC ID | Mô tả | Expected |
|-------|-------|----------|
| TC-LG-001 | Luận giải Cát | Có nội dung tích cực |
| TC-LG-002 | Luận giải Hung | Có cảnh báo + lời khuyên |
| TC-LG-003 | Không có cách cục | Thông báo "Không có cách cục đặc biệt" |
| TC-LG-004 | Nhiều cách cục | Liệt kê đầy đủ, phân loại Cát/Hung |

### Test Script Template

```python
# test_cach_cuc.py
import pytest
from chart import generate_birth_chart
from interpretation import detect_cach_cuc

class TestCachCuc:
    def test_ta_huu_giap_menh(self):
        """Test Tả Hữu Giáp Mệnh"""
        # Tìm một ngày sinh có Tả Hữu giáp Mệnh
        chart = generate_birth_chart(15, 6, 1990, 6, 'nam')
        cach_cuc = detect_cach_cuc(chart)
        
        # Kiểm tra có phát hiện cách cục không
        cach_cuc_names = [c['name'] for c in cach_cuc]
        # Assert based on actual chart
        
    def test_song_loc(self):
        """Test Song Lộc"""
        # Test case cho Song Lộc
        pass
        
    def test_menh_vo_chinh_dieu(self):
        """Test Mệnh Vô Chính Diệu"""
        pass
```

### Priority: **HIGH**
### Deadline: 22/12/2025

---

## TASK-QC-003: Regression Test

### Checklist

- [ ] Lá số vẫn tính đúng sau khi thêm tính năng
- [ ] Số lượng sao vẫn >= 114
- [ ] Tứ Hóa vẫn đúng theo Nam Phái
- [ ] Tuần Triệt vẫn đúng
- [ ] Độ sáng sao vẫn đúng
- [ ] UI không bị vỡ layout

### Priority: **MEDIUM**
### Deadline: 23/12/2025

---

# 📊 TỔNG KẾT SPRINT

## Story Points

| Task | Assignee | Points | Priority |
|------|----------|--------|----------|
| DEV-001: Mệnh Chủ/Thân Chủ | Developer | 3 | HIGH |
| DEV-002: Cách Cục | Developer | 8 | HIGH |
| QC-001: Test Mệnh/Thân Chủ | QC | 3 | HIGH |
| QC-002: Test Cách Cục | QC | 5 | HIGH |
| QC-003: Regression | QC | 2 | MEDIUM |
| **TOTAL** | | **21** | |

## Timeline

```
16/12 ─────────────────────────────────────────> 23/12

[DEV-001: Mệnh Chủ/Thân Chủ ████████░░░░░░░░] 16-18/12
                                    ↓
                          [QC-001 ████░░░░░░] 18-20/12

[DEV-002: Cách Cục ████████████████████░░░░░░] 16-21/12
                                          ↓
                                [QC-002 ████████] 21-22/12

                                        [QC-003 Regression ████] 22-23/12
```

## Definition of Done

- [ ] Code đã review
- [ ] Unit test passed
- [ ] QC test passed
- [ ] UI đẹp, responsive
- [ ] Documentation updated

---

*Task Assignment Document - Sprint 01 - Version 1.0*

