/**
 * Cayley-Dickson Construction Visualization
 * ==========================================
 * Shows the chain R → C → H → O mapped to Dịch progression:
 * Thái Cực → Lưỡng Nghi → Tứ Tượng → Bát Quái
 */

const CayleyDickson = (() => {

    function init(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        let html = `<div class="cd-chain">`;

        CAYLEY_DICKSON.forEach((stage, idx) => {
            html += `
                <div class="cd-stage" style="--stage-color: ${stage.color}">
                    <div class="cd-header">
                        <span class="cd-algebra">${stage.algebra}</span>
                        <span class="cd-dim">dim = ${stage.dim}</span>
                    </div>
                    <div class="cd-body">
                        <div class="cd-names">
                            <span class="cd-math-name">${stage.name}</span>
                            <span class="cd-dich-name">${stage.dich}</span>
                        </div>
                        <p class="cd-desc">${stage.desc}</p>
                        <div class="cd-props">
                            ${stage.props.map(p => {
                                const isLost = p.startsWith("Mất");
                                return `<span class="cd-prop ${isLost ? 'lost' : 'kept'}">${p}</span>`;
                            }).join("")}
                        </div>
                    </div>
                </div>
                ${idx < CAYLEY_DICKSON.length - 1 ? `
                    <div class="cd-arrow">
                        <div class="cd-arrow-line"></div>
                        <div class="cd-arrow-label">×2</div>
                        <div class="cd-arrow-head">▶</div>
                    </div>
                ` : ""}
            `;
        });

        html += `</div>`;

        // Hurwitz theorem note
        html += `
            <div class="cd-hurwitz">
                <h4>Định lý Hurwitz (1898)</h4>
                <p>Chỉ có <strong>4 đại số chia chuẩn hóa</strong> trên số thực: <strong>R, C, H, O</strong> (chiều 1, 2, 4, 8).</p>
                <p>Mỗi bước nhân đôi chiều (Cayley-Dickson) mất đi một tính chất đại số. Sau O (chiều 8 = Bát Quái), bước tiếp theo (Sedenion, chiều 16) mất luôn tính <em>chia được</em> → không còn ý nghĩa vật lý.</p>
                <p class="hurwitz-insight">→ Bát Quái là <strong>giới hạn tự nhiên cuối cùng</strong> của cấu trúc đại số, giải thích tại sao hệ thống Dịch dừng lại ở 8 quẻ đơn.</p>
            </div>
        `;

        container.innerHTML = html;
    }

    return { init };
})();


/**
 * Properties Panel — Non-commutativity & Non-associativity examples
 */
const PropertiesPanel = (() => {

    function init(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        let html = "";

        // Non-commutativity
        html += `<div class="prop-section">
            <h4>Tính không giao hoán (Non-commutativity)</h4>
            <p class="prop-explain">eᵢ × eⱼ ≠ eⱼ × eᵢ  →  Thứ tự Thượng/Hạ quái có ý nghĩa. Đảo chiều = đổi Sinh ↔ Khắc.</p>
            <div class="examples-grid">`;

        NONCOMMUTATIVE_EXAMPLES.forEach(ex => {
            html += `
                <div class="example-card noncommut">
                    <div class="ex-forward"><span class="sinh-dot"></span> ${ex.forward}</div>
                    <div class="ex-reverse"><span class="khac-dot"></span> ${ex.reverse}</div>
                </div>
            `;
        });

        html += `</div></div>`;

        // Non-associativity
        html += `<div class="prop-section">
            <h4>Tính không kết hợp (Non-associativity) — Tam Tài</h4>
            <p class="prop-explain">(eᵢeⱼ)eₖ ≠ eᵢ(eⱼeₖ)  →  Nhóm 3 yếu tố (Tam Tài: Thiên–Địa–Nhân) tương tác khác nhau tùy cách kết hợp.</p>
            <div class="examples-grid">`;

        NONASSOCIATIVE_EXAMPLES.forEach(ex => {
            html += `
                <div class="example-card nonassoc">
                    <div class="ex-label">${ex.label}</div>
                    <div class="ex-left">${ex.left}</div>
                    <div class="ex-right">${ex.right}</div>
                    <div class="ex-result ${ex.result.includes('Mất') ? 'warn' : 'ok'}">${ex.result}</div>
                </div>
            `;
        });

        html += `</div></div>`;

        container.innerHTML = html;
    }

    return { init };
})();
