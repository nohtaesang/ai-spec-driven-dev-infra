# Architecture Guardrails — Framework

This document provides a **generic framework** for defining and enforcing architectural boundaries. Each project defines its own concrete rules using this framework.

## Purpose

Architecture guardrails prevent structural decay by making forbidden dependency patterns explicit and automatically detectable. Without guardrails, module boundaries erode over time as expedient shortcuts accumulate.

## How to Define Guardrails

Each project should create a project-level document (e.g., `ARCHITECTURE_LINT_RULES.md`) that specifies:

### 1. Layer Model

Define the architectural layers and their responsibilities:

```
{{CORE_LAYER}}       Pure domain types. No framework dependencies.
{{DATA_LAYER}}       Data access and persistence. No UI/rendering awareness.
{{APP_LAYER}}        Application logic. Integrates layers.
```

### 2. Forbidden Dependency Table

Enumerate what each layer must NOT depend on:

| Source Layer | Forbidden Dependency | Rationale |
|---|---|---|
| `{{CORE_LAYER}}` | Framework imports (e.g., UI, ORM) | Core stays framework-agnostic |
| `{{DATA_LAYER}}` | Presentation types | Data layer is UI-independent |
| `{{APP_LAYER}}` | Direct filesystem in hot paths | App logic receives prepared data |

### 3. Detection Patterns

For each forbidden dependency, define a grep-able pattern:

```bash
# Example: core must not import framework
grep -rn --include='*.rs' -E 'use framework::' {{CORE_LAYER}}/
```

## Lint Script Framework

A template lint script is provided at `scripts/architecture_lint/lint_template.sh`. Projects should copy and customize it with their specific rules.

The script:
- Accepts a source root path as argument
- Checks each forbidden pattern via grep
- Reports violations with file and line number
- Exits non-zero on any violation

## Why These Boundaries Matter

1. **Testability** — Lower layers can be tested without upper-layer dependencies.
2. **Portability** — Framework-specific layers can be swapped without touching domain logic.
3. **Performance** — Hot paths stay free of I/O and blocking operations.
4. **Clarity** — Each module has a single, well-defined responsibility.

## Automated Enforcement

- `scripts/architecture_lint/lint_template.sh` — customizable lint script
- `/analyze` and `/audit` should check for guardrail violations
- CI/CD should run the lint script as a pre-merge check

## Project-Level Extensions

The following are **project-specific** and should NOT be in this template:

- Concrete crate/module names
- Specific forbidden import patterns
- Performance guardrails tied to a specific runtime (e.g., game loop, render loop)
- Decision memory for project-specific architectural choices
- Benchmark targets and fixture definitions

See `PROJECT_EXTENSIONS.md` for the full list of what belongs in the project repo.
