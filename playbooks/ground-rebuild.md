# Playbook: Rebuild mission ground systems

Related techniques: EFX-05, RSL-03, RSL-07

Use in an exercise first. Adapt to your mission's procedures and authority before relying on it.

## Steps

1. Assume every online system and credential is compromised.
2. Stand up clean hardware or a clean cloud tenant with no trust to the old environment.
3. Restore identity services, then mission control, then flight dynamics from offline backups.
4. Verify restored images and databases against offline hash records.
5. Issue new credentials and keys; do not import old ones.
6. Command a simulator, then a single contact with the spacecraft under two-person control.
7. Rotate every secret on the rotation checklist, including on-orbit keys and supplier access.
8. Reconnect external interfaces one at a time with monitoring in place.

## Measure

- Time to first trusted command
- Number of secrets rotated against the checklist
- Data lost between last backup and incident
