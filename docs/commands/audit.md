# /audit — Full Project System Audit

> **Milestone command.** Use `/audit` at phase boundaries, milestones, or for periodic full-project reviews. For validating recent changes only, use `/check` instead.
>
> The authoritative audit definition is in [`docs/ai/CLAUDE.md`](../ai/CLAUDE.md) (see Step 7: Automatic Audit).

Use this command to perform a full system-level review of consistency across all documentation and between documentation and code.

## Instructions for Claude

1. Read all governance documents first:
   - `docs/core/SPEC.md` — non-negotiable constraints
   - `docs/core/NON_GOALS.md` — scope boundary
   - `docs/core/ASSUMPTIONS.md` — design context
   - `docs/ai/DOCUMENT_SYSTEM.md` — document registry
   - `docs/core/DEFINITIONS.md`
   - Relevant ADRs from `docs/project/decisions/`

2. Then read all project content documents that exist.

3. Check for (13-point audit):
   - **SPEC violations**: any document contradicting SPEC.md
   - **Non-goal violations**: features conflicting with NON_GOALS.md
   - **Assumption conflicts**: designs that silently contradict ASSUMPTIONS.md
   - **Hierarchy violations**: lower document contradicting a higher one
   - **Extension boundary violations**: domain-specific concepts in core
   - **Performance constraint violations**: designs incompatible with SPEC performance requirements
   - **ADR conflicts**: work contradicting accepted ADRs
   - **Term drift**: terms used in documents but not defined in `DEFINITIONS.md`
   - **Contradictions**: statements in one document that conflict with another
   - **Orphaned references**: links to documents or sections that don't exist
   - **Stale content**: information that appears outdated vs. current state
   - **Missing registrations**: documents that exist but aren't listed in `DOCUMENT_SYSTEM.md`
   - **Code drift**: code that doesn't match documented architecture (if code exists)

4. Produce an audit report:
   - **Status**: Overall health (green / yellow / red)
   - **Issues**: List of problems found, categorized by type
   - **Recommendations**: Suggested fixes, prioritized

5. Do NOT fix issues automatically. Present findings for review.
