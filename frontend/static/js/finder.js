/**
 * finder.js - Finder Page Logic
 * Công cụ tìm giờ sinh (Reverse Lookup) - Slot Machine UI
 */

// --- GLOBAL STATE ---
let globalCandidates = [];
let currentYear = 0;
let currentMonth = 0;
let currentDay = 0;
let currentHour = 0;
const GIO_CHI = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi'];
const GIO_RANGE = [
    '23h - 1h', '1h - 3h', '3h - 5h', '5h - 7h', '7h - 9h', '9h - 11h',
    '11h - 13h', '13h - 15h', '15h - 17h', '17h - 19h', '19h - 21h', '21h - 23h'
];

// --- PRE-DEFINED DEFAULTS FOR TESTING ---
const DEFAULT_TRAITS = [
    'Đa nghi, hay soi xét', 'Đào hoa, đa tình',
    'Hào phóng, rộng lượng', 'Thích cô độc/Tôn giáo', 'Thông minh, sắc sảo',
    'Công nghệ thông tin (IT)',
    'Cao lớn', 'Gầy, ốm'
];

// Will be populated from template
let EVENT_OPTIONS = [];

// --- INIT ---
document.addEventListener('DOMContentLoaded', function () {
    // Toggle Calendar Labels
    const chkSolar = document.getElementById('isSolar');
    if (chkSolar) {
        chkSolar.addEventListener('change', function () {
            const isSolar = this.checked;
            document.getElementById('lblMonth').textContent = isSolar ? 'Tháng (DL)' : 'Tháng (ÂL)';
            document.getElementById('lblDay').textContent = isSolar ? 'Ngày (DL)' : 'Ngày (ÂL)';
        });
    }

    // Init Choices.js
    const selects = document.querySelectorAll('.trait-select');
    selects.forEach(select => {
        const choices = new Choices(select, {
            removeItemButton: true,
            placeholder: true,
            placeholderValue: 'Chọn...',
            searchPlaceholderValue: 'Tìm kiếm...',
        });

        const options = Array.from(select.options).map(o => o.value);
        const toSelect = DEFAULT_TRAITS.filter(t => options.includes(t));
        if (toSelect.length > 0) choices.setChoiceByValue(toSelect);
    });

    // Init Events
    document.getElementById('btnAddEvent').addEventListener('click', () => addEventRow());
});

function addEventRow(type = '', year = '') {
    const container = document.getElementById('eventsContainer');
    const rowId = 'evt_' + Date.now();

    const div = document.createElement('div');
    div.className = 'input-group mb-2';
    div.id = rowId;

    let optionsHtml = '<option value="">Chọn sự kiện...</option>';
    EVENT_OPTIONS.forEach(opt => {
        const selected = (opt === type) ? 'selected' : '';
        optionsHtml += `<option value="${opt}" ${selected}>${opt}</option>`;
    });

    div.innerHTML = `
        <select class="form-select form-select-sm event-type">
            ${optionsHtml}
        </select>
        <input type="number" class="form-control form-control-sm event-year" placeholder="Năm (DL)" value="${year}" style="max-width: 80px;">
        <button type="button" class="btn btn-outline-danger btn-sm" onclick="removeEventRow('${rowId}')">✕</button>
    `;

    container.appendChild(div);
}

function removeEventRow(rowId) {
    document.getElementById(rowId).remove();
}

