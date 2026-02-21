# 🛠️ HƯỚNG DẪN IMPLEMENTATION - TÍNH NĂNG TÀI MỆNH

**Dành cho:** Dev Team  
**Thời gian dự kiến:** 4-6 giờ  
**Tham khảo:** BA_TAI_MENH_FEATURE.md

---

## ⚡ QUICK START

### Bước 1: Thêm API Endpoint (30 phút)

**File:** `python/app.py`

Thêm vào cuối file, trước `if __name__ == '__main__':`:

```python
# ═══════════════════════════════════════════════════════════════════════════
# TAI MENH ANALYSIS API
# ═══════════════════════════════════════════════════════════════════════════

# Advice dict
TAI_MENH_ADVICE = {
    "Tài Mệnh Song Toàn": [
        "Biết trân trọng những gì mình có.",
        "Chia sẻ tài năng và may mắn cho người khác.",
        "Không kiêu ngạo, giữ đức khiêm tốn."
    ],
    "Tài Cao Mệnh Thấp": [
        "Tu dưỡng đạo đức, làm việc thiện để cải mệnh.",
        "Tìm quý nhân phò tá, đừng cố gắng một mình.",
        "Kiên nhẫn, vạn sự khởi đầu nan.",
        "Tránh đầu tư mạo hiểm, giữ ổn định."
    ],
    "Mệnh Cao Tài Thấp": [
        "Trau dồi kỹ năng, học hỏi không ngừng.",
        "Biết ơn và sống tích cực.",
        "Không ỷ lại vào may mắn, phải tự phấn đấu."
    ],
    "Tài Mệnh Đều Thấp": [
        "Không bỏ cuộc, nghịch cảnh rèn luyện người.",
        "Tìm môi trường phù hợp để phát triển.",
        "Tu tâm, hành thiện để tích đức.",
        "Kết giao với người tốt, tránh tiểu nhân."
    ],
    "Tài Vượt Mệnh": [
        "Tìm quý nhân, môi trường tốt để tài năng phát huy.",
        "Kiên nhẫn chờ thời, vận may sẽ đến.",
        "Làm việc thiện để tích phúc đức."
    ],
    "Mệnh Vượt Tài": [
        "Trau dồi kỹ năng để xứng đáng với may mắn.",
        "Biết ơn và chia sẻ với người khác.",
        "Không lãng phí thời gian, may mắn có giới hạn."
    ],
    "Tài Mệnh Cân Bằng": [
        "Cuộc sống ổn định, tiếp tục phát triển.",
        "Cân bằng giữa làm việc và nghỉ ngơi.",
        "Giữ gìn sức khỏe và các mối quan hệ."
    ]
}

TAI_MENH_CATEGORY_META = {
    "Tài Mệnh Song Toàn": {"icon": "👑", "color": "#f1c40f"},
    "Tài Cao Mệnh Thấp": {"icon": "🎭", "color": "#9b59b6"},
    "Mệnh Cao Tài Thấp": {"icon": "🍀", "color": "#27ae60"},
    "Tài Mệnh Đều Thấp": {"icon": "💪", "color": "#e67e22"},
    "Tài Vượt Mệnh": {"icon": "⚡", "color": "#3498db"},
    "Mệnh Vượt Tài": {"icon": "🌟", "color": "#1abc9c"},
    "Tài Mệnh Cân Bằng": {"icon": "⚖️", "color": "#95a5a6"},
}


@app.route('/api/tai-menh', methods=['POST'])
def get_tai_menh():
    """
    Đánh giá Tài và Mệnh - FEAT-TAI-MENH-001
    
    Request:
        {"chart": {...}}
        
    Response:
        {
            "status": "success",
            "data": {
                "tai_score": 7.5,
                "menh_score": 6.0,
                "category": "Tài Vượt Mệnh",
                ...
            }
        }
    """
    try:
        from analytics.talent_fortune_engine import TalentFortuneAnalyzer
        
        data = request.json
        chart = data.get('chart', {})
        
        if not chart:
            return jsonify({
                'status': 'error', 
                'message': 'Cần cung cấp dữ liệu lá số'
            }), 400
        
        # Analyze
        analyzer = TalentFortuneAnalyzer(chart)
        result = analyzer.analyze()
        
        # Enrich with advice and meta
        category = result.get('category', 'Tài Mệnh Cân Bằng')
        advice_list = TAI_MENH_ADVICE.get(category, [])
        meta = TAI_MENH_CATEGORY_META.get(category, {"icon": "❓", "color": "#7f8c8d"})
        
        return jsonify({
            'status': 'success',
            'data': {
                **result,
                'category_icon': meta['icon'],
                'category_color': meta['color'],
                'advice': advice_list
            }
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'status': 'error', 
            'message': str(e)
        }), 500
```

