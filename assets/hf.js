/* Paper Theatre helpers — deterministic, seek-safe GSAP primitives. */
(function () {
  const HF = {};

  HF.frame = function (id, build) {
    if (!window.gsap) throw new Error("GSAP is not loaded for frame " + id);
    const root = document.getElementById("root");
    const tl = window.gsap.timeline({ paused: true });
    build(tl, root);
    window.__timelines = window.__timelines || {};
    window.__timelines[id] = tl;
  };

  HF.all = function (sel, root) {
    return Array.from((root || document).querySelectorAll(sel));
  };

  /* Deterministic pseudo-random in [0,1); no Math.random. */
  HF.rand = function (i, salt) {
    const x = Math.sin((i + 1) * 127.1 + (salt || 0) * 311.7) * 43758.5453;
    return x - Math.floor(x);
  };

  /* Lyric / text entrance. */
  HF.reveal = function (tl, sel, at, o) {
    o = o || {};
    const els = HF.all(sel);
    if (!els.length) return;
    const from = {
      opacity: 0,
      y: o.y == null ? 36 : o.y,
      x: o.x == null ? 0 : o.x,
      scale: o.scale == null ? 1 : o.scale,
      rotation: o.rot == null ? 0 : o.rot,
      filter: "blur(6px)",
    };
    const to = {
      opacity: 1,
      y: 0,
      x: 0,
      scale: 1,
      rotation: 0,
      filter: "blur(0px)",
      duration: o.dur == null ? 0.7 : o.dur,
      ease: o.ease || "power3.out",
      stagger: o.stagger == null ? 0.08 : o.stagger,
    };
    tl.fromTo(els, from, to, at);
  };

  /* Rubber-stamp slam. */
  HF.stamp = function (tl, sel, at, o) {
    o = o || {};
    const els = HF.all(sel);
    if (!els.length) return;
    const rot = o.rot == null ? -3 : o.rot;
    tl.fromTo(
      els,
      { opacity: 0, scale: 2.2, rotation: rot + 9, y: o.y == null ? -10 : o.y },
      {
        opacity: 1,
        scale: 1,
        rotation: rot,
        y: 0,
        duration: o.dur == null ? 0.42 : o.dur,
        ease: o.ease || "back.out(2.2)",
        stagger: o.stagger == null ? 0.06 : o.stagger,
      },
      at,
    );
  };

  /* Horizontal paper strip. */
  HF.strip = function (tl, sel, at, o) {
    o = o || {};
    const els = HF.all(sel);
    if (!els.length) return;
    tl.fromTo(
      els,
      { opacity: 0, x: o.x == null ? -90 : o.x, rotation: o.rot == null ? -1.2 : o.rot },
      {
        opacity: 1,
        x: 0,
        rotation: 0,
        duration: o.dur == null ? 0.5 : o.dur,
        ease: "back.out(1.5)",
        stagger: o.stagger == null ? 0.05 : o.stagger,
      },
      at,
    );
  };

  HF.out = function (tl, sel, at, o) {
    o = o || {};
    const els = HF.all(sel);
    if (!els.length) return;
    tl.to(
      els,
      {
        opacity: 0,
        y: o.y == null ? -24 : o.y,
        x: o.x == null ? 0 : o.x,
        duration: o.dur == null ? 0.35 : o.dur,
        ease: o.ease || "power2.in",
        stagger: o.stagger == null ? 0 : o.stagger,
      },
      at,
    );
  };

  /* Slow plate move. x/y are pixel offsets, scale is a multiplier. */
  HF.plate = function (tl, sel, o) {
    o = o || {};
    const el = typeof sel === "string" ? document.querySelector(sel) : sel;
    if (!el) return;
    tl.fromTo(
      el,
      { scale: o.s0 == null ? 1.04 : o.s0, x: o.x0 == null ? 0 : o.x0, y: o.y0 == null ? 0 : o.y0 },
      {
        scale: o.s1 == null ? 1.1 : o.s1,
        x: o.x1 == null ? 0 : o.x1,
        y: o.y1 == null ? 0 : o.y1,
        duration: o.dur == null ? 12 : o.dur,
        ease: o.ease || "none",
      },
      o.at || 0,
    );
  };

  /* A quick flash on a target layer (use a full-bleed div). */
  HF.flash = function (tl, sel, at, o) {
    o = o || {};
    const el = document.querySelector(sel);
    if (!el) return;
    tl.fromTo(el, { opacity: 0 }, { opacity: o.peak == null ? 0.85 : o.peak, duration: 0.06, ease: "none" }, at);
    tl.to(el, { opacity: 0, duration: o.dur == null ? 0.28 : o.dur, ease: "power1.in" }, at + 0.06);
  };

  /* Short deterministic camera shake. */
  HF.shake = function (tl, sel, at, o) {
    o = o || {};
    const el = document.querySelector(sel);
    if (!el) return;
    const a = o.amp == null ? 14 : o.amp;
    const step = o.step == null ? 0.055 : o.step;
    const n = o.beats == null ? 4 : o.beats;
    for (let i = 0; i < n; i++) {
      const dx = (i % 2 === 0 ? 1 : -1) * a * (1 - i / (n + 1));
      const dy = (i % 3 === 0 ? -1 : 1) * a * 0.55 * (1 - i / (n + 1));
      tl.to(el, { x: dx, y: dy, duration: step, ease: "none" }, at + i * step);
    }
    tl.to(el, { x: 0, y: 0, duration: step, ease: "none" }, at + n * step);
  };

  /* Paper bubbles. Creates deterministic bubbles and animates them once. */
  HF.bubbles = function (tl, root, o) {
    o = o || {};
    const host = document.querySelector(o.host || ".bubble-field") || root;
    const count = o.count == null ? 18 : o.count;
    const dur = o.dur == null ? 10 : o.dur;
    const color = o.dark ? " dark" : "";
    const sizeMin = o.min == null ? 8 : o.min;
    const sizeMax = o.max == null ? 44 : o.max;
    const frag = document.createDocumentFragment();
    const made = [];
    for (let i = 0; i < count; i++) {
      const b = document.createElement("div");
      b.className = "bubble" + color;
      const s = sizeMin + HF.rand(i, 3) * (sizeMax - sizeMin);
      b.style.width = s + "px";
      b.style.height = s + "px";
      b.style.left = HF.rand(i, 5) * 96 + "%";
      b.style.top = "0px";
      b.style.opacity = 0;
      b.style.zIndex = o.z == null ? 4 : o.z;
      frag.appendChild(b);
      made.push(b);
    }
    host.appendChild(frag);
    made.forEach((b, i) => {
      const delay = HF.rand(i, 9) * (o.spread == null ? dur * 0.75 : o.spread);
      const travel = 700 + HF.rand(i, 11) * 520;
      const sway = (HF.rand(i, 12) - 0.5) * 120;
      const life = dur * (0.55 + HF.rand(i, 13) * 0.45);
      tl.fromTo(
        b,
        { y: 0, x: 0, opacity: 0, scale: 0.6 },
        {
          y: -travel,
          x: sway,
          opacity: o.opacity == null ? 0.85 : o.opacity,
          scale: 1,
          duration: life,
          ease: "none",
          onComplete: () => {},
        },
        delay,
      );
      tl.to(b, { opacity: 0, duration: 0.45, ease: "power1.in" }, delay + life - 0.45);
    });
  };

  /* Confetti pieces falling once. */
  HF.confetti = function (tl, root, o) {
    o = o || {};
    const host = document.querySelector(o.host || ".confetti-field") || root;
    const count = o.count == null ? 24 : o.count;
    const colors = o.colors || ["#D4462F", "#E7A93D", "#83B7A6", "#F2E7D1", "#3C63A6"];
    const frag = document.createDocumentFragment();
    const made = [];
    for (let i = 0; i < count; i++) {
      const c = document.createElement("div");
      c.className = "confetti";
      c.style.left = HF.rand(i, 21) * 100 + "%";
      c.style.top = "-40px";
      c.style.background = colors[i % colors.length];
      c.style.width = 10 + HF.rand(i, 22) * 16 + "px";
      c.style.height = 16 + HF.rand(i, 23) * 30 + "px";
      c.style.opacity = 0;
      frag.appendChild(c);
      made.push(c);
    }
    host.appendChild(frag);
    made.forEach((c, i) => {
      const delay = (o.at == null ? 0 : o.at) + HF.rand(i, 24) * (o.spread == null ? 1.2 : o.spread);
      tl.fromTo(
        c,
        { y: 0, x: 0, rotation: 0, opacity: 1 },
        {
          y: 700 + HF.rand(i, 25) * 500,
          x: (HF.rand(i, 26) - 0.5) * 380,
          rotation: 540 + HF.rand(i, 27) * 540,
          duration: 2.4 + HF.rand(i, 28) * 1.8,
          ease: "none",
        },
        delay,
      );
      tl.to(c, { opacity: 0, duration: 0.5 }, delay + 2.4);
    });
  };

  /* Bubble column / paper wipe that grows to cover the frame. */
  HF.coverIn = function (tl, sel, at, dur) {
    const el = document.querySelector(sel);
    if (!el) return;
    tl.fromTo(el, { scale: 0, opacity: 1 }, { scale: 1, duration: dur || 0.5, ease: "power2.in" }, at);
  };
  HF.coverOut = function (tl, sel, at, dur) {
    const el = document.querySelector(sel);
    if (!el) return;
    tl.fromTo(el, { scale: 1, opacity: 1 }, { scale: 0, duration: dur || 0.5, ease: "power2.out" }, at);
  };

  window.HF = HF;
})();
