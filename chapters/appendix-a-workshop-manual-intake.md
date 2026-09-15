# Appendix A. Future Workshop Manual Intake

## Required additions

- ~~Full verified torque atlas~~ - **service, chassis and towing torques extracted** into [chapter 5](05-torque-specifications.md), 15 September 2026. Engine and transmission internals, HVAC and trim still to extract as needed.
- ~~VIN-correct fluid capacities, Motorcraft product specifications, service intervals~~ - now sourced from the Owner's Manual into [chapter 3](03-oem-parts-catalog.md) and [chapter 6](06-fluids-and-capacities.md). **WSM received 15 September 2026 (REF-028).** Resolved from it: transmission capacity (**18.2 qt dry fill**), front axle (**Dana M235, 9.25 in**), axle code `4M` and transmission code `G` decodes, and the **11.6 in rear axle fill procedure** (drain, then fill 4.12 qt through the ELD adaptor hole). **Not in the WSM: GCWR** - sourced instead from the Towing Guide (REF-029): 29,000 lb.
- Wiring diagrams, connector views, fuse/relay functions, diagnostic tests, and module/programming references.
- OEM parts diagrams and Ford/Motorcraft part numbers.
- Service Bulletins, recalls, customer-satisfaction programs, and revision history.

## Source - received

The **2023-2025 F-350 Super Duty 7.3L workshop manual** arrived on 15 September 2026 and is catalogued as **REF-028**. It is an HTML compilation of Ford service information, about 39,000 pages, with a Repair and Diagnosis tree, a single-page version for searching, and labor times. It is held in `imports/` and not committed.

It is labelled for the Platinum trim but states it is identical for the other 7.3L variants. **It is not VIN-specific**, so check option-dependent entries against this truck's build.

Torque atlas extracted into [chapter 5](05-torque-specifications.md). Still to mine: wiring for [chapter 7](07-electrical-atlas.md) and service procedures. GCWR is not in the WSM; it came from the Towing Guide (REF-029).

## Revision record

| Version | Date | Summary |
| --- | --- | --- |
| 1.0 | September 2026 | Initial compiled reference; placeholders retained for WSM data |
| 1.3 | September 2026 | Chapters 3 and 6 populated from REF-001; remaining WSM gaps narrowed |
| 1.7 | 15 September 2026 | WSM received (REF-028): transmission capacity, front axle, code decodes and rear axle fill procedure recorded in chapter 6 |
| 1.8 | 15 September 2026 | Torque atlas extracted into chapter 5 (provisional list corrected); GCWR 29,000 lb from the Towing Guide (REF-029) |
| | | |
