#!/usr/bin/env python3
"""Add five extra cuts to the 13-frame MV.

We split at existing scene boundaries, keeping the sum of durations identical:

  08 shipping 9.55 + 08b radar 4.00       = 13.55
  10 damage 11.00 + 10b pierce 5.13 +
     10c invincible 6.17                   = 22.30
  11 menu 20.00 + 11b race 5.00            = 25.00
  13 choice/tomorrow 12.20 + 13b end 15.627 = 27.827

Part A is a copy with a shorter duration (the later tweens simply never play).
Part B/C is a copy with the same markup and a compact script for only the later
scene; the earlier scenes and covers are hidden with gsap.set.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent.parent
frames = root / "compositions" / "frames"

A_FRAMES = [
    ("08-f8", "08a-f8a", 9.55),
    ("10-f10", "10a-f10a", 11.00),
    ("11-f11", "11a-f11a", 20.00),
    ("13-f13", "13a-f13a", 12.20),
]

SCRIPT = {
    "08b-f8b": """HF.frame("08b-f8b", function (tl, root) {
          gsap.set("#f8-cover, #f8-ship", { display: "none" });
          gsap.set("#f8-radar", { opacity: 1 });
          HF.plate(tl, "#f8-radar-plate img", { s0: 1.05, s1: 1.14, x0: 24, x1: -30, y0: 0, y1: 14, dur: 4.0, at: 0 });
          HF.reveal(tl, "#f8-sharkcount", 0.0, { y: 18, dur: .5 });
          HF.stamp(tl, "#f8-warnring", 0.10, { rot: 0, dur: .35, stagger: .12 });
          tl.to("#f8-alarm", { opacity: 1, duration: .3 }, .20);
          tl.to("#f8-alarm", { rotation: 90, duration: 3.4, ease: "none" }, .20);
          tl.to("#f8-alertover", { opacity: .55, duration: .25, yoyo: true, repeat: 3, ease: "sine.inOut" }, .30);
          tl.fromTo("#f8-beep", { opacity: 0, x: -30 }, { opacity: 1, x: 0, duration: .16, ease: "power1.out", repeat: 4, yoyo: true }, 1.89);
          tl.to("#f8-beep", { opacity: 1, duration: .1 }, 2.75);
          HF.stamp(tl, "#f8-what .stamp", 3.10, { rot: -2.5, dur: .35 });
          tl.fromTo("#f8-redflash", { opacity: 0 }, { opacity: .9, duration: .2, ease: "power2.in" }, 3.79);
        });""",
    "10b-f10b": """HF.frame("10b-f10b", function (tl, root) {
          gsap.set("#f10-cover, #f10-damage, #f10-inv", { display: "none" });
          gsap.set("#f10-pierce", { opacity: 1 });
          HF.plate(tl, "#f10-pierce-plate img", { s0: 1.15, s1: 1.26, x0: -60, x1: 30, y0: 0, y1: -20, dur: 5.13, at: 0 });
          HF.all(".f10-spear").forEach(function (el, i) {
            tl.fromTo(el, { scaleX: 0, opacity: 0 }, { scaleX: 1, opacity: .86, duration: .35, ease: "power3.in" }, 0.0 + i * .24);
          });
          HF.stamp(tl, "#f10-pw1", 0.00, { rot: -4, dur: .3 });
          HF.stamp(tl, "#f10-pw2", 1.15, { rot: 2, dur: .3 });
          HF.stamp(tl, "#f10-pw3", 2.30, { rot: -2, dur: .3 });
          HF.stamp(tl, "#f10-pw4", 3.45, { rot: 4, dur: .3 });
          HF.stamp(tl, "#f10-brains", 2.70, { rot: -1.5, dur: .35 });
          [0.0, 1.15, 2.30, 3.45].forEach(function (t) { HF.shake(tl, "#f10-pierce", t, { amp: 14, beats: 3 }); });
          tl.fromTo("#f10-flash", { opacity: 0 }, { opacity: 1, duration: .2, ease: "power2.in" }, 5.0);
        });""",
    "10c-f10c": """HF.frame("10c-f10c", function (tl, root) {
          gsap.set("#f10-cover, #f10-damage, #f10-pierce", { display: "none" });
          gsap.set("#f10-inv", { opacity: 1 });
          HF.plate(tl, "#f10-inv-plate img", { s0: 1.02, s1: 1.09, x0: 10, x1: -14, y0: 0, y1: 10, dur: 6.17, at: 0 });
          tl.fromTo("#f10-rays", { rotation: 0, opacity: .12 }, { rotation: 22, opacity: .26, duration: 6.17, ease: "none" }, 0);
          HF.reveal(tl, "#f10-c1", 0.00, { x: -20, y: 0, dur: .4 });
          HF.reveal(tl, "#f10-c2", 1.64, { x: -20, y: 0, dur: .4 });
          HF.stamp(tl, "#f10-invtitle", 3.03, { rot: -1.2, dur: .45 });
          HF.stamp(tl, "#f10-indest", 4.42, { rot: 1.2, dur: .45 });
          tl.fromTo("#f10-flash", { opacity: 0 }, { opacity: 1, duration: .2, ease: "power2.in" }, 5.95);
        });""",
    "11b-f11b": """HF.frame("11b-f11b", function (tl, root) {
          gsap.set("#f11-cover, #f11-menu", { display: "none" });
          gsap.set("#f11-race", { opacity: 1 });
          HF.plate(tl, "#f11-race-plate img", { s0: 1.12, s1: 1.02, x0: -40, x1: 30, y0: 0, y1: 8, dur: 5.0, at: 0 });
          HF.stamp(tl, "#f11-go .display", 0.00, { rot: -3, dur: .34 });
          HF.reveal(tl, "#f11-racehint", 1.20, { y: 12, dur: .4 });
          HF.shake(tl, "#f11-race", 0.00, { amp: 16, beats: 4 });
          tl.fromTo("#f11-checker", { opacity: 0 }, { opacity: 1, duration: .1 }, 0);
          tl.fromTo("#f11-flash", { opacity: 0 }, { opacity: 1, duration: .2, ease: "power2.in" }, 4.72);
        });""",
    "13b-f13b": """HF.frame("13b-f13b", function (tl, root) {
          gsap.set("#f13-cover, #f13-choice, #f13-tomorrow", { display: "none" });
          gsap.set("#f13-end", { opacity: 1 });
          HF.plate(tl, "#f13-end-plate img", { s0: 1.02, s1: 1.06, x0: 0, x1: -8, y0: 0, y1: 4, dur: 15.627, at: 0 });
          tl.fromTo("#f13-plaque", { opacity: 0, xPercent: -50, yPercent: -46, scale: .97, rotation: .7 }, { opacity: 1, xPercent: -50, yPercent: -50, scale: 1, rotation: .7, duration: .9, ease: "power3.out" }, 1.0);
          tl.fromTo("#f13-dim", { opacity: 0 }, { opacity: .32, duration: 1.0 }, 1.2);
          tl.fromTo("#f13-black", { opacity: 0 }, { opacity: 1, duration: 1.8, ease: "sine.in" }, 13.4);
        });""",
}

B_FRAMES = [
    ("08-f8", "08b-f8b", 4.00),
    ("10-f10", "10b-f10b", 5.13),
    ("10-f10", "10c-f10c", 6.17),
    ("11-f11", "11b-f11b", 5.00),
    ("13-f13", "13b-f13b", 15.627),
]


def replace_script(text: str, new_script: str) -> str:
    pattern = re.compile(
        r'(<script src="\.\./\.\./assets/hf\.js"></script>\s*<script>)[\s\S]*?(</script>)'
    )
    return pattern.sub(lambda m: m.group(1) + "\n        " + new_script + "\n      " + m.group(2), text, count=1)


for old_stem, new_stem, duration in A_FRAMES:
    text = (frames / f"{old_stem}.html").read_text(encoding="utf-8")
    text = text.replace(old_stem, new_stem)
    text = re.sub(r'data-duration="[^"]*"', f'data-duration="{duration:g}"', text, count=1)
    (frames / f"{new_stem}.html").write_text(text, encoding="utf-8")
    print("A", new_stem, duration)

for old_stem, new_stem, duration in B_FRAMES:
    text = (frames / f"{old_stem}.html").read_text(encoding="utf-8")
    text = text.replace(old_stem, new_stem)
    text = re.sub(r'data-duration="[^"]*"', f'data-duration="{duration:g}"', text, count=1)
    text = replace_script(text, SCRIPT[new_stem])
    (frames / f"{new_stem}.html").write_text(text, encoding="utf-8")
    print("B", new_stem, duration)

for old_stem in ("08-f8", "10-f10", "11-f11", "13-f13"):
    (frames / f"{old_stem}.html").unlink()
    print("removed", old_stem)
