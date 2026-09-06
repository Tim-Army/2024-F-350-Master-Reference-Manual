# 6. Fluids & Capacities

## Status

Populated from the **7.3L gasoline** capacity tables of the 2024 Super Duty Owner's Manual (REF-001, v1.1, edition 202307, pp. 520-545). Diesel and 6.8L values are excluded.

Two items remain **configuration-dependent** and are not yet resolved for this VIN - the front and rear axle assemblies. Both are flagged below.

> **Do not substitute across similar-sounding fluids.** The transmission takes MERCON **ULV**; the transfer case and hydraulic power steering take MERCON **LV**. Ford's note is explicit: use only MERCON ULV where MERCON ULV is required, as any other fluid could cause transmission damage.

## Capacities and specifications

| System | Capacity | Specification | Motorcraft product |
| --- | --- | --- | --- |
| Engine oil (including filter) | **8.0 qt (7.57 L)** | WSS-M2C961-A1, SAE 5W-30 | XO-5W30-Q1SP / XO-5W30-Q1FS |
| Engine oil - extreme cold | 8.0 qt (7.57 L) | WSS-M2C963-A1, SAE 0W-30 | Recommended where ambient reaches -22°F (-30°C) or below |
| Cooling system | **22.5 qt (21.3 L)** | WSS-M97B57-A2 | Motorcraft Yellow Prediluted Antifreeze/Coolant, VC-13DL-G |
| Fuel tank (176" wheelbase) | **48.0 gal (181.7 L)** | Minimum 87 octane | Larger tank tied to this truck's 176" wheelbase |
| Automatic transmission (10R140) | Not published in the owner's manual | WSS-M2C949-A, MERCON **ULV** | XT-12-QULV |
| Transfer case | **1.9 qt (1.8 L)** | WSS-M2C938-A, MERCON **LV** | XT-10-QLVC |
| Brake fluid | Fill as required | WSS-M6C65-A2, DOT 4 LV (or ISO 4925 Class 6) | PM-20 |
| Hydraulic power steering | Fill as required | WSS-M2C938-A, MERCON **LV** | XT-10-QLVC |
| Air conditioning refrigerant | 27 oz (0.765 kg) | WSH-M17B19-A, R-134a | YN-19 |
| A/C refrigerant compressor oil | 3.7 fl oz (110 ml) | WSH-M1C231-B, PAG | YN-12-D |
| Washer fluid | Fill as required | WSS-M14P19-A | ZC-32-B2 |

Engine oil: Ford recommends Motorcraft motor oil, or an oil of the recommended viscosity grade displaying the API Certification Mark for gasoline engines. **Do not use supplemental engine oil additives** - Ford states they are unnecessary and could cause engine damage not covered by warranty.

Coolant: use **prediluted** coolant. Ford warns that concentrated coolant added without dilution will not flow correctly through the small passages of the engine cooling system.

## Front axle - confirm which is fitted

The owner's manual publishes two front axle variants. This truck is 4X4, but the assembly is not identified on the window sticker.

| Variant | Capacity | Specification | Motorcraft product |
| --- | --- | --- | --- |
| Front axle 9.25 (4WD, without limited slip) | 2.20 qt (2.08 L) | WSP-M2C197-A, SAE 80W-90 | XY-80W90-QL |
| Front axle 9.25 (4WD, with limited slip) | 2.20 qt (2.08 L) including friction modifier | WSP-M2C197-A + EST-M2C118-A | Add 4.4 fl oz (130 ml) XL-3 within the 2.2 qt total |
| Front axle 10.08 | 2.75 qt (2.6 L) | WSP-M2C197-A, SAE 80W-90 | XY-80W90-QL |

**Confirm the axle before filling.** The window sticker (REF-003) was reviewed and does **not** identify the axle assembly - it carries only the `4.30 ELECTRONIC-LOCKING AXLE` option line, which gives the ratio and the locker but not the ring gear size. Identify instead from the **axle tag** (on the differential cover) or the **axle code on the door jamb Safety Compliance Certification Label**.

## Rear axle - confirm which is fitted

The truck has a **4.30 electronic-locking** rear axle (verified, REF-003), which narrows the options but does not resolve the ring gear size. Four rear axle families appear in the manual; the two consistent with an electronic locker are:

| Variant | Capacity | Specification |
| --- | --- | --- |
| Rear axle 10.5, with electronic locking differential | 3.3-3.5 qt (3.1-3.3 L) | WSS-M2C942-A, SAE 75W-85 synthetic hypoid (XY-75W85-QL) |
| Rear axle 11.8 single rear wheel, electric locking differential | 4.05 qt (3.83 L) | WSL-M2C192-A, SAE 75W-140 synthetic (XY-75W140-QL) |

This is an SRW truck, which points toward one of these two - but **the specification differs between them (75W-85 vs 75W-140), not just the quantity.** The towing interval exception in [chapter 3](03-oem-parts-catalog.md) also depends on which fluid is in the axle.

**The window sticker cannot settle this** - see the front axle note above. The door jamb label is the document to photograph: it carries the axle code *and* both Gross Axle Weight Ratings, closing this gap and the loading gap in [chapter 10](10-fifth-wheel-and-towing.md) at the same time.

For reference, the other published variants (not expected on this truck): rear axle 11.8 light/heavy duty, 4.21 qt open or 3.95 qt limited slip; rear axle 12.4, 4.65 qt limited slip.

## Fluid level checks

Included in the multi-point inspection at every scheduled maintenance interval: brake, coolant recovery reservoir, automatic transmission, and window washer.

Ford notes that under high-load operation - extended high engine speed, heavy loads, engine braking, hard cornering, track or off-road use - oil consumption of approximately **1 quart per 500 miles** is possible. Check engine oil at every refueling under those conditions. Towing a fifth-wheel qualifies.

## Open items

- Automatic transmission fluid **capacity** is not published in the owner's manual, and is **not** on the window sticker. It requires the Workshop Manual - see [Appendix A](appendix-a-workshop-manual-intake.md).
- Front and rear axle assemblies to be identified from the axle tag or door jamb label, then the tables above reduced to the single applicable row.

### Sources checked and ruled out

Every held document that could plausibly carry the axle identification has now been searched. None does.

| Document | Result |
| --- | --- |
| Window sticker (REF-003) | Ratio and locker only (`4.30 ELECTRONIC-LOCKING AXLE`); no assembly ID, no GAWR, no fluid capacities |
| Owner's Manual (REF-001) | All capacities except the transmission; axle variants listed generically, never tied to a VIN |
| Camper Loading Guide (REF-002) | Loading document only. Contains no gear ratios and no ring gear sizes; every reference to an axle is either a weight rating or the electronic-locking differential's option weight. Does supply front GAWR and cargo ratings - see [chapter 10](10-fifth-wheel-and-towing.md) |
| Wheel / Tire Kit (REF-010) | Generic 2020 accessory sheet for P275/55R20; not applicable to this truck and contains no axle data |

**Remaining sources, in order of ease:**

1. **Door jamb Safety Compliance Certification Label** - carries the axle code and both GAWRs. One photograph closes this and the [chapter 10](10-fifth-wheel-and-towing.md) loading gap together.
2. **Axle tag** on the differential cover - stamped with the assembly and ratio.
3. Ford Workshop Manual or a dealer VIN lookup.
