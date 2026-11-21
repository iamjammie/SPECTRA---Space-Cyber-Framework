# Assessment environments

SPECTRA techniques name the safest environment that can answer their assessment question. Use the
least capable environment that works.

| Environment | What it is | Good for | Not for |
|-------------|-----------|----------|---------|
| Passive open-source review | Reading what is already public | Mission and Exposure states | Anything that touches a system |
| Tabletop | People, procedures and decisions | Response, authority, recovery planning | Proving a control works |
| Isolated cyber range | Copy of ground systems with no route to operations | Ground footholds, pivots, rebuilds | RF and flight behaviour |
| Digital twin | Simulated spacecraft and ground loop | Command authority, telemetry trust, fleet operations | Hardware-specific flaws |
| Hardware-in-the-loop or flatsat | Flight-like hardware on a bench | Flight software, boot, bus and key handling | Radiated tests |
| Shielded or cabled RF lab | Radios connected by cable or inside a shielded room | Link authentication, replay, interference margin | Any radiated emission |
| Authorised ground assessment | Scoped test of operational ground IT | Exposure, identity and segmentation | Anything that can command a spacecraft |

## Reference layout

```
 [ Operator workstations ]--[ Mission control replica ]--[ Front-end / baseband sim ]
            |                         |                           |
     [ Identity replica ]      [ Key store (test keys) ]   == cabled RF, attenuated ==
            |                         |                           |
 [ Enterprise IT replica ]     [ Flight dynamics replica ]  [ Flatsat or digital twin ]
            |
 [ Attacker enclave ]   -- no route to operational networks, test keys only --
```

## Safety rules

1. No connection, credential or key is shared between the lab and operations.
2. No radiated transmission. RF tests are cabled or shielded.
3. Test keys only. Never load operational key material.
4. Written authorisation names the scope, the environment and the stop conditions.
5. Operational spacecraft and third-party systems are out of scope unless their owner has agreed in
   writing and a safety review has been completed.
6. Findings that reveal weaknesses in real systems are handled as sensitive.
