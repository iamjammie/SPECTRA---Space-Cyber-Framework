# Playbook: Suspected loss of command authority

Related techniques: CTL-01, CTL-02, CTL-03, CTL-09, EFX-08, RSL-04

Use in an exercise first. Adapt to your mission's procedures and authority before relying on it.

## Steps

1. Declare the incident and move responders to out-of-band communications.
2. Stop all routine commanding. Hold the stored command schedule if the spacecraft allows it safely.
3. Reconcile ground command history with on-board command counters for the last contacts.
4. Check telemetry against independent sources: tracking data, link metrics and dissimilar sensors.
5. Treat the primary mission control system as untrusted. Move to the alternate site with separate credentials.
6. Read back the on-board schedule, key slots, fault-protection tables and authorised stations.
7. Rotate command keys using the rehearsed on-orbit rekey procedure.
8. Attest flight software against the release hash; restore from the protected image if it differs.
9. Notify tracking and conjunction services if manoeuvring cannot be ruled out.
10. Resume commanding with independent approval for every hazardous command until the cause is known.

## Measure

- Time from first indication to holding commanding
- Time to command from the alternate site
- Time to an attested spacecraft state
