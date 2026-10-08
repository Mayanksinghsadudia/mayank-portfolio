import os
import wave
import subprocess
import numpy as np
import cv2
import imageio_ffmpeg

def main():
    print("=== Generating Fluid, Continuous 3D Presenter Video ===")
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # 1. Load Audio and compute envelope
    audio_path = 'assets/temp_audio.wav'
    if not os.path.exists(audio_path):
        audio_path = r'C:\Users\hp\Documents\Codex\2026-10-07\https-www-instagram-com-p-deixis4avpj\outputs\Mayank-Indian-English-introduction.wav'

    wav_temp = 'assets/speech_audio_30s.wav'
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
    # Smooth with 3-frame kernel for reactive speech syllables
    smoothed = np.convolve(rms_values, np.ones(3)/3.0, mode='same')
    
    active_frames = int(26.5 * fps)
    p90 = np.percentile(smoothed[:active_frames], 90) if len(smoothed) > 0 else 1.0
    p10 = np.percentile(smoothed[:active_frames], 10) if len(smoothed) > 0 else 0.0
    mouth_open = np.clip((smoothed - p10) / (p90 - p10 + 1e-6), 0.0, 1.0) ** 0.85
    # Force mouth closed after 26.5s and during pause at 12.3-12.8s
    mouth_open[int(26.5 * fps):] = 0.0
    pause_start, pause_end = int(12.35 * fps), int(12.75 * fps)
    mouth_open[pause_start:pause_end] *= np.linspace(1.0, 0.0, pause_end - pause_start)

    # 2. Load Reel Poses (1376x768)
    W, H = 1376, 768
    raw_r = cv2.imread('assets/reel_pose_rest.jpg')
    raw_t = cv2.imread('assets/reel_pose_talk.jpg')
    raw_p = cv2.imread('assets/reel_pose_pres.jpg')

    im_r = cv2.resize(raw_r, (W, H), interpolation=cv2.INTER_LANCZOS4)
    im_t = cv2.resize(raw_t, (W, H), interpolation=cv2.INTER_LANCZOS4)
    im_p = cv2.resize(raw_p, (W, H), interpolation=cv2.INTER_LANCZOS4)

    # 3. Setup Coordinate Grids & Anatomical Masks
    gx, gy = np.meshgrid(np.arange(W), np.arange(H))
    
    # Accurate Mouth Aperture (Center: x=962, y=164)
    dist_mouth = ((gx - 962.0) / 25.0)**2 + ((gy - 164.0) / 14.0)**2
    mouth_mask = np.clip(1.0 - dist_mouth, 0.0, 1.0)[:, :, None].astype(np.float32)

    # Pre-render closed-mouth versions of talk and pres poses
    closed_t = (im_t.astype(np.float32) * (1.0 - mouth_mask) + im_r.astype(np.float32) * mouth_mask).astype(np.uint8)
    closed_p = (im_p.astype(np.float32) * (1.0 - mouth_mask) + im_r.astype(np.float32) * mouth_mask).astype(np.uint8)

    # Jaw / Chin Drop Weight (Center: x=962, y=176)
    dx_chin = (gx - 962.0) / 26.0
    dy_chin = (gy - 176.0) / 16.0
    chin_weight = np.exp(-(dx_chin**2 + dy_chin**2)).astype(np.float32)
    chin_weight[gy < 162] = 0.0 # Only pull down below the upper lip

    # Eye Blink Weights (Left eye: x=942, y=131; Right eye: x=982, y=131)
    eye_w_left = np.exp(-(((gx - 942.0)/12.0)**2 + ((gy - 131.0)/9.0)**2))
    eye_w_right = np.exp(-(((gx - 982.0)/12.0)**2 + ((gy - 131.0)/9.0)**2))
    eye_weight = np.clip(eye_w_left + eye_w_right, 0.0, 1.0).astype(np.float32)

    # Arm region mask for micro-articulation and motion blur (x: 720..900, y: 240..430)
    arm_region = np.exp(-(((gx - 800.0)/80.0)**2 + ((gy - 340.0)/70.0)**2)).astype(np.float32)
    arm_mask = np.zeros((H, W), dtype=np.float32)
    arm_mask[240:430, 720:900] = 1.0
    arm_mask = cv2.GaussianBlur(arm_mask, (25, 25), 0)[:, :, None]

    # Monitor Glow Mask (x: 780..1270, y: 200..380)
    monitor_mask = np.zeros((H, W), dtype=np.float32)
    monitor_mask[200:380, 780:1270] = 1.0
    monitor_mask = cv2.GaussianBlur(monitor_mask, (41, 41), 0)[:, :, None]

    # Motion blur kernel for rapid gesture transitions (11px vertical)
    k_size = 11
    mb_kernel = np.zeros((k_size, k_size))
    mb_kernel[:, int((k_size - 1)/2)] = np.ones(k_size) / k_size

    # 4. Blink Schedule (every ~3.6 seconds)
    blink_times = [2.2, 5.8, 9.4, 13.0, 16.8, 20.6, 24.2, 28.0]
    def get_blink_factor(t):
        for bt in blink_times:
            dt = t - bt
            if 0.0 <= dt <= 0.17: # ~5 frames
                # Smooth blink curve: 0 -> 1 -> 0
                phase = dt / 0.17
                return np.sin(phase * np.pi)
        return 0.0

    # 5. Timeline Function for High-Level Pose State
    # Transitions are snappy (6 frames = 0.20s) with motion blur, not slow 1-second crossfades!
    def get_timeline_pose(t):
        # 0.0 to 6.6s: Talk (intro)
        if t < 6.6:
            return ('talk', 'talk', 0.0)
        # 6.6 to 6.8s: Quick gesture UP -> Present (screens)
        elif t < 6.8:
            return ('talk', 'pres', (t - 6.6) / 0.20)
        # 6.8 to 12.2s: Present monitors
        elif t < 12.2:
            return ('pres', 'pres', 0.0)
        # 12.2 to 12.4s: Quick gesture DOWN -> Talk during speech pause
        elif t < 12.4:
            return ('pres', 'talk', (t - 12.2) / 0.20)
        # 12.4 to 18.6s: Talk (creative design)
        elif t < 18.6:
            return ('talk', 'talk', 0.0)
        # 18.6 to 18.8s: Quick gesture UP -> Present (portfolio harmony)
        elif t < 18.8:
            return ('talk', 'pres', (t - 18.6) / 0.20)
        # 18.8 to 23.2s: Present screens
        elif t < 23.2:
            return ('pres', 'pres', 0.0)
        # 23.2 to 23.4s: Quick gesture DOWN -> Talk (call to action)
        elif t < 23.4:
            return ('pres', 'talk', (t - 23.2) / 0.20)
        # 23.4 to 26.5s: Talk (GitHub / collaboration)
        elif t < 26.5:
            return ('talk', 'talk', 0.0)
        # 26.5 to 27.2s: Smooth return to Rest pose as speech finishes
        elif t < 27.2:
            return ('talk', 'rest', (t - 26.5) / 0.70)
        # 27.2 to 30.0s: Confident Rest with continuous breathing & sway
        else:
            return ('rest', 'rest', 0.0)

    # 6. Setup FFmpeg Output Pipe
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
        '-crf', '18',
        '-c:a', 'aac',
        '-b:a', '192k',
        '-movflags', '+faststart',
        out_video
    ]
    
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)

    print("Rendering fluid continuous presenter frames (900 frames)...")
    for f in range(total_frames):
        t = f / fps
        pose_a, pose_b, blend = get_timeline_pose(t)
        op = mouth_open[f]
        blink_fac = get_blink_factor(t)
        is_speaking = 1.0 if (t < 26.4 and op > 0.05) else 0.0

        # A. Base frame rendering with syllable lip-sync
        def get_pose_frame(pose_key):
            if pose_key == 'rest':
                return im_r
            elif pose_key == 'talk':
                # Blend between closed mouth and open mouth
                return (closed_t.astype(np.float32) * (1.0 - op) + im_t.astype(np.float32) * op).astype(np.uint8)
            elif pose_key == 'pres':
                return (closed_p.astype(np.float32) * (1.0 - op) + im_p.astype(np.float32) * op).astype(np.uint8)

        if blend == 0.0 or pose_a == pose_b:
            frame = get_pose_frame(pose_a)
        else:
            frame_a = get_pose_frame(pose_a)
            frame_b = get_pose_frame(pose_b)
            # Smoothstep blend
            s = blend * blend * (3.0 - 2.0 * blend)
            frame_blend = cv2.addWeighted(frame_a, 1.0 - s, frame_b, s, 0)
            
            # Apply directional motion blur to transitioning arm for natural rapid gesture
            if 0.15 < blend < 0.85:
                arm_crop = frame_blend[240:430, 720:900]
                blurred_arm = cv2.filter2D(arm_crop, -1, mb_kernel)
                frame_blend[240:430, 720:900] = blurred_arm
            frame = frame_blend

        # B. Syllable-Driven Chin & Jaw Dropping Remap
        if op > 0.02:
            disp_jaw = (4.0 * op * chin_weight).astype(np.float32)
            map_x = gx.astype(np.float32)
            map_y = (gy - disp_jaw).astype(np.float32)
            frame = cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR)

        # C. Eyelid Blinking Remap
        if blink_fac > 0.02:
            disp_blink = (5.5 * blink_fac * eye_weight).astype(np.float32)
            map_x = gx.astype(np.float32)
            map_y = (gy - disp_blink).astype(np.float32)
            frame = cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR)

        # D. Dynamic Hand/Arm Micro-Articulations (Subtle speech cadence gestures)
        if pose_a != 'rest' and is_speaking > 0.0:
            arm_dy = int(round(3.5 * np.cos(2 * np.pi * t / 1.6) * is_speaking + 2.0 * op))
            arm_dx = int(round(2.0 * np.sin(2 * np.pi * t / 1.4) * is_speaking))
            if arm_dy != 0 or arm_dx != 0:
                M_arm = np.float32([[1, 0, arm_dx], [0, 1, arm_dy]])
                warped_arm = cv2.warpAffine(frame, M_arm, (W, H), borderMode=cv2.BORDER_REFLECT)
                frame = (frame.astype(np.float32) * (1.0 - arm_mask) + warped_arm.astype(np.float32) * arm_mask).astype(np.uint8)

        # E. Continuous Skeletal Kinematics across the ENTIRE scene (Never Freezes!)
        # 1. Weight shift sway: compound harmonic wave
        x_sway = 3.6 * np.sin(2 * np.pi * t / 3.4) + 1.2 * np.sin(2 * np.pi * t / 1.7 + 0.4)
        # 2. Breathing expansion: vertical diaphragmatic lift
        y_breath = 2.4 * np.sin(2 * np.pi * t / 3.8)
        # 3. Conversational head nod & accent on stressed syllables
        y_nod = 3.2 * op + 1.0 * np.sin(2 * np.pi * t / 1.25) * is_speaking
        # 4. Subtle conversational head tilt
        angle_tilt = 0.8 * np.sin(2 * np.pi * t / 2.7) * (1.0 if t < 26.5 else 0.3)

        total_dx = x_sway
        total_dy = y_breath + y_nod

        # Sub-pixel bilinear warp for organic float
        center = (962.0, 200.0)
        M_kinematic = cv2.getRotationMatrix2D(center, angle_tilt, 1.0)
        M_kinematic[0, 2] += total_dx
        M_kinematic[1, 2] += total_dy

        frame_kinematic = cv2.warpAffine(frame, M_kinematic, (W, H), borderMode=cv2.BORDER_REFLECT, flags=cv2.INTER_LINEAR)

        # F. Active Monitor Screen Pulse & Code Glow
        pulse = 1.0 + 0.035 * np.sin(2 * np.pi * t / 1.5) + 0.015 * np.cos(2 * np.pi * t / 0.8)
        frame_flt = frame_kinematic.astype(np.float32)
        frame_flt = frame_flt * (1.0 - monitor_mask * 0.16) + (frame_flt * pulse) * (monitor_mask * 0.16)

        final_frame = np.clip(frame_flt, 0, 255).astype(np.uint8)
        proc.stdin.write(final_frame.tobytes())

        if f % 150 == 0:
            print(f"  Rendered Frame {f}/{total_frames} ({t:.1f}s / 30.0s)")

    proc.stdin.close()
    proc.wait()
    print("=== Master 3D Presenter Video Generated Successfully! ===")
    print(f"Saved to: {out_video}")

if __name__ == '__main__':
    main()
