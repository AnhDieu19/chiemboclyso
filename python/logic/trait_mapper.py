"""
Trait Mapper: Convert user input (traits, events) into finding criteria.
"""

class TraitMapper:
    def __init__(self):
        # Maps specific string to criteria
        # Criteria format: {'cung': 'Mệnh', 'sao': 'Tử Vi'} or {'cung': 'Phu Thê', 'sao': ['Không', 'Kiếp']}
        self.rules = {
            # --- TÍNH CÁCH ---
            "Nóng nảy, vội vã": [
                {'cung': 'Mệnh', 'sao': 'Hỏa Tinh'},
                {'cung': 'Mệnh', 'sao': 'Linh Tinh'},
                {'cung': 'Mệnh', 'sao': 'Kinh Dương'},
                {'cung': 'Mệnh', 'sao': 'Đà La'},
                {'cung': 'Mệnh', 'sao': 'Thất Sát'},
                {'cung': 'Mệnh', 'sao': 'Phá Quân'},
            ],
            "Ôn hòa, điềm đạm": [
                {'cung': 'Mệnh', 'sao': 'Thiên Lương'},
                {'cung': 'Mệnh', 'sao': 'Thiên Đồng'},
                {'cung': 'Mệnh', 'sao': 'Thái Âm'},
                {'cung': 'Mệnh', 'sao': 'Thiên Phủ'},
                {'cung': 'Mệnh', 'sao': 'Thiên Tướng'},
            ],
            "Đa nghi, hay soi xét": [
                {'cung': 'Mệnh', 'sao': 'Cự Môn'},
                {'cung': 'Mệnh', 'sao': 'Phúc Bình'},
                {'cung': 'Mệnh', 'sao': 'Thiên Riêu'},
            ],
             "Vui vẻ, lạc quan": [
                {'cung': 'Mệnh', 'sao': 'Thiên Đồng'},
                {'cung': 'Mệnh', 'sao': 'Hóa Lộc'},
                {'cung': 'Mệnh', 'sao': 'Hỷ Thần'},
                {'cung': 'Mệnh', 'sao': 'Thiên Hỹ'},
            ],
            "Thích cô độc/Tôn giáo": [
                {'cung': 'Mệnh', 'sao': 'Cô Thần'},
                {'cung': 'Mệnh', 'sao': 'Quả Tú'},
                {'cung': 'Mệnh', 'sao': 'Hoa Cái'},
                {'cung': 'Mệnh', 'sao': 'Thiên Không'},
                {'cung': 'Mệnh', 'sao': 'Thiên Cơ', 'tinh_chat': 'Hãm'}, # Often religious
                {'cung': 'Mệnh', 'sao': 'Thiên Lương'},
            ],
             "Đào hoa, đa tình": [
                {'cung': 'Mệnh', 'sao': 'Tham Lang'},
                {'cung': 'Mệnh', 'sao': 'Đào Hoa'},
                {'cung': 'Mệnh', 'sao': 'Hồng Loan'},
                {'cung': 'Mệnh', 'sao': 'Liêm Trinh'},
                {'cung': 'Mệnh', 'sao': 'Thái Âm'}, 
            ],
            "Bướng bỉnh, bảo thủ": [
                {'cung': 'Mệnh', 'sao': 'Vũ Khúc'},
                {'cung': 'Mệnh', 'sao': 'Thất Sát'},
                {'cung': 'Mệnh', 'sao': 'Đà La'},
                {'cung': 'Mệnh', 'sao': 'Cô Thần'},
            ],
            "Thông minh, sắc sảo": [
                {'cung': 'Mệnh', 'sao': 'Thiên Cơ'},
                {'cung': 'Mệnh', 'sao': 'Thái Dương'},
                {'cung': 'Mệnh', 'sao': 'Khôi Việt'}, # Thien Khoi/Thien Viet
                {'cung': 'Mệnh', 'sao': 'Thiên Khôi'},
                {'cung': 'Mệnh', 'sao': 'Thiên Việt'},
                {'cung': 'Mệnh', 'sao': 'Văn Xương'},
                {'cung': 'Mệnh', 'sao': 'Văn Khúc'},
                {'cung': 'Mệnh', 'sao': 'Hóa Khoa'},
            ],
             "Cẩn thận, tỉ mỉ": [
                {'cung': 'Mệnh', 'sao': 'Thiên Lương'},
                {'cung': 'Mệnh', 'sao': 'Lộc Tồn'},
                {'cung': 'Mệnh', 'sao': 'Thiên Cơ'},
            ],

            # --- NGOẠI HÌNH ---
            "Cao lớn": [
                {'cung': 'Mệnh', 'sao': 'Thiên Tướng'}, 
                {'cung': 'Mệnh', 'sao': 'Phá Quân'},
                {'cung': 'Mệnh', 'sao': 'Thiên Lương'},
                {'cung': 'Mệnh', 'sao': 'Thiên Khôi'},
            ],
            "Thấp bé": [
                 {'cung': 'Mệnh', 'sao': 'Thiên Cơ'},
                 {'cung': 'Mệnh', 'sao': 'Vũ Khúc'},
                 {'cung': 'Mệnh', 'sao': 'Thái Âm', 'tinh_chat': 'Hãm'},
            ],
             "Mập, đầy đặn": [
                 {'cung': 'Mệnh', 'sao': 'Thiên Phủ'}, 
                 {'cung': 'Mệnh', 'sao': 'Thái Âm', 'tinh_chat': 'Miếu'}, 
                 {'cung': 'Mệnh', 'sao': 'Thiên Đồng'},
                 {'cung': 'Mệnh', 'sao': 'Tham Lang'},
            ],
             "Gầy, ốm": [
                 {'cung': 'Mệnh', 'sao': 'Thất Sát'},
                 {'cung': 'Mệnh', 'sao': 'Cự Môn'},
                 {'cung': 'Mệnh', 'sao': 'Thiên Cơ'},
                 {'cung': 'Mệnh', 'sao': 'Đà La'},
                 {'cung': 'Mệnh', 'sao': 'Hóa Kỵ'},
            ],
            "Da trắng": [{'cung': 'Mệnh', 'sao': 'Thái Âm'}, {'cung': 'Mệnh', 'sao': 'Thiên Phủ'}, {'cung': 'Mệnh', 'sao': 'Thiên Tướng'}],
            "Da ngăm đen": [{'cung': 'Mệnh', 'sao': 'Thất Sát'}, {'cung': 'Mệnh', 'sao': 'Tham Lang'}, {'cung': 'Mệnh', 'sao': 'Phá Quân'}],
            "Mặt vuông chữ điền": [{'cung': 'Mệnh', 'sao': 'Thất Sát'}, {'cung': 'Mệnh', 'sao': 'Thiên Phủ'}, {'cung': 'Mệnh', 'sao': 'Vũ Khúc'}],
             "Mặt tròn": [{'cung': 'Mệnh', 'sao': 'Thiên Đồng'}, {'cung': 'Mệnh', 'sao': 'Thái Âm'}, {'cung': 'Mệnh', 'sao': 'Tham Lang'}],
             "Mắt cận thị/kém": [{'cung': 'Mệnh', 'sao': 'Thái Dương', 'tinh_chat': 'Hãm'}, {'cung': 'Mệnh', 'sao': 'Đà La'}, {'cung': 'Mệnh', 'sao': 'Hóa Kỵ'}],

            # --- NGHỀ NGHIỆP ---
            "Giáo viên/Giảng dạy": [
                {'cung': 'Quan Lộc', 'sao': 'Thiên Lương'},
                {'cung': 'Quan Lộc', 'sao': 'Cự Môn'},
                {'cung': 'Quan Lộc', 'sao': 'Văn Xương'},
                {'cung': 'Quan Lộc', 'sao': 'Văn Khúc'},
                {'cung': 'Quan Lộc', 'sao': 'Hóa Khoa'},
                 {'cung': 'Mệnh', 'sao': 'Cự Môn'}, # Nói nhiều
            ],
             "Công nghệ thông tin (IT)": [
                {'cung': 'Quan Lộc', 'sao': 'Thiên Cơ'}, # Máy móc
                {'cung': 'Quan Lộc', 'sao': 'Hỏa Tinh'}, # Điện
                {'cung': 'Quan Lộc', 'sao': 'Linh Tinh'}, # Điện
                {'cung': 'Quan Lộc', 'sao': 'Không Kiếp'}, # Sáng tạo đột phá
                 {'cung': 'Mệnh', 'sao': 'Thiên Cơ'},
            ],


            # --- HÔN NHÂN ---
            "Kết hôn muộn (> 30 tuổi)": [
                {'cung': 'Phu Thê', 'sao': 'Cô Thần'},
                {'cung': 'Phu Thê', 'sao': 'Quả Tú'},
                {'cung': 'Phu Thê', 'sao': 'Vũ Khúc'},
                {'cung': 'Phu Thê', 'sao': 'Triệt'},
                {'cung': 'Phu Thê', 'sao': 'Tuần'},
            ],
             "Vợ chồng hay khắc khẩu/bất hòa": [
                {'cung': 'Phu Thê', 'sao': 'Cự Môn'},
                {'cung': 'Phu Thê', 'sao': 'Hóa Kỵ'},
                {'cung': 'Phu Thê', 'sao': 'Phúc Bình'},
            ],
        }

    def get_criteria(self, trait_name):
        """
        Return list of possible criteria for a trait.
        Logic: OR condition. If trait is present, at least ONE of the criteria should ideally be met.
        BUT for 'Finder', we usually treat these as suggestions ("likely has Star X OR Star Y").
        """
        return self.rules.get(trait_name, [])

    def map_event_to_rules(self, event_name, event_year):
        """
        Map event to rules specifically for a year (Lưu Niên/Tiểu Hạn).
        Example: "Kết hôn" -> Check Hỷ sự in year.
        """
        rules = []
        if event_name == "Kết hôn":
            # Check signs of marriage in limit (Tiểu Hạn/Lưu Niên)
            # This is complex, usually involves Checking Phu The, Dao Hoa, Hong Loan...
            pass
        return rules
