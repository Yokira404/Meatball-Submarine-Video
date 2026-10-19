---
compositionId: meatball-submarine
duration_s: 191.627
canvas: { w: 1920, h: 1080, fps: 30 }
style:
  font: "Fraunces / Space Grotesk / Space Mono"
  palette: ["#F2E7D1", "#16172A", "#1B2A55", "#D4462F", "#E7A93D", "#83B7A6"]
assets: "18 shots • 16 AI key-art plates in assets/img/ • custom SVG/CSS paper layers"
build_notes:
  - "18 panels tile the track exactly"
  - "one paused GSAP timeline per frame, registered under the frame stem"
  - "every frame is a <template> sub-composition"
  - "lyrics are anchored to the official LRC timestamps"
  - "all motion is seek-safe; no Math.random, no network, no CSS animations"
  - "the 5 added cuts are at 89.10, 114.70, 119.83, 146.00 and 176.00 — all existing musical / scene boundaries"
avoid:
  - "generic lyric-video karaoke bars"
  - "stock AI art look, glossy 3D, neon"
  - "tiny text, text over faces, more than two lyric lines at once"
---

# STORYBOARD — Meatball Submarine (18 panels)

One continuous night at sea, now cut into eighteen shots: cook → launch → cross →
descend → season → alarm → shark attack → counterattack → pierce litany → power-up →
menu parade → race → the choice → tomorrow → curtain.

## Frame 1 — f1

- src: compositions/frames/01-f1.html
- duration: 11.300s
- span_sec: [0.000, 11.300]
- pacing: phrase_flow
- mood: [cinematic, dreamy, playful]
- feel: slow held underwater pad; one moonlit gesture
- visual: `title-dark` plate; moon upper right, small sandwich sub lower left. Title lockup
  centre-left. A slow push-in, paper bubbles, a red stamp on the downbeat at 4.2s. Cream
  iris closes at the end.

### Groups

- **g1** — free_design
  - span_sec: [0.000, 11.300]
  - free_design: { dominant_system: "paper-theatre title card", primitives: ["plate-drift", "letterpress-rise", "stamp-land", "bubble-field", "iris-out"], density_topology: "single gesture, one hold" }
  - anchors: [0.37, 4.20, 7.60, 10.40]
  - copy: ["MILI", "MEATBALL SUBMARINE", "a whale-maid delivery service"]
  - notes: "No lyrics. Cream type on navy; one tomato-red accent."

## Frame 2 — f2

- src: compositions/frames/02-f2.html
- duration: 11.100s
- span_sec: [11.300, 22.400]
- pacing: beat_cut
- mood: [warm, playful]
- feel: verse 1 — one reveal per vocal phrase, steam curling on the offbeats
- visual: `kitchen` plate. Push-in from the porthole to the pot, then the maid's face on
  “How exciting!”. Recipe card lower left; ingredient tags pop. Ends with a cream steam wipe.

### Groups

- **g1** — free_design
  - span_sec: [11.300, 19.750]
  - free_design: { dominant_system: "recipe-card lyric over a warm galley plate", primitives: ["plate-push-in", "recipe-card-slide", "ingredient-tag-pop", "steam-drift"], density_topology: "one lyric line + two tags per phrase" }
  - anchors: [11.30, 13.12, 15.30, 18.00]
  - copy: ["Tomato sauce", "simmering with onion blocks"]
- **g2** — free_design
  - span_sec: [19.750, 22.400]
  - free_design: { dominant_system: "stamp burst on the exclamation", primitives: ["stamp-land", "paper-confetti", "plate-push-in"], density_topology: "one hit" }
  - anchors: [19.75, 21.00]
  - copy: ["How exciting!"]

## Frame 3 — f3

- src: compositions/frames/03-f3.html
- duration: 11.240s
- span_sec: [22.400, 33.640]
- pacing: beat_cut
- mood: [playful, warm, hype]
- feel: pre-chorus build — each ingredient line lands on its own beat, the sandwich becomes a vessel
- visual: `drydock` plate. Pan from the giant sub hull to the maid on the ladder, then pull
  back. Butter, marinara, meatball and delivery callouts slam on. A navy hatch iris closes.

### Groups

