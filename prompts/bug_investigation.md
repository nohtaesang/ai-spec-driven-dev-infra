# Prompt Template: Bug Investigation

## Bug Report

- **Symptom**: [What the user observes]
- **Expected behavior**: [What should happen instead]
- **Steps to reproduce**: [How to trigger the bug]
- **Severity**: [Critical / High / Medium / Low]

## Context

- **Affected module(s)**: [Which parts of the codebase]
- **Related systems**: [What subsystems are involved]
- **Recent changes**: [Any recent commits that might be related]

## Investigation Checklist

1. [ ] Reproduce the issue
2. [ ] Identify root cause (not just symptom)
3. [ ] Check if this is a known anti-pattern (project performance guardrails)
4. [ ] Check if an architectural boundary was crossed (architecture guardrails)
5. [ ] Check if the bug reveals a spec/code inconsistency

## Fix Constraints

1. [ ] No new architectural violations introduced
2. [ ] No performance guardrail violations
3. [ ] Test added that would have caught the bug
4. [ ] Architecture lint passes
5. [ ] Definition of Done checklist passes

## Output

- Root cause analysis
- The fix (code changes)
- Test coverage for the fix
- Related issues discovered during investigation
