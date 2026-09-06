#!/usr/bin/env python3
"""Build the single-page HTML edition of the master reference manual.

Reads the Markdown chapters and logs, converts each with pandoc, and wraps the
result in the manual's HTML template. Chapter anchors are namespaced (#c01,
#c14, #log-service) so cross-file links in the Markdown keep resolving on the
single page.

Usage: python3 build-html.py  ->  writes manual.html
"""
import html
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "manual.html"

# (source path, anchor id, rail number, rail label)
SECTIONS = [
    ("chapters/01-vehicle-information.md",            "c01", "01", "Vehicle Information"),
    ("chapters/02-factory-build-and-operation.md",    "c02", "02", "Factory Build &amp; Operation"),
    ("chapters/03-oem-parts-catalog.md",              "c03", "03", "OEM Parts Catalog"),
    ("chapters/04-maintenance-and-service-log.md",    "c04", "04", "Maintenance &amp; Service"),
    ("chapters/05-torque-specifications.md",          "c05", "05", "Torque Specifications"),
    ("chapters/06-fluids-and-capacities.md",          "c06", "06", "Fluids &amp; Capacities"),
    ("chapters/07-electrical-atlas.md",               "c07", "07", "Electrical Atlas"),
    ("chapters/08-forscan-and-module-programming.md", "c08", "08", "FORScan &amp; Programming"),
    ("chapters/09-accessories-and-modifications.md",  "c09", "09", "Accessories &amp; Mods"),
    ("chapters/10-fifth-wheel-and-towing.md",         "c10", "10", "Fifth-Wheel &amp; Towing"),
    ("chapters/11-troubleshooting.md",                "c11", "11", "Troubleshooting"),
    ("chapters/12-3d-printed-accessories.md",         "c12", "12", "3D-Printed Accessories"),
    ("chapters/13-reference-documents.md",            "c13", "13", "Reference Documents"),
    ("chapters/14-vehicle-history-and-title.md",      "c14", "14", "Vehicle History &amp; Title"),
    ("chapters/appendix-a-workshop-manual-intake.md", "apxa", "A", "Appendix A. WSM Intake"),
    ("logs/service-log.md",                           "log-service",   "L1", "Service Log"),
    ("logs/module-change-log.md",                     "log-module",    "L2", "Module Change Log"),
    ("logs/accessory-log.md",                         "log-accessory", "L3", "Accessory Record"),
    ("logs/scale-weights.md",                         "log-scale",     "L4", "Scale Weights"),
]

# Markdown file -> on-page anchor, for rewriting cross-references.
LINK_MAP = {pathlib.Path(src).name: anc for src, anc, _, _ in SECTIONS}


def convert(path: pathlib.Path) -> str:
    """Render one Markdown file to an HTML fragment via pandoc."""
    res = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html", str(path)],
        capture_output=True, text=True,
    )
    if res.returncode:
        sys.exit(f"pandoc failed on {path}: {res.stderr}")
    return res.stdout


def rewrite_links(frag: str) -> str:
    """Point inter-file Markdown links at their on-page anchors."""
    def sub(m):
        target = m.group(1).split("#")[0]
        name = pathlib.Path(target).name
        if name in LINK_MAP:
            return f'href="#{LINK_MAP[name]}"'
        if target.startswith("imports/") or target.startswith("../imports/"):
            # Local-only material: keep the path visible, but it is not a link.
            return 'href="#c13" class="local-ref"'
        return m.group(0)
    return re.sub(r'href="([^"#][^"]*\.md[^"]*)"', sub, frag)


def promote_headings(frag: str, anchor: str) -> str:
    """h1 -> section title; demote the rest so the page has one h1."""
    frag = re.sub(r"<h3\b", "<h4", frag)
    frag = re.sub(r"</h3>", "</h4>", frag)
    frag = re.sub(r"<h2\b", "<h3", frag)
    frag = re.sub(r"</h2>", "</h3>", frag)
    frag = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", frag, count=1, flags=re.S)
    return frag


def title_of(path: pathlib.Path) -> str:
    for line in path.read_text().splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def wrap_tables(frag: str) -> str:
    """Give every table its own horizontally scrollable container."""
    return re.sub(r"<table>(.*?)</table>",
                  r'<div class="tablewrap"><table>\1</table></div>',
                  frag, flags=re.S)


def status_chips(frag: str) -> str:
    """Tag the manual's own confidence vocabulary so it reads at a glance."""
    frag = frag.replace("Confirm with Ford WSM</td>",
                        '<span class="chip chip-caution">Confirm with Ford WSM</span></td>')
    frag = frag.replace(">Held</td>", '><span class="chip chip-ok">Held</span></td>')
    frag = frag.replace(">Catalogued only</td>",
                        '><span class="chip chip-muted">Catalogued only</span></td>')
    return frag


def build() -> str:
    nav, body = [], []
    for src, anchor, num, label in SECTIONS:
        path = ROOT / src
        if not path.exists():
            sys.exit(f"missing source: {src}")
        frag = wrap_tables(status_chips(rewrite_links(promote_headings(convert(path), anchor))))
        kind = "log" if anchor.startswith("log") else "chapter"
        if anchor == "log-service":
            nav.append('<li class="rail-sep">Running records</li>')
        nav.append(
            f'<li><a href="#{anchor}" data-anchor="{anchor}">'
            f'<span class="rail-num">{num}</span><span class="rail-label">{label}</span></a></li>'
        )
        body.append(
            f'<section class="section {kind}" id="{anchor}">\n'
            f'  <div class="section-head"><span class="section-num">{num}</span>'
            f'<h2>{html.escape(title_of(path)).replace("&amp;", "&")}</h2></div>\n'
            f'{frag}\n</section>'
        )
    tpl = (ROOT / "template.html").read_text()
    return tpl.replace("<!--NAV-->", "\n".join(nav)).replace("<!--BODY-->", "\n".join(body))


if __name__ == "__main__":
    OUT.write_text(build())
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
