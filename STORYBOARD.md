---
compositionId: meatball-submarine
duration_s: 191.627
canvas: { w: 1920, h: 1080, fps: 30 }
style:
  font: "Fraunces / Space Grotesk / Space Mono"
  palette: ["#F2E7D1", "#16172A", "#1B2A55", "#D4462F", "#E7A93D", "#83B7A6"]
assets: "16 AI key-art plates in assets/img/ + custom SVG/CSS paper layers; all local"
build_notes:
  - "one paused GSAP timeline per frame, registered under the frame stem"
  - "every frame is a <template> sub-composition; heads are discarded by the runtime"
  - "lyrics are anchored to the official LRC timestamps listed below, converted to frame-local seconds"
  - "all motion is fromTo / seek-safe; no Math.random, no network, no CSS animations"
  - "frame-to-frame is a hard cut; each frame opens on a matching colour/paper state from the previous frame's last beat"
avoid:
  - "generic lyric-video karaoke bars"
  - "stock AI art look, glossy 3D, neon"
  - "tiny text, text over faces, more than two lyric lines at once"
---

# STORYBOARD — Meatball Submarine

A paper-theatre undersea delivery musical. Thirteen frames, one continuous night at sea: cook →
launch → cross → descend → season → alarm → shark attack → counterattack → menu parade → race →
the choice → tomorrow → curtain.

## Frame 1 — f1

- src: compositions/frames/01-f1.html
- duration: 11.300s
- span_sec: [0.000, 11.300]
- pacing: phrase_flow
- mood: [cinematic, dreamy, playful]
- feel: slow held underwater pad with a single moonlit gesture; no lyric until the last beat
- visual: `title-dark` plate. Moon upper right, tiny sandwich sub lower left. Title lockup centre-left.
  A slow push-in, paper bubbles rising, a red stamp lands on the downbeat at 4.2s. At 10.4s a cream
  paper iris closes to a circle and the title holds.

### Groups

- **g1** — free_design
  - span_sec: [0.000, 11.300]
  - free_design: { dominant_system: "paper-theatre title card", primitives: ["plate-drift", "letterpress-rise", "stamp-land", "bubble-field", "iris-out"], density_topology: "single gesture, one hold" }
  - anchors: [0.37, 4.20, 7.60, 10.40]
  - copy: ["MILI", "MEATBALL SUBMARINE", "a whale-maid delivery service", "lyrics & music by Mili"]
  - notes: "No lyrics yet. Keep the moon and title clean. Type is cream on navy; one tomato-red accent line."

## Frame 2 — f2

- src: compositions/frames/02-f2.html
- duration: 11.100s
- span_sec: [11.300, 22.400]
- pacing: beat_cut
- mood: [warm, playful]
- feel: verse 1 — a cosy groove, one reveal per vocal phrase, steam curling on the offbeats
- visual: `kitchen` plate. Slow push-in from the porthole to the pot, then to the maid's face on
  “How exciting!”. Recipe card lower left; ingredient tags pop on the beat. Steam and bubble paper
  layers drift. Ends with a cream steam wipe.

### Groups

- **g1** — free_design
  - span_sec: [11.300, 19.750]
  - free_design: { dominant_system: "recipe-card lyric over a warm galley plate", primitives: ["plate-push-in", "recipe-card-slide", "ingredient-tag-pop", "steam-drift"], density_topology: "one lyric line + two tags per phrase" }
  - anchors: [11.30, 13.12, 15.30, 18.00]
  - copy: ["Tomato sauce", "simmering with onion blocks"]
  - notes: "Two-line lyric at lower left, 84px Fraunces. Tags: TOMATO / ONION / MEATBALL, rotated."
- **g2** — free_design
  - span_sec: [19.750, 22.400]
  - free_design: { dominant_system: "stamp burst on the exclamation", primitives: ["stamp-land", "paper-confetti", "plate-push-in"], density_topology: "one hit" }
  - anchors: [19.75, 21.00]
  - copy: ["How exciting!"]
  - notes: "Big tomato-red stamp, rotated −4°, lands with the vocal. Steam wipe covers the last 0.4s."

## Frame 3 — f3

