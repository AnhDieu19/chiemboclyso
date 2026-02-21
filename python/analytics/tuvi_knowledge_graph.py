"""
Tử Vi Knowledge Graph
Xây dựng và visualize mối quan hệ giữa các sao, cung, ngũ hành trong Tử Vi Đẩu Số.

Các Node:
- Sao (Stars): 14 Chính Tinh + Phụ Tinh
- Cung (Palaces): 12 cung chức năng
- Ngũ Hành (Elements): Kim, Mộc, Thủy, Hỏa, Thổ
- Can Chi: 10 Thiên Can, 12 Địa Chi

Các Edges:
- sao THUỘC cung (in palace)
- sao THUỘC nhóm ngũ hành
- sao SINH/KHẮC sao
- cung SINH/KHẮC cung
"""
import sys
import os
import json

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import networkx as nx
    import matplotlib.pyplot as plt
    from matplotlib import font_manager
except ImportError:
    print("Cần cài đặt: pip install networkx matplotlib")
    sys.exit(1)

from data.can_chi import THIEN_CAN, DIA_CHI, NGU_HANH
from data.chinh_tinh import CHINH_TINH

# ═══════════════════════════════════════════════════════════════════════════════
# NGŨ HÀNH TƯƠNG SINH TƯƠNG KHẮC
# ═══════════════════════════════════════════════════════════════════════════════
NGU_HANH_SINH = {
    'Kim': 'Thủy', 'Thủy': 'Mộc', 'Mộc': 'Hỏa', 'Hỏa': 'Thổ', 'Thổ': 'Kim'
}
NGU_HANH_KHAC = {
    'Kim': 'Mộc', 'Mộc': 'Thổ', 'Thổ': 'Thủy', 'Thủy': 'Hỏa', 'Hỏa': 'Kim'
}

# Ngũ hành của các Chính Tinh
SAO_NGU_HANH = {
    'Tử Vi': 'Thổ',      # Đế tinh
    'Thiên Cơ': 'Mộc',   # Mưu tinh
    'Thái Dương': 'Hỏa', # Thủ sao có ánh sáng
    'Vũ Khúc': 'Kim',    # Tài tinh
    'Thiên Đồng': 'Thủy', # Phúc tinh
    'Liêm Trinh': 'Hỏa', # Ám tinh
    'Thiên Phủ': 'Thổ',  # Tài khố
    'Thái Âm': 'Thủy',   # Mẫu tinh
    'Tham Lang': 'Thủy', # Đào hoa tinh
    'Cự Môn': 'Thủy',    # Khẩu thiệt tinh
    'Thiên Tướng': 'Thủy', # Ấn tinh
    'Thiên Lương': 'Mộc', # Phúc thọ tinh
    'Thất Sát': 'Kim',   # Sát tinh
    'Phá Quân': 'Thủy',  # Háo tinh
}

# Ngũ hành của 12 Địa Chi (Cung vị)
CHI_NGU_HANH = {
    'Tý': 'Thủy', 'Sửu': 'Thổ', 'Dần': 'Mộc', 'Mão': 'Mộc',
    'Thìn': 'Thổ', 'Tỵ': 'Hỏa', 'Ngọ': 'Hỏa', 'Mùi': 'Thổ',
    'Thân': 'Kim', 'Dậu': 'Kim', 'Tuất': 'Thổ', 'Hợi': 'Thủy'
}

# 12 Cung chức năng
CUNG_NAMES = [
    'Mệnh', 'Phụ Mẫu', 'Phúc Đức', 'Điền Trạch', 'Quan Lộc', 'Nô Bộc',
    'Thiên Di', 'Tật Ách', 'Tài Bạch', 'Tử Tức', 'Phu Thê', 'Huynh Đệ'
]

# Cung đối xứng (Lục Xung)
CUNG_DOI_XUNG = {
    0: 6, 1: 7, 2: 8, 3: 9, 4: 10, 5: 11,
    6: 0, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5
}

