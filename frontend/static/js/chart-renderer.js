/**
 * chart-renderer.js - Tử Vi Chart Rendering
 * Vẽ lá số tử vi 4x4 grid
 */

const DIA_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi'];

// Palace order in grid (reading order: top-left to bottom-right, skipping center)
const GRID_POSITIONS = [
    { pos: 5, row: 1, col: 1 },   // Tỵ
    { pos: 6, row: 1, col: 2 },   // Ngọ
    { pos: 7, row: 1, col: 3 },   // Mùi
    { pos: 8, row: 1, col: 4 },   // Thân
    { pos: 4, row: 2, col: 1 },   // Thìn
    { pos: 9, row: 2, col: 4 },   // Dậu
    { pos: 3, row: 3, col: 1 },   // Mão
    { pos: 10, row: 3, col: 4 },  // Tuất
    { pos: 2, row: 4, col: 1 },   // Dần
    { pos: 1, row: 4, col: 2 },   // Sửu
    { pos: 0, row: 4, col: 3 },   // Tý
    { pos: 11, row: 4, col: 4 }   // Hợi
];

// Main stars that should be highlighted
const MAIN_STARS = [
    'Tử Vi', 'Thiên Cơ', 'Thái Dương', 'Vũ Khúc', 'Thiên Đồng', 'Liêm Trinh',
    'Thiên Phủ', 'Thái Âm', 'Tham Lang', 'Cự Môn', 'Thiên Tướng', 'Thiên Lương',
    'Thất Sát', 'Phá Quân'
];

function getStarBrightness(star, position) {
    const brightPositions = {
        'Tử Vi': [6, 7],
        'Thái Dương': [5, 6, 7],
        'Thái Âm': [9, 10, 11],
        'Thiên Phủ': [1, 2, 3]
    };
    if (brightPositions[star] && brightPositions[star].includes(position)) {
        return 'M'; // Miếu
    }
    return '';
}

function getLifeStage(chiIndex) {
    const stages = ['Đế Vượng', 'Suy', 'Bệnh', 'Tử', 'Mộ', 'Tuyệt', 'Thai', 'Dưỡng', 'Trường Sinh', 'Mộc Dục', 'Quan Đới', 'Lâm Quan'];
    return stages[chiIndex] || '';
}

function renderChart(chartData) {
    const grid = document.getElementById('chartGrid');
    grid.innerHTML = '';

    // Create map for easy lookup
    const palaceMap = {};
    chartData.dia_ban.forEach(p => {
        const chiIndex = DIA_CHI.indexOf(p.dia_chi);
        if (chiIndex !== -1) {
            palaceMap[chiIndex] = p;
        }
    });

    // Create 4x4 grid
    const cells = [];
    for (let i = 0; i < 16; i++) {
        cells.push(null);
    }

    // Place palaces
    GRID_POSITIONS.forEach(gp => {
        const index = (gp.row - 1) * 4 + (gp.col - 1);
        const palaceData = palaceMap[gp.pos];
        if (palaceData) {
            cells[index] = { type: 'palace', data: palaceData, chiIndex: gp.pos };
        }
    });

    // Render cells
    for (let row = 1; row <= 4; row++) {
        for (let col = 1; col <= 4; col++) {
            const index = (row - 1) * 4 + (col - 1);
            // Center panel (2x2)
            if (row === 2 && col === 2) {
                const centerDiv = document.createElement('div');
                centerDiv.className = 'center-info';
                centerDiv.innerHTML = renderCenterInfo(chartData.basic_info, chartData.interpretation);
                grid.appendChild(centerDiv);
                continue;
            }
            if ((row === 2 && col === 3) || (row === 3 && col === 2) || (row === 3 && col === 3)) {
                continue;
            }
            const cell = cells[index];
            if (cell && cell.type === 'palace') {
                grid.appendChild(renderPalace(cell.data, cell.chiIndex));
            }
        }
    }
}

function renderCenterInfo(basicInfo, oldInterp) {
    return `
        <div class="center-title">TỬ VI ĐẨU SỐ</div>
        <div class="info-grid">
            <span class="info-label">Năm:</span>
            <span class="info-value">${basicInfo.can_chi_nam}</span>
            <span class="info-label">Tháng:</span>
            <span class="info-value">${basicInfo.can_chi_thang}</span>
            <span class="info-label">Ngày:</span>
            <span class="info-value">${basicInfo.can_chi_ngay}</span>
            <span class="info-label">Giờ:</span>
            <span class="info-value">${basicInfo.can_chi_gio}</span>
            <span class="info-label">Mệnh Chủ:</span>
            <span class="info-value">${basicInfo.menh_chu_star}</span>
            <span class="info-label">Cục:</span>
            <span class="info-value">${basicInfo.cuc}</span>
            <span class="info-label">Nạp Âm:</span>
            <span class="info-value">${basicInfo.menh_chu}</span>
        </div>
    `;
}

function renderPalace(palaceData, chiIndex) {
    const div = document.createElement('div');
    div.className = 'palace';
    const chi = palaceData.dia_chi;
    const cung = palaceData.cung_name || '';

    const monthNum = ((chiIndex - 2 + 12) % 12) + 1;

    const formatStar = (s, type) => {
        let className = type === 'main' ? 'main-star' : (type === 'good' ? 'aux-star good' : 'aux-star bad');
        if (type === 'main' && ['H', 'Hãm'].includes(s.brightness)) className += ' bad';
        if (s.brightness && s.brightness !== '') className += ` bright-${s.brightness.toLowerCase()}`;

        let label = s.name;
        if (s.brightness) label += ` (${s.brightness})`;

        return `<span class="${className}" style="${s.color ? 'color:' + s.color : ''}">${label}</span>`;
    };

    const mainStarsHtml = (palaceData.chinh_tinh || []).map(s => formatStar(s, 'main')).join('<br>');
    const goodStarsHtml = (palaceData.phu_tinh_tot || []).map(s => formatStar(s, 'good')).join('<br>');
    const badStarsHtml = (palaceData.phu_tinh_xau || []).map(s => formatStar(s, 'bad')).join('<br>');

    let markers = '';
    if (palaceData.is_menh) markers += '<span class="menh-marker">MỆNH</span> ';
    if (palaceData.is_than) markers += '<span class="than-marker">THÂN</span>';
    if (palaceData.tuan) markers += '<span class="tuan-marker">TUẦN</span> ';
    if (palaceData.triet) markers += '<span class="triet-marker">TRIỆT</span>';

    div.innerHTML = `
        <div class="palace-header">
            <span class="palace-code">${chi}</span>
            <span class="palace-name">${cung.toUpperCase()}</span>
        </div>
        <div class="main-stars">${mainStarsHtml}</div>
        ${markers ? `<div style="margin:3px 0">${markers}</div>` : ''}
        <div class="stars-columns">
            <div class="stars-good">${goodStarsHtml}</div>
            <div class="stars-bad">${badStarsHtml}</div>
        </div>
        <div class="palace-footer">
            <span>Tháng ${monthNum}</span>
            <span>${getLifeStage(chiIndex)}</span>
            ${palaceData.tieu_han_age ? `<span class="tieu-han-badge">TH ${palaceData.tieu_han_age}</span>` : ''}
        </div>
    `;
    return div;
}