---

### Bước 2: Test API (10 phút)

```bash
# Start server
cd python
python app.py

# Test với curl (trong terminal khác)
curl -X POST http://localhost:5000/api/tai-menh \
  -H "Content-Type: application/json" \
  -d '{"chart": {}}'
# Expected: error về chart trống

# Test với chart thật (dùng Postman hoặc code)
```

**Test script Python:**

```python
# test_tai_menh_api.py
import requests
from chart import generate_birth_chart

# Generate sample chart
chart = generate_birth_chart(28, 3, 1994, 4, 'nu')

# Call API
response = requests.post(
    'http://localhost:5000/api/tai-menh',
    json={'chart': chart}
)

print(response.json())
```

---

### Bước 3: Thêm UI HTML (30 phút)

**File:** `python/templates/index.html`

Thêm section này sau phần luận giải (sau `#interpretation-section`):

```html
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<!-- TAI MENH SECTION -->
<!-- ═══════════════════════════════════════════════════════════════════════ -->
<section id="tai-menh-section" class="tai-menh-container" style="display: none;">
    <div class="section-header">
        <h3>📊 ĐÁNH GIÁ TÀI VÀ MỆNH</h3>
        <p class="subtitle">"Chữ Tài chữ Mệnh khéo là ghét nhau" - Nguyễn Du</p>
    </div>
    
    <div class="score-container">
        <div class="score-card">
            <div class="score-label">TÀI</div>
            <div class="score-subtitle">Tài năng</div>
            <div class="score-bar-container">
                <div id="tai-bar" class="score-bar"></div>
            </div>
            <div id="tai-score" class="score-value">0/10</div>
        </div>
        
        <div class="score-card">
            <div class="score-label">MỆNH</div>
            <div class="score-subtitle">Vận mệnh</div>
            <div class="score-bar-container">
                <div id="menh-bar" class="score-bar"></div>
            </div>
            <div id="menh-score" class="score-value">0/10</div>
        </div>
    </div>
    
    <div id="category-badge" class="category-badge">
        <span id="category-icon" class="badge-icon"></span>
        <span id="category-name" class="badge-name"></span>
        <span id="gap-value" class="badge-gap"></span>
    </div>
    
    <div id="insight-box" class="insight-box">
        <div class="box-header">📖 Insight</div>
        <p id="insight-text" class="box-content"></p>
    </div>
    
    <div id="advice-box" class="advice-box">
        <div class="box-header">💡 Lời khuyên</div>
        <ul id="advice-list" class="advice-list"></ul>
    </div>
    
    <div class="factors-container">
        <details class="factors-detail">
            <summary>📈 Chi tiết điểm TÀI</summary>
            <ul id="tai-factors" class="factors-list"></ul>
        </details>
        
        <details class="factors-detail">
            <summary>📉 Chi tiết điểm MỆNH</summary>
            <ul id="menh-factors" class="factors-list"></ul>
        </details>
    </div>
</section>
```

---

### Bước 4: Thêm CSS (20 phút)

**File:** `python/static/css/chart.css`

Thêm vào cuối file:

