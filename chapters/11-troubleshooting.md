# 11. Troubleshooting

## Placeholder symptom index

| Symptom | First checks | Authoritative source |
| --- | --- | --- |
| Camera image missing | Power cycle; configuration history; camera connections | Owner manual / REF-008 / Ford WSM |
| Trailer brakes or lights inoperative | Connector, trailer wiring, fuse/relay, controller, trailer fault | Owner manual / Ford WSM |
| No-start or low battery | Battery condition, connections, charging system, codes | Owner manual / Ford WSM |
| Towing handling concern | Loading, tire pressures, hitch/trailer ratings, scale weights | Owner manual / hitch manual |
| **BLIS / Cross Traffic Alert inoperative** | Repaired by Ford under the buyback (REF-026); treat a recurrence as a repeat fault. Pull DTCs; check sensor connectors, rear bumper sensor mounting, and trailer-tow BLIS configuration | Ford WSM / REF-015 / REF-026 |
| **Passenger-side window inoperative** | Repaired by Ford under the buyback (REF-026); treat a recurrence as a repeat fault. Check door module, switch, regulator, and window motor; test from both door and master switch | Ford WSM / REF-026 |

## A/C evaporator drain

**Location.** The evaporator drain tube passes through the **firewall on the passenger side, inside the frame rail, just above the passenger-side exhaust manifold**. It is easiest to see from underneath the truck, where it appears as a short black tube lying horizontally and standing proud of the firewall by only about **3/16-1/4 in**. Pulling the fender liner gives the clearest view. This location is from Ford forum and parts sources, **not from a Ford figure** - the workshop manual (REF-028) carries no location illustration for it, only the inspection table below. **Confirmed by owner photo - see below.**

**Found and photographed 21 September 2026 - [REF-031](../references/REF-031-ac-evaporator-drain.jpeg) close-up (IMG_1735), [REF-032](../references/REF-032-ac-drain-wheel-well-view.jpeg) wide view (IMG_1728).** The drain is a **black rubber grommet seated in the dash panel**, showing through a cut in the foil heat-shield blanket, with a **slotted grey plastic drain fitting inserted in its center**. The slots are the outlet - condensate runs out between them, and the fitting also keeps road debris from packing the opening. Surrounding context in IMG_1733-1739 is foil blanket, taped seams and the floor pan. **How to get eyes on it (owner photo sequence IMG_1716-1739, wide to close).** Work from the **passenger-side front wheel**: crouch behind the tire and look rearward and up, past the trailing edge of the inner fender liner. The liner, the frame rail and the foil-wrapped dash panel come into view in that order - **[REF-032](../references/REF-032-ac-drain-wheel-well-view.jpeg) is that view** (IMG_1728), and the grommet sits in the foil-covered panel beyond (IMG_1733-1735). No jacking, no liner removal - the sight line exists with the wheel on the ground, though a light helps because the area is in deep shade.

**Earlier misidentification, recorded so it is not repeated:** the stepped black stub in IMG_1682/1683 was first read as the drain, but the owner identified it as an **exhaust oxygen sensor** - it has a wire and its boot seats in the exhaust pipe.

**What Ford does say.** REF-028's routine inspection lists the drain tube conditions and their dispositions: *disconnected*, *leaking* and *routed incorrectly* require repair or replacement; *missing* and *restricted* require repair or replacement. The A/C odor procedure adds two checks - the evaporator core drain tube for restriction, and the **inner cowl drain area and air inlet screen** for obstruction or standing water.

**Symptom to watch.** Wet passenger-side carpet during or after A/C use means either a restricted drain backing condensate into the cabin, or condensate tracking back through the drain-tube seal. The field test: run the A/C hard for 10-15 minutes on a humid day and look for a clear drip landing under the passenger footwell. No puddle plus damp carpet is a plugged drain.

**Clearing it.** Low-pressure compressed air from below, or a zip tie worked gently a short way in. **Never push a wire or screwdriver up the tube** - puncturing the evaporator case turns a free fix into a dash-out repair.

**TSB 20-2170 - does not apply to this truck.** Ford's fix for condensate entering at the drain-tube seal (remove the metal shield, fit an elbow on the drain tube, tape over it) covers **2018-2020** F-150/Expedition/Navigator/Super Duty **built 31 Aug 2018 through 2 Feb 2020**. This truck is a 2024 and falls outside it. Worth knowing only as a precedent if the same symptom appears, since the underlying design complaint was a drain that lets water back past the seal.

### Removing the passenger (RH) fender splash shield

From the workshop manual (REF-028), *Fender Splash Shield: Removal*, F-250/F-350. The manual illustrates the LH side and notes the RH is similar, so the RH-specific steps are called out below. **Every fastener here is low torque - inch-pounds, not foot-pounds.**

| Step | Fastener | Torque on reassembly |
| --- | --- | --- |
| 1 | **Remove the wheel and tire** (single rear wheel procedure). Wheel nuts go back to **150 lb-ft** with the truck on its tires, per [chapter 5](05-torque-specifications.md) | 150 lb-ft |
| 2 | **If equipped with mud flaps:** remove the bolts, then the pushpin, bolt and mud flap. This truck has **no mud flaps yet** - the WeatherTech set is on the [short-term list](09-accessories-and-modifications.md), so this step will apply after they are fitted | 10 lb-in (1.1 N·m) |
| 3 | Remove the bolts along the shield | 10 lb-in (1.1 N·m) |
| 4 | Remove the bolt and the **pin-type retainer** | 35 lb-in (4 N·m) |
| 5 | Remove the bolts | 9 lb-in (1 N·m) |
| 6 | **RH side:** remove the bolt | 35 lb-in (4 N·m) |
| 7 | **RH side:** remove the nut | Not specified |
| 8 | **RH side:** release the **wiring harness retainers** and remove the shield. (The LH side also has hood latch release cable retainers to free - the RH side does not) | - |

