# Bootstrap Document Validator

Validates that bootstrap-generated documents are complete and clean before the project proceeds to Phase 1.

## Usage

```bash
python3 scripts/bootstrap_check/check_bootstrap_docs.py [docs_root]
```

If `docs_root` is omitted, defaults to the current directory.

## When to Run

Run once after bootstrap completes (after Step B9, before the first `/next`).

## What It Checks

| Rule | What it catches | Why it matters |
|---|---|---|
| `missing-file` | Required bootstrap file doesn't exist | Bootstrap didn't complete |
| `unresolved-placeholder` | `{{PLACEHOLDER}}` patterns remain | Template wasn't filled in |
| `leftover-marker` | `<!-- BOOTSTRAP:PENDING -->` still present | Bootstrap didn't clean up |
| `missing-section` | Required heading absent | Document structure is incomplete |
| `empty-section` | Heading exists but no content below it | Content wasn't generated |
| `dummy-value` | `TBD`, `TODO`, `placeholder`, `lorem ipsum` | Content is fake |
| `name-mismatch` | Project name differs across documents | Cross-file inconsistency |

## Exit Codes

- `0` — All checks pass (warnings are informational)
- `1` — At least one failure found

## Customization

Edit the configuration section at the top of the script to:
- Add required files (`REQUIRED_FILES`)
- Add required sections per file (`REQUIRED_SECTIONS`)
- Add placeholder patterns (`PLACEHOLDER_PATTERNS`)
- Add dummy value patterns (`DUMMY_VALUES`)