# Cung Tam Hợp
CUNG_TAM_HOP = {
    0: [0, 4, 8],   # Tý Thìn Thân (Thủy cục)
    1: [1, 5, 9],   # Sửu Tỵ Dậu (Kim cục)
    2: [2, 6, 10],  # Dần Ngọ Tuất (Hỏa cục)
    3: [3, 7, 11],  # Mão Mùi Hợi (Mộc cục)
}

# Phụ tinh quan trọng
PHU_TINH = {
    'Lục Cát': ['Tả Phụ', 'Hữu Bật', 'Văn Xương', 'Văn Khúc', 'Thiên Khôi', 'Thiên Việt'],
    'Lục Sát': ['Kinh Dương', 'Đà La', 'Hỏa Tinh', 'Linh Tinh', 'Địa Không', 'Địa Kiếp'],
    'Tứ Hóa': ['Hóa Lộc', 'Hóa Quyền', 'Hóa Khoa', 'Hóa Kỵ'],
}


def build_tuvi_knowledge_graph():
    """Xây dựng Knowledge Graph cho Tử Vi"""
    G = nx.DiGraph()
    
    # ═══════════════════════════════════════════════════════════════════════
    # 1. THÊM NODES
    # ═══════════════════════════════════════════════════════════════════════
    
    # Ngũ Hành là nodes trung tâm
    for hanh in NGU_HANH:
        G.add_node(hanh, type='ngu_hanh', color='#FFD700')
    
    # 14 Chính Tinh
    for star in CHINH_TINH['tu_vi_group']:
        G.add_node(star, type='chinh_tinh', group='tu_vi', color='#FF6B6B')
    for star in CHINH_TINH['thien_phu_group']:
        G.add_node(star, type='chinh_tinh', group='thien_phu', color='#4ECDC4')
    
    # 12 Địa Chi (Cung vị)
    for i, chi in enumerate(DIA_CHI):
        G.add_node(chi, type='dia_chi', index=i, color='#95E1D3')
    
    # Phụ tinh
    for group, stars in PHU_TINH.items():
        for star in stars:
            G.add_node(star, type='phu_tinh', group=group, color='#A8D8EA')
    
    # ═══════════════════════════════════════════════════════════════════════
    # 2. THÊM EDGES - MỐI QUAN HỆ
    # ═══════════════════════════════════════════════════════════════════════
    
    # Ngũ Hành Tương Sinh
    for hanh_from, hanh_to in NGU_HANH_SINH.items():
        G.add_edge(hanh_from, hanh_to, relation='sinh', weight=2)
    
    # Ngũ Hành Tương Khắc
    for hanh_from, hanh_to in NGU_HANH_KHAC.items():
        G.add_edge(hanh_from, hanh_to, relation='khac', weight=1.5)
    
    # Sao -> Ngũ Hành (thuộc về)
    for star, hanh in SAO_NGU_HANH.items():
        G.add_edge(star, hanh, relation='thuoc', weight=1)
    
    # Địa Chi -> Ngũ Hành
    for chi, hanh in CHI_NGU_HANH.items():
        G.add_edge(chi, hanh, relation='thuoc', weight=1)
    
    # Sao quan hệ (Sinh/Khắc dựa trên ngũ hành)
    all_stars = list(SAO_NGU_HANH.keys())
    for s1 in all_stars:
        for s2 in all_stars:
            if s1 != s2:
                h1, h2 = SAO_NGU_HANH[s1], SAO_NGU_HANH[s2]
                if NGU_HANH_SINH.get(h1) == h2:
                    G.add_edge(s1, s2, relation='sinh_sao', weight=0.8)
                elif NGU_HANH_KHAC.get(h1) == h2:
                    G.add_edge(s1, s2, relation='khac_sao', weight=0.5)
    
    # Vòng Tử Vi và Thiên Phủ (liên kết nội bộ)
    tu_vi_stars = CHINH_TINH['tu_vi_group']
    for i in range(len(tu_vi_stars) - 1):
        G.add_edge(tu_vi_stars[i], tu_vi_stars[i+1], relation='vong_tuvi', weight=1)
    
    thien_phu_stars = CHINH_TINH['thien_phu_group']
    for i in range(len(thien_phu_stars) - 1):
        G.add_edge(thien_phu_stars[i], thien_phu_stars[i+1], relation='vong_thien_phu', weight=1)
    
    return G


