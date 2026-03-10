#!/usr/bin/env bash
# Spec ↔ Code Consistency Checker — Template
#
# Copy this script to your project and customize the TYPES section
# with your project-specific required type definitions.
#
# Usage: ./scripts/spec_consistency_check/check.sh [source_root]
# Exit codes: 0 = consistent, 1 = mismatches found

set -euo pipefail

SOURCE_ROOT="${1:-.}"
MISSING=0
FOUND=0

red()     { printf '\033[0;31m  MISSING: %s\033[0m\n' "$*"; }
green()   { printf '\033[0;32m  FOUND:   %s\033[0m\n' "$*"; }
heading() { printf '\n=== %s ===\n' "$*"; }

# ============================================================
# TYPES — Customize this section for your project
# ============================================================
# List all core types that must exist in the codebase per your
# spec/architecture documents.
#
# Example (uncomment and modify):
#
# REQUIRED_TYPES=(
#   {{DOMAIN_TYPE_1}}
#   {{DOMAIN_TYPE_2}}
#   {{DOMAIN_TYPE_3}}
# )
#
# ============================================================

REQUIRED_TYPES=()

# File extension for type definitions (change for your language)
FILE_GLOB="*.rs"

# Regex pattern for type definitions (change for your language)
# Rust: struct, enum, trait, type
# TypeScript: interface, type, class
# Python: class
TYPE_PATTERN="(struct|enum|trait|type)"

heading "Spec ↔ Code Consistency Check"
echo "Scanning: $SOURCE_ROOT"

if [ "${#REQUIRED_TYPES[@]}" -eq 0 ]; then
  echo ""
  echo "No required types configured."
  echo "Copy this template and add your types in the TYPES section."
  echo "See docs/process/SPEC_CODE_CONSISTENCY.md for guidance."
  exit 0
fi

if [ ! -d "$SOURCE_ROOT" ]; then
  echo "WARNING: Source directory '$SOURCE_ROOT' not found."
  exit 1
fi

echo ""
for type_name in "${REQUIRED_TYPES[@]}"; do
  match=$(grep -rn --include="$FILE_GLOB" -E "$TYPE_PATTERN\s+$type_name\b" "$SOURCE_ROOT" 2>/dev/null | head -1 || true)
  if [ -n "$match" ]; then
    green "$type_name — $match"
    FOUND=$((FOUND + 1))
  else
    red "$type_name"
    MISSING=$((MISSING + 1))
  fi
done

# Summary
echo ""
heading "Summary"
echo "  Found:   $FOUND / ${#REQUIRED_TYPES[@]}"
echo "  Missing: $MISSING / ${#REQUIRED_TYPES[@]}"

if [ "$MISSING" -gt 0 ]; then
  printf '\033[0;31m\nSpec/code drift detected. %d type(s) missing.\033[0m\n' "$MISSING"
  exit 1
else
  printf '\033[0;32m\nAll spec types accounted for.\033[0m\n'
  exit 0
fi
