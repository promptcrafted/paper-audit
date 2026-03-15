# Example: RhombiLoRA Paper Audit

This is a sanitized version of a real 7-round adversarial audit conducted on
a three-paper ML research series about lattice topology in neural network
weight spaces.

**Papers audited:**
- Paper 1: Graph theory benchmarks (LOCKED — read-only audit)
- Paper 2: Weighted topology extensions
- Paper 3: Learnable bridge architecture with cybernetic feedback

**Results:** 232 findings across 7 rounds. 87 fixed, zero CRITICAL or MAJOR
findings remaining at completion. Both Papers 2 and 3 declared submission-ready.

## What to look for

1. **Round 1** shows the factual foundation — catching stale experimental data,
   IP boundary violations, and wrong numbers early.
2. **Round 2** demonstrates how abstract-body mismatches and overclaims are
   systematically identified.
3. **Round 3** shows cross-paper coherence checking — broken citation chains,
   terminology drift, stale cross-references.
4. **Rounds 4-6** progressively tighten figures, reproducibility, writing, and
   claims calibration.
5. **Round 7** is the final integration pass — only CRITICAL/MAJOR findings
   acted on.

## Key patterns demonstrated

- **Hub validation against raw data** — agents find issues, hub confirms by
  reading the actual experiment files
- **Deferred findings** — items punted to later rounds where they're more
  appropriate (e.g., experiment counts deferred from R1 to R2)
- **Cascading fixes** — one correction in R1 (stale Fiedler value) triggers
  updates in 3 other locations
- **IP boundary enforcement** — Round 1 caught proprietary values exposed in
  a graph construction example
- **Claims calibration** — "universal" downgraded to "robust" when evidence
  base is 6 experiments at 2 scales
