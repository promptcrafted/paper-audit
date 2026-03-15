# Round 1: Hub Validation — Factual Foundation

> Hub independently confirms or rejects each agent finding against raw data.

## Agent 1C (Paper 1 Math) — VALIDATED

- **24 claims checked, 1 discrepancy (MINOR)**
- F-01-02: Algebraic connectivity range 2.3-2.5x stated in text, but Table 1 shows 2.55x
  - **Hub verdict: ACCEPTED.** The table data is authoritative; the text range should technically be 2.3-2.6x. However, Paper 1 is LOCKED and this is not egregious (abstract's "2.4x" is correct, table has exact values).

## Agent 1D (IP Boundary) — VALIDATED

- **1 CRITICAL finding, 2 informational**
- F-01-01: Paper 2 lists proprietary values as graph edge weights
  - **Hub verdict: ACCEPTED.** Independently verified at P2 lines 652-656. **FIX APPLIED:** Removed specific edge-value triplets, kept divisibility relationships. Both EN and IT versions fixed.
- F-01-02 (IP LOW): Statistical characterization within policy — no action.
- F-01-03 (IP INFO): Methodology phrasing acceptable — no action.

## Agent 1A (Paper 3 Math) — VALIDATED

- **101 claims checked, 12 discrepancies (6 MAJOR, 6 MINOR)**

### MAJOR findings — all independently verified against raw data:

- **F-01-05/06/07 (Stale experimental data):** Hub verified results JSON at step 10000: metric_mean=0.0944, val_loss=0.4024. Paper had 0.085 and 0.4022 from in-progress readings. **ACCEPTED — FIXED.** Table 2 updated. Metric range updated throughout. Strengthens the claim — tighter band.

- **F-01-08 (Per-module ratio):** Hub verified source document line 74: q_proj=22,477:1. Paper had 34,000:1. No source anywhere contains 34,000. **ACCEPTED — FIXED.** Section 6.1 rewritten with correct values.

- **F-01-09 (Misattributed value):** Hub verified inventory: k_proj=46,570:1, v_proj=24,462:1. Paper grouped both at 46,570:1. **ACCEPTED — FIXED.** Now separates k and v values correctly.

- **F-01-10 (Cross-experiment claim):** Hub verified: metric for experiment H = 1.002. Paper claimed "converges to ~0.10 across all three scales" but H is 10x higher. **ACCEPTED — FIXED.** Rewritten to distinguish regimes.

### MINOR findings — disposition:

- **F-01-01 (experiment count):** "15 experiments" vs Table 1 count. **DEFERRED to Round 2** (internal consistency).
- **F-01-02 (convergence band):** 10%→11.2%. **ACCEPTED — FIXED.**
- **F-01-03 (step mixing):** Val loss presented as step 10K; actually step 4K. **ACCEPTED — FIXED.**
- **F-01-04 (rounding):** 0.0918→0.092. **ACCEPTED — no fix needed.** Acceptable 2-sig-fig rounding.
- **F-01-11 (initial conditions):** 0.005/83%→0.006/79%. **ACCEPTED — FIXED.**
- **F-01-12 (unit mixing):** Ambiguous units. **DEFERRED to Round 2** for deeper investigation.

## Agent 1B (Paper 2 Math) — VALIDATED

- **97 claims checked, 6 discrepancies (2 MAJOR, 4 MINOR)**

### MAJOR findings:

- **MAJOR-1 (Unverifiable claim):** Paper claims statistical values with no saved output. Hub re-ran the script — output **matches paper exactly.** **ACCEPTED — VERIFIED.** Output saved for reproducibility.

- **MAJOR-2 (Parameter mismatch):** Code uses n_restarts=100, max_iters=5000. Paper said "20 restarts of 1,000 iterations." **ACCEPTED — FIXED.** Both language versions updated.

### MINOR findings:

- **MINOR-1 (stale count):** Test count 256→312. **DEFERRED to Round 5.**
- **MINOR-2 (rounding):** Off by 1 in last digit. **ACCEPTED — FIXED.**
- **MINOR-3 (hedging):** Adequate with "approximately." **ACCEPTED — no fix needed.**
- **MINOR-4 (omission):** Table omits 2 distributions. **DEFERRED to Round 4.**

## Round 1 Summary

| Metric | P1 (1C) | P2 (1B) | P2 (1D) | P3 (1A) | Total |
|--------|---------|---------|---------|---------|-------|
| Claims checked | 24 | 97 | 3 | 101 | 225 |
| CRITICAL | 0 | 0 | 1 | 0 | 1 |
| MAJOR | 0 | 2 | 0 | 6 | 8 |
| MINOR | 1 | 4 | 0 | 6 | 11 |
| Fixed this round | 0 | 3 | 1 | 8 | 12 |
| Deferred | 0 | 2 | 0 | 2 | 4 |
| No action needed | 1 | 1 | 2 | 2 | 6 |

**No CRITICAL findings remain open.** All MAJOR findings resolved (7 fixed, 1 verified correct). Paper 1 remains LOCKED.
