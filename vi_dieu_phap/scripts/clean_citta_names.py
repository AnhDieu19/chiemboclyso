import json
import re

INPUT_FILE = 'python/vi_dieu_phap/data/json/citta.json'
OUTPUT_FILE = 'python/vi_dieu_phap/data/json/citta.json'

def load_data():
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(data)} items to {OUTPUT_FILE}")

def clean_name(item):
    name = item['name']
    short = item['short_name']
    
    # Logic: Prefer 'name' but remove prefix "Tâm " to make it shorter for Label
    # Example: "Tâm Đại Thiện Hợp Trí..." -> "Đại Thiện Hợp Trí..."
    
    # 1. Kama Sobhana (Dai Thien, Dai Qua, Dai Duy Tac)
    if "Đại Thiện" in name or "Đại Quả" in name or "Đại Duy Tác" in name:
        new_short = name.replace("Tâm ", "")
        # Remove "Thọ " to make it even shorter? User said "tên tiếng việt", let's keep it descriptive but remove "Tâm"
        item['short_name'] = new_short
        
    # 2. Ahetuka (Vo Nhan)
    # Ex: "Nhãn Thức Thọ Xả (Quả Bất Thiện)" -> Keep as is (remove "Tâm " if exists)
    # Currently name is "Nhãn Thức Thọ Xả...". Short is "Nhãn (QBThiện)". 
    # User wants descriptive name sans numbers. 
    # Let's use `name` but remove "Tâm " prefix.
    elif item['group'] == 'Ahetuka':
        item['short_name'] = name.replace("Tâm ", "")

    # 3. Rupa (Sac Gioi)
    # Ex: "Tâm Sơ Thiền..." -> "Sơ Thiền..."
    elif "Thiền" in name:
        item['short_name'] = name.replace("Tâm ", "")

    # 4. Arupa (Vo Sac)
    # Ex: "Tâm Thiện Không Vô Biên Xứ" -> "Thiện Không Vô Biên Xứ"
    elif item['plane'] == 'Arupavacara':
        item['short_name'] = name.replace("Tâm ", "")

    # 5. Lokuttara (Sieu The)
    # Ex: "Tâm Sơ Đạo (Magga)" -> "Sơ Đạo (Magga)"
    elif item['plane'] == 'Lokuttara':
        item['short_name'] = name.replace("Tâm ", "")
        
    # 6. Akusala (Bat Thien) - Tham/San/Si
    # Already processed manually or via prev script?
    # Name: "Tâm Tham Thọ Hỷ..." -> "Tham Thọ Hỷ..."
    elif item['group'] == 'Akusala':
         # If current short_name is nice (no numbers), keep it or use full name minus "Tâm"
         # Current: "Tham (Hỷ-Tà-Không)" -> Nice and short.
         # Full: "Tâm Tham Thọ Hỷ Hợp Tà Không Trợ"
         # User request: "dùng tên tiếng việt". 
         # "Tham (Hỷ-Tà-Không)" is Vietnamese enough? 
         # Or does user mean "Tham Thọ Hỷ Hợp Tà Không Trợ"?
         # Let's switch to FULL Descriptive Name minus "Tâm" to be safe and "tooltip giai thich".
         item['short_name'] = name.replace("Tâm ", "")

    # Clean up double spaces
    item['short_name'] = re.sub(r'\s+', ' ', item['short_name']).strip()
    
    # Ensure description exists
    if not item.get('description'):
        item['description'] = f"{item['name']} ({item.get('name_pali', '')})"

def process():
    data = load_data()
    for item in data:
        clean_name(item)
    save_data(data)

if __name__ == "__main__":
    process()
