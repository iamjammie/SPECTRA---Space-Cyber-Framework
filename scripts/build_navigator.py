#!/usr/bin/env python3
"""Build the offline SPECTRA Navigator.

Reads framework/data/*.json, validates it, and injects it into navigator/template.html
to produce the single self-contained index.html at the repository root.

Usage: python3 scripts/build_navigator.py
Needs only the Python standard library.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import validate  # noqa: E402

ROOT = validate.ROOT
PLACEHOLDER = "/*__SPECTRA_DATA__*/null"


def main():
    data = validate.load()
    errs = validate.validate(data)
    if errs:
        for e in errs:
            print("ERROR", e)
        sys.exit("Dataset is not consistent; index.html was not rebuilt.")
    tmpl = (ROOT / "navigator" / "template.html").read_text(encoding="utf-8")
    if PLACEHOLDER not in tmpl:
        sys.exit("placeholder missing from navigator/template.html")
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    out = tmpl.replace(PLACEHOLDER, blob)
    (ROOT / "index.html").write_text(out, encoding="utf-8")
    print("Wrote index.html (%.0f KB, %d techniques)" % (len(out.encode()) / 1024, len(data["techniques"])))
    (ROOT / "docs" / "technique-catalogue.md").write_text(catalogue(data), encoding="utf-8")
    print("Wrote docs/technique-catalogue.md")


def catalogue(d):
    """Plain Markdown listing of every technique, for reading without the navigator."""
    ctl = {c["id"]: c["name"] for c in d["controls"]}
    basis = {b["id"]: b["name"] for b in d["taxonomy"]["basis"]}
    out = ["# SPECTRA technique catalogue", "",
           "Generated from `framework/data/` by `scripts/build_navigator.py`. Do not edit by hand.", ""]
    for p in d["phases"]:
        out += ["## %d. %s" % (p["n"], p["name"]), "", p["desc"], ""]
        for t in d["techniques"]:
            if t["phase"] != p["id"]:
                continue
            out += ["### %s %s" % (t["id"], t["name"]), "", t["description"], "",
                    "- Segments: %s. Tier %d. Evidence: %s." % (", ".join(t["segments"]), t["tier"], basis[t["basis"]]),
                    "- Detection: %s" % t["detection"],
                    "- Controls: %s" % "; ".join("%s %s" % (c, ctl[c]) for c in t["controls"]),
                    "- Assessment question: %s" % t["assessment"]["question"], ""]
    return "\n".join(out)


if __name__ == "__main__":
    main()
