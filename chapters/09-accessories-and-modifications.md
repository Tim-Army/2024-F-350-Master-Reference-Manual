# 9. Accessories & Modifications

## Planned roadmap

| Phase | Planned items |
| --- | --- |
| Immediate | Sam's Club Plus membership (military discount); Michelin Defender LTX M/S2 tires; Covercraft Spacer Mesh PrecisionFit covers (front EM / rear AU); lace-on leather steering-wheel cover |
| Protection | Wheel-well liners; window deflectors; mud flaps; sill protection; LampGard; paint protection film; TowTector; tailgate lock; Console Vault |
| Towing | B&W; Companion OEM fifth-wheel hitch; 7-way extension/adapters; plug tester; chocks; levelers; infrared thermometer |
| Storage | Dee Zee under-seat drawer; bed cover (8-foot compatibility needs vendor confirmation); console and modular 3D-printed organizers |
| Maintenance / security | Grease tools, dielectric grease, cleaning supplies, spare adapters/pins; coupler/wheel locks and security cable |

## Timbren - suspension and brake enhancement

Vendor fitment search for this truck (2024 F-350 Super Duty, 4WD, XLT):
<https://timbren.com/search?Year/2024/Make/Ford/Model/F350-Super-Duty/Drive-Wheel/4WD/More-Info/XLT>

Ten products list for this configuration. Prices are USD as listed on 6 September 2026 and will drift - reconfirm before ordering.

### Suspension Enhancement System (SES)

Rubber progressive-rate helper springs. Relevant to the fifth-wheel use case: they resist squat and sway under pin weight.

| SKU | Product | Fitment | Price |
| --- | --- | --- | --- |
| `FR350SDJ` | Rear SES Suspension Kit | F-350 Super Duty, 2017-present | $468.32 |
| `FRTT350J` | Rear SES **Severe-Service** Suspension Kit | F-250/F-350 2017-present; F-450 2015-present | $468.32 |
| `FF350SDC` | Front SES Suspension Kit | F-250/F-350 Super Duty 4WD, 2005-present | $316.90 |

The two rear kits are the same price; the severe-service variant is the heavier-duty option and the one to evaluate first for sustained fifth-wheel towing.

> **A helper spring does not raise payload.** SES kits support and level a load - they do not increase GVWR, GAWR, or the cargo weight rating. The payload ceiling in [chapter 10](10-fifth-wheel-and-towing.md) is unchanged by fitting one, and the truck's door label remains the legal limit.

### Spacer kits (lifted trucks only)

Needed only if the truck is lifted. This truck is at factory ride height, so **none of these apply** unless that changes.

| SKU | For kit | Price |
| --- | --- | --- |
| `SPCRTORTTN` | FR350SDJ (and FERSDLB, TORTTN) | $62.43 |
| `SPCRDR2500D` | FRTT350J (and DR2500D, DRTT3500E) | $62.43 |
| `SPCRFF350SDC` | FF350SDC | $62.43 |

### Brake Enhancement System (BES)

| SKU | Product | Fitment | Price |
| --- | --- | --- | --- |
| `BES-20FB059` | Front BES Brake Kit | F-250/F-350 4WD, 2023-present | $616.45 |
| `TIM-D2490SD` | Front BES Brake Pads | F-250/F-350, 2023-present | $114.03 |
| `TIM-D2491SD` | Rear BES Brake Pads | F-250/F-350, 2023-present | $92.09 |
| `TIM-R207305` | Front BES Rotor | F-250/F-350 4WD, 2013-present | $251.21 |

Brake work bears on the service history in [chapter 14](14-vehicle-history-and-title.md): brakes were checked at six separate dealer visits between 10,914 and 35,930 miles. Establish the current pad and rotor condition before deciding between pads alone and the full front kit.

**Before ordering any of these**, confirm fitment against the truck's actual configuration - Timbren's fitment filter does not know about the FX4 package, the snowplow/camper package front springs, or the 11,900 lb GVWR package.

## Wheel and tire changes

The truck runs **LT275/70R18E BSW all-terrain** from the factory (REF-003). The planned Michelin Defender LTX M/S2 replacement should match that size and load range E; anything else changes the loading math in [chapter 10](10-fifth-wheel-and-towing.md).

If a tire size does change, two steps follow (REF-010):

- **Speedometer recalibration.** The PCM may need recalibrating through Ford diagnostic software - see [chapter 8](08-forscan-and-module-programming.md) and log the change there.
- **TPMS sensor wake-up**, so the sensors transmit current pressures. Ford specifies special service tool 204-D081A (204-D081), starting at the left front valve stem with the ignition on.

## Accessory installation record

For each installed item, capture manufacturer, part number, vendor, date, cost, photos, torque/wiring instructions, installation notes, warranty, and removal process.

See [logs/accessory-log.md](../logs/accessory-log.md) for the running record.