def visualize_ngu_hanh_graph(G, output_path='tuvi_ngu_hanh.png'):
    """Visualize chỉ Ngũ Hành và Tương Sinh/Khắc"""
    # Lọc chỉ Ngũ Hành nodes
    ngu_hanh_nodes = [n for n, d in G.nodes(data=True) if d.get('type') == 'ngu_hanh']
    H = G.subgraph(ngu_hanh_nodes).copy()
    
    plt.figure(figsize=(10, 10))
    
    # Vị trí vòng tròn
    pos = nx.circular_layout(H)
    
    # Màu cho từng hành
    colors = {'Kim': '#FFD700', 'Mộc': '#228B22', 'Thủy': '#1E90FF', 'Hỏa': '#FF4500', 'Thổ': '#8B4513'}
    node_colors = [colors.get(n, '#888888') for n in H.nodes()]
    
    # Vẽ edges
    sinh_edges = [(u, v) for u, v, d in H.edges(data=True) if d.get('relation') == 'sinh']
    khac_edges = [(u, v) for u, v, d in H.edges(data=True) if d.get('relation') == 'khac']
    
    nx.draw_networkx_edges(H, pos, edgelist=sinh_edges, edge_color='green', 
                            arrows=True, arrowsize=20, connectionstyle="arc3,rad=0.1",
                            style='solid', width=2)
    nx.draw_networkx_edges(H, pos, edgelist=khac_edges, edge_color='red', 
                            arrows=True, arrowsize=20, connectionstyle="arc3,rad=-0.2",
                            style='dashed', width=1.5)
    
    # Vẽ nodes
    nx.draw_networkx_nodes(H, pos, node_color=node_colors, node_size=3000)
    nx.draw_networkx_labels(H, pos, font_size=14, font_weight='bold')
    
    plt.title('Ngu Hanh Tuong Sinh Tuong Khac', fontsize=16)
    plt.legend(['Tuong Sinh (xanh)', 'Tuong Khac (do)'], loc='upper left')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