// --- FORM SUBMIT ---
document.getElementById('finderForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    const btn = document.getElementById('btnSearch');
    btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Loading...';
    btn.disabled = true;

    try {
        const traitSelects = document.querySelectorAll('.trait-select');
        let selectedTraits = [];
        traitSelects.forEach(select => Array.from(select.selectedOptions).forEach(opt => selectedTraits.push(opt.value)));

        let events = [];
        document.querySelectorAll('#eventsContainer .input-group').forEach(row => {
            const type = row.querySelector('.event-type').value;
            const year = row.querySelector('.event-year').value;
            if (type && year) {
                events.push({ type: type, year: parseInt(year) });
            }
        });

        const payload = {
            year: document.getElementById('year').value,
            month: document.getElementById('month').value || null,
            day: document.getElementById('day').value || null,
            gender: document.getElementById('gender').value,
            calendar_type: document.getElementById('isSolar').checked ? 'solar' : 'lunar',
            known_hour: document.getElementById('birthHour').value,
            traits: selectedTraits,
            events: events
        };

        console.log("Sending Payload:", payload);

        const response = await fetch('/api/finder/solve', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const result = await response.json();

        if (result.success) {
            renderLeaderboard(result.candidates);

            if (result.top_timeline) {
                renderLifeChart(result.top_timeline);
            }

            document.getElementById('resultCount').textContent = `${result.total} permutations`;
            initSlotMachine(result.all_candidates || result.candidates, payload);
        } else {
            alert('Lỗi: ' + (result.error || 'Unknown error'));
        }

    } catch (err) {
        console.error(err);
        alert('Connection Error');
    } finally {
        btn.innerHTML = '🚀 Tìm Kiếm Lá Số';
        btn.disabled = false;
    }
});

// --- CHART JS ---
let lifeChartInstance = null;

function renderLifeChart(timelineData) {
    const ctx = document.getElementById('lifeChart').getContext('2d');

    const labels = timelineData.map(t => `${t.year} (${t.age})`);
    const scores = timelineData.map(t => t.score);

    if (lifeChartInstance) lifeChartInstance.destroy();

    lifeChartInstance = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Vận Khí',
                data: scores,
                borderColor: '#4299e1',
                backgroundColor: 'rgba(66, 153, 225, 0.1)',
                tension: 0.4,
                fill: true,
                pointRadius: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: { beginAtZero: true, max: 100 }
            },
            plugins: {
                legend: { display: false }
            }
        }
    });
}

function renderLeaderboard(candidates) {
    const sorted = [...candidates].sort((a, b) => b.success_info.score - a.success_info.score).slice(0, 3);

    const container = document.getElementById('topRankContainer');
    container.innerHTML = '';

    document.getElementById('leaderboardSection').style.display = 'block';

    const medals = ['🥇', '🥈', '🥉'];

    sorted.forEach((c, idx) => {
        const day = c.date.day;

        const col = document.createElement('div');
        col.className = 'col-md-4';
        col.innerHTML = `
            <div class="rank-card text-center">
                <div class="gold-trophy">${medals[idx]}</div>
                <h6 class="fw-bold my-2">Ngày ${day} - ${GIO_CHI[c.date.hour]}</h6>
                <span class="archetype-badge mb-2">${c.success_info.archetype}</span>
                <div class="text-muted small">Điểm Cách Cục: <b class="text-dark">${c.success_info.score}</b></div>
            </div>
        `;
        container.appendChild(col);
    });
}


// --- SLOT MACHINE LOGIC ---

function initSlotMachine(candidates, input) {
    resetBestFitState();

    globalCandidates = {};
    const dayScores = {};

    candidates.forEach(c => {
        const day = c.date.day;
        const hour = c.date.hour;
        const score = c.match_info.score;

        if (!globalCandidates[day]) globalCandidates[day] = {};
        globalCandidates[day][hour] = c;

        if (!dayScores[day] || score > dayScores[day]) {
            dayScores[day] = score;
        }
    });

    if (candidates && candidates.length > 0) {
        currentYear = candidates[0].date.year;
        currentMonth = candidates[0].date.month;
    } else {
        currentYear = parseInt(input.year);
        currentMonth = 1;
    }

    const availableDays = Object.keys(globalCandidates).map(d => parseInt(d)).sort((a, b) => a - b);
    currentDay = availableDays[0];

    let initialHour = 0;
    if (input.known_hour && input.known_hour != -1) {
        initialHour = parseInt(input.known_hour);
    }
    currentHour = initialHour;

    // Setup UI
    document.getElementById('initialState').style.display = 'none';
    document.getElementById('slotMachine').style.display = 'flex';
    document.getElementById('btnAutoSnap').style.display = 'inline-block';

    // Render Reels
    renderReel('reelYear', [currentYear]);
    renderReel('reelMonth', [currentMonth]);

    const dayItems = availableDays.map(d => {
        const maxScore = dayScores[d] || 0;
        let dotClass = 'dot-grey';
        if (maxScore >= 100) dotClass = 'dot-green';
        else if (maxScore >= 50) dotClass = 'dot-yellow';

        return {
            value: d,
            label: `Ngày ${d}`,
            html: `Ngày ${d} <span class="heat-dot ${dotClass}"></span>`
        };
    });
    renderReel('reelDay', dayItems, true);

    updateHourReel(currentDay);

    // Attach Listeners
    attachScrollListener('reelDay', (val) => {
        currentDay = parseInt(val);
        updateHourReel(currentDay);
    });

    attachScrollListener('reelHour', (val) => {
        currentHour = parseInt(val);
        updateResultPanel();
    });

    setTimeout(() => {
        scrollToItem('reelDay', currentDay);
        scrollToItem('reelHour', currentHour);
    }, 100);

    document.getElementById('btnAutoSnap').onclick = () => autoSnapBestFit(dayScores);
}

