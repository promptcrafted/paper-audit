# Round 6: Hub Validation — Bibliography + Claims Calibration

> Citations complete? Claims properly calibrated to evidence strength?

## Agent 6A: Citation Completeness — 3 findings

- **F-6A-01 (MAJOR):** 9 orphan bib entries (39% orphan rate). **ACCEPTED — PARTIALLY FIXED** (2 cited, 6 removed, 1 kept)
- **F-6A-02 (MINOR):** 4 orphan bib entries in Paper 2. **ACCEPTED — FIXED** (removed)
- **F-6A-03 (MINOR):** One citation's framing noted. **NOTED — NO ACTION**

## Agent 6B: Related Work Gaps — 8 findings

### HIGH (2):
- **F-6B-01:** Key comparison method (LoRA-XS) discussion lost during consolidation. **ACCEPTED — FIXED** (restored)
- **F-6B-02:** Key comparison method (MELoRA) discussion lost during consolidation. **ACCEPTED — FIXED** (restored)

### MEDIUM (3):
- **F-6B-03/04:** Two methods not cited. **NOTED — NO ACTION** (different technique category)
- **F-6B-05:** Foundational cybernetics reference uncited in text. **ACCEPTED — FIXED**

### LOW (3): Uncited adapter merging cluster removed from bib. **ACCEPTED — FIXED**

## Agent 6C: Claims Calibration — 13 findings

### HIGH (2):
- **F-6C-H1:** "natural representational structure" implies pre-existing preference. **ACCEPTED — FIXED** (→"under these training conditions")
- **F-6C-H2:** "unique attractor" is a formal dynamical systems claim. **ACCEPTED — FIXED** (→"robust attractor")

### MEDIUM (7):
- **F-6C-M1:** "necessary and sufficient" appears 4 times. **NOTED** (already qualified in R2)
- **F-6C-M2:** "emerges identically" when ratios differ 4x between scales. **ACCEPTED — FIXED** (→"consistently")
- **F-6C-M3:** "Initialization is cosmetic" dismissive. **ACCEPTED — FIXED** (→"effects vanish within 200 steps")
- **F-6C-M5:** "rejecting arbitrary patterns" implies agency. **ACCEPTED — FIXED** (→"developing no structure without it")
- **F-6C-M6:** "latent geometric preferences" implies pre-existence. **ACCEPTED — FIXED** (→"receptive to geometric structure")
- **F-6C-M7:** Causal claim for confounded experiment. **ACCEPTED — FIXED** (→"additional evidence that the effect requires")
- **F-6C-M4:** "Discovers" in title. **NOTED — NO ACTION** (defensible; Discussion now cautious)

### LOW (4):
- **F-6C-L1:** "identical" used 3 times for 0.16% delta. **ACCEPTED — FIXED** (→"matching")
- **F-6C-L2:** "exactly 3" for empirical observation. **ACCEPTED — FIXED** (→"effectively 3")
- **F-6C-L4:** "convergence proof" in figure caption. **ACCEPTED — FIXED** (→"convergence evidence")
- **F-6C-L3:** Abstract scope claim. **NOTED** (clear in context)

## Round 6 Summary

| Category | Findings | Fixed | Noted |
|----------|----------|-------|-------|
| Agent 6A | 3 | 2 | 1 |
| Agent 6B | 8 | 5 | 3 |
| Agent 6C | 13 | 10 | 3 |
| **Total** | **24** | **17** | **7** |

**Claims calibration was the highest-value sub-round.** Every "universal," "unique," "identical," "proves," and "natural" was either defended or softened. This is what makes the difference between a paper that reviewers trust and one they don't.
