/**
 * Tu Vi Knowledge Graph - Playback Module
 * Playback state và các hàm điều khiển playback
 */

// ═══════════════════════════════════════════════════════════════════════════
// PLAYBACK STATE
// ═══════════════════════════════════════════════════════════════════════════

const CHI_HOUR_NAMES = ['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi'];

let playbackState = {
    isPlaying: false,
    intervalId: null,
    currentDate: { year: 1950, month: 1, day: 1, hour: 0 },
    startDate: { year: 1950, month: 1, day: 1, hour: 0 },
    endDate: { year: 2000, month: 12, day: 31, hour: 11 },
    stepAmount: 1,     // số lượng
    stepUnit: 'hour',  // đơn vị: hour, day, week, month, year, decade, cycle
    speed: 3, // 1-10
    totalSteps: 0,
    currentStep: 0
};

// ═══════════════════════════════════════════════════════════════════════════
// QUICK STEP PRESET
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Set quick step preset
 */
function setQuickStep(amount, unit) {
    document.getElementById('step-amount').value = amount;
    document.getElementById('step-unit').value = unit;
    playbackState.stepAmount = amount;
    playbackState.stepUnit = unit;

    // Update active button
    document.querySelectorAll('.quick-step-buttons button').forEach(btn => {
        btn.classList.remove('active');
    });
    event.target.classList.add('active');

    // Recalculate total steps
    playbackState.totalSteps = calculateTotalSteps();
}

// ═══════════════════════════════════════════════════════════════════════════
// TIME CALCULATION FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Calculate total steps based on step amount and unit
 */
function calculateTotalSteps() {
    const start = playbackState.startDate;
    const end = playbackState.endDate;
    const amount = playbackState.stepAmount;
    const unit = playbackState.stepUnit;

    // Calculate total time span
    const startDate = new Date(start.year, start.month - 1, start.day);
    const endDate = new Date(end.year, end.month - 1, end.day);
    const totalDays = Math.floor((endDate - startDate) / (1000 * 60 * 60 * 24));

    switch (unit) {
        case 'hour':
            return Math.floor((totalDays * 12) / amount);
        case 'day':
            return Math.floor(totalDays / amount);
        case 'week':
            return Math.floor(totalDays / (7 * amount));
        case 'month':
            const totalMonths = (end.year - start.year) * 12 + (end.month - start.month);
            return Math.floor(totalMonths / amount);
        case 'year':
            return Math.floor((end.year - start.year) / amount);
        case 'decade':
            return Math.floor((end.year - start.year) / (10 * amount));
        case 'cycle':
            return Math.floor((end.year - start.year) / (60 * amount));
        default:
            return 1;
    }
}

/**
 * Get days in month
 */
function getDaysInMonth(year, month) {
    return new Date(year, month, 0).getDate();
}

// ═══════════════════════════════════════════════════════════════════════════
// TIME ADVANCE/REWIND FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Advance time by one step based on stepAmount and stepUnit
 */
function advanceTime() {
    const current = playbackState.currentDate;
    const amount = playbackState.stepAmount;
    const unit = playbackState.stepUnit;

    switch (unit) {
        case 'hour':
            for (let i = 0; i < amount; i++) {
                current.hour++;
                if (current.hour > 11) {
                    current.hour = 0;
                    advanceDay();
                }
            }
            break;
        case 'day':
            for (let i = 0; i < amount; i++) {
                advanceDay();
            }
            break;
        case 'week':
            for (let i = 0; i < amount * 7; i++) {
                advanceDay();
            }
            break;
        case 'month':
            for (let i = 0; i < amount; i++) {
                current.month++;
                if (current.month > 12) {
                    current.month = 1;
                    current.year++;
                }
            }
            break;
        case 'year':
            current.year += amount;
            break;
        case 'decade':
            current.year += amount * 10;
            break;
        case 'cycle':
            current.year += amount * 60;
            break;
    }

    playbackState.currentStep++;
}

function advanceDay() {
    const current = playbackState.currentDate;
    current.day++;
    const daysInMonth = getDaysInMonth(current.year, current.month);
    if (current.day > daysInMonth) {
        current.day = 1;
        current.month++;
        if (current.month > 12) {
            current.month = 1;
            current.year++;
        }
    }
}

/**
 * Go back one step
 */
