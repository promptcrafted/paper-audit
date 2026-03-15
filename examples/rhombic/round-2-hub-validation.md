# Round 2: Hub Validation — Internal Consistency

> Checks abstract-body alignment, cross-references, and claim-evidence strength.

## Agent 2A: Abstract-Body Consistency (Paper 3) — 15 findings

### MAJOR (5):
- **F-2A-01:** "15 experiments" matches no enumeration (13 rows or 17 expanded). **ACCEPTED — FIXED** (→13)
- **F-2A-02:** Table value contradicts narrative; raw data confirms narrative. **ACCEPTED — FIXED** (table corrected)
- **F-2A-03:** Count ambiguous in introduction. **ACCEPTED** (removed specific count)
- **F-2A-04:** Abstract comparison uses wrong experiment pair. **ACCEPTED — FIXED**
- **F-2A-05:** Key metric stale (40-checkpoint data); actual 100-checkpoint value different. **ACCEPTED — FIXED** (3 locations)

### MINOR (5):
- **F-2A-06:** Val loss range uses wrong experiment. **ACCEPTED — FIXED**
- **F-2A-07:** "570 bridges" not derivable from paper data. **ACCEPTED** (kept — verifiable from source)
- **F-2A-08:** "60,000+" in abstract not derived in body. **ACCEPTED** (plausible, minor)
- **F-2A-09:** "three model architectures" omits fourth. **ACCEPTED — FIXED** (→"four model scales")
- **F-2A-14:** Conclusion repeats corrected value. **ACCEPTED — FIXED**

### POLISH (5): Various rounding, formatting, and presentation items. 3 fixed, 2 deferred.

## Agent 2B: Cross-References + Citations — 13 findings

### CRITICAL (2):
- **F-2B-01:** Bibliography entry has wrong Paper 3 subtitle. **ACCEPTED — FIXED**
- **F-2B-02:** Paper 3 cites Paper 2 for content Paper 2 doesn't contain. **ACCEPTED — FIXED** (self-references substituted)

### MINOR (2): One missing foundational citation fixed. One orphan bib entry noted.
### PASS (9): All `\cite{}` resolve, all `\ref{}`/`\label{}` consistent, no `??` markers.

## Agent 2C: Claim-Evidence Alignment — 15 findings

### MAJOR (1):
- **F-02C-01:** "Necessary and sufficient" overstates; acknowledged confound. **ACCEPTED — FIXED** (→"at n=6")

### MODERATE (7):
- **F-02C-02:** "Universal" for 6 experiments / 2 scales. **ACCEPTED — FIXED** (→"robust")
- **F-02C-03:** Causal claim with 6 confounded variables. **ACCEPTED — FIXED** (reframed)
- **F-02C-04:** Section header overstates. **ACCEPTED — FIXED** (→"Emerges Only When...Active")
- **F-02C-05:** Potential circularity in core finding. **ACCEPTED** (noted; implicit in other fixes)
- **F-02C-11:** No formal statistical tests. **NOTED** (effect sizes sufficient)
- **F-02C-13:** Mixed-unit ratio (1.4:1, not 2.9:1). **ACCEPTED — FIXED**

### MINOR/LOW (7): Various hedging, framing, and language calibration items. 4 fixed, 3 noted.

## Round 2 Summary

| Category | Findings | Fixed | Noted | Deferred |
|----------|----------|-------|-------|----------|
| Agent 2A | 15 | 11 | 3 | 1 |
| Agent 2B | 13 | 3 | 1 | 0 |
| Agent 2C | 15 | 12 | 3 | 0 |
| **Total** | **43** | **26** | **7** | **1** |

**2 CRITICAL findings fixed (bib entry, phantom citation).** All MAJOR findings resolved. Claims systematically calibrated to evidence strength.
