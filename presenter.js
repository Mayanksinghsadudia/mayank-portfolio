(() => {
  "use strict";
  const config = window.MAYANK_PRESENTER;
  if (!config || !config.videoSrc) return;
  const frame = document.querySelector("#hero .avatar-frame");
  if (!frame) return;
  frame.classList.add("portfolio-presenter");

  const video = document.createElement("video");
  video.src = config.videoSrc;
  video.preload = "metadata";
  video.muted = Boolean(config.autoplay);
  video.playsInline = true;
  video.setAttribute("playsinline", "");
  video.setAttribute("aria-hidden", "true");
  video.className = "presenter-video";
  video.style.display = "none";

  const controls = document.createElement("div");
  controls.className = "presenter-controls";
  controls.setAttribute("role", "group");
  controls.setAttribute("aria-label", "Portfolio introduction controls");

  const makeButton = (label, className) => {
    const button = document.createElement("button");
    button.type = "button";
    button.textContent = label;
    if (className) button.className = className;
    controls.append(button);
    return button;
  };

  const playButton = makeButton("▶ Meet Mayank", "presenter-play");
  const muteButton = makeButton(video.muted ? "Sound on" : "Mute sound");
  const stopButton = makeButton("Stop");
  const textButton = makeButton("Text");
  textButton.setAttribute("aria-expanded", "false");

  const transcript = document.createElement("div");
  transcript.className = "presenter-transcript";
  transcript.id = "presenter-transcript";
  transcript.hidden = true;
  const paragraph = document.createElement("p");
  paragraph.textContent = config.intro;
  transcript.append(paragraph);
  textButton.setAttribute("aria-controls", transcript.id);

  const status = document.createElement("div");
  status.className = "presenter-status";
  status.setAttribute("role", "status");
  status.hidden = true;

  frame.append(video, controls, transcript, status);

  let started = false;
  const showStatus = text => {
    status.textContent = text;
    status.hidden = !text;
  };

  const restorePoster = () => {
    video.style.display = "none";
    frame.classList.remove("presenter-active");
    playButton.textContent = started ? "↻ Replay intro" : "▶ Meet Mayank";
  };

  const startPlayback = async () => {
    showStatus("");
    video.style.display = "block";
    frame.classList.add("presenter-active");
    if (video.ended) video.currentTime = 0;
    try {
      await video.play();
      started = true;
      playButton.textContent = "Ⅱ Pause intro";
    } catch (err) {
      // If autoplay was blocked with sound, retry unmuted
      if (!video.muted) {
        video.muted = true;
        muteButton.textContent = "Sound on";
        await video.play();
        started = true;
        playButton.textContent = "Ⅱ Pause intro";
      } else {
        throw err;
      }
    }
  };

  playButton.addEventListener("click", async () => {
    if (!video.paused && !video.ended) {
      video.pause();
      playButton.textContent = "▶ Resume intro";
      return;
    }
    showStatus("");
    try {
      await startPlayback();
    } catch {
      restorePoster();
      showStatus("The introduction could not play. You can read it with the Text button.");
    }
  });

  video.addEventListener("playing", () => {
    frame.classList.add("presenter-active");
    video.style.display = "block";
    playButton.textContent = "Ⅱ Pause intro";
    showStatus("");
  });

  video.addEventListener("pause", () => {
    playButton.textContent = "▶ Resume intro";
  });

  video.addEventListener("ended", restorePoster);
  video.addEventListener("error", () => {
    restorePoster();
    showStatus("The introduction is temporarily unavailable. Use Text to read it.");
  });

  muteButton.addEventListener("click", async () => {
    const enablingSound = video.muted;
    video.muted = !enablingSound;
    muteButton.textContent = video.muted ? "Sound on" : "Mute sound";
    if (enablingSound && video.paused) {
      try { await startPlayback(); }
      catch { showStatus("Select Meet Mayank to play the introduction."); }
    }
  });

  stopButton.addEventListener("click", () => {
    video.pause();
    video.currentTime = 0;
    restorePoster();
  });

  textButton.addEventListener("click", () => {
    transcript.hidden = !transcript.hidden;
    textButton.setAttribute("aria-expanded", String(!transcript.hidden));
  });

  document.addEventListener("visibilitychange", () => {
    if (document.hidden && !video.paused) {
      video.pause();
      playButton.textContent = "▶ Resume intro";
    }
  });
})();
