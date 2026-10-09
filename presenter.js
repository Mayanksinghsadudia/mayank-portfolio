(() => {
  "use strict";
  const config = window.MAYANK_PRESENTER;
  const frame = document.getElementById("home-presenter");
  if (!config?.videoSrc || !frame) return;

  const hero = frame.closest("#hero");
  const sceneVideo = Boolean(config.sceneVideo && hero);
  const controls = frame.querySelector(".presenter-controls");
  const play = document.getElementById("presenter-play");
  const sound = document.getElementById("presenter-sound");
  const subtitleBox = document.getElementById("presenter-subtitles");
  const ccBtn = document.getElementById("presenter-cc");

  const video = document.createElement("video");
  video.crossOrigin = "anonymous";
  video.src = config.videoSrc;
  if (config.posterSrc) video.poster = config.posterSrc;
  video.preload = "metadata";
  video.playsInline = true;
  video.muted = true;
  video.setAttribute("aria-label", "Mayank introducing his portfolio");
  video.className = sceneVideo ? "presenter-scene-video" : "presenter-video";
  frame.prepend(video);

  let started = false;
  let userPaused = false;
  let ccEnabled = true;
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");

  // Timed Speech Segments for live closed captions
  const speechSegments = [
    { start: 0.0, end: 1.2, text: "👋 [Mayank walks in]" },
    { start: 1.2, end: 6.0, text: "Hi, I'm Mayank Singh Sadudia, a data analyst and graphic designer based in Indore." },
    { start: 6.0, end: 7.6, text: "I use Python, SQL, Excel, and Power BI to turn data into clear insights." },
    { start: 7.6, end: 14.5, text: "I also create brand identities, packaging, and engaging visuals. My portfolio brings analytical thinking and creative design together." },
    { start: 14.5, end: 21.0, text: "Explore my projects, visit my GitHub, and get in touch. I'd love to collaborate." },
    { start: 21.0, end: 25.0, text: "✨ [Looking forward to collaborating with you!]" }
  ];

  function updateSubtitles() {
    if (!subtitleBox) return;
    if (!ccEnabled || video.paused || video.ended) {
      if (!ccEnabled) subtitleBox.style.display = "none";
      return;
    }
    const t = video.currentTime;
    const match = speechSegments.find(s => t >= s.start && t < s.end);
    if (match) {
      subtitleBox.textContent = match.text;
      subtitleBox.style.display = "block";
    } else {
      subtitleBox.style.display = "none";
    }
  }

  function updatePlay() {
    if (!play) return;
    const text = video.ended ? "Replay introduction" : video.paused ? (started ? "Resume introduction" : "Play introduction") : "Pause introduction";
    play.textContent = text;
    play.setAttribute("aria-label", text);
    play.classList.toggle("is-playing", !video.paused && !video.ended);
  }

  function updateSound() {
    if (!sound) return;
    sound.textContent = video.muted ? "Sound on" : "Mute sound";
    sound.setAttribute("aria-label", sound.textContent);
    sound.classList.toggle("sound-active", !video.muted);
  }

  function unavailable() {
    video.pause();
    frame.classList.remove("presenter-active");
    hero?.classList.remove("scene-video-active");
    if (controls) controls.hidden = true;
  }

  async function start() {
    if (video.ended) video.currentTime = 0;
    try {
      await video.play();
    } catch {
      updatePlay();
    }
  }

  video.addEventListener("loadeddata", () => {
    if (controls) controls.hidden = false;
  });

  video.addEventListener("playing", () => {
    started = true;
    frame.classList.add("presenter-active");
    if (sceneVideo) hero.classList.add("scene-video-active");
    updatePlay();
    updateSound();
  });

  video.addEventListener("pause", () => {
    updatePlay();
    updateSubtitles();
  });

  video.addEventListener("ended", () => {
    updatePlay();
    if (subtitleBox) subtitleBox.style.display = "none";
  });

  video.addEventListener("timeupdate", updateSubtitles);
  video.addEventListener("error", unavailable);

  if (play) {
    play.addEventListener("click", () => {
      if (!video.paused && !video.ended) {
        userPaused = true;
        video.pause();
      } else {
        userPaused = false;
        start();
      }
    });
  }

  if (sound) {
    sound.addEventListener("click", () => {
      video.muted = !video.muted;
      updateSound();
      if (!video.muted) {
        if (video.paused) {
          userPaused = false;
          start();
        }
      }
    });
  }

  if (ccBtn) {
    ccBtn.addEventListener("click", () => {
      ccEnabled = !ccEnabled;
      ccBtn.classList.toggle("active", ccEnabled);
      if (!ccEnabled && subtitleBox) subtitleBox.style.display = "none";
      else updateSubtitles();
    });
  }

  // Switch video edition seamlessly
  function switchEdition(editionKey, btnElement) {
    if (!config.editions || !config.editions[editionKey]) return;
    const edition = config.editions[editionKey];
    const wasPlaying = !video.paused && !video.ended;
    const currentTime = video.currentTime;

    video.src = edition.videoSrc;
    video.load();

    video.addEventListener("loadedmetadata", function onMeta() {
      video.removeEventListener("loadedmetadata", onMeta);
      if (currentTime < video.duration) {
        video.currentTime = currentTime;
      }
      if (wasPlaying || !userPaused) {
        start();
      }
    });

    document.querySelectorAll(".presenter-edition-pill").forEach(p => p.classList.remove("active"));
    if (btnElement) btnElement.classList.add("active");

    const descElem = document.getElementById("presenter-edition-desc");
    if (descElem) descElem.textContent = edition.desc;
  }

  window.switchPresenterEdition = switchEdition;

  window.togglePresenterSound = () => {
    if (sound) sound.click();
    else {
      video.muted = !video.muted;
      updateSound();
    }
  };

  const observer = new IntersectionObserver(entries => {
    const visible = entries.some(entry => entry.isIntersecting);
    if (!visible) video.pause();
    else if (config.autoplay && !reduceMotion.matches && !userPaused && !video.ended && !document.hidden) start();
  }, { threshold: .35 });

  observer.observe(frame);

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) video.pause();
    else if (!userPaused && !video.ended && config.autoplay && !reduceMotion.matches) start();
  });

  reduceMotion.addEventListener("change", event => {
    if (event.matches) video.pause();
  });
})();
