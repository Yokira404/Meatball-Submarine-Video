# BRIEF — Meatball Submarine (fan MV)

- **Workflow:** music-to-video
- **Flow:** autonomous (user delegated freely; checkpoint summaries only)
- **Deliverable:** one playable HTML composition (`index.html`) + a rendered MP4 preview
- **Music:** `assets/bgm.mp3` — Mili, “Meatball Submarine” (3:11.63, 168 BPM)
- **Canvas:** 1920 × 1080, 30 fps, 16:9
- **Lyrics:** synced to the official LRC timings; displayed as key lines, not a full karaoke rail
- **Story:** a whale-maid runs a one-submarine sandwich delivery service. She cooks, launches,
  crosses the Atlantic, gets ambushed by sharks who take bites out of her sub, fires back with
  condiment torpedoes, survives, watches the customer choose the roast beef submarine instead,
  and still promises to come back tomorrow.
- **Look:** a handmade cut-paper picture book — cream paper, deep navy, tomato red, mustard,
  seafoam, coarse halftone, risograph misregistration, letterpress type. Everything on screen
  is styled as paper, ink, or printed ephemera so the AI illustrations read as one illustrated
  world rather than stock art.
- **Assets:** 16 AI key-art plates generated from the two character reference sheets, held in
  `assets/img/`; custom CSS/SVG paper theatre, bubbles, sonar, speed lines and typography.
- **Non-negotiables:** all assets local (no network at render), deterministic timelines, one
  paused GSAP timeline per frame, full-screen images never crop the character’s face, lyrics
  legible at 1080p, no on-screen text baked into the generated art except diegetic props.
