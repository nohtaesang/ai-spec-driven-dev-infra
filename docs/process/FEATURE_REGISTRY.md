# Feature Registry — Framework

This document provides a **generic framework** for centralized feature, test, and flag tracking. Each project defines its own concrete registry using this framework.

> **This framework is optional.** Adopt it when your project reaches a scale where code alone is no longer sufficient as SSOT for feature state. See [When to Adopt](#when-to-adopt) below.

## When to Adopt

This framework adds value when **reading the code is no longer enough** to answer "what features exist, what state are they in, and are they tested?"

**Adopt when** your project has any of:
- 20+ distinct features across multiple modules
- Feature flags that gate runtime behavior
- Multiple test categories (guard, consistency, balance, etc.) that need per-feature tracking
- Diagnostic/validation binaries that map to specific features

**Skip when** your project has:
- A small number of modules where `cargo test` / `npm test` + linter is sufficient gate
- No feature flags
- Code that one person can read end-to-end in an hour

The cost of adopting later is low — enumerate existing features once and start tracking. There is no benefit to adopting early "just in case."

## Why Feature Drift Is Dangerous

- **Features exist in code but not in any tracking document** — no one knows what is "done" vs. "in progress" vs. "experimental".
- **Tests cover some features but not others** — coverage gaps are invisible until a regression ships.
- **Feature flags drift from their intended state** — a flag meant to be temporary becomes permanent; a disabled flag blocks a dependency.
- **AI sessions assume a feature is complete** when it is only partially implemented, leading to incorrect design decisions.
- **Adding or removing a feature has unknown ripple effects** because dependency chains are not recorded.

Feature drift is a coordination failure, not a documentation chore. A central registry makes the current state of every feature explicit and verifiable.

## What a Feature Registry Tracks

A Feature Registry is a single document (e.g., `FEATURE_REGISTRY.md` in the project repo) that records the following per feature:

| Column | What It Records | Example Placeholder |
|---|---|---|
| Feature ID | Unique, stable identifier | `FEAT-NNN` |
| Name | Short human-readable name | `{{FEATURE_NAME}}` |
| Status | Implementation state | `planned` / `in-progress` / `done` / `deprecated` |
| Flag | Feature flag name (if any) | `{{FLAG_NAME}}` or `none` |
| Flag State | Current toggle state | `on` / `off` / `n/a` |
| Test Coverage | Number of tests or coverage tier | `{{COUNT}}` or `minimal` / `standard` / `comprehensive` |
| Dependencies | Other features this depends on | `FEAT-NNN, FEAT-NNN` or `none` |
| Owner Layer | Which architectural layer owns this | `{{LAYER_NAME}}` |
| CI Included | Whether CI validates this feature | `yes` / `no` / `partial` |

Projects may add or remove columns based on their needs. The above is a starting template.

## How to Set Up a Feature Registry

### 1. Define Feature ID Convention

Choose a prefix and numbering scheme:

```
FEAT-001, FEAT-002, ...
```

IDs are stable — do not renumber. Deprecated features are marked, not removed.

### 2. Define Status Transitions

```
planned → in-progress → done
                      → deprecated
```

Only one transition per task. Status changes must correspond to a task in `TASKS.md`.

### 3. Define Minimum Coverage Rules

Each project should define what "minimum acceptable coverage" means per feature status:

| Status | Minimum Coverage Requirement |
|---|---|
| `planned` | None required |
| `in-progress` | At least basic path coverage |
| `done` | Project-defined minimum (e.g., happy path + primary error paths) |
| `deprecated` | Existing tests retained until removal |

### 4. Define Flag Lifecycle Rules

If the project uses feature flags:

```
Flag created (off) → Flag enabled (on) → Flag removed (feature is permanent)
```

- Flags must have a planned removal date or condition.
- Stale flags (past removal date, still present) are flagged during `/audit`.

## Claude Code Integration

### When Claude Code Updates the Registry

| Event | Registry Action |
|---|---|
| New feature task created | Add row with status `planned` |
| Implementation task starts (`[-]`) | Set status to `in-progress` |
| Implementation task completes (`[x]`) | Set status to `done`, verify coverage minimum |
| Feature flag added/toggled in code | Update Flag and Flag State columns |
| Tests added for a feature | Update Test Coverage column |
| Feature deprecated via ADR | Set status to `deprecated` |

### `/next` Pipeline Integration

Registry verification fits into the existing pipeline:

```
/next pipeline:
  1. Restore context (SPEC.md, TASKS.md, Registry)
  2. Detect/select task
  3. Execute task
  4. Update Registry (if feature-related change)
  5. /analyze (includes Registry gap check)
  6. /audit (includes Registry consistency check)
  7. Mark complete
```

### `/analyze` Checks

During analysis, verify:

- [ ] Every `done` feature meets minimum coverage
- [ ] No `in-progress` features without a corresponding `[-]` task
- [ ] No orphan flags (flag in code but not in Registry)
- [ ] No orphan features (feature in code but not in Registry)

### `/audit` Checks

During audit, additionally verify:

- [ ] All feature IDs are unique and sequential
- [ ] Dependency chains have no cycles
- [ ] Stale flags identified (past planned removal)
- [ ] CI coverage matches CI Included column
- [ ] No `planned` features with tests but no task (indicates untracked work)

## Registry Document Template

Projects should create their registry using this structure:

```markdown
# Feature Registry

**Source of truth for feature status, test coverage, and flag state.**

Last updated: {{DATE}}

## Active Features

| ID | Name | Status | Flag | Flag State | Tests | Depends | Layer | CI |
|----|------|--------|------|------------|-------|---------|-------|----|
| FEAT-001 | {{NAME}} | {{STATUS}} | {{FLAG}} | {{STATE}} | {{COUNT}} | {{DEPS}} | {{LAYER}} | {{CI}} |

## Deprecated Features

| ID | Name | Deprecated Date | ADR | Removal Target |
|----|------|-----------------|-----|----------------|
| FEAT-NNN | {{NAME}} | {{DATE}} | ADR-NNN | {{TARGET_DATE}} |

## Coverage Rules

| Status | Minimum |
|--------|---------|
| planned | — |
| in-progress | {{PROJECT_MINIMUM}} |
| done | {{PROJECT_MINIMUM}} |

## Flag Lifecycle

| Flag | Feature | Created | Planned Removal | Current State |
|------|---------|---------|-----------------|---------------|
| {{FLAG_NAME}} | FEAT-NNN | {{DATE}} | {{DATE}} | on/off |
```

## Relationship to Other Documents

| Document | Relationship |
|---|---|
| `TASKS.md` | Tasks drive status transitions. A feature status change requires a corresponding task. |
| `SPEC.md` | Features must not violate SPEC constraints. Registry does not override SPEC. |
| `DEFINITIONS.md` | Feature names that are domain terms must be registered in DEFINITIONS.md. |
| `SPEC_CODE_CONSISTENCY.md` | Registry tracks feature-level state; Spec/Code Consistency tracks type-level state. Complementary, not overlapping. |
| `ARCHITECTURE_GUARDRAILS.md` | Owner Layer column must align with defined architectural layers. |
| `DECISIONS.md` | Feature deprecation requires an ADR. |

## Project-Level Extensions

The following are **project-specific** and should NOT be in this template:

- Concrete feature names and IDs
- Concrete flag names and values
- Concrete test count numbers or G:C:B ratios
- Project-specific CI pipeline names or scripts
- Project-specific coverage thresholds
- Concrete layer/module names

See `PROJECT_EXTENSIONS.md` for the full list of what belongs in the project repo.
