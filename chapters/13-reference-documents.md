# 13. Reference Documents

## Holdings

The two **VIN-specific records** - the window sticker and the CARFAX - are committed to [`references/`](../references/). Everything else is a **Ford publication**, held locally in `imports/truck-f350/` (gitignored) rather than committed, since redistributing Ford's copyrighted manuals is not ours to do. This chapter is the authoritative catalog either way.

**Status legend:** *In repo* = committed under `references/`. *Held* = present locally in `imports/`, not committed. *Catalogued only* = referenced but no copy retained.

## Source library

| ID | Document | Local filename | Pages | Classification / purpose | Status |
| --- | --- | --- | --- | --- | --- |
| REF-001 | 2024 Ford Super Duty Owner's Manual, v1.1 EN-US | `2024_Ford_Super_Duty_Owners_Manual_version_1.1_om_EN-US.pdf` | 711 | Ford OEM; operation, maintenance, specifications, safety | Held |
| REF-002 | 2024 Ford Camper Loading Guide | `2024MYCamperLoading8223.pdf` | 138 | Ford OEM; payload, axle loading, center of gravity | Held |
| REF-003 | Window sticker / build sheet | [`references/REF-003-window-sticker.pdf`](../references/REF-003-window-sticker.pdf) | 1 | VIN-specific; verified build data, options, MSRP, warranty | **In repo** |
| REF-004 | Original dealer advertisement | - | - | VIN-specific archive; preserve factual metadata and photos | Catalogued only |
| REF-005 | Vehicle photos | `IMG_1374` - `IMG_1468` (95 files) | - | VIN-specific documentation; captured 2026-09-05 | Held |
| REF-006 | 2024 Super Duty Quick Reference Guide | `2024_Super_Duty_QRG_English.pdf` | 28 | Ford OEM; operating quick reference | Held |
| REF-007 | 2023 Super Duty Fifth-Wheel Hitch Owner Manual & Installation | `2023_CMY_Super_Duty_5th_Wheel_Hitch_Owner_Manual_and_Installation.pdf` | 90 | Ford OEM; hitch operation, parts, installation guidance | Held |
| REF-008 | Rear Camera Kit Enable/Disable Procedure | `2020_P558_Rear_Camera_Kit_Enable_Disable.pdf` | 2 | Ford service procedure; APIM/BCM configuration | Held |
| REF-009 | Spare Tire Lock (F-150 / Ranger) | `2024_CMY_F150_Ranger_Spare_Tire_Lock.pdf` | 7 | Reference; retain with vehicle security documents. **Note:** covers F-150/Ranger, not Super Duty - confirm applicability | Held |
| REF-010 | Wheel / Tire Kit installation instruction (SKM2DJ-1K007-AA) | `WHEEL_TIRE_KIT.pdf` | 10 | Generic Ford **accessory** wheel/tire kit sheet, © 2020, specifying **P275/55R20**. **Does not match this truck** (LT275/70R18E load range E all-terrain), is not VIN-specific, and contains no axle data. Useful only for its TPMS wake-up and speedometer recalibration notes | Held |
| REF-011 | 2024 Super Duty Quick Start Guide | `24M_Super_Duty_QSG_ENG_V1.pdf` | 24 | Ford OEM quick-start reference | Held |
| REF-012 | 2024 Wrecker Towing Guide | `2024_Wrecker_Towing_Guide.pdf` | 13 | Ford reference; recovery/towing guidance | Held |

## Accessory and kit documentation

Added with the September 2026 import. These were not in the Edition 1.0 catalog.

