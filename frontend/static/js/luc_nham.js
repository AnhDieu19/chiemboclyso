/**
 * ĐẠI LỤC NHÂM - Grand Six Ren Divination
 * Frontend rendering & API interaction
 */

const API_BASE = window.location.protocol === 'file:' ? 'http://localhost:5001' : '';

// ═══════════════════════════════════════════════════════════════
// BÀN THỨC LAYOUT: 12 Cung → 4×4 grid (bỏ 4 ô giữa)
// Row 0: Tỵ(5) Ngọ(6) Mùi(7) Thân(8)    (Nam)
// Row 1: Thìn(4) [center] [center] Dậu(9)
// Row 2: Mão(3)  [center] [center] Tuất(10)
// Row 3: Dần(2) Sửu(1) Tý(0)  Hợi(11)    (Bắc)
// ═══════════════════════════════════════════════════════════════
const GRID_LAYOUT = [
    [5, 6, 7, 8],
    [4, -1, -1, 9],
    [3, -1, -1, 10],
    [2, 1, 0, 11],
];

const CHI_NAMES = [
    "Tý (23h-1h)", "Sửu (1h-3h)", "Dần (3h-5h)", "Mão (5h-7h)",
    "Thìn (7h-9h)", "Tỵ (9h-11h)", "Ngọ (11h-13h)", "Mùi (13h-15h)",
    "Thân (15h-17h)", "Dậu (17h-19h)", "Tuất (19h-21h)", "Hợi (21h-23h)"
];

const NATURE_LABELS = {
    'đại_cát': '🌟 ĐẠI CÁT', 'dai_cat': '🌟 ĐẠI CÁT',
    'cát': '⭐ CÁT', 'cat': '⭐ CÁT',
    'trung': '⚖️ TRUNG',
    'hung': '⚠️ HUNG',
    'đại_hung': '🔥 ĐẠI HUNG', 'dai_hung': '🔥 ĐẠI HUNG',
};

const NATURE_COLORS = {
    'đại_cát': '#1abc9c', 'dai_cat': '#1abc9c',
    'cát': '#27ae60', 'cat': '#27ae60',
    'trung': '#f39c12',
    'hung': '#e74c3c',
    'đại_hung': '#c0392b', 'dai_hung': '#c0392b',
};

const REL_ICONS = {
    'sinh': '➜ sinh', 'bi_sinh': '⬅ bị sinh',
    'khac': '⚔ khắc', 'bi_khac': '💀 bị khắc', 'hoa': '☯ hòa',
};

// ═══════════════════════════════════════════════════════════════
// API CALL
// ═══════════════════════════════════════════════════════════════

async function calculateLucNham() {
    const formData = new FormData(document.getElementById('lucNhamForm'));
    const data = Object.fromEntries(formData);

    try {
        const response = await fetch(API_BASE + '/api/luc-nham/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        if (result.success) {
            renderAll(result.data);
        } else {
            alert('Lỗi: ' + result.error);
        }
    } catch (e) {
        alert('Lỗi kết nối: ' + e + '\n\nHãy đảm bảo server đang chạy.');
    }
}

// ═══════════════════════════════════════════════════════════════
// RENDER ORCHESTRATOR
// ═══════════════════════════════════════════════════════════════

function renderAll(data) {
    document.getElementById('resultArea').style.display = 'block';
    renderHeader(data);
    renderLucNhamCycle(data.luc_nham_info);
    renderKhoaThe(data.khoa_the);
    renderStrategy(data.chien_luoc);
    renderTuKhoa(data.tu_khoa);
    renderTamTruyen(data.tam_truyen);
    renderBanThuc(data.ban_thuc);
    renderDirections(data);
    renderQuantumVedic(data.quantum_vedic);
    renderQuantumAnalysis(data.quantum_analysis, data.quantum_vedic);
    if (data.knowledge_graph) renderKnowledgeGraph(data.knowledge_graph);
    renderDetailTable(data.ban_thuc);
}

// ═══════════════════════════════════════════════════════════════
// INDIVIDUAL RENDERERS
// ═══════════════════════════════════════════════════════════════

