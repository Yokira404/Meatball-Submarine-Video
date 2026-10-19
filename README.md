# Meatball Submarine — a paper-theatre music video

A 3:11 animated music video for **Mili — “Meatball Submarine”**, built as an HTML
composition and rendered to MP4.

The whale-maid runs a one-submarine sandwich delivery service. She cooks, launches,
crosses the Atlantic, gets ambushed by sharks who take bites out of her sub, fires back
with condiment torpedoes, survives, watches the customer choose the roast beef submarine
instead — and still promises to come back tomorrow.

## Watch it

### The rendered film (easiest)

```
renders/meatball-submarine-web.mp4    # 136 MB, starts playing immediately
renders/meatball-submarine.mp4        # 592 MB master, higher bitrate
```

1920 × 1080 · 30 fps · 03:11.63 · H.264 + AAC · with the full track.

### The storyboard contact sheet

```
renders/storyboard-contact-sheet.jpg
```

16 frames pulled from the finished MP4, with scene names and timestamps.

### The portable HTML player

The player loads the 13 animated scenes in iframes and keeps its own audio clock, so it
plays exactly like the render and supports seeking.

```bash
node serve.cjs
# open http://127.0.0.1:8080/player.html
```

On Windows you can also double-click `view.cmd`.

> Serving over HTTP matters: browsers block cross-file access from `file://`, so scenes
> will not load if you open `player.html` directly.

### The HyperFrames project

`index.html` is the authored composition (18 sub-compositions, one paused GSAP timeline
per frame, BGM on track 11). To open it in the HyperFrames preview / Studio:

```bash
npx hyperframes preview .
```

To re-render:

```bash
npx hyperframes render . -q looks -o renders/meatball-submarine.mp4 --fps 30
```

### Editing

- Lyric timings, story beats and shot notes live in `STORYBOARD.md`.
- Each scene is one file in `compositions/frames/` (18 panels, `01-f1.html` … `13b-f13b.html`).
- After editing a frame, rebuild the player's scene files with
  `python tools/build_previews.py` (stdlib only), then reload `player.html`.
- Re-render with the command above. The 18 frames tile the track exactly; keep
  `duration_s = 191.627` in `STORYBOARD.md` if you re-run the plan validator.

## The look

A handmade cut-paper picture book: warm cream stock, deep navy ink, tomato red, mustard,
seafoam; risograph misregistration, coarse halftone, torn edges, letterpress type. All
key art is generated in that single style from the supplied whale-maid reference sheets,
then composed with paper layers, stamps, receipt cards, radar scopes, speed lines and
SVG confetti so the AI plates read as one illustrated world rather than stock art.

Type: **Fraunces** (feeling), **Space Grotesk** (instruction), **Space Mono** (machine
voice), all vendored under `assets/fonts/`.

## Structure

```
index.html                     HyperFrames root composition
player.html                    portable iframe player + audio
serve.cjs                      tiny static server for the player
STORYBOARD.md                  the 18-panel shot plan, lyric timings, visual notes
frame.md                       brand / palette / typography rules
audiomap.json                  beat, phrase and section analysis
assets/bgm.mp3                 Mili — Meatball Submarine
assets/img/                    the 16 key-art plates + grain
assets/fonts/                  vendored Fraunces / Space Grotesk / Space Mono
assets/base.css                shared paper-theatre system
assets/hf.js                   deterministic GSAP helpers
compositions/frames/           18 panel files, 01-f1.html … 13b-f13b.html
renders/meatball-submarine.mp4 the rendered film (master)
renders/meatball-submarine-web.mp4 the lighter web encode
renders/storyboard-contact-sheet.jpg
```

## Shot list

| # | time | scene |
|---|------|-------|
| 01 | 0:00 | Overture — moonlit title |
| 02 | 0:11 | The galley — tomato sauce, recipe card, “How exciting!” |
| 03 | 0:22 | Drydock 03 — butter, marinara, 12 meatball seats |
| 04 | 0:33 | “So I leap” — launch into the Atlantic |
| 05 | 0:46 | Coral valley — jellyfish, feast, “Wait for me” |
| 06 | 0:57 | The deep — sonar porthole, depth gauge, “No signal” |
| 07 | 1:08 | Parmesan — cheese snow, “Tasty dilemma / Carbohydrates” |
| 08 | 1:19 | Prime shipping — packing slip, barcode, checklist |
| 09 | 1:29 | Radar alarm — “Beep beep beep / What's going on” |
| 10 | 1:33 | Sharks — “They're biting on me” |
| 11 | 1:43 | Damage — mayo/cheddar torn off, “But I'll fight your enemies” |
| 12 | 1:54 | Pierce — a wall of spears, “All their tiny brains” |
| 13 | 1:59 | Invincible — sunburst, “I'm invincible / Indestructible” |
| 14 | 2:06 | The fleet — menu parade, nine submarines |
| 15 | 2:26 | The race — checkered flags, “GO” |
| 16 | 2:31 | Final chorus — the race, then the direct-address portrait |
| 17 | 2:43 | The choice / tomorrow — the roast beef, the promise |
| 18 | 2:56 | Curtain call — the title holds through the silence |

## Production notes

- **Lyric timing** is taken from the official LRC (e.g. 00:11.30 “Tomato sauce…”, 01:33.10
  “Radars went off”), converted to frame-local seconds. The track is 168 BPM; the frame
  cuts are on phrase / section boundaries and the type lands on the vocal.
- **Image generation:** the local ComfyUI API was not running and no ComfyUI install was
  found on this machine, so the character plates were generated through the configured
  Labnana API — `gemini-3-pro-image` (NanoBanana Pro) with the two character reference
  sheets, 2K, 16:9 — and one plate (`fight`) was retouched with `gpt-image-2` to remove
  the “BLT” lettering. The stylization is intentional: the whole film is one paper-collage
  print world, with type and paper mechanics doing the storytelling between plates.
- **Blender:** the Blender plugin was available, but the final visual language is 2D
  cut-paper; no 3D insert was used. `STORYBOARD.md` leaves room for a 3D periscope insert
  if you want to extend it.
- **Checked** with `npx hyperframes check . --snapshots`: 0 errors, 0 layout failures,
  3 contrast warnings (the oversized scarlet title words over painted plates — they carry
  a paper outline and remain legible). 5 review snapshots inspected. Final render verified
  with `ffprobe` (1920×1080, 30 fps, 191.63 s, AAC audio).
- **Determinism:** no `Math.random`, no network fetches at render time; every bubble,
  cheese flake and confetti piece is seeded from its index. All fonts/images/audio are
  local.
- **Git checkpoint:** the original 13-panel cut is preserved at tag
  `checkpoint-13-frames` (commit `a9e3095`). `main` now carries the 18-panel cut.

## Credits

- Music & lyrics: **Mili** — “Meatball Submarine”, from *Miracle Milk* (2015).
- Character reference sheets supplied by the user.
- This is a fan-made, non-commercial paper-theatre interpretation.
