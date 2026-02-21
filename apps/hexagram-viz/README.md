# Hexagram Visualization - Quẻ Dịch

Ứng dụng visualization 64 quẻ Dịch, Hà Đồ, Lạc Thư.

## Nguồn gốc
Thư mục gốc: `hexagram_viz/`

## Cấu trúc
```
hexagram-viz/
├── index.html          # Trang chính
├── style.css           # Styles
├── script.js           # Main script
├── hexagrams.json      # Dữ liệu 64 quẻ
├── trigrams_hetu.json  # Dữ liệu Hà Đồ bát quái
├── css/                # Additional styles
├── js/                 # Additional scripts
└── data/               # Additional data
```

## Chạy
```bash
cd hexagram_viz
python -m http.server 8081
```

Truy cập: http://localhost:8081

## Tính năng
- Hiển thị 64 quẻ Dịch
- Bát quái Hà Đồ / Lạc Thư
- Interactive visualization
