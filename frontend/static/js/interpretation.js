/**
 * interpretation.js - Chart Interpretation Rendering
 * Hiển thị giải đoán lá số tử vi
 */

function renderInterpretation(interpretation, chart) {
    const div = document.getElementById('interpretation');
    const basic = interpretation.basic_info || {};
    const menh = interpretation.menh_interpretation || {};
    const than = interpretation.than_interpretation || {};
    const tuHoaAnalysis = interpretation.tu_hoa_analysis || [];
    const lifeAspects = interpretation.life_aspects || {};

    const strengthBadge = (strength) => {
        const colors = {
            'Rất tốt': '#006400',
            'Tốt': '#228B22',
            'Trung bình': '#DAA520',
            'Nhiều thử thách': '#CD853F',
            'Khó khăn': '#8B0000'
        };
        return `<span style="background:${colors[strength] || '#666'};color:#fff;padding:2px 8px;border-radius:4px;font-size:12px">${strength}</span>`;
    };

    const aspectLabels = {
        'su_nghiep': '💼 Sự nghiệp',
        'tai_chinh': '💰 Tài chính',
        'hon_nhan': '💕 Hôn nhân',
        'suc_khoe': '🏋️ Sức khỏe',
        'con_cai': '👶 Con cái',
        'gia_dinh': '🏡 Gia đình',
        'di_chuyen': '✈️ Di chuyển'
    };

    let lifeAspectsHtml = '';
    for (const [key, label] of Object.entries(aspectLabels)) {
        const aspect = lifeAspects[key] || {};
        if (aspect.strength) {
            lifeAspectsHtml += `
                <div style="border:1px solid #ddd;padding:10px;margin:5px 0;border-radius:5px;background:#fafafa">
                    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px">
                        <strong>${label}</strong>
                        ${strengthBadge(aspect.strength)}
                    </div>
                    <p style="margin:0;font-size:13px;color:#555">${aspect.interpretation || ''}</p>
                    ${aspect.combination_effects?.length ? `<p style="margin:5px 0 0;font-size:12px;color:#006400">✦ ${aspect.combination_effects.join(' ✦ ')}</p>` : ''}
                </div>
            `;
        }
    }

    let tuHoaHtml = tuHoaAnalysis.length ? tuHoaAnalysis.map(t => `<li>${t}</li>`).join('') : '<li>Không có dữ liệu Tứ Hóa</li>';

    div.innerHTML = `
        <h3 class="interp-title">📖 GIẢI ĐOÁN CHI TIẾT LÁ SỐ</h3>
        
        <div class="interp-section" style="background:#f0f7ff;padding:15px;border-radius:8px;margin-bottom:15px">
            <h4 style="margin-top:0">🌟 Thông Tin Cơ Bản</h4>
            <table style="width:100%;border-collapse:collapse">
                <tr><td style="padding:5px"><strong>Năm sinh:</strong></td><td>${basic.year_can_chi || '?'}</td>
                    <td style="padding:5px"><strong>Bản Mệnh (Nạp Âm):</strong></td><td>${basic.nap_am || '?'}</td></tr>
                <tr><td style="padding:5px"><strong>Cục:</strong></td><td>${basic.cuc || '?'}</td>
                    <td style="padding:5px"><strong>Cung Mệnh:</strong></td><td>${basic.menh_chi || '?'}</td></tr>
                <tr><td style="padding:5px"><strong>Cung Thân:</strong></td><td>${basic.than_chi || '?'}</td>
                    <td></td><td></td></tr>
            </table>
            
            <div style="display:flex;justify-content:center;gap:20px;margin-top:15px;padding:10px;background:linear-gradient(135deg,rgba(139,0,0,0.1),rgba(218,165,32,0.1));border-radius:8px">
                <div style="text-align:center;padding:10px 25px;background:rgba(139,0,0,0.15);border:2px solid #8B0000;border-radius:6px;min-width:130px">
                    <div style="font-size:11px;font-weight:600;text-transform:uppercase;color:#666">Mệnh Chủ</div>
                    <div style="font-size:15px;font-weight:700;color:#8B0000;margin-top:5px">★ ${basic.menh_chu || '?'}</div>
                </div>
                <div style="text-align:center;padding:10px 25px;background:rgba(218,165,32,0.15);border:2px solid #DAA520;border-radius:6px;min-width:130px">
                    <div style="font-size:11px;font-weight:600;text-transform:uppercase;color:#666">Thân Chủ</div>
                    <div style="font-size:15px;font-weight:700;color:#DAA520;margin-top:5px">★ ${basic.than_chu || '?'}</div>
                </div>
            </div>
        </div>
        
        <div class="interp-section" style="background:#fffff0;padding:15px;border-radius:8px;margin-bottom:15px">
            <div style="display:flex;justify-content:space-between;align-items:center">
                <h4 style="margin:0">Đại Cung Mệnh</h4>
                ${strengthBadge(menh.strength || 'Trung bình')}
            </div>
            <p style="margin:10px 0">${menh.interpretation || 'Đang phân tích...'}</p>
            ${menh.key_stars?.length ? `<p><strong>Chính Tinh:</strong> ${menh.key_stars.join(', ')}</p>` : ''}
            ${menh.combination_effects?.length ? `
                <div style="background:#e8f5e9;padding:10px;border-radius:5px;margin-top:10px">
                    <strong>🔮 Cách cục đặc biệt:</strong>
                    <ul style="margin:5px 0 0;padding-left:20px">
                        ${menh.combination_effects.map(e => `<li>${e}</li>`).join('')}
                    </ul>
                </div>
            ` : ''}
        </div>
        
        <div class="interp-section" style="background:#fff5f5;padding:15px;border-radius:8px;margin-bottom:15px">
            <h4 style="margin-top:0">Tứ Hóa & Ảnh Hưởng</h4>
            <ul style="margin:0;padding-left:20px;line-height:1.8">
                ${tuHoaHtml}
            </ul>
        </div>
        
        <div class="interp-section" style="margin-bottom:15px">
            <h4>📊 Các Phương Diện Cuộc Sống</h4>
            ${lifeAspectsHtml || '<p>Đang phân tích các phương diện...</p>'}
        </div>
        
        ${interpretation.cach_cuc?.length ? `
        <div class="interp-section" style="background:#fff8e1;padding:15px;border-radius:8px;margin-bottom:15px">
            <h4 style="margin-top:0">🌟 Cách Cục Đặc Biệt</h4>
            <div style="display:flex;flex-wrap:wrap;gap:10px">
                ${interpretation.cach_cuc.map(cc => `
                    <div style="background:${cc.rank?.includes('Hung') ? 'rgba(244,67,54,0.1)' : 'rgba(76,175,80,0.1)'};
                                border:1px solid ${cc.rank?.includes('Hung') ? '#f44336' : '#4caf50'};
                                padding:12px;border-radius:8px;flex:1;min-width:280px">
                        <div style="font-weight:bold;color:${cc.rank?.includes('Hung') ? '#c62828' : '#2e7d32'}">
                            ${cc.icon || '✨'} ${cc.name}
                        </div>
                        <div style="font-size:12px;color:#666;margin-top:4px">${cc.rank}</div>
                        ${cc.stars?.length ? `
                            <div style="font-size:11px;color:#1565c0;margin-top:6px;background:rgba(33,150,243,0.1);padding:4px 8px;border-radius:4px;display:inline-block">
                                📋 Sao cần có: ${cc.stars.join(', ')}
                            </div>
                        ` : ''}
                        ${cc.detection_details ? `
                            <div style="font-size:11px;color:#7b1fa2;margin-top:6px;background:rgba(156,39,176,0.1);padding:4px 8px;border-radius:4px">
                                📍 ${cc.detection_details}
                            </div>
                        ` : ''}
                        <div style="font-size:13px;margin-top:8px">${cc.meaning}</div>
                        <div style="font-size:12px;color:#555;margin-top:8px;font-style:italic">💡 ${cc.advice}</div>
                    </div>
                `).join('')}
            </div>
        </div>
        ` : ''}
        
        ${window.currentTaiMenh ? renderTaiMenhSection(window.currentTaiMenh) : ''}
        
        <div class="interp-section" style="background:#e8f5e9;padding:15px;border-radius:8px;margin-bottom:15px">
            <h4 style="margin-top:0">🔮 Tổng Quan Vận Mệnh</h4>
            <p style="font-size:14px;line-height:1.6">${interpretation.fortune || ''}</p>
        </div>
        
        <div class="interp-section" style="background:#fff3e0;padding:15px;border-radius:8px;margin-bottom:15px">
            <h4 style="margin-top:0">💡 Lời Khuyên</h4>
            <p style="font-size:14px;line-height:1.6">${interpretation.advice || ''}</p>
        </div>
        
        <!-- Nút Hỏi Thầy AI -->
        <div class="interp-section" style="background:linear-gradient(135deg,#667eea,#764ba2);padding:20px;border-radius:12px;text-align:center">
            <h4 style="margin:0 0 10px;color:#fff">🧙 Thầy Tử Vi AI</h4>
            <p style="color:rgba(255,255,255,0.9);margin-bottom:15px;font-size:13px">
                Hỏi thầy tử vi AI với 50 năm kinh nghiệm để được luận giải chi tiết
            </p>
            <button onclick="openAIModal()" style="background:#fff;color:#667eea;border:none;padding:12px 30px;border-radius:25px;font-weight:bold;cursor:pointer;font-size:14px;box-shadow:0 4px 15px rgba(0,0,0,0.2)">
                🔮 Hỏi Thầy AI Luận Giải
            </button>
        </div>
    `;
}

