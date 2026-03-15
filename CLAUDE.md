# Paper Audit — 7-Round Adversarial Framework

You are operating inside the **paper-audit** framework — an open-source,
agent-driven methodology for adversarial quality assurance of academic papers.

## Architecture

Seven sequential rounds, each with specialized agents dispatched in parallel,
followed by hub validation against raw data:

| Round | Focus | Agents |
|-------|-------|--------|
| 1 | Factual Foundation | math-accuracy, ip-boundary |
| 2 | Internal Consistency | abstract-body, cross-refs, claim-evidence |
| 3 | Cross-Paper Coherence | narrative-arc + custom terminology/cross-ref agents |
| 4 | Figures + Reproducibility | figure-text, reproducibility |
| 5 | Writing Quality | ai-tic-detector + custom prose/limitations agents |
| 6 | Bibliography + Claims | claims-calibration + custom citation agents |
| 7 | Final Integration | submission-checklist + custom read-through agents |

## Key Principles

1. **Agents find, the hub decides.** Agents report findings with severity
   ratings. The hub validates each finding against raw data before accepting.
   Agent severity is advisory — the hub may upgrade or downgrade.

2. **Every finding gets a verdict.** ACCEPTED — FIXED, ACCEPTED — NOTED, or
   REJECTED. No finding goes undispositioned.

3. **Escalation schedule.** Early rounds fix CRITICAL errors. Later rounds
   address polish. Round 7 only acts on CRITICAL/MAJOR.

4. **Rewrite log tracks provenance.** Every change links to the finding that
   prompted it. No undocumented edits during an audit.

## Severity Levels

- **CRITICAL** — Wrong numbers, broken references, missing figures, IP violations
- **MAJOR** — Unsupported claims, inconsistent terminology, reproducibility gaps
- **MINOR** — Style issues, weak transitions, minor formatting
- **POLISH** — Typos, spacing, cosmetic preferences

See `docs/SEVERITY_GUIDE.md` for the full decision tree.

## File Structure

```
.claude/agents/     # Agent definitions (YAML frontmatter + instructions)
docs/               # METHODOLOGY.md, SEVERITY_GUIDE.md
templates/          # FINDINGS_TRACKER.md, REWRITE_LOG.md, hub-validation.md
examples/           # Sanitized real-world audit trails
```

## Usage

1. Copy `templates/` into your paper repo as `audit/`
2. Copy `.claude/agents/` into your project's `.claude/agents/`
3. Run Round 1 agents against your paper
4. Fill in `hub-validation.md` for each round
5. Update `FINDINGS_TRACKER.md` and `REWRITE_LOG.md` as you go
6. Repeat through Round 7

## Adapting Agents

Agent definitions are markdown files with YAML frontmatter. Customize:
- `model:` field (opus for deep analysis, sonnet for pattern matching)
- Detection patterns and red flags for your domain
- Output format to match your tracking preferences

The framework is domain-agnostic. The agents shipped here are tuned for
ML/AI papers but the methodology applies to any technical writing.
