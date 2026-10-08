(() => {
  "use strict";
  const config = window.MAYANK_PRESENTER;
  const frame = document.getElementById("home-presenter");
  // Activate only after the actual character clip has been delivered.
  if (!config?.videoSrc || !frame) return;
  const hero = frame.closest("#hero");
  const sceneVideo = Boolean(config.sceneVideo && hero);
  const controls = frame.querySelector(".presenter-controls");
  const play = document.getElementById("presenter-play");
  const sound = document.getElementById("presenter-sound");
  const video = document.createElement("video");
  video.crossOrigin = "anonymous";
  video.src = config.videoSrc;
  video.preload = "metadata";
  video.playsInline = true;
  video.muted = true;
  video.setAttribute("aria-label", "Mayank introducing his portfolio");
  const canvas = document.createElement("canvas");
  canvas.className = "presenter-canvas";
  canvas.setAttribute("role", "img");
  canvas.setAttribute("aria-label", "Mayank's animated 3D introduction");
  frame.prepend(canvas);
  if (sceneVideo) hero.prepend(video);
  else frame.prepend(video);
  let renderer = null;
  let drawing = null;
  let visible = false;
  let started = false;
  let userPaused = false;
  const reduceMotion = matchMedia("(prefers-reduced-motion: reduce)");
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

  function stopDrawing() {
    if (drawing === null) return;
    if (video.cancelVideoFrameCallback) video.cancelVideoFrameCallback(drawing);
    else cancelAnimationFrame(drawing);
    drawing = null;
  }
  function draw() {
    if (video.paused || video.ended || !renderer) return;
    try { renderer.render(video); }
    catch { unavailable(); return; }
    drawing = video.requestVideoFrameCallback ? video.requestVideoFrameCallback(draw) : requestAnimationFrame(draw);
  }
  function updatePlay() {
    play.textContent = video.ended ? "Replay introduction" : video.paused ? (started ? "Resume introduction" : "Play introduction") : "Pause introduction";
    play.setAttribute("aria-label", play.textContent);
  }
  function unavailable() {
    video.pause();
    stopDrawing();
    frame.classList.remove("presenter-active");
    hero?.classList.remove("scene-video-active");
    controls.hidden = true;
  }
  async function start() {
    if (video.ended) video.currentTime = 0;
    try { await video.play(); }
    catch { updatePlay(); }
  }
  if (config.chromaKey) {
    video.hidden = true;
    try { renderer = createRenderer(); }
    catch {
      if (!config.alphaVideoSrc || !video.canPlayType('video/webm; codecs="vp9"')) return;
      video.hidden = false;
      video.src = config.alphaVideoSrc;
      video.className = "presenter-video";
      canvas.remove();
    }
  } else {
    canvas.remove();
    video.className = sceneVideo ? "presenter-scene-video" : "presenter-video";
  }
  video.addEventListener("loadeddata", () => { controls.hidden = false; });
  video.addEventListener("playing", () => {
    started = true;
    frame.classList.add("presenter-active");
    if (sceneVideo) hero.classList.add("scene-video-active");
    updatePlay();
    stopDrawing();
    if (renderer) draw();
  });
  video.addEventListener("pause", () => { stopDrawing(); updatePlay(); });
  video.addEventListener("ended", () => { stopDrawing(); updatePlay(); });
  video.addEventListener("error", unavailable);
  play.addEventListener("click", () => {
    if (!video.paused && !video.ended) { userPaused = true; video.pause(); }
    else { userPaused = false; start(); }
  });
  sound.addEventListener("click", () => {
    video.muted = !video.muted;
    sound.textContent = video.muted ? "Sound on" : "Mute sound";
    sound.setAttribute("aria-label", sound.textContent);
    if (!video.muted) { video.currentTime = 0; userPaused = false; start(); }
  });
  const observer = new IntersectionObserver(entries => {
    visible = entries.some(entry => entry.isIntersecting);
    if (!visible) video.pause();
    else if (config.autoplay && !reduceMotion.matches && !userPaused && !video.ended && !document.hidden) start();
  }, {threshold: .35});
  observer.observe(frame);
  document.addEventListener("visibilitychange", () => {
    if (document.hidden) video.pause();
    else if (visible && config.autoplay && !reduceMotion.matches && !userPaused && !video.ended) start();
  });
  reduceMotion.addEventListener("change", event => { if (event.matches) video.pause(); });
})();
