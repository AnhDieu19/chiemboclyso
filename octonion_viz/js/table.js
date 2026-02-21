/**
 * Interactive Multiplication Table
 * =================================
 * 8×8 Octonion multiplication table with Bát Quái trigram symbols.
 * Hover to highlight row/column and show product info.
 */

const MultTable = (() => {

    function init(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;

        const table = document.createElement("table");
        table.className = "mult-table";

        // Header row
        const thead = document.createElement("thead");
        const headerRow = document.createElement("tr");
        headerRow.appendChild(createTH("×")); // corner cell
        for (let j = 0; j < 8; j++) {
            headerRow.appendChild(createTH(TRIGRAMS[j].symbol + " " + TRIGRAMS[j].name, j));
        }
        thead.appendChild(headerRow);
        table.appendChild(thead);

        // Body rows
        const tbody = document.createElement("tbody");
        for (let i = 0; i < 8; i++) {
            const row = document.createElement("tr");

            // Row header
            const th = document.createElement("th");
            th.innerHTML = `<span class="tri-sym">${TRIGRAMS[i].symbol}</span> ${TRIGRAMS[i].name}`;
            th.style.color = TRIGRAMS[i].color;
            row.appendChild(th);

            for (let j = 0; j < 8; j++) {
                const td = document.createElement("td");
                const r = MULT_TABLE[i][j];

                const signStr = r.sign < 0 ? "−" : "";
                const target = TRIGRAMS[r.index];

                td.innerHTML = `<span class="cell-sign ${r.sign < 0 ? 'neg' : 'pos'}">${signStr}</span><span class="cell-sym">${target.symbol}</span>`;
                td.className = getCellClass(i, j, r);
                td.dataset.row = i;
                td.dataset.col = j;
                td.dataset.result = `${TRIGRAMS[i].symbol} × ${TRIGRAMS[j].symbol} = ${signStr}${target.symbol} ${target.name}`;
                td.dataset.sign = r.sign;

                td.addEventListener("mouseenter", () => onCellHover(i, j, true));
                td.addEventListener("mouseleave", () => onCellHover(i, j, false));

                row.appendChild(td);
            }

            tbody.appendChild(row);
        }
        table.appendChild(tbody);
        container.appendChild(table);

        // Info bar
        const info = document.createElement("div");
        info.id = "mult-info";
        info.className = "mult-info";
        info.innerHTML = `<p class="hint">Hover một ô để xem chi tiết phép nhân</p>`;
        container.appendChild(info);
    }

    function createTH(text, colIdx) {
        const th = document.createElement("th");
        if (colIdx !== undefined) {
            th.innerHTML = `<span class="tri-sym">${TRIGRAMS[colIdx].symbol}</span><br><span class="th-name">${TRIGRAMS[colIdx].name}</span>`;
            th.style.color = TRIGRAMS[colIdx].color;
        } else {
            th.textContent = text;
            th.className = "corner-cell";
        }
        return th;
    }

    function getCellClass(i, j, r) {
        const classes = ["mult-cell"];

        if (i === 0 || j === 0) {
            classes.push("identity");
        } else if (i === j) {
            classes.push("self-product"); // eᵢ² = -e₀
        } else if (r.sign > 0) {
            classes.push("positive");
        } else {
            classes.push("negative");
        }

        return classes.join(" ");
    }

    function onCellHover(i, j, active) {
        const table = document.querySelector(".mult-table");
        const rows = table.querySelectorAll("tbody tr");
        const headers = table.querySelectorAll("thead th");

        if (active) {
            // Highlight row and column
            rows.forEach((row, ri) => {
                row.classList.toggle("row-highlight", ri === i);
                const cells = row.querySelectorAll("td");
                cells.forEach((cell, ci) => {
                    cell.classList.toggle("col-highlight", ci === j);
                    cell.classList.toggle("active-cell", ri === i && ci === j);
                });
            });

            headers.forEach((th, hi) => {
                th.classList.toggle("col-highlight", hi === j + 1);
            });

            // Update info
            const r = MULT_TABLE[i][j];
            const target = TRIGRAMS[r.index];
            const signStr = r.sign < 0 ? "−" : "+";
            const signClass = r.sign < 0 ? "khac" : "sinh";

            let xorExplain = "";
            if (i > 0 && j > 0 && i !== j) {
                const xorResult = i ^ j;
                xorExplain = `<span class="xor-badge">${TRIGRAMS[i].binary} ⊕ ${TRIGRAMS[j].binary} = ${TRIGRAMS[xorResult].binary}</span>`;
            }

            const info = document.getElementById("mult-info");
            if (info) {
                info.innerHTML = `
                    <div class="mult-detail">
                        <span class="operand" style="color:${TRIGRAMS[i].color}">${TRIGRAMS[i].symbol} ${TRIGRAMS[i].name} (e${i === 0 ? '₀' : '₁₂₃₄₅₆₇'[i-1]})</span>
                        <span class="operator">×</span>
                        <span class="operand" style="color:${TRIGRAMS[j].color}">${TRIGRAMS[j].symbol} ${TRIGRAMS[j].name} (e${'₀₁₂₃₄₅₆₇'[j]})</span>
                        <span class="equals">=</span>
                        <span class="result ${signClass}" style="color:${target.color}">${signStr}${target.symbol} ${target.name}</span>
                        ${xorExplain}
                    </div>
                    ${i > 0 && j > 0 && i !== j ? `<div class="commute-check">
                        Đảo: ${TRIGRAMS[j].symbol}×${TRIGRAMS[i].symbol} = ${MULT_TABLE[j][i].sign < 0 ? '−' : '+'}${TRIGRAMS[MULT_TABLE[j][i].index].symbol}
                        <span class="sign-badge khac">Không giao hoán!</span>
                    </div>` : ""}
                `;
            }
        } else {
            rows.forEach(row => {
                row.classList.remove("row-highlight");
                row.querySelectorAll("td").forEach(cell => {
                    cell.classList.remove("col-highlight", "active-cell");
                });
            });
            headers.forEach(th => th.classList.remove("col-highlight"));

            const info = document.getElementById("mult-info");
            if (info) {
                info.innerHTML = `<p class="hint">Hover một ô để xem chi tiết phép nhân</p>`;
            }
        }
    }

    return { init };
})();