- **g1** — free_design
  - span_sec: [22.400, 28.300]
  - free_design: { dominant_system: "assembly-line callouts on a drydock plate", primitives: ["plate-pan", "callout-leader-line", "label-pop", "butter-drips"], density_topology: "two callouts per bar" }
  - anchors: [22.40, 25.25, 27.10]
  - copy: ["Butter up the sourdough submarine", "Marinara flavoured bedding"]
- **g2** — free_design
  - span_sec: [28.300, 31.470]
  - free_design: { dominant_system: "meatball seat manifest", primitives: ["grid-count", "meatball-pop", "plate-push"], density_topology: "count-up grid" }
  - anchors: [28.30, 30.00]
  - copy: ["Meatball seats in my submarine", "x 12"]
- **g3** — free_design
  - span_sec: [31.470, 33.640]
  - free_design: { dominant_system: "delivery stamp and hatch wipe", primitives: ["stamp-land", "paper-iris"], density_topology: "one hit + transition" }
  - anchors: [31.47, 33.10]
  - copy: ["Delivery under the sea"]

## Frame 4 — f4

- src: compositions/frames/04-f4.html
- duration: 5.640s
- span_sec: [33.640, 39.280]
- pacing: beat_cut
- mood: [hype, playful, cinematic]
- feel: chorus 1 — full-band lift, line changes on every vocal phrase, the sub surfs the Atlantic
- visual: `launch` plate. Fast dolly-out, parallax bubbles and paper waves, speed lines on the
  kick. Lyrics on the left as cream strips. Ends on “To show you what I've achieved”.

### Groups

- **g1** — free_design
  - span_sec: [33.640, 39.280]
  - free_design: { dominant_system: "chorus paper-strip stack over a launch plate", primitives: ["plate-dolly-out", "strip-slam", "speed-lines", "bubble-parallax"], density_topology: "one strip per phrase, stacked" }
  - anchors: [33.64, 35.04, 37.26]
  - copy: ["So I leap", "And swim against Atlantic stream", "To show you what I've achieved"]

## Frame 4b — f4b

- src: compositions/frames/04b-f4b.html
- duration: 7.270s
- span_sec: [39.280, 46.550]
- pacing: beat_cut
- mood: [cinematic, hype, dreamy]
- feel: “Going deep” — a new descent plate, then the feast refrain and two stamps
- visual: NEW `descent` plate (generated). The sandwich sub sinks through the abyss, seen
  from above, the whale-maid in the glowing porthole, jellyfish and sonar rings. “Going deep”
  navy band; mustard “Tonight we'll make dinner a feast”; two “Just count it on me” stamps.
  Cream iris into the coral valley.

### Groups

- **g1** — free_design
  - span_sec: [39.280, 46.550]
  - free_design: { dominant_system: "descent plate with a deep-water colour grade", primitives: ["plate-sink", "navy-band", "strip-slam", "stamp-land", "cream-iris"], density_topology: "one held descent, two stamps" }
  - anchors: [39.28, 40.71, 42.70, 44.11, 46.20]
  - copy: ["Going deep", "Tonight we'll make dinner a feast", "Just count it on me", "Just count it on me"]

## Frame 5 — f5

- src: compositions/frames/05-f5.html
- duration: 10.950s
- span_sec: [46.550, 57.500]
- pacing: phrase_flow
- mood: [dreamy, warm, elegant]
- feel: bridge — floating, legato, jellyfish and light; lyrics drift rather than cut
- visual: `coral` plate. Very slow lateral drift; foreground jellyfish and bubbles parallax.
  Lyrics lower left in italic Fraunces. A lone lantern on “Wait for me”. Bubble dissolve.

### Groups

- **g1** — free_design
  - span_sec: [46.550, 52.150]
  - free_design: { dominant_system: "drifting italic lyric over a coral valley", primitives: ["golden-drift", "jellyfish-parallax", "soft-dissolve"], density_topology: "one line per 2 bars" }
  - anchors: [46.55, 48.55, 50.93]
  - copy: ["Soaring through the barnacle valleys", "And peachy coral reefs", "Wait for me"]
