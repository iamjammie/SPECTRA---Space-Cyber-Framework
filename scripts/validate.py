#!/usr/bin/env python3
"""Validate the SPECTRA dataset: required fields, unique ids and every cross-reference.

Usage: python3 scripts/validate.py
Exits non-zero and lists every problem found. Needs only the Python standard library.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "framework" / "data"
FILES = ["meta", "taxonomy", "phases", "techniques", "controls", "mission_effects",
         "data_sources", "actors", "incidents", "attack_paths"]


def load():
    return {n: json.loads((DATA / (n + ".json")).read_text(encoding="utf-8")) for n in FILES}


def validate(d):
    errs = []

    def ids(items, pattern, label):
        seen = set()
        for it in items:
            i = it.get("id")
            if not isinstance(i, str) or not re.fullmatch(pattern, i):
                errs.append("%s: bad id %r" % (label, i))
            if i in seen:
                errs.append("%s: duplicate id %s" % (label, i))
            seen.add(i)
        return seen

    tax = d["taxonomy"]
    tx = {k: {x["id"] for x in v} for k, v in tax.items()}
    phases = {p["id"] for p in d["phases"]}
    techs = ids(d["techniques"], r"[A-Z]{3}-\d{2}", "technique")
    ctrls = ids(d["controls"], r"SC-\d{2}", "control")
    effs = ids(d["mission_effects"], r"ME-\d{2}", "mission effect")
    dss = ids(d["data_sources"], r"DS-\d{2}", "data source")
    actors = ids(d["actors"], r"TA-\d{2}", "actor")
    incs = ids(d["incidents"], r"INC-\d{2}", "incident")
    ids(d["attack_paths"], r"AP-\d{2}", "attack path")

    def refs(owner, values, universe, what):
        if not values and what not in ("mission", "incident", "actor"):
            errs.append("%s: no %s listed" % (owner, what))
        for v in values:
            if v not in universe:
                errs.append("%s: unknown %s %r" % (owner, what, v))

    def text(owner, obj, keys):
        for k in keys:
            v = obj.get(k)
            if not isinstance(v, str) or len(v.strip()) < 3:
                errs.append("%s: missing text field %r" % (owner, k))

    for t in d["techniques"]:
        o = t.get("id", "?")
        text(o, t, ["name", "description", "precondition", "detection"])
        if t.get("phase") not in phases or not o.startswith(str(t.get("phase"))):
            errs.append("%s: phase does not match id" % o)
        refs(o, t.get("segments", []), tx["segments"], "segment")
        refs(o, t.get("assets", []), tx["assets"], "asset")
        refs(o, t.get("vectors", []), tx["vectors"], "vector")
        refs(o, t.get("missions", []), tx["missions"], "mission")
        refs(o, t.get("effects", []), effs, "mission effect")
        refs(o, t.get("controls", []), ctrls, "control")
        refs(o, t.get("data_sources", []), dss, "data source")
        if t.get("tier") not in tx["tiers"]:
            errs.append("%s: bad tier" % o)
        if t.get("basis") not in tx["basis"]:
            errs.append("%s: bad evidence basis" % o)
        a = t.get("assessment", {})
        text(o, a, ["question", "evidence", "recovery_test"])
        refs(o, a.get("environments", []), tx["envs"], "test environment")

    for c in d["controls"]:
        text(c["id"], c, ["name", "description", "verify"])
        if c.get("function") not in tx["functions"]:
            errs.append("%s: bad function" % c["id"])
    used = {c for t in d["techniques"] for c in t["controls"]}
    for c in sorted(ctrls - used):
        errs.append("%s: control is not mapped to any technique" % c)
    used = {e for t in d["techniques"] for e in t["effects"]}
    for e in sorted(effs - used):
        errs.append("%s: mission effect is not used by any technique" % e)
    used = {s for t in d["techniques"] for s in t["data_sources"]}
    for s in sorted(dss - used):
        errs.append("%s: data source is not used by any technique" % s)

    for a in d["actors"]:
        o = a["id"]
        text(o, a, ["name", "summary", "motivation", "origin"])
        if a.get("type") not in tx["actor_types"]:
            errs.append("%s: bad actor type" % o)
        if a.get("tier") not in tx["tiers"]:
            errs.append("%s: bad tier" % o)
        refs(o, [m["id"] for m in a.get("techniques", [])], techs, "technique")
        for m in a.get("techniques", []):
            if m.get("basis") not in tx["map_basis"]:
                errs.append("%s: bad mapping basis on %s" % (o, m.get("id")))
        if not a.get("sources"):
            errs.append("%s: no sources" % o)

    for i in d["incidents"]:
        o = i["id"]
        text(o, i, ["title", "summary", "date"])
        refs(o, i.get("actors", []), actors, "actor")
        refs(o, i.get("techniques", []), techs, "technique")
        refs(o, i.get("segments", []), tx["segments"], "segment")
        if i.get("attribution") not in tx["attribution"]:
            errs.append("%s: bad attribution" % o)
        if i.get("kind") not in tx["incident_kinds"]:
            errs.append("%s: bad kind" % o)
        if not i.get("sources"):
            errs.append("%s: no sources" % o)

    order = {p["id"]: p["n"] for p in d["phases"]}
    for p in d["attack_paths"]:
        o = p["id"]
        text(o, p, ["name", "summary"])
        refs(o, [s["technique"] for s in p.get("steps", [])], techs, "technique")
        refs(o, p.get("breakpoints", []), ctrls, "control")
        refs(o, p.get("incidents", []), incs, "incident")
    return errs


def main():
    d = load()
    errs = validate(d)
    for e in errs:
        print("ERROR", e)
    print("%d techniques, %d controls, %d mission effects, %d data sources, %d actors, %d incidents, %d attack paths" % (
        len(d["techniques"]), len(d["controls"]), len(d["mission_effects"]), len(d["data_sources"]),
        len(d["actors"]), len(d["incidents"]), len(d["attack_paths"])))
    if errs:
        sys.exit("%d problem(s) found" % len(errs))
    print("Dataset is consistent.")


if __name__ == "__main__":
    main()
