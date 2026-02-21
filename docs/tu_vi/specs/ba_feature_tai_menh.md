# 📊 BA DOCUMENT: TÍNH NĂNG ĐÁNH GIÁ TÀI VÀ MỆNH

**Mã tính năng:** FEAT-TAI-MENH-001  
**Ngày tạo:** 22/12/2025  
**Phiên bản:** 1.0  
**Tác giả:** BA Team  
**Trạng thái:** Ready for Development

---

## 1. 📋 TỔNG QUAN

### 1.1 Mô tả tính năng
Tính năng **Đánh giá Tài và Mệnh** cho phép người dùng hiểu mối quan hệ giữa **Tài năng (TÀI)** và **Vận mệnh (MỆNH)** trong lá số Tử Vi, dựa trên triết lý:

> **"Chữ Tài chữ Mệnh khéo là ghét nhau"** - Nguyễn Du, Truyện Kiều

### 1.2 Mục tiêu
- Cung cấp điểm số định lượng cho Tài (0-10) và Mệnh (0-10)
- Phân loại mối quan hệ Tài-Mệnh thành các category
- Đưa ra insight và lời khuyên cá nhân hóa
- Hiển thị trực quan trên giao diện web

### 1.3 Đối tượng sử dụng
- Người dùng cuối muốn hiểu về tài năng và vận mệnh
- Người nghiên cứu Tử Vi

---

## 2. 🎯 YÊU CẦU CHỨC NĂNG

### 2.1 UC-TAI-MENH-01: Tính điểm Tài (Talent Score)

**Mô tả:** Đánh giá mức độ tài năng dựa trên các sao trong lá số

**Input:** Dữ liệu lá số từ API `/api/generate`

**Logic tính điểm:**

| Tiêu chí | Sao | Điểm | Vị trí |
|----------|-----|------|--------|
| Văn tinh (Trí tuệ) | Văn Xương, Văn Khúc | +1.5 mỗi sao | Mệnh/Thân |
| Học vấn danh tiếng | Hóa Khoa | +2.0 (Mệnh/Thân), +1.0 (Quan Lộc) | Mệnh/Thân/Quan Lộc |
| Thông minh | Thiên Khôi, Thiên Việt | +0.5 mỗi sao | Mệnh/Thân |
| Nghệ thuật | Hoa Cái, Long Trì, Phượng Các | +1.0 mỗi sao | Mệnh/Thân |
| Lãnh đạo | Hóa Quyền | +1.0 | Mệnh/Thân |
| Mưu lược | Thiên Cơ | +1.0 | Mệnh |
| **Trừ điểm** | Địa Không, Địa Kiếp | -1.5 mỗi sao | Mệnh/Thân |

**Điểm khởi đầu:** 5.0  
**Thang điểm:** 0 - 10

**Output:**
```json
{
  "score": 7.5,
  "factors": [
    "Văn Xương tại Mệnh/Thân (+1.5)",
    "Hóa Khoa tại Mệnh/Thân (+2.0)",
    "Thiên Cơ tại Mệnh (+1.0)"
  ]
}
```

---

### 2.2 UC-TAI-MENH-02: Tính điểm Mệnh (Fortune Score)

**Mô tả:** Đánh giá mức độ may mắn/hạnh phúc dựa trên các sao trong lá số

**Logic tính điểm:**

| Tiêu chí | Sao | Điểm | Vị trí |
|----------|-----|------|--------|
| Sung túc | Lộc Tồn, Hóa Lộc | +1.5 mỗi sao | Mệnh/Thân |
| Phúc hậu | Thiên Phủ, Thái Âm, Thiên Đồng | +1.0 mỗi sao | Mệnh |
| Quý nhân đôi bên | Tả Phụ + Hữu Bật (cả 2) | +1.5 | Mệnh/Thân |
| Hạnh phúc hôn nhân | Hồng Loan, Thiên Hỷ | +1.0 mỗi sao | Phu Thê |
| Tuần/Triệt bảo vệ | Tuần hoặc Triệt | +0.5 | Mệnh |
| **Trừ điểm (Mệnh)** | Kình Dương, Đà La, Hỏa Tinh, Linh Tinh, Cô Thần, Quả Tú, Thiên Hình, Hóa Kỵ | -0.5 mỗi sao | Mệnh |
| **Trừ điểm (Phu Thê)** | Các sao trên | -0.3 mỗi sao | Phu Thê |

**Điểm khởi đầu:** 5.0  
**Thang điểm:** 0 - 10