function renderHeader(data) {
    const cc = data.can_chi_info;
    document.getElementById('headerCanChi').textContent =
        `Ngày ${cc.full_ngay} (${cc.can_ngay_han}${cc.chi_ngay_han}) — Giờ ${cc.full_gio} (${cc.can_gio_han}${cc.chi_gio_han})`;
    document.getElementById('headerNguyetTuong').textContent =
        `Nguyệt Tướng: ${data.nguyet_tuong.ten} (${data.nguyet_tuong.dia_chi}) • Khóa Thể: ${data.khoa_the.ten} ${data.khoa_the.han}`;
}

function renderLucNhamCycle(items) {
    const container = document.getElementById('lucNhamCycle');
    container.innerHTML = '';
    items.forEach(item => {
        const div = document.createElement('div');
        div.className = 'nham-item';
        div.innerHTML = `
            <div class="nham-han">${item.han}</div>
            <div class="nham-name">${item.name}</div>
            <div class="nham-phase">${item.giai_doan}<br><small>${item.y_nghia}</small></div>
        `;
        container.appendChild(div);
    });
}

function renderKhoaThe(kt) {
    const color = NATURE_COLORS[kt.tinh_chat] || '#333';
    document.getElementById('khoaTheCard').innerHTML = `
        <h2 style="color: ${color}">${kt.ten}</h2>
        <h4 style="color: ${color}">${kt.han}</h4>
        <p class="mt-3">${kt.y_nghia}</p>
        <span class="badge" style="background: ${color}; font-size: 0.9rem;">${kt.tinh_chat.toUpperCase()}</span>
    `;
}

function renderStrategy(s) {
    document.getElementById('strategyCard').innerHTML = `
        <div class="strategy-icon">${s.icon}</div>
        <h3 class="mt-2">${s.chien_luoc}</h3>
        <p>${s.mo_ta}</p>
        <span class="badge bg-secondary" style="font-size: 0.9rem;">${s.muc_do}</span>
    `;
}

function renderTuKhoa(tuKhoa) {
    const grid = document.getElementById('tuKhoaGrid');
    grid.innerHTML = '';
    tuKhoa.forEach(k => {
        const cls = k.diem > 0 ? 'positive' : (k.diem < 0 ? 'negative' : 'neutral');
        const div = document.createElement('div');
        div.className = `khoa-card ${cls}`;
        div.innerHTML = `
            <div class="khoa-number">Khóa ${k.khoa}</div>
            <div class="khoa-chi">
                <span class="thuong">${k.thuong_ten}</span>
                <span class="arrow">${REL_ICONS[k.quan_he] || k.quan_he}</span>
                <span class="ha">${k.ha_ten}</span>
            </div>
            <div>
                <span class="hanh-badge hanh-${k.ngu_hanh_thuong}">${k.ngu_hanh_thuong}</span>
                ${k.diem > 0 ? '+' : ''}${k.diem}
                <span class="hanh-badge hanh-${k.ngu_hanh_ha}">${k.ngu_hanh_ha}</span>
            </div>
            <div class="khoa-role">
                <strong>${k.vai_tro}</strong><br>
                <small>${k.mo_ta}</small>
            </div>
        `;
        grid.appendChild(div);
    });
}

function renderTamTruyen(tt) {
    const flow = document.getElementById('tamTruyenFlow');
    flow.innerHTML = '';
    const stages = [
        { key: 'so_truyen', cls: 'so-truyen', label: '初傳 Sơ Truyền' },
        { key: 'trung_truyen', cls: 'trung-truyen', label: '中傳 Trung Truyền' },
        { key: 'mat_truyen', cls: 'mat-truyen', label: '末傳 Mạt Truyền' },
    ];

    stages.forEach((stage, idx) => {
        if (idx > 0) {
            const arrow = document.createElement('div');
            arrow.className = 'truyen-arrow';
            arrow.textContent = '➜';
            flow.appendChild(arrow);
        }

        const t = tt[stage.key];
        const card = document.createElement('div');
        card.className = `truyen-card ${stage.cls}`;
        card.innerHTML = `
            <div class="truyen-label">${stage.label}</div>
            <div class="truyen-chi">${t.ten} ${t.han}</div>
            <span class="hanh-badge hanh-${t.ngu_hanh}">${t.ngu_hanh}</span>
            ${t.than_tuong ? `<div class="mt-1"><small>🛡️ ${t.than_tuong}</small></div>` : ''}
            <div><strong>${t.vai_tro}</strong></div>
            <div style="font-size:0.82rem; color:#666">${t.mo_ta}</div>
            <div class="truyen-quantum">⚛️ ${t.quantum_analog}</div>
        `;
        flow.appendChild(card);
    });
}

