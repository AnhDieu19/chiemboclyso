import json
import os
import uuid

DATA_DIR = 'python/vi_dieu_phap/data/json'

def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(filename, data):
    with open(os.path.join(DATA_DIR, filename), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(data)} items to {filename}")

def migrate():
    # Load raw entity data
    citta = load_json('citta.json')
    cetasika = load_json('cetasika.json')
    rupa = load_json('rupa.json')
    nibbana = load_json('nibbana.json')

    categories = []
    category_map = {} # name -> id to avoid duplicates

    def ensure_category(name, cat_type, parent_id=None, level_prefix="CAT"):
        # Generate ID based on name or simple slug
        # But we need consistent IDs.
        # Let's simple check if exists by name/parent combo? 
        # For simplicity, we create a deterministic ID or use what we used in Repo logic
        
        # Simple slug
        slug = name.upper().replace(' ', '_').replace('(', '').replace(')', '').replace('-', '_')
        cat_id = f"{level_prefix}_{slug}"
        
        # Check duplicate IDs with different parents? 
        # For this dataset, names are mostly unique enough or we append parent.
        if cat_id in category_map:
            return category_map[cat_id]
        
        cat = {
            "id": cat_id,
            "name": name,
            "type": cat_type,
            "parent_id": parent_id
        }
        categories.append(cat)
        category_map[cat_id] = cat_id
        return cat_id

    # 1. ROOT
    root_id = "ROOT"
    categories.append({"id": root_id, "name": "Bốn Pháp Siêu Lý (Paramattha)", "type": "root", "parent_id": None})

    # 2. Main Categories
    cat_citta = ensure_category("Tâm (Citta)", "category", root_id, "CAT")
    cat_cetasika = ensure_category("Sở Hữu Tâm (Cetasika)", "category", root_id, "CAT")
    cat_rupa = ensure_category("Sắc Pháp (Rupa)", "category", root_id, "CAT")
    cat_nibbana = ensure_category("Niết Bàn (Nibbāna)", "category", root_id, "CAT")

    # 3. Process Citta Hierarchy (Re-implement logic from Repository to generate STATIC categories)
    new_citta = []
    citta_cetasika_relations = []
    
    for c in citta:
        # Re-create the logic to find parent_id
        group = c["group"]
        plane = c.get("plane", "Unknown")
        name = c["name"]
        
        # L1
        l1_id = None
        l1_name = plane
        if group == "Akusala": l1_name = "Bất Thiện (Akusala)"
        elif group == "Ahetuka": l1_name = "Vô Nhân (Ahetuka)"
        elif plane == "Kamavacara" and "Kusala" in group: l1_name = "Dục Giới Tịnh Hảo (Thiện)"
        elif plane == "Kamavacara" and "Vipaka" in group: l1_name = "Dục Giới Tịnh Hảo (Quả)"
        elif plane == "Kamavacara" and "Kiriya" in group: l1_name = "Dục Giới Tịnh Hảo (Duy Tác)"
        elif plane == "Rupavacara": l1_name = "Sắc Giới (Rupa)"
        elif plane == "Arupavacara": l1_name = "Vô Sắc Giới (Arupa)"
        elif plane == "Lokuttara": l1_name = "Siêu Thế (Lokuttara)"
        
        l1_id = ensure_category(l1_name, "sub_category", cat_citta, "L1")
        parent_id = l1_id
        
        # L2 & L3 Logic
        if group == "Akusala":
            if "Tham" in name:
                parent_id = ensure_category("Tâm Tham", "sub_category", parent_id, "L2")
                if "Hợp Tà" in name: parent_id = ensure_category("Hợp Tà", "sub_category", parent_id, "L3")
                elif "Ly Tà" in name: parent_id = ensure_category("Ly Tà", "sub_category", parent_id, "L3")
                
                if "Có Trợ" in name or "Hữu Dẫn" in name: parent_id = ensure_category("Có Trợ", "sub_category", parent_id, "L4")
                elif "Không Trợ" in name or "Vô Dẫn" in name: parent_id = ensure_category("Không Trợ", "sub_category", parent_id, "L4")
            elif "Sân" in name:
                 parent_id = ensure_category("Tâm Sân", "sub_category", parent_id, "L2")
                 if "Có Trợ" in name: parent_id = ensure_category("Có Trợ", "sub_category", parent_id, "L3_SAN")
                 elif "Không Trợ" in name: parent_id = ensure_category("Không Trợ", "sub_category", parent_id, "L3_SAN")
            elif "Si" in name:
                 parent_id = ensure_category("Tâm Si", "sub_category", parent_id, "L2")

        elif group == "Ahetuka":
             if "Quả Bất Thiện" in name: parent_id = ensure_category("Quả Bất Thiện", "sub_category", parent_id, "L2")
             elif "Quả Thiện" in name: parent_id = ensure_category("Quả Thiện", "sub_category", parent_id, "L2")
             else: parent_id = ensure_category("Duy Tác Vô Nhân", "sub_category", parent_id, "L2")

        elif plane == "Kamavacara":
             if "Hợp Trí" in name: parent_id = ensure_category("Hợp Trí", "sub_category", parent_id, "L2")
             elif "Ly Trí" in name: parent_id = ensure_category("Ly Trí", "sub_category", parent_id, "L2")
             if "Hữu Dẫn" in name or "Có Trợ" in name: parent_id = ensure_category("Hữu Dẫn", "sub_category", parent_id, "L3")
             elif "Vô Dẫn" in name or "Không Trợ" in name: parent_id = ensure_category("Vô Dẫn", "sub_category", parent_id, "L3")

        elif plane in ["Rupavacara", "Arupavacara"]:
             if "Thiện" in name or "Kusala" in c.get("name_pali", ""): parent_id = ensure_category("Thiện", "sub_category", parent_id, f"L2_{plane}")
             elif "Quả" in name or "Vipaka" in c.get("name_pali", ""): parent_id = ensure_category("Quả", "sub_category", parent_id, f"L2_{plane}")
             elif "Duy Tác" in name or "Tác" in c.get("name_pali", ""): parent_id = ensure_category("Duy Tác", "sub_category", parent_id, f"L2_{plane}")

        elif plane == "Lokuttara":
             if "Đạo" in name: parent_id = ensure_category("Đạo (Magga)", "sub_category", parent_id, "L2")
             elif "Quả" in name: parent_id = ensure_category("Quả (Phala)", "sub_category", parent_id, "L2")

        # Create Normalized Entity
        ent = c.copy()
        ent['parent_id'] = parent_id
        if 'factors' in ent:
            for fac in ent['factors']:
                citta_cetasika_relations.append({
                    "citta_id": ent['id'],
                    "cetasika_id": fac
                })
            del ent['factors']
        new_citta.append(ent)
        
    # 4. Process Cetasika
    new_cetasika = []
    for c in cetasika:
        # Simple grouping by 'group' field
        g_name = c["group"]
        cat_id = ensure_category(g_name, "sub_category", cat_cetasika, "GRP_CET")
        
        ent = c.copy()
        ent['parent_id'] = cat_id
        new_cetasika.append(ent)

    # 5. Process Rupa
    new_rupa = []
    for r in rupa:
        g_name = r["group"]
        cat_id = ensure_category(g_name, "sub_category", cat_rupa, "GRP_RUP")
        
        ent = r.copy()
        ent['parent_id'] = cat_id
        new_rupa.append(ent)
        
    # 6. Process Nibbana
    new_nibbana = []
    for n in nibbana:
        # Direct child of Nibbana Category specificed in Categories
        # But wait, we define category for Nibbana as distinct
        # Nibbana entity has group 'Nibbana'
        ent = n.copy()
        ent['parent_id'] = cat_nibbana
        new_nibbana.append(ent)

    # SAVE ALL TABLES
    save_json('categories.json', categories)
    save_json('citta.json', new_citta)
    save_json('cetasika.json', new_cetasika)
    save_json('rupa.json', new_rupa)
    save_json('nibbana.json', new_nibbana)
    save_json('citta_cetasika.json', citta_cetasika_relations)

if __name__ == "__main__":
    migrate()
