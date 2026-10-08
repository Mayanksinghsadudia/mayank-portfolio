import os
import wave
import subprocess
import numpy as np
import cv2
import imageio_ffmpeg

def main():
    print("=== Generating Reel-Style 3D Presenter Video (Gemini AI Engine) ===")
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # 1. Load Audio and compute envelope
    audio_path = 'assets/temp_audio.wav'
    if not os.path.exists(audio_path):
        audio_path = r'C:\Users\hp\Documents\Codex\2026-10-07\https-www-instagram-com-p-deixis4avpj\outputs\Mayank-Indian-English-introduction.wav'

    # Convert audio to wav if mp3
    wav_temp = 'assets/speech_audio_30s.wav'
    # Ensure 30s audio with pad
    subprocess.run([
        ffmpeg_exe, '-y',
        '-i', audio_path,
        '-af', 'apad=whole_dur=30',
        '-t', '30',
        '-c:a', 'pcm_s16le',
        '-ar', '24000',
        '-ac', '1',
        wav_temp
    ], check=True)

    with wave.open(wav_temp, 'rb') as w:
        sr = w.getframerate()
        n_samples = w.getnframes()
        raw_audio = np.frombuffer(w.readframes(n_samples), dtype=np.int16).astype(np.float32)
        duration = n_samples / sr

    fps = 30
    total_frames = int(round(duration * fps)) # 900 frames for 30s
    samples_per_frame = sr / fps
    print(f"Audio duration: {duration:.2f}s, total frames: {total_frames} at {fps} fps")

    # Compute RMS energy per frame
    rms_values = []
    for i in range(total_frames):
        s_start = int(i * samples_per_frame)
        s_end = min(int((i + 1) * samples_per_frame), n_samples)
        chunk = raw_audio[s_start:s_end]
        if len(chunk) > 0:
            rms = np.sqrt(np.mean(chunk**2))
        else:
            rms = 0.0
        rms_values.append(rms)
    
    rms_values = np.array(rms_values)
    smoothed = np.convolve(rms_values, np.ones(3)/3.0, mode='same')
    
    p95 = np.percentile(smoothed[:int(27.0*fps)], 95) if len(smoothed) > 0 else 1.0
    p15 = np.percentile(smoothed[:int(27.0*fps)], 15) if len(smoothed) > 0 else 0.0
    mouth_open = np.clip((smoothed - p15) / (p95 - p15 + 1e-6), 0.0, 1.0) ** 0.80
    # ensure mouth is closed after 27.2s
    mouth_open[int(27.2 * fps):] = 0.0

    # 2. Load Reel Poses (1376x768)
    W, H = 1376, 768
    raw_r = cv2.imread('assets/reel_pose_rest.jpg')
    raw_t = cv2.imread('assets/reel_pose_talk.jpg')
    raw_p = cv2.imread('assets/reel_pose_pres.jpg')

    im_r = cv2.resize(raw_r, (W, H), interpolation=cv2.INTER_LANCZOS4)
    im_t = cv2.resize(raw_t, (W, H), interpolation=cv2.INTER_LANCZOS4)
    im_p = cv2.resize(raw_p, (W, H), interpolation=cv2.INTER_LANCZOS4)

    # 3. Feathered Mouth Mask
    # Global mouth center: x = 964, y = 120
    gy, gx = np.ogrid[:H, :W]
    dist_mouth = ((gx - 964.0) / 22.0)**2 + ((gy - 120.0) / 16.0)**2
    mouth_mask = np.clip(1.0 - dist_mouth, 0.0, 1.0) ** 1.5
    mouth_mask_3c = mouth_mask[:, :, None].astype(np.float32)

    # Pre-render closed-mouth versions for talk and pres poses
    closed_t = (im_t.astype(np.float32) * (1.0 - mouth_mask_3c) + im_r.astype(np.float32) * mouth_mask_3c).astype(np.uint8)
    closed_p = (im_p.astype(np.float32) * (1.0 - mouth_mask_3c) + im_r.astype(np.float32) * mouth_mask_3c).astype(np.uint8)

    # Monitor screen glow mask (x: 780 to 1270, y: 200 to 380)
    monitor_mask = np.zeros((H, W), dtype=np.float32)
    monitor_mask[200:380, 780:1270] = 1.0
    monitor_mask = cv2.GaussianBlur(monitor_mask, (41, 41), 0)[:, :, None]

    # 4. Setup FFmpeg Output Pipe
    out_video = 'assets/mayank_reel_presenter.mp4'
    cmd = [
        ffmpeg_exe, '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{W}x{H}',
        '-pix_fmt', 'bgr24',
        '-r', str(fps),
        '-i', '-',
        '-i', wav_temp,
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'fast',
        '-crf', '19',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-movflags', '+faststart',
        out_video
    ]
    
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    # 5. Timeline Function
    def get_timeline_state(t):
        if t < 0.8:
            return ('rest', 'rest', 0.0)
        elif t < 1.4:
            alpha = (t - 0.8) / 0.6
            return ('rest', 'talk', alpha)
        elif t < 6.2:
            return ('talk', 'talk', 0.0)
        elif t < 7.0:
            alpha = (t - 6.2) / 0.8
            return ('talk', 'pres', alpha)
        elif t < 12.0:
            return ('pres', 'pres', 0.0)
        elif t < 12.8:
            alpha = (t - 12.0) / 0.8
            return ('pres', 'talk', alpha)
        elif t < 20.5:
            return ('talk', 'talk', 0.0)
        elif t < 21.3:
            alpha = (t - 20.5) / 0.8
            return ('talk', 'pres', alpha)
        elif t < 24.5:
            return ('pres', 'pres', 0.0)
        elif t < 25.5:
            alpha = (t - 24.5) / 1.0
            return ('pres', 'rest', alpha)
        else:
            return ('rest', 'rest', 0.0)

    def smoothstep(x):
        return x * x * (3.0 - 2.0 * x)

    print("Rendering Reel-style presenter frames...")
    for f in range(total_frames):
        t = f / fps
        pose_a, pose_b, blend = get_timeline_state(t)
        s_blend = smoothstep(blend)
        openness = mouth_open[f]

        def render_pose(key):
            if key == 'rest':
                return im_r
            elif key == 'talk':
                o = float(openness)
                return (closed_t.astype(np.float32) * (1.0 - o) + im_t.astype(np.float32) * o).astype(np.uint8)
            elif key == 'pres':
                o = float(openness)
                return (closed_p.astype(np.float32) * (1.0 - o) + im_p.astype(np.float32) * o).astype(np.uint8)

        frame_a = render_pose(pose_a)
        if blend == 0.0 or pose_a == pose_b:
            frame = frame_a
        else:
            frame_b = render_pose(pose_b)
            frame = cv2.addWeighted(frame_a, 1.0 - s_blend, frame_b, s_blend, 0)

        # Micro-dynamics: breathing + subtle speech nod
        y_breath = 1.0 * np.sin(2 * np.pi * t / 3.4)
        x_sway = 0.6 * np.sin(2 * np.pi * t / 5.0)
        y_nod = 1.2 * openness if pose_a != 'rest' else 0.0

        dy = int(round(y_breath + y_nod))
        dx = int(round(x_sway))

        if dy != 0 or dx != 0:
            M_trans = np.float32([[1, 0, dx], [0, 1, dy]])
            frame = cv2.warpAffine(frame, M_trans, (W, H), borderMode=cv2.BORDER_REFLECT)

        # Ambient monitor data pulse
        pulse = 1.0 + 0.03 * np.sin(2 * np.pi * t / 1.6)
        frame_flt = frame.astype(np.float32)
        frame_flt = frame_flt * (1.0 - monitor_mask * 0.18) + (frame_flt * pulse) * (monitor_mask * 0.18)

        final_frame = np.clip(frame_flt, 0, 255).astype(np.uint8)
        proc.stdin.write(final_frame.tobytes())

        if f % 150 == 0:
            print(f"  Frame {f}/{total_frames} ({t:.1f}s)")

    proc.stdin.close()
    proc.wait()
    print("Reel-style presenter video generated successfully!")
    print(f"Output saved to: {out_video}")

if __name__ == '__main__':
    main()
