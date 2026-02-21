/**
 * Tu Vi Knowledge Graph - Star Name Mapping Module
 * Mapping từ tên sao API (không dấu) sang tên hiển thị (có dấu)
 */

// ═══════════════════════════════════════════════════════════════════════════
// STAR NAME MAPPING (API không dấu -> Graph có dấu)
// ═══════════════════════════════════════════════════════════════════════════
const STAR_NAME_MAP = {
    // Chính tinh - Vòng Tử Vi
    'Tu Vi': 'Tử Vi',
    'Thien Co': 'Thiên Cơ',
    'Thai Duong': 'Thái Dương',
    'Vu Khuc': 'Vũ Khúc',
    'Thien Dong': 'Thiên Đồng',
    'Liem Trinh': 'Liêm Trinh',
    // Chính tinh - Vòng Thiên Phủ
    'Thien Phu': 'Thiên Phủ',
    'Thai Am': 'Thái Âm',
    'Tham Lang': 'Tham Lang',
    'Cu Mon': 'Cự Môn',
    'Thien Tuong': 'Thiên Tướng',
    'Thien Luong': 'Thiên Lương',
    'That Sat': 'Thất Sát',
    'Pha Quan': 'Phá Quân',
    // Lục Cát
    'Ta Phu': 'Tả Phụ',
    'Huu Bat': 'Hữu Bật',
    'Van Xuong': 'Văn Xương',
    'Van Khuc': 'Văn Khúc',
    'Thien Khoi': 'Thiên Khôi',
    'Thien Viet': 'Thiên Việt',
    // Lục Sát
    'Kinh Duong': 'Kinh Dương',
    'Da La': 'Đà La',
    'Hoa Tinh': 'Hỏa Tinh',
    'Linh Tinh': 'Linh Tinh',
    'Dia Khong': 'Địa Không',
    'Dia Kiep': 'Địa Kiếp',
    // Tứ Hóa
    'Hoa Loc': 'Hóa Lộc',
    'Hoa Quyen': 'Hóa Quyền',
    'Hoa Khoa': 'Hóa Khoa',
    'Hoa Ky': 'Hóa Kỵ',
    // Tạp tinh quan trọng
    'Loc Ton': 'Lộc Tồn',
    'Thien Ma': 'Thiên Mã',
    'Dao Hoa': 'Đào Hoa',
    'Hong Loan': 'Hồng Loan',
    'Thien Hy': 'Thiên Hỹ',
    'Thien Hinh': 'Thiên Hình',
    'Thien Rieu': 'Thiên Riêu',
    'Co Than': 'Cô Thần',
    'Qua Tu': 'Quả Tú',
    'Thien Khong': 'Thiên Không',
    'Kiep Sat': 'Kiếp Sát',
    'Pha Toai': 'Phá Toái',
    'Hoa Cai': 'Hoa Cái',
    'Tuan': 'Tuần',
    'Triet': 'Triệt',
    // Vòng Thái Tuế
    'Thai Tue': 'Thái Tuế',
    'Thieu Duong': 'Thiếu Dương',
    'Tang Mon': 'Tang Môn',
    'Thieu Am': 'Thiếu Âm',
    'Quan Phu': 'Quan Phù',
    'Tu Phu': 'Từ Phù',
    'Tue Pha': 'Tuế Phá',
    'Long Duc': 'Long Đức',
    'Bach Ho': 'Bạch Hổ',
    'Phuc Duc': 'Phúc Đức',
    'Dieu Khach': 'Điếu Khách',
    'Truc Phu': 'Trực Phù',
    // Vòng Trường Sinh
    'Truong Sinh': 'Trường Sinh',
    'Moc Duc': 'Mộc Dục',
    'Quan Doi': 'Quan Đới',
    'Lam Quan': 'Lâm Quan',
    'De Vuong': 'Đế Vượng',
    'Suy': 'Suy',
    'Benh': 'Bệnh',
    'Tu': 'Tử',
    'Mo': 'Mộ',
    'Tuyet': 'Tuyệt',
    'Thai': 'Thai',
    'Duong': 'Dưỡng',
    // Vòng Bác Sĩ
    'Bac Si': 'Bác Sĩ',
    'Luc Si': 'Lực Sĩ',
    'Thanh Long': 'Thanh Long',
    'Tieu Hao': 'Tiểu Hao',
    'Tuong Quan': 'Tướng Quân',
    'Tau Thu': 'Tàu Thu',
    'Phi Liem': 'Phi Liêm',
    'Hy Than': 'Hỷ Thần',
    'Benh Phu': 'Bệnh Phù',
    'Dai Hao': 'Đại Hao',
    'Phuc Binh': 'Phúc Bình',
    'Quan Phu2': 'Quan Phủ',
    // Sao khác
    'An Quang': 'Ân Quang',
    'Thien Quy': 'Thiên Quý',
    'Thien Quan': 'Thiên Quan',
    'Thien Phuc': 'Thiên Phúc',
    'Thien Duc': 'Thiên Đức',
    'Nguyet Duc': 'Nguyệt Đức',
    'Long Tri': 'Long Trì',
    'Phuong Cac': 'Phượng Các',
    'Thai Phu': 'Thái Phụ',
    'Phong Cao': 'Phong Cáo',
    'Quan Doi2': 'Quan Đới',
    'Hoa Cai2': 'Hoa Cái',
    'Giap Quan': 'Giáp Quân',
    'Giap Khong': 'Giáp Không',
    'Kiem Khong': 'Kiếm Không',
    // Thêm các sao còn thiếu
    'Thien La': 'Thiên La',
    'Dia Vong': 'Địa Võng',
    'Thien Thuong': 'Thiên Thường',
    'Thien Su': 'Thiên Sứ',
    'Thien Giai': 'Thiên Giải',
    'Dia Giai': 'Địa Giải',
    'Thien Tai': 'Thiên Tài',
    'Thien Tho': 'Thiên Thọ',
    'Tam Thai': 'Tam Thai',
    'Bat Toa': 'Bát Tọa',
    'Thien Khoc': 'Thiên Khốc',
    'Thien Hu': 'Thiên Hư',
    'Thien Y': 'Thiên Y',
    'Bac Sy': 'Bác Sĩ',
    'Luc Sy': 'Lục Sĩ',
};

/**
 * Normalize star name for matching (API -> Graph)
 * @param {string} name - Tên sao từ API (không dấu)
 * @returns {string} - Tên sao hiển thị (có dấu)
 */
function normalizeStarName(name) {
    if (!name) return '';
    if (STAR_NAME_MAP[name]) return STAR_NAME_MAP[name];
    return name;
}

// Export to global scope
window.STAR_NAME_MAP = STAR_NAME_MAP;
window.normalizeStarName = normalizeStarName;
