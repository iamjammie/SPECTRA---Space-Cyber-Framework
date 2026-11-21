# Playbook: Command key compromise

Related techniques: CTL-09, MNP-10, SRV-09, RSL-04

Use in an exercise first. Adapt to your mission's procedures and authority before relying on it.

## Steps

1. Confirm the suspicion: key-store access records, key use outside passes, key material found outside hardware.
2. Identify every spacecraft, station and system that holds or trusts the key.
3. Convene the key ceremony with dual control.
4. Generate replacement keys in hardware.
5. Rekey spacecraft in priority order using the protected rekey path; verify by authenticated command.
6. Revoke the old key on board and on the ground; confirm frames under the old key are rejected.
7. Check on-board key slots and authorised-station lists for entries you do not recognise.
8. Review how the key was exposed and close that route before closing the incident.

## Measure

- Time from suspicion to first spacecraft rekeyed
- Time to full fleet rekey
- Old key rejected everywhere: yes or no
