# Playbook: Terminal fleet disablement

Related techniques: CTL-11, EFX-04, SRV-10

Use in an exercise first. Adapt to your mission's procedures and authority before relying on it.

## Steps

1. Freeze the management plane: disable bulk actions and update jobs.
2. Isolate the management network from remote access and enterprise IT.
3. Measure the scope from fleet telemetry: which models, firmware versions and regions.
4. Preserve one affected terminal and management logs for analysis.
5. Decide per model whether remote recovery is possible; test on lab terminals first.
6. Start logistics for replacement where remote recovery is not possible.
7. Tell customers what happened, what still works and when to expect service.
8. Rebuild management systems from trusted media before reconnecting them.
9. Re-enable fleet actions with rate limits and second approval in force.

## Measure

- Share of fleet affected
- Share recovered remotely
- Time to restore service to priority customers
