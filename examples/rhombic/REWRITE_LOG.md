# Rewrite Log — RhombiLoRA Audit

> Every change linked to the finding that prompted it.

## Round 1 (12 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| F-01-01 | P2 | Removed specific edge values, kept divisibility relationships | IP boundary violation — proprietary values exposed |
| F-01-01 | P2-IT | Same fix in Italian version | Mirror fix |
| F-01-03/04 | P3 | Table 2 updated: stale metric and loss values | In-progress readings replaced with final values |
| F-01-05 | P3 | Metric range updated at 3 locations | Cascading from stale data correction |
| F-01-06/07 | P3 | Section 6.1 per-module ratios rewritten | Wrong value (34K→22K); misattributed grouping |
| F-01-08 | P3 | Correlation metric section rewritten | Claim incorrect for one experiment regime |
| F-01-09 | P3 | Convergence band delta 10%→11% | Arithmetic: (71337-64168)/64168=11.2% |
| F-01-10 | P3 | Val loss now states correct step count | Was presenting 4K result as 10K |
| F-01-12 | P3 | Initial conditions corrected | Source table disagrees with paper |
| F-01-16 | P2+IT | SA parameters updated both versions | Code uses 100/5000, paper said 20/1000 |
| F-01-18 | P2 | Spectral gap last digit corrected | 0.0314→0.0313 per computation |

## Round 2 (26 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| F-2B-01 | P2 bib | Paper 3 subtitle corrected | Wrong title in bibliography |
| F-2B-02 | P3 | Phantom citation replaced with self-references | Paper 2 doesn't contain cited content |
| F-2B-12 | P3 | Foundational citation added | Fiedler (1973) used but uncited |
| F-2A-01 | P3 | "15 experiments" → "13 experiments" (2 locations) | Table has 13 rows |
| F-2A-02 | P3 | Table value corrected to match raw data | Table said 1%, raw data = 0% |
| F-2A-04/05 | P3 | Key metric updated (3 locations) | Stale 40-checkpoint figure |
| F-02C-01 | P3 | "necessary and sufficient" → "at n=6" (4 locations) | Confound acknowledged |
| F-02C-02 | P3 | "universal" → "robust" (3 locations) | 6 experiments / 2 scales insufficient |
| F-02C-06 | P3 | "scale-invariant" → "scale-consistent" (3 locations) | N=2 cybernetic scales |
| F-02C-13 | P3 | IC/RD ratio corrected (1.4:1 not 2.9:1) | Mixed-unit error |
| ... | P3 | 15 additional minor language calibrations | Various claim-evidence alignment |

## Round 3 (7 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| T-001 | P3 | Symbol unified (`\mathcal{B}` → `\mathbf{M}`) | Inconsistent within paper |
| F-3A-03 | P3 | Paper 2 citation added to §2.4 | Narrative chain was broken |
| F-3A-11 | P3 | "Prior work" → "Preliminary experiments" | Self-reference, not separate publication |
| F-3A-02 | P2 | Scale annotations added to comparison table | Comparing different scales without noting it |
| F-3A-05 | P2 | Test count 256→312 (2 locations) | Stale count |

## Round 4 (9 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| F-4A-01 | P3 | 5 figure references added | Unreferenced figures |
| F-4A-03 | P3 | Figure caption scope clarified | Caption metric didn't match text scope |
| 4B-01/02/03 | P3 | Key experiment fully specified in appendix | Optimizer, data, target modules all missing |
| 4B-04/05/06 | P3 | Controller parameters added to appendix table | 5 gain constants, decay dynamics, update rules |
| 4B-12 | P3 | Train/val split specified | "alpaca-cleaned (90/10 train/val split)" |
| F-4C-07 | P2 | Table footnotes added | Silent omission of 2 distributions |

## Round 5 (11 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| 5A-10-1 | P3 | "robust" reduced from 5 to 2 occurrences | AI tic pattern |
| 5A-10-2 | P3 | "the fact that" removed (2 locations) | Filler phrase |
| 5A-10-3 | P3 | Assertive absolutes softened | "unambiguous" → "consistent" |
| P3-TR-01 | P3 | Transition paragraph added before Results | Missing Method→Results bridge |
| P3-JD-03 | P3 | Reminder glosses added for technical terms | Jargon without definition |
| L-01 | P3 | Single-seed limitation added | Unacknowledged |
| L-04 | P3 | Ablation-scale limitation added | Unacknowledged |
| L-08 | P3 | Controller sensitivity limitation added | Unacknowledged |
| L-02 | P3 | Scale range limitation expanded | Partially acknowledged |

## Round 6 (17 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| F-6B-01/02 | P3 | Two comparison methods restored to Related Work | Lost during consolidation |
| F-6B-05 | P3 | Foundational cybernetics citation added | Beer (1972) uncited |
| F-6A-01 | P3 bib | 6 orphan entries removed | 39% orphan rate |
| F-6A-02 | P2 bib | 4 orphan entries removed | Unused citations |
| F-6C-H1/H2 | P3 | 2 overclaims fixed ("natural"→"under conditions", "unique"→"robust") | Formal claims unsupported |
| F-6C-M2-M7 | P3 | 6 medium overclaims calibrated | Language exceeded evidence |
| F-6C-L1/L2/L4 | P3 | 3 low-level language calibrations | "identical"→"matching", "exactly"→"effectively", "proof"→"evidence" |

## Round 7 (5 changes)

| Finding | Paper | Change | Justification |
|---------|-------|--------|---------------|
| F-7A-01 | P3 | Geometric description corrected | "Perpendicular to axis" → "grouped by vanishing coordinate" |
| F-7A-02 | P3 | Ordering claim weakened | k > v → k >= v (tied at one scale) |
| F-7A-13 | P3 | Word redundancy fixed in abstract | "effective...effectively" |
| F-7C-01 | P2 | Overfull hbox fixed | sloppypar wrapper |
| F-7C-02 | P3 | Overfull hbox fixed | sloppypar wrapper |
