#!/usr/bin/env python3
"""
Bootstrap Document Validator

Validates that bootstrap-generated documents are complete and clean
before the project proceeds to Phase 1.

Run after bootstrap completes:
    python3 scripts/bootstrap_check/check_bootstrap_docs.py [docs_root]

Exit codes: 0 = all checks pass, 1 = failures found
"""

import re
import sys
from pathlib import Path

# ============================================================
# Configuration
# ============================================================

DOCS_ROOT_DEFAULT = "."

# Required files that bootstrap must produce.
# Paths are relative to docs_root.
REQUIRED_FILES = [
    "docs/core/SPEC.md",
    "docs/core/VISION.md",
    "docs/core/PRINCIPLES.md",
    "docs/core/ASSUMPTIONS.md",
    "docs/core/NON_GOALS.md",
    "docs/core/DEFINITIONS.md",
    "docs/project/PROJECT_STATE.md",
]

# Required section headings per file (level 1 or 2 headings).
# Key: file path (relative), Value: list of required heading substrings.
REQUIRED_SECTIONS = {
    "docs/core/SPEC.md": [
        "System Scope",
        "Specification Enforcement",
    ],
    "docs/core/VISION.md": [
        "Why",
        "Target Users",
    ],
    "docs/core/PRINCIPLES.md": [
        "Design Principles",
        "Engineering Principles",
    ],
    "docs/core/ASSUMPTIONS.md": [],  # sections vary by project
    "docs/core/NON_GOALS.md": [],  # sections vary by project
    "docs/core/DEFINITIONS.md": [],  # terms vary by project
    "docs/project/PROJECT_STATE.md": [
        "Current Phase",
        "Current Focus",
        "What Changed Recently",
        "Active Risks",
        "Next Likely Decisions",
        "Next Session Start",
    ],
}

# Patterns that indicate unresolved template placeholders.
PLACEHOLDER_PATTERNS = [
    r"\{\{[A-Z_]+\}\}",           # {{PLACEHOLDER}}
    r"\{\{#each\b",               # {{#each ...}}
    r"\{\{#if\b",                 # {{#if ...}}
    r"\{\{/each\}\}",             # {{/each}}
    r"\{\{/if\}\}",               # {{/if}}
]

# Markers that should have been removed during bootstrap.
LEFTOVER_MARKERS = [
    "<!-- BOOTSTRAP:PENDING -->",
    "<!-- BOOTSTRAP:PLACEHOLDER -->",
    "<!-- PROJECT SETUP INSTRUCTIONS",
]

# Dummy values that indicate content was not actually filled in.
DUMMY_VALUES = [
    r"(?i)^[\s*-]*TBD\s*$",
    r"(?i)^[\s*-]*TODO\s*$",
    r"(?i)^[\s*-]*placeholder\s*$",
    r"(?i)^[\s*-]*lorem ipsum",
    r"(?i)^[\s*-]*to be (decided|determined|defined)\s*$",
]

# Minimum meaningful content: a section must have at least this many
# non-empty, non-heading lines to count as "has content".
MIN_SECTION_LINES = 1


# ============================================================
# Output helpers
# ============================================================

class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[0;33m"
    RESET = "\033[0m"


failures: list[str] = []
warnings: list[str] = []


def fail(file: str, rule: str, detail: str) -> None:
    msg = f"FAIL  [{file}] {rule}: {detail}"
    failures.append(msg)
    print(f"{Colors.RED}  {msg}{Colors.RESET}")


def warn(file: str, rule: str, detail: str) -> None:
    msg = f"WARN  [{file}] {rule}: {detail}"
    warnings.append(msg)
    print(f"{Colors.YELLOW}  {msg}{Colors.RESET}")


def ok(message: str) -> None:
    print(f"{Colors.GREEN}  OK    {message}{Colors.RESET}")


def heading(text: str) -> None:
    print(f"\n=== {text} ===")


# ============================================================
# Check functions
# ============================================================

def check_file_exists(docs_root: Path, rel_path: str) -> bool:
    """Rule: required bootstrap file must exist."""
    full = docs_root / rel_path
    if not full.is_file():
        fail(rel_path, "missing-file", "Required bootstrap file does not exist")
        return False
    return True


def check_no_placeholders(docs_root: Path, rel_path: str) -> None:
    """Rule: no unresolved {{PLACEHOLDER}} patterns."""
    full = docs_root / rel_path
    lines = full.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines, 1):
        for pattern in PLACEHOLDER_PATTERNS:
            if re.search(pattern, line):
                fail(rel_path, "unresolved-placeholder",
                     f"Line {i}: {line.strip()}")


def check_no_leftover_markers(docs_root: Path, rel_path: str) -> None:
    """Rule: bootstrap markers must be removed after bootstrap."""
    full = docs_root / rel_path
    content = full.read_text(encoding="utf-8")
    for marker in LEFTOVER_MARKERS:
        if marker in content:
            fail(rel_path, "leftover-marker",
                 f"Found '{marker}' — should have been removed during bootstrap")


def check_required_sections(docs_root: Path, rel_path: str) -> None:
    """Rule: required section headings must be present."""
    required = REQUIRED_SECTIONS.get(rel_path, [])
    if not required:
        return
    full = docs_root / rel_path
    content = full.read_text(encoding="utf-8")
    # Extract all headings (# or ##)
    headings_found = re.findall(r"^#{1,2}\s+(.+)$", content, re.MULTILINE)
    headings_lower = [h.lower() for h in headings_found]
    for section in required:
        if not any(section.lower() in h for h in headings_lower):
            fail(rel_path, "missing-section",
                 f"Required section containing '{section}' not found")


