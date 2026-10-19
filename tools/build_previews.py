#!/usr/bin/env python3
"""Build standalone single-frame preview pages from HyperFrames <template> frames.

Preview lives at analysis/previews/ — same depth as compositions/frames/, so all
../../assets/... URLs keep working.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
frames = sorted((root / "compositions" / "frames").glob("*.html"))
outdir = root / "analysis" / "previews"
outdir.mkdir(parents=True, exist_ok=True)

for f in frames:
    if f.name.endswith(".preview.html"):
        continue
    text = f.read_text(encoding="utf-8")
    m = re.search(r"<template>([\s\S]*)</template>", text)
    if not m:
        print("skip (no template):", f)
        continue
    body = m.group(1)
    out = outdir / (f.stem + ".preview.html")
    out.write_text(
        "<!doctype html>\n<html lang=\"en\">\n<head>\n"
        "<meta charset=\"UTF-8\" />\n"
        "<script src=\"../../assets/gsap.min.js\"></script>\n"
        f"<title>{f.stem} preview</title>\n"
        "<style>html,body{width:1920px;height:1080px;overflow:hidden;margin:0;background:#000}#root{position:absolute;inset:0;width:1920px;height:1080px;overflow:hidden}</style>\n"
        "</head>\n<body>\n"
        + body
        + "\n</body>\n</html>\n",
        encoding="utf-8",
    )
    print("wrote", out.relative_to(root))