function renderBanThuc(banThuc) {
    const grid = document.getElementById('banThucGrid');
    grid.innerHTML = '';

    for (let row = 0; row < 4; row++) {
        for (let col = 0; col < 4; col++) {
            const chiIdx = GRID_LAYOUT[row][col];

            if (chiIdx === -1) {
                const div = document.createElement('div');
                div.className = 'cung-cell center-cell';
                if (row === 1 && col === 1) {
                    div.innerHTML = `
                        <div class="text-center">
                            <h5 style="color: #b9770e; margin-bottom:4px;">天 圓 地 方</h5>
                            <small style="color: #666;">Thiên Viên Địa Phương</small>
                            <div class="mt-2" style="font-size:2rem;">壬</div>
                            <small style="color:#888;">Dương Thủy</small>
                        </div>
                    `;
                } else {
                    div.innerHTML = '<div class="text-center" style="color:#ccc; font-size: 0.8rem;">•</div>';
                }
                grid.appendChild(div);
                continue;
            }

            const cung = banThuc[String(chiIdx)];
            if (!cung) {
                grid.appendChild(document.createElement('div'));
                continue;
            }

            const div = document.createElement('div');
            div.className = 'cung-cell';

            const thanCls = cung.than_tuong_tinh_chat ?
                `than-${cung.than_tuong_tinh_chat}` : 'than-trung';

            let natureIcon = '⚖️';
            if (cung.nature.includes('cát') || cung.nature.includes('cat')) natureIcon = '⭐';
            if (cung.nature.includes('hung')) natureIcon = '⚠️';
            if (cung.nature.includes('đại_cát') || cung.nature.includes('dai_cat')) natureIcon = '🌟';
            if (cung.nature.includes('đại_hung') || cung.nature.includes('dai_hung')) natureIcon = '🔥';

            div.innerHTML = `
                <div class="huong-badge">${cung.huong}</div>
                <div class="thien-dia-row">
                    <span class="thien-chi-badge">${cung.thien_chi} ${cung.thien_han}</span>
                    <span class="dia-chi-badge">${cung.dia_chi} ${cung.dia_han}</span>
                </div>
                ${cung.than_tuong ? `
                    <div class="than-tuong-box ${thanCls}">
                        ${cung.than_tuong} ${cung.than_tuong_han}
                    </div>
                ` : ''}
                <div class="d-flex justify-content-between" style="font-size:0.75rem;">
                    <span class="hanh-badge hanh-${cung.hanh_thien}">${cung.hanh_thien}</span>
                    <span style="color:#95a5a6;">${cung.quan_he}</span>
                    <span class="hanh-badge hanh-${cung.hanh_dia}">${cung.hanh_dia}</span>
                </div>
                ${cung.nguyet_tuong_ten ? `<div style="font-size:0.68rem; color:#8e44ad; text-align:center;">✧ ${cung.nguyet_tuong_ten}</div>` : ''}
                <div class="cung-footer">
                    ${natureIcon} <strong class="nature-${cung.nature}">${cung.score}</strong>
                    ${cung.dong_vat.length ? `<br><span class="dong-vat-text">${cung.dong_vat.join(' ')}</span>` : ''}
                </div>
            `;
            grid.appendChild(div);
        }
    }
}