- **g2** — free_design
  - span_sec: [52.150, 57.500]
  - free_design: { dominant_system: "feast refrain as floating paper lanterns", primitives: ["lantern-rise", "soft-dissolve", "bubble-dissolve"], density_topology: "two lines, then a held breath" }
  - anchors: [52.15, 54.13, 55.43, 57.00]
  - copy: ["Tonight we'll make dinner a feast", "Just count it on me", "Just count it on me"]

## Frame 6 — f6

- src: compositions/frames/06-f6.html
- duration: 11.300s
- span_sec: [57.500, 68.800]
- pacing: beat_cut
- mood: [cinematic, tense, dreamy]
- feel: instrumental descent — sonar pings, depth gauge, the sub dropping through black water
- visual: `abyss` plate in a porthole. Slow sink; sonar rings pulse. Space Mono depth readout
  counts 200 → 1,860 m. “No signal” stamp. Mustard flash into the galley.

### Groups

- **g1** — free_design
  - span_sec: [57.500, 68.800]
  - free_design: { dominant_system: "sonar instrumentation over an abyss plate", primitives: ["depth-count", "sonar-ring", "plate-sink", "blip-ping", "colour-flash"], density_topology: "one ping per phrase" }
  - anchors: [57.50, 59.64, 61.79, 63.93, 66.08, 68.60]
  - copy: ["DEPTH 0200 M", "DEPTH 0860 M", "DEPTH 1860 M", "NO SIGNAL"]

## Frame 7 — f7

- src: compositions/frames/07-f7.html
- duration: 10.750s
- span_sec: [68.800, 79.550]
- pacing: beat_cut
- mood: [playful, warm, hype]
- feel: verse 2 — bright and tactile, cheese snow and a two-word punchline
- visual: `parmesan` plate. Push through the cheese blizzard toward the maid's laughing face.
  “PARMESAN CRISPY SKIN” display; “Tasty dilemma / Carbohydrates” fast stamps. Cheese sneeze.

### Groups

- **g1** — free_design
  - span_sec: [68.800, 74.200]
  - free_design: { dominant_system: "food-poster supers over a cheese-blizzard plate", primitives: ["plate-push-in", "cheese-snow", "display-word-slam"], density_topology: "two display words, one hold" }
  - anchors: [68.80, 71.50, 73.90]
  - copy: ["Parmesan crispy skin"]
- **g2** — free_design
  - span_sec: [74.200, 79.550]
  - free_design: { dominant_system: "double stamp punchline", primitives: ["double-stamp", "cheese-burst", "paper-flash"], density_topology: "two hits then a sneeze wipe" }
  - anchors: [74.20, 76.00, 79.20]
  - copy: ["Tasty dilemma", "Carbohydrates"]

## Frame 8 — f8a

- src: compositions/frames/08a-f8a.html
- duration: 9.550s
- span_sec: [79.550, 89.100]
- pacing: beat_cut
- mood: [playful, tense, hype]
- feel: shipping montage — the checklist fills, then “Prime shipping” slams
- visual: `parmesan` plate reframed as a packing table; shipping manifest ticks on each vocal.
  Barcode, priority stamp, packing slip. Ends on the ship/radar cut at 89.10.

### Groups

- **g1** — free_design
  - span_sec: [79.550, 89.100]
  - free_design: { dominant_system: "packing-slip typography over a warm plate", primitives: ["manifest-slide", "checkbox-tick", "plate-pan", "label-stack"], density_topology: "checklist accumulates" }
  - anchors: [79.55, 82.75, 85.96, 88.60]
  - copy: ["Season up the gluten-free submarine", "Slather it in mascarpone cheese", "Meatball seats in my submarine", "Prime shipping under the sea"]

## Frame 9 — f8b

- src: compositions/frames/08b-f8b.html
- duration: 4.000s
- span_sec: [89.100, 93.100]
- pacing: beat_cut
- mood: [tense, aggressive]
- feel: radar alarm — four bars of pure panic before the sharks
- visual: `radar` plate, full screen. Green sweep → red alert; shark count card; “BEEP BEEP
  BEEP”; “What's going on”; red flash into the attack.

### Groups

