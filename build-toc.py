#!/usr/bin/env python3
"""Regenerate the README's Contents section from the Markdown sources.

Scans each chapter and log for its H1 title and H2 sections, and rewrites the
block between the CONTENTS markers in README.md. Run after adding or renaming
a section so the table of contents cannot drift from the manual.

Usage: python3 build-toc.py
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).parent
BEGIN, END = "<!--CONTENTS-->", "<!--/CONTENTS-->"

# (path, label shown in the # column)
ENTRIES = [
    ("chapters/01-vehicle-information.md",            "1"),
    ("chapters/02-factory-build-and-operation.md",    "2"),
    ("chapters/03-oem-parts-catalog.md",              "3"),
    ("chapters/04-maintenance-and-service-log.md",    "4"),
    ("chapters/05-torque-specifications.md",          "5"),
    ("chapters/06-fluids-and-capacities.md",          "6"),
    ("chapters/07-electrical-atlas.md",               "7"),
    ("chapters/08-forscan-and-module-programming.md", "8"),
    ("chapters/09-accessories-and-modifications.md",  "9"),
    ("chapters/10-fifth-wheel-and-towing.md",         "10"),
    ("chapters/11-troubleshooting.md",                "11"),
    ("chapters/12-3d-printed-accessories.md",         "12"),
    ("chapters/13-reference-documents.md",            "13"),
    ("chapters/14-vehicle-history-and-title.md",      "14"),
    ("chapters/15-fifth-wheel-candidates.md",         "15"),
    ("chapters/appendix-a-workshop-manual-intake.md", "A"),
]
LOGS = [
    ("logs/service-log.md",        "L1"),
    ("logs/module-change-log.md",  "L2"),
    ("logs/accessory-log.md",      "L3"),
    ("logs/scale-weights.md",      "L4"),
]


def slug(text: str) -> str:
    """GitHub's heading anchor: lowercase, strip punctuation, spaces to dashes."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    return re.sub(r"\s+", "-", s)


def parse(path: pathlib.Path):
    """Return (h1 title, [h2 section titles]) for one file."""
    title, sections = path.stem, []
    for line in path.read_text().splitlines():
        if line.startswith("# ") and title == path.stem:
            title = line[2:].strip()
        elif line.startswith("## "):
            sections.append(line[3:].strip())
    return title, sections


def strip_number(title: str) -> str:
    """'3. OEM Parts Catalog' -> 'OEM Parts Catalog'."""
    return re.sub(r"^(?:\d+\.|Appendix [A-Z]\.)\s*", "", title)


def rows(entries):
    out = []
    for rel, num in entries:
        path = ROOT / rel
        if not path.exists():
            sys.exit(f"missing: {rel}")
        title, sections = parse(path)
        out.append(f"| **{num}** | **[{strip_number(title)}]({rel})** |")
        for s in sections:
            out.append(f"| | [{s}]({rel}#{slug(s)}) |")
    return out


def build() -> str:
    lines = ["| # | Section |", "| --- | --- |"]
    lines += rows(ENTRIES)
    lines.append("| | |")
    lines.append("| | **Running records** |")
    lines += rows(LOGS)
    return "\n".join(lines)


if __name__ == "__main__":
    readme = ROOT / "README.md"
    text = readme.read_text()
    if BEGIN not in text:
        sys.exit(f"{BEGIN} marker not found in README.md")
    head, rest = text.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    readme.write_text(f"{head}{BEGIN}\n\n{build()}\n\n{END}{tail}")
    print(f"rewrote Contents ({len(build().splitlines()) - 2} rows)")
