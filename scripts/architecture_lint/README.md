# Architecture Lint — Template

A customizable lint script for detecting forbidden dependency patterns across project modules.

## Usage

1. Copy `lint_template.sh` to your project as `lint.sh`
2. Edit the RULES section with your project-specific patterns
3. Run: `./scripts/architecture_lint/lint.sh [source_root]`

## How It Works

Each rule uses `grep` to search for forbidden patterns in a specific directory. If any match is found, it's reported as a violation and the script exits non-zero.

The `check_rule` function accepts:
- `label` — human-readable description of the rule
- `dir` — directory to search
- `pattern` — extended regex pattern to match
- `glob` — file glob (defaults to `*.rs`, change for other languages)

## See Also

- `docs/process/ARCHITECTURE_GUARDRAILS.md` — framework for defining guardrails
- `docs/process/PROJECT_EXTENSIONS.md` — what belongs in project repos
