# ĐẶC TẢ ỨNG DỤNG: VI DIỆU PHÁP (ABHIDHAMMA APP)

**Ngày tạo:** 31/12/2024
**Phiên bản:** 1.0
**Mục tiêu:** Xây dựng công cụ hỗ trợ học tập và thực hành Thắng Pháp (Abhidhamma) và Thiền Định (Meditation).

---

## 1. MỤC TIÊU & TÍNH NĂNG CHÍNH (CORE OBJECTIVES)

**Mục tiêu cốt lõi:** Xây dựng hệ thống **Knowledge Graph (Đồ thị tri thức)** trực quan hóa cấu trúc Tâm và Sở Hữu Tâm của Vi Diệu Pháp, sử dụng thư viện **D3.js**. Giúp người học thấy rõ mối quan hệ chằng chịt và tương tác giữa các pháp thực tính.

### 1.1. Interactive Mind Graph (D3.js)
- **Nodes (Nút):**
    - **Citta Nodes:** 89/121 Tâm (Màu sắc phân theo Vực: Dục, Sắc, Vô Sắc, Siêu Thế).
    - **Cetasika Nodes:** 52 Sở Hữu Tâm (Màu sắc theo Nhóm: Bất Thiện, Tịnh Hảo...).
    - **Root Nodes:** 6 Nhân (Tham, Sân, Si, Vô Tham...).
- **Edges (Cạnh/Liên kết):**
    - **Associated With (Tương ưng):** Nối Tâm <-> Sở Hữu Tâm (Ví dụ: Tâm Tham nối với Sở hữu Tham, Tà kiến...).
    - **Root Cause (Nhân sanh):** Nối Tâm <-> Nhân.
- **Interactions:**
    - **Zoom/Pan:** Khám phá đồ thị khổng lồ.
    - **Filter:** Chỉ hiện Tâm Bất Thiện, hoặc chỉ hiện Tâm có Trí tuệ.
    - **Click:** Xem chi tiết (Definition, Pāli name) của Node bên sidebar.

### 1.2. Thư Viện Dữ Liệu Số (Paramattha Database)
- Tra cứu danh sách dạng bảng (Table View) cho những người muốn xem kiểu truyền thống.
- Search nhanh theo từ khóa Việt/Pāli.

### 1.3. Phân Tích Cấu Trúc (Strict Analysis)
- Chọn 1 Tâm bất kỳ -> Hệ thống highlight tất cả các Sở hữu tâm đi kèm.
- Chọn 1 Sở hữu tâm (VD: Tật - Ghen tị) -> Hệ thống sáng lên tất cả các Tâm mà Tật có thể sanh khởi.

---

## 2. KIẾN TRÚC DỮ LIỆU (DATA STRUCTURE)

### 2.1. Citta (Tâm)
```json
{
  "id": "citta_01",
  "name_vi": "Tâm Tham Câu Hành Hỷ Hợp Tà Vô Dẫn",
  "name_pali": "Somanassa-sahagatam ditthigata-sampayuttam asankharika-cittam",
  "group": "Bất Thiện Tâm",
  "factors": ["phassa", "vedana", "lobha", "ditthi", ...] // Các sở hữu tâm đi kèm
}
```



---

## 3. MASTER DATA DEFINITIONS (PYTHON DICT/TUPLE)
Cấu trúc dữ liệu chuẩn phục vụ Hard-mode coding (Define constants).

### 3.1. Phân loại Vực (Planes of Existence)
```python
CITTA_PLANES = {
    "KAMAVACARA": ("Dục Giới", 54),
    "RUPAVACARA": ("Sắc Giới", 15),
    "ARUPAVACARA": ("Vô Sắc Giới", 12),
    "LOKUTTARA": ("Siêu Thế", 8)  # Hoặc 40
}
```

