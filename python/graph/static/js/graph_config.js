/**
 * Tu Vi Knowledge Graph Configuration
 * 
 * This file contains all the settings for the graph's appearance and behavior.
 * Modify this file to change colors, forces, sizes, and other visual properties.
 */

const TuViGraphConfig = {
    // ========================================================================
    // 1. VISUAL SETTINGS (COLORS)
    // ========================================================================
    colors: {
        // Ngũ Hành (The Five Elements) - High Priority Colors
        ngu_hanh: {
            "Kim": "#FFFFFF",       // Trắng (White)
            "Mộc": "#2ecc71",     // Xanh Lục (Green)
            "Thủy": "#00a8ff",    // Xanh Dương Sáng (Blue)
            "Hỏa": "#ff4757",     // Đỏ (Red)
            "Thổ": "#ffa502"      // Vàng Đất (Orange/Yellow)
        },

        // Node Types (Categories)
        types: {
            ngu_hanh: "#dfe6e9",      // Default for Ngũ Hành group if specific element not found
            thien_can: "#E91E63",     // Thiên Can (Pink)
            dia_chi: "#00BCD4",       // Địa Chi (Cyan)
            chinh_tinh_tuvi: "#FF6B6B", // Chính Tinh - Vòng Tử Vi (Coral Red)
            chinh_tinh_phu: "#4ECDC4",  // Chính Tinh - Vòng Thiên Phủ (Turquoise)
            luc_cat: "#27ae60",       // Lục Cát (Emerald)
            luc_sat: "#e74c3c",       // Lục Sát (Red)
            tu_hoa: "#9b59b6",        // Tứ Hóa (Purple)
            muoi_hai_cung: "#e1b12c", // 12 Cung (Yellow/Gold)
            thai_tue: "#f39c12",      // Thái Tuế (Orange)
            truong_sinh: "#1abc9c",   // Trường Sinh (Teal)
            bac_sy: "#34495e",        // Bác Sĩ (Dark Blue)
            tap_tinh: "#95a5a6",      // Tạp Tinh (Grey)
            default: "#888888"        // Fallback color
        },

        // Link/Edge Colors (Relationships)
        links: {
            sinh: "#27ae60",      // Tương Sinh (Green)
            khac: "#e74c3c",      // Tương Khắc (Red)
            thuoc: "#888888",     // Thuộc (Grey)
            vong: "#3498db",      // Vòng (Blue)
            dong_hanh: "#9b59b6"  // Đồng Hành (Purple)
        }
    },

    // ========================================================================
    // 2. DIMENSIONS & SIZES
    // ========================================================================
    dimensions: {
        nodeRadius: {
            default: 20,
            hover: 25   // slightly larger when interacting (handled in CSS/JS usually but good to note)
        },
        strokeWidth: {
            node: 2,
            link: {
                sinh: 4,
                khac: 3,
                thuoc: 2,
                vong: 2,
                dong_hanh: 2
            }
        },
        arrowMarkerSize: 6
    },

    // ========================================================================
    // 3. SIMULATION SETTINGS (PHYSICS)
    // ========================================================================
    simulation: {
        chargeStrength: -1000,   // Negative value repels nodes (spreads them out)
        chargeDistanceMax: 600,  // Maximum distance where charge force is applied
        linkDistance: 150,       // Preferred distance between connected nodes
        collisionStrength: 0.7,  // Prevents node overlap (0 to 1)
        collisionPadding: 15     // Extra space around nodes for collision detection
    },

    // ========================================================================
    // 4. ZOOM & PAN
    // ========================================================================
    zoom: {
        minScale: 0.2,
        maxScale: 5,
        transitionDuration: 750 // Milliseconds for reset zoom animation
    },

    // ========================================================================
    // 5. OPACITY SETTINGS
    // ========================================================================
    opacity: {
        active: 1.0,
        inactive: 0.1,    // Dimmed state for nodes
        linkActive: 1.0,
        linkInactive: 0.05,
        linkHidden: 0.0
    }
};

// Expose to global scope
window.TuViGraphConfig = TuViGraphConfig;