def check_no_empty_sections(docs_root: Path, rel_path: str) -> None:
    """Rule: sections must have meaningful content, not just a heading."""
    full = docs_root / rel_path
    lines = full.read_text(encoding="utf-8").splitlines()

    # Find heading lines and check content between them
    heading_indices = []
    for i, line in enumerate(lines):
        if re.match(r"^#{1,3}\s+", line):
            heading_indices.append(i)

    for idx, h_idx in enumerate(heading_indices):
        heading_text = lines[h_idx].strip()
        # Determine section boundaries
        start = h_idx + 1
        end = heading_indices[idx + 1] if idx + 1 < len(heading_indices) else len(lines)

        # Count non-empty, non-separator lines in this section
        content_lines = []
        for line in lines[start:end]:
            stripped = line.strip()
            if stripped and stripped != "---" and not stripped.startswith("#"):
                content_lines.append(stripped)

        if len(content_lines) < MIN_SECTION_LINES:
            # Skip if heading is just a divider-like thing
            if any(keyword in heading_text.lower() for keyword in
                   ["purpose", "scope", "enforcement"]):
                # These are structural sections that must have content
                fail(rel_path, "empty-section",
                     f"Section '{heading_text}' has no meaningful content")
            else:
                # Other sections: warn only (some may legitimately be empty initially)
                warn(rel_path, "empty-section",
                     f"Section '{heading_text}' appears empty")


def check_no_dummy_values(docs_root: Path, rel_path: str) -> None:
    """Rule: no obvious dummy/placeholder text values."""
    full = docs_root / rel_path
    lines = full.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines, 1):
        for pattern in DUMMY_VALUES:
            if re.match(pattern, line):
                fail(rel_path, "dummy-value",
                     f"Line {i}: '{line.strip()}' looks like a placeholder value")


def check_project_name_consistency(docs_root: Path) -> None:
    """Rule: project name in SPEC.md and VISION.md should match."""
    spec = docs_root / "docs/core/SPEC.md"
    vision = docs_root / "docs/core/VISION.md"
    if not spec.is_file() or not vision.is_file():
        return  # Already caught by missing-file check

    spec_content = spec.read_text(encoding="utf-8")
    vision_content = vision.read_text(encoding="utf-8")

    # Extract first heading from each (likely contains project name)
    spec_h1 = re.search(r"^#\s+(.+)$", spec_content, re.MULTILINE)
    vision_h1 = re.search(r"^#\s+(.+)$", vision_content, re.MULTILINE)

    if not spec_h1 or not vision_h1:
        return

    # Simple heuristic: if both start with the same word, likely consistent
    spec_first = spec_h1.group(1).split()[0].lower().rstrip(":")
    vision_first = vision_h1.group(1).split()[0].lower().rstrip(":")

    # Only warn if they look like project names (not generic words)
    generic = {"spec", "vision", "specification", "project"}
    if spec_first not in generic and vision_first not in generic:
        if spec_first != vision_first:
            warn("cross-file", "name-mismatch",
                 f"SPEC.md title starts with '{spec_h1.group(1)}', "
                 f"VISION.md title starts with '{vision_h1.group(1)}' — verify consistency")


# ============================================================
# Main
# ============================================================

def main() -> int:
    docs_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DOCS_ROOT_DEFAULT)

    if not (docs_root / "docs/core").is_dir():
        print(f"Error: '{docs_root}/docs/core/' not found. "
              f"Run from repository root or pass docs_root as argument.")
        return 1

    print("Bootstrap Document Validator")
    print(f"Root: {docs_root.resolve()}")

    # ---- Phase 1: File existence ----
    heading("Required Files")
    existing_files = []
    for rel_path in REQUIRED_FILES:
        if check_file_exists(docs_root, rel_path):
            ok(rel_path)
            existing_files.append(rel_path)

    # ---- Phase 2: Content checks (only on existing files) ----
    heading("Template Placeholders")
    for rel_path in existing_files:
        check_no_placeholders(docs_root, rel_path)
    if not any("unresolved-placeholder" in f for f in failures):
        ok("No unresolved placeholders found")

    heading("Leftover Markers")
    for rel_path in existing_files:
        check_no_leftover_markers(docs_root, rel_path)
    if not any("leftover-marker" in f for f in failures):
        ok("No leftover bootstrap markers found")

    heading("Required Sections")
    for rel_path in existing_files:
        check_required_sections(docs_root, rel_path)
    if not any("missing-section" in f for f in failures):
        ok("All required sections present")

    heading("Empty Sections")
    for rel_path in existing_files:
        check_no_empty_sections(docs_root, rel_path)

    heading("Dummy Values")
    for rel_path in existing_files:
        check_no_dummy_values(docs_root, rel_path)
    if not any("dummy-value" in f for f in failures):
        ok("No dummy values found")

    heading("Cross-File Consistency")
    check_project_name_consistency(docs_root)
    if not any("name-mismatch" in w for w in warnings):
        ok("Project naming looks consistent")

    # ---- Summary ----
    heading("Summary")
    print(f"  Failures: {len(failures)}")
    print(f"  Warnings: {len(warnings)}")

    if failures:
        print(f"\n{Colors.RED}Bootstrap validation FAILED. "
              f"Fix {len(failures)} issue(s) before proceeding.{Colors.RESET}")
        return 1
    elif warnings:
        print(f"\n{Colors.YELLOW}Bootstrap validation PASSED with warnings. "
              f"Review {len(warnings)} warning(s).{Colors.RESET}")
        return 0
    else:
        print(f"\n{Colors.GREEN}Bootstrap validation PASSED. "
              f"All documents are clean.{Colors.RESET}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
