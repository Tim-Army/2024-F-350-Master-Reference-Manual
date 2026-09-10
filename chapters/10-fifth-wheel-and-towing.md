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
| Hitch, 200 lb people, 200 lb cargo | 4,005 lb | 3,709 lb | **3,709 lb** | Rear GAWR |
| **Hitch, 400 lb people, 200 lb cargo** | 3,805 lb | 3,629 lb | **3,629 lb** | **Rear GAWR** |
| Hitch, 800 lb people, 400 lb cargo | 3,205 lb | 3,269 lb | **3,205 lb** | Payload |

### Working case

The planning assumption for this truck is **400 lb of people and 200 lb of cargo**, which gives a **maximum pin weight of 3,629 lb** - call it **3,600 lb**.

| Pin ratio | Loaded trailer supported |
| --- | --- |
| 30% | 12,100 lb |
| **25%** | **14,500 lb** |
| 20% | 18,100 lb |
| 15% | 24,200 lb |

At that load the truck grosses **11,590 lb of its 11,900 lb GVWR**, with the front axle at 4,120 of 5,990 lb.

The figure is not sensitive to how the occupants sit: varying their split between axles from 35% to 45% rearward moves the answer only between 3,609 and 3,649 lb. **Bed cargo matters more** - every pound in the bed comes straight off the pin allowance, since both land on the rear axle.

**The rear axle is the binding limit in most of the range, not payload.** Payload only takes over once the cab is full, because occupants sit largely forward of the rear axle and so consume payload faster than they consume rear-axle capacity. An earlier version of this chapter compared payload remaining against total rear-axle margin and concluded payload governs; that was wrong, because the rear margin must also absorb the hitch, the bed cargo and part of the occupants before any pin weight is added.

The front axle is not a constraint: it carries 4,120 lb against a 5,990 lb rating, and a fifth-wheel pin slightly *unloads* the front rather than adding to it.

The hitch is not a constraint either - the B&W Companion is rated 25,000 lb gross tow and 6,250 lb vertical load, well above anything the truck can carry.

**GCWR is not yet known** and could bind before either figure above on a long grade; source it from the Workshop Manual or Ford's towing guide.

> **Verify by weighing, not by arithmetic.** The occupant split between axles above is an estimate. Weigh the truck loaded and coupled, and measure actual pin weight with the [Sherline scale](09-accessories-and-modifications.md#short-term) - a fifth wheel's pin can run well above the nominal 20-25% depending on how the trailer is loaded.

> **The earlier estimate was low.** Working from the Camper Loading Guide, this chapter previously put payload at roughly 3,900-4,050 lb. The real figure is **4,566 lb** - about 600 lb higher. The cause is identifiable: that estimate assumed the guide's 5,200 lb front GAWR block, and this truck is actually a **5,990 lb** front GAWR truck, almost certainly because of the snowplow prep / camper package. The possibility was flagged at the time; the door label settles it.

Measure actual pin weight with the [Sherline scale](09-accessories-and-modifications.md#short-term) rather than relying on the 20-25% assumption.

## Front-mounted motorcycle carrier - archived

> **Not being pursued.** Archived 9 September 2026. The analysis is kept because the numbers are sound and the question may come back - if it does, this is the starting point rather than a fresh calculation.

The idea: carry a scooter on a front hitch receiver, so the fifth-wheel search is not restricted to toy haulers.

| Component | Model | Weight |
| --- | --- | --- |
| Front receiver | EcoHitch front mount | ~47 lb |
| Carrier | Black Widow / Discount Ramps `AMC-400-DLX` | 58 lb |
| Motorcycle | Yamaha Zuma 125 (wet) | ~282 lb |
| **Total added at the front** | | **~387 lb** |

Carrier breakdown: aluminum track 28-32 lb, steel receiver assembly 15-18 lb, steel wheel chock 7-9 lb, aluminum ramp 7-9 lb, hardware 1-2 lb.

### What it does to the axle loads

**A front-mounted load is a cantilever ahead of the front axle, so it does not behave like cargo in the bed.** It adds *more* than its own weight to the front axle, and *lifts* weight off the rear.

Taking the moment about the rear axle, with a 176-inch wheelbase:

| Carrier overhang ahead of front axle | Front axle | Rear axle |
| --- | --- | --- |
| 30 in | 4,573 lb (+453) | 3,014 lb (-66) |
| **40 in** | **4,595 lb (+475)** | **2,992 lb (-88)** |
| 50 in | 4,617 lb (+497) | 2,970 lb (-110) |

**The front axle is comfortable** - about 4,600 lb against a 5,990 lb GAWR, leaving roughly 1,400 lb of margin. Front axle capacity is not the problem.

### What it does to pin weight

With the carrier fitted, and the working case of 400 lb people plus 200 lb cargo:

| Limit | Allows |
| --- | --- |
| Payload | **3,418 lb** |
| GVWR | 3,552 lb |
| Rear GAWR | 3,717 lb |
| **Max pin** | **3,418 lb** - governed by **payload** |

**The governing constraint flips.** Without the carrier the rear axle binds at 3,629 lb; with it, payload binds at 3,418 lb, because the 387 lb counts fully against the 4,566 lb payload while the cantilever *reduces* rear-axle load.

**Net cost to pin weight: about 211 lb, not 387 lb** - the rear-axle unloading gives roughly 176 lb back. At a 25% pin ratio that is a **13,700 lb trailer** rather than 14,500 lb: roughly 800 lb of trailer given up to carry the scooter.

### Points to verify

| Item | Note |
| --- | --- |
| **Front receiver tongue-weight rating** | **Confirmed: 1,000 lb.** The carrier and scooter together put ~340 lb on it (58 + 282; the receiver's own weight is part of the truck, not tongue load), so it runs at about **a third of its rating** |
| Carrier capacity | `AMC-400-DLX` implies a 400 lb rating against a 282 lb scooter - adequate |
| Fitment against this VIN | Appears compatible; no aftermarket coolers fitted |
| Ground clearance when loading | A longer curved ramp would ease the approach angle |
| Headlight obstruction | Likely minimal given the Zuma's narrow profile - check on low beam at night |
| Radiator and intercooler airflow | Should be acceptable for a 125, but monitor coolant temperature on hot days while towing |
| Front license plate | May need relocating depending on carrier position. The truck has the factory front plate bracket (REF-003) |
| Legal overhang and lighting | Front overhang limits and any obstruction of lighting or the plate vary by state - check for the states routinely driven |

### Assessment as archived

The weight case held up. The front axle had ample margin at roughly 4,600 of 5,990 lb, the rear axle was *helped* rather than hurt, and the real cost was 211 lb of pin allowance - around 800 lb of trailer at a typical pin ratio.

Nothing in the numbers ruled it out. It was set aside as a direction, not rejected on weight - and the one specification that had been outstanding is now confirmed: the **front receiver is rated 1,000 lb**, against roughly 340 lb of carrier and scooter, so it runs at about a third of its capacity.

**No open technical questions remain on this idea.** Payload governs the towing consequence, at 3,418 lb of pin rather than 3,629 lb, and that is a trade rather than an obstacle. If it is revived, the only items left are practical: ground clearance on loading, headlight and plate obstruction, radiator airflow on hot days, and state overhang rules.

## Payload and loading

- Ford's Camper Loading Guide remains relevant even when towing: factory options, front/rear axle loading, center of gravity, payload labels, and actual scale weights govern safe loading.
- Obtain CAT-scale records with truck-only and loaded trailer configurations; retain individual axle weights and compare with door-label ratings.

See [logs/scale-weights.md](../logs/scale-weights.md) for recorded weigh tickets.
