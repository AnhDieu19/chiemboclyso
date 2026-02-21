import json
import os
from typing import List, Dict, Any, Optional, Set, Tuple
from vi_dieu_phap.domain.models import Node, Link, GraphData


class JsonRepository:
    """
    Repository that loads Vi Diệu Pháp data from JSON files
    and constructs a complete Knowledge Graph.

    Features:
    - Lazy-loaded, cached graph data (computed once)
    - Rule-engine based hierarchy matching for Citta
    - Deduplication of links
    """

    def __init__(self, data_dir: Optional[str] = None):
        if data_dir is None:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.data_dir = os.path.abspath(os.path.join(current_dir, '..', 'data', 'json'))
        else:
            self.data_dir = data_dir

        print(f"DEBUG: JsonRepository LOADED. Data Dir: {self.data_dir}")

        # Raw data containers
        self.citta: List[Dict] = []
        self.cetasika: List[Dict] = []
        self.rupa: List[Dict] = []
        self.nibbana: List[Dict] = []
        self.categories: List[Dict] = []
        self.citta_cetasika: List[Dict] = []
        self.vedana: List[Dict] = []
        self.hetu: List[Dict] = []
        self.rules: List[Dict] = []

        # Cached graph
        self._cached_graph: Optional[GraphData] = None

        self._load_data()

        if self.cetasika:
            print(f"DEBUG: First Cetasika loaded: {self.cetasika[0]}")

    def _load_data(self):
        """Load all JSON data files."""
        self.categories = self._read_json('categories.json')
        self.citta = self._read_json('citta.json')
        self.cetasika = self._read_json('cetasika.json')
        self.rupa = self._read_json('rupa.json')
        self.nibbana = self._read_json('nibbana.json')
        self.citta_cetasika = self._read_json('citta_cetasika.json')
        self.vedana = self._read_json('master_vedana.json')
        self.hetu = self._read_json('master_hetu.json')
        self.rules = self._read_json('rules_hierarchy.json')

    def _read_json(self, filename: str) -> List[Dict[str, Any]]:
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"WARNING: File not found: {filepath}")
            return []
        except json.JSONDecodeError as e:
            print(f"ERROR: Invalid JSON in {filepath}: {e}")
            return []
        except Exception as e:
            print(f"ERROR: Reading {filepath}: {e}")
            return []

    def invalidate_cache(self):
        """Clear cached graph data (call after data changes)."""
        self._cached_graph = None

    def get_all_data(self) -> GraphData:
        """Build and return the complete graph. Cached after first call."""
        if self._cached_graph is not None:
            return self._cached_graph
        self._cached_graph = self._build_graph()
        return self._cached_graph

    def _build_graph(self) -> GraphData:
        """Build the complete knowledge graph using Rule Engine logic."""
        nodes: List[Node] = []
        links: List[Link] = []
        existing_node_ids: Set[str] = set()
        link_set: Set[Tuple[str, str, str]] = set()

        def add_node(node: Node):
            if node.id not in existing_node_ids:
                nodes.append(node)
                existing_node_ids.add(node.id)

        def add_link(source: str, target: str, link_type: str):
            key = (source, target, link_type)
            if key not in link_set:
                links.append(Link(source=source, target=target, type=link_type))
                link_set.add(key)

        # --- Pre-compute lookups ---
        vedana_map = {v['id']: v for v in self.vedana}
        rule_map = {r['id']: r for r in self.rules}

        rule_depth_cache: Dict[str, int] = {}
        for rule in self.rules:
            rule_depth_cache[rule['id']] = self._compute_rule_depth(rule, rule_map)

        cetasika_to_hetu: Dict[str, str] = {}
        for h in self.hetu:
            cet_id = h.get("cetasika_id")
            if cet_id:
                cetasika_to_hetu[cet_id] = h["id"]

        # ===== 1. Categories =====
        for cat in self.categories:
            add_node(Node(
                id=cat["id"], name=cat["name"], type=cat["type"],
                group="Structure", val=20 if cat["type"] == 'category' else 15
            ))
            if cat.get("parent_id"):
                add_link(cat["parent_id"], cat["id"], "structure")

        # ===== 2. Rules (Hierarchy Nodes) =====
        for rule in self.rules:
            add_node(Node(
                id=rule['id'], name=rule['name'],
                type=rule.get('type', 'sub_category'),
                group=rule.get('group', 'Structure'), val=15
            ))
            if rule.get('parent_id'):
                add_link(rule['parent_id'], rule['id'], "structure")

        # ===== 3. Citta (Consciousness) =====
        for cit in self.citta:
            name = cit.get("name", "")
            group = cit.get("group", "")
            plane = cit.get("plane", "")

            best_rule = self._match_citta_to_rule(name, group, plane, rule_depth_cache)
            parent_id = best_rule['id'] if best_rule else "CAT_TÂM_CITTA"
            cit_group = best_rule.get('group', group) if best_rule else group

            v_name, v_color = None, None
            vedana_id = cit.get("vedana_id")
            if vedana_id and vedana_id in vedana_map:
                v_name = vedana_map[vedana_id]["name"]
                v_color = vedana_map[vedana_id].get("color", "")

            add_node(Node(
                id=cit["id"],
                name=cit.get("short_name", cit["name"]),
                name_pali=cit.get("name_pali", ""),
                type="citta", group=cit_group, plane=plane,
                description=cit.get("description", ""),
                val=10, vedana=v_name, vedana_color=v_color
            ))
            add_link(parent_id, cit["id"], "structure")

            # Association: Citta -> Cetasika (from factors)
            factors = cit.get("factors", [])
            for cet_id in factors:
                add_link(cit["id"], cet_id, "association")

            # Root cause: Citta -> Hetu (via factors that map to hetu)
            for fid in factors:
                if fid in cetasika_to_hetu:
                    add_link(cit["id"], cetasika_to_hetu[fid], "root_cause")

        # ===== 4. Cetasika =====
        cetasika_groups: Dict[str, str] = {}
        for cet in self.cetasika:
            g_name = cet["group"]
            if g_name not in cetasika_groups:
                gid = f"GRP_CET_{g_name}"
                cetasika_groups[g_name] = gid
                add_node(Node(id=gid, name=g_name, type="sub_category", group="Cetasika", val=15))
                add_link("CAT_SỞ_HỮU_TÂM_CETASIKA", gid, "structure")

            add_node(Node(
                id=cet["id"], name=cet["name"], name_pali=cet.get("name_pali"),
                type="cetasika", group=cet["group"], val=8
            ))
            add_link(cetasika_groups[g_name], cet["id"], "structure")

        # ===== 5. Rupa =====
        rupa_groups: Dict[str, str] = {}
        for rup in self.rupa:
            g_name = rup["group"]
            if g_name not in rupa_groups:
                gid = f"GRP_RUP_{g_name}"
                rupa_groups[g_name] = gid
                add_node(Node(id=gid, name=g_name, type="sub_category", group="Rupa", val=15))
                add_link("CAT_SẮC_PHÁP_RUPA", gid, "structure")

            add_node(Node(
                id=rup["id"], name=rup["name"], name_pali=rup.get("name_pali"),
                type="rupa", group=rup["group"],
                description=rup.get("description", ""), val=8
            ))
            add_link(rupa_groups[g_name], rup["id"], "structure")

        # ===== 6. Nibbana =====
        for nib in self.nibbana:
            add_node(Node(
                id=nib["id"], name=nib["name"], name_pali=nib.get("name_pali"),
                type="nibbana", group="Nibbana",
                description=nib.get("description", ""), val=15
            ))
            add_link("CAT_NIẾT_BÀN_NIBBĀNA", nib["id"], "structure")

        # ===== 7. Hetu (Roots) =====
        for h in self.hetu:
            add_node(Node(
                id=h["id"], name=h["name"], type="hetu", group="Root",
                description=h.get("description", ""), val=25
            ))

        result = GraphData(nodes=nodes, links=links)
        stats = result.stats
        print(f"DEBUG REPO: Built graph - {stats['total_nodes']} nodes, {stats['total_links']} links", flush=True)
        print(f"  Link types: {stats['link_types']}", flush=True)

        return result

    @staticmethod
    def _compute_rule_depth(rule: Dict, rule_map: Dict[str, Dict]) -> int:
        """Pre-compute depth of a rule in the hierarchy (with cycle protection)."""
        depth = 0
        pid = rule.get('parent_id')
        visited: Set[str] = set()
        while pid and pid not in visited:
            visited.add(pid)
            if pid in rule_map:
                pid = rule_map[pid].get('parent_id')
                depth += 1
            else:
                break
        return depth

    def _match_citta_to_rule(self, name: str, group: str, plane: str,
                              depth_cache: Dict[str, int]) -> Optional[Dict]:
        """Find the deepest matching rule for a Citta."""
        best_rule = None
        max_depth = -1

        for rule in self.rules:
            criteria = rule.get('criteria', {})

            if 'group' in criteria and criteria['group'] != group:
                continue
            if 'plane' in criteria and criteria['plane'] != plane:
                continue

            if 'name_contains' in criteria:
                val = criteria['name_contains']
                vals = val if isinstance(val, list) else [val]
                if not all(v in name for v in vals):
                    continue

            if 'name_contains_any' in criteria:
                if not any(v in name for v in criteria['name_contains_any']):
                    continue

            if 'name_not_contains' in criteria:
                val = criteria['name_not_contains']
                vals = val if isinstance(val, list) else [val]
                if any(v in name for v in vals):
                    continue

            depth = depth_cache.get(rule['id'], 0)
            if depth > max_depth:
                max_depth = depth
                best_rule = rule

        return best_rule
