# STEP 7: Automatic Audit

## Purpose

Run a comprehensive consistency check across all affected documents. Broader than analysis — covers the full 13-point audit.

Runs automatically after every task. Do not skip. Do not wait for user request.

## Required Reads

- `docs/core/SPEC.md` (re-read)
- `docs/core/DEFINITIONS.md` (re-read)
- `docs/project/TASKS.md` (re-read)
- `docs/ai/GOVERNANCE_CHECKS.md`
- `docs/ai/templates/AUDIT_REPORT.md`

## Procedure

1. Re-read SPEC.md, DEFINITIONS.md, and TASKS.md.
2. Check for all 13 audit points:
   - **SPEC violations**: any document contradicting SPEC.md
   - **Non-goal violations**: features conflicting with NON_GOALS.md
   - **Assumption conflicts**: designs that silently contradict ASSUMPTIONS.md
   - **Hierarchy violations**: lower document contradicting a higher one
   - **Extension boundary violations**: domain-specific concepts in core
   - **Performance constraint violations**: designs incompatible with SPEC performance requirements
   - **ADR conflicts**: work contradicting accepted ADRs
   - **Term drift**: terms used in modified documents but not in DEFINITIONS.md
   - **Contradictions**: statements that conflict across documents
   - **Orphaned references**: links to documents or sections that don't exist
   - **Stale content**: information outdated given the work just completed
   - **Missing registrations**: documents that exist but are not listed in DOCUMENT_SYSTEM.md
   - **Code drift**: implementation that diverges from documented architecture

## Output Format

Use the exact format from `docs/ai/templates/AUDIT_REPORT.md`:

```
## Audit Result
Scope: <list of modified docs, related ADRs, related tasks>

Checks:
- SPEC violations: none | <list>
- Non-goal violations: none | <list>
- Assumption conflicts: none | <list>
- Hierarchy violations: none | <list>
- Extension violations: none | <list>
- Performance violations: none | <list>
- ADR conflicts: none | <list>
- Term drift: none | <list>
- Contradictions: none | <list>
- Orphaned refs: none | <list>
- Stale content: none | <list>
- Missing registrations: none | <list>
- Code drift: none | <list>

Risk level: low | medium | high
Status: green | yellow | red

Violations:
- none | <list>

Recommended action:
- continue | fix before close | escalate to ADR
```

## Stop Conditions

- **Red** (any SPEC/hierarchy/extension/performance/non-goal violation or ADR conflict) → **stop**. Do not complete task.
- **Yellow** (non-blocking issues) → note and proceed to Step 8.
- **Green** → proceed to Step 8.