function renderDirections(data) {
    const b = data.best_direction;
    const w = data.worst_direction;
    document.getElementById('bestDir').textContent = `${b.huong} (${b.dia_chi}) — Điểm: ${b.score}`;
    document.getElementById('bestReason').textContent = b.reason;
    document.getElementById('worstDir').textContent = `${w.huong} (${w.dia_chi}) — Điểm: ${w.score}`;
    document.getElementById('worstReason').textContent = w.reason;
}

function renderQuantumVedic(qv) {
    if (!qv) return;
    document.getElementById('qvTotal').textContent = qv.tong_cau_hinh?.toLocaleString() || '1,440';
    document.getElementById('qvFormula').textContent = qv.cong_thuc || '12 × 12 × 12';
}

// ═══════════════════════════════════════════════════════════════
// QUANTUM ANALYSIS RENDERERS (Dynamic)
// ═══════════════════════════════════════════════════════════════

/* Đại Việt: Kim = Trắng (White), Thổ = Vàng (Yellow) */
const HANH_COLORS = {
    'Kim': '#9E9E9E', 'Mộc': '#27ae60', 'Thủy': '#2980b9',
    'Hỏa': '#e74c3c', 'Thổ': '#FFB300',
};

function renderQuantumAnalysis(qa, qv) {
    if (!qa) return;
    renderSuperposition(qa.superposition, qa.ngu_hanh_distribution);
    renderEntanglement(qa.entanglement);
    renderDecoherenceTimeline(qa.decoherence_timeline);
    renderParticleTable(qa.than_tuong_fields);
    renderConceptMapping(qv?.concept_mapping);
    renderSymmetryAnalysis(qa.symmetry);
}

function renderSuperposition(sp, dist) {
    if (!sp) return;

    // Coherence meter
    const bar = document.getElementById('coherenceBar');
    const val = document.getElementById('coherenceValue');
    setTimeout(() => { bar.style.width = sp.coherence_pct + '%'; }, 100);
    val.textContent = sp.coherence_pct + '%';

    document.getElementById('entropyValue').textContent = sp.entropy;
    document.getElementById('maxEntropyValue').textContent = sp.max_entropy;
    document.getElementById('coherenceInterpretation').textContent = sp.interpretation;

    // Ngũ Hành distribution
    const container = document.getElementById('nguHanhQuantumDist');
    container.innerHTML = '<div style="font-weight:600; margin-bottom:8px;">Phân Bố Ngũ Hành ↔ Lực Cơ Bản</div>';

    if (!dist) return;
    const maxCount = Math.max(...Object.values(dist).map(d => d.count));

    for (const [hanh, info] of Object.entries(dist)) {
        const pct = (info.count / maxCount) * 100;
        const color = HANH_COLORS[hanh] || '#999';
        const row = document.createElement('div');
        row.className = 'hanh-quantum-row';
        row.innerHTML = `
            <span class="hanh-name" style="color:${color}">
                <span class="hanh-badge hanh-${hanh}">${hanh}</span>
            </span>
            <div class="hanh-bar-bg">
                <div class="hanh-bar-fill" style="width:${pct}%; background:${color};"></div>
            </div>
            <span style="width:30px; text-align:center; font-weight:700;">${info.count}</span>
            <span class="hanh-force">${info.force || ''} ${info.boson ? '(' + info.boson + ')' : ''}</span>
        `;
        container.appendChild(row);
    }
}

function renderEntanglement(ent) {
    if (!ent) return;

    const grid = document.getElementById('entanglementGrid');
    grid.innerHTML = '';

    ent.pairs.forEach(p => {
        const isPos = p.correlation >= 0;
        const absCor = Math.abs(p.correlation);
        const pct = absCor * 100;

        const div = document.createElement('div');
        div.className = 'entanglement-pair';
        div.innerHTML = `
            <div class="pair-label">${p.pair}</div>
            <div class="hanh-pair">
                <span class="hanh-badge hanh-${p.hanh_a}">${p.hanh_a}</span>
                <span style="color:#636e72; font-size:0.8rem;"> ${p.relation} </span>
                <span class="hanh-badge hanh-${p.hanh_b}">${p.hanh_b}</span>
            </div>
            <div class="correlation-bar">
                <div class="correlation-fill ${isPos ? 'positive' : 'negative'}" style="width:${pct}%"></div>
            </div>
            <div style="font-size:0.85rem; font-weight:600; color:${isPos ? '#00b894' : '#d63031'};">
                ${isPos ? '+' : ''}${p.correlation.toFixed(2)}
            </div>
            <div class="bell-state">${p.bell_state}</div>
        `;
        grid.appendChild(div);
    });

    document.getElementById('avgEntanglement').textContent =
        `Trung bình Entanglement: ${ent.avg_entanglement.toFixed(3)} | Cặp mạnh nhất: ${ent.max_entangled_pair}`;
    document.getElementById('entanglementInterpretation').textContent = ent.interpretation;
}

