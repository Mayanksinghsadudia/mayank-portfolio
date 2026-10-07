import os
import wave
import subprocess
import numpy as np
import cv2
import imageio_ffmpeg

def main():
    print("=== Generating High-Fidelity Studio Presenter Video (Google Veo / Flow Style) ===")
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # 1. Load Audio and compute envelope
    audio_wav = 'assets/temp_audio.wav'
    with wave.open(audio_wav, 'rb') as w:
        sr = w.getframerate()
        n_samples = w.getnframes()
        raw_audio = np.frombuffer(w.readframes(n_samples), dtype=np.int16).astype(np.float32)
        duration = n_samples / sr

    fps = 30
    total_frames = int(round(duration * fps))
    samples_per_frame = sr / fps
    print(f"Audio duration: {duration:.2f}s, total frames: {total_frames} at {fps} fps")

    # RMS energy envelope
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
    
    p95 = np.percentile(smoothed, 95) if len(smoothed) > 0 else 1.0
    p15 = np.percentile(smoothed, 15) if len(smoothed) > 0 else 0.0
    mouth_open = np.clip((smoothed - p15) / (p95 - p15 + 1e-6), 0.0, 1.0) ** 0.80

    # 2. Load Studio Poses (720x960)
    W, H = 720, 960
    raw_r = cv2.imread('assets/studio_pose_rest.jpg')
    raw_t = cv2.imread('assets/studio_pose_talk.jpg')
    raw_p = cv2.imread('assets/studio_pose_pres.jpg')

    im_r = cv2.resize(raw_r, (W, H), interpolation=cv2.INTER_LANCZOS4)
    im_t = cv2.resize(raw_t, (W, H), interpolation=cv2.INTER_LANCZOS4)
    im_p = cv2.resize(raw_p, (W, H), interpolation=cv2.INTER_LANCZOS4)

    # 3. Create Feathered Mouth Mask
    # Mouth location in 720x960: center x=225, y=208, rx=34, ry=24
    gy, gx = np.ogrid[:H, :W]
    dist_mouth = ((gx - 225.0) / 34.0)**2 + ((gy - 208.0) / 24.0)**2
    mouth_mask = np.clip(1.0 - dist_mouth, 0.0, 1.0) ** 1.5
    mouth_mask_3c = mouth_mask[:, :, None].astype(np.float32)

    # Pre-render closed-mouth versions for talk and pres poses
    closed_t = (im_t.astype(np.float32) * (1.0 - mouth_mask_3c) + im_r.astype(np.float32) * mouth_mask_3c).astype(np.uint8)
    closed_p = (im_p.astype(np.float32) * (1.0 - mouth_mask_3c) + im_r.astype(np.float32) * mouth_mask_3c).astype(np.uint8)

    # Monitor screen coordinates for ambient UI pulse (x: 110 to 550, y: 160 to 350)
    monitor_mask = np.zeros((H, W), dtype=np.float32)
    monitor_mask[160:350, 110:550] = 1.0
    monitor_mask = cv2.GaussianBlur(monitor_mask, (31, 31), 0)[:, :, None]

    # 4. Setup FFmpeg Pipe
    out_video = 'assets/mayank_presenter_video.mp4'
    cmd = [
        ffmpeg_exe, '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{W}x{H}',
        '-pix_fmt', 'bgr24',
        '-r', str(fps),
        '-i', '-',
        '-i', audio_wav,
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-preset', 'slow',
        '-crf', '18',
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
        elif t < 1.3:
            alpha = (t - 0.8) / 0.5
            return ('rest', 'talk', alpha)
        elif t < 5.2:
            return ('talk', 'talk', 0.0)
        elif t < 5.7:
            alpha = (t - 5.2) / 0.5
            return ('talk', 'pres', alpha)
        elif t < 10.2:
            return ('pres', 'pres', 0.0)
        elif t < 10.7:
            alpha = (t - 10.2) / 0.5
            return ('pres', 'talk', alpha)
        elif t < 16.2:
            return ('talk', 'talk', 0.0)
        elif t < 16.7:
            alpha = (t - 16.2) / 0.5
            return ('talk', 'pres', alpha)
        elif t < 21.0:
            return ('pres', 'pres', 0.0)
        elif t < 21.5:
            alpha = (t - 21.0) / 0.5
            return ('pres', 'talk', alpha)
        elif t < 25.5:
            return ('talk', 'talk', 0.0)
        elif t < 26.5:
            alpha = (t - 25.5) / 1.0
            return ('talk', 'rest', alpha)
        else:
            return ('rest', 'rest', 0.0)

    # Ease-in-out curve
    def smoothstep(x):
        return x * x * (3.0 - 2.0 * x)

    print("Rendering studio presenter frames...")
    for f in range(total_frames):
        t = f / fps
        pose_a, pose_b, blend = get_timeline_state(t)
        s_blend = smoothstep(blend)

        openness = mouth_open[f]

        # Generate base pose with accurate mouth state
        def render_pose(key):
            if key == 'rest':
                return im_r
            elif key == 'talk':
                # Blend between closed_t and open im_t based on audio energy
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

        # Micro-dynamics: breathing + vocal nod
        y_breath = 1.2 * np.sin(2 * np.pi * t / 3.2)
        x_sway = 0.8 * np.sin(2 * np.pi * t / 4.8)
        y_nod = 1.5 * openness if pose_a != 'rest' else 0.0
        
        dy = int(round(y_breath + y_nod))
        dx = int(round(x_sway))

        if dy != 0 or dx != 0:
            M_trans = np.float32([[1, 0, dx], [0, 1, dy]])
            frame = cv2.warpAffine(frame, M_trans, (W, H), borderMode=cv2.BORDER_REFLECT)

        # Ambient monitor data pulse (realistic active UI screen glow)
        pulse = 1.0 + 0.025 * np.sin(2 * np.pi * t / 1.8)
        frame_flt = frame.astype(np.float32)
        frame_flt = frame_flt * (1.0 - monitor_mask * 0.15) + (frame_flt * pulse) * (monitor_mask * 0.15)

        # Slow cinematic Veo-style camera push-in: scale 1.000 -> 1.028
        zoom = 1.0 + 0.028 * (f / total_frames)
        M_zoom = cv2.getRotationMatrix2D((W * 0.45, H * 0.35), 0, zoom)
        frame_zoomed = cv2.warpAffine(frame_flt, M_zoom, (W, H), borderMode=cv2.BORDER_REFLECT)

        final_frame = np.clip(frame_zoomed, 0, 255).astype(np.uint8)
        proc.stdin.write(final_frame.tobytes())

        if f % 150 == 0:
            print(f"  Frame {f}/{total_frames} ({t:.1f}s)")

    proc.stdin.close()
    proc.wait()
    print("Studio presenter video generated successfully!")
    print(f"Output saved to: {out_video}")

if __name__ == '__main__':
    main()
