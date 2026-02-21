/**
 * form-handler.js - Birth Form & Calendar Logic
 * Xử lý form nhập ngày sinh và gọi API
 */

let isLunar = false;

function setCalendarMode(mode) {
    isLunar = mode === 'lunar';
    document.getElementById('btnSolar').classList.toggle('active', !isLunar);
    document.getElementById('btnLunar').classList.toggle('active', isLunar);
    document.getElementById('leapMonth').classList.toggle('show', isLunar);
    document.getElementById('dayLabel').textContent = isLunar ? 'Ngày (Âm)' : 'Ngày';
    document.getElementById('monthLabel').textContent = isLunar ? 'Tháng (Âm)' : 'Tháng';
}

// Attach Event Listener
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('birthForm');
    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            document.getElementById('loading').classList.add('show');
            document.getElementById('results').classList.remove('show');

            const dayInput = document.getElementById('day').value;
            const hourInput = document.getElementById('hour').value;

            const data = {
                day: dayInput ? parseInt(dayInput) : null,
                month: parseInt(document.getElementById('month').value),
                year: parseInt(document.getElementById('year').value),
                hour: hourInput !== "" ? parseInt(hourInput) : null,
                gender: document.getElementById('gender').value,
                is_lunar: isLunar,
                leap_month: document.getElementById('leapMonthCheck').checked
            };

            try {
                const response = await fetch('/api/generate', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (!response.ok || result.status === 'error' || result.error) {
                    alert('Lỗi: ' + (result.message || result.error || 'Không thể tạo lá số'));
                } else {
                    const chartData = result.data;
                    const interpretation = result.data.interpretation;

                    // Store data for AI
                    window.currentChart = chartData;
                    window.currentInterpretation = interpretation;
                    window.currentTaiMenh = chartData.tai_menh || null;

                    renderChart(chartData);
                    renderInterpretation(interpretation, chartData);
                    document.getElementById('results').classList.add('show');
                    document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
                }
            } catch (error) {
                alert('Lỗi kết nối: ' + error.message);
            } finally {
                document.getElementById('loading').classList.remove('show');
            }
        });
    }
});