function renderDecoherenceTimeline(timeline) {
    if (!timeline) return;

    const container = document.getElementById('decoherenceTimeline');
    container.innerHTML = '';

    timeline.forEach((stage, idx) => {
        if (idx > 0) {
            const arrow = document.createElement('div');
            arrow.className = 'decoherence-arrow';
            arrow.textContent = '⟶';
            container.appendChild(arrow);
        }

        const div = document.createElement('div');
        div.className = `decoherence-stage stage-${idx}`;
        div.innerHTML = `
            <div class="stage-header">${stage.quantum_phase}</div>
            <div class="stage-chi">${stage.chi} ${stage.han}</div>
            <div class="stage-quantum">${stage.stage}</div>
            <div>
                <span class="hanh-badge hanh-${stage.ngu_hanh}">${stage.ngu_hanh}</span>
                ${stage.than_tuong ? `<span style="font-size:0.8rem; opacity:0.9;"> 🛡️ ${stage.than_tuong}</span>` : ''}
            </div>
            <div class="stage-vedic">🙏 ${stage.vedic_deity}</div>
            ${stage.particle ? `<div class="stage-particle">⚛️ ${stage.particle}</div>` : ''}
            <div style="font-size:0.78rem; margin-top:6px; opacity:0.85;">${stage.interpretation}</div>
        `;
        container.appendChild(div);
    });
}

function renderParticleTable(fields) {
    if (!fields) return;

    const tbody = document.getElementById('particleTableBody');
    tbody.innerHTML = '';

    fields.forEach(f => {
        const natureColor = NATURE_COLORS[f.tinh_chat] || '#636e72';
        const tr = document.createElement('tr');
        tr.innerHTML = `
            <td>
                <strong>${f.ten}</strong> ${f.han}<br>
                <small style="color:${natureColor};">${(NATURE_LABELS[f.tinh_chat] || f.tinh_chat)}</small>
            </td>
            <td>${f.cung} → ${f.thien}</td>
            <td><span class="hanh-badge hanh-${f.ngu_hanh}">${f.ngu_hanh}</span></td>
            <td><span class="particle-badge">${f.particle}</span></td>
            <td class="vedic-name">${f.vedic}</td>
            <td class="role-text">${f.role}</td>
        `;
        tbody.appendChild(tr);
    });
}

function renderConceptMapping(concepts) {
    if (!concepts) return;

    const container = document.getElementById('conceptMappingGrid');
    container.innerHTML = '';

    concepts.forEach((c, idx) => {
        const row = document.createElement('div');
        row.className = 'concept-row';
        row.innerHTML = `
            <div class="concept-ln">
                ${c.luc_nham}
            </div>
            <div class="concept-qt">${c.quantum}</div>
            <div class="concept-vd">${c.vedic}</div>
            <div>
                <span class="concept-formula">${c.formula}</span>
                <span class="expand-btn" onclick="this.closest('.concept-row').classList.toggle('expanded')"> chi tiết ▾</span>
            </div>
            <div class="concept-detail">${c.detail}</div>
        `;
        container.appendChild(row);
    });
}

