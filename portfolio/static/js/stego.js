/*
 * Pixel grid with a hidden message.
 * Every cell gets a random "noise" shade. Cells that belong to the message
 * differ only slightly (like a flipped least-significant bit) until the
 * pointer lens or the reveal toggle brings them out.
 */
(function () {
  const figure = document.querySelector(".stego");
  if (!figure) return;

  const canvas = figure.querySelector(".stego-canvas");
  const toggle = figure.querySelector(".stego-toggle");
  const live = figure.querySelector("[data-stego-live]");
  const ctx = canvas.getContext("2d");
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  let cols, rows, cell, mask, noise, reveal;
  let pointer = null;
  let revealedAll = false;
  let sweep = reduceMotion ? null : -0.2; // one intro sweep, left to right

  function css(name) {
    return getComputedStyle(document.documentElement).getPropertyValue(name).trim();
  }

  function buildMask() {
    const words = figure.dataset.message.split(" ");
    const narrow = canvas.clientWidth < 640;
    // Narrow screens: one word per line. Wide: two balanced lines.
    const half = Math.ceil(words.length / 2);
    const lines = narrow
      ? words
      : [words.slice(0, half).join(" "), words.slice(half).join(" ")].filter(Boolean);
    const off = document.createElement("canvas");
    off.width = cols; off.height = rows;
    const o = off.getContext("2d");
    o.fillStyle = "#000";
    o.textAlign = "center";
    o.textBaseline = "middle";
    const lineH = rows / (lines.length + 0.35);
    let size = lineH * 1.05;
    o.font = `800 ${size}px "Bricolage Grotesque", sans-serif`;
    const widest = Math.max(...lines.map((l) => o.measureText(l).width));
    if (widest > cols * 0.9) size *= (cols * 0.9) / widest;
    o.font = `800 ${size}px "Bricolage Grotesque", sans-serif`;
    lines.forEach((line, i) => {
      o.fillText(line, cols / 2, rows / 2 + (i - (lines.length - 1) / 2) * lineH);
    });
    const data = o.getImageData(0, 0, cols, rows).data;
    mask = new Uint8Array(cols * rows);
    for (let i = 0; i < mask.length; i++) mask[i] = data[i * 4 + 3] > 90 ? 1 : 0;
  }

  function setup() {
    const ratio = window.devicePixelRatio || 1;
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    canvas.width = Math.round(w * ratio);
    canvas.height = Math.round(h * ratio);
    ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
    cell = w < 640 ? 9 : 12;
    cols = Math.floor(w / cell);
    rows = Math.floor(h / cell);
    noise = new Float32Array(cols * rows).map(() => Math.random());
    reveal = new Float32Array(cols * rows);
    buildMask();
  }

  function draw() {
    const w = canvas.clientWidth;
    const h = canvas.clientHeight;
    const ox = (w - cols * cell) / 2;
    const oy = (h - rows * cell) / 2;
    const rule = css("--rule");
    const muted = css("--muted");
    const signal = css("--signal");
    const cobalt = css("--cobalt");
    const lens = Math.max(70, w * 0.09);

    ctx.clearRect(0, 0, w, h);
    let busy = false;

    for (let y = 0; y < rows; y++) {
      for (let x = 0; x < cols; x++) {
        const i = y * cols + x;
        const cx = ox + x * cell + cell / 2;
        const cy = oy + y * cell + cell / 2;

        let target = revealedAll ? 1 : 0;
        if (pointer) {
          const d = Math.hypot(cx - pointer.x, cy - pointer.y);
          target = Math.max(target, 1 - d / lens);
        }
        if (sweep !== null) {
          const band = 1 - Math.abs(x / cols - sweep) * 7;
          target = Math.max(target, band);
        }
        target = Math.max(0, Math.min(1, target));
        reveal[i] += (target - reveal[i]) * 0.18;
        if (Math.abs(target - reveal[i]) > 0.01) busy = true;

        const r = reveal[i];
        const n = noise[i];
        const size = cell - 3;
        if (mask[i]) {
          const base = 0.25 + n * 0.45;
          ctx.globalAlpha = base + (1 - base) * r;
          ctx.fillStyle = r > 0.3 ? (n > 0.78 ? signal : cobalt) : (n > 0.5 ? muted : rule);
        } else {
          ctx.globalAlpha = (0.25 + n * 0.45) * (1 - r * 0.7);
          ctx.fillStyle = n > 0.5 ? muted : rule;
        }
        ctx.fillRect(cx - size / 2, cy - size / 2, size, size);
      }
    }
    ctx.globalAlpha = 1;

    if (sweep !== null) {
      sweep += 0.012;
      if (sweep > 1.3) sweep = null;
      busy = true;
    }
    if (busy) requestAnimationFrame(draw);
    else running = false;
  }

  let running = false;
  function kick() {
    if (!running) { running = true; requestAnimationFrame(draw); }
  }

  canvas.addEventListener("pointermove", (e) => {
    const rect = canvas.getBoundingClientRect();
    pointer = { x: e.clientX - rect.left, y: e.clientY - rect.top };
    kick();
  });
  canvas.addEventListener("pointerleave", () => { pointer = null; kick(); });

  toggle.addEventListener("click", () => {
    revealedAll = !revealedAll;
    toggle.setAttribute("aria-pressed", String(revealedAll));
    toggle.textContent = revealedAll ? "Hide message" : "Reveal message";
    live.textContent = revealedAll ? `Hidden message: ${figure.dataset.message}` : "";
    kick();
  });

  let resizeTimer;
  window.addEventListener("resize", () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { setup(); kick(); }, 150);
  });
  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", kick);

  const start = () => { setup(); kick(); };
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(start);
  else start();
})();
