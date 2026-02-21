import json
import os
import sys

# Add project root to path
sys.path.insert(0, os.getcwd())

from vi_dieu_phap.data.citta_master import CITTA_MASTER
from vi_dieu_phap.data.cetasika_master import CETASIKA_MASTER
from vi_dieu_phap.data.rupa_master import RUPA_MASTER
from vi_dieu_phap.data.nibbana_master import NIBBANA_MASTER

OUTPUT_DIR = "vi_dieu_phap/data/json"

def save_json(data, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved {filepath}")

if __name__ == "__main__":
    save_json(CITTA_MASTER, "citta.json")
    save_json(CETASIKA_MASTER, "cetasika.json")
    save_json(RUPA_MASTER, "rupa.json")
    save_json(NIBBANA_MASTER, "nibbana.json")
