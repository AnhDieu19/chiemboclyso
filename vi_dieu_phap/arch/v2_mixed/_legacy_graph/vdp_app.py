import sys
import os
from flask import Flask, render_template, jsonify

# Add project root to path to import data modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from python.vi_dieu_phap.data.citta_master import CITTA_MASTER
from python.vi_dieu_phap.data.cetasika_master import CETASIKA_MASTER

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('vdp_index.html')

@app.route('/api/data')
def get_graph_data():
    nodes = []
    links = []
    
    # 1. Add Cetasika Nodes (Mental Factors)
    for cet in CETASIKA_MASTER:
        nodes.append({
            "id": cet["id"],
            "name": cet["name"],
            "name_pali": cet["name_pali"],
            "type": "cetasika",
            "group": cet["group"],
            "val": 5 # Size
        })
        
    # 2. Add Citta Nodes (Consciousness)
    for cit in CITTA_MASTER:
        nodes.append({
            "id": cit["id"],
            "name": cit["name"],
            "short_name": cit.get("short_name", cit["name"]), # Fallback to full name if missing
            "name_pali": cit["name_pali"],
            "type": "citta",
            "group": cit["group"],
            "plane": cit["plane"],
            "val": 10 # Size
        })
        
        # 3. Create Links (Citta -> Cetasika)
        # Type: "tuong_ung" (Associated With)
        if "factors" in cit:
            for factor_id in cit["factors"]:
                links.append({
                    "source": cit["id"],
                    "target": factor_id,
                    "type": "tuong_ung"
                })
                
    return jsonify({
        "nodes": nodes,
        "links": links
    })

if __name__ == '__main__':
    app.run(debug=True, port=5001)
