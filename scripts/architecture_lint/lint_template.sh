#!/usr/bin/env bash
# Architecture Lint — Template
#
# Copy this script to your project and customize the RULES section
# with your project-specific forbidden dependency patterns.
#
# Usage: ./scripts/architecture_lint/lint.sh [source_root]
# Exit codes: 0 = clean, 1 = violations found

set -euo pipefail

SOURCE_ROOT="${1:-.}"
VIOLATIONS=0

red()     { printf '\033[0;31m%s\033[0m\n' "$*"; }
green()   { printf '\033[0;32m%s\033[0m\n' "$*"; }
heading() { printf '\n=== %s ===\n' "$*"; }

# Check a single rule: search for a forbidden pattern in a directory.
# Arguments: label, directory, grep_pattern, file_glob (default: *.rs)
check_rule() {
  local label="$1" dir="$2" pattern="$3" glob="${4:-*.rs}"
  if [ ! -d "$dir" ]; then
    return
  fi
  local matches
  matches=$(grep -rn --include="$glob" -E "$pattern" "$dir" 2>/dev/null || true)
  if [ -n "$matches" ]; then
    red "VIOLATION: $label"
    echo "$matches"
    VIOLATIONS=$((VIOLATIONS + 1))
  fi
}

heading "Architecture Lint"

# ============================================================
# RULES — Customize this section for your project
# ============================================================
#
# Example rules (uncomment and modify):
#
# heading "Rule 1 — {{CORE_LAYER}} must not import framework"
# check_rule \
#   "{{CORE_LAYER}} imports framework" \
#   "$SOURCE_ROOT/{{CORE_LAYER}}" \
#   'use framework::|extern crate framework'
#
# heading "Rule 2 — {{DATA_LAYER}} must not reference UI types"
# check_rule \
#   "{{DATA_LAYER}} references UI types" \
#   "$SOURCE_ROOT/{{DATA_LAYER}}" \
#   'Widget|View|Renderer|Screen'
#
# heading "Rule 3 — {{APP_LAYER}} must not perform filesystem I/O in hot paths"
# check_rule \
#   "{{APP_LAYER}} performs filesystem I/O" \
#   "$SOURCE_ROOT/{{APP_LAYER}}" \
#   'std::fs::|File::open|File::create'
#
# ============================================================

echo ""
echo "No project-specific rules configured."
echo "Copy this template and add your rules in the RULES section."
echo "See docs/process/ARCHITECTURE_GUARDRAILS.md for guidance."

# ============================================================
# Summary
# ============================================================
echo ""
if [ "$VIOLATIONS" -gt 0 ]; then
  red "Found $VIOLATIONS architecture violation(s)."
  exit 1
else
  green "No architecture violations detected."
  exit 0
fi
