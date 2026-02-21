import json
import os

class VdpRepository:
    def __init__(self, data_dir=None):
        if data_dir is None:
            # Default to json directory relative to this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.data_dir = os.path.join(current_dir, 'data', 'json')
        else:
            self.data_dir = data_dir
            
        self.citta = []
        self.cetasika = []
        self.rupa = []
        self.nibbana = []
        self.categories = []
        self.citta_cetasika = []
        self.vedana = []
        self.hetu = [] # New: Roots
        self.rules = [] # New: Hierarchy Rules
        self._load_data()

    def _load_data(self):
        """Loads data from JSON files (ERD Structure)."""
        self.categories = self._read_json('categories.json')
        self.citta = self._read_json('citta.json')
        self.cetasika = self._read_json('cetasika.json')
        self.rupa = self._read_json('rupa.json')
        self.nibbana = self._read_json('nibbana.json')
        self.citta_cetasika = self._read_json('citta_cetasika.json')
        self.vedana = self._read_json('master_vedana.json')
        self.hetu = self._read_json('master_hetu.json') # Load Roots
        self.rules = self._read_json('rules_hierarchy.json') # Load Rules

    def _read_json(self, filename):
        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # print(f"Warning: File not found {filepath}")
            return []
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return []

    def get_citta(self): return self.citta
    def get_cetasika(self): return self.cetasika
    def get_rupa(self): return self.rupa
    def get_nibbana(self): return self.nibbana

    def get_graph_data(self):
        """
        Constructs graph (ORM Style - Rule Engine).
        """
        nodes = []
        links = []
        
        # 1. Categories Table (Structure Headers)
        cat_map = {c['id']: c for c in self.categories}
        
        for cat in self.categories:
            nodes.append({
                "id": cat["id"],
                "name": cat["name"],
                "type": cat["type"], 
                "group": "Structure",
                "val": 20 if cat["type"] == 'category' else 15
            })
            if cat["parent_id"]:
                 links.append({"source": cat["parent_id"], "target": cat["id"], "type": "structure"})

        # Master Data Lookups
        vedana_map = {v['id']: v for v in self.vedana}

        # --- RULE ENGINE LOGIC for CITTA ---
        
        # A. Build Hierarchy Nodes from Rules
        # Calculate Depth for each rule to help "Best Match"
        # We can infer depth by traversing parent_id up to ROOT or CAT_CITTA
        
        rule_map = {r['id']: r for r in self.rules}
        
        def get_rule_depth(rule):
            depth = 0
            pid = rule.get('parent_id')
            while pid:
                if pid in rule_map:
                    pid = rule_map[pid].get('parent_id')
                    depth += 1
                else:
                    break # Reached static category
            return depth

        # Add Rule Nodes to Graph
        existing_nodes = {n["id"]: n for n in nodes}
        
        for rule in self.rules:
            if rule['id'] not in existing_nodes:
                nodes.append({
                    "id": rule['id'],
                    "name": rule['name'],
                    "type": rule.get('type', 'sub_category'),
                    "group": rule.get('group', 'Structure'),
                    "val": 15
                })
                existing_nodes[rule['id']] = True
                
                if rule.get('parent_id'):
                    links.append({"source": rule['parent_id'], "target": rule['id'], "type": "structure"})

        # B. Process Citta Entities
        for cit in self.citta:
            name = cit.get("name", "")
            group = cit.get("group", "")
            plane = cit.get("plane", "")
            pali = cit.get("name_pali", "")
            
            # Find Best Match Rule (Deepest)
            best_rule = None
            max_depth = -1
            
            for rule in self.rules:
                criteria = rule.get('criteria', {})
                match = True
                
                # Check Group
                if 'group' in criteria and criteria['group'] != group:
                    match = False
                
                # Check Plane
                if match and 'plane' in criteria and criteria['plane'] != plane:
                    match = False

                # Check Name Contains (String)
                if match and 'name_contains' in criteria:
                    val = criteria['name_contains']
                    if isinstance(val, list):
                        for v in val:
                            if v not in name: 
                                match = False; break
                    else:
                        if val not in name: match = False

                # Check Name Contains Any (List)
                if match and 'name_contains_any' in criteria:
                     found_any = False
                     for v in criteria['name_contains_any']:
                         if v in name: 
                             found_any = True; break
                     if not found_any: match = False
                     
                # Check Name NOT Contains
                if match and 'name_not_contains' in criteria:
                    val = criteria['name_not_contains']
                    if isinstance(val, list):
                        for v in val:
                            if v in name:
                                match = False; break
                    else:
                        if val in name: match = False

                if match:
                    depth = get_rule_depth(rule)
                    if depth > max_depth:
                        max_depth = depth
                        best_rule = rule
            
            # Determine Parent
            parent_id = "CAT_CITTA" # Default fallback
            if best_rule:
                parent_id = best_rule['id']
                # Determine Group (Granular) from Rule
                cit_group = best_rule.get('group', group)
            else:
                cit_group = group # Fallback to generic group
                
                # Fallback Logic for static Category linkage if no rule matched
                # (e.g. if we forgot rules for certain groups)
                # But our Rules cover all groups now.

            # Enrich with Relations
            extra_info = {}
            if "vedana_id" in cit and cit["vedana_id"] in vedana_map:
                extra_info["vedana"] = vedana_map[cit["vedana_id"]]["name"]
                extra_info["vedana_color"] = vedana_map[cit["vedana_id"]].get("color", "")
            if "kicca_id" in cit:
                # We can lookup Kicca name here if we loaded master_kicca
                pass 

            nodes.append({
                "id": cit["id"],
                "name": cit.get("short_name", cit["name"]), 
                "full_name": cit["name"],
                "name_pali": cit.get("name_pali", ""),
                "type": "citta",
                "group": cit_group, # Assigned by Rule Engine
                "plane": cit.get("plane", "Unknown"), 
                "description": cit.get("description", ""),
                "val": 10,
                **extra_info
            })
            
            links.append({"source": parent_id, "target": cit["id"], "type": "structure"})

            # Association Links
            if "factors" in cit:
                for factor_id in cit["factors"]:
                    links.append({
                        "source": cit["id"],
                        "target": factor_id,
                        "type": "association"
                    })

        # C. Cetasika (Same old logic, or can move to rules too later)
        # keeping basic logic for now as requested focus was Citta Hierarchy Refactor
        cetasika_groups = {}
        for cet in self.cetasika:
            g_name = cet["group"]
            if g_name not in cetasika_groups:
                 cetasika_groups[g_name] = f"GRP_CET_{g_name}"
                 if cetasika_groups[g_name] not in existing_nodes:
                     nodes.append({
                         "id": cetasika_groups[g_name],
                         "name": g_name,
                         "type": "sub_category",
                         "group": "Cetasika",
                         "val": 15
                     })
                     links.append({"source": "CAT_SỞ_HỮU_TÂM_CETASIKA", "target": cetasika_groups[g_name], "type": "structure"})
            
            nodes.append({
                "id": cet["id"],
                "name": cet["name"],
                "name_pali": cet["name_pali"],
                "type": "cetasika",
                "group": "Cetasika",
                "val": 8
            })
            links.append({"source": cetasika_groups[g_name], "target": cet["id"], "type": "structure"})

        # D. Rupa
        rupa_groups = {}
        for rup in self.rupa:
            g_name = rup["group"]
            if g_name not in rupa_groups:
                 rupa_groups[g_name] = f"GRP_RUP_{g_name}"
                 if rupa_groups[g_name] not in existing_nodes:
                     nodes.append({
                         "id": rupa_groups[g_name],
                         "name": g_name,
                         "type": "sub_category",
                         "group": "Rupa",
                         "val": 15
                     })
                     links.append({"source": "CAT_SẮC_PHÁP_RUPA", "target": rupa_groups[g_name], "type": "structure"})

            nodes.append({
                "id": rup["id"],
                "name": rup["name"],
                "name_pali": rup["name_pali"],
                "type": "rupa",
                "group": "Rupa",
                "description": rup.get("description", ""),
                "val": 8
            })
            links.append({"source": rupa_groups[g_name], "target": rup["id"], "type": "structure"})

        # E. Nibbana
        for nib in self.nibbana:
            nodes.append({
                "id": nib["id"],
                "name": nib["name"],
                "name_pali": nib["name_pali"],
                "type": "nibbana",
                "group": "Nibbana",
                "description": nib.get("description", ""),
                "val": 15
            })
            links.append({"source": "CAT_NIẾT_BÀN_NIBBĀNA", "target": nib["id"], "type": "structure"})

        # F. Hetu (Roots)
        # Add 6 Root Nodes
        if self.hetu:
            for h in self.hetu:
                nodes.append({
                    "id": h["id"],
                    "name": h["name"],
                    "type": "hetu",
                    "group": "Root",
                    "color": h.get("color", "#ccc"),
                    "description": h.get("description", ""),
                    "val": 25 # Bigger node
                })
                # Add link to Root Category if it existed, for now floating or linked to 'CAT_NHÂN'?
                # Let's assume they are Special Nodes.

        # ... (Inside Citta Loop, extract root links) ...
        # Since we iterate citta above, let's inject logic there? 
        # No, let's iterate again merely for links to avoid touching the complex loop above excessively, 
        # OR just append links here since we have CITTA IDs.
        
        # Efficient way: Modify the loop "B. Process Citta Entities" to add root links.
        # But since I am using replace_file_content with range 281, I am at the end.
        # I will iterate citta again for simplicity of code injection here.
        
        for cit in self.citta:
            if "root_ids" in cit:
                for rid in cit["root_ids"]:
                    links.append({
                        "source": cit["id"],
                        "target": rid,
                        "type": "root_cause"
                    })

        return {"nodes": nodes, "links": links}

    def get_graph_data_by_type(self, relation_type):
        """
        Filter graph data by relation type: 'structure', 'association', or 'root_cause'
        Returns only nodes and links relevant to that relationship type.
        """
        all_data = self.get_graph_data()
        
        # Filter links by type
        filtered_links = [l for l in all_data['links'] if l['type'] == relation_type]
        
        # Get relevant node IDs
        connected_node_ids = set()
        for link in filtered_links:
            connected_node_ids.add(link['source'])
            connected_node_ids.add(link['target'])
        
        # For structure, include all structural nodes
        if relation_type == 'structure':
            for node in all_data['nodes']:
                if node.get('type') in ['root', 'category', 'sub_category'] or node.get('group') == 'Structure':
                    connected_node_ids.add(node['id'])
        
        filtered_nodes = [n for n in all_data['nodes'] if n['id'] in connected_node_ids]
        
        return {'nodes': filtered_nodes, 'links': filtered_links}