- src: compositions/frames/03-f3.html
- duration: 11.240s
- span_sec: [22.400, 33.640]
- pacing: beat_cut
- mood: [playful, warm, hype]
- feel: pre-chorus build — each ingredient line lands on its own beat, the sandwich grows into a vessel
- visual: `drydock` plate. Camera pans from the giant sub hull to the maid on the ladder, then pulls
  back to reveal the full sandwich. Butter, marinara, meatball and delivery labels slam on. A red
  “DELIVERY: UNDER THE SEA” stamp closes the frame; the sub's dark hatch fills the screen.

### Groups

- **g1** — free_design
  - span_sec: [22.400, 28.300]
  - free_design: { dominant_system: "assembly-line callouts on a drydock plate", primitives: ["plate-pan", "callout-leader-line", "label-pop", "butter-drips"], density_topology: "two callouts per bar, left to right" }
  - anchors: [22.40, 25.25, 27.10]
  - copy: ["Butter up the sourdough submarine", "Marinara flavoured bedding"]
  - notes: "Callout leader lines point to the hull. Type 64–76px, cream cards. Butter drips are SVG."
- **g2** — free_design
  - span_sec: [28.300, 31.470]
  - free_design: { dominant_system: "meatball seat manifest", primitives: ["grid-count", "meatball-pop", "plate-push"], density_topology: "count-up grid" }
  - anchors: [28.30, 30.00]
  - copy: ["Meatball seats in my submarine", "x 12"]
  - notes: "A 3×4 grid of little meatball circles fills in one by one. The lyric sits above it."
- **g3** — free_design
  - span_sec: [31.470, 33.640]
  - free_design: { dominant_system: "delivery stamp and hatch wipe", primitives: ["stamp-land", "paper-iris"], density_topology: "one hit + transition" }
  - anchors: [31.47, 33.10]
  - copy: ["Delivery under the sea"]
  - notes: "Red double-border stamp. The sub hatch is a dark navy circle that grows to full frame at 33.3."

## Frame 4 — f4

- src: compositions/frames/04-f4.html
- duration: 12.910s
- span_sec: [33.640, 46.550]
- pacing: beat_cut
- mood: [hype, playful, cinematic]
- feel: chorus 1 — full-band lift, line changes on every vocal phrase, the sub surfs the Atlantic
- visual: `launch` plate (the hero sandwich sub with the whale-maid at the wheel). Fast dolly-out,
  parallax bubbles and paper waves, speed lines on the kick. Lyrics in a left-hand column, each line
  a stamped paper strip. “Just count it on me” repeats as two red stamps. Ends with a porthole iris
  into the coral valley.

### Groups

- **g1** — free_design
  - span_sec: [33.640, 39.280]
  - free_design: { dominant_system: "chorus paper-strip stack over a launch plate", primitives: ["plate-dolly-out", "strip-slam", "speed-lines", "bubble-parallax"], density_topology: "one strip per phrase, stacked" }
  - anchors: [33.64, 35.04, 37.26]
  - copy: ["So I leap", "And swim against Atlantic stream", "To show you what I've achieved"]
  - notes: "Title-scale “So I leap” (150px) then two smaller strips. Strips are cream with a red edge."
- **g2** — free_design
  - span_sec: [39.280, 46.550]
  - free_design: { dominant_system: "deep-dive colour shift into a feast stamp", primitives: ["navy-wash", "stamp-land", "wave-foreground", "porthole-iris"], density_topology: "one wash, two stamps, one transition" }
  - anchors: [39.28, 40.71, 42.70, 44.11, 46.20]
  - copy: ["Going deep", "Tonight we'll make dinner a feast", "Just count it on me", "Just count it on me"]
  - notes: "At 39.28 a navy wash drops over the plate (not a blackout). Stamps land on 42.70 and 44.11."

## Frame 5 — f5

- src: compositions/frames/05-f5.html
- duration: 10.950s
- span_sec: [46.550, 57.500]
- pacing: phrase_flow
- mood: [dreamy, warm, elegant]
- feel: bridge — floating, legato, jellyfish and light; lyrics drift rather than cut
- visual: `coral` plate. Very slow lateral drift left-to-right, foreground jellyfish and bubbles
  parallaxing at different depths. Lyrics lower left in italic Fraunces, one line at a time with
  soft dissolve. “Wait for me” gets a lone lantern. Ends with a slow navy bubble dissolve.

