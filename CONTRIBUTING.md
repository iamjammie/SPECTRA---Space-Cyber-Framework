# Contributing

A proposed technique should include a problem statement, mission/domain, preconditions, assessment question, safe test environment, evidence requirement, detection opportunity, defensive breakpoint, mission effect, recovery test, references and a statement of novelty within SPECTRA.

Do not submit classified, sensitive mission, credential, export-controlled or operational targeting information.

## How to add or change content

1. Edit the JSON in `framework/data/`. A technique must follow `framework/schema/technique.schema.json`.
2. Run `python3 scripts/validate.py`, then `python3 scripts/build_navigator.py`.
3. Commit the data together with the rebuilt `index.html` and `docs/technique-catalogue.md`. CI rejects a stale build.

Actor and incident records need at least one public source and an honest label: use Claimed for anything only the actor asserts, and Assessed for links that are your own judgement. Describe behaviour, never a procedure against a real system.
