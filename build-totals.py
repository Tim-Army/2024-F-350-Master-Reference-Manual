#!/usr/bin/env python3
"""Insert or refresh a total row at the foot of each phase table in chapter 9.

Sums the Price column of every row in a phase table, skipping rows whose Status
is Deferred and rows with no price. Where a price cell holds more than one
figure - "$62.20 + $8.97 shipping", "$328.99 ea / $1,315.96 set" - the largest
is taken, which is the item's own cost rather than a shipping charge or unit
price. Run after changing any price.

Usage: python3 build-totals.py
"""
import pathlib
import re
import sys

CHAPTER = pathlib.Path(__file__).parent / "chapters" / "09-accessories-and-modifications.md"
PHASES = ["Immediate", "Protection", "Towing",
          "Electronics and recording", "Storage", "Maintenance and security",
          # not a phase, but its table is totalled the same way
          "Researching"]
TOTAL_LABEL = "**Phase total**"
MONEY = re.compile(r"\$([\d,]+\.\d{2})")


def cells(line: str):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def price_of(cell: str):
    """Largest dollar figure in the cell, or None."""
    found = [float(m.replace(",", "")) for m in MONEY.findall(cell)]
    return max(found) if found else None


def main() -> None:
    lines = CHAPTER.read_text().splitlines()
    out, phase, changed = [], None, 0
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^###\s+(.*)$", line)
        if m:
            phase = m.group(1).strip() if m.group(1).strip() in PHASES else None
        elif line.startswith("##"):
            phase = None

        # A phase table starts at its header row; consume the whole table.
        if phase and line.startswith("|") and cells(line)[:1] == ["Item"]:
            table = []
            while i < len(lines) and lines[i].startswith("|"):
                table.append(lines[i])
                i += 1
            total = 0.0
            counted = 0
            for row in table[2:]:
                c = cells(row)
                if len(c) < 4 or c[0].startswith(TOTAL_LABEL):
                    continue
                status = c[2].replace("*", "").strip()
                if status == "Deferred":
                    continue
                p = price_of(c[1])
                if p is not None:
                    total += p
                    counted += 1
            table = [r for r in table if not cells(r)[0].startswith(TOTAL_LABEL)]
            n = len(cells(table[0]))
            amount = f"**${total:,.2f}**" if counted else "-"
            note = f"*{counted} items priced*" if counted else "*nothing priced yet*"
            row = f"| {TOTAL_LABEL} | {amount} | " + " | ".join(
                [note] + [""] * (n - 4)) + " |"
            table.append(row)
            out.extend(table)
            changed += 1
            print(f"{phase:<26} ${total:>10,.2f}  ({counted} items)")
            continue

        out.append(line)
        i += 1

    if not changed:
        sys.exit("no phase tables found - check the phase names")
    CHAPTER.write_text("\n".join(out) + "\n")
    print(f"\nupdated {changed} phase tables")


if __name__ == "__main__":
    main()
