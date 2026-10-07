(() => {
  "use strict";
  const config = window.MAYANK_PRESENTER;
  // Enable only after the real speaking clip has been generated and delivered.
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
  video.style.display = "none";
  const canvas = document.createElement("canvas");
  canvas.className = "presenter-canvas";
  canvas.setAttribute("aria-label", "Animated Mayank introducing his portfolio");
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
  frame.append(video, canvas, controls, transcript, status);

  let renderer = null;
  let initializing = null;
  let frameRequest = null;
  let usingNativeAlpha = false;
  let started = false;
  const showStatus = text => {
    status.textContent = text;
    status.hidden = !text;
  };
  const stopDrawing = () => {
    if (frameRequest === null) return;
    if (video.cancelVideoFrameCallback) video.cancelVideoFrameCallback(frameRequest);
    else cancelAnimationFrame(frameRequest);
    frameRequest = null;
  };
  const draw = () => {
    if (video.paused || video.ended || !renderer) return;
    renderer.render(video);
    frameRequest = video.requestVideoFrameCallback ? video.requestVideoFrameCallback(draw) : requestAnimationFrame(draw);
  };
  const restorePoster = () => {
    stopDrawing();
    frame.classList.remove("presenter-active");
    playButton.textContent = started ? "↻ Replay intro" : "▶ Meet Mayank";
  };

  function createRenderer() {
    const gl = canvas.getContext("webgl", { alpha:true, premultipliedAlpha:false });
    if (!gl) return null;
    const compile = (type, source) => {
      const shader = gl.createShader(type);
      gl.shaderSource(shader, source);
      gl.compileShader(shader);
      if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) throw new Error("Shader initialization failed");
      return shader;
    };
    const program = gl.createProgram();
    gl.attachShader(program, compile(gl.VERTEX_SHADER, "attribute vec2 pos; varying vec2 uv; void main(){uv=vec2((pos.x+1.0)*0.5,(1.0-pos.y)*0.5);gl_Position=vec4(pos,0.0,1.0);}"));
    gl.attachShader(program, compile(gl.FRAGMENT_SHADER, "precision mediump float; varying vec2 uv; uniform sampler2D clip; void main(){vec3 c=texture2D(clip,uv).rgb;float excess=c.g-max(c.r,c.b);float a=1.0-smoothstep(0.08,0.28,excess);a*=smoothstep(0.15,0.42,length(c-vec3(0.0,1.0,0.0)));c.g=mix(min(c.g,max(c.r,c.b)+0.02),c.g,a);gl_FragColor=vec4(c,a);}"));
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) throw new Error("Renderer initialization failed");
    gl.useProgram(program);
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1,-1,1,-1,-1,1,1,1]), gl.STATIC_DRAW);
    const position = gl.getAttribLocation(program, "pos");
    gl.enableVertexAttribArray(position);
    gl.vertexAttribPointer(position, 2, gl.FLOAT, false, 0, 0);
    const texture = gl.createTexture();
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.uniform1i(gl.getUniformLocation(program, "clip"), 0);
    return { render(source) {
      if (canvas.width !== source.videoWidth || canvas.height !== source.videoHeight) {
        canvas.width = source.videoWidth;
        canvas.height = source.videoHeight;
        gl.viewport(0, 0, canvas.width, canvas.height);
      }
      gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, source);
      gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    }};
  }
  const initialize = async () => {
    if (initializing) return initializing;
    initializing = (async () => {
      try { renderer = createRenderer(); } catch { renderer = null; }
      if (!renderer) {
        if (!config.alphaVideoSrc) throw new Error("This browser cannot display the avatar animation.");
        usingNativeAlpha = true;
        video.src = config.alphaVideoSrc;
        video.style.display = "";
        video.className = "presenter-alpha-video";
        canvas.remove();
      }
      video.load();
    })();
    return initializing;
  };

  const startPlayback = async () => {
    showStatus("");
    await initialize();
    if (video.ended) video.currentTime = 0;
    await video.play();
    started = true;
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
    playButton.textContent = "Ⅱ Pause intro";
    showStatus("");
    stopDrawing();
    if (!usingNativeAlpha) draw();
  });
  video.addEventListener("pause", stopDrawing);
  video.addEventListener("ended", restorePoster);
  video.addEventListener("error", () => {
    restorePoster();
    showStatus("The introduction is temporarily unavailable. Use Text to read it.");
  });
  muteButton.addEventListener("click", async () => {
    const enablingSound = video.muted;
    video.muted = !enablingSound;
    muteButton.textContent = video.muted ? "Sound on" : "Mute sound";
    if (enablingSound) {
      video.currentTime = 0;
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
  // Muted playback is allowed on load; spoken audio starts with visitor input.
  // Honor visitors who request reduced motion and wait until the home hero is visible.
  if (config.autoplay && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const observer = new IntersectionObserver(async entries => {
      if (!entries.some(entry => entry.isIntersecting)) return;
      observer.disconnect();
      try { await startPlayback(); }
      catch { restorePoster(); }
    }, { threshold: 0.35 });
    observer.observe(frame);
  }
})();