**Installation:** Ford's entire instruction is *"To install, reverse the removal procedure."*

**Socket sizes - confirmed by the owner 21 September 2026.** Ford specifies torque for every fastener here but never a socket size. On this truck: **10 mm for one bolt, 6 mm for the rest.** The **two push-on nuts were turned with a flat-blade screwdriver** rather than a socket. The pin-type retainer is not a socket job - it pulls with a trim tool.

**Shortcut that worked: no full shield removal.** The owner **pried the rear edge of the fiber liner out far enough to flex it** and reach the drain by hand, instead of taking the shield off. That is the least-disturbance route to the grommet.

**Practical notes.** The 9 and 10 lb-in figures are barely more than snug - a 1/4 in drive is the right tool and a 1/2 in drive torque wrench cannot read that low, including the [digital wrench in chapter 9](09-accessories-and-modifications.md), whose range starts at 3.8 lb-ft (45 lb-in). Plastic shields strip easily, so these numbers matter more than they look. Note also that **the drain grommet can be seen without removing the shield at all** - see the wheel-well sight line above and [REF-032](../references/REF-032-ac-drain-wheel-well-view.jpeg).

### Drain flush as performed, 21 September 2026

Recorded from the owner's work at **38,926 miles**. **This was done to chase a sour smell in the interior, not as preventive maintenance** - it is step two of a staged attack on the odor (see below). There was no wet-carpet symptom, so the drain was not suspected of backing up; the evaporator was suspected of holding the smell.

| Step | Detail |
| --- | --- |
| 1 | Loosened the RH fender splash shield fasteners (**10 mm x 1, 6 mm for the rest**; two push-on nuts turned off with a flat-blade screwdriver) |
| 2 | **Pried the rear edge of the fiber liner out** and flexed it enough to reach the drain - the shield was never fully removed |
| 3 | Fed the **applicator hose all the way up the drain** and discharged the **entire canister** of aerosol cleaner |
| 4 | Caught the excess in a pail as it drained back out |
| 5 | **Waited 15 minutes** for the product to work |
| 6 | Started the engine and ran the **blower and A/C on low for 5 minutes** to push condensate and residue through the drain |
| 7 | Shut down, reassembled the shield, and **replaced the cabin air filter** |

**Product used: [Lubegard Kool-It Evaporator & Heater Foam Cleaner](https://www.lubegard.com/products/evap), part `96030`**, 6 oz (170 g) net with one applicator tip and hose. Aerosol foam, EV and hybrid compatible, EV OEM approved, extremely flammable - no drilling required. The label reads `165-2810` with a UPC beginning `83137968` (IMG_1766-1767).

**The owner's method matches the manufacturer's directions exactly.** Kool-It's own steps are: locate the drain tube with the ignition off; insert the application tip and hose through the drain opening; once the tip reaches the evaporator/heater core, shake the can, attach the hose fully to the cap nozzle, then **press the cap down to lock it and discharge the entire can**; remove the hose and refit anything moved for access; **allow about 15 minutes** to work and deodorize; then **run the fan on its lowest setting for 5 minutes**, so the foam condenses and collapses, carrying contaminants out through the drain. Lubegard notes that the usual cause of the smell is moisture failing to drain, and that feeding the hose up the drain **clears any blockage on the way in** - which is exactly the preventive value here. Lubegard suggests a lift for underside access; the wheel-well-and-flex-the-liner route above did the job without one.

**Tech support:** Lubegard hotline 800-333-5823 or 206-762-5343.

**Old cabin air filter (IMG_1768-1769).** Heavily loaded - grey-brown across the full pleat depth with visible fiber and debris on the inlet face, against the clean white of the replacement. It was due. Replaced with a **Motorcraft FP-92**, which fit. **$36.78 bought over the counter at the Ford dealer**, 21 September 2026. Note that the parts catalog in [chapter 3](03-oem-parts-catalog.md) lists **FP-119** for this truck - that conflict is flagged there and still to be resolved.

### Interior sour smell - remediation plan

The odor was present when the truck was bought (8 September 2026). The owner is working through the likely sources in order, cheapest and least invasive first:

| Step | Work | Status |
| --- | --- | --- |
| 1 | **Hard plastics cleaned** throughout the cab - dash, console, door cards, trim | **Done** |
| 2 | **Evaporator and heater core foamed** with Lubegard Kool-It `96030` through the drain, and the **cabin air filter replaced** with a Motorcraft **FP-92** - the old one was heavily loaded | **Done 21 September 2026**, 38,926 mi |
| 3 | **Cloth seats scrubbed** with an upholstery cleaner | Planned - a later day |

**Why this order is right.** A sour, musty smell in a cab usually comes from one of three places: microbial growth on the evaporator core, a loaded cabin filter holding damp debris, or soiled upholstery and carpet. Steps 1 and 2 clear the first two and cost little. If the smell survives step 3, the remaining suspects are **the carpet and its underlay** - which hold water far longer than seat fabric - and any **past water intrusion**, so check the passenger footwell for staining or a tide line, and re-check the drain and the cowl inlet screen for standing water. Note also that the **evaporator is a repeat-treatment item**: if the smell returns after a few weeks, it points back at the core rather than the fabric.

**Verification.** Judge the evaporator work with the cab closed up after a hot, humid drive with the A/C on - that is when a core-sourced smell is strongest. A first-start whiff that fades is the classic evaporator signature; a smell that is constant regardless of the blower points at fabric.

