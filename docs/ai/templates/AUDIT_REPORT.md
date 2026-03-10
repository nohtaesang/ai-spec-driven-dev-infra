# Audit Report Template

Used by Step 7 (Automatic Audit). Output exactly in this format.

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

## Verdict Rules

- **Red** = any SPEC/hierarchy/extension/performance/non-goal violation or ADR conflict → stop. Do not close task.
- **Yellow** = non-blocking issues (term drift, stale content, orphaned refs) → note and proceed.
- **Green** = clean → proceed to Step 8.
