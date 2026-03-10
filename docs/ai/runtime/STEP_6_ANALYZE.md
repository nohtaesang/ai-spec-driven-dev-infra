# STEP 6: Automatic Analysis

## Purpose

Run governance checks on all work produced in Step 5. Detect violations before the audit step.

Runs automatically after every task. Do not skip. Do not wait for user request.

## Required Reads

- Target document and all documents modified during the task
- `docs/ai/GOVERNANCE_CHECKS.md`
- `docs/ai/templates/ANALYSIS_REPORT.md`

## Procedure

1. Check the target document and all documents modified during the task.
2. **Verify SPEC conformance** — flag any deviation from SPEC sections.
3. **Verify non-goal boundary** — flag any feature that conflicts with `NON_GOALS.md`.
4. **Verify assumption alignment** — flag any design that silently contradicts `ASSUMPTIONS.md`.
5. **Verify extension boundary** — flag any domain-specific concepts leaking into core.
6. **Verify performance constraints** — flag designs that violate SPEC performance requirements.
7. Verify consistency with `PRINCIPLES.md` and architecture documents.
8. Verify the document hierarchy is respected.
9. **Check ADR consistency** — verify no contradiction with accepted ADRs.
10. **Check term registration** — verify all new domain terms are in DEFINITIONS.md.
11. Identify gaps, ambiguities, or open questions.

## Output Format

Use the exact format from `docs/ai/templates/ANALYSIS_REPORT.md`. Do not deviate.

## Verdict Rules

See `docs/ai/templates/ANALYSIS_REPORT.md` for the complete verdict rules.

- Any **FAIL** → stop immediately. Do not proceed to Step 7.
- **CHANGE NEEDED** on assumption alignment → may proceed only if the assumption change is proposed as part of the task.
- All **pass** → proceed to Step 7.
