# /audit — Full Project System Audit

> **Milestone command.** Use `/audit` at phase boundaries, milestones, or for periodic full-project reviews. For validating recent changes only, use `/check` instead.
>
> Authoritative step definition: `docs/ai/runtime/STEP_7_AUDIT.md`
> Output template: `docs/ai/templates/AUDIT_REPORT.md`
> Governance checks: `docs/ai/GOVERNANCE_CHECKS.md`

Use this command to perform a full system-level review of consistency across all documentation and between documentation and code.

## Instructions for Claude

1. Read all governance documents first:
   - `docs/core/SPEC.md` — non-negotiable constraints
   - `docs/core/NON_GOALS.md` — scope boundary
   - `docs/core/ASSUMPTIONS.md` — design context
   - `docs/ai/DOCUMENT_SYSTEM.md` — document registry
   - `docs/core/DEFINITIONS.md`
   - `docs/ai/GOVERNANCE_CHECKS.md` — fail conditions
   - Relevant ADRs from `docs/project/decisions/`

2. Then read all project content documents that exist.

3. Check for all 13 audit points per `docs/ai/runtime/STEP_7_AUDIT.md`:
   - SPEC violations, non-goal violations, assumption conflicts
   - Hierarchy violations, extension boundary violations, performance violations
   - ADR conflicts, term drift, contradictions
   - Orphaned references, stale content, missing registrations, code drift

4. Produce output in the exact format from `docs/ai/templates/AUDIT_REPORT.md`.

   **Red** = stop. **Yellow** = note and proceed. **Green** = clean.

   See `docs/ai/GOVERNANCE_CHECKS.md` for the full list of fail conditions.

5. Do NOT fix issues automatically. Present findings for review.