function renderSymmetryAnalysis(sym) {
    if (!sym) return;

    document.getElementById('breakFormula').textContent =
        `Z₁₂ → Z₁₂ / rotation(${sym.offset})`;
    document.getElementById('symmetryBreakText').textContent =
        `${sym.type} — góc xoay φ = ${sym.angle}°`;

    const analysis = document.getElementById('symmetryAnalysis');
    const broken = sym.broken;
    analysis.innerHTML = `
        <div class="symmetry-item" style="border-left-color: ${broken ? '#e17055' : '#00b894'};">
            <h6>${broken ? '⚡ Đối Xứng Bị Phá Vỡ' : '🔮 Đối Xứng Được Bảo Toàn'}</h6>
            <p>${broken
                ? `Thiên bàn xoay ${sym.angle}° so với Địa bàn → phá vỡ đối xứng gốc Z₁₂, tạo ra sự phân cực năng lượng giữa các cung. Trong vật lý, đây tương đương cơ chế Higgs: phá vỡ đối xứng tạo ra khối lượng (hiện thực hóa).`
                : sym.offset === 0
                    ? 'Thiên ≡ Địa → đối xứng hoàn hảo nhưng bế tắc (Phục Ngâm). Trong vật lý, trạng thái đối xứng hoàn hảo = chân không, không có sự kiện.'
                    : 'Thiên xung Địa → đối xứng nghịch đảo (Phản Ngâm). Tương đương phản vật chất: mọi thứ bị đảo ngược.'
            }</p>
        </div>
        <div class="symmetry-item mt-2">
            <h6>🌀 Vòng Tròn Nhân Quả</h6>
            <p>
                Nhóm Z₁₂ tuần hoàn: 12 bước xoay → trở về gốc.<br>
                <strong>6! = 720</strong> hoán vị 6 giai đoạn Lục Nhâm = 720 cặp hạt Vệ Đà.<br>
                <strong>1.440 = 2 × 720</strong> = Âm × Dương × 6! = toàn bộ cấu hình bàn thức.
            </p>
        </div>
    `;
}

function renderDetailTable(banThuc) {
    const tbody = document.getElementById('detailTableBody');
    tbody.innerHTML = '';

    const sorted = Object.values(banThuc).sort((a, b) => b.score - a.score);

    sorted.forEach(c => {
        const tr = document.createElement('tr');
        const scoreClass = c.score >= 3 ? 'text-success fw-bold' :
                           c.score >= 1 ? 'text-success' :
                           c.score <= -3 ? 'text-danger fw-bold' :
                           c.score <= -1 ? 'text-danger' : 'text-muted';

        tr.innerHTML = `
            <td><strong>${c.dia_chi} ${c.dia_han}</strong></td>
            <td>${c.huong}</td>
            <td>
                <span class="thien-chi-badge">${c.thien_chi} ${c.thien_han}</span> /
                <span class="dia-chi-badge">${c.dia_chi}</span>
            </td>
            <td>${c.than_tuong ? `${c.than_tuong} ${c.than_tuong_han}` : '—'}</td>
            <td>
                <span class="hanh-badge hanh-${c.hanh_thien}">${c.hanh_thien}</span>
                ${c.quan_he}
                <span class="hanh-badge hanh-${c.hanh_dia}">${c.hanh_dia}</span>
            </td>
            <td class="${scoreClass} text-center">${c.score}</td>
            <td class="nature-${c.nature}">${NATURE_LABELS[c.nature] || c.nature}</td>
        `;
        tbody.appendChild(tr);
    });
}

// ═══════════════════════════════════════════════════════════════
// KNOWLEDGE GRAPH RENDERER
// ═══════════════════════════════════════════════════════════════

function renderKnowledgeGraph(kg) {
    // 1. Summary Stats
    const summary = kg.graph_summary || {};
    const el = (id, val) => { const e = document.getElementById(id); if (e) e.textContent = val; };
    el('kgNodeCount', summary.total_nodes || 0);
    el('kgEdgeCount', summary.total_edges || 0);
    el('kgEntityTypes', Object.keys(summary.entity_types || {}).length);

    // 2. Operational Strategy (CASE WHEN)
    renderKgStrategy(kg.operational_strategy);

    // 3. Vedic Force Routing
    renderKgVedicRouting(kg.vedic_force_routing);

    // 4. Interaction Events (RDF Reification)
    renderKgInteractions(kg.interaction_events);

    // 5. SiKe Anchors
    renderKgSikeAnchors(kg.sike_anchors);
}