**Output:**
```json
{
  "score": 6.5,
  "factors": [
    "Lộc Tồn - Sung túc (+1.5)",
    "Thiên Phủ tại Mệnh - Phúc hậu (+1.0)",
    "Tả Hữu hội - Quý nhân (+1.5)"
  ]
}
```

---

### 2.3 UC-TAI-MENH-03: Phân loại Tài-Mệnh

**Logic phân loại:**

| Category | Điều kiện | Icon | Màu |
|----------|-----------|------|-----|
| **Tài Mệnh Song Toàn** | Tài ≥ 7.0 VÀ Mệnh ≥ 7.0 | 👑 | Gold |
| **Tài Cao Mệnh Thấp** | Tài ≥ 7.0 VÀ Mệnh ≤ 4.0 | 🎭 | Purple |
| **Mệnh Cao Tài Thấp** | Tài ≤ 4.0 VÀ Mệnh ≥ 7.0 | 🍀 | Green |
| **Tài Mệnh Đều Thấp** | Tài ≤ 4.0 VÀ Mệnh ≤ 4.0 | 💪 | Orange |
| **Tài Vượt Mệnh** | Gap ≥ 3.0 VÀ Tài > Mệnh | ⚡ | Blue |
| **Mệnh Vượt Tài** | Gap ≥ 3.0 VÀ Mệnh > Tài | 🌟 | Cyan |
| **Tài Mệnh Cân Bằng** | Mặc định | ⚖️ | Gray |

**Insight cho từng category:**

```python
INSIGHTS = {
    "Tài Mệnh Song Toàn": "Rất hiếm! Cả tài năng và may mắn đều cao.",
    "Tài Cao Mệnh Thấp": "Đúng như Kiều: Tài năng xuất chúng nhưng đời lắm gian truân.",
    "Mệnh Cao Tài Thấp": "Bình dị mà hạnh phúc, tuy không xuất chúng nhưng đời an nhàn.",
    "Tài Mệnh Đều Thấp": "Cần nỗ lực nhiều hơn người khác để vượt qua nghịch cảnh.",
    "Tài Vượt Mệnh": "Tài năng không được may mắn hỗ trợ, có thể gặp trắc trở.",
    "Mệnh Vượt Tài": "May mắn nhiều hơn tài năng, nên biết ơn và tu dưỡng.",
    "Tài Mệnh Cân Bằng": "Tài năng và may mắn tương đối cân bằng."
}
```

---

### 2.4 UC-TAI-MENH-04: API Endpoint

**Endpoint:** `POST /api/tai-menh`

**Request:**
```json
{
  "chart": { /* Dữ liệu lá số từ /api/generate */ }
}
```

**Response:**
```json
{
  "status": "success",
  "data": {
    "tai_score": 7.5,
    "tai_factors": [
      "Văn Xương tại Mệnh/Thân (+1.5)",
      "Hóa Khoa tại Mệnh/Thân (+2.0)"
    ],
    "menh_score": 6.0,
    "menh_factors": [
      "Lộc Tồn - Sung túc (+1.5)",
      "Thiên Phủ tại Mệnh - Phúc hậu (+1.0)"
    ],
    "gap": 1.5,
    "category": "Tài Vượt Mệnh",
    "category_icon": "⚡",
    "category_color": "#3498db",
    "insight": "Tài năng không được may mắn hỗ trợ, có thể gặp trắc trở.",
    "advice": "Nên tu dưỡng đạo đức, làm việc thiện để cải mệnh."
  }
}
```

---

### 2.5 UC-TAI-MENH-05: Hiển thị UI

**Wireframe:**