function renderReel(reelId, items, isComplex = false) {
    const reel = document.getElementById(reelId);
    const spacers = reel.querySelectorAll('.reel-spacer');
    const topSpacer = spacers[0] ? spacers[0].cloneNode(true) : document.createElement('div');
    const bottomSpacer = spacers[1] ? spacers[1].cloneNode(true) : document.createElement('div');
    if (!spacers[0]) topSpacer.className = 'reel-spacer';
    if (!spacers[1]) bottomSpacer.className = 'reel-spacer';
    reel.innerHTML = '';
    reel.appendChild(topSpacer);

    items.forEach(item => {
        const div = document.createElement('div');
        div.className = 'reel-item';
        let val = item;
        if (isComplex) {
            div.dataset.value = item.value;
            div.innerHTML = item.html;
            val = item.value;
        } else {
            div.dataset.value = item;
            div.textContent = item;
        }

        div.onclick = function () {
            scrollToItem(reelId, val);
        };

        reel.appendChild(div);
    });

    reel.appendChild(bottomSpacer);
}

function updateHourReel(day) {
    const candidatesOfDay = globalCandidates[day] || {};
    const hourItems = [];

    for (let h = 0; h < 12; h++) {
        const c = candidatesOfDay[h];
        const score = c ? c.match_info.score : 0;
        let dotClass = 'dot-grey';
        if (score >= 100) dotClass = 'dot-green';
        else if (score >= 50) dotClass = 'dot-yellow';

        hourItems.push({
            value: h,
            html: `${GIO_CHI[h]} <small class="text-muted" style="font-size:0.8em">(${GIO_RANGE[h]})</small> <span class="heat-dot ${dotClass}"></span>`
        });
    }

    renderReel('reelHour', hourItems, true);

    attachScrollListener('reelHour', (val) => {
        currentHour = parseInt(val);
        updateResultPanel();
    });

    scrollToItem('reelHour', currentHour);
    updateResultPanel();
}

