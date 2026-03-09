# /implement — Implement Features

> **Internal mode.** This mode is normally invoked internally by `/next` depending on task type. It remains available for standalone use when needed.
>
> The authoritative workflow is defined in [`docs/ai/CLAUDE.md`](../ai/CLAUDE.md) (see Step 5: `type: implement`).

Use this mode when writing code. Ensures documentation is respected and updated.

## Instructions for Claude

1. Read the relevant documents:
   - `docs/core/SPEC.md` — non-negotiable constraints
   - `docs/core/NON_GOALS.md` — scope boundary
   - `docs/core/ASSUMPTIONS.md` — design context
   - `docs/ai/CLAUDE.md` — behavioral rules
   - `docs/ai/CHANGE_PROTOCOL.md`
   - Architecture documents (if they exist)
   - `docs/project/TASKS.md`
   - Relevant ADRs from `docs/project/decisions/`
   - Any model or UX documents relevant to the feature

2. Verify before implementing:
   - Feature is within current scope
   - Feature is listed in `TASKS.md`
   - **SPEC conformance** — implementation matches SPEC.md constraints
   - **Non-goal boundary** — feature does not conflict with NON_GOALS.md
   - **Assumption alignment** — implementation aligns with ASSUMPTIONS.md
   - **Extension boundary** — domain-specific code is in extensions, not core
   - **Performance constraints** — respects SPEC performance requirements
   - **ADR consistency** — implementation aligns with accepted ADRs
   - Required terms are defined in `DEFINITIONS.md`

3. If documentation needs updating:
   - Update docs FIRST, following the Change Protocol
   - Then proceed with implementation

4. Implement the feature:
   - Follow architectural boundaries
   - Use domain terms consistently
   - Write tests

5. After implementation:
   - Update `TASKS.md` (mark complete, move to `DONE.md`)
   - Create ADR file in `docs/project/decisions/` if any architectural decisions were made
   - Update `DECISIONS.md` index
