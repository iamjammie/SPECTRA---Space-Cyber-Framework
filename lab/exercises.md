# Exercise catalogue

Each exercise validates one attack path from `framework/data/attack_paths.json`. Run them in the
environment named; do not adapt them to operational systems.

| # | Exercise | Path | Environment | Passes when |
|---|----------|------|-------------|-------------|
| 1 | Bulk terminal action brake | AP-01 | Range plus lab terminals | A fleet-wide action is rate-limited and needs a second approval; wiped lab terminals are recovered. |
| 2 | Hostile mission control | AP-02 | Digital twin | Hazardous commands from a compromised console are held for independent approval; alternate site regains command. |
| 3 | Unkeyed uplink | AP-03 | Cabled RF plus flatsat | Unauthenticated and replayed frames are rejected in every mode, including safe mode, and reported. |
| 4 | Poisoned build | AP-04 | Range | A changed dependency fails reproducibility or signing checks before release; roll-out halts on a canary. |
| 5 | Leaked provider key | AP-05 | Range plus provider sandbox | The key's scope prevents schedule changes; the backup path does not share the key. |
| 6 | Navigation hold-over | AP-06 | Cabled RF | Receivers alarm on spoofing; timing holds over for the target period. |
| 7 | Clear-link audit | AP-07 | Cabled RF | No housekeeping or user data is readable without keys. |
| 8 | Altered product | AP-08 | Range | A changed product and a changed plan are both rejected downstream. |
| 9 | Payload crossover | AP-09 | Flatsat | Platform messages injected from the payload interface are blocked and flagged. |
| 10 | Rebuild under extortion | AP-10 | Range plus tabletop | Mission control is rebuilt from offline backups in target time and every secret is rotated. |

## Running an exercise

1. Open the path in the navigator and pin it to the matrix.
2. For each step, read the technique's assessment question and evidence requirement.
3. Agree stop conditions and an observer who can halt the exercise.
4. Run the minimum action that answers the question.
5. Record break, detect, respond, continue and recover in `assessment/register-template.csv`.
6. Set technique status in the navigator and export the assessment.
