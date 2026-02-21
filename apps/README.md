# 📱 Tu Vi Frontend Applications

Thư mục này tổ chức các ứng dụng frontend thành các app độc lập.

## Cấu trúc

```
apps/
├── tuvi-web/          # Web app chính (Flask templates + static)
├── hexagram-viz/      # Quẻ Dịch visualization (standalone HTML/JS)
├── acupoints-viz/     # Huyệt đạo visualization (standalone HTML/JS)  
├── math-viz/          # Toán học visualization (standalone HTML/JS)
├── octonion-viz/      # Bát nguyên visualization (standalone HTML/JS)
└── README.md          # File này
```

## Mô tả từng app

### 🌟 tuvi-web (Main Web App)
- **Loại**: Flask web app (server-rendered templates)
- **Nguồn**: `frontend/templates/` + `frontend/static/`
- **Port**: Served through API Gateway (port 5001)
- **Mô tả**: Giao diện web chính cho Tử Vi, bao gồm lập lá số, tra cứu, phân tích

### 🔮 hexagram-viz (Quẻ Dịch)
- **Loại**: Standalone static HTML/JS/CSS
- **Nguồn**: `hexagram_viz/`
- **Mô tả**: Visualization 64 quẻ Dịch, Hà Đồ, Lạc Thư
- **Chạy**: Mở `index.html` trực tiếp hoặc dùng HTTP server

### 📍 acupoints-viz (Huyệt Đạo)
- **Loại**: Standalone static HTML/JS/CSS  
- **Nguồn**: `acupoints_viz/`
- **Mô tả**: 3D visualization các huyệt đạo trên cơ thể
- **Chạy**: Mở `index.html` trực tiếp hoặc dùng HTTP server

### 📐 math-viz (Toán Lý Số)
- **Loại**: Standalone static HTML/JS/CSS
- **Nguồn**: `math_viz/`
- **Mô tả**: Visualization các khái niệm toán học trong Tử Vi
- **Chạy**: Mở `index.html` trực tiếp hoặc dùng HTTP server

### 🎱 octonion-viz (Bát Nguyên)
- **Loại**: Standalone static HTML/JS/CSS
- **Nguồn**: `octonion_viz/`
- **Mô tả**: Visualization Octonion / Bát nguyên số
- **Chạy**: Mở `index.html` trực tiếp hoặc dùng HTTP server

## Cách chạy

### Static apps (hexagram, acupoints, math, octonion)
```bash
# Dùng Python HTTP server
cd apps/hexagram-viz
python -m http.server 8080

# Hoặc dùng Node.js
npx serve .
```

### Main web app (tuvi-web)
```bash
# Chạy qua API Gateway (monolith mode)
python run_monolith.py

# Hoặc microservice mode
python run_all.py
```

## Thêm app mới

1. Tạo thư mục mới trong `apps/`
2. Thêm `README.md` mô tả app
3. Nếu là static app: thêm `index.html` + assets
4. Nếu là Flask app: thêm `app.py` + templates
5. Cập nhật file `apps/README.md` này