| ID | Document | Local filename | Pages | Relevance |
| --- | --- | --- | --- | --- |
| REF-013 | Super Duty Trailer Camera & TPMS Kits (SKPC3J-14A350-AA) | `SKPC3J-14A350-AA_2024-CMY_Super_Duty_Trailer_Camera_and_Tire_Pressure_Monitoring_System_TPMS_Kits.pdf` | 87 | Trailer camera and trailer TPMS retrofit; wiring and configuration |
| REF-014 | Super Duty Trailer 360 Camera System Kit (SKPC3J-13A974-C) | `2023_CMY_F_Super_Duty_Trailer_360_Camera_System_Kit_SKPC3J_13A974_C_1_1.pdf` | 79 | Extends the factory 360-degree package to the trailer |
| REF-015 | Trailer Blind Spot Monitoring for 5th Wheel & Gooseneck (SKPC3J-13A973-AA) | `SKPC3J-13A973-AA_2024-CMY_Super_Duty_Trailer_Blind_Spot_Monitoring_for_5th_Wheel_and_Gooseneck_Kit.pdf` | 30 | Directly applicable - truck has BLIS and fifth-wheel prep |
| REF-016 | Super Duty Rear View Mirror Camera | `2020_CMY_Super_Duty_Rear_View_Mirror_Camera_1_28_2026_FINAL.pdf` | 30 | Mirror-camera install/configuration |
| REF-017 | Remote Start (2024) | `2024_Remote_Start_9_20_2023_FINAL.pdf` | 54 | Truck has factory Remote Start System |
| REF-018 | Wireless RF Keypad Instructions (SKES7J-19G544-AC) | `2020_CMY_Wireless_RF_Keypad_Instructions_SKES7J_19G544_AC.pdf` | 44 | Keypad entry; truck has SecuriCode keypad |
| REF-019 | Super Duty Chassis Cab Pro Power Onboard v2 | `2023_CMY_Super_Duty_Chassis_Cab_Pro_Power_Onboard_v2.pdf` | 11 | **Chassis cab** document - not this truck's configuration; retained for reference only |
| REF-020 | Quick Start Guide with FCC verbiage (11/2024) | `Quickstart_Guide_with_FCC_Verbiage_11_2024.pdf` | 3 | Accessory FCC/regulatory statements |
| REF-021 | Dealer listing images | 17 files (`*.avif`, `*.webp`) | - | Listing photography; pairs with REF-004 |
| REF-023 | Safety Compliance Certification Label (door jamb), photographed 8 Sep 2026 | - | 1 | VIN-specific; **GVWR, front and rear GAWR, axle code, paint and trim codes, tire pressures**. Transcribed into [chapter 1](01-vehicle-information.md) | Photo, to file |
| REF-024 | Tire and Loading Information Label (door jamb), photographed 8 Sep 2026 | - | 1 | VIN-specific; **payload 4,566 lb**, seating capacity, tire pressures | Photo, to file |
| REF-025 | CAT Scale ticket 1132726251630, 8 Sep 2026 | - | 1 | Truck-only axle weights; basis for the margins in [chapter 10](10-fifth-wheel-and-towing.md) and the [scale weights log](../logs/scale-weights.md) | To file |
| REF-022 | CARFAX Vehicle History Report, run 2026-09-05 | [`references/REF-022-carfax-report.pdf`](../references/REF-022-carfax-report.pdf) | 11 | VIN-specific; title, ownership, buyback disclosure, 15 service records. Basis for [chapter 14](14-vehicle-history-and-title.md) |

## Future source intake

Add the Ford Workshop Manual and wiring excerpts as sourced material becomes available. Record publication date, section, vehicle applicability, and any superseding publication.

Still missing after the September 2026 import: the **Ford Workshop Manual** (the single largest gap - see [Appendix A](appendix-a-workshop-manual-intake.md)), the original dealer advertisement (REF-004), and Motorcraft parts documentation for chapter 3.

### Documents that do not apply to this truck

Three held documents cover other vehicles or configurations. They are retained for reference but must not be used as specifications for this VIN:

| ID | Why it does not apply |
| --- | --- |
| REF-009 | Spare tire lock for F-150 / Ranger, not Super Duty |
| REF-010 | Accessory wheel/tire kit for P275/55R20; this truck runs LT275/70R18E |
| REF-019 | Pro Power Onboard for chassis cab, not this pickup configuration |

**Now a priority given the buyback:** the Ford repair orders from the reacquisition period, and any Field Service Action or recall history by VIN. CARFAX records that Ford took the truck back and why, but not what was attempted or fixed. See [chapter 14](14-vehicle-history-and-title.md).