### Groups

- **g1** — free_design
  - span_sec: [46.550, 52.150]
  - free_design: { dominant_system: "drifting italic lyric over a coral valley", primitives: ["golden-drift", "jellyfish-parallax", "soft-dissolve"], density_topology: "one line per 2 bars" }
  - anchors: [46.55, 48.55, 50.93]
  - copy: ["Soaring through the barnacle valleys", "And peachy coral reefs", "Wait for me"]
  - notes: "No hard stamps here. Use 1.2s dissolves, 8px rises. “Wait for me” is tomato red."
- **g2** — free_design
  - span_sec: [52.150, 57.500]
  - free_design: { dominant_system: "feast refrain as floating paper lanterns", primitives: ["lantern-rise", "soft-dissolve", "bubble-dissolve"], density_topology: "two lines, then a held breath" }
  - anchors: [52.15, 54.13, 55.43, 57.00]
  - copy: ["Tonight we'll make dinner a feast", "Just count it on me", "Just count it on me"]
  - notes: "Two “Just count it on me” lines stack, then a bubble column swallows the frame at 57.1."

## Frame 6 — f6

- src: compositions/frames/06-f6.html
- duration: 11.300s
- span_sec: [57.500, 68.800]
- pacing: beat_cut
- mood: [cinematic, tense, dreamy]
- feel: instrumental descent — sonar pings, a depth gauge, the sub dropping through black water
- visual: `abyss` plate. Very slow sink; concentric sonar rings pulse on each 4-bar phrase. Space Mono
  depth readout counts 200 → 1,860 m. A few bioluminescent jellyfish. No lyrics. At 68.8 a cheese-yellow
  flash cuts to the galley.

### Groups

- **g1** — free_design
  - span_sec: [57.500, 68.800]
  - free_design: { dominant_system: "sonar instrumentation over an abyss plate", primitives: ["depth-count", "sonar-ring", "plate-sink", "blip-ping", "colour-flash"], density_topology: "one ping per phrase, one continuous sink" }
  - anchors: [57.50, 59.64, 61.79, 63.93, 66.08, 68.60]
  - copy: ["DEPTH 0200 M", "DEPTH 0860 M", "DEPTH 1860 M", "NO SIGNAL"]
  - notes: "Machine voice only. Rings expand from the sub silhouette. The last 0.3s is a mustard flash."

## Frame 7 — f7

- src: compositions/frames/07-f7.html
- duration: 10.750s
- span_sec: [68.800, 79.550]
- pacing: beat_cut
- mood: [playful, warm, hype]
- feel: verse 2 — bright and tactile, cheese snow and a two-word punchline
- visual: `parmesan` plate. Push in through the cheese blizzard toward the maid's laughing face.
  “PARMESAN CRISPY SKIN” as a giant two-line display; “Tasty dilemma / Carbohydrates” as two fast
  red stamps. A sneeze of parmesan covers the frame at 79.4 and cuts to the shipping label.

### Groups

- **g1** — free_design
  - span_sec: [68.800, 74.200]
  - free_design: { dominant_system: "food-poster supers over a cheese-blizzard plate", primitives: ["plate-push-in", "cheese-snow", "display-word-slam"], density_topology: "two display words, one hold" }
  - anchors: [68.80, 71.50, 73.90]
  - copy: ["Parmesan crispy skin"]
  - notes: "PARMESAN in 170px Fraunces cream, CRISPY SKIN in 96px tomato red, stacked."
- **g2** — free_design
  - span_sec: [74.200, 79.550]
  - free_design: { dominant_system: "double stamp punchline", primitives: ["double-stamp", "cheese-burst", "paper-flash"], density_topology: "two hits then a sneeze wipe" }
  - anchors: [74.20, 76.00, 79.20]
  - copy: ["Tasty dilemma", "Carbohydrates"]
  - notes: "Two stamps land 0.35s apart, rotated opposite ways. Cheese particles fly out."

