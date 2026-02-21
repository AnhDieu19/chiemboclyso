"""
Bảng 81 số linh nghĩa trong Ngũ Cách đặt tên
Nguồn: Danh Tính học - Phong Thủy đặt tên

Mỗi số từ 1-81 có:
- type: DAI_CAT (Đại Cát), CAT (Cát), TRUNG_CAT (Trung Cát), HUNG (Hung)
- name: Tên gọi của số
- meaning: Ý nghĩa tổng quát
- details: Chi tiết về Cơ nghiệp, Gia đình, Sức khỏe, Hàm nghĩa
"""

# Phân loại Cát/Hung
DAI_CAT = "DAI_CAT"  # Đại Cát
CAT = "CAT"          # Cát
TRUNG_CAT = "TRUNG_CAT"  # Trung Cát
HUNG = "HUNG"        # Hung

# Bảng 81 số linh nghĩa
NGU_CACH_MEANINGS = {
    1: {
        "type": DAI_CAT,
        "name": "Thái Cực chi số",
        "meaning": "Số khởi đầu vạn vật, đại cát đại lợi",
        "details": {
            "co_nghiep": "Có quyền uy, lãnh đạo",
            "gia_dinh": "Gia đình hòa thuận",
            "suc_khoe": "Khỏe mạnh, trường thọ",
            "ham_nghia": "Số đứng đầu, có uy quyền, phú quý vinh hoa"
        }
    },
    2: {
        "type": HUNG,
        "name": "Phân ly chi số",
        "meaning": "Số chia ly, không tốt",
        "details": {
            "co_nghiep": "Sự nghiệp bấp bênh",
            "gia_dinh": "Gia đình ly tán",
            "suc_khoe": "Sức khỏe yếu",
            "ham_nghia": "Số phân ly, cô độc, không thuận lợi"
        }
    },
    3: {
        "type": DAI_CAT,
        "name": "Cát tường chi số",
        "meaning": "Số may mắn, hanh thông",
        "details": {
            "co_nghiep": "Sự nghiệp phát triển",
            "gia_dinh": "Gia đình êm ấm",
            "suc_khoe": "Thể lực tốt",
            "ham_nghia": "Trời đất nhân hợp, vạn sự như ý"
        }
    },
    4: {
        "type": HUNG,
        "name": "Tứ tượng chi số",
        "meaning": "Số không ổn định",
        "details": {
            "co_nghiep": "Khó khăn nhiều",
            "gia_dinh": "Bất hòa",
            "suc_khoe": "Dễ đau ốm",
            "ham_nghia": "Số bốn mùa biến đổi, vất vả"
        }
    },
    5: {
        "type": DAI_CAT,
        "name": "Trung ương chi số",
        "meaning": "Số trung tâm, cân bằng ngũ hành",
        "details": {
            "co_nghiep": "Phát triển bền vững",
            "gia_dinh": "Hạnh phúc",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Ngũ Hoàng trung cung, âm dương hòa hợp"
        }
    },
    6: {
        "type": DAI_CAT,
        "name": "Thiên đức chi số",
        "meaning": "Số đức trời ban",
        "details": {
            "co_nghiep": "Được quý nhân phù trợ",
            "gia_dinh": "Con cháu hiếu thuận",
            "suc_khoe": "Trường thọ",
            "ham_nghia": "Thiên đức quý nhân chiếu mệnh"
        }
    },
    7: {
        "type": CAT,
        "name": "Thất chính chi số",
        "meaning": "Số cương nghị, quyết đoán",
        "details": {
            "co_nghiep": "Thành công bằng nỗ lực",
            "gia_dinh": "Cần điều hòa",
            "suc_khoe": "Tốt nếu biết điều độ",
            "ham_nghia": "Bắc Đẩu thất tinh, cứng rắn"
        }
    },
    8: {
        "type": DAI_CAT,
        "name": "Bát quái chi số",
        "meaning": "Số phát triển, thịnh vượng",
        "details": {
            "co_nghiep": "Tài lộc dồi dào",
            "gia_dinh": "Gia đình hưng vượng",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Bát quái hanh thông, vạn sự cát"
        }
    },
    9: {
        "type": HUNG,
        "name": "Cửu tuyền chi số",
        "meaning": "Số cuối cùng, cần cẩn thận",
        "details": {
            "co_nghiep": "Thăng trầm",
            "gia_dinh": "Biến động",
            "suc_khoe": "Cần chú ý",
            "ham_nghia": "Số tận cùng, cực thịnh rồi suy"
        }
    },
    10: {
        "type": HUNG,
        "name": "Không hư chi số",
        "meaning": "Số rỗng không, bất lợi",
        "details": {
            "co_nghiep": "Khó giữ được",
            "gia_dinh": "Cô đơn",
            "suc_khoe": "Yếu",
            "ham_nghia": "Số mười trở về không, vạn sự thành không"
        }
    },
    11: {
        "type": DAI_CAT,
        "name": "Hạn tân chi số",
        "meaning": "Số tái sinh, phát triển mới",
        "details": {
            "co_nghiep": "Thành công từ khó khăn",
            "gia_dinh": "Hòa thuận",
            "suc_khoe": "Phục hồi tốt",
            "ham_nghia": "Vượt qua khó khăn đến thành công"
        }
    },
    12: {
        "type": HUNG,
        "name": "Bạc nhược chi số",
        "meaning": "Số yếu đuối, thiếu may mắn",
        "details": {
            "co_nghiep": "Khó phát triển",
            "gia_dinh": "Ít người thân",
            "suc_khoe": "Yếu",
            "ham_nghia": "Ý chí bạc nhược, khó thành công lớn"
        }
    },
    13: {
        "type": DAI_CAT,
        "name": "Trí tuệ chi số",
        "meaning": "Số trí tuệ, tài năng thành công, mưu lược siêu phàm",
        "details": {
            "co_nghiep": "Có tài năng, có sự nghiệp văn chương, phát triển tiền tài",
            "gia_dinh": "Tổ tông phù hộ, con cháu hiếu thuận, thấy được đoàn viên",
            "suc_khoe": "Thấy được sức khỏe trường thọ, tam tài thịnh vượng",
            "ham_nghia": "Phúc hợp tài năng có mưu lược, có tính kiên nhẫn làm việc. Được chỉ dẫn tốt, hưởng phú quý hạnh phúc, là người có trí tuệ"
        }
    },
    14: {
        "type": HUNG,
        "name": "Phá bại chi số",
        "meaning": "Số phá hủy, tan rã",
        "details": {
            "co_nghiep": "Dễ thất bại",
            "gia_dinh": "Không hòa thuận",
            "suc_khoe": "Kém",
            "ham_nghia": "Số phá bại gia nghiệp"
        }
    },
    15: {
        "type": DAI_CAT,
        "name": "Phúc thọ chi số",
        "meaning": "Số phúc đức, tài lộc dồi dào",
        "details": {
            "co_nghiep": "Giàu có",
            "gia_dinh": "Đầm ấm hạnh phúc",
            "suc_khoe": "Trường thọ",
            "ham_nghia": "Phúc lộc song toàn, vạn sự như ý"
        }
    },
    16: {
        "type": DAI_CAT,
        "name": "Hậu đức chi số",
        "meaning": "Số đức hậu, quý nhân phù trợ",
        "details": {
            "co_nghiep": "Được người giúp đỡ",
            "gia_dinh": "Ấm êm",
            "suc_khoe": "Tốt",
            "ham_nghia": "Đức dày được lộc, quý nhân nâng đỡ"
        }
    },
    17: {
        "type": DAI_CAT,
        "name": "Cương nhu chi số",
        "meaning": "Số cương nhu song hành, vượt qua mọi khó khăn kiên cường",
        "details": {
            "co_nghiep": "Có quyền lực, văn xướng, liên quan đến nghệ thuật",
            "gia_dinh": "Nữ biết điều hòa công việc, hiền hậu thì gia đình viên mãn",
            "suc_khoe": "Toàn tâm thì sẽ thấy được trường thọ",
            "ham_nghia": "Uy vũ kiên cường, ý chí kiên định, có ý chí và nghị lực vượt qua mọi khó khăn. Nếu biết được tu dưỡng đạo đức, tâm ôn hòa sẽ có phúc lộc"
        }
    },
    18: {
        "type": DAI_CAT,
        "name": "Hữu chí chi số",
        "meaning": "Số có chí quyết tâm thành công",
        "details": {
            "co_nghiep": "Thành công bằng nỗ lực",
            "gia_dinh": "Gia đình hạnh phúc",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Có chí làm nên sự nghiệp lớn"
        }
    },
    19: {
        "type": HUNG,
        "name": "Đa nạn chi số",
        "meaning": "Số nhiều khó khăn, tai nạn",
        "details": {
            "co_nghiep": "Vất vả",
            "gia_dinh": "Biến cố",
            "suc_khoe": "Cần cẩn thận",
            "ham_nghia": "Nhiều trắc trở, tai ương"
        }
    },
    20: {
        "type": HUNG,
        "name": "Hư vô chi số",
        "meaning": "Số không tốt, phá sự nghiệp",
        "details": {
            "co_nghiep": "Có tài năng nhưng sự nghiệp không được may mắn",
            "gia_dinh": "Tình thân bất lập, anh em không hợp nhau, xa quê hương lập nghiệp, mọi sự nhẫn nhịn trong nhà mới được bình yên",
            "suc_khoe": "Số này sức khỏe yếu. Người tam tài phối trí không tốt sẽ đoạn mệnh, phế tật. Người thuộc vận Kim và Mộc được an toàn",
            "ham_nghia": "Mọi việc không tốt, một đời không được bình an, tai họa ập đến, không như ý, rơi vào cảnh éo le. Vì vạn sự không thành, cuối đời sống khép mình"
        }
    },
    21: {
        "type": DAI_CAT,
        "name": "Đầu lĩnh chi số",
        "meaning": "Số đứng đầu, lãnh đạo",
        "details": {
            "co_nghiep": "Quyền cao chức trọng",
            "gia_dinh": "Gia đình thịnh vượng",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Đứng đầu muôn người, thành đại nghiệp"
        }
    },
    22: {
        "type": HUNG,
        "name": "Thu thảo chi số",
        "meaning": "Số suy yếu như cỏ mùa thu",
        "details": {
            "co_nghiep": "Khó phát triển",
            "gia_dinh": "Lẻ loi",
            "suc_khoe": "Yếu",
            "ham_nghia": "Số suy bại, như cỏ héo mùa thu"
        }
    },
    23: {
        "type": DAI_CAT,
        "name": "Vượng thịnh chi số",
        "meaning": "Số hưng vượng, phát triển",
        "details": {
            "co_nghiep": "Thành công rực rỡ",
            "gia_dinh": "Thịnh vượng",
            "suc_khoe": "Tốt",
            "ham_nghia": "Vượng như mặt trời đang lên"
        }
    },
    24: {
        "type": DAI_CAT,
        "name": "Dư khánh chi số",
        "meaning": "Số dư dật, phú quý",
        "details": {
            "co_nghiep": "Giàu có dư thừa",
            "gia_dinh": "Con cháu đông đúc",
            "suc_khoe": "Trường thọ",
            "ham_nghia": "Phúc lộc dư thừa, tài lộc dồi dào"
        }
    },
    25: {
        "type": CAT,
        "name": "Anh tuấn chi số",
        "meaning": "Số anh hùng, tài năng",
        "details": {
            "co_nghiep": "Nổi bật trong lĩnh vực",
            "gia_dinh": "Được kính trọng",
            "suc_khoe": "Khỏe",
            "ham_nghia": "Tài năng xuất chúng, anh tuấn hơn người"
        }
    },
    26: {
        "type": HUNG,
        "name": "Anh hùng chi số",
        "meaning": "Số anh hùng nhưng đau khổ",
        "details": {
            "co_nghiep": "Thành công nhưng cô đơn",
            "gia_dinh": "Thiếu hạnh phúc",
            "suc_khoe": "Cần chú ý",
            "ham_nghia": "Anh hùng thường gặp bi kịch"
        }
    },
    27: {
        "type": HUNG,
        "name": "Bất thuận chi số",
        "meaning": "Số không thuận lợi",
        "details": {
            "co_nghiep": "Nhiều trắc trở",
            "gia_dinh": "Mâu thuẫn",
            "suc_khoe": "Không ổn định",
            "ham_nghia": "Mọi việc không suôn sẻ"
        }
    },
    28: {
        "type": HUNG,
        "name": "Ly biệt chi số",
        "meaning": "Số hành khất vô định, hào khí sinh ly",
        "details": {
            "co_nghiep": "Là người có học thức, có tướng làm quan nhưng có hung tinh chiếu mệnh",
            "gia_dinh": "Anh em ít liên lạc, con cái ly biệt",
            "suc_khoe": "Người tâm tính không tốt, không có hại lớn",
            "ham_nghia": "Người có số này gặp vận nguy nan. Có khí chất hào kiệt, nhiều sóng gió biến phát, khó tránh bị chê trách, phỉ báng hoặc lúc tai họa ập đến bị hại, hoặc khắc con cháu, cũng có thể từ nhỏ đã ly biệt người thân"
        }
    },
    29: {
        "type": DAI_CAT,
        "name": "Trí mưu chi số",
        "meaning": "Số mưu trí, thành công",
        "details": {
            "co_nghiep": "Thành công bằng trí tuệ",
            "gia_dinh": "Hạnh phúc",
            "suc_khoe": "Tốt",
            "ham_nghia": "Mưu trí hơn người, thành đại sự"
        }
    },
    30: {
        "type": TRUNG_CAT,
        "name": "Bất an chi số",
        "meaning": "Số thăng trầm, may rủi",
        "details": {
            "co_nghiep": "Lúc thành lúc bại",
            "gia_dinh": "Biến động",
            "suc_khoe": "Cần chú ý",
            "ham_nghia": "Nửa cát nửa hung, thăng trầm bất định"
        }
    },
    31: {
        "type": DAI_CAT,
        "name": "Hưng gia chi số",
        "meaning": "Số hưng thịnh gia đạo",
        "details": {
            "co_nghiep": "Thành công vững chắc",
            "gia_dinh": "Gia đình hưng vượng",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Xây dựng cơ đồ vững bền"
        }
    },
    32: {
        "type": DAI_CAT,
        "name": "Cơ may chi số",
        "meaning": "Số có cơ may, nhiều hy vọng",
        "details": {
            "co_nghiep": "Là người có học thức, văn chương phát triển, có sự nghiệp tổ tiên để lại",
            "gia_dinh": "Gia đình hưng vượng, thấy được viên mãn, con cháu hưng thịnh",
            "suc_khoe": "Thấy được an khang, nhưng người Tam Tài không tốt thì có bệnh",
            "ham_nghia": "Số có cơ may nhiều hy vọng. Nếu được bề trên, cấp trên nâng đỡ, dìu dắt thì thế thành công như chẻ tre. Bản tính hiền hậu, có đức, yêu thương mọi người. Gia đình hưng vượng, phồn vinh. Số cát cao nhất"
        }
    },
    33: {
        "type": DAI_CAT,
        "name": "Thăng long chi số",
        "meaning": "Số rồng bay lên, hiển đạt",
        "details": {
            "co_nghiep": "Thăng tiến nhanh chóng",
            "gia_dinh": "Vinh hiển",
            "suc_khoe": "Tốt",
            "ham_nghia": "Như rồng gặp mây, thăng thiên"
        }
    },
    34: {
        "type": HUNG,
        "name": "Phá gia chi số",
        "meaning": "Số phá tan gia đạo",
        "details": {
            "co_nghiep": "Tan rã",
            "gia_dinh": "Ly tán",
            "suc_khoe": "Biến động",
            "ham_nghia": "Số phá gia bại sản"
        }
    },
    35: {
        "type": CAT,
        "name": "Bình an chi số",
        "meaning": "Số bình an, ổn định",
        "details": {
            "co_nghiep": "Bình ổn phát triển",
            "gia_dinh": "Yên ấm",
            "suc_khoe": "Ổn định",
            "ham_nghia": "Cuộc sống bình an, thuận lợi"
        }
    },
    36: {
        "type": HUNG,
        "name": "Ba lan chi số",
        "meaning": "Số sóng gió, biến động",
        "details": {
            "co_nghiep": "Nhiều thăng trầm",
            "gia_dinh": "Bất ổn",
            "suc_khoe": "Cần cẩn thận",
            "ham_nghia": "Đời nhiều sóng gió, biến cố"
        }
    },
    37: {
        "type": DAI_CAT,
        "name": "Xuất chúng chi số",
        "meaning": "Số xuất chúng, hơn người",
        "details": {
            "co_nghiep": "Nổi bật thành công",
            "gia_dinh": "Được kính nể",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Tài năng vượt trội, thành công lớn"
        }
    },
    38: {
        "type": TRUNG_CAT,
        "name": "Văn nhân chi số",
        "meaning": "Số văn nhân, học giả",
        "details": {
            "co_nghiep": "Thành công trong học thuật",
            "gia_dinh": "Bình yên",
            "suc_khoe": "Ổn định",
            "ham_nghia": "Hay chữ nghĩa, thành công bằng văn"
        }
    },
    39: {
        "type": DAI_CAT,
        "name": "Phú quý chi số",
        "meaning": "Số giàu sang, phú quý",
        "details": {
            "co_nghiep": "Tài lộc dồi dào",
            "gia_dinh": "Vinh hoa",
            "suc_khoe": "Trường thọ",
            "ham_nghia": "Phú quý song toàn, vinh hiển"
        }
    },
    40: {
        "type": TRUNG_CAT,
        "name": "Thối ẩn chi số",
        "meaning": "Số lui về ẩn dật",
        "details": {
            "co_nghiep": "Thành công rồi lui",
            "gia_dinh": "Yên bình",
            "suc_khoe": "Tốt nếu biết nghỉ ngơi",
            "ham_nghia": "Nên biết lui khi thành công"
        }
    },
    41: {
        "type": DAI_CAT,
        "name": "Thuần dương chi số",
        "meaning": "Số thuần dương, mạnh mẽ",
        "details": {
            "co_nghiep": "Thành công lớn",
            "gia_dinh": "Thịnh vượng",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Dương khí đầy đủ, vạn sự hanh thông"
        }
    },
    42: {
        "type": TRUNG_CAT,
        "name": "Đa năng chi số",
        "meaning": "Số đa tài, nhiều khả năng",
        "details": {
            "co_nghiep": "Làm nhiều việc nhưng không chuyên",
            "gia_dinh": "Bình ổn",
            "suc_khoe": "Cần cân bằng",
            "ham_nghia": "Đa nghề nhưng cần tập trung"
        }
    },
    43: {
        "type": HUNG,
        "name": "Tán tài chi số",
        "meaning": "Số tan tài, mất của",
        "details": {
            "co_nghiep": "Khó giữ tiền",
            "gia_dinh": "Thiếu hụt",
            "suc_khoe": "Cần chú ý",
            "ham_nghia": "Tiền vào tay rồi ra"
        }
    },
    44: {
        "type": HUNG,
        "name": "Phiền não chi số",
        "meaning": "Số phiền muộn, lo lắng",
        "details": {
            "co_nghiep": "Nhiều khó khăn",
            "gia_dinh": "Không yên",
            "suc_khoe": "Stress",
            "ham_nghia": "Đời nhiều phiền não, lo âu"
        }
    },
    45: {
        "type": DAI_CAT,
        "name": "Thuận phong chi số",
        "meaning": "Số thuận buồm xuôi gió",
        "details": {
            "co_nghiep": "Thành công thuận lợi",
            "gia_dinh": "Hạnh phúc",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Mọi việc thuận buồm xuôi gió"
        }
    },
    46: {
        "type": HUNG,
        "name": "Trở trệ chi số",
        "meaning": "Số trở ngại, chậm chạp",
        "details": {
            "co_nghiep": "Chậm phát triển",
            "gia_dinh": "Thiếu thuận lợi",
            "suc_khoe": "Ì ạch",
            "ham_nghia": "Mọi việc chậm chạp, trở ngại"
        }
    },
    47: {
        "type": DAI_CAT,
        "name": "Thu hoạch chi số",
        "meaning": "Số thu hoạch, gặt hái",
        "details": {
            "co_nghiep": "Thành quả xứng đáng",
            "gia_dinh": "Đầy đủ",
            "suc_khoe": "Tốt",
            "ham_nghia": "Công sức bỏ ra được đền đáp"
        }
    },
    48: {
        "type": DAI_CAT,
        "name": "Trí mưu đại chi số",
        "meaning": "Số đại trí mưu",
        "details": {
            "co_nghiep": "Thành công bằng mưu lược",
            "gia_dinh": "Được kính nể",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Mưu trí tuyệt vời, thành đại sự"
        }
    },
    49: {
        "type": TRUNG_CAT,
        "name": "Chuyển biến chi số",
        "meaning": "Số thay đổi, biến chuyển",
        "details": {
            "co_nghiep": "Lúc thăng lúc trầm",
            "gia_dinh": "Biến động",
            "suc_khoe": "Cần thích ứng",
            "ham_nghia": "Đời nhiều thay đổi, cần linh hoạt"
        }
    },
    50: {
        "type": TRUNG_CAT,
        "name": "Thành bại chi số",
        "meaning": "Số thành bại xen kẽ",
        "details": {
            "co_nghiep": "Lên xuống thất thường",
            "gia_dinh": "Không ổn định",
            "suc_khoe": "Cần cẩn thận",
            "ham_nghia": "Đời có lúc thành lúc bại"
        }
    },
    51: {
        "type": TRUNG_CAT,
        "name": "Vãn thành chi số",
        "meaning": "Số thành công muộn",
        "details": {
            "co_nghiep": "Nửa sau đời thành công",
            "gia_dinh": "Bình yên cuối đời",
            "suc_khoe": "Tốt dần theo tuổi",
            "ham_nghia": "Thành công đến muộn nhưng bền"
        }
    },
    52: {
        "type": DAI_CAT,
        "name": "Đạt quan chi số",
        "meaning": "Số đạt được quyền cao",
        "details": {
            "co_nghiep": "Chức cao vọng trọng",
            "gia_dinh": "Vinh hiển",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Đạt được địa vị cao trong xã hội"
        }
    },
    53: {
        "type": TRUNG_CAT,
        "name": "Nội hư chi số",
        "meaning": "Số ngoài thực trong rỗng",
        "details": {
            "co_nghiep": "Bề ngoài tốt, bên trong thiếu",
            "gia_dinh": "Cần xây dựng",
            "suc_khoe": "Cần bồi bổ",
            "ham_nghia": "Cần xây dựng từ bên trong"
        }
    },
    54: {
        "type": HUNG,
        "name": "Thảm đạm chi số",
        "meaning": "Số ảm đạm, buồn thảm",
        "details": {
            "co_nghiep": "Khó thành công",
            "gia_dinh": "Không vui",
            "suc_khoe": "Lo âu",
            "ham_nghia": "Đời nhiều buồn phiền"
        }
    },
    55: {
        "type": TRUNG_CAT,
        "name": "Ngoại an chi số",
        "meaning": "Số bên ngoài yên ổn",
        "details": {
            "co_nghiep": "Ổn định nhưng không phát triển",
            "gia_dinh": "Bình yên",
            "suc_khoe": "Ổn",
            "ham_nghia": "Cuộc sống yên ổn, không nhiều biến động"
        }
    },
    56: {
        "type": HUNG,
        "name": "Thiếu lực chi số",
        "meaning": "Số thiếu sức, yếu đuối",
        "details": {
            "co_nghiep": "Khó thành công lớn",
            "gia_dinh": "Cần nỗ lực",
            "suc_khoe": "Yếu",
            "ham_nghia": "Thiếu nghị lực, cần rèn luyện"
        }
    },
    57: {
        "type": CAT,
        "name": "Cương nghị chi số",
        "meaning": "Số cứng rắn, kiên quyết",
        "details": {
            "co_nghiep": "Thành công bằng ý chí",
            "gia_dinh": "Cần mềm mỏng",
            "suc_khoe": "Khỏe",
            "ham_nghia": "Cương nghị, quyết đoán thành công"
        }
    },
    58: {
        "type": TRUNG_CAT,
        "name": "Tiên khổ chi số",
        "meaning": "Số trước khổ sau sướng",
        "details": {
            "co_nghiep": "Khởi đầu khó, sau thành công",
            "gia_dinh": "Hạnh phúc về sau",
            "suc_khoe": "Cải thiện theo tuổi",
            "ham_nghia": "Trải qua khó khăn mới đến thành công"
        }
    },
    59: {
        "type": HUNG,
        "name": "Bất đạt chi số",
        "meaning": "Số không đạt được",
        "details": {
            "co_nghiep": "Khó đạt mục tiêu",
            "gia_dinh": "Thiếu thốn",
            "suc_khoe": "Yếu",
            "ham_nghia": "Mọi việc khó đạt như ý"
        }
    },
    60: {
        "type": HUNG,
        "name": "Suy bại chi số",
        "meaning": "Số suy tàn, thất bại",
        "details": {
            "co_nghiep": "Khó giữ được thành quả",
            "gia_dinh": "Suy vi",
            "suc_khoe": "Giảm sút",
            "ham_nghia": "Số suy bại, khó vượt qua"
        }
    },
    61: {
        "type": CAT,
        "name": "Danh lợi chi số",
        "meaning": "Số có danh có lợi",
        "details": {
            "co_nghiep": "Thành công cả danh và lợi",
            "gia_dinh": "Được kính nể",
            "suc_khoe": "Tốt",
            "ham_nghia": "Danh lợi song toàn"
        }
    },
    62: {
        "type": HUNG,
        "name": "Suy nhược chi số",
        "meaning": "Số yếu đuối, suy sụp",
        "details": {
            "co_nghiep": "Khó phát triển",
            "gia_dinh": "Thiếu hạnh phúc",
            "suc_khoe": "Yếu",
            "ham_nghia": "Số suy yếu, cần nghị lực"
        }
    },
    63: {
        "type": DAI_CAT,
        "name": "Thọ phúc chi số",
        "meaning": "Số phúc đức trường thọ",
        "details": {
            "co_nghiep": "Thành công bền vững",
            "gia_dinh": "Hạnh phúc",
            "suc_khoe": "Trường thọ",
            "ham_nghia": "Phúc thọ vẹn toàn"
        }
    },
    64: {
        "type": HUNG,
        "name": "Trầm luân chi số",
        "meaning": "Số chìm nổi, khó khăn",
        "details": {
            "co_nghiep": "Thăng trầm bất định",
            "gia_dinh": "Biến động",
            "suc_khoe": "Cần chú ý",
            "ham_nghia": "Đời nhiều sóng gió"
        }
    },
    65: {
        "type": DAI_CAT,
        "name": "Hưng long chi số",
        "meaning": "Số hưng thịnh, phát triển",
        "details": {
            "co_nghiep": "Phát triển mạnh",
            "gia_dinh": "Thịnh vượng",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Vạn sự hưng long"
        }
    },
    66: {
        "type": HUNG,
        "name": "Tiến thoái chi số",
        "meaning": "Số tiến thoái lưỡng nan",
        "details": {
            "co_nghiep": "Khó quyết định",
            "gia_dinh": "Mâu thuẫn",
            "suc_khoe": "Stress",
            "ham_nghia": "Khó tiến khó lui"
        }
    },
    67: {
        "type": DAI_CAT,
        "name": "Hạnh thông chi số",
        "meaning": "Số may mắn, hanh thông",
        "details": {
            "co_nghiep": "Thuận lợi phát triển",
            "gia_dinh": "Hạnh phúc",
            "suc_khoe": "Tốt",
            "ham_nghia": "Vạn sự hanh thông"
        }
    },
    68: {
        "type": DAI_CAT,
        "name": "Đại phát chi số",
        "meaning": "Số phát đạt, thịnh vượng",
        "details": {
            "co_nghiep": "Thành công lớn",
            "gia_dinh": "Giàu có",
            "suc_khoe": "Khỏe mạnh",
            "ham_nghia": "Phát đạt, phú quý"
        }
    },
    69: {
        "type": HUNG,
        "name": "Bất định chi số",
        "meaning": "Số không ổn định",
        "details": {
            "co_nghiep": "Lúc được lúc mất",
            "gia_dinh": "Biến động",
            "suc_khoe": "Không ổn",
            "ham_nghia": "Đời bất định, khó lường"
        }
    },
    70: {
        "type": HUNG,
        "name": "Không hư chi số",
        "meaning": "Số rỗng không, thất bại",
        "details": {
            "co_nghiep": "Khó thành công",
            "gia_dinh": "Thiếu thốn",
            "suc_khoe": "Yếu",
            "ham_nghia": "Vạn sự thành không"
        }
    },
    71: {
        "type": TRUNG_CAT,
        "name": "Thất lợi chi số",
        "meaning": "Số mất lợi, ít may mắn",
        "details": {
            "co_nghiep": "Khó có lợi lớn",
            "gia_dinh": "Bình thường",
            "suc_khoe": "Trung bình",
            "ham_nghia": "Số bình thường, ít may mắn"
        }
    },
    72: {
        "type": HUNG,
        "name": "Tương lai chi số",
        "meaning": "Số tương lai bấp bênh",
        "details": {
            "co_nghiep": "Khó dự đoán",
            "gia_dinh": "Không chắc chắn",
            "suc_khoe": "Cần cẩn thận",
            "ham_nghia": "Tương lai không rõ ràng"
        }
    },
    73: {
        "type": TRUNG_CAT,
        "name": "Bình thuận chi số",
        "meaning": "Số bình ổn, thuận lợi",
        "details": {
            "co_nghiep": "Ổn định phát triển",
            "gia_dinh": "Yên ấm",
            "suc_khoe": "Tốt",
            "ham_nghia": "Cuộc sống bình thuận"
        }
    },
    74: {
        "type": HUNG,
        "name": "Cô độc chi số",
        "meaning": "Số cô đơn, lẻ loi",
        "details": {
            "co_nghiep": "Ít người giúp",
            "gia_dinh": "Cô đơn",
            "suc_khoe": "Cần chú ý",
            "ham_nghia": "Số cô độc, ít người thân"
        }
    },
    75: {
        "type": TRUNG_CAT,
        "name": "Thủ thành chi số",
        "meaning": "Số giữ được thành quả",
        "details": {
            "co_nghiep": "Giữ được cơ nghiệp",
            "gia_dinh": "Bình yên",
            "suc_khoe": "Ổn định",
            "ham_nghia": "Giữ được những gì đã có"
        }
    },
    76: {
        "type": HUNG,
        "name": "Tản mạn chi số",
        "meaning": "Số tan rã, tản mác",
        "details": {
            "co_nghiep": "Khó tập trung",
            "gia_dinh": "Ly tán",
            "suc_khoe": "Phân tán",
            "ham_nghia": "Mọi thứ dễ tan rã"
        }
    },
    77: {
        "type": TRUNG_CAT,
        "name": "Hậu kỳ chi số",
        "meaning": "Số may mắn về sau",
        "details": {
            "co_nghiep": "Nửa sau đời tốt",
            "gia_dinh": "Hạnh phúc cuối đời",
            "suc_khoe": "Tốt dần",
            "ham_nghia": "Vận may đến muộn"
        }
    },
    78: {
        "type": TRUNG_CAT,
        "name": "Tiền khổ chi số",
        "meaning": "Số đầu khổ sau sướng",
        "details": {
            "co_nghiep": "Nửa đầu vất vả, nửa sau thành công",
            "gia_dinh": "Hạnh phúc về sau",
            "suc_khoe": "Cải thiện",
            "ham_nghia": "Trước khổ sau sướng"
        }
    },
    79: {
        "type": HUNG,
        "name": "Cực khổ chi số",
        "meaning": "Số rất vất vả",
        "details": {
            "co_nghiep": "Nhiều khó khăn",
            "gia_dinh": "Thiếu thốn",
            "suc_khoe": "Yếu",
            "ham_nghia": "Đời nhiều vất vả"
        }
    },
    80: {
        "type": TRUNG_CAT,
        "name": "Hoàn kết chi số",
        "meaning": "Số kết thúc rồi lại bắt đầu",
        "details": {
            "co_nghiep": "Có thể làm lại từ đầu",
            "gia_dinh": "Có thể xây dựng lại",
            "suc_khoe": "Có thể phục hồi",
            "ham_nghia": "Kết thúc để bắt đầu mới"
        }
    },
    81: {
        "type": DAI_CAT,
        "name": "Hoàn nguyên chi số",
        "meaning": "Số quay về gốc, đại cát như số 1",
        "details": {
            "co_nghiep": "Thành công rực rỡ",
            "gia_dinh": "Vinh hiển",
            "suc_khoe": "Trường thọ",
            "ham_nghia": "81 quay về 1, vạn sự phục sinh, đại cát đại lợi"
        }
    }
}


def get_meaning(number):
    """Lấy ý nghĩa của số từ 1-81, nếu > 81 thì lấy phần dư"""
    if number <= 0:
        return None
    # Nếu số > 81, lấy phần dư (81 -> 81, 82 -> 1, 83 -> 2, ...)
    if number > 81:
        number = number % 81
        if number == 0:
            number = 81
    return NGU_CACH_MEANINGS.get(number)


def get_type_display(type_code):
    """Chuyển mã loại thành tên hiển thị tiếng Việt"""
    mapping = {
        DAI_CAT: "Đại Cát",
        CAT: "Cát",
        TRUNG_CAT: "Trung Cát",
        HUNG: "Hung"
    }
    return mapping.get(type_code, type_code)
