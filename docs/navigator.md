# Using the SPECTRA Navigator

Open `index.html` in any current browser. It is one file, makes no network requests and works from
a USB stick or an air-gapped machine.

## Views

| View | Use it to |
|------|-----------|
| Matrix | See all techniques by state. Filter, recolour, and open any technique for full detail. |
| Threat surface | Start from a segment, asset or way in and jump to the techniques that touch it. |
| Attack paths | Read worked chains, see where to break them, and overlay a path on the matrix. |
| Threat actors | Browse actor profiles and overlay an actor's techniques on the matrix. |
| Incidents | Browse public incidents, claims and research by year, with sources. |
| Controls | Mark which controls you have in place and see what each one breaks. |
| Assessment | Record a status and notes per technique, then export, import or print. |
| About | Method, labels, crosswalk and limits. |

## Filtering

Filters combine with AND across groups and OR within a group. Available groups: segment, asset, way
in, mission type, adversary capability, evidence, threat actor, mission effect, control and
detection data. Counts beside each option show how many techniques you would get. The search box
searches every field. Tick **Dim instead of hide** to keep the whole matrix visible.

**Colour by** changes what cell colour means: phase, adversary capability, evidence, actor activity,
control coverage or assessment status.

## Assessment data

Statuses, notes and control states are saved in the browser's local storage on your machine. Use
**Export assessment** to save a JSON file (format in `framework/schema/assessment.schema.json`) and
**Import assessment** to load one. `examples/sample-assessment.json` is a fictional example.

## Links

The address bar updates as you filter, so a URL such as
`index.html#view=matrix&seg=space&basis=O` reopens the same view.

## Keyboard

`/` focuses search. `Esc` closes the detail panel.

## Rebuilding

Edit the JSON in `framework/data/`, then:

```bash
python3 scripts/validate.py
python3 scripts/build_navigator.py
```

No packages are needed.