function updateResultPanel() {
    const dayData = globalCandidates[currentDay];
    const candidate = dayData ? dayData[currentHour] : null;

    const scoreDisplay = document.getElementById('scoreDisplay');
    const menhContent = document.getElementById('menhContent');
    const detailsList = document.getElementById('matchDetailsList');

    if (!candidate) {
        console.warn("UpdateResultPanel: MISSING CANDIDATE", { currentDay, currentHour, dayDataKeys: dayData ? Object.keys(dayData) : 'No Day Data' });
        scoreDisplay.textContent = "N/A";
        menhContent.textContent = "-";
        detailsList.innerHTML = '<li class="list-group-item text-muted">Không có dữ liệu</li>';
        return;
    } else {
        console.log("UpdateResultPanel: FOUND", { day: currentDay, hour: currentHour, score: candidate.match_info.score });
    }

    const score = candidate.match_info.score;
    scoreDisplay.textContent = score;
    if (score >= 100) scoreDisplay.style.color = '#48bb78';
    else if (score >= 50) scoreDisplay.style.color = '#ecc94b';
    else scoreDisplay.style.color = '#718096';

    const summary = candidate.chart_summary;
    menhContent.innerHTML = `Tại <b>${summary.menh_at}</b> <br> Sao: ${summary.menh_chinh_tinh.join(', ')}`;

    if (candidate.success_info) {
        const s = candidate.success_info;
        menhContent.innerHTML += `<br><div class="mt-2 pt-2 border-top"><span class="badge bg-info text-dark">${s.archetype}</span> <small>Điểm số: ${s.score}</small></div>`;
    }

    const details = candidate.match_info?.details || {};
    let html = '';
    for (const [key, val] of Object.entries(details)) {
        html += `<li class="list-group-item">
            <strong>${key}</strong>
            <ul class="mb-0 ps-3 small text-muted" style="list-style-type:square">
                ${val.map(v => `<li>${v}</li>`).join('')}
            </ul>
        </li>`;
    }
    if (!html) html = '<li class="list-group-item text-muted">Không có tiêu chí nào khớp.</li>';
    detailsList.innerHTML = html;
}

// --- SCROLL HELPERS ---

function attachScrollListener(reelId, callback) {
    const reel = document.getElementById(reelId);
    let timeout;

    reel.onscroll = () => {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            const center = reel.scrollTop + reel.clientHeight / 2;
            const items = reel.querySelectorAll('.reel-item');
            let closest = null;
            let minDiff = 9999;

            items.forEach(item => {
                const itemCenter = item.offsetTop + item.clientHeight / 2;
                const diff = Math.abs(center - itemCenter);

                item.classList.remove('active');

                if (diff < minDiff) {
                    minDiff = diff;
                    closest = item;
                }
            });

            if (closest) {
                closest.classList.add('active');
                const val = closest.dataset.value;
                if (val !== undefined) callback(val);
            }
        }, 100);
    };
}

function scrollToItem(reelId, value) {
    const reel = document.getElementById(reelId);
    const item = Array.from(reel.querySelectorAll('.reel-item')).find(i => i.dataset.value == value);
    if (item) {
        reel.scrollTo({
            top: item.offsetTop - 175,
            behavior: 'smooth'
        });
    }
}

// --- BEST FIT ---
let bestFitCandidates = [];
let bestFitIndex = -1;

function autoSnapBestFit(dayScores) {
    if (bestFitCandidates.length === 0) {
        let globalMax = -1;
        Object.values(dayScores).forEach(s => {
            if (s > globalMax) globalMax = s;
        });

        if (globalMax <= 0) {
            alert("Không có kết quả khớp nào đáng kể.");
            return;
        }

        Object.keys(globalCandidates).forEach(d => {
            const dayVal = parseInt(d);
            const hoursObj = globalCandidates[dayVal];
            for (let h = 0; h < 12; h++) {
                if (hoursObj[h] && hoursObj[h].match_info.score === globalMax) {
                    bestFitCandidates.push({ day: dayVal, hour: h });
                }
            }
        });

        bestFitCandidates.sort((a, b) => {
            if (a.day !== b.day) return a.day - b.day;
            return a.hour - b.hour;
        });

        bestFitIndex = -1;
    }

    if (bestFitCandidates.length === 0) return;

    bestFitIndex = (bestFitIndex + 1) % bestFitCandidates.length;
    const target = bestFitCandidates[bestFitIndex];

    const btn = document.getElementById('btnAutoSnap');
    btn.innerHTML = `⚡ Tìm khớp nhất (${bestFitIndex + 1}/${bestFitCandidates.length})`;

    scrollToItem('reelDay', target.day);
    currentDay = target.day;
    updateHourReel(target.day);

    setTimeout(() => {
        scrollToItem('reelHour', target.hour);
    }, 500);
}

function resetBestFitState() {
    bestFitCandidates = [];
    bestFitIndex = -1;
    const btn = document.getElementById('btnAutoSnap');
    if (btn) btn.innerHTML = `⚡ Tìm khớp nhất (Best Fit)`;
}
