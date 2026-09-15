# 6. Fluids & Capacities

## Status

Populated from the **7.3L gasoline** capacity tables of the 2024 Super Duty Owner's Manual (REF-001, v1.1, edition 202307, pp. 520-545). Diesel and 6.8L values are excluded.

The **rear axle is resolved**: it is an 11.6 in axle, identified from its tag on 11 September 2026. The **transmission capacity** and **front axle type** now come from the 2024 F-350 **Workshop Service Manual (REF-028)**, received 15 September 2026.

> **Do not substitute across similar-sounding fluids.** The transmission takes MERCON **ULV**; the transfer case and hydraulic power steering take MERCON **LV**. Ford's note is explicit: use only MERCON ULV where MERCON ULV is required, as any other fluid could cause transmission damage.

## Capacities and specifications

| System | Capacity | Specification | Motorcraft product |
| --- | --- | --- | --- |
| Engine oil (including filter) | **8.0 qt (7.57 L)** | WSS-M2C961-A1, SAE 5W-30 | XO-5W30-Q1SP / XO-5W30-Q1FS |
| Engine oil - extreme cold | 8.0 qt (7.57 L) | WSS-M2C963-A1, SAE 0W-30 | Recommended where ambient reaches -22°F (-30°C) or below |
| Cooling system | **22.5 qt (21.3 L)** | WSS-M97B57-A2 | Motorcraft Yellow Prediluted Antifreeze/Coolant, VC-13DL-G |
| Fuel tank (176" wheelbase) | **48.0 gal (181.7 L)** | Minimum 87 octane | Larger tank tied to this truck's 176" wheelbase |
| Automatic transmission (10R140) | **18.2 qt (17.22 L)** - approximate **dry fill**; a fluid change takes less (REF-028) | WSS-M2C949-A, MERCON **ULV** | XT-12-QULV |
| Transfer case | **1.9 qt (1.8 L)** | WSS-M2C938-A, MERCON **LV** | XT-10-QLVC |
| Brake fluid | Fill as required | WSS-M6C65-A2, DOT 4 LV (or ISO 4925 Class 6) | PM-20 |
| Hydraulic power steering | Fill as required | WSS-M2C938-A, MERCON **LV** | XT-10-QLVC |
| Air conditioning refrigerant | 27 oz (0.765 kg) | WSH-M17B19-A, R-134a | YN-19 |
| A/C refrigerant compressor oil | 3.7 fl oz (110 ml) | WSH-M1C231-B, PAG | YN-12-D |
| Washer fluid | Fill as required | WSS-M14P19-A | ZC-32-B2 |

Engine oil: Ford recommends Motorcraft motor oil, or an oil of the recommended viscosity grade displaying the API Certification Mark for gasoline engines. **Do not use supplemental engine oil additives** - Ford states they are unnecessary and could cause engine damage not covered by warranty.

Coolant: use **prediluted** coolant. Ford warns that concentrated coolant added without dilution will not flow correctly through the small passages of the engine cooling system.

## Front axle - Dana M235, 9.25 in

**Resolved from the Workshop Service Manual (REF-028), 15 September 2026.** The WSM describes the F-250/F-350 front drive axle as a **Dana M235**, in conventional or limited-slip form; its fluid table lists that as the **9.25 in** 4WD front axle. The **10.08 in** applies to the F-450/F-550/F-600 front axle, not this truck. The axle identification is pin-stamped on the differential cover plate.

| Variant | Capacity | Specification | Motorcraft product |
| --- | --- | --- | --- |
| Front axle 9.25 (4WD, without limited slip) | 2.20 qt (2.08 L) | WSP-M2C197-A, SAE 80W-90 | XY-80W90-QL |
| Front axle 9.25 (4WD, with limited slip) | 2.20 qt (2.08 L) including friction modifier | WSP-M2C197-A + EST-M2C118-A | Add 4.4 fl oz (130 ml) XL-3 within the 2.2 qt total |
| Front axle 10.08 | 2.75 qt (2.6 L) | WSP-M2C197-A, SAE 80W-90 | XY-80W90-QL |

**Conventional or limited slip?** The window sticker (REF-003) lists no limited-slip front axle option, so it is **most likely conventional**. The capacity is 2.20 qt either way; the only difference is the 4.4 fl oz of XL-3 friction modifier a limited-slip axle needs. Confirm from the pin-stamped ID on the front differential cover before the first service.

## Rear axle - 11.6 in, confirmed

**Identified 11 September 2026** from the owner's photos of the axle tag (IMG_1548-1557). The tag is a white and yellow bar-code label wrapped around the passenger-side rear axle tube, beside the differential. It reads:

```
…467B 23 007025
TC05A 4E30 - 11.6
```

- **`4E30`** - a 4.30 ratio with the electronic locker (the `E`). This matches the window sticker's `4.30 ELECTRONIC-LOCKING AXLE` (REF-003).
- **`11.6`** - the ring gear size, 11.6 in.
- The housing casting is marked **`RFPC3H-4025AC`** (IMG_1557-1558).

The door label's axle code **`4M`** (REF-023) and the **7,230 lb rear GAWR** are consistent with this axle.

| Rear axle 11.6 | Capacity | Specification | Motorcraft product |
| --- | --- | --- | --- |
| **4.30 final drive ratio - this truck** | **4.44-4.54 qt (4.2-4.3 L)** | WSL-M2C192-A, **SAE 75W-140 synthetic** | XY-75W140-QL |
| Other ratios (3.31/3.55/3.73) - for reference | 4.33-4.44 qt (4.1-4.2 L) | WSL-M2C192-A | XY-75W140-QL |

Source: REF-001, "Rear Axle - 11.6", p. 542. Unlike the manual's limited-slip entries, this one lists **no friction modifier additive**.

> **Three Ford sources give three capacities for this axle.** Owner's Manual: **4.44-4.54 qt**. WSM quick-lookup fluid table: **3.65-3.80 qt**. WSM 11.6 in axle specifications, electronic locker with 4.30 ratio: **4.12 qt (3.9 L)**. The axle-specific WSM figure is the most specific of the three, so **use 4.12 qt**. All three agree on SAE 75W-140 synthetic, WSL-M2C192-A.

**Do not fill to the fill plug.** The WSM's differential fluid level check warns that the 11.6 in axle's fill hole is too low for the capacity it needs. The procedure is:

1. Remove the differential housing cover and drain the fluid.
2. Reinstall the cover.
3. Disconnect the electronic locking differential (ELD) connector and remove the ELD connector adaptor bolt.
4. Add the measured amount, 4.12 qt, through the adaptor hole.
5. Reinstall the adaptor and torque its bolt to **133 lb-in (15 Nm)**, then reconnect the ELD connector.

A shop that tops up to the fill plug will leave the axle underfilled.

**The 75W-140 synthetic also settles the towing exception** in [chapter 3](03-oem-parts-catalog.md). If the axle holds WSL-M2C192-A 75W-140 synthetic, as Ford specifies for it, the 30,000 mi towing change interval is **waived** and the 150,000 mi interval applies. When the axle is serviced, make sure the refill is 75W-140 synthetic, not the 75W-85 some other Super Duty axles take.

> **Correction, 11 September 2026.** This chapter previously listed only four rear axle families and short-listed the 10.5 and the 11.8 single-rear-wheel axles as the likely fits. The owner's manual actually lists six rear axles: 10.5, 10.8, **11.6**, 11.8 light/heavy duty, 11.8 single-rear-wheel and 12.4. The 11.6, the one fitted, had been missed.

## Fluid level checks

Included in the multi-point inspection at every scheduled maintenance interval: brake, coolant recovery reservoir, automatic transmission, and window washer.

Ford notes that under high-load operation - extended high engine speed, heavy loads, engine braking, hard cornering, track or off-road use - oil consumption of approximately **1 quart per 500 miles** is possible. Check engine oil at every refueling under those conditions. Towing a fifth-wheel qualifies.

## Open items

- ~~Transmission fluid capacity~~ - **resolved**: 18.2 qt dry fill (REF-028).
- ~~Front axle assembly~~ - **resolved**: Dana M235, 9.25 in (REF-028). Still to confirm: conventional or limited slip, from the pin-stamped ID on the cover.
- Rear axle capacity conflict between the Owner's Manual and the WSM - working to the WSM's 4.12 qt; see above.

### How the rear axle was identified

| Source | Result |
| --- | --- |
| Window sticker (REF-003) | Ratio and locker only (`4.30 ELECTRONIC-LOCKING AXLE`) |
| Door jamb label (REF-023) | Axle code `4M` and the GAWRs. Misread as `G` until 11 September 2026; `G` is the transmission code |
| **Axle tag** | **`4E30 - 11.6`**, which settles it. The 4 September photos showed only the bar-code side; the 11 September photos show the printed side |
| Owner's Manual (REF-001) | The capacity and specification for the 11.6 axle at 4.30 |
| Workshop Service Manual (REF-028) | Confirms axle code `4M` = **4.30 ratio, electronic locking differential**; gives the 4.12 qt axle-specific capacity and the ELD-hole fill procedure |
| Camper Loading Guide (REF-002), Wheel / Tire Kit (REF-010) | No axle identification |