- **g1** — free_design
  - span_sec: [89.100, 93.100]
  - free_design: { dominant_system: "radar-room alert", primitives: ["radar-sweep", "blip-appear", "alarm-flash", "mono-type"], density_topology: "accelerating blips" }
  - anchors: [89.10, 90.99, 92.20]
  - copy: ["Beep beep beep", "What's going on", "RADARS WENT OFF"]

## Frame 10 — f9

- src: compositions/frames/09-f9.html
- duration: 10.600s
- span_sec: [93.100, 103.700]
- pacing: beat_cut
- mood: [aggressive, tense, playful]
- feel: shark attack — comic-book violence, screen shake, jaws, one line per hit
- visual: `shark` plate. Push-ins and pulls on each phrase; red flash on “biting”; giant type
  enters from the edges. Ends on a black torn wedge.

### Groups

- **g1** — free_design
  - span_sec: [93.100, 99.800]
  - free_design: { dominant_system: "attack callouts over a shark plate", primitives: ["screen-shake", "jaw-snap", "alert-flash", "type-slam"], density_topology: "one hit per lyric" }
  - anchors: [93.10, 94.48, 96.56, 97.83]
  - copy: ["Radars went off", "Showing the sharks on the screen", "Closing in", "The sharks opened up their mouths"]
- **g2** — free_design
  - span_sec: [99.800, 103.700]
  - free_design: { dominant_system: "bite refrain with torn-paper cuts", primitives: ["double-hit", "torn-wipe", "red-flash"], density_topology: "two hits + exit" }
  - anchors: [99.80, 101.35, 103.30]
  - copy: ["They're biting on me", "They're biting on me"]

## Frame 11 — f10a

- src: compositions/frames/10a-f10a.html
- duration: 11.000s
- span_sec: [103.700, 114.700]
- pacing: beat_cut
- mood: [aggressive, hype, cinematic]
- feel: damage and defiance — mayo and cheddar torn off, then “But I'll fight your enemies”
- visual: `fight-retouch` plate. Mayo/cheddar blobs fly off with labels; damage report card;
  “I may be weak” chip; “But I'll fight your enemies” big; two “count on me” stamps.

### Groups

- **g1** — free_design
  - span_sec: [103.700, 114.700]
  - free_design: { dominant_system: "damage callouts and condiment counterattack", primitives: ["blob-tear", "stamp-land", "speed-line-burst", "screen-shake"], density_topology: "two damage beats, then a build" }
  - anchors: [103.70, 105.90, 108.06, 109.75, 111.35, 112.75]
  - copy: ["Licked off my mayonnaise dressing", "Tored off my cheddar sliced cheese", "I may be weak", "But I'll fight your enemies", "So count it on me", "Just count it on me"]

## Frame 12 — f10b

- src: compositions/frames/10b-f10b.html
- duration: 5.130s
- span_sec: [114.700, 119.830]
- pacing: beat_cut
- mood: [aggressive, hype]
- feel: rapid-fire pierce litany — a wall of spears and four PIERCE stamps
- visual: `fight-retouch` plate zoomed into the torpedoes. Thin paper spears shoot across;
  four PIERCE stamps alternate cream/mustard/red; “All their tiny brains” at 117.4.

### Groups

- **g1** — free_design
  - span_sec: [114.700, 119.830]
  - free_design: { dominant_system: "wall of spears for the pierce litany", primitives: ["spear-grid", "type-rush", "paper-shred"], density_topology: "accumulate to a wall" }
  - anchors: [114.70, 115.85, 117.00, 117.40, 118.15]
  - copy: ["Pierce and pierce and pierce and pierce it through", "All their tiny brains"]

## Frame 13 — f10c

- src: compositions/frames/10c-f10c.html
- duration: 6.170s
- span_sec: [119.830, 126.000]
- pacing: beat_cut
- mood: [hype, cinematic]
- feel: the power-up — couplets, then “I'm invincible / Indestructible” in a sunburst
- visual: `invincible` plate. Couplets left; rotating rays; “I'm invincible” at 122.86,
  “Indestructible” at 124.25; white flash.

### Groups

- **g1** — free_design
  - span_sec: [119.830, 126.000]
  - free_design: { dominant_system: "duel couplets into a sunburst power-up", primitives: ["split-couplet", "sunburst", "title-slam", "flash"], density_topology: "two couplets, one held apex" }
  - anchors: [119.83, 121.47, 122.86, 124.25, 125.80]
  - copy: ["An eye for eye", "And arm for arm", "I'm invincible", "Indestructible"]

