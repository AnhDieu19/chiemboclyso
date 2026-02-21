# 🎯 TECH LEAD ACTION PLAN - CRITICAL ISSUES RESOLUTION

**Date:** 22/12/2025  
**Tech Lead:** Auto  
**Priority:** 🔴 CRITICAL

---

## 📋 EXECUTIVE SUMMARY

QC review identified **2 CRITICAL issues** that must be fixed immediately:
1. **CUC_TABLE not used** - Table exists but code uses algorithm instead
2. **CUC_TABLE data incorrect** - Table values don't match expected standard

**Impact:** 
- Tests may pass but production results could be wrong
- Two sources of truth causing confusion
- Data integrity risk

---

## 🔍 ROOT CAUSE ANALYSIS

### Issue #1: CUC_TABLE Not Used
- **Location:** `core/cuc_calc.py` → `determine_cuc()` function
- **Current behavior:** Uses algorithmic calculation
- **Expected behavior:** Should use `CUC_TABLE` lookup (per tests and BA docs)
- **Why it matters:** Tests verify against table, but production uses algorithm

### Issue #2: CUC_TABLE Data Incorrect
- **Location:** `data/cung_cuc.py` → `CUC_TABLE` dictionary
- **Problem:** Table values don't match expected Nam Phái standard
- **Example:** Giáp+Tý should be "Thủy Nhị Cục" but table shows wrong value

---

## ✅ DECISION: APPROACH TO FIX

**Decision:** Use **Option A - Fix `determine_cuc()` to use CUC_TABLE**

**Rationale:**
1. Tests are written to verify against `CUC_TABLE`
2. BA documentation references table lookup
3. Table lookup is more maintainable and verifiable
4. Algorithm can be kept as fallback/verification

**Action Items:**
1. Fix `CUC_TABLE` data to match expected values
2. Modify `determine_cuc()` to use table lookup
3. Keep algorithm as validation/fallback
4. Update tests to verify both approaches match

---

## 🚀 IMPLEMENTATION PLAN

### Phase 1: Fix CUC_TABLE Data (HOTFIX - Priority 1)

**Task:** `TECH-001: Fix CUC_TABLE data values`

**Files to modify:**
- `python/data/cung_cuc.py`

**Expected values (from test_hotfix_cuc.py):**
```python
# Giáp/Kỷ (0, 5)
(0, 0): 'Thủy Nhị Cục', (0, 1): 'Hỏa Lục Cục', (0, 2): 'Mộc Tam Cục',
(0, 3): 'Mộc Tam Cục', (0, 4): 'Kim Tứ Cục', (0, 5): 'Kim Tứ Cục',
(0, 6): 'Thổ Ngũ Cục', (0, 7): 'Thổ Ngũ Cục', (0, 8): 'Hỏa Lục Cục',
(0, 9): 'Hỏa Lục Cục', (0, 10): 'Thủy Nhị Cục', (0, 11): 'Thủy Nhị Cục',

# Ất/Canh (1, 6)
(1, 0): 'Hỏa Lục Cục', (1, 1): 'Thủy Nhị Cục', (1, 2): 'Kim Tứ Cục',
(1, 3): 'Kim Tứ Cục', (1, 4): 'Thổ Ngũ Cục', (1, 5): 'Thổ Ngũ Cục',
(1, 6): 'Hỏa Lục Cục', (1, 7): 'Hỏa Lục Cục', (1, 8): 'Thủy Nhị Cục',
(1, 9): 'Thủy Nhị Cục', (1, 10): 'Mộc Tam Cục', (1, 11): 'Mộc Tam Cục',

# Bính/Tân (2, 7)
(2, 0): 'Thủy Nhị Cục', (2, 1): 'Mộc Tam Cục', (2, 2): 'Thổ Ngũ Cục',
(2, 3): 'Thổ Ngũ Cục', (2, 4): 'Hỏa Lục Cục', (2, 5): 'Hỏa Lục Cục',
(2, 6): 'Thủy Nhị Cục', (2, 7): 'Thủy Nhị Cục', (2, 8): 'Mộc Tam Cục',
(2, 9): 'Mộc Tam Cục', (2, 10): 'Kim Tứ Cục', (2, 11): 'Kim Tứ Cục',

# Đinh/Nhâm (3, 8)
(3, 0): 'Mộc Tam Cục', (3, 1): 'Kim Tứ Cục', (3, 2): 'Hỏa Lục Cục',
(3, 3): 'Hỏa Lục Cục', (3, 4): 'Thủy Nhị Cục', (3, 5): 'Thủy Nhị Cục',
(3, 6): 'Mộc Tam Cục', (3, 7): 'Mộc Tam Cục', (3, 8): 'Kim Tứ Cục',
(3, 9): 'Kim Tứ Cục', (3, 10): 'Thổ Ngũ Cục', (3, 11): 'Thổ Ngũ Cục',

# Mậu/Quý (4, 9)
(4, 0): 'Kim Tứ Cục', (4, 1): 'Thổ Ngũ Cục', (4, 2): 'Thủy Nhị Cục',
(4, 3): 'Thủy Nhị Cục', (4, 4): 'Mộc Tam Cục', (4, 5): 'Mộc Tam Cục',
(4, 6): 'Kim Tứ Cục', (4, 7): 'Kim Tứ Cục', (4, 8): 'Thổ Ngũ Cục',
(4, 9): 'Thổ Ngũ Cục', (4, 10): 'Hỏa Lục Cục', (4, 11): 'Hỏa Lục Cục',
```