## Frame 8 — f8

- src: compositions/frames/08-f8.html
- duration: 13.550s
- span_sec: [79.550, 93.100]
- pacing: beat_cut
- mood: [playful, tense, hype]
- feel: pre-chorus 2 — a shipping montage that turns into an alarm; the last four bars are pure panic
- visual: First half `parmesan` plate reframed as a packing table with a shipping manifest; then at
  88.60 hard cut to `radar` plate (green sweep, shark blips). “BEEP BEEP BEEP” in Space Mono fills the
  lower third, alarm lamps spin, the radar turns red. At 93.1 the frame cuts on the alarm peak.

### Groups

- **g1** — free_design
  - span_sec: [79.550, 88.600]
  - free_design: { dominant_system: "packing-slip typography over a warm plate", primitives: ["manifest-slide", "checkbox-tick", "plate-pan", "label-stack"], density_topology: "checklist accumulates" }
  - anchors: [79.55, 82.75, 85.96, 88.60]
  - copy: ["Season up the gluten-free submarine", "Slather it in mascarpone cheese", "Meatball seats in my submarine", "Prime shipping under the sea"]
  - notes: "A shipping manifest on the right, each line ticked on its vocal. Keep the maid visible."
- **g2** — free_design
  - span_sec: [88.600, 93.100]
  - free_design: { dominant_system: "radar-room alert", primitives: ["radar-sweep", "blip-appear", "alarm-flash", "mono-type"], density_topology: "accelerating blips" }
  - anchors: [88.60, 90.99, 92.20, 93.10]
  - copy: ["Beep beep beep", "What's going on", "RADARS WENT OFF"]
  - notes: "Hard cut to the radar plate. Green → amber → red. Last word lands exactly at 93.1."

## Frame 9 — f9

- src: compositions/frames/09-f9.html
- duration: 10.600s
- span_sec: [93.100, 103.700]
- pacing: beat_cut
- mood: [aggressive, tense, playful]
- feel: shark attack — comic-book violence, screen shake, jaws, one line per hit
- visual: `shark` plate. Hard push-ins / pulls on each phrase, red flash on “biting”, giant jaw SVGs
  enter from the edges and snap shut. “They're biting on me” lands twice. Ends on a bite: a black
  paper wedge snaps across the frame, then cuts to the torn hull.

### Groups

- **g1** — free_design
  - span_sec: [93.100, 99.800]
  - free_design: { dominant_system: "attack callouts over a shark plate", primitives: ["screen-shake", "jaw-snap", "alert-flash", "type-slam"], density_topology: "one hit per lyric" }
  - anchors: [93.10, 94.48, 96.56, 97.83]
  - copy: ["Radars went off", "Showing the sharks on the screen", "Closing in", "The sharks opened up their mouths"]
  - notes: "Type 80–110px. Jaws are cream paper with red gums; they must not cover the maid's face."
- **g2** — free_design
  - span_sec: [99.800, 103.700]
  - free_design: { dominant_system: "bite refrain with torn-paper cuts", primitives: ["double-hit", "torn-wipe", "red-flash"], density_topology: "two hits + exit" }
  - anchors: [99.80, 101.35, 103.30]
  - copy: ["They're biting on me", "They're biting on me"]
  - notes: "Same line twice, second one bigger and torn. Exit on a black wedge at 103.5."

## Frame 10 — f10

- src: compositions/frames/10-f10.html
- duration: 22.300s
- span_sec: [103.700, 126.000]
- pacing: beat_cut
- mood: [aggressive, hype, cinematic]
- feel: the fight — damage, defiance, a rapid-fire litany, then a heroic power-up; the biggest arc in the song
- visual: `fight` plate for the damage and counterattack; `invincible` plate for the litany and the
  power-up. Mayo and cheddar fly off as labelled paper blobs. “PIERCE AND PIERCE…” becomes a wall of
  spears. “AN EYE FOR AN EYE / AN ARM FOR AN ARM” trades sides. “I'M INVINCIBLE / INDESTRUCTIBLE”
  finishes in a full-frame sunburst.

### Groups

