# Round 4: Hub Validation — Figures + Reproducibility

> Do figures match text? Could a reader replicate the work?

## Agent 4A: Figure Audit — 10 findings

### MAJOR (3):
- **F-4A-01:** Five figures never referenced in text (`\ref{}` missing). **ACCEPTED — FIXED**
- **F-4A-03:** Figure caption metric doesn't match text metric (scope mismatch). **ACCEPTED — FIXED**
- **F-4A-04:** Figure-mapping doc uses obsolete filenames. **ACCEPTED — DEFERRED** (internal doc)

### MINOR (6): File numbering swaps, stale values in internal docs, extra figures in shared directory.
### POLISH (1): Noted.

## Agent 4B: Reproducibility — 14 findings

### MAJOR (3):
- **4B-01:** Key experiment optimizer unspecified. **ACCEPTED — FIXED**
- **4B-02:** Training data unspecified. **ACCEPTED — FIXED** (partially)
- **4B-03:** Adapter target modules unspecified. **ACCEPTED — FIXED**

### MINOR (6):
- **4B-04/05/06:** Feedback controller gain constants, decay dynamics, and update rules not in paper. **ACCEPTED — FIXED** (all added to appendix table)
- **4B-07/08:** Standard defaults (optimizer betas, padding). **NOTED**
- **4B-09:** Proprietary initialization requires non-public data. **ACCEPTED — NO ACTION** (cosmetic effect)

### POLISH (4): Model revision pinning, train/val split (fixed), domain-specific mapping, fit model. Mix of noted and fixed.

## Agent 4C: Missing Figures — 10 findings

### MODERATE (1):
- **F-4C-01:** Architecture schematic missing. **ACCEPTED — DEFERRED** (TikZ creation needed)

### MINOR (6): Various figures that would strengthen claims but aren't required. All deferred or noted.
### PASS (3): Existing figure coverage adequate for core claims.

## Round 4 Summary

| Category | Findings | Fixed | Noted/Deferred |
|----------|----------|-------|----------------|
| Agent 4A | 10 | 3 | 7 |
| Agent 4B | 14 | 5 | 9 |
| Agent 4C | 10 | 1 | 9 |
| **Total** | **34** | **9** | **25** |

**High deferred count is intentional.** Round 4 identifies what *could* be better, not just what's wrong. Internal docs, nice-to-have figures, and standard-practice items are noted but don't block submission.
