# Scoring and maturity

## Technique status

| Status | Meaning |
|--------|---------|
| Not assessed | No test or review yet. |
| Exposed | The assessment question was answered unfavourably and no control stopped the transition. |
| Partly mitigated | A control slowed or detected the transition but did not reliably stop it, or recovery failed. |
| Mitigated and verified | A control stopped the transition in a test, detection fired, and the recovery test passed. |
| Not applicable | The precondition cannot hold for this mission. Record why. |

## Per-technique measures

Record these in the notes field or the register:

- **Break**: which control stopped the transition first (control id), or none.
- **Detect**: time from action to analyst awareness.
- **Respond**: time from awareness to containment decision.
- **Continue**: share of mission service delivered while the effect was in force.
- **Recover**: time to a state you can attest as trusted.

## Control coverage

A technique's coverage is the share of its mapped controls you have marked in place (partial counts
half). Coverage is a planning aid. Only a test moves a technique to Mitigated and verified.

## Path score

For a chosen attack path, the result is the state at which the path was first broken. Earlier is
better. A path that reaches Mission Effect is a finding even if every later step was detected.

## Maturity levels

| Level | Description |
|-------|-------------|
| 0 Unknown | No mission dependency map. Techniques not assessed. |
| 1 Mapped | Dependencies and trust boundaries documented. Paths selected. |
| 2 Reviewed | Techniques assessed by tabletop and design review. |
| 3 Tested | Priority paths tested in a range, twin or flatsat. Breakpoints confirmed. |
| 4 Measured | Detection, response and continuity measured for priority paths. |
| 5 Proven recovery | Trusted recovery rehearsed and attested for the worst reachable states. |