def visualize_chinh_tinh_graph(G, output_path='tuvi_chinh_tinh.png'):
    """Visualize 14 Chính Tinh và Ngũ Hành"""
    # Lọc Chính Tinh + Ngũ Hành
    chinh_tinh_nodes = [n for n, d in G.nodes(data=True) 
                        if d.get('type') in ['chinh_tinh', 'ngu_hanh']]
    H = G.subgraph(chinh_tinh_nodes).copy()
    
    plt.figure(figsize=(14, 14))
    
    # Layout
    pos = nx.spring_layout(H, k=2, iterations=50, seed=42)
    
    # Vẽ edges theo loại
    thuoc_edges = [(u, v) for u, v, d in H.edges(data=True) if d.get('relation') == 'thuoc']
    vong_edges = [(u, v) for u, v, d in H.edges(data=True) 
                  if d.get('relation') in ['vong_tuvi', 'vong_thien_phu']]
    
    nx.draw_networkx_edges(H, pos, edgelist=thuoc_edges, edge_color='#cccccc', 
                            arrows=True, arrowsize=10, alpha=0.5)
    nx.draw_networkx_edges(H, pos, edgelist=vong_edges, edge_color='blue', 
                            arrows=True, arrowsize=15, width=2, alpha=0.7)
    
    # Màu nodes
    node_colors = []
    node_sizes = []
    for n, d in H.nodes(data=True):
        if d.get('type') == 'ngu_hanh':
            node_colors.append('#FFD700')
            node_sizes.append(2500)
        elif d.get('group') == 'tu_vi':
            node_colors.append('#FF6B6B')
            node_sizes.append(1800)
        else:
            node_colors.append('#4ECDC4')
            node_sizes.append(1800)
    
    nx.draw_networkx_nodes(H, pos, node_color=node_colors, node_size=node_sizes)
    nx.draw_networkx_labels(H, pos, font_size=10)
    
    plt.title('14 Chinh Tinh va Ngu Hanh', fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


def visualize_full_graph(G, output_path='tuvi_full_graph.png'):
    """Visualize toàn bộ Knowledge Graph"""
    plt.figure(figsize=(20, 20))
    
    pos = nx.spring_layout(G, k=1.5, iterations=100, seed=42)
    
    # Màu theo type
    type_colors = {
        'ngu_hanh': '#FFD700',
        'chinh_tinh': '#FF6B6B',
        'dia_chi': '#95E1D3',
        'phu_tinh': '#A8D8EA'
    }
    
    node_colors = [type_colors.get(G.nodes[n].get('type', ''), '#888888') for n in G.nodes()]
    node_sizes = [2000 if G.nodes[n].get('type') == 'ngu_hanh' else 1000 for n in G.nodes()]
    
    # Vẽ edges
    nx.draw_networkx_edges(G, pos, alpha=0.3, arrows=True, arrowsize=8)
    
    # Vẽ nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=node_sizes, alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=8)
    
    plt.title('Tu Vi Knowledge Graph', fontsize=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Saved: {output_path}")


def export_graph_json(G, output_path='tuvi_graph.json'):
    """Export graph sang JSON để dùng với D3.js hoặc frontend"""
    data = {
        'nodes': [],
        'links': []
    }
    
    for node, attrs in G.nodes(data=True):
        data['nodes'].append({
            'id': node,
            'type': attrs.get('type', 'unknown'),
            'group': attrs.get('group', ''),
            'color': attrs.get('color', '#888888')
        })
    
    for source, target, attrs in G.edges(data=True):
        data['links'].append({
            'source': source,
            'target': target,
            'relation': attrs.get('relation', ''),
            'weight': attrs.get('weight', 1)
        })
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Saved: {output_path}")
    return data


def print_graph_stats(G):
    """In thống kê graph"""
    print("\n" + "="*60)
    print("TU VI KNOWLEDGE GRAPH - THONG KE")
    print("="*60)
    print(f"So node: {G.number_of_nodes()}")
    print(f"So edge: {G.number_of_edges()}")
    
    # Đếm theo type
    type_counts = {}
    for n, d in G.nodes(data=True):
        t = d.get('type', 'unknown')
        type_counts[t] = type_counts.get(t, 0) + 1
    
    print("\nPhan loai node:")
    for t, count in type_counts.items():
        print(f"  - {t}: {count}")
    
    # Đếm theo relation
    rel_counts = {}
    for u, v, d in G.edges(data=True):
        r = d.get('relation', 'unknown')
        rel_counts[r] = rel_counts.get(r, 0) + 1
    
    print("\nPhan loai quan he:")
    for r, count in sorted(rel_counts.items(), key=lambda x: -x[1]):
        print(f"  - {r}: {count}")
    
    print("="*60 + "\n")


if __name__ == "__main__":
    print("Dang xay dung Tu Vi Knowledge Graph...")
    
    # Build graph
    G = build_tuvi_knowledge_graph()
    print_graph_stats(G)
    
    # Output directory
    output_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Export JSON (cho frontend)
    export_graph_json(G, os.path.join(output_dir, 'tuvi_graph.json'))
    
    # Visualize
    visualize_ngu_hanh_graph(G, os.path.join(output_dir, 'tuvi_ngu_hanh.png'))
    visualize_chinh_tinh_graph(G, os.path.join(output_dir, 'tuvi_chinh_tinh.png'))
    visualize_full_graph(G, os.path.join(output_dir, 'tuvi_full_graph.png'))
    
    print("\nHoan thanh! Kiem tra cac file output.")
