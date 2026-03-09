# /check — Validate Recent Changes

Validate recent changes or implementation output against infrastructure rules. Unlike `/audit` (which performs a full project-level review), `/check` focuses on **recent work only**.

---

## Instructions for Claude

1. Identify the recent changes — files modified in the current session or since the last task completion.

2. Check the following:

   - **Documentation drift** — do modified documents still align with their parent documents in the hierarchy?
   - **TODO / FIXME without roadmap reference** — are there untracked TODOs or FIXMEs that should be tasks?
   - **Duplicated definitions** — are terms defined in multiple places instead of only in `DEFINITIONS.md`?
   - **Magic numbers or configuration violations** — are there hardcoded values that should be configurable or documented?
   - **Missing documentation updates** — did code or design changes require doc updates that were not made?
   - **SSOT violations** — is any concept defined in more than one place (single source of truth)?

3. **Output structure**:

```
Scope: <files checked>

Warnings:
- <warning>

Rule violations:
- <violation>

Recommended fixes:
- <fix>
```

If no issues are found:

```
All checked changes comply with infrastructure rules.
```

4. Do NOT fix issues automatically. Present findings for review.

---

## Relationship to `/audit`

| Command | Scope | When to use |
|---|---|---|
| `/check` | Recent changes only | After completing work, before marking a task done |
| `/audit` | Full project system | At milestones, phase boundaries, or periodic reviews |
