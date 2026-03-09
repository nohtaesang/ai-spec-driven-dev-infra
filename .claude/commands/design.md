# /design — Create or Modify System Design

> **Internal mode.** This mode is normally invoked internally by `/next` depending on task type. It remains available for standalone use when needed.
>
> The authoritative workflow is defined in [`docs/ai/CLAUDE.md`](../ai/CLAUDE.md) (see Step 5: `type: design`).

Use this mode to create new design documents or update existing ones.

## Instructions for Claude

1. Read the relevant documents:
   - `docs/core/SPEC.md` — non-negotiable constraints
   - `docs/core/NON_GOALS.md` — scope boundary
   - `docs/core/ASSUMPTIONS.md` — design context
   - `docs/core/PRINCIPLES.md`
   - `docs/core/DEFINITIONS.md`
   - `docs/ai/CHANGE_PROTOCOL.md`
   - Relevant ADRs from `docs/project/decisions/`
   - Target document(s) specified by the user

2. Before drafting, verify governance compliance:
   - **SPEC conformance** — design must implement, not contradict, the SPEC
   - **Non-goal boundary** — feature must not conflict with NON_GOALS.md
   - **Assumption alignment** — identify which assumptions the design depends on
   - **Extension boundary** — domain-specific features go in extensions, not core
   - **Performance constraints** — design must respect SPEC performance requirements
   - **ADR consistency** — check existing ADRs for relevant prior decisions

3. Follow the Change Protocol:
   - Identify affected documents
   - Check for conflicts
   - Draft the change
   - Present for review before applying

4. When writing design content:
   - Use terms from `DEFINITIONS.md` consistently
   - Add new terms to `DEFINITIONS.md` if needed
   - Reference other documents rather than duplicating content
   - Include rationale for design choices

5. After applying changes:
   - Create ADR file in `docs/project/decisions/` if an architectural decision was made
   - Update `DECISIONS.md` index
   - Update `docs/project/TASKS.md` if task status changed
