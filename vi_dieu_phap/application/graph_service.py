from typing import Dict, Any, List, Optional
from vi_dieu_phap.domain.models import Node, Link, GraphData
from vi_dieu_phap.infrastructure.json_repository import JsonRepository


class GraphService:
    """
    Application service that provides filtered graph views.
    Caches filtered results for performance.
    """

    def __init__(self, repository: JsonRepository):
        self.repository = repository
        # Cached filtered graphs
        self._cache: Dict[str, Dict[str, Any]] = {}

    def _get_cached_or_build(self, key: str, builder) -> Dict[str, Any]:
        """Generic cache-or-build pattern."""
        if key not in self._cache:
            self._cache[key] = builder()
        return self._cache[key]

    def get_full_data(self) -> Dict[str, Any]:
        """Return the complete graph data."""
        return self._get_cached_or_build('full', self._build_full)

    def get_structure_graph(self) -> Dict[str, Any]:
        """Return only structure (hierarchy) links and connected nodes."""
        return self._get_cached_or_build('structure', self._build_structure)

    def get_association_graph(self) -> Dict[str, Any]:
        """Return only association links (Citta <-> Cetasika) and connected nodes."""
        return self._get_cached_or_build('association', self._build_association)

    def get_root_cause_graph(self) -> Dict[str, Any]:
        """Return only root_cause links (Citta -> Hetu) and connected nodes."""
        return self._get_cached_or_build('root_cause', self._build_root_cause)

    def get_stats(self) -> Dict[str, Any]:
        """Return graph statistics."""
        data = self.repository.get_all_data()
        return data.stats

    # --- Private builders ---

    def _build_full(self) -> Dict[str, Any]:
        return self.repository.get_all_data().to_dict()

    def _build_structure(self) -> Dict[str, Any]:
        data = self.repository.get_all_data()
        return self._filter_by_link_type(data, 'structure')

    def _build_association(self) -> Dict[str, Any]:
        data = self.repository.get_all_data()
        return self._filter_by_link_type(data, 'association')

    def _build_root_cause(self) -> Dict[str, Any]:
        data = self.repository.get_all_data()
        return self._filter_by_link_type(data, 'root_cause')

    @staticmethod
    def _filter_by_link_type(data: GraphData, link_type: str) -> Dict[str, Any]:
        """Filter graph to only include links of a specific type and their connected nodes."""
        filtered_links = [l for l in data.links if l.type == link_type]

        connected_ids = set()
        for l in filtered_links:
            connected_ids.add(l.source)
            connected_ids.add(l.target)

        filtered_nodes = [n for n in data.nodes if n.id in connected_ids]
        return GraphData(filtered_nodes, filtered_links).to_dict()
