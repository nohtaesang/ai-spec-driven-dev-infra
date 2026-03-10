# Governance Checks

Explicit fail conditions for automated governance. These are the rules that `/next` (Steps 5–7), `/analyze`, `/audit`, and `/check` enforce. A check either **passes** or **fails** — there is no ambiguity.

---

## Task State Checks

| Condition | Verdict |
|---|---|
| More than one `[-]` task exists in TASKS.md | **FAIL** — resolve before continuing |
| `[-]` task has no `progress:` field | **FAIL** — add progress before any other work |
| New task selected while another is `[-]` | **FAIL** — complete, abandon, or block current task first |
| Task marked `[x]` without DONE.md entry | **FAIL** — append DONE.md before closing |
| Task marked `[x]` without analysis + audit passing | **FAIL** — run analysis and audit first |
| Task dependencies (`depends:`) not all `[x]` | **FAIL** — cannot start task |

## Document Integrity Checks

| Condition | Verdict |
|---|---|
| Design document not registered in DOCUMENT_SYSTEM.md | **FAIL** — register before treating as authoritative |
| Placeholder document treated as authoritative constraint | **FAIL** — placeholders exist for structure only; content is not binding until the design task completes |
| New domain term used in a design document but absent from DEFINITIONS.md | **FAIL** — term drift; register in DEFINITIONS.md before proceeding |
| Definition in DEFINITIONS.md contradicts SPEC.md | **FAIL** — SPEC.md wins; update DEFINITIONS.md |
| Document references a non-existent document or section | **FAIL** — orphaned reference; fix or remove |

## Change Control Checks

| Condition | Verdict |
|---|---|
| SPEC.md modified without a prior ADR | **FAIL** — create ADR first |
| NON_GOALS.md modified without a prior ADR | **FAIL** — create ADR first |
| ASSUMPTIONS.md modified without a prior ADR | **FAIL** — create ADR first |
| Architecture decision made without ADR | **FAIL** — create ADR |
| Accepted ADR contradicted by new work | **FAIL** — create superseding ADR or revise the work |

## Conformance Checks

| Condition | Verdict |
|---|---|
| Lower-level document contradicts higher-level document | **FAIL** — hierarchy violation |
| Implementation contradicts design document | **FAIL** — update design or fix implementation |
| Design document contradicts SPEC.md | **FAIL** — stop immediately |
| Feature conflicts with NON_GOALS.md | **FAIL** — stop and flag |
| Design silently depends on unverified assumption | **WARN** — verify against ASSUMPTIONS.md |
| Domain-specific feature placed in core (not extension) | **FAIL** — extension boundary violation |
| Design violates SPEC.md performance constraints | **FAIL** — redesign required |

## Stop Conditions

Claude must **stop and report** (not proceed) when any of the following are true:

- SPEC.md would be contradicted
- NON_GOALS.md would be violated
- More than one `[-]` task exists
- Target document is not registered in DOCUMENT_SYSTEM.md
- Implementation is requested but governing design docs are still placeholders
- Architecture change is implied but no ADR exists or is proposed
- Required related documents were not read before executing
- Accepted ADR would be contradicted without a superseding ADR

---

## How This File Is Used

- `/next` Step 5 checks stop conditions before executing.
- `/next` Step 6 (analysis) runs conformance and document integrity checks.
- `/next` Step 7 (audit) runs all checks above.
- `/analyze` and `/audit` reference these conditions for pass/fail determination.
- `/check` references these conditions for focused validation.

Any **FAIL** verdict on a non-waivable check blocks task completion.
