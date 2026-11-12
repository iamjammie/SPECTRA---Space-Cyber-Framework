# SPECTRA methodology

SPECTRA assesses a space mission by following an adversary through nine states. Each state is a
question the adversary must answer before moving on, and a place where the defender can stop them.

| # | State | Adversary question | Defender question |
|---|-------|--------------------|-------------------|
| 1 | Mission | What is this mission for and how is it built? | What do we expose about ourselves? |
| 2 | Exposure | What capability and weakness can I prepare? | What can be researched without touching us? |
| 3 | Positioning | Where can I get a first foothold? | Which segment boundary is weakest? |
| 4 | Control | How do I turn a foothold into authority? | What does command authority really depend on? |
| 5 | Survival | How do I stay and stay unseen? | How would we know our telemetry and logs are lying? |
| 6 | Transit | Which trusted path carries me to the next segment? | What can each trusted path carry? |
| 7 | Manipulation | What can I take or change quietly? | Can we prove our data and parameters are intact? |
| 8 | Mission Effect | How do I break the service? | What does one effect cost the mission? |
| 9 | Resilience | How do I stop them recovering? | Can we return to a trusted state under attack? |

## Units of the framework

- **Technique**: one behaviour in one state. Every technique carries the segments, assets and ways
  in that it touches, the capability tier it needs, an evidence label, the mission effects it can
  lead to, the controls that break it, the data that reveals it, and a safe way to assess it.
- **Control**: a defensive breakpoint, grouped by Govern, Identify, Protect, Detect, Respond and
  Recover. Each control states how to verify it by test, not by document review.
- **Mission effect**: the consequence in mission terms. Assessments are scored against effects.
- **Attack path**: an ordered chain of techniques from Mission to Resilience, with the controls most
  likely to break it first.
- **Actor and incident records**: public reporting mapped onto techniques, each with a label that
  says how well supported the link is.

## The assessment loop

1. Map mission dependencies and trust boundaries.
2. Select an attack path.
3. Define preconditions and an authorised test environment.
4. Execute the minimum controlled validation needed to test each transition.
5. Capture security and mission evidence.
6. Identify the first effective defensive breakpoint.
7. Measure detection, response and containment.
8. Measure mission continuity.
9. Validate trusted recovery where authorised.
10. Record residual risk and engineering action.

Steps 4 to 9 map onto the fields of each technique: assessment question, test environments,
evidence, detection, controls and recovery test.

## Labels

**Evidence.** Observed (reported in real incidents against space or satellite-service
organisations), Demonstrated (shown by research, exercises or on-orbit tests), Theorised (assessed
as plausible from design).

**Capability tier.** 1 Opportunistic, 2 Capable, 3 Advanced, 4 Strategic. The tier is the lowest
level SPECTRA judges sufficient, not a statement about who has done it.

**Actor links.** Reported, Claimed (by the actor, unverified) or Assessed (typical of the actor
class; SPECTRA's own judgement).

## Relationship to other frameworks

SPECTRA is not a renamed matrix. It keeps a tactic-level crosswalk to Aerospace SPARTA and MITRE
ATT&CK (see the About view in the navigator) and deliberately does not reuse their technique
identifiers. Use SPARTA, SPACE-SHIELD or EMB3D when you need their depth on a single technique or
device class; use SPECTRA to decide which path to test, how to test it safely and whether recovery
works.
