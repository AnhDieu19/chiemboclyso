/**
 * ai-chat.js - AI Master Chat Modal
 * Giao diện chat với thầy tử vi AI
 */

let aiChatHistory = [];

function openAIModal() {
    const modal = document.getElementById('aiModal');
    if (modal) {
        modal.style.display = 'block';
        aiChatHistory = [];
        document.getElementById('aiChatMessages').innerHTML = `
            <div class="ai-welcome-box">
                <div class="ai-welcome-icon">🧙‍♂️</div>
                <p>Xin chào! Tôi là thầy tử vi AI với 50 năm kinh nghiệm.</p>
                <p class="ai-welcome-hint">Nhấn "Xin Thầy Luận Giải" để tôi xem lá số của bạn,<br>hoặc gõ câu hỏi vào ô bên dưới.</p>
            </div>
        `;
    }
}

function closeAIModal() {
    const modal = document.getElementById('aiModal');
    if (modal) {
        modal.style.display = 'none';
    }
}

async function askAIFull() {
    if (!window.currentChart) {
        alert('Vui lòng tạo lá số trước!');
        return;
    }

    const messagesDiv = document.getElementById('aiChatMessages');
    messagesDiv.innerHTML = `
        <div style="text-align:center;padding:50px">
            <div class="spinner" style="margin:0 auto 20px"></div>
            <p>Thầy đang xem lá số, xin đợi giây lát...</p>
        </div>
    `;

    try {
        const response = await fetch('/api/ask-ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chart: window.currentChart,
                interpretation: window.currentInterpretation
            })
        });

        const result = await response.json();

        if (result.success) {
            messagesDiv.innerHTML = `
                <div class="ai-message" style="background:#f0f4ff;padding:15px;border-radius:12px;margin:10px 0;border-left:4px solid #667eea">
                    <div style="display:flex;align-items:center;margin-bottom:10px">
                        <span style="font-size:24px;margin-right:10px">🧙‍♂️</span>
                        <strong style="color:#667eea">Thầy Tử Vi AI</strong>
                    </div>
                    <div style="white-space:pre-wrap;line-height:1.7;font-size:14px">${formatAIResponse(result.response)}</div>
                </div>
            `;
        } else {
            messagesDiv.innerHTML = `
                <div style="background:#fff0f0;padding:15px;border-radius:8px;color:#c00">
                    <strong>Lỗi:</strong> ${result.response || result.error}
                </div>
            `;
        }
    } catch (error) {
        messagesDiv.innerHTML = `
            <div style="background:#fff0f0;padding:15px;border-radius:8px;color:#c00">
                <strong>Lỗi kết nối:</strong> ${error.message}
            </div>
        `;
    }
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

async function sendChatMessage() {
    const input = document.getElementById('aiChatInput');
    const message = input.value.trim();

    if (!message) return;
    if (!window.currentChart) {
        alert('Vui lòng tạo lá số trước!');
        return;
    }

    input.value = '';

    const messagesDiv = document.getElementById('aiChatMessages');

    messagesDiv.innerHTML += `
        <div class="user-message" style="background:#e3f2fd;padding:12px 15px;border-radius:12px;margin:10px 0;text-align:right;border-right:4px solid #2196f3">
            <strong>Bạn:</strong> ${escapeHtml(message)}
        </div>
        <div id="aiLoading" style="text-align:left;padding:10px">
            <span style="color:#666">Thầy đang suy nghĩ...</span>
        </div>
    `;

    messagesDiv.scrollTop = messagesDiv.scrollHeight;

    try {
        const response = await fetch('/api/chat-ai', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                chart: window.currentChart,
                interpretation: window.currentInterpretation,
                message: message,
                history: aiChatHistory
            })
        });

        const result = await response.json();

        const loading = document.getElementById('aiLoading');
        if (loading) loading.remove();

        if (result.success) {
            messagesDiv.innerHTML += `
                <div class="ai-message" style="background:#f0f4ff;padding:12px 15px;border-radius:12px;margin:10px 0;border-left:4px solid #667eea">
                    <div style="display:flex;align-items:center;margin-bottom:8px">
                        <span style="font-size:20px;margin-right:8px">🧙‍♂️</span>
                        <strong style="color:#667eea">Thầy</strong>
                    </div>
                    <div style="white-space:pre-wrap;line-height:1.6;font-size:14px">${formatAIResponse(result.response)}</div>
                </div>
            `;

            aiChatHistory.push({ role: 'user', parts: [message] });
            aiChatHistory.push({ role: 'model', parts: [result.response] });
        } else {
            messagesDiv.innerHTML += `
                <div style="background:#fff0f0;padding:10px;border-radius:8px;color:#c00;margin:10px 0">
                    ${result.response || result.error}
                </div>
            `;
        }

        messagesDiv.scrollTop = messagesDiv.scrollHeight;

    } catch (error) {
        const loading = document.getElementById('aiLoading');
        if (loading) loading.remove();

        messagesDiv.innerHTML += `
            <div style="background:#fff0f0;padding:10px;border-radius:8px;color:#c00;margin:10px 0">
                Lỗi: ${error.message}
            </div>
        `;
    }
}

function formatAIResponse(text) {
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/^### (.*$)/gm, '<h4 style="margin:15px 0 8px;color:#667eea">$1</h4>')
        .replace(/^## (.*$)/gm, '<h3 style="margin:18px 0 10px;color:#333">$1</h3>')
        .replace(/^- (.*$)/gm, '• $1');
}

// Handle Enter key in chat input
document.addEventListener('keypress', function (e) {
    if (e.target.id === 'aiChatInput' && e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendChatMessage();
    }
});
