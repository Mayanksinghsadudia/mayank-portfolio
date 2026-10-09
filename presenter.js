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
  video.autoplay = true;
  video.loop = Boolean(config.loop);
  // Default to unmuted so it plays normally with audio without touch
  video.muted = false;
  video.defaultMuted = false;
  video.controls = false;
  video.setAttribute("aria-label", "Mayank introducing his portfolio");
  video.className = config.sceneVideo ? "presenter-scene-video" : "presenter-video";
  frame.prepend(video);

  let visible = true;
  let starting = false;
  const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

  async function start() {
    if (starting || document.hidden || reducedMotion.matches) return;
    starting = true;
    try {
      // First attempt: play unmuted directly without user touch
      video.muted = false;
      await video.play();
    } catch (unmutedErr) {
      // If browser security policy blocks unmuted autoplay, immediately run muted so video begins
      video.muted = true;
      try {
        await video.play();
      } catch (err) {
        console.warn("Autoplay playback error:", err);
      }
    } finally {
      starting = false;
    }
  }

  // Immediately attempt playback on page load
  start();

  video.addEventListener("playing", () => {
    frame.classList.add("presenter-active");
    hero?.classList.add("scene-video-active");
  });
  video.addEventListener("error", () => {
    frame.classList.remove("presenter-active");
    hero?.classList.remove("scene-video-active");
  });

  // Seamless auto-unmute on any natural user interaction (scroll, move, touch, key) - no buttons needed!
  function autoUnmute() {
    if (video.muted) {
      video.muted = false;
      video.play().catch(() => {});
    }
  }
  ["pointerdown", "touchstart", "mousemove", "scroll", "wheel", "keydown"].forEach(evt => {
    window.addEventListener(evt, autoUnmute, { passive: true, once: evt === "pointerdown" || evt === "touchstart" });
  });

  const observer = new IntersectionObserver(entries => {
    visible = entries.some(entry => entry.isIntersecting);
    if (!visible) video.pause();
    else if (config.autoplay) start();
  }, { threshold: .15 });
  observer.observe(frame);

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) video.pause();
    else if (visible && config.autoplay) start();
  });

  reducedMotion.addEventListener("change", event => {
    if (event.matches) video.pause();
    else if (visible && config.autoplay) start();
  });
})();