## Frame 14 — f11a

- src: compositions/frames/11a-f11a.html
- duration: 11.180s
- span_sec: [126.000, 137.180]
- pacing: beat_cut
- mood: [playful, hype, elegant]
- feel: instrumental fleet reveal with a menu counter
- visual: `menu` plate. Wide fleet reveal; the menu board and “08 submarines” counter fill in.
  Hands off to the new close-up menu board at 137.18.

### Groups

- **g1** — free_design
  - span_sec: [126.000, 137.180]
  - free_design: { dominant_system: "slow fleet reveal with a menu counter", primitives: ["plate-drift", "row-highlight", "counter-tick", "steam"], density_topology: "quiet accumulation" }
  - anchors: [126.00, 130.00, 134.00, 137.18]
  - copy: ["THE FLEET", "08 SUBMARINES", "ALL FRESHLY BAKED"]

## Frame 14b — f11a2

- src: compositions/frames/11a2-f11a2.html
- duration: 8.820s
- span_sec: [137.180, 146.000]
- pacing: beat_cut
- mood: [playful, hype, elegant]
- feel: rapid menu litany — one giant item stamp per lyric, accelerating
- visual: NEW `menuboard` plate (generated). The whale-maid presents a giant illustrated menu;
  HAM / BLT / SALAMI / VEGGIE & CHEESE / SO MANY SUBMARINES / MARINE MARINE SUB / AVOCADO /
  ROAST BEEF / TERIYAKI slam on in red, ink and cream. “Menu complete” and a checkered wipe.

### Groups

- **g1** — free_design
  - span_sec: [137.180, 146.000]
  - free_design: { dominant_system: "giant menu-item supers over a close menu-board plate", primitives: ["menu-stamp", "row-flash", "colour-chip", "checker-wipe"], density_topology: "one item per lyric, accelerating" }
  - anchors: [137.18, 138.00, 138.70, 139.40, 140.30, 141.37, 142.91, 144.30, 145.29]
  - copy: ["Ham", "BLT", "Salami", "Veggie & cheese", "So many submarines", "Marine marine sub", "Avocado", "Roast beef", "And teriyaki"]

## Frame 15 — f11b

- src: compositions/frames/11b-f11b.html
- duration: 5.000s
- span_sec: [146.000, 151.000]
- pacing: beat_cut
- mood: [hype, playful]
- feel: starting-flag race launch — checkered border, GO, engine shake
- visual: `race` plate. Checkered paper borders; giant GO; starting-grid chip; speed lines;
  white flash into the final chorus.

### Groups

- **g1** — free_design
  - span_sec: [146.000, 151.000]
  - free_design: { dominant_system: "starting-flag race launch", primitives: ["checker-wipe", "speed-line-burst", "engine-shake", "plate-push"], density_topology: "one burst, one hold" }
  - anchors: [146.00, 147.20, 150.72]
  - copy: ["GO"]

## Frame 16 — f12

- src: compositions/frames/12-f12.html
- duration: 6.850s
- span_sec: [151.000, 157.850]
- pacing: beat_cut
- mood: [hype, playful, cinematic]
- feel: final-chorus race — maximum forward motion, one line per phrase
- visual: `race` plate. “So I leap” paper banner; speed strips; speedometer; the race against
  the roast beef and BLT submarines. Ends as “Tonight…” begins.

### Groups

- **g1** — free_design
  - span_sec: [151.000, 157.850]
  - free_design: { dominant_system: "race-poster supers with speed lines", primitives: ["speed-line-burst", "plate-push", "type-slam", "checker-wipe"], density_topology: "one line per phrase, accelerating" }
  - anchors: [151.00, 152.16, 154.35, 156.55]
  - copy: ["So I leap", "And race against those submarines", "To show you what I've achieved", "Increased speed"]

## Frame 16b — f12b

