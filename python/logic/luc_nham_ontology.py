"""
ĐẠI LỤC NHÂM — BẢN THỂ LUẬN (ONTOLOGY MODULE)
═══════════════════════════════════════════════════════════════════════════════
Thiết kế Bản thể luận cho Đồ Thị Tri Thức Lượng Tử - Siêu Hình.
Tích hợp RDF/OWL/LPG (Labeled Property Graph) để mô phỏng Knowledge Graph.

Implements:
  - Entity Classes: EarthlyBranch, HeavenlyStem, SiKe_Anchor,
    SanChuan_Transmission, VedicDeva_Particle, QuantumForce_Field,
    Loka_Dimension, Interaction_Event
  - RDF Reification cho trạng thái song song Cát/Hung
  - Algorithm 2: Tứ Khóa CASE WHEN operational_strategy
  - Algorithm 3: Tam Truyền Vedic force routing
    (Samprasadagati / Saparayanagati)
  - Knowledge Graph builder (nodes + edges) cho in-memory graph
═══════════════════════════════════════════════════════════════════════════════
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# ═══════════════════════════════════════════════════════════════════════════════
# 1. SPATIOTEMPORAL CLASSES — Cấu Trúc Thời-Không
# ═══════════════════════════════════════════════════════════════════════════════

# --- Thiên Can (10 Hạt Khối Lượng Cơ Sở) ---

HEAVENLY_STEM_DATA = [
    # (name, han, wu_xing, yin_yang, symbolic_meaning, quantum_charge_ratio, vedic_mass_particle)
    ('Giáp', '甲', 'Mộc', 'Dương', 'Áo giáp chiến binh – Khai mở, xung phong',
     '+7/11', 'Dharma-bīja (Hạt giống Pháp)'),
    ('Ất', '乙', 'Mộc', 'Âm', 'Dây leo uốn lượn – Mềm dẻo, linh hoạt',
     '-4/11', 'Prāṇa-sūkṣma (Vi tế khí)'),
    ('Bính', '丙', 'Hỏa', 'Dương', 'Ngọn lửa rực rỡ – Quang minh, phát tán',
     '+6/11', 'Tejas-aṇu (Hỏa vi tử)'),
    ('Đinh', '丁', 'Hỏa', 'Âm', 'Đinh sắt gắn kết – Tụ hội, kiên cố',
     '-5/11', 'Agni-bindu (Hỏa điểm)'),
    ('Mậu', '戊', 'Thổ', 'Dương', 'Vỏ rùa bảo hộ – Nền tảng, kiên cố',
     '+5/11', 'Pṛthivī-tattva (Địa đại)'),
    ('Kỷ', '己', 'Thổ', 'Âm', 'Sợi tơ xe kéo – Kết nối, mạng lưới',
     '-6/11', 'Kṣiti-paramāṇu (Địa nguyên tử)'),
    ('Canh', '庚', 'Kim', 'Dương', 'Lưỡi rìu kép – Phán xét, quyết đoán',
     '+4/11', 'Vajra-dhātu (Kim cương giới)'),
    ('Tân', '辛', 'Kim', 'Âm', 'Mũi kim châm cứu – Tinh xảo, sắc sảo',
     '-7/11', 'Śūnya-bindu (Không điểm)'),
    ('Nhâm', '壬', 'Thủy', 'Dương', 'Dòng sông phong bế – Vận chuyển, lưu thông',
     '+3/11', 'Āpas-tattva (Thủy đại)'),
    ('Quý', '癸', 'Thủy', 'Âm', 'Giọt sương mai – Tinh khiết, ẩn tàng',
     '-8/11', 'Soma-rasa (Cam lộ)'),
]


@dataclass
class HeavenlyStem:
    """
    Class: HeavenlyStem (≅ MassParticle)
    Đại diện cho 10 hạt khối lượng cơ sở của Thiên Can.
    """
    index: int
    name: str
    han: str
    wu_xing: str
    yin_yang: str
    symbolic_meaning: str
    quantum_charge_ratio: str
    vedic_mass_particle: str

    @property
    def node_id(self) -> str:
        return f"HeavenlyStem_{self.index}_{self.name}"

    @property
    def labels(self) -> List[str]:
        return ['HeavenlyStem', 'MassParticle']

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': self.labels,
            'index': self.index,
            'name': self.name,
            'han': self.han,
            'wu_xing': self.wu_xing,
            'yin_yang': self.yin_yang,
            'symbolic_meaning': self.symbolic_meaning,
            'quantum_charge_ratio': self.quantum_charge_ratio,
            'vedic_mass_particle': self.vedic_mass_particle,
        }


# --- Địa Chi (12 Trục Không Gian) ---

EARTHLY_BRANCH_DATA = [
    # (name, han, wu_xing, yin_yang, spatial_deg, animal, direction)
    ('Tý',   '子', 'Thủy', 'Dương',   0, 'Chuột', 'Bắc'),
    ('Sửu',  '丑', 'Thổ',  'Âm',     30, 'Trâu',  'Đông Bắc'),
    ('Dần',  '寅', 'Mộc',  'Dương',  60, 'Hổ',    'Đông Bắc'),
    ('Mão',  '卯', 'Mộc',  'Âm',     90, 'Thỏ',   'Đông'),
    ('Thìn', '辰', 'Thổ',  'Dương', 120, 'Rồng',  'Đông Nam'),
    ('Tỵ',   '巳', 'Hỏa',  'Âm',    150, 'Rắn',   'Đông Nam'),
    ('Ngọ',  '午', 'Hỏa',  'Dương', 180, 'Ngựa',  'Nam'),
    ('Mùi',  '未', 'Thổ',  'Âm',    210, 'Dê',    'Tây Nam'),
    ('Thân', '申', 'Kim',  'Dương', 240, 'Khỉ',   'Tây Nam'),
    ('Dậu',  '酉', 'Kim',  'Âm',    270, 'Gà',    'Tây'),
    ('Tuất', '戌', 'Thổ',  'Dương', 300, 'Chó',   'Tây Bắc'),
    ('Hợi',  '亥', 'Thủy', 'Âm',    330, 'Heo',   'Tây Bắc'),
]


@dataclass
class EarthlyBranch:
    """
    Class: EarthlyBranch (≅ QuantumSpoke)
    Đại diện cho 12 nhánh không gian, mang spin_state đối xứng.
    """
    index: int
    name: str
    han: str
    wu_xing: str
    yin_yang: str
    spatial_degree: int
    animal: str
    direction: str
    spin_state: str = 'Opposite_To_Mate'

    @property
    def node_id(self) -> str:
        return f"EarthlyBranch_{self.index}_{self.name}"

    @property
    def labels(self) -> List[str]:
        return ['EarthlyBranch', 'QuantumSpoke']

    @property
    def mate_index(self) -> int:
        """Chỉ số đối xung (cách 6 cung)"""
        return (self.index + 6) % 12

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': self.labels,
            'index': self.index,
            'name': self.name,
            'han': self.han,
            'wu_xing': self.wu_xing,
            'yin_yang': self.yin_yang,
            'spatial_degree': self.spatial_degree,
            'spin_state': self.spin_state,
            'animal': self.animal,
            'direction': self.direction,
        }


# ═══════════════════════════════════════════════════════════════════════════════
# 2. DYNAMIC STRUCTURAL CLASSES — Cấu Trúc Động Lực Học
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class SiKe_Anchor:
    """
    Class: SiKe_Anchor (Nút neo Tứ Khóa)
    Subclasses:
      - Origin_Essence (K1: Từ Can Ngày 1 — Bản chất)
      - Persistence_Continuity (K2: Từ Chi Ngày 2 — Sự tiếp diễn)
      - Present_Trigger (K3: Từ Can Giờ 1 — Tác nhân)
      - Future_Drift (K4: Từ Chi Giờ 2 — Khuynh hướng)
    """
    khoa_num: int
    role: str                # 'Origin_Essence', 'Persistence_Continuity', ...
    role_vi: str             # Tên tiếng Việt
    thuong_than: str         # Thượng Thần (Thiên Can/Chi trên)
    ha_than: str             # Hạ Thần (Thiên Can/Chi dưới)
    wu_xing_thuong: str
    wu_xing_ha: str
    relation: str            # sinh/khac/hoa/bi_sinh/bi_khac
    score: int
    strength: str            # 'Strong' / 'Weak' / 'Neutral'

    @property
    def node_id(self) -> str:
        return f"SiKe_K{self.khoa_num}_{self.role}"

    @property
    def labels(self) -> List[str]:
        return ['SiKe_Anchor', self.role]

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': self.labels,
            'khoa_num': self.khoa_num,
            'role': self.role,
            'role_vi': self.role_vi,
            'thuong_than': self.thuong_than,
            'ha_than': self.ha_than,
            'wu_xing_thuong': self.wu_xing_thuong,
            'wu_xing_ha': self.wu_xing_ha,
            'relation': self.relation,
            'score': self.score,
            'strength': self.strength,
        }


SIKE_ROLES = {
    1: ('Origin_Essence', 'Bản Chất Nội Tại',
        'Nguồn gốc sâu xa, nền tảng cốt lõi của sự việc'),
    2: ('Persistence_Continuity', 'Hoàn Cảnh Khách Quan',
        'Sự tiếp diễn và ràng buộc từ bên ngoài'),
    3: ('Present_Trigger', 'Động Lực Kích Hoạt',
        'Tác nhân bùng phát, yếu tố thời cơ hiện tại'),
    4: ('Future_Drift', 'Khuynh Hướng Tương Lai',
        'Xu hướng phát triển và đích đến'),
}


@dataclass
class SanChuan_Transmission:
    """
    Class: SanChuan_Transmission (Quỹ đạo Tam Truyền)
    Subclasses: Initial_Phase, Middle_Phase, Final_Phase
    Mỗi phase mang lực Vệ Đà và quantum phase tương ứng.
    """
    phase: str               # 'Initial_Phase', 'Middle_Phase', 'Final_Phase'
    phase_vi: str
    chi_name: str
    chi_han: str
    wu_xing: str
    than_tuong: str
    # Vedic force routing
    vedic_deity: str         # Brahma / Vishnu / Shiva
    quantum_phase: str       # Superposition→Collapse / Unitary Evolution / Eigenstate
    # Force calculations
    vedic_force_type: str    # 'Samprasadagati' / 'Saparayanagati' / 'Neutral'
    force_weight: float      # Trọng số lực tích lũy
    rudra_perturbation: float  # Nhiễu loạn từ Thần Tướng

    @property
    def node_id(self) -> str:
        return f"SanChuan_{self.phase}_{self.chi_name}"

    @property
    def labels(self) -> List[str]:
        return ['SanChuan_Transmission', self.phase]

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': self.labels,
            'phase': self.phase,
            'phase_vi': self.phase_vi,
            'chi_name': self.chi_name,
            'chi_han': self.chi_han,
            'wu_xing': self.wu_xing,
            'than_tuong': self.than_tuong,
            'vedic_deity': self.vedic_deity,
            'quantum_phase': self.quantum_phase,
            'vedic_force_type': self.vedic_force_type,
            'force_weight': round(self.force_weight, 3),
            'rudra_perturbation': round(self.rudra_perturbation, 3),
            'net_force': round(self.force_weight + self.rudra_perturbation, 3),
        }


# ═══════════════════════════════════════════════════════════════════════════════
# 3. VEDIC QUANTUM INTERACTIONS
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class VedicDeva_Particle:
    """
    Class: VedicDeva_Particle
    33 hạt quan sát được (Vasu_Gluon, Rudra_Electromagnetic, Aditya_Photon, ...)
    Mapped từ 12 Thần Tướng.
    """
    than_tuong: str
    han: str
    particle: str
    vedic_entity: str
    subclass: str            # 'Vasu_Gluon' / 'Rudra_Electromagnetic' / 'Aditya_Photon' / 'Ashvinau_Spin'
    tinh_chat: str           # đại_cát / cát / trung / hung / đại_hung
    ngu_hanh: str
    rudra_moment: float      # Mô-men từ tính (nhiễu loạn Rudra)

    @property
    def node_id(self) -> str:
        return f"VedicDeva_{self.than_tuong}"

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': ['VedicDeva_Particle', self.subclass],
            'than_tuong': self.than_tuong,
            'han': self.han,
            'particle': self.particle,
            'vedic_entity': self.vedic_entity,
            'subclass': self.subclass,
            'tinh_chat': self.tinh_chat,
            'ngu_hanh': self.ngu_hanh,
            'rudra_moment': round(self.rudra_moment, 3),
        }


# Mapping Thần Tướng → Vedic Subclass + Rudra moment
THAN_TUONG_VEDIC_MAP = {
    'Quý Nhân':   ('Aditya_Photon',         +1.0),
    'Đằng Xà':    ('Vasu_Gluon',            -0.7),
    'Chu Tước':    ('Rudra_Electromagnetic', -0.5),
    'Lục Hợp':    ('Aditya_Photon',         +0.6),
    'Câu Trận':   ('Vasu_Gluon',            -0.3),
    'Thanh Long':  ('Aditya_Photon',         +0.9),
    'Thiên Không': ('Ashvinau_Spin',          0.0),
    'Bạch Hổ':    ('Rudra_Electromagnetic', -0.8),
    'Thái Thường': ('Ashvinau_Spin',         +0.4),
    'Huyền Vũ':   ('Vasu_Gluon',            -0.6),
    'Thái Âm':    ('Ashvinau_Spin',         +0.3),
    'Thiên Hậu':  ('Aditya_Photon',         +0.7),
}


@dataclass
class QuantumForce_Field:
    """
    Class: QuantumForce_Field
    5 lực chi phối các cạnh (edges) trong đồ thị.
    """
    force_type: str           # Samprasadagati_Sheng / Saparayanagati_Ke / ...
    force_vi: str
    wu_xing_source: str
    wu_xing_target: str
    coupling_constant: float  # Hằng số ghép nối
    vedic_force: str          # Tên lực Vệ Đà

    @property
    def node_id(self) -> str:
        return f"Force_{self.force_type}_{self.wu_xing_source}_{self.wu_xing_target}"

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': ['QuantumForce_Field', self.force_type],
            'force_type': self.force_type,
            'force_vi': self.force_vi,
            'wu_xing_source': self.wu_xing_source,
            'wu_xing_target': self.wu_xing_target,
            'coupling': round(self.coupling_constant, 4),
            'vedic_force': self.vedic_force,
        }


# Mapping Ngũ Hành quan hệ → QuantumForce_Field
FORCE_FIELD_MAP = {
    'sinh':    ('Samprasadagati_Sheng', 'Tương Sinh', 'Samprasadagati (Proximity-Distance)', +1.0),
    'bi_sinh': ('Samprasadagati_Sheng', 'Bị Sinh',    'Samprasadagati (nhận năng lượng)',     +0.7),
    'hoa':     ('Nityagati_Confinement', 'Hòa Hợp',   'Nityagati (ổn định nội tại)',          +0.5),
    'bi_khac': ('Saparayanagati_Ke',    'Bị Khắc',    'Saparayanagati (bị phân rã)',         -0.7),
    'khac':    ('Saparayanagati_Ke',     'Tương Khắc', 'Saparayanagati (Distance-Distance)',  -1.0),
}


@dataclass
class Loka_Dimension:
    """
    Class: Loka_Dimension
    Cấu trúc không gian đa chiều — điểm nối trung tâm.
    """
    loka_name: str
    description: str
    dimension_level: int  # 1-7 (Bhur → Satya)

    def to_dict(self) -> Dict:
        return {
            'node_id': f"Loka_{self.loka_name}",
            'labels': ['Loka_Dimension'],
            'loka_name': self.loka_name,
            'description': self.description,
            'dimension_level': self.dimension_level,
        }


LOKA_DIMENSIONS = [
    Loka_Dimension('Bhur_Loka', 'Vật chất hữu hình - Hiện thực trần thế', 1),
    Loka_Dimension('Bhuvar_Loka', 'Không gian trung gian - Năng lượng tinh tế', 2),
    Loka_Dimension('Svar_Loka', 'Thiên giới - Ý thức siêu việt', 3),
    Loka_Dimension('Mahar_Loka', 'Giới trí tuệ - Tầm nhìn vĩ mô', 4),
    Loka_Dimension('Jana_Loka', 'Giới sáng tạo - Nguồn sinh lực', 5),
    Loka_Dimension('Tapo_Loka', 'Giới tu luyện - Chuyển hóa nghiệp', 6),
    Loka_Dimension('Satya_Loka', 'Chân lý tối thượng - Brahman', 7),
]


# ═══════════════════════════════════════════════════════════════════════════════
# 4. RDF REIFICATION — Interaction_Event
# ═══════════════════════════════════════════════════════════════════════════════

@dataclass
class Interaction_Event:
    """
    RDF Reification: Vật thể hóa mối quan hệ thành một nút sự kiện.
    Giải quyết nghịch lý đa trạng thái Cát/Hung trên cùng một tọa độ.

    Thay vì triplet đơn:
      (Gui_Water) --> (Chen_Storage)
    Tạo nút sự kiện mới:
      Interaction_Event_001 --> Gui_Water
      Interaction_Event_001 --> Chen_Storage
      Interaction_Event_001 --> "Tương Khắc" (Saparayanagati)
      Interaction_Event_001 --> "Nguyệt Tướng" (Samprasadagati)
    """
    event_id: str
    event_type: str          # 'Lục Nhâm Tương Tác' / 'Quantum Entanglement'
    source_node: str         # Node A (Thiên Chi trên)
    target_node: str         # Node B (Địa Chi dưới)
    than_tuong: str          # Thần Tướng tại vị trí
    # Dual states
    cat_factors: List[str] = field(default_factory=list)
    hung_factors: List[str] = field(default_factory=list)
    cat_weight: float = 0.0  # Tổng trọng số cát
    hung_weight: float = 0.0  # Tổng trọng số hung
    # Force vectors
    samprasadagati_force: float = 0.0  # Lực tương sinh
    saparayanagati_force: float = 0.0  # Lực tương khắc
    rudra_perturbation: float = 0.0    # Nhiễu loạn điện từ Thần Tướng

    @property
    def node_id(self) -> str:
        return f"Interaction_{self.event_id}"

    @property
    def net_probability(self) -> float:
        """Xác suất nghiêng về Cát (>0) hay Hung (<0)"""
        total = abs(self.cat_weight) + abs(self.hung_weight)
        if total == 0:
            return 0.0
        return (self.cat_weight - self.hung_weight) / total

    @property
    def state_label(self) -> str:
        p = self.net_probability
        if p >= 0.5:
            return 'Đại Cát'
        elif p >= 0.15:
            return 'Cát'
        elif p >= -0.15:
            return 'Trung Tính'
        elif p >= -0.5:
            return 'Hung'
        else:
            return 'Đại Hung'

    def to_dict(self) -> Dict:
        return {
            'node_id': self.node_id,
            'labels': ['Interaction_Event', 'Quantum_Entanglement'],
            'event_type': self.event_type,
            'source_node': self.source_node,
            'target_node': self.target_node,
            'than_tuong': self.than_tuong,
            'cat_factors': self.cat_factors,
            'hung_factors': self.hung_factors,
            'cat_weight': round(self.cat_weight, 3),
            'hung_weight': round(self.hung_weight, 3),
            'net_probability': round(self.net_probability, 3),
            'state_label': self.state_label,
            'forces': {
                'samprasadagati': round(self.samprasadagati_force, 3),
                'saparayanagati': round(self.saparayanagati_force, 3),
                'rudra_perturbation': round(self.rudra_perturbation, 3),
                'net_force': round(
                    self.samprasadagati_force +
                    self.saparayanagati_force +
                    self.rudra_perturbation, 3
                ),
            },
        }


# ═══════════════════════════════════════════════════════════════════════════════
# 5. KNOWLEDGE GRAPH BUILDER
# ═══════════════════════════════════════════════════════════════════════════════

class KnowledgeGraphBuilder:
    """
    Xây dựng Knowledge Graph (in-memory) từ bàn thức Lục Nhâm.
    Kết hợp tất cả entity classes và RDF Reification.
    """

    def __init__(self, engine):
        """
        Args:
            engine: Instance của LucNhamEngine đã tính toán xong
        """
        self.engine = engine
        self.nodes: List[Dict] = []
        self.edges: List[Dict] = []
        self.interaction_events: List[Interaction_Event] = []
        self.sike_anchors: List[SiKe_Anchor] = []
        self.sanchuan_transmissions: List[SanChuan_Transmission] = []
        self.vedic_particles: List[VedicDeva_Particle] = []
        self.force_fields: List[QuantumForce_Field] = []

    def build(self) -> Dict:
        """Build complete Knowledge Graph"""
        self._init_static_entities()
        self._build_sike_anchors()
        self._build_sanchuan_transmissions()
        self._build_interaction_events()
        self._build_vedic_particles()
        self._compute_operational_strategy()
        self._compute_vedic_force_routing()

        return {
            'graph_summary': self._get_summary(),
            'static_entities': {
                'heavenly_stems': [
                    HeavenlyStem(i, *d).to_dict()
                    for i, d in enumerate(HEAVENLY_STEM_DATA)
                ],
                'earthly_branches': [
                    EarthlyBranch(i, *d).to_dict()
                    for i, d in enumerate(EARTHLY_BRANCH_DATA)
                ],
                'loka_dimensions': [l.to_dict() for l in LOKA_DIMENSIONS],
            },
            'sike_anchors': [a.to_dict() for a in self.sike_anchors],
            'operational_strategy': self.operational_strategy,
            'sanchuan_transmissions': [t.to_dict() for t in self.sanchuan_transmissions],
            'vedic_force_routing': self.vedic_routing_summary,
            'interaction_events': [e.to_dict() for e in self.interaction_events],
            'vedic_particles': [p.to_dict() for p in self.vedic_particles],
            'force_fields': [f.to_dict() for f in self.force_fields],
            'nodes': self.nodes,
            'edges': self.edges,
        }

    # ── Initialize Static Entities ──────────────────────────────────────────

    def _init_static_entities(self):
        """Algorithm 1: Khởi tạo thực thể đồng cấu Khối Lượng và Không Gian"""
        # 10 Heavenly Stems (Mass Particles)
        for i, d in enumerate(HEAVENLY_STEM_DATA):
            stem = HeavenlyStem(i, *d)
            self.nodes.append(stem.to_dict())

        # 12 Earthly Branches (Quantum Spokes)
        for i, d in enumerate(EARTHLY_BRANCH_DATA):
            branch = EarthlyBranch(i, *d)
            self.nodes.append(branch.to_dict())

            # Edge: EarthlyBranch <--> opposite mate (spin entanglement)
            mate_idx = (i + 6) % 12
            if i < mate_idx:
                self.edges.append({
                    'type': 'SPIN_ENTANGLED',
                    'source': branch.node_id,
                    'target': f"EarthlyBranch_{mate_idx}_{EARTHLY_BRANCH_DATA[mate_idx][0]}",
                    'properties': {'entanglement': 'Opposite_Spin'},
                })

        # 7 Loka Dimensions
        for loka in LOKA_DIMENSIONS:
            self.nodes.append(loka.to_dict())

    # ── Build Tứ Khóa Anchors (Algorithm 2) ────────────────────────────────

    def _build_sike_anchors(self):
        """
        Algorithm 2: Xây dựng và phân luồng Tứ Khóa (Si Ke Logic)
        Tạo 4 nút neo với strength và role phân loại.
        """
        for khoa_data in self.engine.tu_khoa:
            k_num = khoa_data['khoa']
            role_name, role_vi, _ = SIKE_ROLES[k_num]

            # Determine strength
            score = khoa_data['diem']
            if score >= 2:
                strength = 'Strong'
            elif score <= -2:
                strength = 'Weak'
            else:
                strength = 'Neutral'

            anchor = SiKe_Anchor(
                khoa_num=k_num,
                role=role_name,
                role_vi=role_vi,
                thuong_than=khoa_data['thuong_ten'],
                ha_than=khoa_data['ha_ten'],
                wu_xing_thuong=khoa_data['ngu_hanh_thuong'],
                wu_xing_ha=khoa_data['ngu_hanh_ha'],
                relation=khoa_data['quan_he'],
                score=score,
                strength=strength,
            )
            self.sike_anchors.append(anchor)
            self.nodes.append(anchor.to_dict())

            # Edge: SiKe → EarthlyBranch (plate condition)
            self.edges.append({
                'type': 'ANCHORED_ON',
                'source': anchor.node_id,
                'target': f"EarthlyBranch_{khoa_data.get('ha_chi_idx', 0)}_{khoa_data['ha_ten']}",
                'properties': {'relation': khoa_data['quan_he']},
            })

    def _compute_operational_strategy(self):
        """
        Algorithm 2 Extension: CASE WHEN operational_strategy
        Cypher-style branching logic cho chiến lược hành động.
        """
        if len(self.sike_anchors) < 4:
            self.operational_strategy = {
                'strategy': 'Insufficient_Data',
                'strategy_vi': 'Không đủ dữ liệu',
                'description': 'Cần đủ 4 khóa để phân tích.',
            }
            return

        origin = self.sike_anchors[0]    # K1: Day_Stem_1
        persist = self.sike_anchors[1]   # K2: Day_Stem_2
        trigger = self.sike_anchors[2]   # K3: Hour_Stem_1
        drift = self.sike_anchors[3]     # K4: Hour_Stem_2

        # CASE WHEN branching (from ontology doc Algorithm 2)
        if origin.strength == 'Strong' and trigger.strength == 'Weak':
            strategy = 'Delay_or_Prepare'
            strategy_vi = 'Trì Hoãn & Chuẩn Bị'
            desc = ('Nền tảng (K1) vững chắc nhưng thời cơ (K3) chưa chín. '
                    'Tích lũy lực lượng, chờ đợi tín hiệu kích hoạt mới.')
            icon = '⏳'
            muc_do = 'Cát (chờ)'

        elif origin.strength == 'Weak' and trigger.strength == 'Strong':
            strategy = 'Seize_Narrow_Window'
            strategy_vi = 'Chớp Thời Cơ Hẹp'
            desc = ('Nền tảng (K1) yếu nhưng cửa sổ thời cơ (K3) đang mở rộng. '
                    'Phải hành động ngay — cơ hội sẽ không chờ đợi!')
            icon = '🎯'
            muc_do = 'Cát (gấp)'

        elif (origin.strength == 'Strong' and trigger.strength == 'Strong'
              and origin.wu_xing_thuong == trigger.wu_xing_thuong):
            strategy = 'Proceed_With_Precision'
            strategy_vi = 'Tiến Hành Chính Xác'
            desc = ('Nền tảng (K1) và thời cơ (K3) đều mạnh + đồng hành cùng cấu trúc. '
                    'Đại cát — hành động mạnh mẽ và có chủ đích.')
            icon = '⚡'
            muc_do = 'Đại Cát'

        elif origin.strength == 'Strong' and trigger.strength == 'Strong':
            strategy = 'Proceed_With_Caution'
            strategy_vi = 'Tiến Hành Thận Trọng'
            desc = ('Cả K1 và K3 mạnh nhưng khác cấu trúc Ngũ Hành. '
                    'Lực nhiều nhưng hướng khác → cần lọc qua Nhân Bàn trước khi quyết.')
            icon = '⚡'
            muc_do = 'Cát'

        else:
            strategy = 'Filter_Via_Earth_And_Human_Plates'
            strategy_vi = 'Lọc Qua Địa Bàn & Nhân Bàn'
            desc = ('Cả nền tảng lẫn thời cơ ở trạng thái không rõ ràng. '
                    'Phải phân tích sâu qua cấu trúc Bàn Thức 12 cung trước khi quyết.')
            icon = '🔍'
            muc_do = 'Trung Tính'

        # Supplement with K2 (persistence) and K4 (drift)
        drift_note = ''
        if drift.strength == 'Strong' and drift.score > 0:
            drift_note = 'Xu hướng tương lai (K4) tích cực — kết quả dài hạn khả quan.'
        elif drift.strength == 'Weak' or drift.score < 0:
            drift_note = 'Lưu ý: Xu hướng tương lai (K4) tiêu cực — cần đề phòng hậu quả.'

        persist_note = ''
        if persist.strength == 'Weak':
            persist_note = 'Hoàn cảnh bên ngoài (K2) bất lợi — rào cản nhiều.'
        elif persist.strength == 'Strong':
            persist_note = 'Hoàn cảnh (K2) thuận lợi — môi trường hỗ trợ.'

        self.operational_strategy = {
            'strategy': strategy,
            'strategy_vi': strategy_vi,
            'icon': icon,
            'muc_do': muc_do,
            'description': desc,
            'drift_note': drift_note,
            'persist_note': persist_note,
            'origin_strength': origin.strength,
            'trigger_strength': trigger.strength,
            'persist_strength': persist.strength,
            'drift_strength': drift.strength,
            'cypher_pattern': (
                f"MATCH (origin:SiKe_Anchor {{role: 'Origin_Essence', strength: '{origin.strength}'}}) "
                f"MATCH (trigger:SiKe_Anchor {{role: 'Present_Trigger', strength: '{trigger.strength}'}}) "
                f"→ operational_strategy = '{strategy}'"
            ),
        }

    # ── Build Tam Truyền Transmissions (Algorithm 3) ────────────────────────

    def _build_sanchuan_transmissions(self):
        """
        Algorithm 3: Điều hướng Tam Truyền thông qua trường lực Vệ Đà.
        Mỗi phase nhận Vedic force routing: Samprasadagati (sinh) / Saparayanagati (khắc).
        """
        from data.luc_nham_tables import (
            get_ngu_hanh_relation, get_relation_score,
            THAP_NHI_THAN_TUONG,
        )

        phases = [
            ('so_truyen',   'Initial_Phase', 'Sơ Truyền',
             'Superposition → Collapse', 'Brahma (Tạo)'),
            ('trung_truyen', 'Middle_Phase', 'Trung Truyền',
             'Unitary Evolution',         'Vishnu (Duy trì)'),
            ('mat_truyen',   'Final_Phase',  'Mạt Truyền',
             'Eigenstate',                'Shiva (Hủy/Tái sinh)'),
        ]

        prev_wu_xing = None
        cumulative_force = 0.0

        for key, phase, phase_vi, quantum_phase, vedic_deity in phases:
            tt = self.engine.tam_truyen[key]
            wu_xing = tt['ngu_hanh']
            than_tuong = tt['than_tuong']
            than_info = THAP_NHI_THAN_TUONG.get(than_tuong, {})

            # Determine Vedic force type from Ngũ Hành relation
            if prev_wu_xing:
                relation = get_ngu_hanh_relation(prev_wu_xing, wu_xing)
            else:
                # Sơ Truyền: relation to K1 (origin)
                if self.engine.tu_khoa:
                    relation = get_ngu_hanh_relation(
                        self.engine.tu_khoa[0]['ngu_hanh_thuong'], wu_xing
                    )
                else:
                    relation = 'hoa'

            # Map to Vedic force
            force_info = FORCE_FIELD_MAP.get(relation, FORCE_FIELD_MAP['hoa'])
            vedic_force_type = force_info[0]
            base_weight = force_info[3]

            # Rudra electromagnetic perturbation from Thần Tướng
            vedic_map = THAN_TUONG_VEDIC_MAP.get(than_tuong, ('Ashvinau_Spin', 0.0))
            rudra_moment = vedic_map[1]

            # Tinh chất of Thần Tướng adjusts perturbation
            tc = than_info.get('tinh_chat', 'trung')
            if tc == 'đại_cát':
                rudra_perturbation = abs(rudra_moment) * 0.4
            elif tc == 'cát':
                rudra_perturbation = abs(rudra_moment) * 0.2
            elif tc == 'hung':
                rudra_perturbation = -abs(rudra_moment) * 0.3
            elif tc == 'đại_hung':
                rudra_perturbation = -abs(rudra_moment) * 0.5
            else:
                rudra_perturbation = 0.0

            # Cumulative force (bào mòn hoặc gia tốc)
            cumulative_force += base_weight + rudra_perturbation

            transmission = SanChuan_Transmission(
                phase=phase,
                phase_vi=phase_vi,
                chi_name=tt['ten'],
                chi_han=tt['han'],
                wu_xing=wu_xing,
                than_tuong=than_tuong,
                vedic_deity=vedic_deity,
                quantum_phase=quantum_phase,
                vedic_force_type=vedic_force_type,
                force_weight=base_weight,
                rudra_perturbation=rudra_perturbation,
            )
            self.sanchuan_transmissions.append(transmission)
            self.nodes.append(transmission.to_dict())

            # Create force field edge
            if prev_wu_xing:
                ff = QuantumForce_Field(
                    force_type=vedic_force_type,
                    force_vi=force_info[1],
                    wu_xing_source=prev_wu_xing,
                    wu_xing_target=wu_xing,
                    coupling_constant=abs(base_weight),
                    vedic_force=force_info[2],
                )
                self.force_fields.append(ff)
                self.edges.append({
                    'type': vedic_force_type,
                    'source': self.sanchuan_transmissions[-2].node_id
                            if len(self.sanchuan_transmissions) >= 2
                            else 'Origin',
                    'target': transmission.node_id,
                    'properties': ff.to_dict(),
                })

            prev_wu_xing = wu_xing

        # Store cumulative result for routing summary
        self._cumulative_force = cumulative_force

    def _compute_vedic_force_routing(self):
        """Vedic force routing summary: tổng trọng số tại Hậu Truyền"""
        cumulative = getattr(self, '_cumulative_force', 0.0)

        if cumulative >= 1.5:
            verdict = 'Đại Cát — Năng lượng Samprasadagati gia tốc mạnh'
            verdict_en = 'Strong Samprasadagati acceleration → Highly favorable'
        elif cumulative >= 0.5:
            verdict = 'Cát — Lực Samprasadagati duy trì thuận lợi'
            verdict_en = 'Samprasadagati sustaining → Favorable'
        elif cumulative >= -0.5:
            verdict = 'Trung Tính — Lực cân bằng, kết quả phụ thuộc hành động'
            verdict_en = 'Balanced forces → Outcome depends on action'
        elif cumulative >= -1.5:
            verdict = 'Hung — Lực Saparayanagati gây ma sát, cản trở'
            verdict_en = 'Saparayanagati friction → Obstacles ahead'
        else:
            verdict = 'Đại Hung — Saparayanagati phân rã mạnh, tránh hành động'
            verdict_en = 'Strong Saparayanagati decay → Avoid action'

        self.vedic_routing_summary = {
            'cumulative_force': round(cumulative, 3),
            'verdict_vi': verdict,
            'verdict_en': verdict_en,
            'phases': [
                {
                    'phase': t.phase_vi,
                    'force_type': t.vedic_force_type,
                    'weight': round(t.force_weight, 3),
                    'rudra': round(t.rudra_perturbation, 3),
                    'net': round(t.force_weight + t.rudra_perturbation, 3),
                    'vedic_deity': t.vedic_deity,
                }
                for t in self.sanchuan_transmissions
            ],
            'interpretation': (
                f"Hạt (sự kiện) đi từ Sơ Truyền → Trung Truyền → Mạt Truyền. "
                f"Tổng trọng số tích lũy = {round(cumulative, 3)}. "
                f"{'Gia tốc bởi Samprasadagati (tương sinh)' if cumulative > 0 else 'Bào mòn bởi Saparayanagati (tương khắc)'}."
            ),
        }

    # ── Build Interaction Events (RDF Reification) ──────────────────────────

    def _build_interaction_events(self):
        """
        RDF Reification: Tạo Interaction_Event cho mỗi cung trên bàn thức.
        Mỗi event chứa ĐỒNG THỜI cả yếu tố Cát và Hung.
        """
        from data.luc_nham_tables import (
            DIA_CHI, DIA_BAN, THAP_NHI_THAN_TUONG, NGUYET_TUONG_TEN,
            get_dia_chi_ngu_hanh, get_ngu_hanh_relation, get_relation_score,
        )

        for dia_pos in range(12):
            thien_chi_idx = self.engine.thien_ban[dia_pos]
            thien_chi = DIA_CHI[thien_chi_idx]
            dia_chi = DIA_BAN[dia_pos]['chi']
            than_tuong_name = self.engine.than_tuong_map.get(dia_pos, '')
            than_info = THAP_NHI_THAN_TUONG.get(than_tuong_name, {})
            nguyet_tuong = NGUYET_TUONG_TEN.get(thien_chi_idx, '')

            # Ngũ Hành relation
            hanh_thien = get_dia_chi_ngu_hanh(thien_chi_idx)
            hanh_dia = DIA_BAN[dia_pos]['ngu_hanh']
            relation = get_ngu_hanh_relation(hanh_thien, hanh_dia)
            rel_score = get_relation_score(relation)

            # --- Collect CÁT factors ---
            cat_factors = []
            cat_weight = 0.0

            # Tương sinh / hòa
            if relation in ('sinh', 'bi_sinh', 'hoa'):
                cat_factors.append(
                    f"{hanh_thien} {relation} {hanh_dia} "
                    f"(Samprasadagati: năng lượng duy trì)"
                )
                cat_weight += abs(rel_score)

            # Thần Tướng cát
            tc = than_info.get('tinh_chat', 'trung')
            if tc in ('đại_cát', 'cát'):
                cat_factors.append(
                    f"{than_tuong_name} ({than_info.get('y_nghia', '')}) — {tc}")
                cat_weight += 4 if tc == 'đại_cát' else 2

            # Nguyệt Tướng
            if nguyet_tuong:
                cat_factors.append(
                    f"Nguyệt Tướng: {nguyet_tuong} chiếu tại {dia_chi}")
                cat_weight += 1

            # --- Collect HUNG factors ---
            hung_factors = []
            hung_weight = 0.0

            # Tương khắc
            if relation in ('khac', 'bi_khac'):
                hung_factors.append(
                    f"{hanh_thien} {relation} {hanh_dia} "
                    f"(Saparayanagati: phân rã cấu trúc)"
                )
                hung_weight += abs(rel_score)

            # Thần Tướng hung
            if tc in ('đại_hung', 'hung'):
                hung_factors.append(
                    f"{than_tuong_name} ({than_info.get('y_nghia', '')}) — {tc}")
                hung_weight += 4 if tc == 'đại_hung' else 2

            # Rudra perturbation from Thần Tướng
            vedic_data = THAN_TUONG_VEDIC_MAP.get(than_tuong_name, ('', 0.0))
            rudra = vedic_data[1]

            # Force vectors
            force_cfg = FORCE_FIELD_MAP.get(relation, FORCE_FIELD_MAP['hoa'])
            samprasadagati = max(0, force_cfg[3])
            saparayanagati = min(0, force_cfg[3])

            event = Interaction_Event(
                event_id=f"cung_{dia_pos:02d}_{dia_chi}",
                event_type='Lục Nhâm Tương Tác / Quantum Entanglement',
                source_node=f"EarthlyBranch_{thien_chi_idx}_{thien_chi}",
                target_node=f"EarthlyBranch_{dia_pos}_{dia_chi}",
                than_tuong=than_tuong_name,
                cat_factors=cat_factors,
                hung_factors=hung_factors,
                cat_weight=cat_weight,
                hung_weight=hung_weight,
                samprasadagati_force=samprasadagati,
                saparayanagati_force=saparayanagati,
                rudra_perturbation=rudra,
            )
            self.interaction_events.append(event)
            self.nodes.append(event.to_dict())

            # Edges to source/target
            self.edges.append({
                'type': 'REIFIED_INTERACTION',
                'source': event.node_id,
                'target': event.source_node,
                'properties': {'role': 'thien_chi'},
            })
            self.edges.append({
                'type': 'REIFIED_INTERACTION',
                'source': event.node_id,
                'target': event.target_node,
                'properties': {'role': 'dia_chi'},
            })

    # ── Build Vedic Particles ───────────────────────────────────────────────

    def _build_vedic_particles(self):
        """Build VedicDeva_Particle nodes from Thần Tướng map"""
        from data.luc_nham_tables import THAP_NHI_THAN_TUONG

        for pos, name in self.engine.than_tuong_map.items():
            info = THAP_NHI_THAN_TUONG.get(name, {})
            vedic_data = THAN_TUONG_VEDIC_MAP.get(
                name, ('Ashvinau_Spin', 0.0))

            # Get quantum mapping from extra data
            qv = self.engine.__class__._get_quantum_vedic_map(name)

            particle = VedicDeva_Particle(
                than_tuong=name,
                han=info.get('han', ''),
                particle=qv.get('particle', ''),
                vedic_entity=qv.get('vedic', ''),
                subclass=vedic_data[0],
                tinh_chat=info.get('tinh_chat', 'trung'),
                ngu_hanh=info.get('ngu_hanh', ''),
                rudra_moment=vedic_data[1],
            )
            self.vedic_particles.append(particle)
            self.nodes.append(particle.to_dict())

    # ── Summary ─────────────────────────────────────────────────────────────

    def _get_summary(self) -> Dict:
        return {
            'total_nodes': len(self.nodes),
            'total_edges': len(self.edges),
            'entity_types': {
                'HeavenlyStem': 10,
                'EarthlyBranch': 12,
                'SiKe_Anchor': len(self.sike_anchors),
                'SanChuan_Transmission': len(self.sanchuan_transmissions),
                'Interaction_Event': len(self.interaction_events),
                'VedicDeva_Particle': len(self.vedic_particles),
                'QuantumForce_Field': len(self.force_fields),
                'Loka_Dimension': 7,
            },
            'ontology_standard': 'RDF/OWL + LPG (Labeled Property Graph)',
            'reification': 'RDF Reification for dual Cát/Hung quantum states',
        }