```
┌─────────────────────────────────────────────────────────────┐
│                   ĐÁNH GIÁ TÀI VÀ MỆNH                     │
│                 "Chữ Tài chữ Mệnh khéo ghét nhau"           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────────┐            ┌─────────────┐               │
│   │   TÀI       │            │    MỆNH     │               │
│   │   7.5/10    │            │    6.0/10   │               │
│   │ ████████░░  │            │ ██████░░░░  │               │
│   └─────────────┘            └─────────────┘               │
│                                                             │
│              ┌───────────────────────┐                      │
│              │   ⚡ TÀI VƯỢT MỆNH    │                      │
│              │   Gap: +1.5           │                      │
│              └───────────────────────┘                      │
│                                                             │
│   📖 Insight:                                               │
│   "Tài năng không được may mắn hỗ trợ, có thể gặp          │
│    trắc trở."                                               │
│                                                             │
│   💡 Lời khuyên:                                            │
│   "Nên tu dưỡng đạo đức, làm việc thiện để cải mệnh."      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│   ▼ CHI TIẾT ĐIỂM TÀI                                      │
│   ✅ Văn Xương tại Mệnh/Thân (+1.5)                         │
│   ✅ Hóa Khoa tại Mệnh/Thân (+2.0)                          │
│   ❌ Địa Không phá Tài (-1.5)                               │
├─────────────────────────────────────────────────────────────┤
│   ▼ CHI TIẾT ĐIỂM MỆNH                                     │
│   ✅ Lộc Tồn - Sung túc (+1.5)                              │
│   ✅ Thiên Phủ tại Mệnh (+1.0)                              │
│   ❌ Kình Dương tại Mệnh (-0.5)                             │
└─────────────────────────────────────────────────────────────┘
```

**Màu sắc:**
- Điểm cao (≥7): `#27ae60` (Xanh lá)
- Điểm trung bình (4-7): `#f39c12` (Cam)
- Điểm thấp (<4): `#e74c3c` (Đỏ)
- Factors tích cực: `#2ecc71` (Xanh lá sáng)
- Factors tiêu cực: `#e74c3c` (Đỏ)

---

## 3. 🏗️ THIẾT KẾ KỸ THUẬT

### 3.1 Sử dụng Engine sẵn có

**File hiện có:** `python/analytics/talent_fortune_engine.py`

**Class:** `TalentFortuneAnalyzer`

**Methods:**
- `score_talent()` → dict
- `score_fortune()` → dict  
- `analyze()` → dict (kết hợp cả 2)

### 3.2 Cần bổ sung

#### 3.2.1 Thêm Lời khuyên (Advice)

```python
ADVICE = {
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
```

#### 3.2.2 Thêm API Endpoint

**File:** `python/app.py`

```python
@app.route('/api/tai-menh', methods=['POST'])
def get_tai_menh():
    """
    Đánh giá Tài và Mệnh (UC-TAI-MENH)
    """
    try:
        from analytics.talent_fortune_engine import TalentFortuneAnalyzer
        
        data = request.json
        chart = data.get('chart', {})
        
        if not chart:
            return jsonify({'status': 'error', 'message': 'Cần cung cấp dữ liệu lá số'}), 400
        
        analyzer = TalentFortuneAnalyzer(chart)
        result = analyzer.analyze()
        
        # Thêm advice
        category = result.get('category', 'Tài Mệnh Cân Bằng')
        advice_list = ADVICE.get(category, [])
        
        # Thêm icon và color
        CATEGORY_META = {
            "Tài Mệnh Song Toàn": {"icon": "👑", "color": "#f1c40f"},
            "Tài Cao Mệnh Thấp": {"icon": "🎭", "color": "#9b59b6"},
            "Mệnh Cao Tài Thấp": {"icon": "🍀", "color": "#27ae60"},
            "Tài Mệnh Đều Thấp": {"icon": "💪", "color": "#e67e22"},
            "Tài Vượt Mệnh": {"icon": "⚡", "color": "#3498db"},
            "Mệnh Vượt Tài": {"icon": "🌟", "color": "#1abc9c"},
            "Tài Mệnh Cân Bằng": {"icon": "⚖️", "color": "#95a5a6"},
        }
        
        meta = CATEGORY_META.get(category, {"icon": "❓", "color": "#7f8c8d"})
        
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
        return jsonify({'status': 'error', 'message': str(e)}), 500
```

#### 3.2.3 Thêm UI Component

**File:** `python/templates/index.html`

Thêm section Tài-Mệnh vào sau phần luận giải:

