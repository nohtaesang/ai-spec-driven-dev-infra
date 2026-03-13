# Project-Level Extensions

This document defines the boundary between **template-level infrastructure** (this repo) and **project-specific content** (each project repo). Understanding this boundary prevents template pollution and keeps the infrastructure reusable.

## What Stays in the Template

These are generic, reusable across all projects:

| Item | Location | Purpose |
|---|---|---|
| CLAUDE.md | Root | AI session rules |
| Core rules & workflow | `CLAUDE.md`, `.claude/commands/` | `/next` pipeline and governance |
| Foundation doc templates | `docs/core/` | SPEC, DEFINITIONS, VISION, etc. |
| AI governance docs | `docs/ai/` | DOCUMENT_SYSTEM, CHANGE_PROTOCOL, BOOTSTRAP |
| Project tracking structure | `docs/project/` | TASKS, DONE, DECISIONS |
| Definition of Done | `docs/process/` | Generic task completion checklist |
| Change Impact Checklist | `docs/process/` | Generic change review checklist |
| Repository Conventions | `docs/process/` | File and module placement rules |
| Config & Constants Policy | `docs/process/` | Magic numbers and config rules |
| AI Session Bootstrap template | `docs/process/` | Template with placeholders |
| Architecture Guardrails framework | `docs/process/` | How to define guardrails |
| Spec/Code Consistency framework | `docs/process/` | How to set up consistency checks |
| Feature Registry framework | `docs/process/` | How to set up feature/test/flag tracking |
| Lint script template | `scripts/architecture_lint/` | Customizable lint skeleton |
| Consistency check template | `scripts/spec_consistency_check/` | Customizable check skeleton |
| Prompt templates | `prompts/` | Reusable AI prompt patterns |

## What Belongs in Each Project Repo

These are project-specific and must NOT be added to this template:

| Item | Example | Why Project-Specific |
|---|---|---|
| Performance guardrails | Render loop rules, latency budgets | Tied to specific runtime/framework |
| Decision memory | "Why we chose X over Y" | Project-specific reasoning |
| Concrete architecture lint rules | `core must not import framework_x` | Tied to project module names |
| Concrete spec/code type lists | `MyType, MyEntity, MyConfig` | Tied to project domain model |
| Dataset fixtures | `datasets/test/minimal/` | Tied to project data formats |
| Benchmark suites | `benchmarks/feature_x_latency` | Tied to project performance targets |
| Concrete Feature Registry | `FEATURE_REGISTRY.md` with real features | Tied to project feature set |
| Concrete AI session bootstrap | Filled-in architecture summary | Tied to project architecture |
| Filled-in foundation docs | SPEC.md with real constraints | Tied to project scope |

## How Projects Should Extend

When a project is created from this template:

1. **Fill in foundation docs** during bootstrap (`/next` handles this).
2. **Copy and customize** the lint and consistency check templates with project-specific rules.
3. **Create project-level docs** for performance guardrails, decision memory, and concrete architecture rules.
4. **Fill in AI_SESSION_BOOTSTRAP.md** placeholders with project architecture details.
5. **Add project-level directories** as needed (datasets, benchmarks, fixtures).

## Recognizing Boundary Violations

Signs that project-specific content has leaked into the template:

- File references a specific programming language or framework by name
- File contains hardcoded module/crate/package names
- File lists specific domain types by name
- File defines latency budgets or performance targets
- File contains project-specific architectural decisions
