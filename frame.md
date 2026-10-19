---
name: paper-theatre-risograph
description: A tactile cut-paper picture-book system for a 3-minute animated music video — cream stock, deep navy ink, tomato red, mustard and seafoam, Fraunces display + Space Grotesk labels + Space Mono instrumentation.
colors:
  paper: "#F2E7D1"
  ink: "#16172A"
  navy: "#1B2A55"
  red: "#D4462F"
  mustard: "#E7A93D"
  seafoam: "#83B7A6"
typography:
  display: "Fraunces"
  sans: "Space Grotesk"
  mono: "Space Mono"
spacing:
  margin: 96px
  gutters: [16, 24, 40, 64]
components:
  lyric: "Fraunces 600 / 68–96px / ink on paper / letterpress offset shadow"
  title: "Fraunces 900 italic / 180–260px / tight / paper cut shadow"
  label: "Space Grotesk 700 / 20–28px / 0.14em tracking / uppercase"
  stamp: "Space Mono 700 / 3px double border / rotate −6°..+4°"
---

# Paper Theatre / Risograph

## Overview

A handmade picture-book world: every surface is warm cream paper, every illustration is a
layer cut from construction paper and printed with misregistered riso ink. Type behaves like
rubber stamps, recipe cards and letterpress plates. The mood is Mili: cheerful on the surface,
a little dark underneath, never glossy.

## The Frame

- 16:9. Keep a 96px safe margin. Full-bleed plates are allowed; text lives on paper.
- Images are treated as **printed plates**, not photos: `filter: saturate(.96) contrast(1.02)`,
  a cream tint at 4–8%, and a halftone overlay at 6–10%. Never add glossy gradients or blur.
- Paper objects have a hard 1–3px inset edge and a single soft drop shadow. No glass, no neon,
  no 3D bevels.
- Everything is slightly imperfect: stamps rotate, cards sit 1–2° off-axis, torn edges are
  polygons, rules are hand-ruled.

## Composition Rules

- One dominant plate + one typographic gesture + one moving paper layer per beat.
- Lyrics go lower-left or upper-left, never across a face. Titles can center.
- Keep text to two lines at a time; use Space Mono for numbers, depths, radar callouts.
- Red is voltage: use it for the hot line, the alert, the punch. Never fill a whole frame red
  except for a deliberate one-beat flash.
- Leave breathing room; the song is fast, the frames must not all shout.

## Do

- Cream paper ground (#F2E7D1), navy ink (#16172A), tomato red (#D4462F), mustard (#E7A93D),
  seafoam (#83B7A6).
- Letterpress offset shadows (2–4px, no blur) and paper-cut drop shadows (12–24px, soft).
- Coarse halftone dots, grain, torn-paper edges, visible fibers.
- Fraunces for feeling; Space Grotesk for instruction; Space Mono for machine voice.

## Don't

- Don't use pure white or pure black.
- Don't use glassmorphism, neon glow, chrome, 3D bevels or generic gradient meshes.
- Don't set lyrics in a thin geometric sans; don't center every line.
- Don't cover the character's eyes with type; don't put text over busy coral.