```html
<!-- Tài Mệnh Section -->
<div id="tai-menh-section" class="tai-menh-container" style="display: none;">
    <h3>📊 ĐÁNH GIÁ TÀI VÀ MỆNH</h3>
    <p class="subtitle">"Chữ Tài chữ Mệnh khéo là ghét nhau"</p>
    
    <div class="score-bars">
        <div class="score-item">
            <label>TÀI (Tài năng)</label>
            <div class="score-bar">
                <div id="tai-bar" class="score-fill"></div>
            </div>
            <span id="tai-score">0/10</span>
        </div>
        <div class="score-item">
            <label>MỆNH (Vận mệnh)</label>
            <div class="score-bar">
                <div id="menh-bar" class="score-fill"></div>
            </div>
            <span id="menh-score">0/10</span>
        </div>
    </div>
    
    <div id="category-badge" class="category-badge">
        <span id="category-icon"></span>
        <span id="category-name"></span>
        <span id="gap-value"></span>
    </div>
    
    <div id="insight-box" class="insight-box">
        <h4>📖 Insight</h4>
        <p id="insight-text"></p>
    </div>
    
    <div id="advice-box" class="advice-box">
        <h4>💡 Lời khuyên</h4>
        <ul id="advice-list"></ul>
    </div>
    
    <details class="factors-detail">
        <summary>▼ Chi tiết điểm TÀI</summary>
        <ul id="tai-factors"></ul>
    </details>
    
    <details class="factors-detail">
        <summary>▼ Chi tiết điểm MỆNH</summary>
        <ul id="menh-factors"></ul>
    </details>
</div>
```

#### 3.2.4 CSS Styles

**File:** `python/static/css/chart.css`

```css
/* Tai Menh Section */
.tai-menh-container {
    background: linear-gradient(135deg, #2c3e50 0%, #1a1a2e 100%);
    border-radius: 12px;
    padding: 24px;
    margin-top: 24px;
    color: #ecf0f1;
}

.tai-menh-container h3 {
    text-align: center;
    color: #f1c40f;
    margin-bottom: 4px;
}

.tai-menh-container .subtitle {
    text-align: center;
    font-style: italic;
    color: #bdc3c7;
    margin-bottom: 24px;
}

.score-bars {
    display: flex;
    gap: 24px;
    justify-content: center;
    margin-bottom: 24px;
}

.score-item {
    flex: 1;
    max-width: 200px;
}

.score-item label {
    display: block;
    text-align: center;
    margin-bottom: 8px;
    font-weight: bold;
}

.score-bar {
    height: 20px;
    background: #34495e;
    border-radius: 10px;
    overflow: hidden;
}

.score-fill {
    height: 100%;
    border-radius: 10px;
    transition: width 0.5s ease;
}

.score-fill.high { background: linear-gradient(90deg, #27ae60, #2ecc71); }
.score-fill.medium { background: linear-gradient(90deg, #f39c12, #f1c40f); }
.score-fill.low { background: linear-gradient(90deg, #c0392b, #e74c3c); }

.category-badge {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    padding: 16px;
    border-radius: 8px;
    margin-bottom: 20px;
    font-size: 1.2em;
    font-weight: bold;
}

.insight-box, .advice-box {
    background: rgba(255,255,255,0.05);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 16px;
}

.insight-box h4, .advice-box h4 {
    margin-top: 0;
    color: #f1c40f;
}

.factors-detail {
    background: rgba(255,255,255,0.03);
    border-radius: 8px;
    padding: 12px;
    margin-bottom: 12px;
}

.factors-detail summary {
    cursor: pointer;
    font-weight: bold;
}

.factors-detail ul {
    margin-top: 12px;
    padding-left: 20px;
}

.factor-positive { color: #2ecc71; }
.factor-negative { color: #e74c3c; }
```

#### 3.2.5 JavaScript

**File:** `python/static/js/main.js`

```javascript
// Tai Menh Analysis
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
        }
    } catch (error) {
        console.error('Error analyzing Tai Menh:', error);
    }
}

function displayTaiMenh(data) {
    // Show section
    document.getElementById('tai-menh-section').style.display = 'block';
    
    // Update scores
    const taiScore = data.tai_score;
    const menhScore = data.menh_score;
    
    document.getElementById('tai-score').textContent = `${taiScore}/10`;
    document.getElementById('menh-score').textContent = `${menhScore}/10`;
    
    // Update bars
    const taiBar = document.getElementById('tai-bar');
    const menhBar = document.getElementById('menh-bar');
    
    taiBar.style.width = `${taiScore * 10}%`;
    menhBar.style.width = `${menhScore * 10}%`;
    
    taiBar.className = 'score-fill ' + getScoreClass(taiScore);
    menhBar.className = 'score-fill ' + getScoreClass(menhScore);
    
    // Category badge
    const badge = document.getElementById('category-badge');
    badge.style.backgroundColor = data.category_color + '33';
    badge.style.border = `2px solid ${data.category_color}`;
    
    document.getElementById('category-icon').textContent = data.category_icon;
    document.getElementById('category-name').textContent = data.category;
    document.getElementById('gap-value').textContent = `Gap: ${data.gap > 0 ? '+' : ''}${data.gap}`;
    
    // Insight
    document.getElementById('insight-text').textContent = data.insight;
    
    // Advice
    const adviceList = document.getElementById('advice-list');
    adviceList.innerHTML = '';
    data.advice.forEach(a => {
        const li = document.createElement('li');
        li.textContent = a;
        adviceList.appendChild(li);
    });
    
    // Factors
    displayFactors('tai-factors', data.tai_factors);
    displayFactors('menh-factors', data.menh_factors);
}

function getScoreClass(score) {
    if (score >= 7) return 'high';
    if (score >= 4) return 'medium';
    return 'low';
}

function displayFactors(elementId, factors) {
    const ul = document.getElementById(elementId);
    ul.innerHTML = '';
    factors.forEach(f => {
        const li = document.createElement('li');
        li.textContent = f;
        li.className = f.includes('+') ? 'factor-positive' : 'factor-negative';
        ul.appendChild(li);
    });
}
```