### 3.2. Danh sách 52 Sở Hữu Tâm (Cetasikas Master)
```python
# Format: (ID, Pāli Name, Vietnamese Name, Group ID)
CETASIKAS_MASTER = [
    # Biến hành (Universals) - 7
    ("CET_01", "Phassa", "Xúc", "ANNASAMANA"),
    ("CET_02", "Vedana", "Thọ", "ANNASAMANA"),
    ("CET_03", "Sanna", "Tưởng", "ANNASAMANA"),
    ("CET_04", "Cetana", "Tư", "ANNASAMANA"),
    ("CET_05", "Ekaggata", "Nhất hành", "ANNASAMANA"),
    ("CET_06", "Jivitindriya", "Mạng quyền", "ANNASAMANA"),
    ("CET_07", "Manasikara", "Tác ý", "ANNASAMANA"),
    
    # Biệt cảnh (Occasionals) - 6
    ("CET_08", "Vitakka", "Tầm", "ANNASAMANA"),
    ("CET_09", "Vicara", "Tứ", "ANNASAMANA"),
    ("CET_10", "Adhimokkha", "Thắng giải", "ANNASAMANA"),
    ("CET_11", "Viriya", "Cần", "ANNASAMANA"),
    ("CET_12", "Piti", "Hỷ", "ANNASAMANA"),
    ("CET_13", "Chanda", "Dục", "ANNASAMANA"),
    
    # Bất thiện (Unwholesome) - 14
    ("CET_14", "Moha", "Si", "AKUSALA"),
    ("CET_15", "Ahirika", "Vô tàm", "AKUSALA"),
    ("CET_16", "Anottappa", "Vô quý", "AKUSALA"),
    ("CET_17", "Uddhacca", "Phóng dật", "AKUSALA"),
    ("CET_18", "Lobha", "Tham", "AKUSALA"),
    ("CET_19", "Ditthi", "Tà kiến", "AKUSALA"),
    ("CET_20", "Mana", "Ngã mạn", "AKUSALA"),
    ("CET_21", "Dosa", "Sân", "AKUSALA"),
    ("CET_22", "Issa", "Tật", "AKUSALA"),
    ("CET_23", "Macchariya", "Lận", "AKUSALA"),
    ("CET_24", "Kukkucca", "Hối", "AKUSALA"),
    ("CET_25", "Thina", "Hôn trầm", "AKUSALA"),
    ("CET_26", "Middha", "Thụy miên", "AKUSALA"),
    ("CET_27", "Vicikiccha", "Hoài nghi", "AKUSALA"),
    
    # Tịnh hảo (Beautiful) - 25
    ("CET_28", "Saddha", "Tín", "SOBHANA"),
    ("CET_29", "Sati", "Niệm", "SOBHANA"),
    ("CET_30", "Hiri", "Tàm", "SOBHANA"),
    ("CET_31", "Ottappa", "Quý", "SOBHANA"),
    ("CET_32", "Alobha", "Vô tham", "SOBHANA"),
    ("CET_33", "Adosa", "Vô sân", "SOBHANA"),
    ("CET_34", "Tatramajjhattata", "Trung bình (Xả)", "SOBHANA"),
    # ... (Các sở hữu tịnh hảo còn lại)
    ("CET_52", "Panna", "Trí tuệ", "SOBHANA")
]
```

### 3.3. Cấu Trúc Tâm (Citta Structure)
```python
class Citta:
    def __init__(self, id, pali_name, viet_name, plane, root, associated_cetasikas):
        self.id = id
        self.pali_name = pali_name
        self.viet_name = viet_name
        self.plane = plane  # Dục giới, Sắc giới...
        self.root = root    # Tham, Sân, Si, Vô tham...
        self.associated_cetasikas = associated_cetasikas # List các ID Cetasika đi kèm

# Ví dụ Data: Tâm Tham 1
CITTA_01 = Citta(
    id="CIT_01",
    pali_name="Somanassa-sahagatam ditthigata-sampayuttam asankharika-cittam",
    viet_name="Tâm Tham, câu hành Hỷ, hợp Tà, vô dẫn",
    plane="KAMAVACARA",
    root=["LOBHA", "MOHA"], # Sinh lên do Tham và Si
    associated_cetasikas=[
        "CET_01", "CET_02", "CET_03", "CET_04", "CET_05", "CET_06", "CET_07", # 7 Biến hành
        "CET_08", "CET_09", "CET_10", "CET_11", "CET_12", "CET_13",           # 6 Biệt cảnh
        "CET_14", "CET_15", "CET_16", "CET_17",                               # 4 Si phần
        "CET_18", "CET_19"                                                    # Tham, Tà kiến
    ]
)
```

---

