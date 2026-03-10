# Analysis Report Template

Used by Step 6 (Automatic Analysis). Output exactly in this format.

```
## Analysis Result
Task: TASK-NNN
Target: <file path>

Checks:
- SPEC conformance: pass | FAIL: <detail>
- Non-goal boundary: pass | FAIL: <detail>
- Assumption alignment: pass | CHANGE NEEDED: <detail>
- Extension boundary: pass | FAIL: <detail>
- Performance constraints: pass | FAIL: <detail>
- ADR consistency: pass | CONFLICT: <detail>
- Term registration: pass | FAIL: <unregistered terms>

Findings:
1. <observation>
2. ...

Risks:
- <risk, if any>

Required follow-up:
- none | <action items>
```

## Verdict Rules

- Any **FAIL** → stop immediately. Do not proceed to Step 7.
- All **pass** → proceed to Step 7.
- **CHANGE NEEDED** on assumption alignment → note but may proceed if the assumption change is proposed.
