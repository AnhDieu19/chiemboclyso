/**
 * analytics.js - Analytics Beauty Report Logic
 * Báo Cáo Phân Tích "Hồng Nhan" (1950 - 2007)
 * 
 * Requires server-side data injected as globals before this script:
 *   currentGender, dataSource, serverFateLabels, serverPieData,
 *   serverBeautySets, serverBarDatasets, serverLineLabels,
 *   serverLineLucky, serverLineTragic, serverLineBeautyRate
 */

// 5 Cấp Độ Hồng Nhan (BA Spec)
const HONG_NHAN_LEVELS = {
    "VERY_HAPPY": { name: "Hồng Nhan Phú Quý", icon: "👑", color: "#4caf50" },
    "HAPPY": { name: "Hồng Nhan Hạnh Phúc", icon: "🌸", color: "#8bc34a" },
    "NEUTRAL": { name: "Hồng Nhan Bình Thường", icon: "⚖️", color: "#ffeb3b" },
    "TRAGIC": { name: "Hồng Nhan Vất Vả", icon: "😔", color: "#ff9800" },
    "VERY_TRAGIC": { name: "Hồng Nhan Bạc Mệnh", icon: "💔", color: "#f44336" }
};

const FATE_LEVELS = ["VERY_HAPPY", "HAPPY", "NEUTRAL", "TRAGIC", "VERY_TRAGIC"];

// Raw Data from Server (for filtering)
const rawPieData = serverPieData || [];
const rawBarDatasets = serverBarDatasets || [];
const rawBeautySets = serverBeautySets || [];
const rawLineLabels = serverLineLabels || [];

// Current Filter State
let currentFilter = {
    set: 'all',
    year: 'all',
    gender: currentGender
};

// Calculate Probabilities
function calculateProbabilities(data) {
    const total = data.reduce((a, b) => a + b, 0);
    const probabilities = {};
    FATE_LEVELS.forEach((level, idx) => {
        probabilities[level] = total > 0 ? (data[idx] / total * 100) : 0;
    });
    return { total, probabilities };
}

// Get Filtered Data
function getFilteredData() {
    let data = [...rawPieData];
    let total = data.reduce((a, b) => a + b, 0);

    if (currentFilter.set !== 'all') {
        const setIndex = rawBeautySets.findIndex(s => {
            const setMap = {
                "DAO_HONG": "Đào Hồng Hỷ",
                "VAN_TINH": "Văn Xương/Khúc",
                "QUYEN_RU": "Tham/Liêm",
                "PHUC_THIEN": "Phủ/Tướng/Âm"
            };
            return s === setMap[currentFilter.set];
        });

        if (setIndex >= 0) {
            data = FATE_LEVELS.map(level => {
                const dataset = rawBarDatasets.find(d => {
                    const levelMap = {
                        "VERY_HAPPY": "Hồng Nhan Phú Quý",
                        "HAPPY": "Hồng Nhan Hạnh Phúc",
                        "NEUTRAL": "Hồng Nhan Bình Thường",
                        "TRAGIC": "Hồng Nhan Vất Vả",
                        "VERY_TRAGIC": "Hồng Nhan Bạc Mệnh"
                    };
                    return d.label === levelMap[level];
                });
                return dataset ? (dataset.data[setIndex] || 0) : 0;
            });
            total = data.reduce((a, b) => a + b, 0);
        }
    }

    return { levels: data, total };
}

// Update Legend
function updateLegend() {
    const { levels, total } = getFilteredData();
    const { probabilities } = calculateProbabilities(levels);
    const container = document.getElementById('legendContainer');

    if (!container) return;

    container.innerHTML = FATE_LEVELS.map(level => {
        const levelInfo = HONG_NHAN_LEVELS[level];
        const count = levels[FATE_LEVELS.indexOf(level)];
        const pct = probabilities[level].toFixed(2);

        return `
            <div style="display: flex; align-items: center; gap: 12px; padding: 12px; background: white; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <span style="font-size: 1.5em;">${levelInfo.icon}</span>
                <div style="width: 24px; height: 24px; border-radius: 4px; background: ${levelInfo.color}; border: 2px solid #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.2);"></div>
                <div style="flex: 1;">
                    <div style="font-weight: bold; color: #2c3e50; font-size: 0.95em;">${levelInfo.name}</div>
                    <div style="font-size: 0.85em; color: #7f8c8d;">
                        ${count.toLocaleString()} mẫu (${pct}%)
                    </div>
                </div>
            </div>
        `;
    }).join('');

    const filterCount = document.getElementById('filterCount');
    if (filterCount) filterCount.textContent = total.toLocaleString();
}

// Apply Filters
function applyFilters() {
    currentFilter.set = document.getElementById('filterSet').value;
    currentFilter.year = document.getElementById('filterYear').value;
    updateCharts();
    updateLegend();

    // If year filter is set, auto-drill to that year in the line chart
    if (currentFilter.year !== 'all' && lineChart) {
        selectedYear = currentFilter.year;
        currentView = 'month';
        const url = `/api/v1/analytics/drilldown?gender=${currentGender}&year=${selectedYear}`;
        document.getElementById('chartTitle').innerText = `Dữ liệu Năm ${selectedYear} (Theo Tháng)`;
        document.getElementById('resetZoomBtn').style.display = 'block';
        updateChartData(url);
    } else if (currentFilter.year === 'all' && lineChart) {
        // Reset drill down when year filter is cleared
        resetDrillDown();
    }
}

