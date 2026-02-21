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

def clean_short_name(name):
    # Remove numbers like " 1", " 2" in "Tham 1", "Sân 1"
    # Example: "Tham 1 (Hỷ-Tà-Không)" -> "Tham (Hỷ-Tà-Không)"
    # Example: "Si 1 (Xả-Hoài Nghi)" -> "Si (Xả-Hoài Nghi)"
    return re.sub(r' (\d+) ', ' ', name)

def generate_full_data():
    data = load_data()
    
    # 1. Clean existing Akusala/Ahetuka short_names
    for item in data:
        if item.get('group') in ['Akusala', 'Ahetuka']:
            item['short_name'] = clean_short_name(item['short_name'])

    # 2. Identify missing groups and generate
    # Existing data has ~43 items. We need to preserve them but potentially update them.
    # However, generating missing variants (Vipaka, Kiriya) is key.

    # Extract template for Kamavacara Kusala (Similiar structure for Vipaka/Kiriya)
    # IDs CIT_31 to CIT_38 correspond to 8 Dai Thien
    # We will clone them to create Dai Qua (Vipaka) and Dai Duy Tac (Kiriya)
    
    kusala_templates = [d for d in data if d.get('group') == 'Kusala' and d.get('plane') == 'Kamavacara']
    
    # --- Generate Kama Sobhana Vipaka (8) ---
    next_id = 39 # Assuming CIT_38 is last Kusala
    new_items = []
    
    for tmpl in kusala_templates:
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{next_id:02d}"
        new_item['short_name'] = tmpl['short_name'].replace("Đ.Thiện", "Đ.Quả")
        new_item['name'] = tmpl['name'].replace("Đại Thiện", "Đại Quả")
        new_item['name_pali'] = tmpl['name_pali'].replace("kusala", "vipaka") # Simple heuristic
        new_item['group'] = "Kama-Vipaka" # Distinct group or stick to general 'Vipaka'?
        # Factors might be slightly different but usually identical for Sobhana
        new_items.append(new_item)
        next_id += 1

    # --- Generate Kama Sobhana Kiriya (8) ---
    for tmpl in kusala_templates:
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{next_id:02d}"
        new_item['short_name'] = tmpl['short_name'].replace("Đ.Thiện", "Đ.Duy Tác")
        new_item['name'] = tmpl['name'].replace("Đại Thiện", "Đại Duy Tác")
        new_item['name_pali'] = tmpl['name_pali'].replace("kusala", "kiriya")
        new_item['group'] = "Kama-Kiriya"
        new_items.append(new_item)
        next_id += 1

    # --- Generate Rupa (Fine Material) ---
    # Existing data may have some Rupa Kusala. Let's find them.
    # IDs CIT_39.. are likely occupied by my generation above if I append. 
    # But original data had 43 items. Meaning CIT_39-43 were Rupa Kusala?
    
    # Let's filter out original Rupa Items to regenerate properly or re-id them
    original_rupas = [d for d in data if d.get('plane') == 'Rupavacara']
    # If we have 5, those are likely Kusala.
    
    # Remove original Rupas from 'data' list to re-add them with sorted IDs?
    # Or just keep them and append Vipaka/Kiriya.
    
    # Strategy: Re-build the entire list based on known blocks to ensure ID continuity.
    # 1. Akusala (12)
    # 2. Ahetuka (18)
    # 3. Kama Sobhana (24) = 8 Kusala + 8 Vipaka + 8 Kiriya
    # 4. Rupa (15) = 5 Kusala + 5 Vipaka + 5 Kiriya
    # 5. Arupa (12) = 4 Kusala + 4 Vipaka + 4 Kiriya
    # 6. Lokuttara (8) = 4 Magga + 4 Phala
    
    final_list = []
    
    # helper to find items in original data
    def find_original(condition_func):
        return [d for d in data if condition_func(d)]

    # 1. Akusala (12)
    akusala = find_original(lambda d: d['group'] == 'Akusala')
    final_list.extend(akusala) # IDs CIT_01..12
    
    # 2. Ahetuka (18)
    ahetuka = find_original(lambda d: d['group'] == 'Ahetuka')
    final_list.extend(ahetuka) # IDs CIT_13..30
    
    # 3. Kama Sobhana (24)
    # 3a. Kusala (Original CIT_31..38)
    k_kusala = find_original(lambda d: d.get('group') == 'Kusala' and d.get('plane') == 'Kamavacara')
    final_list.extend(k_kusala)
    
    # 3b. Vipaka (New)
    for i, tmpl in enumerate(k_kusala):
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{39+i:02d}" # 30 + 8 = 38. Next is 39.
        new_item['short_name'] = tmpl['short_name'].replace("Đ.Thiện", "Đ.Quả")
        new_item['name'] = tmpl['name'].replace("Đại Thiện", "Đại Quả")
        new_item['group'] = "Kama-Vipaka"
        final_list.append(new_item)
        
    # 3c. Kiriya (New)
    for i, tmpl in enumerate(k_kusala):
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{47+i:02d}" # 38+8 = 46. Next 47.
        new_item['short_name'] = tmpl['short_name'].replace("Đ.Thiện", "Đ.Tác")
        new_item['name'] = tmpl['name'].replace("Đại Thiện", "Đại Duy Tác")
        new_item['group'] = "Kama-Kiriya"
        final_list.append(new_item)

    # 4. Rupa (15)
    # 4a. Kusala (Original CIT_39..? No, original were separate. Let's find original Rupas)
    r_kusala_orig = find_original(lambda d: d.get('plane') == 'Rupavacara')
    # Assuming these are Kusala.
    
    start_id = 55 # 46+8=54. Next 55.
    r_kusala = []
    for i, tmpl in enumerate(r_kusala_orig):
        tmpl['id'] = f"CIT_{start_id+i:02d}"
        tmpl['group'] = "Rupa-Kusala" 
        r_kusala.append(tmpl)
        final_list.append(tmpl)

    # We need 5 Rupa items. If original data has fewer, we have a problem. 
    # Assuming original has 5 (Sơ thiền -> Ngũ thiền).
    
    # 4b. Vipaka
    for i, tmpl in enumerate(r_kusala):
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{start_id+5+i:02d}"
        new_item['short_name'] = tmpl['short_name'].replace("Thiền", "Quả") # Example: Sơ Thiền -> Sơ Quả (Sắc)
        new_item['name'] = tmpl['name'].replace("Thiện", "Quả")
        new_item['group'] = "Rupa-Vipaka"
        final_list.append(new_item)
        
    # 4c. Kiriya
    for i, tmpl in enumerate(r_kusala):
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{start_id+10+i:02d}"
        new_item['short_name'] = tmpl['short_name'].replace("Thiền", "Tác")
        new_item['name'] = tmpl['name'].replace("Thiện", "Duy Tác")
        new_item['group'] = "Rupa-Kiriya"
        final_list.append(new_item)

    # 5. Arupa (12)
    # Data likely missing entirely. Construct from templates.
    # Base: Không Vô Biên, Thức Vô Biên, Vô Sở Hữu, Phi Tưởng Phi Phi Tưởng.
    arupa_names = [
        ("Không Vô Biên Xứ", "Akasanancayatana"),
        ("Thức Vô Biên Xứ", "Vinnanancayatana"),
        ("Vô Sở Hữu Xứ", "Akincannayatana"),
        ("Phi Tưởng Phi Phi Tưởng Xứ", "Nevasannanasannayatana")
    ]
    
    start_id = 70 # 54 + 15 = 69. Next 70.
    
    # 5a. Kusala
    arupa_kusala = []
    for i, (name, pali) in enumerate(arupa_names):
        item = {
            "id": f"CIT_{start_id+i:02d}",
            "short_name": f"{name} (Thiện)",
            "name": f"Tâm Thiện {name}",
            "name_pali": f"{pali} Kusala Citta",
            "group": "Arupa-Kusala",
            "plane": "Arupavacara",
            "factors": ["CET_34", "CET_35"], # Minimal factors, placeholder
            "val": 10
        }
        arupa_kusala.append(item)
        final_list.append(item)
        
    # 5b. Vipaka
    for i, tmpl in enumerate(arupa_kusala):
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{start_id+4+i:02d}"
        new_item['short_name'] = tmpl['short_name'].replace("Thiện", "Quả")
        new_item['name'] = tmpl['name'].replace("Thiện", "Quả")
        new_item['group'] = "Arupa-Vipaka"
        final_list.append(new_item)

    # 5c. Kiriya
    for i, tmpl in enumerate(arupa_kusala):
        new_item = tmpl.copy()
        new_item['id'] = f"CIT_{start_id+8+i:02d}"
        new_item['short_name'] = tmpl['short_name'].replace("Thiện", "Tác")
        new_item['name'] = tmpl['name'].replace("Thiện", "Duy Tác")
        new_item['group'] = "Arupa-Kiriya"
        final_list.append(new_item)

    # 6. Lokuttara (8) - Sơ Đạo/Quả, Nhị, Tam, Tứ.
    maggas = ["Sơ Đạo", "Nhị Đạo", "Tam Đạo", "Tứ Đạo"]
    maggas_pali = ["Sotapatti Magga", "Sakadagami Magga", "Anagami Magga", "Arahatta Magga"]
    phalas = ["Sơ Quả", "Nhị Quả", "Tam Quả", "Tứ Quả"]
    phalas_pali = ["Sotapatti Phala", "Sakadagami Phala", "Anagami Phala", "Arahatta Phala"]
    
    start_id = 82
    
    for i, name in enumerate(maggas):
        item = {
             "id": f"CIT_{start_id+i:02d}",
             "short_name": name,
             "name": f"Tâm {name} (Magga)",
             "name_pali": maggas_pali[i],
             "group": "Lokuttara-Magga",
             "plane": "Lokuttara",
             "val": 12
        }
        final_list.append(item)

    for i, name in enumerate(phalas):
        item = {
             "id": f"CIT_{start_id+4+i:02d}",
             "short_name": name,
             "name": f"Tâm {name} (Phala)",
             "name_pali": phalas_pali[i],
             "group": "Lokuttara-Phala",
             "plane": "Lokuttara",
             "val": 12
        }
        final_list.append(item)

    save_data(final_list)

if __name__ == "__main__":
    generate_full_data()