- **g1** — free_design
  - span_sec: [103.700, 114.700]
  - free_design: { dominant_system: "damage callouts and condiment counterattack", primitives: ["blob-tear", "stamp-land", "speed-line-burst", "screen-shake"], density_topology: "two damage beats, then a build" }
  - anchors: [103.70, 105.90, 108.06, 109.75, 111.35, 112.75]
  - copy: ["Licked off my mayonnaise dressing", "Tored off my cheddar sliced cheese", "I may be weak", "But I'll fight your enemies", "So count it on me", "Just count it on me"]
  - notes: "MAYO and CHEDDAR labels fly off with the blobs. The last two lines are red stamps."
- **g2** — free_design
  - span_sec: [114.700, 119.830]
  - free_design: { dominant_system: "wall of spears for the pierce litany", primitives: ["spear-grid", "type-rush", "paper-shred"], density_topology: "accumulate to a wall" }
  - anchors: [114.70, 116.00, 117.40]
  - copy: ["Pierce and pierce and pierce and pierce it through", "All their tiny brains"]
  - notes: "Four PIERCE stamps, each rotated, overlapping into a spear wall. ALL THEIR TINY BRAINS below."
- **g3** — free_design
  - span_sec: [119.830, 126.000]
  - free_design: { dominant_system: "duel couplets into a sunburst power-up", primitives: ["split-couplet", "sunburst", "title-slam", "flash"], density_topology: "two couplets, one held apex" }
  - anchors: [119.83, 121.47, 122.86, 124.25, 125.80]
  - copy: ["An eye for eye", "And arm for arm", "I'm invincible", "Indestructible"]
  - notes: "Hard cut to `invincible` at 119.83. Sunburst rotates slowly behind the type; no full 3D spin."

## Frame 11 — f11

- src: compositions/frames/11-f11.html
- duration: 25.000s
- span_sec: [126.000, 151.000]
- pacing: beat_cut
- mood: [playful, hype, elegant]
- feel: instrumental menu parade — a rhythmic list, then the race begins; density is the joke
- visual: `menu` plate for the fleet, `race` plate for the launch of the race. A giant menu board
  cycles through HAM / BLT / SALAMI / VEGGIE & CHEESE / MARINE MARINE SUB / AVOCADO / ROAST BEEF /
  TERIYAKI, each slamming on the lyric. At 146.0 the menu folds into a checkered starting flag and
  the race plate explodes into speed lines.

### Groups

- **g1** — free_design
  - span_sec: [126.000, 137.180]
  - free_design: { dominant_system: "slow fleet reveal with a menu counter", primitives: ["plate-drift", "row-highlight", "counter-tick", "steam"], density_topology: "quiet accumulation" }
  - anchors: [126.00, 130.00, 134.00, 137.18]
  - copy: ["THE FLEET", "08 SUBMARINES", "ALL FRESHLY BAKED"]
  - notes: "No lyrics yet. Let the fleet image breathe; small mono counter in the corner."
- **g2** — free_design
  - span_sec: [137.180, 146.000]
  - free_design: { dominant_system: "rapid menu-board stamps over the fleet", primitives: ["menu-stamp", "row-flash", "colour-chip", "hard-cut"], density_topology: "one item per lyric, accelerating" }
  - anchors: [137.18, 138.00, 138.70, 139.40, 140.30, 141.37, 142.91, 144.30, 145.29]
  - copy: ["Ham", "BLT", "Salami", "Veggie & cheese", "So many submarines", "Marine marine sub", "Avocado", "Roast beef", "And teriyaki"]
  - notes: "Each item is a huge 120–170px word on a coloured paper chip. The list stacks into a menu grid."
- **g3** — free_design
  - span_sec: [146.000, 151.000]
  - free_design: { dominant_system: "starting-flag race launch", primitives: ["checker-wipe", "speed-line-burst", "engine-shake", "plate-push"], density_topology: "one burst, one hold" }
  - anchors: [146.00, 148.00, 150.80]
  - copy: ["GO"]
  - notes: "Menu folds into checkered flags; hard cut to race plate. GO stamp on 146.0."

## Frame 12 — f12

