# /analyze — Analyze Design or Architecture

> **Internal mode.** This mode is normally invoked internally by `/next` depending on task type. It remains available for standalone use when needed.
>
> The authoritative workflow is defined in [`docs/ai/CLAUDE.md`](../ai/CLAUDE.md).

Use this mode to review and reason about the current design or a proposed change.

## Instructions for Claude

1. Read the relevant documents:
   - `docs/core/SPEC.md` — non-negotiable constraints
   - `docs/core/NON_GOALS.md` — scope boundary
   - `docs/core/ASSUMPTIONS.md` — design context
   - `docs/core/DEFINITIONS.md`
   - Architecture documents (if they exist)
   - Relevant ADRs from `docs/project/decisions/`
   - Any other documents specified by the user

2. Identify:
   - Strengths of the current design
   - Gaps or undefined areas
   - Potential conflicts or ambiguities
   - Dependencies between components

3. Check governance compliance:
   - **SPEC conformance** — does the design implement SPEC.md?
   - **Non-goal boundary** — does the design avoid NON_GOALS.md violations?
   - **Assumption alignment** — does the design depend on stated assumptions?
   - **Extension boundary** — are domain-specific features in extensions, not core?
   - **Performance constraints** — does the design respect SPEC performance requirements?
   - **ADR consistency** — does the design align with accepted ADRs?

4. Produce a structured analysis with:
   - **Summary**: What was analyzed
   - **Findings**: Key observations
   - **Governance**: SPEC / non-goal / assumption / extension / performance / ADR status
   - **Risks**: Potential issues
   - **Recommendations**: Suggested next steps

5. Do NOT make changes. This command is read-only analysis.
