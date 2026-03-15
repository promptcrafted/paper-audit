# Findings Tracker — RhombiLoRA Audit

> 232 findings across 7 rounds. 87 fixed, 74 noted, 20 deferred, 0 rejected.

## Summary

| Round | Focus | Findings | Fixed | Noted | Deferred |
|-------|-------|----------|-------|-------|----------|
| 1 | Factual Foundation | 20 | 12 | 6 | 4 |
| 2 | Internal Consistency | 43 | 26 | 7 | 1 |
| 3 | Cross-Paper Coherence | 47 | 7 | 6 | 0 |
| 4 | Figures + Reproducibility | 34 | 9 | 12 | 12 |
| 5 | Writing Quality | 42 | 11 | 19 | 3 |
| 6 | Bibliography + Claims | 24 | 17 | 7 | 0 |
| 7 | Final Integration | 22 | 5 | 17 | 0 |
| **Total** | | **232** | **87** | **74** | **20** |

## Severity Distribution

| Severity | Count | Fixed | Rate |
|----------|-------|-------|------|
| CRITICAL | 3 | 3 | 100% |
| MAJOR | 23 | 22 | 96% |
| MINOR/MODERATE | 98 | 47 | 48% |
| LOW/POLISH | 60 | 10 | 17% |
| PASS/INFO | 48 | — | — |

## Key Patterns

1. **Stale data was the #1 MAJOR source.** Six MAJOR findings in Round 1 traced to
   in-progress experimental readings that were never updated after experiments completed.
   Lesson: always verify numbers against final result files, not intermediate logs.

2. **Claims calibration had the highest fix rate.** Round 6 fixed 17/24 findings (71%).
   Overclaims are easy to fix once identified — the evidence hasn't changed, only the language.

3. **Cross-paper coherence had the most findings but fewest fixes.** 47 findings, 7 fixed.
   Most were PASS confirmations that the papers tell a consistent story. The few fixes
   (broken citation chain, stale test counts) were high-impact.

4. **IP boundary check caught 1 CRITICAL.** Proprietary values were exposed in a graph
   construction example. Caught in Round 1, before any public distribution.

5. **Zero rejected findings.** Every agent finding was either accepted (fixed or noted)
   or resolved by a later round's fix. This suggests the agents were well-calibrated —
   they flagged real issues, not noise.
