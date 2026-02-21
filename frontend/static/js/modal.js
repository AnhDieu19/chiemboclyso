
let constraints = {};

function addConstraint() {
    const star = document.getElementById('revStarSelect').value;
    const palaceVal = document.getElementById('revPalaceSelect').value;
    const palaceName = document.getElementById('revPalaceSelect').options[document.getElementById('revPalaceSelect').selectedIndex].text;

    constraints[star] = parseInt(palaceVal);
    renderConstraints();
}

function removeConstraint(star) {
    delete constraints[star];
    renderConstraints();
}

function renderConstraints() {
    const list = document.getElementById('constraintList');
    list.innerHTML = '';
    const palaceNames = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"];

    for (const [star, palace] of Object.entries(constraints)) {
        const li = document.createElement('li');
        li.style.display = 'flex';
        li.style.justifyContent = 'space-between';
        li.style.marginBottom = '5px';
        const safeStar = star.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
        li.innerHTML = `
            <span><b>${safeStar}</b> tại <b>${palaceNames[palace]}</b></span>
        `;
        const removeBtn = document.createElement('span');
        removeBtn.style.cssText = 'color:red; cursor:pointer;';
        removeBtn.textContent = '×';
        removeBtn.addEventListener('click', () => removeConstraint(star));
        li.appendChild(removeBtn);
        list.appendChild(li);
    }
}

async function searchDates() {
    if (Object.keys(constraints).length === 0) {
        alert("Vui lòng thêm ít nhất 1 điều kiện sao!");
        return;
    }

    const resDiv = document.getElementById('searchResults');
    resDiv.innerHTML = '<div style="text-align:center">Đang tìm kiếm...</div>';

    try {
        const response = await fetch('/api/finder/solve', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ stars: constraints })
        });

        const data = await response.json();

        if (data.error) {
            resDiv.innerHTML = `<div style="color:red">Lỗi: ${data.error}</div>`;
            return;
        }

        if (data.results.length === 0) {
            resDiv.innerHTML = '<div style="text-align:center">Không tìm thấy ngày sinh nào phù hợp!</div>';
            return;
        }

        let html = `<div style="margin-bottom:10px;">Tìm thấy <b>${data.count}</b> kết quả:</div>`;
        html += '<ul style="padding-left: 20px;">';
        data.results.forEach(item => {
            html += `<li style="margin-bottom: 5px;">${item.display}</li>`;
        });
        html += '</ul>';
        resDiv.innerHTML = html;

    } catch (e) {
        resDiv.innerHTML = `<div style="color:red">Lỗi kết nối: ${e}</div>`;
    }
}

// Quick helper to open modal
function openReverseLookup() {
    document.getElementById('reverseLookupModal').style.display = 'block';
}

// Close modal logic
document.addEventListener('DOMContentLoaded', () => {
    const closeBtn = document.querySelector('#reverseLookupModal .close');
    if (closeBtn) {
        closeBtn.onclick = function () {
            document.getElementById('reverseLookupModal').style.display = 'none';
        }
    }

    window.addEventListener('click', function (event) {
        if (event.target == document.getElementById('reverseLookupModal')) {
            document.getElementById('reverseLookupModal').style.display = 'none';
        }
    });
});
