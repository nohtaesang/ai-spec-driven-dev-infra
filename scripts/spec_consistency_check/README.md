# Spec ↔ Code Consistency Checker — Template

A customizable script for verifying that core types from design documents exist in the codebase.

## Usage

1. Copy `check_template.sh` to your project as `check.sh`
2. Edit the TYPES section with your project-specific required types
3. Adjust `FILE_GLOB` and `TYPE_PATTERN` for your language
4. Run: `./scripts/spec_consistency_check/check.sh [source_root]`

## Language Support

| Language | FILE_GLOB | TYPE_PATTERN |
|---|---|---|
| Rust | `*.rs` | `(struct\|enum\|trait\|type)` |
| TypeScript | `*.ts` | `(interface\|type\|class)` |
| Python | `*.py` | `class` |
| Go | `*.go` | `type` |

## See Also

- `docs/process/SPEC_CODE_CONSISTENCY.md` — framework for consistency checking
- `docs/process/PROJECT_EXTENSIONS.md` — what belongs in project repos
