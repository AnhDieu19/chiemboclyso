/**
 * Cyclic Group Zoo — Visual Atlas of All Groups
 * ===============================================
 * Interactive circular diagrams for ℤ₉, ℤ₈, ℤ₁₂, ℤ₁₆, ℤ₆₀
 * Each group shown as a circular ring with labeled nodes.
 */

const CyclicViz = (() => {

    function init(containerId) {
        const container = d3.select(containerId);
        const groups = [
            makeZ9Data(),
            makeZ8Data(),
            makeZ12Data(),
            makeZ16Data(),
            makeZ60Data()
        ];

        groups.forEach(gdata => {
            const card = container.append("div").attr("class", "cyclic-card");
            card.append("h4").html(`${gdata.title} <span class="cyclic-order">|G| = ${gdata.order}</span>`);
            card.append("p").attr("class", "cyclic-desc").text(gdata.desc);

            const svgContainer = card.append("div").attr("class", "cyclic-svg-wrap");
            drawRing(svgContainer.node(), gdata);

            if (gdata.formula) {
                card.append("div").attr("class", "cyclic-formula").html(gdata.formula);
            }
            if (gdata.usedBy) {
                card.append("div").attr("class", "cyclic-usage").html(`<strong>Dùng trong:</strong> ${gdata.usedBy}`);
            }
        });
    }

    function drawRing(containerEl, data) {
        const size = data.size || 200;
        const r = size * 0.38;
        const cx = size / 2, cy = size / 2;

        const svg = d3.select(containerEl).append("svg")
            .attr("viewBox", `0 0 ${size} ${size}`)
            .attr("preserveAspectRatio", "xMidYMid meet")
            .style("width", "100%")
            .style("max-width", `${size}px`);

        const g = svg.append("g");

        // Draw connecting arcs
        const n = data.nodes.length;
        for (let i = 0; i < n; i++) {
            const a1 = (i / n) * 2 * Math.PI - Math.PI / 2;
            const a2 = ((i + 1) / n) * 2 * Math.PI - Math.PI / 2;
            const x1 = cx + r * Math.cos(a1), y1 = cy + r * Math.sin(a1);
            const x2 = cx + r * Math.cos(a2), y2 = cy + r * Math.sin(a2);
            g.append("line")
                .attr("x1", x1).attr("y1", y1).attr("x2", x2).attr("y2", y2)
                .attr("stroke", data.ringColor || "rgba(255,255,255,0.15)")
                .attr("stroke-width", 1);
        }

        // Draw nodes
        data.nodes.forEach((node, i) => {
            const angle = (i / n) * 2 * Math.PI - Math.PI / 2;
            const x = cx + r * Math.cos(angle);
            const y = cy + r * Math.sin(angle);
            const nodeR = data.nodeRadius || 14;

            const nodeColor = node.color || data.defaultColor || "#555";

            g.append("circle")
                .attr("cx", x).attr("cy", y).attr("r", nodeR)
                .attr("fill", nodeColor)
                .attr("fill-opacity", node.weight === 2 ? 0.7 : 0.35)
                .attr("stroke", nodeColor)
                .attr("stroke-width", node.weight === 2 ? 2 : 1);

            g.append("text")
                .attr("x", x).attr("y", y)
                .attr("dy", "0.35em")
                .attr("text-anchor", "middle")
                .attr("font-size", data.fontSize || "9px")
                .attr("font-weight", "600")
                .attr("fill", "#fff")
                .text(node.label);
        });

        // Center label
        if (data.centerLabel) {
            g.append("text")
                .attr("x", cx).attr("y", cy)
                .attr("dy", "0.35em")
                .attr("text-anchor", "middle")
                .attr("font-size", "12px")
                .attr("font-weight", "700")
                .attr("fill", "var(--accent-gold)")
                .text(data.centerLabel);
        }

        // Direction arrow
        if (data.showArrow) {
            const arrowAngle = Math.PI / 2 + 0.3;
            const ar = r + 20;
            g.append("text")
                .attr("x", cx + ar * 0.7)
                .attr("y", cy - ar * 0.2)
                .attr("font-size", "14px")
                .attr("fill", "var(--text-muted)")
                .text("⟳");
        }
    }

    /* ── Data builders ── */

    function makeZ9Data() {
        const palaces = CYCLIC_GROUPS.Z9;
        return {
            title: "ℤ₉ — Phi Cung",
            order: 9,
            desc: palaces.desc,
            size: 220,
            centerLabel: "ℤ₉",
            defaultColor: "#42A5F5",
            showArrow: true,
            nodes: palaces.labels.map((v, i) => ({
                label: `${v} ${palaces.palaceNames[i]}`,
                color: LAC_THU.palaces[v] ? NGU_HANH.colors[LAC_THU.palaces[v].element].bg : "#555"
            })),
            formula: "<code>φ(s, n) = ((s−1 + n) mod 9) + 1</code>",
            usedBy: "Kỳ Môn (Phi Tinh, Bát Môn, Bát Thần), Huyền Không Phi Tinh"
        };
    }

    function makeZ8Data() {
        const ring = CYCLIC_GROUPS.Z8;
        return {
            title: "ℤ₈ — Bát Quái Ring",
            order: 8,
            desc: ring.desc,
            size: 220,
            centerLabel: "ℤ₈",
            defaultColor: "#66BB6A",
            showArrow: true,
            nodes: ring.ring.map((v, i) => ({
                label: `${v} ${ring.labels[i]}`,
                color: LAC_THU.palaces[v] ? NGU_HANH.colors[LAC_THU.palaces[v].element].bg : "#555"
            })),
            formula: "<code>RING = [1,8,3,4,9,2,7,6]</code><br>Hậu Thiên BQ, bỏ Trung Cung (5)",
            usedBy: "Thái Ất (Thái Ất tinh di chuyển, Đại Du)"
        };
    }

    function makeZ12Data() {
        const chi = CYCLIC_GROUPS.Z12;
        return {
            title: "ℤ₁₂ — Địa Chi",
            order: 12,
            desc: chi.desc,
            size: 240,
            centerLabel: "ℤ₁₂",
            defaultColor: "#FF7043",
            nodeRadius: 12,
            fontSize: "8px",
            showArrow: true,
            nodes: chi.labels.map((l, i) => ({
                label: l,
                color: NGU_HANH.colors[chi.elements[i]].bg
            })),
            formula: "<code>(JD + 49) mod 12</code> = Địa Chi ngày",
            usedBy: "Cả hai hệ thống (Tam Cơ, Kể Thần, Can Chi ngày)"
        };
    }

    function makeZ16Data() {
        const r16 = CYCLIC_GROUPS.Z16;
        return {
            title: "ℤ₁₆ (trọng số) — 16 Thần",
            order: 16,
            desc: r16.desc,
            size: 280,
            centerLabel: "18",
            defaultColor: "#AB47BC",
            nodeRadius: 12,
            fontSize: "7.5px",
            showArrow: true,
            nodes: r16.ring.map((l, i) => ({
                label: l,
                color: r16.dwellNodes.includes(l) ? "#F9A825" : "#AB47BC",
                weight: r16.weights[i]
            })),
            formula: `<code>Kỷ Dư mod 18</code><br>Càn & Khôn: lưu 2 toán → |hiệu dụng| = 18`,
            usedBy: "Thái Ất (Văn Xương / Thiên Mục)"
        };
    }

    function makeZ60Data() {
        const cc = CYCLIC_GROUPS.Z60;
        // Show first 12 + last 2 to indicate loop
        const showN = 60;
        return {
            title: "ℤ₆₀ ≅ ℤ₁₀ × ℤ₁₂ — Lục Thập Hoa Giáp",
            order: 60,
            desc: cc.desc,
            size: 320,
            centerLabel: "60",
            defaultColor: "#78909C",
            nodeRadius: 8,
            fontSize: "0px", // too many nodes, hide text
            ringColor: "rgba(120,144,156,0.3)",
            showArrow: true,
            nodes: Array.from({ length: showN }, (_, i) => {
                const { can, chi } = cc.fromIndex(i);
                // Color by Thiên Can element
                const canElements = ["Mộc", "Mộc", "Hỏa", "Hỏa", "Thổ", "Thổ", "Kim", "Kim", "Thủy", "Thủy"];
                return {
                    label: "", // hidden
                    color: NGU_HANH.colors[canElements[i % 10]].bg
                };
            }),
            formula: `<code>(JD + 49) mod 60</code><br>LCM(10,12) = 60. ℤ₆₀ ≅ ℤ₁₀ × ℤ₆ (nhưng ℤ₁₀ × ℤ₁₂ đồng bộ chẵn-chẵn, lẻ-lẻ)`,
            usedBy: "Can Chi ngày/năm → cả hai hệ thống"
        };
    }

    return { init };
})();
