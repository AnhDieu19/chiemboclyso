# TỬ VI NAM PHÁI - UI/UX SPECIFICATIONS

## 📋 Mục Lục

1. [Design System](#1-design-system)
2. [Wireframes](#2-wireframes)
3. [Screen Specifications](#3-screen-specifications)
4. [Component Library](#4-component-library)
5. [Responsive Design](#5-responsive-design)
6. [Accessibility](#6-accessibility)

---

## 1. DESIGN SYSTEM

### 1.1 Color Palette

#### Primary Colors

```css
:root {
  /* Main Theme - Traditional Vietnamese */
  --primary-red: #C41E3A;        /* Đỏ cổ điển */
  --primary-gold: #D4AF37;       /* Vàng hoàng gia */
  --primary-dark: #1A1A2E;       /* Nền tối */
  
  /* Ngũ Hành Colors */
  --metal-gold: #FFD700;         /* Kim - Vàng */
  --wood-green: #228B22;         /* Mộc - Xanh lá */
  --water-blue: #000080;         /* Thủy - Xanh đậm */
  --fire-red: #DC143C;           /* Hỏa - Đỏ */
  --earth-brown: #8B4513;        /* Thổ - Nâu */
  
  /* Tứ Hóa Colors */
  --hoa-loc: #4CAF50;            /* Lộc - Xanh lá */
  --hoa-quyen: #F44336;          /* Quyền - Đỏ */
  --hoa-khoa: #9C27B0;           /* Khoa - Tím */
  --hoa-ky: #212121;             /* Kỵ - Đen */
  
  /* Độ sáng sao */
  --mieu: #FFD700;               /* Miếu - Vàng sáng */
  --vuong: #FFA500;              /* Vượng - Cam */
  --dac: #90EE90;                /* Đắc - Xanh nhạt */
  --binh: #808080;               /* Bình - Xám */
  --ham: #A9A9A9;                /* Hãm - Xám đậm */
}
```

#### Semantic Colors

```css
:root {
  --success: #28A745;
  --warning: #FFC107;
  --danger: #DC3545;
  --info: #17A2B8;
  
  --text-primary: #212529;
  --text-secondary: #6C757D;
  --text-light: #F8F9FA;
  
  --bg-primary: #FFFFFF;
  --bg-secondary: #FFFAF0; /* FloralWhite - Updated 28/12/2025 */
  --bg-dark: #1A1A2E;
}
```

### 1.2 Typography

```css
/* Font Family */
/* Updated 28/12/2025: Clear Sans-serif fonts for better readability */
:root {
  --font-primary: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  --font-chinese: 'Noto Serif SC', serif;  /* Cho chữ Hán */
  
  /* Font Sizes */
  --fs-h1: 2.5rem;    /* 40px */
  --fs-h2: 2rem;      /* 32px */
  --fs-h3: 1.5rem;    /* 24px */
  --fs-h4: 1.25rem;   /* 20px */
  --fs-body: 13px;    /* 13px (Base for Palace content) */
  --fs-main-star: 16px; /* 16px (Main Stars) */
  --fs-small: 0.875rem; /* 14px */
  --fs-tiny: 0.75rem;   /* 12px */
  
  /* Line Heights */
  --lh-tight: 1.2;
  --lh-normal: 1.4;   /* Adjusted for readability */
  --lh-loose: 1.8;
}
```

### 1.3 Spacing

```css
:root {
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-xxl: 3rem;     /* 48px */
}
```

### 1.4 Border & Shadow

```css
:root {
  /* Borders */
  --border-radius-sm: 4px;
  --border-radius-md: 8px;
  --border-radius-lg: 16px;
  --border-radius-full: 50%;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.1);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
  --shadow-gold: 0 4px 15px rgba(212,175,55,0.3);
}
```

---

## 2. WIREFRAMES

### 2.1 Main Layout

```
┌────────────────────────────────────────────────────────────────────────────┐
│                              HEADER                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  🌟 TỬ VI ĐẨU SỐ NAM PHÁI                     [Hướng dẫn] [About]  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        INPUT SECTION                                 │   │
│  │                                                                      │   │
│  │   [Ngày] [Tháng] [Năm]    [Giờ sinh ▼]    [Nam/Nữ]    [LẬP LÁ SỐ]  │   │
│  │                                                                      │   │
│  │   ☐ Nhập Âm lịch    ☐ Tháng nhuận                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌───────────────────────────────────┬────────────────────────────────┐    │
│  │                                   │                                │    │
│  │          CHART SECTION            │      INTERPRETATION SECTION   │    │
│  │                                   │                                │    │
│  │   ┌─────┬─────┬─────┬─────┐      │   📋 THÔNG TIN CƠ BẢN         │    │
│  │   │ Tỵ │Ngọ │Mùi │Thân│      │   • Năm: Quý Dậu                │    │
│  │   ├─────┼─────┼─────┼─────┤      │   • Cục: Mộc Tam Cục          │    │
│  │   │Thìn│           │ Dậu│      │                                │    │
│  │   ├─────┤           ├─────┤      │   📌 PHÂN TÍCH CUNG MỆNH      │    │
│  │   │ Mão│           │Tuất│      │   Cung Mệnh có Tử Vi...        │    │
│  │   ├─────┼─────┬─────┼─────┤      │                                │    │
│  │   │ Dần│ Sửu│ Tý │ Hợi│      │   📌 SỰ NGHIỆP                  │    │
│  │   └─────┴─────┴─────┴─────┘      │   ...                          │    │
│  │                                   │                                │    │
│  └───────────────────────────────────┴────────────────────────────────┘    │
│                                                                              │
├────────────────────────────────────────────────────────────────────────────┤
│                              FOOTER                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  © 2025 Tử Vi Nam Phái | Phiên bản 1.0                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Chart Grid Layout (12 Cung)

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│     ┌──────────┬──────────┬──────────┬──────────┐               │
│     │          │          │          │          │               │
│     │   TỴ     │   NGỌ    │   MÙI    │   THÂN   │               │
│     │  Tật Ách │ Thiên Di │  Nô Bộc  │ Quan Lộc │               │
│     │──────────│──────────│──────────│──────────│               │
│     │ ★Tử Vi   │ ☆Thái Dương│ ☆Vũ Khúc│ ★Thiên Phủ│               │
│     │ ☆Thiên Cơ│          │          │ ☆Thái Âm │               │
│     │          │          │          │          │               │
│     ├──────────┼──────────┴──────────┼──────────┤               │
│     │          │                     │          │               │
│     │  THÌN    │                     │   DẬU    │               │
│     │Điền Trạch│                     │ Phúc Đức │               │
│     │──────────│     THÔNG TIN       │──────────│               │
│     │ ☆Liêm Trinh│    TRUNG TÂM      │ ☆Tham Lang│               │
│     │          │                     │          │               │
│     ├──────────┤   Năm: Quý Dậu     ├──────────┤               │
│     │          │   Cục: Mộc 3       │          │               │
│     │   MÃO    │   Mệnh: Dần        │  TUẤT    │               │
│     │  Tử Tức  │   Thân: Thân       │ Phụ Mẫu  │               │
│     │──────────│                     │──────────│               │
│     │ ☆Cự Môn  │                     │★Thiên Lương│               │
│     │          │                     │          │               │
│     ├──────────┼──────────┬──────────┼──────────┤               │
│     │          │          │          │          │               │
│     │   DẦN    │   SỬU    │    TÝ    │   HỢI    │               │
│     │   MỆNH   │ Huynh Đệ │  Phu Thê │ Tài Bạch │               │
│     │──────────│──────────│──────────│──────────│               │
│     │★Phá Quân │ ☆Thiên Đồng│ ★Thất Sát│☆Thiên Tướng│               │
│     │  🔒THÂN  │          │          │          │               │
│     │          │          │          │          │               │
│     └──────────┴──────────┴──────────┴──────────┘               │
│                                                                   │
│     ★ = Chính Tinh     ☆ = Phụ Tinh     🔒 = Cung Thân          │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.3 Star Detail Popup

```
┌─────────────────────────────────────────────────────────────────┐
│  ╔═════════════════════════════════════════════════════════╗   │
│  ║                      ★ TỬ VI ★                          ║   │
│  ║                    Đế Tinh - Sao Vua                    ║   │
│  ╠═════════════════════════════════════════════════════════╣   │
│  ║                                                         ║   │
│  ║  📊 THÔNG TIN CƠ BẢN                                    ║   │
│  ║  ┌─────────────────────────────────────────────────┐   ║   │
│  ║  │ Loại sao    : Chính Tinh                        │   ║   │
│  ║  │ Ngũ Hành    : Thổ                               │   ║   │
│  ║  │ Âm/Dương    : Âm                                │   ║   │
│  ║  │ Tính chất   : Cát tinh                          │   ║   │
│  ║  │ Độ sáng     : 🌟 MIẾU (Cung Dần)               │   ║   │
│  ║  └─────────────────────────────────────────────────┘   ║   │
│  ║                                                         ║   │
│  ║  📖 Ý NGHĨA                                             ║   │
│  ║  ─────────────────────────────────────────────────────  ║   │
│  ║  Tử Vi là sao đế vương, chủ quyền quý, cao sang.       ║   │
│  ║  Người có Tử Vi tọa Mệnh thường có tư chất lãnh đạo,   ║   │
│  ║  ưa chuộng sự hoàn hảo, có chí tiến thủ...            ║   │
│  ║                                                         ║   │
│  ║  🏷️ KEYWORDS                                            ║   │
│  ║  ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐          ║   │
│  ║  │Quyền lực│ │Cao quý │ │Lãnh đạo│ │Bảo thủ │          ║   │
│  ║  └────────┘ └────────┘ └────────┘ └────────┘          ║   │
│  ║                                                         ║   │
│  ║  🔄 TỨ HÓA HIỆN TẠI: Hóa Lộc 🟢                        ║   │
│  ║                                                         ║   │
│  ║                              [Đóng]                     ║   │
│  ╚═════════════════════════════════════════════════════════╝   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. SCREEN SPECIFICATIONS

### 3.1 Home Screen (Form Input)

#### Elements

| Element | Type | Properties | Notes |
|---------|------|------------|-------|
| Title | H1 | "TỬ VI ĐẨU SỐ NAM PHÁI" | Font 40px, Vàng kim |
| Day Input | Number | Min: 1, Max: 31 | Required |
| Month Input | Number | Min: 1, Max: 12 | Required |
| Year Input | Number | Min: 1900, Max: 2100 | Required |
| Hour Select | Dropdown | 12 options (Tý-Hợi) | Required |
| Gender | Radio | Nam / Nữ | Default: Nam |
| Lunar Toggle | Checkbox | "Nhập Âm lịch" | Default: unchecked |
| Leap Month | Checkbox | "Tháng nhuận" | Only show when Lunar=true |
| Submit Button | Button | "LẬP LÁ SỐ" | Primary style |

#### Interactions

```
User Action              →  System Response
────────────────────────────────────────────────────────
Click "LẬP LÁ SỐ"        →  Validate inputs
                         →  Show loading spinner
                         →  Call API /api/generate
                         →  Display chart + interpretation

Toggle "Âm lịch"         →  Show/hide "Tháng nhuận" checkbox
                         →  Clear converted date display

Invalid input            →  Show inline error message
                         →  Highlight field with red border
```

### 3.2 Chart Display Screen

#### Elements

| Element | Type | Size | Notes |
|---------|------|------|-------|
| Chart Grid | CSS Grid | 4x4 cells | Center cell spans 2x2 |
| Palace Cell | Div | Min 150x150px | Contains stars list |
| Star Name | Span | 12-14px | Color based on type |
| Tu Hoa Badge | Badge | 16x16px | 🟢🔴🟣⚫ |
| Brightness Icon | Icon | 12px | ⭐ for Miếu/Vượng |
| Info Center | Div | 2x2 cells | Shows basic info |

#### Star Display Rules

```css
/* Chính Tinh */
.chinh-tinh {
  font-weight: 600;
  font-size: 14px;
  color: var(--primary-red);
}

/* Phụ Tinh */
.phu-tinh {
  font-weight: 400;
  font-size: 12px;
  color: var(--text-secondary);
}

/* Tứ Hóa */
.hoa-loc::after { content: "🟢"; }
.hoa-quyen::after { content: "🔴"; }
.hoa-khoa::after { content: "🟣"; }
.hoa-ky::after { content: "⚫"; }

/* Độ sáng */
.mieu, .vuong { font-weight: 700; }
.binh { opacity: 0.8; }
.ham { opacity: 0.6; font-style: italic; }
```

### 3.3 Interpretation Panel

#### Structure

```
┌────────────────────────────────────────────┐
│ 📋 LUẬN GIẢI LÁ SỐ                        │
├────────────────────────────────────────────┤
│                                            │
│ ▼ THÔNG TIN CƠ BẢN                        │
│   ├─ Năm sinh: Quý Dậu (1993)             │
│   ├─ Nạp Âm: Kiếm Phong Kim               │
│   ├─ Cục: Mộc Tam Cục                     │
│   └─ Cung Mệnh: Dần                       │
│                                            │
│ ▼ PHÂN TÍCH CUNG MỆNH          [Expand ▼] │
│   Cung Mệnh có Tử Vi hóa Lộc...           │
│                                            │
│ ▶ CÁCH CỤC ĐẶC BIỆT            [Expand ▼] │
│                                            │
│ ▶ SỰ NGHIỆP                    [Expand ▼] │
│                                            │
│ ▶ TÀI CHÍNH                    [Expand ▼] │
│                                            │
│ ▶ TÌNH CẢM                     [Expand ▼] │
│                                            │
│ ▶ SỨC KHỎE                     [Expand ▼] │
│                                            │
└────────────────────────────────────────────┘
```

---

## 4. COMPONENT LIBRARY

### 4.1 Button Components

```html
<!-- Primary Button -->
<button class="btn btn-primary">
  LẬP LÁ SỐ
</button>

<!-- Secondary Button -->
<button class="btn btn-secondary">
  Hủy
</button>

<!-- Icon Button -->
<button class="btn btn-icon">
  <span class="icon">ℹ️</span>
  Hướng dẫn
</button>
```

```css
.btn {
  padding: 12px 24px;
  border-radius: var(--border-radius-md);
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-primary {
  background: linear-gradient(135deg, var(--primary-red), var(--primary-gold));
  color: white;
  border: none;
}

.btn-primary:hover {
  box-shadow: var(--shadow-gold);
  transform: translateY(-2px);
}

.btn-secondary {
  background: transparent;
  border: 2px solid var(--primary-red);
  color: var(--primary-red);
}
```

### 4.2 Input Components

```html
<!-- Text Input -->
<div class="input-group">
  <label for="day">Ngày</label>
  <input type="number" id="day" min="1" max="31" required>
  <span class="error-message">Ngày không hợp lệ</span>
</div>

<!-- Select -->
<div class="input-group">
  <label for="hour">Giờ sinh</label>
  <select id="hour">
    <option value="0">Tý (23:00 - 01:00)</option>
    <option value="1">Sửu (01:00 - 03:00)</option>
    <!-- ... -->
  </select>
</div>

<!-- Radio Group -->
<div class="radio-group">
  <label>Giới tính</label>
  <div class="radio-options">
    <input type="radio" id="male" name="gender" value="nam" checked>
    <label for="male">Nam</label>
    <input type="radio" id="female" name="gender" value="nu">
    <label for="female">Nữ</label>
  </div>
</div>
```

### 4.3 Card Components

```html
<!-- Palace Card -->
<div class="palace-card" data-palace="menh">
  <div class="palace-header">
    <span class="palace-chi">Dần</span>
    <span class="palace-name">Mệnh</span>
    <span class="palace-than-badge">THÂN</span>
  </div>
  <div class="palace-stars">
    <span class="star chinh-tinh mieu hoa-loc">Tử Vi</span>
    <span class="star phu-tinh dac">Văn Xương</span>
    <span class="star phu-tinh binh">Tả Phù</span>
  </div>
</div>
```

### 4.4 Modal Components

```html
<!-- Star Detail Modal -->
<div class="modal" id="star-modal">
  <div class="modal-overlay"></div>
  <div class="modal-content">
    <div class="modal-header">
      <h2 class="star-name">★ Tử Vi ★</h2>
      <button class="modal-close">&times;</button>
    </div>
    <div class="modal-body">
      <!-- Star details -->
    </div>
    <div class="modal-footer">
      <button class="btn btn-primary">Đóng</button>
    </div>
  </div>
</div>
```

---

## 5. RESPONSIVE DESIGN

### 5.1 Breakpoints

```css
/* Mobile First */
:root {
  --breakpoint-sm: 576px;   /* Small phones */
  --breakpoint-md: 768px;   /* Tablets */
  --breakpoint-lg: 992px;   /* Laptops */
  --breakpoint-xl: 1200px;  /* Desktops */
}

/* Media Queries */
/* Mobile (default) */
.chart-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 2px;
}

.palace-card {
  min-width: 80px;
  min-height: 100px;
  font-size: 10px;
}

/* Tablet */
@media (min-width: 768px) {
  .palace-card {
    min-width: 120px;
    min-height: 140px;
    font-size: 12px;
  }
}

/* Desktop */
@media (min-width: 992px) {
  .main-layout {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 24px;
  }
  
  .palace-card {
    min-width: 150px;
    min-height: 180px;
    font-size: 14px;
  }
}
```

### 5.2 Mobile Layout

```
┌──────────────────────────────┐
│         HEADER               │
├──────────────────────────────┤
│                              │
│    ┌────────────────────┐   │
│    │    INPUT FORM      │   │
│    │  [Day][Month][Year]│   │
│    │  [Hour ▼]          │   │
│    │  [Nam] [Nữ]        │   │
│    │  [LẬP LÁ SỐ]       │   │
│    └────────────────────┘   │
│                              │
├──────────────────────────────┤
│                              │
│    ┌────────────────────┐   │
│    │   CHART (4x4)      │   │
│    │ (Scrollable/Zoom)  │   │
│    └────────────────────┘   │
│                              │
├──────────────────────────────┤
│                              │
│    ┌────────────────────┐   │
│    │   INTERPRETATION   │   │
│    │   (Collapsible)    │   │
│    └────────────────────┘   │
│                              │
├──────────────────────────────┤
│         FOOTER               │
└──────────────────────────────┘
```

### 5.3 Touch Interactions (Mobile)

| Gesture | Action |
|---------|--------|
| Tap on Palace | Show palace detail modal |
| Tap on Star | Show star detail tooltip |
| Pinch to Zoom | Zoom in/out chart |
| Swipe Left/Right | Switch between Chart and Interpretation tabs |
| Pull Down | Refresh chart |

---

## 6. ACCESSIBILITY

### 6.1 WCAG 2.1 Compliance

| Criterion | Level | Implementation |
|-----------|-------|----------------|
| 1.1.1 Non-text Content | A | Alt text for all icons |
| 1.3.1 Info and Relationships | A | Semantic HTML, ARIA labels |
| 1.4.3 Contrast | AA | Min 4.5:1 for text |
| 2.1.1 Keyboard | A | All interactive elements focusable |
| 2.4.4 Link Purpose | A | Descriptive link text |
| 3.1.1 Language | A | lang="vi" on html |
| 4.1.2 Name, Role, Value | A | ARIA attributes |

### 6.2 ARIA Labels

```html
<!-- Chart Grid -->
<div class="chart-grid" 
     role="grid" 
     aria-label="Lá số Tử Vi 12 cung">
  
  <div class="palace-card" 
       role="gridcell"
       aria-label="Cung Mệnh, cung Dần, có các sao: Tử Vi hóa Lộc, Văn Xương"
       tabindex="0">
    ...
  </div>
</div>

<!-- Star with Tu Hoa -->
<span class="star" 
      role="button"
      aria-label="Sao Tử Vi, độ sáng Miếu, Hóa Lộc"
      tabindex="0">
  Tử Vi 🟢
</span>

<!-- Modal -->
<div class="modal" 
     role="dialog" 
     aria-modal="true"
     aria-labelledby="modal-title">
  <h2 id="modal-title">Chi tiết sao Tử Vi</h2>
</div>
```

### 6.3 Keyboard Navigation

| Key | Action |
|-----|--------|
| Tab | Navigate between interactive elements |
| Enter/Space | Activate button/link |
| Escape | Close modal |
| Arrow Keys | Navigate within chart grid |

### 6.4 Screen Reader Text

```html
<!-- Visually hidden but read by screen readers -->
<span class="sr-only">
  Tử Vi là sao Chính Tinh, độ sáng Miếu, đang Hóa Lộc
</span>

<style>
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
</style>
```

---

## 📊 UI CHECKLIST

| Category | Item | Status |
|----------|------|--------|
| **Colors** | Primary palette defined | ✅ |
| | Ngũ Hành colors | ✅ |
| | Tứ Hóa colors | ✅ |
| | Contrast check (AA) | ⬜ |
| **Typography** | Vietnamese font (Segoe UI/Tahoma) | ✅ |
| | Font scale defined (13px/16px) | ✅ |
| **Layout** | Desktop wireframe | ✅ |
| | Tablet wireframe | ⬜ |
| | Mobile wireframe | ✅ |
| **Components** | Buttons | ✅ |
| | Inputs | ✅ |
| | Cards | ✅ |
| | Modals | ✅ |
| **Responsive** | Breakpoints defined | ✅ |
| | Mobile layout | ✅ |
| | Touch gestures | ✅ |
| **Accessibility** | ARIA labels | ✅ |
| | Keyboard nav | ✅ |
| | Screen reader | ✅ |

---

*UI/UX Specifications - Phiên bản 1.0*

