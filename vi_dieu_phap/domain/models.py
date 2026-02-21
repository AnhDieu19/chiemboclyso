from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class Node:
    id: str
    name: str
    type: str  # 'citta', 'cetasika', 'rupa', 'nibbana', 'hetu'
    group: str
    val: int = 5
    name_pali: Optional[str] = None
    description: Optional[str] = None
    # Citta specific
    short_name: Optional[str] = None
    plane: Optional[str] = None
    # Vedana info
    vedana: Optional[str] = None
    vedana_color: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary, excluding None values for cleaner JSON."""
        result = {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'group': self.group,
            'val': self.val,
        }
        if self.name_pali:
            result['name_pali'] = self.name_pali
        if self.description:
            result['description'] = self.description
        if self.short_name:
            result['short_name'] = self.short_name
        if self.plane:
            result['plane'] = self.plane
        if self.vedana:
            result['vedana'] = self.vedana
        if self.vedana_color:
            result['vedana_color'] = self.vedana_color
        return result

@dataclass
class Link:
    source: str
    target: str
    type: str  # 'structure', 'association', 'root_cause'
    value: int = 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            'source': self.source,
            'target': self.target,
            'type': self.type,
            'value': self.value,
        }

@dataclass
class GraphData:
    nodes: List[Node]
    links: List[Link]

    def to_dict(self) -> Dict[str, Any]:
        return {
            'nodes': [n.to_dict() for n in self.nodes],
            'links': [l.to_dict() for l in self.links],
        }

    @property
    def stats(self) -> Dict[str, int]:
        """Return graph statistics."""
        link_types = {}
        for l in self.links:
            link_types[l.type] = link_types.get(l.type, 0) + 1
        node_types = {}
        for n in self.nodes:
            node_types[n.type] = node_types.get(n.type, 0) + 1
        return {
            'total_nodes': len(self.nodes),
            'total_links': len(self.links),
            'node_types': node_types,
            'link_types': link_types,
        }