- src: compositions/frames/12b-f12b.html
- duration: 5.950s
- span_sec: [157.850, 163.800]
- pacing: beat_cut
- mood: [hype, playful, cinematic]
- feel: finish line burst, then the direct-address portrait
- visual: NEW `finish` plate (generated) for 2.1s — the sub bursts through a checkered banner,
  confetti, the whale-maid cheering. Hard cut to `portrait` for “So cheer for me, please /
  Just cheer for me, please”. Navy fade.

### Groups

- **g1** — free_design
  - span_sec: [157.850, 160.000]
  - free_design: { dominant_system: "finish-line burst with checkered paper borders", primitives: ["confetti-burst", "checker-wipe", "stamp-land", "hard-cut"], density_topology: "one burst, one cut" }
  - anchors: [157.85, 159.92]
  - copy: ["Tonight we'll make dinner a feast"]
- **g2** — free_design
  - span_sec: [160.000, 163.800]
  - free_design: { dominant_system: "direct-address portrait", primitives: ["spotlight", "soft-rise", "freeze"], density_topology: "one held look" }
  - anchors: [159.92, 161.40, 163.60]
  - copy: ["So cheer for me please", "Just cheer for me please"]

## Frame 17 — f13a

- src: compositions/frames/13a-f13a.html
- duration: 1.890s
- span_sec: [163.800, 165.690]
- pacing: phrase_flow
- mood: [elegant, dark, warm]
- feel: the first beat of the choice — a held wide shot
- visual: `choice` plate. “Instead of looking at me” as the giant leviathan leans toward the
  roast beef submarine. Hard cut to the untouched close-up at 165.69.

### Groups

- **g1** — free_design
  - span_sec: [163.800, 165.690]
  - free_design: { dominant_system: "scale-contrast banquet tableau", primitives: ["spotlight", "plate-hold", "soft-rise"], density_topology: "one long line" }
  - anchors: [163.80, 165.69]
  - copy: ["Instead of looking at me"]

## Frame 17b — f13a2

- src: compositions/frames/13a2-f13a2.html
- duration: 10.310s
- span_sec: [165.690, 176.000]
- pacing: phrase_flow
- mood: [elegant, dark, warm, dreamy]
- feel: the untouched sub, then the sunrise promise
- visual: NEW `untouched` plate (generated): the meatball sub on a silver tray, the leviathan
  shadow and roast beef behind, the maid's hand at the edge, a creased paper heart. “You've
  decided on the roast beef submarine” on a paper card. Crossfade to `tomorrow` at 169.1:
  “Tomorrow I'll come back again / So wait for me please / Just wait for me please”.
  Peach flash into the curtain call.

### Groups

- **g1** — free_design
  - span_sec: [165.690, 169.100]
  - free_design: { dominant_system: "untouched-sub close-up with a paper order card", primitives: ["spotlight", "plate-push", "heart-crease", "soft-dissolve"], density_topology: "one long line, one held object" }
  - anchors: [165.69, 167.20, 169.10]
  - copy: ["You've decided on the roast beef submarine"]
- **g2** — free_design
  - span_sec: [169.100, 176.000]
  - free_design: { dominant_system: "sunrise promise with a paper letter", primitives: ["sunrise-dissolve", "soft-rise", "bubble-drift", "stamp-land"], density_topology: "one line per bar" }
  - anchors: [169.10, 171.30, 172.80, 175.50]
  - copy: ["Tomorrow I'll come back again", "So wait for me please", "Just wait for me please"]

## Frame 18 — f13b

- src: compositions/frames/13b-f13b.html
- duration: 15.627s
- span_sec: [176.000, 191.627]
- pacing: phrase_flow
- mood: [warm, elegant, dreamy]
- feel: curtain call — the stage closes, the title holds through the silence
- visual: `endcard` plate. Theatre curtains, warm footlights, paper stars. The title plaque
  lands at 177.2; holds; fades to black by 191.4.

### Groups

- **g1** — free_design
  - span_sec: [176.000, 191.627]
  - free_design: { dominant_system: "curtain call end card", primitives: ["curtain-close", "footlights", "paper-stars", "fade-to-black"], density_topology: "one held card" }
  - anchors: [176.00, 177.20, 180.00, 189.40, 191.40]
  - copy: ["MEATBALL SUBMARINE", "Mili — Miracle Milk", "a paper-theatre film", "for everyone who waits for tomorrow"]
