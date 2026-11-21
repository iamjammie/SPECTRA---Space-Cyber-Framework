# SPECTRA v0.2

## Space Protection, Exploitation, Continuity, Threat Response & Assurance

A mission-first offensive, defensive and resilience assessment framework for space systems, with an offline navigator.

> **Open [`index.html`](index.html) in any modern browser.** One file, no server, no dependencies, no network calls. Works air-gapped.

<!-- suite-nav:start -->
> **Part of the [iamjammie Hunt suite](https://iamjammie.github.io/FluxHunt/suite.html)** — open-source, offline-first security tooling and knowledge.
>
> 🧠 [Hunt-Sage](https://github.com/iamjammie/hunt-sage) (knowledge) · 🌊 [FluxHunt](https://github.com/iamjammie/FluxHunt) (wire) · 🖥️ [HostHunt](https://github.com/iamjammie/HostHunt) (box) · 📡 [HostVigil](https://github.com/iamjammie/HostVigil) (fleet) · 🔐 [ADHuntX](https://github.com/iamjammie/ADHuntX) (directory) · 🎯 [Sentinel Matrix](https://github.com/iamjammie/Sentinel-Matrix) (detection coverage) · 🧬 [TTP NEXUS](https://github.com/iamjammie/TTP-Nexus) (frameworks) · 🛡️ [ThreatIntFlux](https://github.com/iamjammie/ThreatIntFlux) (threat intel) · 🔦 [Photonwire](https://github.com/iamjammie/PhotonWire) (air gap) · 🛰️ **SPECTRA** (space)
>
> [Suite hub](https://iamjammie.github.io/FluxHunt/suite.html) · [All projects](https://github.com/iamjammie)
<!-- suite-nav:end -->

SPECTRA is deliberately not a renamed compilation of existing space-cyber matrices. Its primary unit is an **attack-path state transition**:

**Mission → Exposure → Positioning → Control → Survival → Transit → Manipulation → Mission Effect → Resilience**

Every assessment technique is intended to be testable in an isolated cyber range, digital twin, hardware-in-the-loop environment, or explicitly authorized assessment.

## What is in the framework

| | Count | What each record carries |
|---|---|---|
| Techniques | 120 across 9 states | Segments, assets, ways in, mission types, capability tier, evidence label, precondition, mission effects, detection and data sources, controls, and a safe assessment (question, environment, evidence, recovery test) |
| Controls | 36 | Govern, Identify, Protect, Detect, Respond, Recover; each with a test that verifies it |
| Mission effects | 12 | Consequences in mission terms |
| Detection data sources | 16 | What telemetry or log reveals a technique |
| Threat actors | 20 | Profile, sources, and technique links labelled Reported, Claimed or Assessed |
| Incidents and research | 36 (1986 to 2026) | Summary, attribution label, mapped techniques, sources |
| Attack paths | 10 | Ordered technique chains with the controls most likely to break them |

## The navigator

| View | Use it to |
|---|---|
| **Matrix** | See every technique by state, as in ATT&CK Navigator. Filter, recolour, open any cell for detail. |
| **Threat surface** | Start from a segment or asset (on-board computer, telecommand uplink, mission control, user terminal, build pipeline and more) and jump to what touches it. |
| **Attack paths** | Read worked chains from reconnaissance to recovery denial and overlay them on the matrix. |
| **Threat actors** | Browse actors linked to space targets and overlay their techniques. |
| **Incidents** | Browse public incidents, claims and research by year, with sources. |
| **Controls** | Mark what you have in place; the matrix then colours by coverage. |
| **Assessment** | Record status and notes per technique; export, import, CSV, print. |

Filters: segment, asset, way in, mission type, adversary capability, evidence, threat actor, mission effect, control, detection data, plus free-text search. Filter state lives in the URL, so views can be bookmarked. Assessment data stays in your browser until you export it. Details in [`docs/navigator.md`](docs/navigator.md).

### Framework influence

SPECTRA draws engineering and threat-modeling lessons from Aerospace SPARTA, MITRE EMB3D/ESTM and ESA SPACE-SHIELD, while using its own mission/path/evidence/breakpoint/recovery structure. Crosswalks are at tactic level only; no identifiers or text are copied. See [`NOTICE`](NOTICE).

### Practical assessment loop

1. Map mission dependencies and trust boundaries.
2. Select an attack path.
3. Define preconditions and an authorized test environment.
4. Execute the minimum controlled validation needed to test the transition.
5. Capture security and mission evidence.
6. Identify the first effective defensive breakpoint.
7. Measure detection, response and containment.
8. Measure mission continuity.
9. Validate trusted recovery where authorized.
10. Record residual risk and engineering action.

### Repository

```text
index.html             the built, standalone navigator: open this
navigator/             navigator template (UI and logic, no data)
framework/data/        techniques, controls, mission effects, actors, incidents, attack paths (JSON, source of truth)
framework/schema/      JSON Schemas for techniques and assessment exports
assessment/            scoring model and assessment register template
playbooks/             practical assessment and recovery procedures
lab/                   cyber-range/HIL environments and exercise catalogue
docs/                  methodology, navigator guide, generated technique catalogue, roadmap
examples/              sample assessment (fictional mission) to import into the navigator
scripts/               validation and build
.github/               CI, Pages deployment and contribution template
```

### Build

Requires only Python 3. No packages.

```bash
python3 scripts/validate.py          # ids, required fields, every cross-reference
python3 scripts/build_navigator.py   # framework/data + navigator/template.html -> index.html
```

To add or change content, edit the JSON in `framework/data/` and rebuild. The navigator derives its filters, counts and overlays from the data.

### Honesty notes

- Technique, control and effect text is original and describes behaviour, not procedures.
- Evidence labels say whether a technique has been **Observed** in real incidents, **Demonstrated** by research, or is **Theorised**.
- Actor and incident records summarise public reporting. Claims by actors are labelled as claims and are not verified.
- Capability tiers and control mappings are this project's judgement; challenge them for your mission.

### Safe use

For defensive research, engineering assurance, education, cyber ranges, digital twins, HIL and explicitly authorized assessments. Do not test operational spacecraft or third-party systems without authorization and appropriate safety controls.
