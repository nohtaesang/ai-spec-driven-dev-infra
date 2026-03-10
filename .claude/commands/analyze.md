# /analyze — Analyze Design or Architecture

> **Internal mode.** This mode is normally invoked internally by `/next` (Step 6). It remains available for standalone use when needed.
>
> Authoritative step definition: `docs/ai/runtime/STEP_6_ANALYZE.md`
> Output template: `docs/ai/templates/ANALYSIS_REPORT.md`
> Governance checks: `docs/ai/GOVERNANCE_CHECKS.md`

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

3. Check governance compliance per `docs/ai/GOVERNANCE_CHECKS.md`:
   - **SPEC conformance** — does the design implement SPEC.md?
   - **Non-goal boundary** — does the design avoid NON_GOALS.md violations?
   - **Assumption alignment** — does the design depend on stated assumptions?
   - **Extension boundary** — are domain-specific features in extensions, not core?
   - **Performance constraints** — does the design respect SPEC performance requirements?
   - **ADR consistency** — does the design align with accepted ADRs?
   - **Term registration** — are all domain terms in DEFINITIONS.md?

4. Produce output in the exact format from `docs/ai/templates/ANALYSIS_REPORT.md`.

   Any **FAIL** blocks task completion. **CHANGE NEEDED** on assumption alignment may proceed only if the assumption change is proposed. See `docs/ai/GOVERNANCE_CHECKS.md` for the full list of fail conditions.

5. Do NOT make changes. This command is read-only analysis.
