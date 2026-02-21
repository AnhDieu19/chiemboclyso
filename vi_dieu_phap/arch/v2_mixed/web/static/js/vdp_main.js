// Module: VDP.Main
// Responsibility: Entry Point, Data Loading

window.VDP = window.VDP || {};

VDP.Main = (function () {
    let allNodes = [];
    let allLinks = [];

    function init() {
        console.log("VDP Initializing...");

        // Initialize Modules
        VDP.Core.init();
        VDP.UI.init();

        // Load Data
        d3.json("/vdp/api/data").then(function (data) {
            allNodes = data.nodes;
            allLinks = data.links;

            // Mutable copies for D3
            const nodes = [...allNodes];
            const links = [...allLinks];

            // Update Counts
            document.getElementById("node-count").innerText = nodes.length;
            document.getElementById("link-count").innerText = links.length;

            // Generate UI
            VDP.UI.renderDynamicFilters(nodes);

            // Render Graph
            VDP.Core.render(nodes, links);

            // Initial Filter Apply (optional) or just let it run

            console.log("VDP Ready.");
        });
    }

    function getAllLinks() { return allLinks; }
    function getAllNodes() { return allNodes; }

    return {
        init: init,
        getAllLinks: getAllLinks,
        getAllNodes: getAllNodes
    };
})();

// Start App when DOM is ready
document.addEventListener("DOMContentLoaded", VDP.Main.init);

// Expose functions to Global scope for HTML onchange handlers (legacy support)
window.updateFilters = VDP.UI.updateFilters;
window.updateColors = VDP.UI.updateColors;
window.searchNode = VDP.UI.searchNode;
