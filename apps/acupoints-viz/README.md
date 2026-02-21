# Acupoints Visualization - Huyệt Đạo 3D

Ứng dụng 3D visualization các huyệt đạo trên cơ thể.

## Nguồn gốc
Thư mục gốc: `acupoints_viz/`

## Cấu trúc
```
acupoints-viz/
├── index.html          # Trang chính (Three.js 3D)
├── css/                # Styles
│   └── style.css
├── js/                 # Scripts
│   ├── main.js
│   ├── scene.js
│   ├── visualization.js
│   └── interactions.js
└── assets/
    └── data/           # Dữ liệu huyệt đạo
```

## Chạy
```bash
cd acupoints_viz
python -m http.server 8082
```

Truy cập: http://localhost:8082

## Tính năng
- 3D human body model
- Interactive acupoint selection
- Meridian pathway visualization