function renderKgStrategy(strategy) {
    const container = document.getElementById('kgStrategyContent');
    if (!container || !strategy) return;

    const strengthClass = (s) => (s || '').toLowerCase();
    const mucDoClass = (m) => {
        if (!m) return '';
        if (m.includes('Đại Cát')) return 'cat';
        if (m.includes('Cát')) return 'cat';
        if (m.includes('Hung')) return 'hung';
        return 'trung';
    };

    container.innerHTML = `
        <div class="kg-strategy-main">
            <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
                <span style="font-size:1.5rem;">${strategy.icon || '⚡'}</span>
                <span class="strategy-name">${strategy.strategy_vi || strategy.strategy}</span>
                <span class="kg-badge">${strategy.muc_do || ''}</span>
            </div>
            <div class="strategy-desc">${strategy.description || ''}</div>
            ${strategy.drift_note ? `<div style="margin-top:8px;font-size:0.85rem;color:#fdcb6e;">📌 ${strategy.drift_note}</div>` : ''}
            ${strategy.persist_note ? `<div style="margin-top:4px;font-size:0.85rem;color:#81ecec;">📌 ${strategy.persist_note}</div>` : ''}
        </div>
        <div class="kg-strategy-strength">
            <div class="kg-strength-item">
                <div class="label">K1 Origin</div>
                <div class="value ${strengthClass(strategy.origin_strength)}">${strategy.origin_strength || '—'}</div>
            </div>
            <div class="kg-strength-item">
                <div class="label">K2 Persist</div>
                <div class="value ${strengthClass(strategy.persist_strength)}">${strategy.persist_strength || '—'}</div>
            </div>
            <div class="kg-strength-item">
                <div class="label">K3 Trigger</div>
                <div class="value ${strengthClass(strategy.trigger_strength)}">${strategy.trigger_strength || '—'}</div>
            </div>
            <div class="kg-strength-item">
                <div class="label">K4 Drift</div>
                <div class="value ${strengthClass(strategy.drift_strength)}">${strategy.drift_strength || '—'}</div>
            </div>
        </div>
    `;
}

function renderKgVedicRouting(routing) {
    const phasesContainer = document.getElementById('kgVedicPhases');
    const verdictEl = document.getElementById('kgVerdict');
    if (!phasesContainer || !routing) return;

    const phases = routing.phases || [];
    let html = '';
    phases.forEach((p, i) => {
        const forceClass = p.force_type.includes('Samprasadagati') ? 'samprasadagati'
                         : p.force_type.includes('Saparayanagati') ? 'saparayanagati'
                         : 'nityagati';
        const weightClass = p.net >= 0 ? 'positive' : 'negative';

        html += `<div class="col-md-4">
            <div class="kg-phase-card ${forceClass}">
                <div class="phase-name">${p.vedic_deity} — ${p.phase}</div>
                <div class="phase-force">${p.force_type}</div>
                <div style="display:flex;justify-content:space-between;margin-top:8px;">
                    <div>
                        <small style="color:#b2bec3;">Base:</small>
                        <span class="phase-weight ${p.weight >= 0 ? 'positive' : 'negative'}">${p.weight > 0 ? '+' : ''}${p.weight}</span>
                    </div>
                    <div>
                        <small style="color:#b2bec3;">Rudra:</small>
                        <span class="phase-weight ${p.rudra >= 0 ? 'positive' : 'negative'}">${p.rudra > 0 ? '+' : ''}${p.rudra}</span>
                    </div>
                    <div>
                        <small style="color:#b2bec3;">Net:</small>
                        <span class="phase-weight ${weightClass}">${p.net > 0 ? '+' : ''}${p.net}</span>
                    </div>
                </div>
            </div>
        </div>`;
    });
    phasesContainer.innerHTML = html;

    // Verdict
    if (verdictEl) {
        const cf = routing.cumulative_force || 0;
        const verdictClass = cf >= 0.5 ? 'cat' : (cf <= -0.5 ? 'hung' : 'trung');
        verdictEl.className = `kg-verdict ${verdictClass}`;
        verdictEl.innerHTML = `
            <div>Tổng Lực Tích Lũy: <strong>${cf > 0 ? '+' : ''}${cf}</strong></div>
            <div style="margin-top:4px;">${routing.verdict_vi || ''}</div>
            <small style="opacity:0.8;">${routing.interpretation || ''}</small>
        `;
    }
}

