"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    CHI TIẾT SAO - STAR DETAILS                               ║
║                    Theo yêu cầu UC-03 của BA                                ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Mỗi sao có đầy đủ thông tin:                                               ║
║  - type: Loại sao (Chính Tinh / Phụ Tinh)                                   ║
║  - group: Nhóm sao                                                          ║
║  - element: Ngũ Hành                                                        ║
║  - nature: Tính chất (Cát / Hung / Trung tính)                             ║
║  - rank: Cấp bậc sao                                                        ║
║  - meaning: Ý nghĩa chi tiết (general, career, relationship, health)       ║
║  - brightness_effect: Ảnh hưởng của độ sáng                                ║
║  - keywords: Từ khóa                                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 14 CHÍNH TINH - CHI TIẾT
# ═══════════════════════════════════════════════════════════════════════════════

CHINH_TINH_DETAILS = {
    'Tử Vi': {
        'type': 'Chính Tinh',
        'group': 'Tử Phủ',
        'element': 'Thổ',
        'nature': 'Cát tinh',
        'rank': 'Đế tinh - Sao vua',
        'meaning': {
            'general': 'Tử Vi là sao đế vương, chủ quyền quý, cao sang. Người có Tử Vi thủ mệnh thường có tư cách lãnh đạo, được kính trọng, có địa vị trong xã hội.',
            'career': 'Thích hợp làm lãnh đạo, quản lý cấp cao, chính trị, công chức cao cấp. Không thích làm việc dưới quyền người khác.',
            'relationship': 'Tính cách cao ngạo, khó gần. Có xu hướng độc đoán trong quan hệ. Cần học cách lắng nghe và khiêm tốn.',
            'health': 'Thường khỏe mạnh, chú ý tim mạch và huyết áp. Dễ bị stress do áp lực công việc.'
        },
        'brightness_effect': {
            'Miếu': 'Phát huy tối đa sức mạnh đế vương, quyền quý song toàn',
            'Vượng': 'Có uy quyền, được kính trọng, địa vị cao',
            'Đắc': 'Có địa vị nhưng phải nỗ lực nhiều',
            'Bình': 'Bình thường, không nổi bật, cần phấn đấu',
            'Hãm': 'Có danh mà không có thực quyền, khó phát triển'
        },
        'keywords': ['quyền lực', 'cao quý', 'lãnh đạo', 'bảo thủ', 'uy nghiêm']
    },
    'Thiên Cơ': {
        'type': 'Chính Tinh',
        'group': 'Tử Phủ',
        'element': 'Mộc',
        'nature': 'Cát tinh',
        'rank': 'Thiện tinh - Sao mưu lược',
        'meaning': {
            'general': 'Thiên Cơ là sao trí tuệ, mưu lược. Người có Thiên Cơ thông minh, nhanh nhẹn, có nhiều ý tưởng sáng tạo.',
            'career': 'Thích hợp làm cố vấn, chiến lược gia, nghiên cứu, giáo dục, công nghệ. Giỏi phân tích và lên kế hoạch.',
            'relationship': 'Đa cảm, hay lo lắng cho người khác. Cần sự ổn định trong tình cảm.',
            'health': 'Hay lo nghĩ, dễ mất ngủ, stress. Chú ý thần kinh và tiêu hóa.'
        },
        'brightness_effect': {
            'Miếu': 'Mưu lược xuất chúng, thành công lớn trong lĩnh vực trí tuệ',
            'Vượng': 'Thông minh lanh lợi, có tài kinh doanh',
            'Đắc': 'Có trí tuệ nhưng cần cơ hội thể hiện',
            'Bình': 'Trí tuệ bình thường, cần học hỏi nhiều',
            'Hãm': 'Hay lo lắng, thiếu quyết đoán, khó thành công'
        },
        'keywords': ['thông minh', 'mưu lược', 'linh hoạt', 'lo lắng', 'sáng tạo']
    },
    'Thái Dương': {
        'type': 'Chính Tinh',
        'group': 'Nhật Nguyệt',
        'element': 'Hỏa',
        'nature': 'Cát tinh',
        'rank': 'Quang minh tinh - Sao ánh sáng',
        'meaning': {
            'general': 'Thái Dương là sao mặt trời, đại diện cho sự quang minh chính đại. Người có Thái Dương thường rộng lượng, hào phóng, hay giúp đỡ người khác.',
            'career': 'Thích hợp làm giáo viên, chính khách, nhà hoạt động xã hội. Có tài diễn thuyết, lãnh đạo.',
            'relationship': 'Tốt với mọi người, có quý nhân. Hay hy sinh cho người khác, đôi khi quá dốc lòng.',
            'health': 'Mắt và tim cần chú ý. Dễ mệt mỏi do làm việc quá sức.'
        },
        'brightness_effect': {
            'Miếu': 'Quang minh lỗi lạc, danh tiếng vang xa, được nhiều người kính trọng',
            'Vượng': 'Có danh tiếng, được quý nhân phù trợ',
            'Đắc': 'Có uy tín nhưng phải cố gắng duy trì',
            'Bình': 'Danh tiếng bình thường, không nổi bật',
            'Hãm': 'Vất vả, lao tâm, dễ bị hiểu lầm, mắt yếu'
        },
        'keywords': ['quang minh', 'hào phóng', 'hy sinh', 'danh tiếng', 'quý nhân']
    },
    'Vũ Khúc': {
        'type': 'Chính Tinh',
        'group': 'Tử Phủ',
        'element': 'Kim',
        'nature': 'Cát tinh',
        'rank': 'Tài tinh - Sao tài lộc',
        'meaning': {
            'general': 'Vũ Khúc là sao tài tinh, chủ về tiền bạc và quyết đoán. Người có Vũ Khúc thường có tài quản lý tiền bạc, kinh doanh giỏi.',
            'career': 'Thích hợp làm tài chính, ngân hàng, kinh doanh, quân đội. Quyết đoán và dám mạo hiểm.',
            'relationship': 'Cứng rắn, ít thể hiện tình cảm. Cần học cách mềm mỏng hơn trong quan hệ.',
            'health': 'Chú ý phổi và hệ hô hấp. Dễ bị căng thẳng trong công việc.'
        },
        'brightness_effect': {
            'Miếu': 'Giàu có, tài lộc dồi dào, kinh doanh phát đạt',
            'Vượng': 'Có tài năng kiếm tiền, sự nghiệp ổn định',
            'Đắc': 'Có tài chính nhưng phải vất vả',
            'Bình': 'Thu nhập bình thường, không giàu không nghèo',
            'Hãm': 'Khó kiếm tiền, dễ mất mát tài sản'
        },
        'keywords': ['tiền bạc', 'quyết đoán', 'cứng rắn', 'kinh doanh', 'thực tế']
    },
    'Thiên Đồng': {
        'type': 'Chính Tinh',
        'group': 'Tử Phủ',
        'element': 'Thủy',
        'nature': 'Cát tinh',
        'rank': 'Phúc tinh - Sao phúc lộc',
        'meaning': {
            'general': 'Thiên Đồng là sao phúc tinh, chủ về hưởng thụ và an nhàn. Người có Thiên Đồng thường ôn hòa, thích cuộc sống nhàn nhã.',
            'career': 'Thích hợp làm nghệ thuật, giải trí, du lịch, nhà hàng khách sạn. Không thích áp lực cao.',
            'relationship': 'Hiền lành, dễ gần. Được mọi người yêu quý. Cần chủ động hơn trong tình cảm.',
            'health': 'Tuổi già an nhàn, khỏe mạnh. Cần chú ý vận động để tránh béo phì.'
        },
        'brightness_effect': {
            'Miếu': 'Phúc khí dồi dào, đời sống sung túc, an nhàn',
            'Vượng': 'Hưởng thụ, cuộc sống thoải mái',
            'Đắc': 'Có phúc nhưng cần làm việc',
            'Bình': 'Cuộc sống bình thường, không nhiều may mắn',
            'Hãm': 'Lười biếng, khó tiến thân, thiếu chí tiến thủ'
        },
        'keywords': ['an nhàn', 'hưởng thụ', 'ôn hòa', 'phúc đức', 'hiền lành']
    },
    'Liêm Trinh': {
        'type': 'Chính Tinh',
        'group': 'Tử Phủ',
        'element': 'Hỏa',
        'nature': 'Trung tính (có thể cát hoặc hung)',
        'rank': 'Tù tinh - Sao phức tạp',
        'meaning': {
            'general': 'Liêm Trinh là sao phức tạp, có tính hai mặt. Người có Liêm Trinh thường nhạy bén, khéo léo trong giao tiếp nhưng dễ gặp thị phi.',
            'career': 'Thích hợp làm luật sư, ngoại giao, kinh doanh, bán hàng. Có tài ăn nói thuyết phục.',
            'relationship': 'Có sức hút, dễ có quan hệ phức tạp. Cần cẩn thận trong tình cảm.',
            'health': 'Chú ý tim và hệ tuần hoàn. Dễ bị stress và mất ngủ.'
        },
        'brightness_effect': {
            'Miếu': 'Khéo léo, thành công trong giao tiếp và đàm phán',
            'Vượng': 'Có tài ngoại giao, được nhiều người tin tưởng',
            'Đắc': 'Có khả năng nhưng cần cẩn thận thị phi',
            'Bình': 'Dễ gặp rắc rối trong quan hệ',
            'Hãm': 'Hay gặp kiện tụng, thị phi, tai tiếng'
        },
        'keywords': ['phức tạp', 'khéo léo', 'thị phi', 'kiện tụng', 'ngoại giao']
    },
    'Thiên Phủ': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Thổ',
        'nature': 'Cát tinh',
        'rank': 'Tài khố tinh - Sao kho tàng',
        'meaning': {
            'general': 'Thiên Phủ là sao tài khố, chủ về sự giàu có và ổn định. Người có Thiên Phủ thường có tài sản, cuộc sống sung túc.',
            'career': 'Thích hợp làm quản lý tài sản, bất động sản, ngân hàng. Giỏi tích lũy và bảo toàn.',
            'relationship': 'Ổn định, đáng tin cậy. Là trụ cột gia đình. Cần chủ động hơn.',
            'health': 'Khỏe mạnh, sống lâu. Chú ý dạ dày và tiêu hóa.'
        },
        'brightness_effect': {
            'Miếu': 'Giàu có, gia đình hạnh phúc, tài sản dồi dào',
            'Vượng': 'Sung túc, ổn định, được mọi người tin tưởng',
            'Đắc': 'Có tài sản nhưng phải vất vả tích lũy',
            'Bình': 'Cuộc sống đủ ăn, không giàu không nghèo',
            'Hãm': 'Khó tích lũy, hay mất của'
        },
        'keywords': ['giàu có', 'ổn định', 'kho tàng', 'sung túc', 'bảo thủ']
    },
    'Thái Âm': {
        'type': 'Chính Tinh',
        'group': 'Nhật Nguyệt',
        'element': 'Thủy',
        'nature': 'Cát tinh',
        'rank': 'Điền sản tinh - Sao tài sản',
        'meaning': {
            'general': 'Thái Âm là sao mặt trăng, đại diện cho tình cảm và tài sản. Người có Thái Âm thường giàu cảm xúc, có tài về nghệ thuật.',
            'career': 'Thích hợp làm nghệ thuật, bất động sản, trang trí nội thất. Có khiếu thẩm mỹ.',
            'relationship': 'Giàu tình cảm, lãng mạn. Hay mơ mộng, cần thực tế hơn.',
            'health': 'Chú ý thận và hệ tiết niệu. Phụ nữ chú ý phụ khoa.'
        },
        'brightness_effect': {
            'Miếu': 'Giàu có về tài sản, nhà cửa. Tình cảm viên mãn',
            'Vượng': 'Có điền sản, cuộc sống đầy đủ',
            'Đắc': 'Có tài sản nhưng phải cố gắng',
            'Bình': 'Tình cảm và tài sản bình thường',
            'Hãm': 'Đa cảm, hay buồn, khó có tài sản'
        },
        'keywords': ['tình cảm', 'tài sản', 'nghệ thuật', 'mơ mộng', 'điền sản']
    },
    'Tham Lang': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Thủy/Mộc',
        'nature': 'Trung tính (đào hoa)',
        'rank': 'Đào hoa tinh - Sao dục vọng',
        'meaning': {
            'general': 'Tham Lang là sao đào hoa, đại diện cho dục vọng và tham vọng. Người có Tham Lang thường có sức hút, đa tài nhưng hay tham lam.',
            'career': 'Thích hợp làm nghệ thuật, giải trí, kinh doanh ăn uống, spa. Có tài xã giao.',
            'relationship': 'Có sức hút mạnh, dễ có nhiều mối quan hệ. Cần kiểm soát dục vọng.',
            'health': 'Chú ý gan và hệ tiết niệu. Cần tiết chế trong ăn uống và tình dục.'
        },
        'brightness_effect': {
            'Miếu': 'Đào hoa tốt, hôn nhân hạnh phúc, có tài nghệ thuật',
            'Vượng': 'Có duyên, được nhiều người yêu quý',
            'Đắc': 'Có sức hút nhưng cần cẩn thận tình cảm',
            'Bình': 'Đào hoa bình thường, không nổi bật',
            'Hãm': 'Đào hoa xấu, dễ sa vào dục vọng, mất mát vì tình'
        },
        'keywords': ['đào hoa', 'dục vọng', 'tham vọng', 'quyến rũ', 'đa tài']
    },
    'Cự Môn': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Thủy',
        'nature': 'Hung tinh (có thể hóa cát)',
        'rank': 'Thị phi tinh - Sao miệng lưỡi',
        'meaning': {
            'general': 'Cự Môn là sao thị phi, đại diện cho ăn nói và tranh cãi. Người có Cự Môn thường có tài ăn nói nhưng dễ gây thị phi.',
            'career': 'Thích hợp làm luật sư, giáo viên, MC, bán hàng. Có tài biện luận và thuyết phục.',
            'relationship': 'Hay tranh cãi, cần học cách im lặng. Miệng lưỡi dễ làm mất lòng người.',
            'health': 'Chú ý miệng, họng và hệ tiêu hóa. Cần kiểm soát lời nói.'
        },
        'brightness_effect': {
            'Miếu': 'Tài ăn nói xuất chúng, có thể làm luật sư, MC giỏi',
            'Vượng': 'Có tài thuyết phục, được tin tưởng',
            'Đắc': 'Có khả năng giao tiếp nhưng cần cẩn thận',
            'Bình': 'Hay gặp thị phi nhỏ, cần kiềm chế',
            'Hãm': 'Hay gây thị phi, tranh cãi, kiện tụng'
        },
        'keywords': ['thị phi', 'ăn nói', 'tranh cãi', 'biện luận', 'miệng lưỡi']
    },
    'Thiên Tướng': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Thủy',
        'nature': 'Cát tinh',
        'rank': 'Ấn tinh - Sao quan ấn',
        'meaning': {
            'general': 'Thiên Tướng là sao ấn tinh, đại diện cho chức vị và sự tin tưởng. Người có Thiên Tướng thường được tin tưởng, giao phó trọng trách.',
            'career': 'Thích hợp làm quản lý, hành chính, công chức. Được cấp trên tin tưởng.',
            'relationship': 'Đáng tin cậy, có trách nhiệm. Hay gánh vác việc cho người khác.',
            'health': 'Khỏe mạnh. Chú ý thận và hệ tiết niệu.'
        },
        'brightness_effect': {
            'Miếu': 'Có chức vị cao, được tin tưởng tuyệt đối',
            'Vượng': 'Có địa vị, được giao trọng trách',
            'Đắc': 'Có uy tín nhưng phải chứng minh',
            'Bình': 'Địa vị bình thường, không nổi bật',
            'Hãm': 'Dễ bị lợi dụng, gánh vác thay người khác'
        },
        'keywords': ['chức vị', 'tin tưởng', 'trách nhiệm', 'quân tử', 'ấn tín']
    },
    'Thiên Lương': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Mộc',  # Theo Nam Phái (Video thầy Lê Quang Lăng)
        'nature': 'Cát tinh',
        'rank': 'Phúc thọ tinh - Ấm tinh (Sao che chở)',
        'meaning': {
            'general': 'Thiên Lương là "Ấm tinh", chủ về sự che chở, thiện lương. Người có Thiên Lương tâm địa rất tốt, thích làm việc thiện, có phong thái người thầy (thích lý luận, dạy bảo).',
            'career': 'Thích hợp làm giáo viên, thầy thuốc, cố vấn, công tác xã hội, từ thiện. Có khả năng giải quyết khủng hoảng (giải ách).',
            'relationship': 'Có sự đối lập: Với gia đình thì khắt khe, chi ly, tiết kiệm; nhưng ra xã hội lại rộng rãi, hào phóng, không toan tính.',
            'health': 'Sống thọ, thường có vẻ ngoài thư sinh hoặc già dặn trước tuổi. Giỏi hoa giải bệnh tật.'
        },
        'brightness_effect': {
            'Miếu': 'Phúc thọ song toàn, trí tuệ xuất chúng. Đặc biệt cư Tý là cách "Phượng Lãm Cao Cương".',
            'Vượng': 'Có đức độ, được kính trọng, lời nói có gang thép',
            'Đắc': 'Hiền lành, thích an phận',
            'Bình': 'Bình thường, tâm tính tốt',
            'Hãm': 'Hay lo lắng thái quá, cô độc, dễ bị hiểu lầm'
        },
        'keywords': ['ấm tinh', 'thiện lương', 'người thầy', 'nguyên tắc', 'giải ách']
    },
    'Thất Sát': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Kim',
        'nature': 'Hung tinh (có thể hóa cát)',
        'rank': 'Tướng tinh - Sao chiến đấu',
        'meaning': {
            'general': 'Thất Sát là sao tướng tinh, đại diện cho sự cương quyết và chiến đấu. Người có Thất Sát thường dũng cảm, quyết đoán nhưng dễ cô độc.',
            'career': 'Thích hợp làm quân đội, cảnh sát, kinh doanh mạo hiểm. Có tài lãnh đạo trong khó khăn.',
            'relationship': 'Cương quyết, ít thể hiện tình cảm. Cần học cách mềm mỏng.',
            'health': 'Chú ý phổi và hệ hô hấp. Dễ bị tai nạn.'
        },
        'brightness_effect': {
            'Miếu': 'Uy quyền lớn, thành công trong lĩnh vực đòi hỏi dũng cảm',
            'Vượng': 'Có quyền lực, được kính sợ',
            'Đắc': 'Có sức mạnh nhưng phải kiềm chế',
            'Bình': 'Khí chất bình thường',
            'Hãm': 'Cô độc, dễ xung đột, hay gặp tai nạn'
        },
        'keywords': ['dũng cảm', 'cương quyết', 'cô độc', 'chiến đấu', 'quyết đoán']
    },
    'Phá Quân': {
        'type': 'Chính Tinh',
        'group': 'Thiên Phủ',
        'element': 'Thủy',
        'nature': 'Hung tinh (có thể hóa cát)',
        'rank': 'Đổi mới tinh - Sao phá vỡ',
        'meaning': {
            'general': 'Phá Quân là sao đổi mới, đại diện cho sự phá vỡ và tiên phong. Người có Phá Quân thường dám nghĩ dám làm, hay thay đổi.',
            'career': 'Thích hợp làm khởi nghiệp, cải cách, sáng tạo. Không thích làm theo lối mòn.',
            'relationship': 'Hay thay đổi, khó gắn bó lâu dài. Cần ổn định hơn.',
            'health': 'Chú ý thận và hệ tiết niệu. Dễ bị tai nạn.'
        },
        'brightness_effect': {
            'Miếu': 'Tiên phong thành công, phá vỡ khuôn mẫu và đạt thành tựu',
            'Vượng': 'Có khả năng đổi mới, được công nhận',
            'Đắc': 'Có ý tưởng nhưng cần kiên trì',
            'Bình': 'Hay thay đổi, khó ổn định',
            'Hãm': 'Phá tán, bất ổn, hay mất mát'
        },
        'keywords': ['đổi mới', 'phá vỡ', 'tiên phong', 'thay đổi', 'bất ổn']
    }
}


def get_star_detail(star_name: str) -> dict:
    """
    Lấy thông tin chi tiết của một sao
    
    Args:
        star_name: Tên sao
        
    Returns:
        dict thông tin chi tiết sao theo format UC-03
    """
    if star_name in CHINH_TINH_DETAILS:
        return CHINH_TINH_DETAILS[star_name]
    
    # Trả về thông tin cơ bản cho sao không có trong bảng chi tiết
    return {
        'type': 'Phụ Tinh',
        'group': 'Khác',
        'element': 'Không xác định',
        'nature': 'Trung tính',
        'rank': 'Phụ tinh',
        'meaning': {
            'general': f'{star_name} là phụ tinh, xem thêm trong bảng phụ tinh.',
            'career': 'Tùy thuộc vào vị trí và tổ hợp sao',
            'relationship': 'Tùy thuộc vào vị trí và tổ hợp sao',
            'health': 'Tùy thuộc vào vị trí và tổ hợp sao'
        },
        'brightness_effect': {},
        'keywords': []
    }

