import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from vi_dieu_phap.infrastructure.json_repository import JsonRepository

def verify():
    print("Initializing Repository...")
    repo = JsonRepository()
    print(f"Stats:")
    print(f"  Citta: {len(repo.citta)}")
    print(f"  Mappings: {len(repo.citta_cetasika)}")
    
    data = repo.get_all_data()
    print(f"Graph Data:")
    print(f"  Nodes: {len(data.nodes)}")
    print(f"  Links: {len(data.links)}")
    
    assoc_links = [l for l in data.links if l.type == 'association']
    print(f"  Association Links: {len(assoc_links)}")
    
    if len(assoc_links) > 0:
        print("  Sample Link:", assoc_links[0])

if __name__ == "__main__":
    verify()
