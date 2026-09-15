# Appendix A. Future Workshop Manual Intake

## Required additions

- Full verified torque atlas, including sequences, torque-angle steps, and one-time-use fasteners.
- ~~VIN-correct fluid capacities, Motorcraft product specifications, service intervals~~ - now sourced from the Owner's Manual into [chapter 3](03-oem-parts-catalog.md) and [chapter 6](06-fluids-and-capacities.md). **WSM received 15 September 2026 (REF-028).** Resolved from it: transmission capacity (**18.2 qt dry fill**), front axle (**Dana M235, 9.25 in**), axle code `4M` and transmission code `G` decodes, and the **11.6 in rear axle fill procedure** (drain, then fill 4.12 qt through the ELD adaptor hole). **Not in the WSM: GCWR**.
- Wiring diagrams, connector views, fuse/relay functions, diagnostic tests, and module/programming references.
- OEM parts diagrams and Ford/Motorcraft part numbers.
- Service Bulletins, recalls, customer-satisfaction programs, and revision history.

## Source - received

The **2023-2025 F-350 Super Duty 7.3L workshop manual** arrived on 15 September 2026 and is catalogued as **REF-028**. It is an HTML compilation of Ford service information, about 39,000 pages, with a Repair and Diagnosis tree, a single-page version for searching, and labor times. It is held in `imports/` and not committed.

It is labelled for the Platinum trim but states it is identical for the other 7.3L variants. **It is not VIN-specific**, so check option-dependent entries against this truck's build.

Still to mine from it, in order: the torque atlas for [chapter 5](05-torque-specifications.md), wiring for [chapter 7](07-electrical-atlas.md), and service procedures. **GCWR is not in it**; source that from Ford's RV & Trailer Towing Guide.

## Revision record

| Version | Date | Summary |
| --- | --- | --- |
| 1.0 | September 2026 | Initial compiled reference; placeholders retained for WSM data |
| 1.3 | September 2026 | Chapters 3 and 6 populated from REF-001; remaining WSM gaps narrowed |
| 1.7 | 15 September 2026 | WSM received (REF-028): transmission capacity, front axle, code decodes and rear axle fill procedure recorded in chapter 6 |
| | | |
