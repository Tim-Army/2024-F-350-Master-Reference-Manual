# 10. Fifth-Wheel & Towing

## OEM fifth-wheel hitch guidance

- The Ford OEM fifth-wheel hitch reference supports use with an 8-foot pickup bed, matching the project-recorded truck configuration.
- Before working between truck and trailer: park transmission, apply parking brake, chock both sides of trailer wheels, and support landing gear. Keep body parts out from between truck and trailer whenever practical.
- Maximum allowable trailer weight is controlled by the lowest-rated component among truck, hitch, trailer, and related equipment. Gross trailer weight includes cargo and consumables.

## Hitching and backing checklist

| Step | Action |
| --- | --- |
| 1 | Inspect hitch, pins, chains, connector, landing gear, tires, and surrounding area. |
| 2 | Use bed camera for kingpin alignment and 360-degree view for perimeter awareness. Trailer-tow BLIS coverage is available; the sensors were repaired under the buyback (REF-026). |
| 3 | Confirm coupling/lock engagement and perform a pull test as specified by hitch/trailer instructions. |
| 4 | Connect breakaway cable, safety equipment, and electrical connector; confirm lights/brakes. |
| 5 | Use trailer guidance and hitch-angle feedback conservatively; pull forward to correct excessive articulation. |

## Loading data for this configuration

**These are the truck's own figures, not estimates.** Taken from the door jamb labels (REF-023, REF-024) and a CAT scale ticket, both recorded 8 September 2026.

| Rating | Figure | Source |
| --- | --- | --- |
| GVWR | 11,900 lb | Door label |
| Front GAWR | 5,990 lb | Door label |
| Rear GAWR | 7,230 lb | Door label |
| **Payload - occupants and cargo** | **4,566 lb** | Tire & Loading label |
| Seating capacity | 5 (2 front, 3 rear) | Tire & Loading label |

### As-weighed, empty

CAT Scale ticket 1132726251630, 8 September 2026, Love's Country Stores, I-70 Exit 45, Greenville IL. Truck only, no trailer.

| Axle | Weight | Rating | Margin |
| --- | --- | --- | --- |
| Steer | 4,120 lb | 5,990 lb | 1,870 lb |
| Drive | 3,080 lb | 7,230 lb | **4,150 lb** |
| **Gross** | **7,200 lb** | 11,900 lb | **4,700 lb** |

The scale-derived margin of 4,700 lb runs slightly above the 4,566 lb label payload; the label figure is the legal limit and the one to work to. Reweigh loaded, and with the trailer attached, before relying on either.

### Maximum pin weight

Two limits apply at once, and **whichever is lower governs**:

- **Payload** - 4,566 lb covers *everything* added to the truck: hitch, occupants, cargo, and pin weight.
- **Rear GAWR** - 7,230 lb, against 3,080 lb as weighed empty. A fifth-wheel pin sits over or just ahead of the rear axle, so essentially all of it lands on that axle, as does the hitch and anything in the bed.

| Load in the truck | Payload allows | Rear GAWR allows | **Max pin** | Governed by |
| --- | --- | --- | --- | --- |
| Hitch only, cab empty | 4,405 lb | 3,989 lb | **3,989 lb** | Rear GAWR |
| **Hitch, 200 lb people, 200 lb cargo** | 4,005 lb | 3,709 lb | **3,709 lb** | **Rear GAWR** |
| Hitch, 400 lb people, 200 lb cargo | 3,805 lb | 3,629 lb | **3,629 lb** | Rear GAWR |
| Hitch, 800 lb people, 400 lb cargo | 3,205 lb | 3,269 lb | **3,205 lb** | Payload |

### Working case

The planning assumption for this truck is **200 lb of people and 200 lb of cargo**, which gives a **maximum pin weight of 3,709 lb** - call it **3,700 lb**.

| Pin ratio | Loaded trailer supported |
| --- | --- |
| 30% | 12,400 lb |
| **25%** | **14,800 lb** |
| 20% | 18,500 lb |
| 15% | 24,700 lb |

At that load the truck grosses **11,470 lb of its 11,900 lb GVWR**, with the front axle at 4,120 of 5,990 lb.

The figure is not sensitive to how the occupants sit: varying their split between axles from 35% to 45% rearward moves the answer only between 3,699 and 3,719 lb, because at 200 lb total they are a small part of the rear-axle load. The **hitch and bed cargo matter more** - every pound in the bed comes straight off the pin allowance.

**The rear axle is the binding limit in most of the range, not payload.** Payload only takes over once the cab is full, because occupants sit largely forward of the rear axle and so consume payload faster than they consume rear-axle capacity. An earlier version of this chapter compared payload remaining against total rear-axle margin and concluded payload governs; that was wrong, because the rear margin must also absorb the hitch, the bed cargo and part of the occupants before any pin weight is added.

The front axle is not a constraint: it carries 4,120 lb against a 5,990 lb rating, and a fifth-wheel pin slightly *unloads* the front rather than adding to it.

The hitch is not a constraint either - the B&W Companion is rated 25,000 lb gross tow and 6,250 lb vertical load, well above anything the truck can carry.

**GCWR is not yet known** and could bind before either figure above on a long grade; source it from the Workshop Manual or Ford's towing guide.

> **Verify by weighing, not by arithmetic.** The occupant split between axles above is an estimate. Weigh the truck loaded and coupled, and measure actual pin weight with the [Sherline scale](09-accessories-and-modifications.md#short-term) - a fifth wheel's pin can run well above the nominal 20-25% depending on how the trailer is loaded.

> **The earlier estimate was low.** Working from the Camper Loading Guide, this chapter previously put payload at roughly 3,900-4,050 lb. The real figure is **4,566 lb** - about 600 lb higher. The cause is identifiable: that estimate assumed the guide's 5,200 lb front GAWR block, and this truck is actually a **5,990 lb** front GAWR truck, almost certainly because of the snowplow prep / camper package. The possibility was flagged at the time; the door label settles it.

Measure actual pin weight with the [Sherline scale](09-accessories-and-modifications.md#short-term) rather than relying on the 20-25% assumption.

## Payload and loading

- Ford's Camper Loading Guide remains relevant even when towing: factory options, front/rear axle loading, center of gravity, payload labels, and actual scale weights govern safe loading.
- Obtain CAT-scale records with truck-only and loaded trailer configurations; retain individual axle weights and compare with door-label ratings.

See [logs/scale-weights.md](../logs/scale-weights.md) for recorded weigh tickets.