**Verification:**
- Run `python tests/test_hotfix_cuc.py` - should pass
- Run `python tests/test_qc_regression_cuc.py` - should pass

**Estimated time:** 30 minutes

---

### Phase 2: Update determine_cuc() to Use Table (HOTFIX - Priority 1)

**Task:** `TECH-002: Refactor determine_cuc() to use CUC_TABLE`

**Files to modify:**
- `python/core/cuc_calc.py`

**Implementation:**
```python
def determine_cuc(year_can_index: int, menh_chi_index: int) -> dict:
    """
    Xác định Ngũ Hành Cục bằng tra bảng CUC_TABLE
    
    Args:
        year_can_index: Index Thiên Can năm sinh (0-9)
        menh_chi_index: Index Địa Chi Cung Mệnh (0-11)
        
    Returns:
        dict với 'name' và 'number' của Cục
    """
    from data import CUC_TABLE, CUC_TYPE
    
    # Giảm Can về 5 nhóm (0-4) vì mỗi nhóm có 2 Can cùng bảng
    can_group = year_can_index % 5
    
    # Tra bảng
    cuc_name = CUC_TABLE[can_group][menh_chi_index]
    
    # Lấy số cục
    cuc_number = CUC_TYPE.get(cuc_name, 2)  # Default 2 nếu không tìm thấy
    
    return {
        'name': cuc_name,
        'number': cuc_number
    }
```

**Keep algorithm as validation:**
```python
def _determine_cuc_algorithmic(year_can_index: int, menh_chi_index: int) -> dict:
    """
    Tính Cục bằng thuật toán (dùng để verify với bảng)
    """
    # ... existing algorithm code ...
```

**Add validation function:**
```python
def verify_cuc_calculation(year_can_index: int, menh_chi_index: int) -> bool:
    """
    Verify table lookup matches algorithm (for testing)
    """
    table_result = determine_cuc(year_can_index, menh_chi_index)
    algo_result = _determine_cuc_algorithmic(year_can_index, menh_chi_index)
    return table_result == algo_result
```

**Verification:**
- Run all existing tests - should pass
- Run `python tests/test_core_engine.py` - should pass
- Manual test with sample charts

**Estimated time:** 1 hour

---

### Phase 3: Update Tests (Priority 2)

**Task:** `TECH-003: Update tests to verify table usage`

**Files to modify:**
- `python/tests/test_core_engine.py` (if needed)
- Add integration test to verify table is actually used

**Estimated time:** 30 minutes

---

## 📊 TESTING STRATEGY

### Pre-deployment Tests:
1. ✅ Run `test_hotfix_cuc.py` - verify table data
2. ✅ Run `test_qc_regression_cuc.py` - verify all 60 cases
3. ✅ Run `test_core_engine.py` - verify core functionality
4. ✅ Run `test_compare_mau.py` - verify against reference chart
5. ✅ Manual test: Generate 5-10 sample charts and verify

### Post-deployment Tests:
1. Smoke test: Generate chart for known date
2. Regression test: Verify existing charts still work
3. Performance test: Ensure no degradation

---

## 🚨 RISK ASSESSMENT

| Risk | Impact | Mitigation |
|------|--------|------------|
| Table data still wrong | HIGH | Use test cases to verify |
| Algorithm was correct, table wrong | MEDIUM | Keep algorithm as fallback |
| Breaking existing charts | HIGH | Run full regression suite |
| Performance degradation | LOW | Table lookup is faster than algorithm |

---

## 📅 TIMELINE

| Phase | Task | Owner | Deadline | Status |
|-------|------|-------|----------|--------|
| 1 | Fix CUC_TABLE data | Dev | Today | ⏳ Pending |
| 2 | Update determine_cuc() | Dev | Today | ⏳ Pending |
| 3 | Run tests | QC | Today | ⏳ Pending |
| 4 | Code review | Tech Lead | Today | ⏳ Pending |
| 5 | Deploy hotfix | DevOps | Today | ⏳ Pending |

**Total estimated time:** 2-3 hours

---

## 🔄 MEDIUM PRIORITY ISSUES (Next Sprint)

After critical issues are fixed, address:

1. **Code duplication in chart_builder.py**
   - Refactor `generate_birth_chart()` and `generate_birth_chart_lunar()`
   - Estimated: 2 hours

2. **Hour format inconsistency**
   - Fix HTML to send Chi index directly
   - Estimated: 1 hour

3. **Exception handling**
   - Replace bare `except:` with specific exceptions
   - Estimated: 30 minutes

4. **Lazy imports**
   - Move analytics import to lazy loading
   - Estimated: 15 minutes

---

## 📝 NOTES

- Algorithm in `determine_cuc()` appears mathematically sound
- However, tests and BA docs expect table lookup
- Decision: Use table as source of truth, keep algorithm for validation
- This aligns with traditional Tử Vi practice (table-based lookup)

---

**Next Steps:**
1. Assign tasks to developers
2. Schedule code review
3. Prepare deployment plan
4. Update documentation

---

*Document created by Tech Lead*  
*Last updated: 22/12/2025*

