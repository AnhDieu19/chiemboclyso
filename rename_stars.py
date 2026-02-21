"""Bulk rename star names to match tuvinamphai.vn convention"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))

# Mapping: old_name -> new_name
RENAMES = {
    'Phục Binh': 'Phúc Bình',
    'Bác Sỹ': 'Bác Sĩ',
    'Kình Dương': 'Kinh Dương',
    'Lực Sỹ': 'Lục Sĩ',
    'Tử Phù': 'Từ Phù',
    'Tả Phù': 'Tả Phụ',
    'Thiên Thương': 'Thiên Thường',
    'Tấu Thư': 'Tàu Thu',
    'Thai Phụ': 'Thái Phụ',
    'Thiên Hỷ': 'Thiên Hỹ',
    # Compound variants
    'Lưu Kình Dương': 'Lưu Kinh Dương',
    'L.Kình Dương': 'L.Kinh Dương',
    'Lưu Tử Phù': 'Lưu Từ Phù',
    # Garbled entry cleanup
    'T奏 Thư': 'Tàu Thu',
    # Module/section name references
    'BÁC SỸ': 'BÁC SĨ',
    'Bác Sỹ Ring': 'Bác Sĩ Ring',
    'Bác Sỹ ring': 'Bác Sĩ ring',
    'Vòng Bác Sỹ': 'Vòng Bác Sĩ',
}

# Directories to process
DIRS = ['python', 'backend', 'frontend']
EXTENSIONS = {'.py', '.html', '.js', '.json'}

def process_file(filepath):
    """Replace all old names with new names in a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except (UnicodeDecodeError, PermissionError):
        return 0
    
    original = content
    changes = 0
    
    # Apply replacements (longest first to avoid partial matches)
    for old, new in sorted(RENAMES.items(), key=lambda x: -len(x[0])):
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            changes += count
    
    if changes > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  {os.path.relpath(filepath, ROOT)}: {changes} replacements")
    
    return changes

def main():
    total = 0
    files_changed = 0
    
    for dir_name in DIRS:
        dir_path = os.path.join(ROOT, dir_name)
        if not os.path.exists(dir_path):
            continue
        for root, dirs, files in os.walk(dir_path):
            # Skip __pycache__
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for fname in files:
                ext = os.path.splitext(fname)[1]
                if ext in EXTENSIONS:
                    fpath = os.path.join(root, fname)
                    n = process_file(fpath)
                    if n > 0:
                        total += n
                        files_changed += 1
    
    print(f"\nDone: {total} replacements in {files_changed} files")

if __name__ == '__main__':
    main()