function rewindTime() {
    const current = playbackState.currentDate;
    const amount = playbackState.stepAmount;
    const unit = playbackState.stepUnit;

    switch (unit) {
        case 'hour':
            for (let i = 0; i < amount; i++) {
                current.hour--;
                if (current.hour < 0) {
                    current.hour = 11;
                    rewindDay();
                }
            }
            break;
        case 'day':
            for (let i = 0; i < amount; i++) {
                rewindDay();
            }
            break;
        case 'week':
            for (let i = 0; i < amount * 7; i++) {
                rewindDay();
            }
            break;
        case 'month':
            for (let i = 0; i < amount; i++) {
                current.month--;
                if (current.month < 1) {
                    current.month = 12;
                    current.year--;
                }
            }
            break;
        case 'year':
            current.year -= amount;
            break;
        case 'decade':
            current.year -= amount * 10;
            break;
        case 'cycle':
            current.year -= amount * 60;
            break;
    }

    playbackState.currentStep = Math.max(0, playbackState.currentStep - 1);
}

function rewindDay() {
    const current = playbackState.currentDate;
    current.day--;
    if (current.day < 1) {
        current.month--;
        if (current.month < 1) {
            current.month = 12;
            current.year--;
        }
        current.day = getDaysInMonth(current.year, current.month);
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// BOUNDARY CHECK FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Check if reached end
 */
function hasReachedEnd() {
    const current = playbackState.currentDate;
    const end = playbackState.endDate;
    const unit = playbackState.stepUnit;

    if (current.year > end.year) return true;
    if (current.year < end.year) return false;

    // For year-based units (year, decade, cycle)
    if (unit === 'year' || unit === 'decade' || unit === 'cycle') {
        return current.year >= end.year;
    }

    if (current.month > end.month) return true;
    if (current.month < end.month) return false;

    if (unit === 'month') return current.month >= end.month;

    if (current.day > end.day) return true;
    if (current.day < end.day) return false;

    if (unit === 'day' || unit === 'week') return current.day >= end.day;

    return current.hour >= end.hour;
}

/**
 * Check if at start
 */
function isAtStart() {
    const current = playbackState.currentDate;
    const start = playbackState.startDate;

    return current.year <= start.year &&
        current.month <= start.month &&
        current.day <= start.day &&
        current.hour <= start.hour;
}

// ═══════════════════════════════════════════════════════════════════════════
// DISPLAY UPDATE FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Update display
 */
function updatePlaybackDisplay() {
    const current = playbackState.currentDate;
    const dateStr = `${String(current.day).padStart(2, '0')}/${String(current.month).padStart(2, '0')}/${current.year}`;
    const hourStr = CHI_HOUR_NAMES[current.hour];

    document.getElementById('current-datetime').textContent = `${dateStr} - Giờ ${hourStr}`;

    // Update progress bar
    const progress = playbackState.totalSteps > 0 ?
        (playbackState.currentStep / playbackState.totalSteps) * 100 : 0;
    document.getElementById('progress-bar').style.width = `${progress}%`;
}

// ═══════════════════════════════════════════════════════════════════════════
// API FETCH FUNCTION
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Fetch chart for current time
 */
async function fetchChartForCurrentTime() {
    const current = playbackState.currentDate;
    const gender = document.getElementById('graph-gender').value;

    try {
        const response = await fetch('/graph/api/chart', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                day: current.day,
                month: current.month,
                year: current.year,
                hour: current.hour,
                gender: gender,
                calendar: 'solar',
                leap_month: false
            })
        });

        const result = await response.json();

        if (result.status === 'success') {
            window.currentChartData = result.data;
            if (window.updateChartPositions) {
                window.updateChartPositions(result.data);
            }
        }
    } catch (error) {
        console.error('Playback fetch error:', error);
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// PLAYBACK CONTROL FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Playback tick
 */
async function playbackTick() {
    if (!playbackState.isPlaying) return;

    if (hasReachedEnd()) {
        stopPlayback();
        return;
    }

    advanceTime();
    updatePlaybackDisplay();
    await fetchChartForCurrentTime();
}

/**
 * Toggle playback
 */
function togglePlayback() {
    if (playbackState.isPlaying) {
        pausePlayback();
    } else {
        startPlayback();
    }
}

/**
 * Start playback
 */
function startPlayback() {
    // Initialize if needed
    initPlaybackState();

    // Show the grid
    document.getElementById('cung-grid-container').style.display = 'block';
    window.cungGridMode = true;

    playbackState.isPlaying = true;
    const btn = document.getElementById('btn-play');
    btn.classList.add('playing');
    btn.innerHTML = '<span class="play-icon">⏸</span> Pause';

    // Calculate interval based on speed (500ms - 3000ms)
    const interval = 3500 - (playbackState.speed * 300);

    // Initial fetch
    fetchChartForCurrentTime();
    updatePlaybackDisplay();

    playbackState.intervalId = setInterval(playbackTick, interval);
}

/**
 * Pause playback
 */
function pausePlayback() {
    playbackState.isPlaying = false;
    if (playbackState.intervalId) {
        clearInterval(playbackState.intervalId);
        playbackState.intervalId = null;
    }

    const btn = document.getElementById('btn-play');
    btn.classList.remove('playing');
    btn.innerHTML = '<span class="play-icon">▶</span> Play';
}

/**
 * Stop and reset playback
 */
function stopPlayback() {
    pausePlayback();

    // Reset to start
    playbackState.currentDate = { ...playbackState.startDate };
    playbackState.currentStep = 0;

    updatePlaybackDisplay();

    // Fetch initial chart
    fetchChartForCurrentTime();
}

/**
 * Step forward
 */
async function stepForward() {
    if (hasReachedEnd()) return;

    // Show grid if hidden
    document.getElementById('cung-grid-container').style.display = 'block';
    window.cungGridMode = true;

    initPlaybackState();
    advanceTime();
    updatePlaybackDisplay();
    await fetchChartForCurrentTime();
}

/**
 * Step backward
 */
async function stepBackward() {
    if (isAtStart()) return;

    // Show grid if hidden
    document.getElementById('cung-grid-container').style.display = 'block';
    window.cungGridMode = true;

    initPlaybackState();
    rewindTime();
    updatePlaybackDisplay();
    await fetchChartForCurrentTime();
}

/**
 * Initialize playback state from form
 */
function initPlaybackState() {
    const startYear = parseInt(document.getElementById('play-start-year').value) || 1950;
    const endYear = parseInt(document.getElementById('play-end-year').value) || 2000;
    const stepAmount = parseInt(document.getElementById('step-amount').value) || 1;
    const stepUnit = document.getElementById('step-unit').value || 'year';
    const speed = parseInt(document.getElementById('play-speed').value) || 3;

    // Only reset if parameters changed
    if (playbackState.startDate.year !== startYear ||
        playbackState.endDate.year !== endYear ||
        playbackState.stepAmount !== stepAmount ||
        playbackState.stepUnit !== stepUnit) {

        playbackState.startDate = { year: startYear, month: 1, day: 1, hour: 0 };
        playbackState.endDate = { year: endYear, month: 12, day: 31, hour: 11 };
        playbackState.currentDate = { ...playbackState.startDate };
        playbackState.stepAmount = stepAmount;
        playbackState.stepUnit = stepUnit;
        playbackState.currentStep = 0;
    }

    playbackState.speed = speed;
    playbackState.totalSteps = calculateTotalSteps();

    // Initialize jitter if needed
    if (!window.nodeJitter) window.nodeJitter = {};
}

/**
 * Speed slider change handler
 */
function onSpeedChange() {
    const speed = parseInt(document.getElementById('play-speed').value);
    document.getElementById('speed-value').textContent = speed + 'x';
    playbackState.speed = speed;

    // If playing, restart with new speed
    if (playbackState.isPlaying) {
        clearInterval(playbackState.intervalId);
        const interval = 3500 - (speed * 300);
        playbackState.intervalId = setInterval(playbackTick, interval);
    }
}

// ═══════════════════════════════════════════════════════════════════════════
// EXPORT TO GLOBAL SCOPE
// ═══════════════════════════════════════════════════════════════════════════

window.CHI_HOUR_NAMES = CHI_HOUR_NAMES;
window.playbackState = playbackState;

window.setQuickStep = setQuickStep;
window.calculateTotalSteps = calculateTotalSteps;
window.getDaysInMonth = getDaysInMonth;
window.advanceTime = advanceTime;
window.rewindTime = rewindTime;
window.hasReachedEnd = hasReachedEnd;
window.isAtStart = isAtStart;
window.updatePlaybackDisplay = updatePlaybackDisplay;
window.fetchChartForCurrentTime = fetchChartForCurrentTime;
window.togglePlayback = togglePlayback;
window.startPlayback = startPlayback;
window.pausePlayback = pausePlayback;
window.stopPlayback = stopPlayback;
window.stepForward = stepForward;
window.stepBackward = stepBackward;
window.initPlaybackState = initPlaybackState;
window.onSpeedChange = onSpeedChange;
