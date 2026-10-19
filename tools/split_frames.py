#!/usr/bin/env python3
"""Split long frames into more shots without shifting the song.

Part A: same markup, shorter root duration (the later tweens simply never play).
Part B/C: same markup + all tweens, wrapped in an inner GSAP timeline added at
         -offset, so frame-local 0 == the original local `offset` state.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
frames = root / "compositions" / "frames"

SPLITS = [
    # old stem, new stem, new duration, inner offset (None = part A)
    ("04-f4", "04a-f4a", 5.64, None),
    ("04-f4", "04b-f4b", 7.27, 5.64),
    ("08-f8", "08a-f8a", 9.55, None),
    ("08-f8", "08b-f8b", 4.00, 9.55),
    ("10-f10", "10a-f10a", 11.00, None),
    ("10-f10", "10b-f10b", 5.13, 11.00),
    ("10-f10", "10c-f10c", 6.17, 16.13),
    ("11-f11", "11a-f11a", 20.00, None),
    ("11-f11", "11b-f11b", 5.00, 20.00),
    ("13-f13", "13a-f13a", 12.20, None),
    ("13-f13", "13b-f13b", 15.627, 12.20),
]


def wrap_build(text: str, frame_id: str, offset: float) -> str:
    marker = f'HF.frame("{frame_id}", function (tl, root) {{'
    start = text.index(marker)
    open_brace = start + len(marker) - 1
    depth = 0
    i = open_brace
    while i < len(text):
        ch = text[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                break
        i += 1
    if depth != 0:
        raise RuntimeError("unbalanced braces")
    body = text[open_brace + 1:i]
    # indent the wrapper to match the frame script
    wrapped = (
        f'HF.frame("{frame_id}", function (tl, root) {{\n'
        f'          var inner = gsap.timeline();\n'
        f'          (function (tl, root) {{{body}\n'
        f'          }})(inner, root);\n'
        f'          tl.add(inner, {(-offset):.6f});\n'
        f'        }}'
    )
    return text[:start] + wrapped + text[i + 1:]


for old_stem, new_stem, duration, offset in SPLITS:
    src = frames / f"{old_stem}.html"
    text = src.read_text(encoding="utf-8")
    text = text.replace(old_stem, new_stem)
    text = re.sub(r'data-duration="[^"]*"', f'data-duration="{duration:g}"', text, count=1)
    if offset is not None:
        text = wrap_build(text, new_stem, offset)
    out = frames / f"{new_stem}.html"
    out.write_text(text, encoding="utf-8")
    print(f"{out.name}  duration={duration:g}  offset={offset}")
