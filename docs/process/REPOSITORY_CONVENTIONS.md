# Repository Conventions

Generic file and module placement rules. Projects using this template should follow these conventions unless an ADR explicitly overrides them.

## Directory Structure

```
project-root/
├── CLAUDE.md                    Project rules for AI sessions
├── docs/
│   ├── core/                    Foundation documents (SPEC, DEFINITIONS, VISION, etc.)
│   ├── model/                   Domain models
│   ├── architecture/            Technical architecture
│   ├── ux/                      User experience design
│   ├── planning/                Scope and roadmap
│   ├── project/                 Tracking (TASKS, DONE, DECISIONS, decisions/)
│   ├── ai/                      AI collaboration governance
│   └── process/                 Reusable process documents
├── src/ or crates/              Application source code
├── tests/                       Integration and end-to-end tests
├── scripts/                     Automation and tooling scripts
├── prompts/                     AI prompt templates
└── config/                      Configuration files
```

## File Placement Rules

| Content Type | Location | Rationale |
|---|---|---|
| Foundation docs | `docs/core/` | Single source of truth for constraints |
| Domain models | `docs/model/` | Separated from implementation |
| Architecture decisions | `docs/project/decisions/` | Immutable ADR records |
| Process guardrails | `docs/process/` | Reusable across phases |
| Source code | `src/` or `crates/` | Standard language convention |
| Unit tests | Adjacent to source (same module) | Co-located for discoverability |
| Integration tests | `tests/` | Separate from unit tests |
| Scripts and tooling | `scripts/` | Automation kept out of source tree |
| AI prompt templates | `prompts/` | Standardized AI interaction patterns |
| Config files | `config/` or project root | Depends on toolchain convention |

## Module Placement Rules

1. **One concept per module.** Avoid god-modules that mix unrelated types.
2. **Public API at module root.** Re-export public types from `mod.rs` or `lib.rs`.
3. **Internal helpers stay private.** Only expose what external modules need.
4. **Tests co-located with source.** Unit tests in the same file or a `tests` submodule.
5. **Cross-module dependencies flow downward.** Higher layers depend on lower layers, never the reverse.

## Documentation Placement Rules

1. **Each concept defined in one place.** Other documents reference, not redefine.
2. **Design docs before code.** The document exists before the implementation.
3. **Process docs are generic.** Project-specific process goes in project-level extensions.
4. **ADRs are append-only.** Supersede, don't edit.

## Configuration Placement Rules

1. **Config files in a predictable location.** `config/` or project root per toolchain convention.
2. **No config values buried in source code.** Tunables belong in config, not hardcoded.
3. **Defaults have a single source of truth.** See `CONFIG_CONSTANTS_POLICY.md`.

## Public API Exposure Rules

1. **Minimize public surface.** Only expose what consumers need.
2. **Public types must be documented.** At minimum, a one-line description.
3. **Breaking changes require an ADR.** Public API changes are architectural decisions.
4. **Domain types must be in DEFINITIONS.md.** Any type that appears in public APIs must be a registered term.
