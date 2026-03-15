# paper-audit

> *Seven rounds. Zero critical findings remaining.*

A structured adversarial audit framework for research papers. Uses specialized AI agents in seven escalating rounds to find errors, inconsistencies, and overclaims before reviewers do.

**Battle-tested:** Developed during the audit of three research papers (232 findings across 7 rounds, 87 fixed, 0 CRITICAL or MAJOR remaining). Both papers shipped submission-ready.

## Why This Exists

Most ML papers go to reviewers with numbers nobody double-checked, abstracts that don't match the body, and claims that outrun the evidence. Peer review catches some of this. A structured adversarial process catches more — and catches it before submission.

This framework runs seven rounds of increasingly focused scrutiny, each with specialized agents that look for different classes of error. Early rounds verify numbers. Later rounds check coherence, prose quality, and calibration of claims. A human hub validates every finding against raw data before accepting it.

## The Seven Rounds

| Round | Focus | Agents | Severity Threshold |
|-------|-------|--------|--------------------|
| 1 | **Factual Foundation** | Math accuracy (per paper), IP boundary | CRITICAL |
| 2 | **Internal Consistency** | Abstract↔body, cross-refs, claim↔evidence | CRITICAL + MAJOR |
| 3 | **Cross-Paper Coherence** | Narrative arc, terminology, forward/backward refs | CRITICAL + MAJOR |
| 4 | **Figures + Reproducibility** | Figure↔text, reproducibility, missing visuals | MAJOR + MINOR |
| 5 | **Writing Quality** | AI tic detection, prose quality, limitations honesty | MINOR + POLISH |
| 6 | **Bibliography + Claims** | Citation completeness, related work gaps, claims calibration | MAJOR + MINOR |
| 7 | **Final Integration** | Fresh read-through, cross-paper final, submission checklist | CRITICAL only |

Early rounds fix what's wrong. Late rounds fix what's imprecise.

## Quick Start

### 1. Copy the templates

```bash
git clone https://github.com/promptcrafted/paper-audit.git
cp -r paper-audit/templates/ your-paper/audit/
```

### 2. Set up the agent definitions

Copy `.claude/agents/` into your project's `.claude/agents/` directory. These are [Claude Code](https://claude.ai/claude-code) agent definitions that can be spawned as sub-agents during the audit.

### 3. Run round by round

Each round follows the same pattern:

1. **Dispatch** — Launch 3-4 specialized agents in parallel
2. **Validate** — Hub reads raw data to confirm/reject each finding
3. **Fix** — Incorporate validated findings
4. **Track** — Update FINDINGS_TRACKER.md and REWRITE_LOG.md

See [docs/METHODOLOGY.md](docs/METHODOLOGY.md) for the complete protocol.

## Finding Format

Every finding follows a structured format for traceability:

```markdown
### F-RR-NN: [Title]
- Agent severity: CRITICAL / MAJOR / MINOR / POLISH
- Location: Paper X, Section Y, Line Z
- Finding: [What is wrong]
- Evidence: [Raw data file + correct value]
- Hub verdict: ACCEPTED — FIXED / ACCEPTED — NOTED / REJECTED
- Fix: [What was changed]
```

Severity definitions:

| Level | Meaning | Action |
|-------|---------|--------|
| **CRITICAL** | Factually wrong numbers, IP exposure, broken references | Must fix before any further work |
| **MAJOR** | Claims unsupported by evidence, inconsistencies between sections | Must fix before submission |
| **MINOR** | Imprecise language, rounding differences, missing context | Fix if straightforward |
| **POLISH** | Stylistic improvements, redundant phrasing | Fix at author's discretion |

## File Structure

```
your-paper/audit/
├── FINDINGS_TRACKER.md          # Running log across all rounds
├── REWRITE_LOG.md               # What changed and why
├── round-1/
│   ├── agent-1A-math-p3.md      # Agent findings
│   ├── agent-1B-math-p2.md
│   ├── agent-1C-math-p1.md
│   ├── agent-1D-ip-boundary.md
│   └── hub-validation.md        # Hub confirmation/rejection
├── round-2/
│   └── ...
└── round-7/
    └── hub-validation.md
```

## Agent Architecture

Each round dispatches 3-4 specialized agents. Agents are adversarial — their job is to find problems, not to praise the paper. The hub is the judge — it validates findings against raw data and accepts or rejects each one.

**Agents cannot modify files.** They report findings. The hub decides what to act on. This separation prevents agents from "fixing" things by introducing new errors.

**Agents run in parallel within a round.** Rounds run sequentially. Each round's fixes are in place before the next round begins.

See [.claude/agents/](.claude/agents/) for the full set of agent definitions.

## Adapting to Your Paper

The framework is designed for multi-paper research projects but works for single papers too:

- **Single paper:** Skip Round 3 (cross-paper coherence). Agents 1A and 7A handle the single paper.
- **No figures:** Skip Round 4 agents 4A and 4C. Keep 4B (reproducibility).
- **No code:** Skip IP boundary agent (1D). Keep everything else.
- **Non-ML papers:** The methodology generalizes. Swap "hyperparameters" for your domain's equivalent in the reproducibility check.

## Results From the Field

The framework was developed and validated on three lattice topology papers:

| Metric | Value |
|--------|-------|
| Total findings | 232 |
| Findings fixed | 87 |
| CRITICAL findings at Round 1 | 4 |
| CRITICAL findings remaining | **0** |
| MAJOR findings remaining | **0** |
| Rounds | 7 |
| Agents deployed | ~25 |
| Papers audited | 3 (simultaneously) |

See [examples/rhombic/](examples/rhombic/) for the complete audit trail.

## Philosophy

- **Numbers first.** Verify every number against raw data before anything else.
- **The hub decides.** Agent findings are proposals, not verdicts.
- **Severity escalation.** Don't polish prose while numbers are wrong.
- **Sparse findings are data.** A round with zero findings means the paper is clean at that level, not that the agents failed.
- **Fix, don't defend.** When a finding is valid, fix it. Don't argue with your own audit.

## License

[MPL-2.0](LICENSE) — Use freely. Modifications to framework files shared back to the commons.

## Built by [Promptcrafted](https://promptcrafted.com)

Developed as part of the [rhombic](https://github.com/promptcrafted/rhombic) research program.
*The scrutiny is the argument. The findings are the evidence.*