function renderKgInteractions(events) {
    const tbody = document.getElementById('kgInteractionTable');
    if (!tbody || !events) return;
    tbody.innerHTML = '';

    events.forEach(ev => {
        const tr = document.createElement('tr');
        const stateMap = {
            'Đại Cát': 'dai-cat',
            'Cát': 'cat',
            'Trung Tính': 'trung',
            'Hung': 'hung',
            'Đại Hung': 'dai-hung',
        };
        const catFactors = (ev.cat_factors || []).map(f => `<div class="cat-text">✦ ${f}</div>`).join('');
        const hungFactors = (ev.hung_factors || []).map(f => `<div class="hung-text">✧ ${f}</div>`).join('');
        const badgeClass = stateMap[ev.state_label] || 'trung';
        const netP = ev.net_probability != null ? ev.net_probability.toFixed(2) : '—';
        const cungName = ev.event_id ? ev.event_id.replace('cung_', '').replace(/_/g, ' ') : '';

        tr.innerHTML = `
            <td>${cungName}</td>
            <td style="font-size:0.75rem;">${ev.source_node ? ev.source_node.split('_').pop() : ''} ↔ ${ev.target_node ? ev.target_node.split('_').pop() : ''}</td>
            <td>${ev.than_tuong || ''}</td>
            <td style="font-size:0.72rem;">${catFactors || '<span style="color:#636e72;">—</span>'}</td>
            <td style="font-size:0.72rem;">${hungFactors || '<span style="color:#636e72;">—</span>'}</td>
            <td style="font-family:monospace;text-align:center;">${netP}</td>
            <td><span class="state-badge ${badgeClass}">${ev.state_label || ''}</span></td>
        `;
        tbody.appendChild(tr);
    });
}

function renderKgSikeAnchors(anchors) {
    const container = document.getElementById('kgSikeAnchors');
    if (!container || !anchors) return;

    let html = '';
    anchors.forEach(a => {
        const strengthClass = (a.strength || '').toLowerCase();
        html += `<div class="col-md-3">
            <div class="kg-sike-card">
                <div class="sike-role">${a.role || ''}</div>
                <div class="sike-name">K${a.khoa_num}: ${a.thuong_than} / ${a.ha_than}</div>
                <div class="sike-detail">
                    ${a.wu_xing_thuong} ${a.relation} ${a.wu_xing_ha}
                    <span style="float:right;" class="${strengthClass}">${a.strength}</span>
                </div>
                <div style="margin-top:4px;font-size:0.75rem;color:#a29bfe;">${a.role_vi || ''}</div>
            </div>
        </div>`;
    });
    container.innerHTML = html;
}

// ═══════════════════════════════════════════════════════════════
// UTILITIES
// ═══════════════════════════════════════════════════════════════

function setCurrentTime() {
    const now = new Date();
    document.querySelector('input[name="year"]').value = now.getFullYear();
    document.querySelector('input[name="month"]').value = now.getMonth() + 1;
    document.querySelector('input[name="day"]').value = now.getDate();
    document.querySelector('input[name="hour"]').value = now.getHours();
    updateCanChiLabel();
}

function updateCanChiLabel() {
    const h = parseInt(document.querySelector('input[name="hour"]').value);
    if (isNaN(h)) return;
    const chiIndex = Math.floor((h + 1) / 2) % 12;
    document.getElementById('canChiLabel').textContent = `Giờ ${CHI_NAMES[chiIndex]} — ${h}h`;
}

// ═══════════════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
    setCurrentTime();
    document.querySelectorAll('#lucNhamForm input').forEach(input => {
        input.addEventListener('change', updateCanChiLabel);
    });
});
