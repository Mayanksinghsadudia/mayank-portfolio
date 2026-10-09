(() => {
  "use strict";
  const config = window.MAYANK_PRESENTER;
  const frame = document.getElementById("home-presenter");
  if (!config?.videoSrc || !frame) return;
  const hero = frame.closest("#hero");
  const video = document.createElement("video");
  video.src = config.videoSrc;
  if (config.posterSrc) video.poster = config.posterSrc;
  video.preload = "auto";
  video.playsInline = true;
  video.autoplay = Boolean(config.autoplay);
  video.loop = Boolean(config.loop);
  video.muted = true;
  video.defaultMuted = true;
  video.controls = false;
  video.setAttribute("aria-label", "Mayank introducing his portfolio");
  video.className = config.sceneVideo ? "presenter-scene-video" : "presenter-video";
  frame.prepend(video);
  let visible = false;
  let starting = false;
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");
  async function start() {
    if (starting || document.hidden || !visible || reducedMotion.matches) return;
    starting = true;
    try { await video.play(); }
    catch { video.muted = true; try { await video.play(); } catch {} }
    finally { starting = false; }
  }
  video.addEventListener("playing", () => {
    frame.classList.add("presenter-active");
    hero?.classList.add("scene-video-active");
  });
  video.addEventListener("error", () => {
    video.pause();
    frame.classList.remove("presenter-active");
    hero?.classList.remove("scene-video-active");
  });
  const observer = new IntersectionObserver(entries => {
    visible = entries.some(entry => entry.isIntersecting);
    if (!visible) video.pause();
    else if (config.autoplay) start();
  }, { threshold: .25 });
  observer.observe(frame);
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) video.pause();
    else if (visible && config.autoplay) start();
  });
  // Browsers allow sound after a real page interaction; no separate media controls.
  function enableSound(event) {
    if (!event.isTrusted || !visible || reducedMotion.matches) return;
    if (event.type === "keydown" && !["Enter", " "].includes(event.key)) return;
    video.muted = false;
    video.defaultMuted = false;
    start();
    document.removeEventListener("pointerdown", enableSound, true);
    document.removeEventListener("keydown", enableSound, true);
  }
  document.addEventListener("pointerdown", enableSound, true);
  document.addEventListener("keydown", enableSound, true);
  reducedMotion.addEventListener("change", event => {
    if (event.matches) video.pause();
    else if (visible && config.autoplay) start();
  });
})();
