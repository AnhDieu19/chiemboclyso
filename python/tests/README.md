# Tu Vi App - Test Suite

Thư mục này chứa toàn bộ các script kiểm thử cho dự án Tử Vi Nam Phái.

## Cấu Trúc File
- `data/`: Chứa các file dữ liệu mẫu, log output (.txt).
- `run_all.py`: Script để chạy toàn bộ Unit Tests.
- `test_*.py`: Các Unit Test chuẩn (unittest/pytest).
- `verify_*.py`: Các script kiểm tra logic cụ thể (manual check).

## Hướng Dẫn Chạy Test

### 1. Chạy tất cả test
```bash
python tests/run_all.py
```

### 2. Chạy test cụ thể
```bash
python tests/test_core_engine.py
python tests/verify_user_chart.py
```

## Ghi Chú
- Các file test cần có đoạn code setup `sys.path` ở đầu để import được module từ thư mục cha (`python/`).
