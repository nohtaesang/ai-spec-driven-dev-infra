# AI Session Bootstrap — Template

Quick-start context template for new AI sessions. Each project should customize this file during bootstrap.

---

## Project Identity

- **Project name**: {{PROJECT_NAME}}
- **One-line description**: {{PROJECT_DESCRIPTION}}
- **Product type**: {{PRODUCT_TYPE}}

## Architecture Overview

{{ARCHITECTURE_SUMMARY}}

## Module / Crate Structure

```
{{MODULE_STRUCTURE}}
```

## Key Guardrails

1. **SPEC.md is supreme.** No document or code may contradict it. Violations halt work.
2. **Architecture boundaries are enforced.** See `docs/process/ARCHITECTURE_GUARDRAILS.md` for the framework and project-level `ARCHITECTURE_LINT_RULES.md` for concrete rules.
3. **Performance guardrails are non-negotiable.** See project-level performance guardrails document.
4. **Domain terms must be registered.** Every domain term in design documents must exist in `docs/core/DEFINITIONS.md`.
5. **One task at a time.** See `docs/project/TASKS.md` for the current phase and active task.
6. **Config policy.** No magic numbers. Tunables in config. See `docs/process/CONFIG_CONSTANTS_POLICY.md`.

## Current Phase

Check `docs/project/TASKS.md` for the active phase and task. The project progresses through:

- **Phase 0**: Project setup (SPEC, DEFINITIONS, VISION, PRINCIPLES, ASSUMPTIONS, NON_GOALS)
- **Phase 1**: Core design documents (models, architecture, UX)
- **Phase 2+**: Implementation (defined per project)

## Forbidden Shortcuts

- Do not skip `/next` — it runs analysis and audit automatically.
- Do not modify SPEC.md without an ADR.
- Do not introduce domain terms without adding them to DEFINITIONS.md.
- Do not skip dependencies in TASKS.md.
- Do not bypass architecture lint rules.
- Do not hardcode tunable values — use config.

{{PROJECT_SPECIFIC_FORBIDDEN_SHORTCUTS}}

## Key References

| Document | Purpose |
|---|---|
| `CLAUDE.md` | Project rules for Claude Code sessions |
| `docs/core/SPEC.md` | Non-negotiable constraints |
| `docs/core/DEFINITIONS.md` | Canonical glossary |
| `docs/process/DEFINITION_OF_DONE.md` | Task completion checklist |
| `docs/process/CHANGE_IMPACT_CHECKLIST.md` | Change review checklist |
| `docs/process/ARCHITECTURE_GUARDRAILS.md` | Architecture guardrail framework |
| `docs/project/TASKS.md` | Current phase and task tracking |
| `docs/project/DECISIONS.md` | ADR index |

{{PROJECT_SPECIFIC_REFERENCES}}

---

> **Note**: Replace all `{{PLACEHOLDER}}` values during project bootstrap. This template is maintained in the infrastructure repo and should not contain project-specific content.
