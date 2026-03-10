# Spec ↔ Code Consistency — Framework

This document defines the **framework** for detecting drift between design documents and implementation code. Each project defines its own concrete type lists and check rules.

## Why Spec/Code Drift Is Dangerous

- **Design discussions reference phantom types** that do not exist in code.
- **AI sessions make incorrect assumptions** based on stale documentation.
- **Refactoring breaks undocumented contracts** because the actual type graph diverges from the documented one.
- **New contributors build on the wrong mental model**, leading to late integration failures.

Spec/code consistency is a structural integrity constraint, not a documentation chore.

## How to Set Up Consistency Checks

### 1. Define the Required Types List

Each project should maintain a list of core types that must exist in the codebase, derived from model and architecture documents:

```
# Example — project-level spec_types.txt
{{DOMAIN_TYPES}}
```

### 2. Define Where to Look

Map types to their expected source locations:

| Type | Expected Location |
|------|-------------------|
| `{{EXAMPLE_TYPE_1}}` | `{{CORE_LAYER}}` |
| `{{EXAMPLE_TYPE_2}}` | `{{DATA_LAYER}}` |

### 3. Run the Checker

A template script is provided at `scripts/spec_consistency_check/check_template.sh`. Projects should copy and customize it with their type list and source paths.

```bash
./scripts/spec_consistency_check/check.sh {{SOURCE_ROOT}}
```

## What the Checker Validates

- **Presence**: Each required type has a `struct`, `enum`, `trait`, `type`, `class`, or `interface` definition in the codebase.
- **Location**: Types appear in the expected module/crate (optional, project-configured).
- **Naming**: Type names match the spec exactly (case-sensitive).

## When to Run

- After completing any design task that introduces or modifies types.
- After completing any implementation task that touches core domain types.
- During `/audit` as part of the full system consistency check.

## Handling Mismatches

| Situation | Action |
|---|---|
| Type in spec but missing from code | Create an implementation task |
| Type in code but missing from spec | Update the relevant design document |
| Type name differs | Align naming — spec is authoritative |
| Type exists but with wrong shape | Reconcile; create ADR if spec needs updating |

## Project-Level Extensions

The following are **project-specific** and must NOT be in this template:
- Concrete type lists (e.g., `MyEntity`, `MyConfig`, `MyEvent`)
- Concrete source paths (e.g., `src/core`, `crates/my_project`)
- Project-specific validation logic
