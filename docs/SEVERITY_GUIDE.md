# Severity Classification Guide

## Levels

### CRITICAL

**Definition:** The finding, if uncorrected, would cause a reviewer to reject the paper or a reader to reach incorrect conclusions.

**Examples:**
- A headline number is wrong (e.g., "6.1x" when the data shows 3.2x)
- Proprietary data is exposed in a table or figure
- A citation points to the wrong paper
- A key equation has an error
- Broken cross-references produce "??" in compiled output

**Action:** Must fix immediately. Block all other work until resolved.

### MAJOR

**Definition:** A significant error or unsupported claim that undermines the paper's argument, but the paper's core contribution survives.

**Examples:**
- An abstract claim is unsupported by the body text
- A "universal" claim is made from 2 data points
- A figure caption describes something different from what the figure shows
- In-progress data is presented as final results
- A confound is not acknowledged in the limitations

**Action:** Must fix before submission. These are the findings that reviewers will catch.

### MINOR

**Definition:** An imprecision, inconsistency, or gap that doesn't threaten the paper's argument but reduces its quality.

**Examples:**
- A percentage is rounded inconsistently (31% in one place, 31.6% in another)
- A term is used before it is defined
- A limitation is acknowledged but could be stated more precisely
- Test count is outdated (256 vs actual 312)

**Action:** Fix if straightforward. Note if the fix would require significant restructuring.

### POLISH

**Definition:** A stylistic improvement that would make the paper read better but has no impact on correctness or argumentation.

**Examples:**
- Redundant phrasing ("effective dimensionality... effectively 3")
- A paragraph transition could be smoother
- An orphan bib entry that isn't cited but does no harm
- Minor formatting inconsistencies

**Action:** Fix at the author's discretion. These are nice-to-haves.

## Decision Tree

```
Is the finding factually wrong?
├── Yes → Does it change the paper's conclusions?
│   ├── Yes → CRITICAL
│   └── No → MAJOR
└── No → Is it an unsupported or overstated claim?
    ├── Yes → Would a reviewer flag it?
    │   ├── Yes → MAJOR
    │   └── No → MINOR
    └── No → Does it affect readability or precision?
        ├── Yes → MINOR
        └── No → POLISH
```

## Common Severity Mistakes

**Over-severity:** Marking a rounding difference as CRITICAL. If the paper says "~30%" and the data shows 31.6%, that's adequate hedging, not an error. MINOR at most.

**Under-severity:** Marking a wrong number as MINOR because the correct number is close. If the paper says 34,000:1 but the data shows 22,477:1, that's MAJOR — the difference is 50%.

**Conflating importance with severity:** A finding about the paper's most important result is not automatically CRITICAL. Severity measures the degree of error, not the importance of the section.
