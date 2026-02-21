"""
Advanced Rules for Reverse Lookup (Finder Level 2)
Defining criteria with weighted scoring and scope.
"""

FINDER_RULES = [
    # --- CAREER ---
    {
        "criteria_id": "CAREER_IT",
        "name": "Công nghệ thông tin (IT)",
        "scope": ["Mệnh", "Quan Lộc", "Thân"],
        "required_one_of": [], # Optional: Must have at least one to be considered
        "positive_stars": ["Thiên Cơ", "Thiên Đồng", "Thái Âm", "Tử Vi", "Phá Quân"], # Cơ Nguyệt Đồng Lương or Sát Phá Tham (Kỹ thuật)
        "positive_stars_bonus": ["Hỏa Tinh", "Linh Tinh", "Địa Không", "Địa Kiếp", "Kinh Dương"], # Kỹ thuật, điện tử
        "negative_stars": [],
        "weight": 2.0
    },
    {
        "criteria_id": "CAREER_TEACHER",
        "name": "Giáo viên/Giảng dạy",
        "scope": ["Mệnh", "Quan Lộc", "Thân"], 
        "positive_stars": ["Thiên Lương", "Cự Môn", "Văn Xương", "Văn Khúc", "Hóa Khoa"],
        "positive_stars_bonus": ["Thái Dương", "Thiên Đồng"],
        "weight": 2.0
    },

    # --- PERSONALITY ---
    {
        "criteria_id": "TRAIT_HOT_TEMPER",
        "name": "Nóng nảy, vội vã",
        "scope": ["Mệnh", "Thân"], # Chỉ xét Mệnh Thân
        "positive_stars": ["Hỏa Tinh", "Linh Tinh", "Kinh Dương", "Đà La", "Thất Sát", "Phá Quân"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_SENTIMENTAL",
        "name": "Đa cảm, yếu đuối",
        "scope": ["Mệnh", "Thân"],
        "positive_stars": ["Thiên Đồng", "Thái Âm", "Thiên Lương", "Hóa Kỵ"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_GENTLE",
        "name": "Ôn hòa, điềm đạm",
        "scope": ["Mệnh", "Thân"],
        "positive_stars": ["Thiên Lương", "Thiên Đồng", "Thái Âm", "Thiên Phủ", "Thiên Tướng"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_SUSPICIOUS",
        "name": "Đa nghi, hay soi xét",
        "scope": ["Mệnh", "Thân"],
        "positive_stars": ["Cự Môn", "Phúc Bình", "Thiên Riêu"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_OPTIMISTIC",
        "name": "Vui vẻ, lạc quan",
        "scope": ["Mệnh", "Thân"],
        "positive_stars": ["Thiên Đồng", "Hóa Lộc", "Hỷ Thần", "Thiên Hỹ"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_GENEROUS",
        "name": "Hào phóng, rộng lượng",
        "scope": ["Mệnh", "Thân", "Tài Bạch"],
        "positive_stars": ["Thiên Phủ", "Hóa Lộc", "Đại Hao", "Thái Dương", "Thiên Đồng"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_LONELY_RELIGIOUS",
        "name": "Thích cô độc/Tôn giáo",
        "scope": ["Mệnh", "Thân", "Phúc Đức"],
        "positive_stars": ["Cô Thần", "Quả Tú", "Hoa Cái", "Thiên Không", "Thiên Lương"],
        "positive_stars_bonus": ["Thiên Cơ"], # Hãm
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_FLIRTY",
        "name": "Đào hoa, đa tình",
        "scope": ["Mệnh", "Thân", "Nô Bộc"],
        "positive_stars": ["Tham Lang", "Đào Hoa", "Hồng Loan", "Liêm Trinh", "Thái Âm"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_STUBBORN",
        "name": "Bướng bỉnh, bảo thủ",
        "scope": ["Mệnh", "Thân"],
        "positive_stars": ["Vũ Khúc", "Thất Sát", "Đà La", "Cô Thần"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_SMART",
        "name": "Thông minh, sắc sảo",
        # Updated Logic: "Displayed" gets absolute points. Inner/Hidden gets partial.
        "scope": {
            "Mệnh": 1.0,       # Bản chất bộc lộ (Tuyệt đối)
            "Quan Lộc": 1.0,   # Thể hiện qua công việc (Tuyệt đối)
            "Thiên Di": 0.9,   # Thể hiện ra ngoài xã hội
            "Tài Bạch": 0.7,   # Tư duy tài chính (Ẩn hơn hoặc chỉ focus tiền bạc)
            "Tật Ách": 0.5     # Tư duy nội tâm (Ít bộc lộ nhất)
        },
        "positive_stars": ["Thiên Cơ", "Thái Dương", "Thiên Khôi", "Thiên Việt", "Văn Xương", "Văn Khúc", "Hóa Khoa"],
        "weight": 1.5
    },
    {
        "criteria_id": "TRAIT_CAREFUL",
        "name": "Cẩn thận, tỉ mỉ",
        "scope": ["Mệnh", "Quan Lộc"],
        "positive_stars": ["Thiên Lương", "Lộc Tồn", "Thiên Cơ"],
        "weight": 1.5
    },

    # --- APPEARANCE ---
    {
        "criteria_id": "APPEARANCE_SKINNY",
        "name": "Gầy, ốm",
        "scope": ["Mệnh", "Tật Ách"], # Mệnh và Tật
        "positive_stars": ["Thất Sát", "Cự Môn", "Thiên Cơ", "Đà La", "Hóa Kỵ"],
        "weight": 1.0
    },
    {
        "criteria_id": "APPEARANCE_TALL",
        "name": "Cao lớn",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thiên Tướng", "Phá Quân", "Thiên Lương", "Thiên Khôi", "Tham Lang"],
        "negative_stars": ["Thiên Cơ", "Vũ Khúc"],
        "weight": 1.0
    },
    {
        "criteria_id": "APPEARANCE_SHORT",
        "name": "Thấp bé",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thiên Cơ", "Vũ Khúc", "Thái Âm"],
        "weight": 1.0
    },
    {
        "criteria_id": "APPEARANCE_FAT",
        "name": "Mập, đầy đặn",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thiên Phủ", "Thái Âm", "Thiên Đồng", "Tham Lang"],
        "weight": 1.0
    },
    {
        "criteria_id": "APPEARANCE_WHITE_SKIN",
        "name": "Da trắng",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thái Âm", "Thiên Phủ", "Thiên Tướng"],
        "weight": 1.0
    },
     {
        "criteria_id": "APPEARANCE_DARK_SKIN",
        "name": "Da ngăm đen",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thất Sát", "Tham Lang", "Phá Quân"],
        "weight": 1.0
    },
     {
        "criteria_id": "APPEARANCE_SQUARE_FACE",
        "name": "Mặt vuông chữ điền",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thất Sát", "Thiên Phủ", "Vũ Khúc"],
        "weight": 1.0
    },
    {
        "criteria_id": "APPEARANCE_ROUND_FACE",
        "name": "Mặt tròn",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thiên Đồng", "Thái Âm", "Tham Lang"],
        "weight": 1.0
    },
    {
        "criteria_id": "APPEARANCE_BAD_EYES",
        "name": "Mắt cận thị/kém",
        "scope": ["Mệnh", "Tật Ách"],
        "positive_stars": ["Thái Dương", "Đà La", "Hóa Kỵ"], # Thai Duong ham
        "weight": 1.0
    },
    
    # --- MARRIAGE ---
    {
        "criteria_id": "MARRIAGE_LATE",
        "name": "Kết hôn muộn (> 30 tuổi)",
        "scope": ["Phu Thê", "Mệnh"],
        "positive_stars": ["Cô Thần", "Quả Tú", "Vũ Khúc", "Triệt", "Tuần"],
        "weight": 1.5
    },
    {
        "criteria_id": "MARRIAGE_CONFLICT",
        "name": "Vợ chồng hay khắc khẩu/bất hòa",
        "scope": ["Phu Thê"],
        "positive_stars": ["Cự Môn", "Hóa Kỵ", "Phúc Bình", "Kinh Dương", "Đà La"],
        "weight": 1.5
    },

    # --- EVENTS (Examples for future expansion, logic handled in code) ---
    # Event logic is often specific (Checking limit years), but we can define involved stars here
    {
        "criteria_id": "EVENT_MARRIAGE",
        "name": "Kết hôn",
        "related_stars": ["Hồng Loan", "Đào Hoa", "Thiên Hỹ", "Hỷ Thần", "Thanh Long"],
        "related_palaces": ["Phu Thê", "Nô Bộc"],
        "weight": 5.0 # Very high importance
    }
]

def get_rule_by_id(criteria_id):
    return next((r for r in FINDER_RULES if r['criteria_id'] == criteria_id), None)

def get_rule_by_name(name):
    # Fuzzy match or direct mapping could occur here
    # For now assume mostly direct mapping from dropdown values
    return next((r for r in FINDER_RULES if r['name'] == name), None)