function renderTaiMenhSection(tm) {
    return `
        <div class="interp-section" style="background:linear-gradient(135deg,rgba(255,215,0,0.15),rgba(255,165,0,0.15));padding:15px;border-radius:8px;margin-bottom:15px;border:2px solid #DAA520">
            <h4 style="margin-top:0;color:#B8860B">📖 TÀI và MỆNH - "Chữ Tài chữ Mệnh khéo là ghét nhau"</h4>
            <div style="font-style:italic;color:#666;font-size:12px;margin-bottom:15px;padding:10px;background:rgba(255,255,255,0.7);border-radius:5px">
                Theo triết lý Truyện Kiều của Nguyễn Du: Con người có TÀI (tài năng) cao thường có MỆNH (may mắn) thấp và ngược lại.
            </div>
            
            <div style="display:flex;gap:15px;margin-bottom:15px">
                <div style="flex:1;text-align:center;padding:15px;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
                    <div style="font-size:11px;color:#666;text-transform:uppercase;margin-bottom:5px">Tài Năng</div>
                    <div style="font-size:32px;font-weight:bold;color:${tm.tai_score >= 7 ? '#4caf50' : tm.tai_score <= 4 ? '#f44336' : '#ff9800'};line-height:1">
                        ${tm.tai_score}
                    </div>
                    <div style="font-size:11px;color:#999">/10</div>
                </div>
                <div style="flex:1;text-align:center;padding:15px;background:#fff;border-radius:8px;box-shadow:0 2px 8px rgba(0,0,0,0.1)">
                    <div style="font-size:11px;color:#666;text-transform:uppercase;margin-bottom:5px">May Mắn</div>
                    <div style="font-size:32px;font-weight:bold;color:${tm.menh_score >= 7 ? '#4caf50' : tm.menh_score <= 4 ? '#f44336' : '#ff9800'};line-height:1">
                        ${tm.menh_score}
                    </div>
                    <div style="font-size:11px;color:#999">/10</div>
                </div>
            </div>
            
            <div style="text-align:center;padding:12px;background:rgba(255,255,255,0.9);border-radius:8px;margin-bottom:12px;border-left:4px solid #DAA520">
                <div style="font-weight:bold;font-size:16px;color:#8B4513;margin-bottom:5px">${tm.category}</div>
                <div style="font-size:14px;color:#555;line-height:1.5">${tm.insight}</div>
            </div>
            
            ${tm.advice && tm.advice.length > 0 ? `
            <div style="margin-top:15px;padding:15px;background:rgba(255,215,0,0.2);border-radius:8px;border-left:4px solid #f39c12">
                <strong style="color:#B8860B;font-size:15px">💡 Lời khuyên:</strong>
                <ul style="margin:8px 0;padding-left:20px;font-size:13px;line-height:1.8;color:#555">
                    ${tm.advice.map(a => `<li style="margin-bottom:5px">${a}</li>`).join('')}
                </ul>
            </div>
            ` : ''}
            
            <details style="margin-top:12px">
                <summary style="cursor:pointer;font-weight:600;color:#8B4513;padding:8px;background:rgba(255,255,255,0.5);border-radius:5px">
                    📊 Chi tiết yếu tố
                </summary>
                <div style="margin-top:10px;padding:10px;background:rgba(255,255,255,0.7);border-radius:5px">
                    <div style="margin-bottom:10px">
                        <strong style="color:#2e7d32">🎨 Tài Năng:</strong>
                        <ul style="margin:5px 0;padding-left:20px;font-size:13px">
                            ${(tm.tai_factors || []).map(f => `<li>${f}</li>`).join('') || '<li>Không có yếu tố đặc biệt</li>'}
                        </ul>
                    </div>
                    <div>
                        <strong style="color:#1976d2">🍀 May Mắn:</strong>
                        <ul style="margin:5px 0;padding-left:20px;font-size:13px">
                            ${(tm.menh_factors || []).map(f => `<li>${f}</li>`).join('') || '<li>Không có yếu tố đặc biệt</li>'}
                        </ul>
                    </div>
                </div>
            </details>
        </div>
    `;
}