```python
# Ví dụ Data: Tâm Tham 1
CITTA_01 = Citta(
    id="CIT_01",
    pali_name="Somanassa-sahagatam ditthigata-sampayuttam asankharika-cittam",
    viet_name="Tâm Tham, câu hành Hỷ, hợp Tà, vô dẫn",
    plane="KAMAVACARA",
    root=["LOBHA", "MOHA"], # Sinh lên do Tham và Si
    associated_cetasikas=[
        "CET_01", "CET_02", "CET_03", "CET_04", "CET_05", "CET_06", "CET_07", # 7 Biến hành
        "CET_08", "CET_09", "CET_10", "CET_11", "CET_12", "CET_13",           # 6 Biệt cảnh
        "CET_14", "CET_15", "CET_16", "CET_17",                               # 4 Si phần
        "CET_18", "CET_19"                                                    # Tham, Tà kiến
    ]
)
```

---

## 4. DIAGRAM: CẤU TRÚC 52 SỞ HỮU TÂM (CETASIKA RELATIONSHIPS)

Sơ đồ phân loại và quan hệ của 52 Sở Hữu Tâm (Mental Factors).

```mermaid
graph TD
    Root[52 Sở Hữu Tâm<br>(Cetasikas)]
    
    %% Groups
    G1[Nhóm Tờ Tha<br>(Annasamana - 13)]
    G2[Nhóm Bất Thiện<br>(Akusala - 14)]
    G3[Nhóm Tịnh Hảo<br>(Sobhana - 25)]
    
    Root --> G1
    Root --> G2
    Root --> G3
    
    %% Sub-Groups Tờ Tha
    G1 --> SG1A[Biến Hành - 7<br>(Universals)]
    G1 --> SG1B[Biệt Cảnh - 6<br>(Occasionals)]
    
    SG1A --> |Có mặt trong TẤT CẢ Tâm| AllCitta((Tất Cả 121 Tâm))
    SG1B --> |Chỉ có trong MỘT SỐ Tâm| SomeCitta((Một Số Tâm))
    
    %% Details Biến Hành
    SG1A --- C1(Xúc) & C2(Thọ) & C3(Tưởng) & C4(Tư) & C5(Nhất Hành) & C6(Mạng Quyền) & C7(Tác Ý)
    
    %% Sub-Groups Bất Thiện
    G2 --> SG2A[Si Phần - 4]
    G2 --> SG2B[Tham Phần - 3]
    G2 --> SG2C[Sân Phần - 4]
    G2 --> SG2D[Hôn Phần - 2]
    G2 --> SG2E[Nghi Phần - 1]
    
    SG2A --> |Có mặt trong 12 Tâm Bất Thiện| BadCitta((12 Tâm Bất Thiện))
    
    %% Details Bất Thiện (Sample)
    SG2B --- C18(Tham) & C19(Tà Kiến) & C20(Ngã Mạn)
    SG2C --- C21(Sân) & C22(Tật) & C23(Lận) & C24(Hối)

    %% Sub-Groups Tịnh Hảo
    G3 --> SG3A[Tịnh Hảo Biến Hành - 19]
    G3 --> SG3B[Ngăn Trừ Phần - 3]
    G3 --> SG3C[Vô Lượng Phần - 2]
    G3 --> SG3D[Trí Tuệ - 1]

    SG3A --> |Có mặt trong TẤT CẢ Tâm Tịnh Hảo| GoodCitta((59/91 Tâm Tịnh Hảo))
    SG3D --- C52(Trí Tuệ<br>Panna)
    
    style Root fill:#f9f,stroke:#333
    style G1 fill:#e1f5fe,stroke:#333
    style G2 fill:#ffebee,stroke:#333
    style G3 fill:#e8f5e9,stroke:#333
```

---

## 5. LỘ TRÌNH PHÁT TRIỂN (ROADMAP)


### Giai đoạn 1: Data Structuring (Database)
- Xây dựng JSON/Dict Data cho 121 Tâm và 52 Sở hữu tâm.
- Define relationship matrix (Tâm nào - Sở hữu nào).

### Giai đoạn 2: Knowledge Graph Visualization (D3.js Core)
- Setup D3.js Force Directed Graph.
- Render Nodes & Edges từ Data.
- Implement Zoom/Pan/Drag interactions.

### Giai đoạn 3: Advanced Analysis & Filtering
- Filter theo nhóm (Chỉ hiện Bất Thiện, Chỉ hiện Thiền...).
- Highlight interactions (Click Node A -> Highligt connected Nodes).
- Sidebar chi tiết thông tin Pāli/Việt.
