# duong_ba_dieu_data.py
# Dữ liệu Thơ Phú và Khẩu Quyết Tử Vi
# Được số hóa từ: docs/tu_vi/research/research_book_kinh_dien_tho_phu.md

THO_PHU_DATA = [
    # --- 1. HÌNH THÁI VÀ TÍNH CÁCH ---
    {
        "id": "TP_HT_001",
        "category": "HinhThai_TinhCach",
        "triggers": {"main_stars": ["Tu Vi"]},
        "content_vi": "Tử Vi thì tầm tước da dâu\nCon người Chính trực chẳng màu oan sai",
        "meaning": "Ngoại hình: Cao vừa phải, da ngăm (da dâu). Tính cách: Chính trực, ngay thẳng, lãnh đạo.",
        "tags": ["Tu Vi", "Ngoai Hinh", "Tinh Cach"]
    },
    {
        "id": "TP_HT_002",
        "category": "HinhThai_TinhCach",
        "triggers": {"main_stars": ["Thien Co"]},
        "content_vi": "Thiên Cơ thì chẳng vắn chẳng dài\nLòng lành Tay Khéo hay hài đúc nghề",
        "meaning": "Ngoại hình: Vừa vặn. Tính cách: Lương thiện, khéo tay, giỏi kỹ thuật/nghề thủ công.",
        "tags": ["Thien Co", "Ngoai Hinh", "Tai Nang"]
    },
    {
        "id": "TP_HT_003",
        "category": "HinhThai_TinhCach",
        "triggers": {"main_stars": ["Tu Vi", "Thien Phu"]},
        "content_vi": "Tử Vi phúc hậu dung hình\nThiên Phủ tiết hạnh thông minh ôn hòa\nHai sao đồng gặp một tòa\nThiên tư ôn thuận thật là tốt thay",
        "meaning": "Tử Vi phúc hậu, Thiên Phủ thông minh ôn hòa. Đồng cung thì tính cách rất tốt, ôn thuận.",
        "tags": ["Tu Vi", "Thien Phu", "Dong Cung"]
    },
    {
        "id": "TP_HT_004",
        "category": "HinhThai_TinhCach",
        "triggers": {"aux_stars": ["Ta Phu", "Huu Bat"], "palace": "Menh"},
        "content_vi": "Tả Hữu đóng ở Mệnh cung\nĐoán rằng số ấy Ly Tông cửa nhà\nTả Hữu cũng hợp Mệnh ta\nLà người cốt cách hoan hòa tốt thay",
        "meaning": "Tả Hữu thủ Mệnh dễ ly hương lập nghiệp. Tính cách hòa nhã, tốt bụng, được giúp đỡ.",
        "tags": ["Ta Phu", "Huu Bat", "Menh"]
    },
    {
        "id": "TP_HT_005",
        "category": "HinhThai_TinhCach",
        "triggers": {"main_stars": ["Thai Duong"]},
        "content_vi": "Thái Dương diện Khuyển xà tề\nCon người tươm tất là dáng thầy gầy khô",
        "meaning": "Ngoại hình: Mặt dài (diện khuyển), gầy. Phong thái: Tươm tất, nghiêm túc như thầy giáo.",
        "tags": ["Thai Duong", "Ngoai Hinh"]
    },
     {
        "id": "TP_HT_006",
        "category": "HinhThai_TinhCach",
        "triggers": {"main_stars": ["Thien Luong"]},
        "content_vi": "Thiên Lương: Thiện ấm triều cương\nPhúc thọ song toàn",
        "meaning": "Tính cách thiện lương, nguyên tắc (triều cương). Cuộc đời có phúc và thọ.",
        "tags": ["Thien Luong", "Phuc Tho"]
    },

    # --- 2. CÁCH CỤC VÀ VỊ TRÍ ĐẶC BIỆT ---
    {
        "id": "TP_CC_001",
        "category": "CachCuc",
        "triggers": {
            "main_stars": ["Pha Quan"],
            "palace": "Quan Loc",
            "branches": ["Ty", "Ngo"],
            "avoid_stars": ["That Sat", "Kinh Duong", "Da La"] # check logic "Sát Tấu"
        },
        "content_vi": "Phá mà cư tọa thủ cửa trời\nLại vô Sát Tấu cả đời Công Khanh",
        "meaning": "Phá Quân Tý/Ngọ (Cửa trời) tại Quan Lộc, không gặp Sát tinh thì làm quan to, sự nghiệp lớn.",
        "tags": ["Pha Quan", "Quan Loc", "Cong Danh"]
    },
    {
        "id": "TP_CC_002",
        "category": "CachCuc",
        "triggers": {
            "main_stars": ["Tu Vi", "Triet"],
            "palace": "Quan Loc"
        },
        "content_vi": "Đái ấn triều hồi",
        "meaning": "Tử Vi gặp Triệt ở Quan: Mất chức hoặc về hưu sớm (trả ấn về triều).",
        "tags": ["Tu Vi", "Triet", "Quan Loc"]
    },
    {
        "id": "TP_CC_003",
        "category": "CachCuc",
        "triggers": {
            "main_stars": ["Thien Dong", "Thien Luong"],
            "branches": ["Dan", "Than"]
        },
        "content_vi": "Đồng Lương đắc cách Dần Thân\nKhi xưa bạch thủ mà nay sang giàu",
        "meaning": "Đồng Lương Dần/Thân: Khởi nghiệp tay trắng (bạch thủ) sau thành đại gia.",
        "tags": ["Thien Dong", "Thien Luong", "Giau Co"]
    },
    {
        "id": "TP_CC_004",
        "category": "CachCuc",
        "triggers": {
            "main_stars": ["Cu Mon", "Thai Duong"],
            "branches": ["Dan", "Than"]
        },
        "content_vi": "Cự Nhật Dần Thân\nQuang Phong Tam Đại",
        "meaning": "Cự Nhật Dần Thân: Ba đời vinh hiển, danh tiếng rực rỡ.",
        "tags": ["Cu Mon", "Thai Duong", "Quy Hien"]
    },
    {
        "id": "TP_CC_005",
        "category": "CachCuc",
        "triggers": {
            "palace": "Phu The",
            "lucky_stars": ["Thai Am", "Thai Duong", "Loc Ton", "Thien Ma", "Thien Dong", "Hoa Quyen", "Hoa Khoa"]
        },
        "content_vi": "Vợ về của có muôn vàn\nÂm Dương Lộc Mã Đế Đồng Quyền Khoa",
        "meaning": "Cung Phu Thê hội tụ sao tốt (Âm, Dương, Lộc, Mã, Đế, Quyền, Khoa): Vợ chồng giàu có, hôn nhân viên mãn.",
        "tags": ["Phu The", "Giau Co"]
    },
     {
        "id": "TP_CC_006",
        "category": "CachCuc",
        "triggers": {
            "aux_stars": ["Thien Khong", "Dao Hoa"]
        },
        "content_vi": "Thiên Không hội Đào Hoa Cầm Kỳ Thi Họa\nTài ba tuyệt vời, quyền biến hơn người\nĐào Hồng hợp Mệnh, cũng một đời lênh đênh",
        "meaning": "Đào Không: Tài năng nghệ thuật, cơ trí nhưng tình duyên/cuộc đời lận đận.",
        "tags": ["Thien Khong", "Dao Hoa", "Tai Nang", "Tinh Duyen"]
    },

    # --- 3. ĐIỀN TRẠCH ---
    {
        "id": "TP_DT_001",
        "category": "DienTrach",
        "triggers": {"main_stars": ["Tu Vi"], "palace": "Dien Trach"},
        "content_vi": "Tử Vi đóng ở cung Điền\nNhà này phải có trang viên thư phòng",
        "meaning": "Nhà rộng, có vườn, có phòng sách/thờ tự thanh tịnh.",
        "tags": ["Tu Vi", "Dien Trach", "Nha Cua"]
    },
    {
        "id": "TP_DT_002",
        "category": "DienTrach",
        "triggers": {"main_stars": ["Vu Khuc"], "palace": ["Tai Bach", "Dien Trach"]},
        "content_vi": "Vũ Khúc Điền Tài\nPhú gia địch quốc\nLâm lai tổ điền",
        "meaning": "Vũ Khúc Điền/Tài: Cực giàu (địch quốc), thừa kế đất đai tổ tiên.",
        "tags": ["Vu Khuc", "Dien Trach", "Tai Bach", "Giau Co"]
    },
    {
        "id": "TP_DT_003",
        "category": "DienTrach",
        "triggers": {"aux_stars": ["Loc Ton", "Thien Ma"], "palace": "Dien Trach"},
        "content_vi": "Lộc Tồn Thiên Mã đồng gia\nCó người nuôi mốt bán ba lên giàu",
        "meaning": "Lộc Mã ở Điền: Kinh doanh bất động sản, buôn bán mát tay.",
        "tags": ["Loc Ton", "Thien Ma", "Bat Dong San"]
    },
    {
        "id": "TP_DT_004",
        "category": "DienTrach",
        "triggers": {"aux_stars": ["Long Tri"], "palace": "Dien Trach"},
        "content_vi": "Long Trì ở Điền khoan phá bỏ cạnh bên",
        "meaning": "Nhà có ao/giếng hoặc gần nguồn nước. Nếu có Phá Quân cần cẩn thận khi sửa chữa.",
        "tags": ["Long Tri", "Dien Trach", "Phong Thuy"]
    },
    {
        "id": "TP_DT_005",
        "category": "DienTrach",
        "triggers": {"aux_stars": ["An Quang", "Thien Quy"], "palace": "Dien Trach"},
        "content_vi": "Điền mà có Quý Quan\nCúng thờ lễ tiết khang trang cửa nhà",
        "meaning": "Nhà chú trọng thờ cúng, bát hương lễ tiết chu đáo.",
        "tags": ["An Quang", "Thien Quy", "Tho Cung"]
    },
    {
        "id": "TP_DT_006",
        "category": "DienTrach",
        "triggers": {"main_stars": ["Thien Phu"], "palace": "Dien Trach"},
        "content_vi": "Thiên Phủ tinh thổ miễn chê\nỞ đâu phát cũ gốc đề gốc đa",
        "meaning": "Nhà ở đất cũ, có cây cổ thụ, tích luỹ tài sản bền vững.",
        "tags": ["Thien Phu", "Dien Trach"]
    },

    # --- 4. TAI ÁCH & HÓA GIẢI ---
    {
        "id": "TP_TA_001",
        "category": "TaiAch_HoaGiai",
        "triggers": {"aux_stars": ["Giai Than", "Thien Duc", "Nguyet Duc"], "palace": "Menh"},
        "content_vi": "Thiên Nguyệt Đức Giải Thần tàng\nCũng là quan phúc một làng trừ hung...",
        "meaning": "Có Giải Thần, Đức: Hóa giải hung họa, làm người đức độ, mặt mũi hồng hào.",
        "tags": ["Giai Than", "Thien Duc", "Nguyet Duc", "Hoa Giai"]
    },
    {
        "id": "TP_TA_002",
        "category": "TaiAch_HoaGiai",
        "triggers": {"aux_stars": ["Tuan", "Triet"], "palace": "Phuc Duc"},
        "content_vi": "Phúc Đức Tuần Triệt ra liền\nCon mất mả trên miền hoang sơn",
        "meaning": "Phúc gặp Tuần/Triệt: Mộ phần thất lạc hoặc con cái yểu mệnh.",
        "tags": ["Phuc Duc", "Tuan", "Triet", "Hung"]
    },
    {
        "id": "TP_TA_003",
        "category": "TaiAch_HoaGiai",
        "triggers": {"aux_stars": ["Thien Hinh", "Song Hao"]},
        "content_vi": "Hiếm hoi bởi tại Hình Hao\nĐến già mới có tay nào con thơ",
        "meaning": "Hình Hao: Hiếm muộn con cái.",
        "tags": ["Thien Hinh", "Song Hao", "Con Cai"]
    },
    {
        "id": "TP_TA_004",
        "category": "TaiAch_HoaGiai",
        "triggers": {"main_stars": ["Thai Am", "Hoa Ky"], "palace": "Tu Tuc"},
        "content_vi": "Thái Âm Hóa Kỵ đồng gia\nÂm hư huyết kém ấy là muộn con",
        "meaning": "Thái Âm Kỵ ở Tử: Khó có con do huyết khí kém (nữ) hoặc bệnh sinh lý.",
        "tags": ["Thai Am", "Hoa Ky", "Tu Tuc"]
    },
    {
        "id": "TP_TA_005",
        "category": "TaiAch_HoaGiai",
        "triggers": {"aux_stars": ["Tang Mon", "Bach Ho"], "palace": "Menh"},
        "content_vi": "Tang Hổ Mệnh cung\nSau trước gái cũng đành lỡ bước cổ",
        "meaning": "Tang Hổ thủ Mệnh: Phụ nữ duyên phận trắc trở, đau buồn.",
        "tags": ["Tang Mon", "Bach Ho", "Tinh Duyen"]
    }
]

def get_poems_by_star(star_name):
    """Lấy các bài thơ liên quan đến một sao."""
    return [p for p in THO_PHU_DATA if star_name in p["triggers"].get("main_stars", []) or star_name in p["triggers"].get("aux_stars", [])]

def get_poems_by_palace(palace_name):
    """Lấy các bài thơ liên quan đến cung."""
    return [p for p in THO_PHU_DATA if p["triggers"].get("palace") == palace_name]