- src: compositions/frames/12-f12.html
- duration: 12.800s
- span_sec: [151.000, 163.800]
- pacing: beat_cut
- mood: [hype, playful, cinematic]
- feel: final chorus — the race and the plea; maximum forward motion, then a held look to camera
- visual: `race` plate. The sub overtakes the roast beef and BLT subs; checkered flags whip past;
  “SO I LEAP” is huge. At 157.85 she bursts through the finish banner; at 159.92 the camera holds on
  her face and the two “cheer for me” lines become a direct address. End on a freeze frame with the
  paper confetti hanging in the air.

### Groups

- **g1** — free_design
  - span_sec: [151.000, 157.850]
  - free_design: { dominant_system: "race-poster supers with speed lines", primitives: ["speed-line-burst", "plate-push", "type-slam", "checker-wipe"], density_topology: "one line per phrase, accelerating" }
  - anchors: [151.00, 152.16, 154.35, 156.55]
  - copy: ["So I leap", "And race against those submarines", "To show you what I've achieved", "Increased speed"]
  - notes: "Big italic display; keep the race readable. At 156.55 a speedometer spins."
- **g2** — free_design
  - span_sec: [157.850, 163.800]
  - free_design: { dominant_system: "finish-line burst into direct address", primitives: ["confetti-burst", "spotlight", "freeze", "stamp-land"], density_topology: "burst, then hold" }
  - anchors: [157.85, 159.92, 161.40, 163.60]
  - copy: ["Tonight we'll make dinner a feast", "So cheer for me please", "Just cheer for me please"]
  - notes: "Freeze at 163.4 on her face; the confetti is frozen mid-air."

## Frame 13 — f13

- src: compositions/frames/13-f13.html
- duration: 27.827s
- span_sec: [163.800, 191.627]
- pacing: phrase_flow
- mood: [elegant, dark, warm, dreamy]
- feel: the turn and the outro — the choice, the promise, the curtain; slow and tender
- visual: `choice` plate for the rejection, `portrait` for the promise, `tomorrow` for the farewell,
  `endcard` for the curtain. The giant leviathan chooses the roast beef submarine; she is left holding
  her meatball sub. A paper heart creases. Then she sails into the sunrise and waves. Curtains close;
  end card holds through the silence.

### Groups

- **g1** — free_design
  - span_sec: [163.800, 169.100]
  - free_design: { dominant_system: "scale-contrast banquet tableau", primitives: ["spotlight", "heart-crease", "plate-hold", "soft-dissolve"], density_topology: "two long lines, one heart" }
  - anchors: [163.80, 165.69, 167.50]
  - copy: ["Instead of looking at me", "You've decided on the roast beef submarine"]
  - notes: "Type lower left, 60–74px. The heart in the image creases on “decided”. No hard stamps."
- **g2** — free_design
  - span_sec: [169.100, 176.000]
  - free_design: { dominant_system: "intimate portrait promise", primitives: ["portrait-dissolve", "soft-rise", "bubble-drift"], density_topology: "one line per bar" }
  - anchors: [169.10, 171.30, 172.80, 175.50]
  - copy: ["Tomorrow I'll come back again", "So wait for me please", "Just wait for me please"]
  - notes: "Use `portrait` for the first line, then dissolve to `tomorrow` on 171.3. Warm, no red."
- **g3** — free_design
  - span_sec: [176.000, 186.000]
  - free_design: { dominant_system: "curtain call", primitives: ["curtain-close", "footlights", "paper-stars", "crossfade"], density_topology: "slow close, then hold" }
  - anchors: [176.00, 180.00, 184.00, 186.00]
  - copy: ["MEATBALL SUBMARINE", "Mili — Miracle Milk", "a paper-theatre film"]
  - notes: "Crossfade to `endcard` over 1.2s. Curtains close by 184.0; title holds."
- **g4** — free_design
  - span_sec: [186.000, 191.627]
  - free_design: { dominant_system: "silent end card", primitives: ["hold", "bubble-drift", "fade-to-black"], density_topology: "one held card" }
  - anchors: [186.00, 190.00, 191.40]
  - copy: ["for everyone who waits for tomorrow", "thank you for listening"]
  - notes: "Music has stopped. Hold the end card, fade to navy by 191.0, black frame at 191.5."