---

## 4. 📋 TASK CHO DEV

### TASK-DEV-TAI-MENH-01: Backend API
**Priority:** HIGH  
**Estimated:** 2 giờ

- [ ] Thêm endpoint `/api/tai-menh` vào `app.py`
- [ ] Import `TalentFortuneAnalyzer` từ analytics
- [ ] Thêm dict `ADVICE` và `CATEGORY_META`
- [ ] Test với Postman/curl

### TASK-DEV-TAI-MENH-02: Frontend UI
**Priority:** HIGH  
**Estimated:** 3 giờ

- [ ] Thêm section HTML vào `index.html`
- [ ] Thêm CSS styles vào `chart.css`
- [ ] Thêm JavaScript functions vào `main.js`
- [ ] Gọi `analyzeTaiMenh()` sau khi generate chart

### TASK-DEV-TAI-MENH-03: Integration
**Priority:** MEDIUM  
**Estimated:** 1 giờ

- [ ] Hook vào flow generate chart
- [ ] Auto-load Tài Mệnh khi có chart
- [ ] Handle loading states
- [ ] Handle errors gracefully

---

## 5. 🧪 TASK CHO QC

### TASK-QC-TAI-MENH-01: Test API
**Priority:** HIGH  
**Estimated:** 1 giờ

**Test cases:**

| # | Input | Expected Output |
|---|-------|-----------------|
| 1 | Chart có Văn Xương + Văn Khúc tại Mệnh | Tài ≥ 8.0 |
| 2 | Chart có Địa Không + Địa Kiếp tại Mệnh | Tài < 4.0 |
| 3 | Chart có Lộc Tồn + Hóa Lộc tại Mệnh | Mệnh ≥ 7.0 |
| 4 | Chart có Kình Đà + Hỏa Linh tại Mệnh | Mệnh < 4.0 |
| 5 | Chart trống (no chart) | Error 400 |

### TASK-QC-TAI-MENH-02: Test UI
**Priority:** HIGH  
**Estimated:** 1 giờ

- [ ] Score bars hiển thị đúng %
- [ ] Colors đúng theo thang điểm
- [ ] Category badge hiển thị đúng
- [ ] Collapsible details hoạt động
- [ ] Responsive trên mobile

### TASK-QC-TAI-MENH-03: Test Edge Cases
**Priority:** MEDIUM  
**Estimated:** 30 phút

- [ ] Score = 0.0 (min)
- [ ] Score = 10.0 (max)
- [ ] Gap = 0 (cân bằng hoàn hảo)
- [ ] All factors positive
- [ ] All factors negative

---

## 6. 📊 ACCEPTANCE CRITERIA

1. ✅ API trả về điểm Tài (0-10) chính xác
2. ✅ API trả về điểm Mệnh (0-10) chính xác
3. ✅ Phân loại category đúng logic
4. ✅ UI hiển thị score bars trực quan
5. ✅ Insight và Advice hiển thị đầy đủ
6. ✅ Responsive trên mobile
7. ✅ Không lỗi console JavaScript
8. ✅ Load time < 500ms

---

## 7. 📎 TÀI LIỆU THAM KHẢO

- `python/analytics/talent_fortune_engine.py` - Engine sẵn có
- `python/analytics/multi_score_engine.py` - Logic scoring bổ sung
- `python/analytics/definitions.py` - Định nghĩa nhóm sao

---

*Tài liệu BA tạo: 22/12/2025*  
*Người tạo: BA Team*  
*Review by: [Pending]*