```css
/* ═══════════════════════════════════════════════════════════════════════════
   TAI MENH SECTION STYLES
   ═══════════════════════════════════════════════════════════════════════════ */

.tai-menh-container {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 16px;
    padding: 32px;
    margin: 24px 0;
    color: #e8e8e8;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

.tai-menh-container .section-header {
    text-align: center;
    margin-bottom: 32px;
}

.tai-menh-container .section-header h3 {
    color: #f1c40f;
    font-size: 1.5em;
    margin: 0 0 8px 0;
}

.tai-menh-container .subtitle {
    color: #a0a0a0;
    font-style: italic;
    margin: 0;
}

/* Score Cards */
.score-container {
    display: flex;
    gap: 24px;
    justify-content: center;
    margin-bottom: 24px;
    flex-wrap: wrap;
}

.score-card {
    background: rgba(255,255,255,0.05);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    min-width: 150px;
    flex: 1;
    max-width: 200px;
}

.score-label {
    font-size: 1.4em;
    font-weight: bold;
    color: #fff;
}

.score-subtitle {
    font-size: 0.85em;
    color: #888;
    margin-bottom: 12px;
}

.score-bar-container {
    height: 12px;
    background: #2c3e50;
    border-radius: 6px;
    overflow: hidden;
    margin-bottom: 8px;
}

.score-bar {
    height: 100%;
    border-radius: 6px;
    transition: width 0.8s ease-out, background 0.3s;
    width: 0%;
}

.score-bar.high { background: linear-gradient(90deg, #27ae60, #2ecc71); }
.score-bar.medium { background: linear-gradient(90deg, #f39c12, #f1c40f); }
.score-bar.low { background: linear-gradient(90deg, #c0392b, #e74c3c); }

.score-value {
    font-size: 1.2em;
    font-weight: bold;
    color: #fff;
}

/* Category Badge */
.category-badge {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    padding: 16px 24px;
    border-radius: 50px;
    margin: 24px auto;
    max-width: 400px;
    font-weight: bold;
    transition: all 0.3s;
}

.badge-icon {
    font-size: 1.5em;
}

.badge-name {
    font-size: 1.1em;
}

.badge-gap {
    font-size: 0.9em;
    opacity: 0.8;
}

/* Insight & Advice Boxes */
.insight-box, .advice-box {
    background: rgba(255,255,255,0.03);
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 16px;
    border-left: 4px solid #f1c40f;
}

.box-header {
    font-weight: bold;
    color: #f1c40f;
    margin-bottom: 8px;
}

.box-content {
    margin: 0;
    line-height: 1.6;
}

.advice-list {
    margin: 0;
    padding-left: 24px;
}

.advice-list li {
    margin-bottom: 8px;
    line-height: 1.5;
}

/* Factors Details */
.factors-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 16px;
    margin-top: 16px;
}

.factors-detail {
    background: rgba(255,255,255,0.02);
    border-radius: 8px;
    padding: 12px 16px;
}

.factors-detail summary {
    cursor: pointer;
    font-weight: bold;
    color: #3498db;
    padding: 8px 0;
}

.factors-detail summary:hover {
    color: #5dade2;
}

.factors-list {
    margin: 12px 0 0 0;
    padding-left: 20px;
}

.factors-list li {
    margin-bottom: 6px;
    font-size: 0.95em;
}

.factors-list li.positive { color: #2ecc71; }
.factors-list li.negative { color: #e74c3c; }

/* Responsive */
@media (max-width: 600px) {
    .tai-menh-container {
        padding: 20px;
    }
    
    .score-container {
        flex-direction: column;
        align-items: center;
    }
    
    .score-card {
        width: 100%;
        max-width: none;
    }
    
    .category-badge {
        flex-direction: column;
        gap: 8px;
    }
}
```

---

### Bước 5: Thêm JavaScript (30 phút)

**File:** `python/static/js/main.js`

Thêm vào cuối file:

```javascript
// ═══════════════════════════════════════════════════════════════════════════
// TAI MENH ANALYSIS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Analyze Tai Menh from chart data
 * @param {Object} chartData - Chart data from /api/generate
 */
async function analyzeTaiMenh(chartData) {
    try {
        const response = await fetch('/api/tai-menh', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ chart: chartData })
        });
        
        const result = await response.json();
        
        if (result.status === 'success') {
            displayTaiMenh(result.data);
        } else {
            console.error('Tai Menh error:', result.message);
        }
    } catch (error) {
        console.error('Error analyzing Tai Menh:', error);
    }
}

/**
 * Display Tai Menh results in UI
 * @param {Object} data - Tai Menh analysis data
 */
function displayTaiMenh(data) {
    // Show section
    const section = document.getElementById('tai-menh-section');
    if (section) {
        section.style.display = 'block';
    }
    
    // Get scores
    const taiScore = data.tai_score || 0;
    const menhScore = data.menh_score || 0;
    
    // Update score text
    const taiScoreEl = document.getElementById('tai-score');
    const menhScoreEl = document.getElementById('menh-score');
    if (taiScoreEl) taiScoreEl.textContent = `${taiScore}/10`;
    if (menhScoreEl) menhScoreEl.textContent = `${menhScore}/10`;
    
    // Update bars with animation
    setTimeout(() => {
        const taiBar = document.getElementById('tai-bar');
        const menhBar = document.getElementById('menh-bar');
        
        if (taiBar) {
            taiBar.style.width = `${taiScore * 10}%`;
            taiBar.className = 'score-bar ' + getScoreClass(taiScore);
        }
        
        if (menhBar) {
            menhBar.style.width = `${menhScore * 10}%`;
            menhBar.className = 'score-bar ' + getScoreClass(menhScore);
        }
    }, 100);
    
    // Category badge
    const badge = document.getElementById('category-badge');
    if (badge) {
        badge.style.backgroundColor = (data.category_color || '#7f8c8d') + '33';
        badge.style.border = `2px solid ${data.category_color || '#7f8c8d'}`;
    }
    
    const iconEl = document.getElementById('category-icon');
    const nameEl = document.getElementById('category-name');
    const gapEl = document.getElementById('gap-value');
    
    if (iconEl) iconEl.textContent = data.category_icon || '❓';
    if (nameEl) nameEl.textContent = data.category || 'Không xác định';
    if (gapEl) {
        const gap = data.gap || 0;
        gapEl.textContent = `Gap: ${gap > 0 ? '+' : ''}${gap}`;
    }
    
    // Insight
    const insightEl = document.getElementById('insight-text');
    if (insightEl) insightEl.textContent = data.insight || '';
    
    // Advice
    const adviceList = document.getElementById('advice-list');
    if (adviceList && data.advice) {
        adviceList.innerHTML = '';
        data.advice.forEach(advice => {
            const li = document.createElement('li');
            li.textContent = advice;
            adviceList.appendChild(li);
        });
    }
    
    // Factors
    displayFactorsList('tai-factors', data.tai_factors || []);
    displayFactorsList('menh-factors', data.menh_factors || []);
}

/**
 * Get score class for styling
 * @param {number} score - Score value (0-10)
 * @returns {string} CSS class name
 */
function getScoreClass(score) {
    if (score >= 7) return 'high';
    if (score >= 4) return 'medium';
    return 'low';
}

/**
 * Display factors list
 * @param {string} elementId - UL element ID
 * @param {Array} factors - Array of factor strings
 */
function displayFactorsList(elementId, factors) {
    const ul = document.getElementById(elementId);
    if (!ul) return;
    
    ul.innerHTML = '';
    factors.forEach(factor => {
        const li = document.createElement('li');
        li.textContent = factor;
        // Positive factors contain (+), negative contain (-)
        if (factor.includes('(+')) {
            li.className = 'positive';
        } else if (factor.includes('(-')) {
            li.className = 'negative';
        }
        ul.appendChild(li);
    });
}

// ═══════════════════════════════════════════════════════════════════════════
// INTEGRATION: Call analyzeTaiMenh after chart generation
// ═══════════════════════════════════════════════════════════════════════════

// Option 1: If you have a callback after chart generation, add:
// analyzeTaiMenh(chartData);

// Option 2: If using event-based, listen for chart ready:
// document.addEventListener('chartReady', (e) => analyzeTaiMenh(e.detail.chart));

// Option 3: Modify existing generateChart() function to call analyzeTaiMenh
```

---

### Bước 6: Integration (15 phút)

Tìm function generate chart trong `main.js` và thêm lời gọi `analyzeTaiMenh()`:

```javascript
// Trong function xử lý response từ /api/generate
// Thêm dòng này sau khi có chartData:

// Analyze Tai Menh
if (chartData) {
    analyzeTaiMenh(chartData);
}
```

---

## ✅ CHECKLIST HOÀN THÀNH

- [ ] Thêm API endpoint `/api/tai-menh`
- [ ] Test API với curl/Postman
- [ ] Thêm HTML section
- [ ] Thêm CSS styles
- [ ] Thêm JavaScript functions
- [ ] Hook vào generate chart flow
- [ ] Test UI trên desktop
- [ ] Test UI trên mobile
- [ ] No console errors

---

## 🧪 TEST COMMANDS

```bash
# Start server
cd python
python app.py

# Test API
curl -X POST http://localhost:5000/api/tai-menh \
  -H "Content-Type: application/json" \
  -d '{"chart": {"cung_map": {}, "positions": {}, "menh_position": 0}}'

# Check linting
python -m py_compile app.py
```

---

*Guide created: 22/12/2025*

