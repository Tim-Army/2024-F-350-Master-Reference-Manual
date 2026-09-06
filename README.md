# 2024 F-350 Master Reference Manual

VIN-specific ownership, towing, and service reference for a 2024 Ford F-350 Super Duty.

**Edition 1.0 - September 2026.** This is a living reference, compiled from the established project conversation and the listed Ford documents. It **summarizes rather than reproduces** source manuals. Values marked *Confirm with Ford WSM* are intentionally not service instructions until verified.

:warning: **Read [chapter 14](chapters/14-vehicle-history-and-title.md) first.** This truck is a Ford manufacturer buyback, reacquired 2026-07-01 over a passenger-window fault and **Cross Traffic / Blind Spot sensors that do not operate correctly**. Neither defect is shown as repaired. Odometer 38,278 mi; bumper-to-bumper warranty expired.

## Vehicle

| Vehicle | Value |
| --- | --- |
| VIN | 1FT8W3BNXRED73946 |
| Model year | 2024 |
| Vehicle | Ford F-350 SRW 4X4 Crew Cab, XLT, 176" WB Styleside |
| Assembly plant | Kentucky Truck Plant, Louisville, Kentucky |
| Engine | 7.3L DEVCT NA PFI gasoline V8, 10-speed TorqShift |
| Bed / towing context | 8-foot bed; factory 5th Wheel Hitch Prep Package, Gooseneck Hitch Kit, 360-Degree Camera Package, and BLIS (verified on window sticker) |
| Axle / GVWR | 4.30 electronic-locking; 11,900 lb GVWR package |
| Odometer / title | 38,278 mi; manufacturer buyback (see chapter 14) |

## How to use this manual

- Navigate by chapter using the contents below.
- Treat *Ford OEM* as a source classification, not a substitute for consulting the original document for complete warnings and procedures.
- Record installed accessories, maintenance, scale weights, and module backups in the [logs](logs/) as work is performed.

## Confidence labels

| Label | Meaning |
| --- | --- |
| Ford OEM | Official Ford publication |
| Recorded | Project-specific information |
| Planned | Intended purchase or work |
| Confirm with Ford WSM | Not yet validated against current service information - do not act on it as a specification |

## Contents

| # | Chapter |
| --- | --- |
| 1 | [Vehicle Information](chapters/01-vehicle-information.md) |
| 2 | [Factory Build & Operation](chapters/02-factory-build-and-operation.md) |
| 3 | [OEM Parts Catalog](chapters/03-oem-parts-catalog.md) |
| 4 | [Maintenance & Service Log](chapters/04-maintenance-and-service-log.md) |
| 5 | [Torque Specifications](chapters/05-torque-specifications.md) |
| 6 | [Fluids & Capacities](chapters/06-fluids-and-capacities.md) |
| 7 | [Electrical Atlas](chapters/07-electrical-atlas.md) |
| 8 | [FORScan & Module Programming](chapters/08-forscan-and-module-programming.md) |
| 9 | [Accessories & Modifications](chapters/09-accessories-and-modifications.md) |
| 10 | [Fifth-Wheel & Towing](chapters/10-fifth-wheel-and-towing.md) |
| 11 | [Troubleshooting](chapters/11-troubleshooting.md) |
| 12 | [3D-Printed Accessories](chapters/12-3d-printed-accessories.md) |
| 13 | [Reference Documents](chapters/13-reference-documents.md) |
| 14 | [Vehicle History & Title](chapters/14-vehicle-history-and-title.md) |
| A | [Appendix A. Future Workshop Manual Intake](chapters/appendix-a-workshop-manual-intake.md) |

## HTML edition

`manual.html` is a single-page HTML build of the whole manual - all 14 chapters, Appendix A, and the four running records, with a chapter rail and cross-links resolved to on-page anchors. Rebuild it after editing any Markdown source:

```bash
python3 build-html.py
```

It requires `pandoc`. `template.html` holds the page shell and styling; the generator only fills in the navigation and body.

## Repository layout

```
chapters/     One Markdown file per manual chapter
logs/         Fillable running records (service, modules, accessories, scale weights)
references/   Notes on the REF-0NN source library
source/       The compiled PDF this repository was scaffolded from
imports/      Local-only staging for uploaded material (gitignored)

build-html.py   Generates manual.html from the Markdown sources
template.html   Page shell and styling for the HTML edition
manual.html     Built single-page HTML edition
```

Ford publications are held locally in `imports/` and cited in
[chapter 13](chapters/13-reference-documents.md) rather than committed.

## Chapter status

Chapters 3, 6, and much of 5, 7, and 11 are deliberate placeholders. They are populated from the Ford Workshop Manual as it is acquired - see [Appendix A](chapters/appendix-a-workshop-manual-intake.md) for the intake list.

## Revision record

| Version | Date | Summary |
| --- | --- | --- |
| 1.0 | September 2026 | Initial compiled reference; placeholders retained for WSM data |
| 1.1 | September 2026 | Ford document library imported (REF-013 - REF-021); build data verified from window sticker |
| 1.2 | September 2026 | CARFAX imported (REF-022); chapter 14 added; manufacturer buyback recorded; service history populated |
