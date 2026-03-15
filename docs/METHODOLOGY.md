# Adversarial Audit Methodology

## Overview

The seven-round adversarial audit is a structured process for finding and fixing errors in research papers before submission. Each round targets a specific class of error with specialized agents. A human hub validates findings against raw data.

The process is designed to be **exhaustive at each level before moving to the next.** Round 1 fixes numbers. Round 2 fixes consistency. You don't fix prose (Round 5) while numbers are still wrong (Round 1).

## Prerequisites

Before starting the audit, you need:

1. **Complete draft(s)** — The paper must be written. The audit does not help with incomplete work.
2. **Raw data access** — Every number in the paper must be traceable to a data file, experiment log, or computation. If you can't verify a number, the audit will flag it.
3. **Clear paper boundaries** — If auditing multiple papers, define which papers can be modified and which are locked (e.g., already published).

## The Hub Pattern

Every round follows the same three-phase pattern:

### Phase 1: Dispatch

Launch 3-4 specialized agents in parallel. Each agent:
- Reads the paper(s) with adversarial intent
- Looks specifically for the error class assigned to its role
- Produces a structured findings report with severity, location, and evidence

Agents do NOT modify files. They report.

### Phase 2: Validate

The hub (human or orchestrator) reads each finding and:
- Checks the claimed error against the raw data source
- Assigns a verdict: ACCEPTED, REJECTED, or NOTED
- For ACCEPTED findings: determines the fix
- For REJECTED findings: documents why the agent was wrong

This step is critical. Agents produce false positives. The hub catches them.

### Phase 3: Fix + Track

- Apply fixes to the paper(s)
- Log each fix in REWRITE_LOG.md with the finding ID and justification
- Update FINDINGS_TRACKER.md with the finding's final status
- Recompile and verify clean build

## Round-by-Round Protocol

### Round 1: Factual Foundation

**Goal:** Every number in the paper is correct.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 1A: Math Accuracy (Paper N) | All numbers | Values, percentages, ratios, statistical claims against raw data |
| 1B: Math Accuracy (Paper N+1) | All numbers | Same as 1A for each additional paper |
| 1C: IP Boundary | All papers | No proprietary data, credentials, or restricted values in text/tables/figures |

**Key principle:** A number verified against the wrong source is still wrong. Check the canonical data file, not a summary or intermediate result.

**Rewrite scope:** Fix all CRITICAL number errors. Report-only for locked papers.

### Round 2: Internal Consistency

**Goal:** The paper doesn't contradict itself.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 2A: Abstract-Body | Each paper | Every abstract claim traced to a specific body section |
| 2B: Cross-Refs + Citations | Each paper | All `\cite{}`, `\ref{}`, bib entries resolve; no orphans, no phantoms |
| 2C: Claim-Evidence | Each paper | Every causal/quantitative claim maps to a specific experiment or dataset |

**Common findings:** Abstract says "15 experiments" but the body lists 13. A claim cites the wrong paper for its evidence. A percentage in the introduction doesn't match the same percentage in Results.

**Rewrite scope:** Fix cross-refs, add missing citations, adjust unsupported claims.

### Round 3: Cross-Paper Coherence

**Goal:** Multiple papers tell a consistent story.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 3A: Narrative Arc | All papers | Later papers correctly summarize earlier ones; story builds logically |
| 3B: Terminology | All papers | Consistent notation, definitions, variable names |
| 3C: Forward/Backward Refs | All papers | "Future work" items are addressed; cross-paper citations are accurate |

**Skip this round for single-paper projects.**

**Rewrite scope:** Align terminology, fix cross-paper inconsistencies. Do not modify locked papers unless the error is egregious.

### Round 4: Figures + Reproducibility

**Goal:** A reader could replicate the work.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 4A: Figure-Text | Each paper | Captions match figure content; numbers in text match numbers in figures |
| 4B: Reproducibility | Each paper | All hyperparameters reported; algorithms fully specified; hardware described |
| 4C: Missing Figures | Each paper | Are there claims that would benefit from visual evidence? |

**Rewrite scope:** Fix caption errors, add reproducibility details, flag missing figures.

### Round 5: Writing Quality

**Goal:** Clean academic prose. No AI verbal tics.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 5A: AI Tic Detector | Each paper | "Remarkably," "it is worth noting," "moreover," "furthermore," etc. |
| 5B: Prose Quality | Each paper | Transitions, sentence variation, jargon density, redundancy |
| 5C: Limitations Honesty | Each paper | All real limitations acknowledged; no overclaiming |

**AI tic patterns to detect:**
- "Something remarkable/extraordinary/significant happens"
- "It is worth noting that..."
- "Moreover" / "Furthermore" (academic filler)
- "This suggests that..." (when you know what it means — just say it)
- "One might argue..." (don't argue; present)

**Rewrite scope:** Remove AI tics, strengthen transitions, add missing limitations.

### Round 6: Bibliography + Claims Calibration

**Goal:** Citations are complete. Claims are properly calibrated.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 6A: Citation Completeness | Each paper | Every prior-work claim cited; no phantom citations |
| 6B: Related Work Gaps | Each paper | Recent publications in the field that should be acknowledged |
| 6C: Claims Calibration | Each paper | "Universal" with 2 data points? "Necessary and sufficient" with confounds? |

**Key principle:** Overclaiming is the #1 reviewer complaint. "Robust" is almost always better than "universal." "Consistent with" is almost always better than "proves."

**Rewrite scope:** Add missing citations, soften overclaims, defend where evidence supports.

### Round 7: Final Integration

**Goal:** Fresh eyes. Submission checklist.

| Agent | Scope | What to Check |
|-------|-------|---------------|
| 7A: Full Read-Through | Each paper (newest first) | Read as a reviewer — catch anything remaining |
| 7B: Cross-Paper Final | All papers | Last coherence check |
| 7C: Submission Checklist | All papers | Clean compile, no TODOs, word limits, code availability, author info |

**Rewrite scope:** Only CRITICAL or MAJOR findings acted on. The paper is declared complete after this round.

## Escalation Schedule

| Round | Primary Focus | Severity Threshold | Typical Fix Rate |
|-------|--------------|-------------------|-----------------|
| 1 | Numbers / IP | CRITICAL | 60-80% of findings fixed |
| 2 | Internal consistency | CRITICAL + MAJOR | 50-70% |
| 3 | Cross-paper coherence | CRITICAL + MAJOR | 30-50% |
| 4 | Figures / Reproducibility | MAJOR + MINOR | 40-60% |
| 5 | Writing quality | MINOR + POLISH | 30-50% |
| 6 | Bibliography / Claims | MAJOR + MINOR | 40-60% |
| 7 | Final integration | CRITICAL only | 10-20% |

Fix rates decrease as the paper improves. Round 7 should find very little.

## Practical Tips

**Time budget:** A full 7-round audit of a single paper takes 2-4 hours of human time (launching agents, validating findings, applying fixes). Agent execution runs in parallel.

**When to stop:** If Round 7 produces zero CRITICAL or MAJOR findings, the paper is submission-ready. MINOR and POLISH findings are at the author's discretion.

**Locked papers:** If a paper is already published, audit it in report-only mode. Flag findings for errata consideration. Do not modify the published text.

**Multiple papers:** Run Round 1 agents on all papers simultaneously. This catches cross-paper number inconsistencies early.

**Version control:** Commit between rounds. If a fix introduces a new problem, you can revert to the pre-round state.