// Reset Filters
function resetFilters() {
    document.getElementById('filterSet').value = 'all';
    document.getElementById('filterYear').value = 'all';
    currentFilter.set = 'all';
    currentFilter.year = 'all';
    updateCharts();
    updateLegend();
}

// Update Charts with Filtered Data
function updateCharts() {
    const { levels } = getFilteredData();

    if (typeof pieChart !== 'undefined' && pieChart) {
        pieChart.data.datasets[0].data = levels;
        pieChart.update();
    }
}

function applyFilter() {
    const gender = document.getElementById('genderFilter').value;
    window.location.href = `/analytics/beauty?gender=${gender}`;
}

// --- Drill Down State ---
let currentView = 'year';
let selectedYear = null;
let selectedMonth = null;

// Common Tooltip Config
const tooltipOptions = {
    callbacks: {
        label: function (context) {
            let label = context.dataset.label || '';
            if (label) { label += ': '; }
            if (context.parsed.y !== null) { label += context.parsed.y + '%'; }
            return label;
        }
    }
};

// --- Chart Initialization ---
// These are called conditionally based on data source

let pieChart = null;
let lineChart = null;

function initCsvCharts() {
    // Pie Chart
    pieChart = new Chart(document.getElementById('pieChart').getContext('2d'), {
        type: 'doughnut',
        data: {
            labels: serverFateLabels,
            datasets: [{
                data: serverPieData,
                backgroundColor: ['#4caf50', '#8bc34a', '#ffeb3b', '#ff9800', '#f44336']
            }]
        },
        options: {
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const label = context.label || '';
                            const value = context.parsed || 0;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = total > 0 ? ((value / total) * 100).toFixed(2) : 0;
                            return `${label}: ${value.toLocaleString()} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });

    // Legend
    if (document.getElementById('legendContainer')) {
        updateLegend();
    }

    // Bar Chart
    new Chart(document.getElementById('barChart').getContext('2d'), {
        type: 'bar',
        data: { labels: serverBeautySets, datasets: serverBarDatasets },
        options: { scales: { x: { stacked: true }, y: { stacked: true } } }
    });

    // Line Chart (Drill Down)
    const ctxLine = document.getElementById('lineChart').getContext('2d');
    lineChart = new Chart(ctxLine, {
        type: 'line',
        data: {
            labels: serverLineLabels,
            datasets: [
                { label: 'Tỷ lệ Sướng (%)', data: serverLineLucky, borderColor: '#4caf50', tension: 0.3 },
                { label: 'Tỷ lệ Khổ (%)', data: serverLineTragic, borderColor: '#f44336', tension: 0.3 }
            ]
        },
        options: {
            onClick: (e) => {
                const points = lineChart.getElementsAtEventForMode(e, 'nearest', { intersect: true }, true);
                if (points.length) {
                    const firstPoint = points[0];
                    const label = lineChart.data.labels[firstPoint.index];
                    handleDrillDown(label);
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        footer: (tooltipItems) => {
                            return 'Click để xem chi tiết...';
                        }
                    }
                }
            }
        }
    });
}

// Beauty Rate Chart (always shown)
function initBeautyRateChart() {
    new Chart(document.getElementById('beautyRateChart').getContext('2d'), {
        type: 'line',
        data: {
            labels: serverLineLabels,
            datasets: [{
                label: 'Tỷ lệ Nhan Sắc (%)',
                data: serverLineBeautyRate,
                borderColor: '#9c27b0',
                backgroundColor: 'rgba(156, 39, 176, 0.1)',
                fill: true, tension: 0.4
            }]
        }
    });
}

// Count Chart (optional)
function initCountChart(countData) {
    new Chart(document.getElementById('countChart').getContext('2d'), {
        type: 'bar',
        data: {
            labels: serverLineLabels,
            datasets: [{
                label: 'Số Hồng Nhan',
                data: countData,
                backgroundColor: '#e91e63',
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (context) => {
                            return `Số lượng: ${context.parsed.y.toLocaleString()}`;
                        }
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            return value.toLocaleString();
                        }
                    }
                }
            }
        }
    });
}

// --- Drill Down Functions ---
async function handleDrillDown(label) {
    let url = `/api/v1/analytics/drilldown?gender=${currentGender}`;

    if (currentView === 'year') {
        selectedYear = label;
        currentView = 'month';
        url += `&year=${selectedYear}`;
        document.getElementById('chartTitle').innerText = `Dữ liệu Năm ${selectedYear} (Theo Tháng)`;
        document.getElementById('resetZoomBtn').style.display = 'block';
    } else if (currentView === 'month') {
        selectedMonth = label;
        currentView = 'day';
        url += `&year=${selectedYear}&month=${selectedMonth}`;
        document.getElementById('chartTitle').innerText = `Dữ liệu Tháng ${selectedMonth}/${selectedYear} (Theo Ngày)`;
    } else {
        return;
    }
    await updateChartData(url);
}

async function resetDrillDown() {
    currentView = 'year';
    selectedYear = null;
    selectedMonth = null;
    document.getElementById('chartTitle').innerText = "Dữ liệu theo Năm (Click vào điểm để xem chi tiết)";
    document.getElementById('resetZoomBtn').style.display = 'none';
    let url = `/api/v1/analytics/drilldown?gender=${currentGender}`;
    await updateChartData(url);
}

async function updateChartData(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        lineChart.data.labels = data.labels;
        lineChart.data.datasets[0].data = data.lucky;
        lineChart.data.datasets[1].data = data.tragic;
        lineChart.update();
    } catch (error) {
        console.error("Error fetching drilldown data:", error);
    }
}
