import os
import wave
import subprocess
import numpy as np
import cv2
from PIL import Image
import imageio_ffmpeg

def main():
    print("Starting Mayank Presenter Video Generation...")
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    
    # 1. Load Audio and compute envelope
    with wave.open('assets/temp_audio.wav', 'rb') as w:
        sr = w.getframerate()
        n_samples = w.getnframes()
        raw_audio = np.frombuffer(w.readframes(n_samples), dtype=np.int16).astype(np.float32)
        duration = n_samples / sr

    fps = 30
    total_frames = int(round(duration * fps))
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
    # Smooth RMS envelope (3-frame moving average)
    smoothed = np.convolve(rms_values, np.ones(3)/3.0, mode='same')
    
    # Normalize envelope to [0, 1] mouth openness
    p95 = np.percentile(smoothed, 95) if len(smoothed) > 0 else 1.0
    p10 = np.percentile(smoothed, 15) if len(smoothed) > 0 else 0.0
    mouth_open = np.clip((smoothed - p10) / (p95 - p10 + 1e-6), 0.0, 1.0)
    # Boost speech openness slightly
    mouth_open = mouth_open ** 0.75

    # 2. Load Images
    im_rest = cv2.imread('assets/aligned_avatar_v6.png', cv2.IMREAD_UNCHANGED) # RGBA (960, 720, 4)
    im_talk = cv2.imread('assets/aligned_talking.png', cv2.IMREAD_UNCHANGED)
    im_pres = cv2.imread('assets/aligned_present.png', cv2.IMREAD_UNCHANGED)

    # Load brush stroke for background
    brush_raw = Image.open('assets/user_brush_stroke_theme.png').convert('RGBA')
    brush_w, brush_h = 580, int(580 * brush_raw.height / brush_raw.width)
    brush_resized = brush_raw.resize((brush_w, brush_h), Image.Resampling.LANCZOS)
    brush_arr = np.array(brush_resized)

    # Pre-render background: #131313 with radial glow and brush
    H, W = 960, 720
    bg_canvas = np.full((H, W, 3), 19, dtype=np.float32) # #131313 BGR = (19, 19, 19)

    # Subtle warm radial ambient glow behind torso (center=(360, 290))
    gy, gx = np.ogrid[:H, :W]
    dist_sq = (gx - 360.0)**2 / (280.0**2) + (gy - 290.0)**2 / (340.0**2)
    glow = np.clip(1.0 - dist_sq, 0.0, 1.0) ** 2
    # Warm amber glow BGR=(10, 35, 65)
    bg_canvas[:, :, 0] += glow * 10
    bg_canvas[:, :, 1] += glow * 35
    bg_canvas[:, :, 2] += glow * 65

    # Paste brush stroke onto background
    bx = (W - brush_w) // 2
    by = 120
    brush_rgb = brush_arr[:, :, :3][:, :, ::-1] # RGBA to BGR
    brush_alpha = (brush_arr[:, :, 3:] / 255.0).astype(np.float32)
    
    bg_canvas[by:by+brush_h, bx:bx+brush_w] = (
        bg_canvas[by:by+brush_h, bx:bx+brush_w] * (1.0 - brush_alpha) +
        brush_rgb * brush_alpha
    )

    # Soft floor contact shadow under shoes (ellipse around x=360, y=880)
    shadow_mask = np.clip(1.0 - ((gx - 360.0)**2 / (140.0**2) + (gy - 880.0)**2 / (35.0**2)), 0.0, 1.0) ** 1.5
    bg_canvas *= (1.0 - shadow_mask[:, :, None] * 0.45)
    bg_canvas = np.clip(bg_canvas, 0, 255).astype(np.uint8)

    # 3. Setup FFmpeg pipe
    out_video = 'assets/mayank_presenter_video.mp4'
    cmd = [
        ffmpeg_exe, '-y',
        '-f', 'rawvideo',
        '-vcodec', 'rawvideo',
        '-s', f'{W}x{H}',
        '-pix_fmt', 'bgr24',
        '-r', str(fps),
        '-i', '-',
        '-i', 'assets/temp_audio.wav',
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

    # 4. Timeline Segment Helper
    def get_pose_weights(t):
        if t < 0.7:
            return ('rest', 'rest', 0.0)
        elif t < 1.0:
            alpha = (t - 0.7) / 0.3
            return ('rest', 'talk', alpha)
        elif t < 4.6:
            return ('talk', 'talk', 0.0)
        elif t < 5.0:
            alpha = (t - 4.6) / 0.4
            return ('talk', 'pres', alpha)
        elif t < 9.8:
            return ('pres', 'pres', 0.0)
        elif t < 10.2:
            alpha = (t - 9.8) / 0.4
            return ('pres', 'talk', alpha)
        elif t < 15.6:
            return ('talk', 'talk', 0.0)
        elif t < 16.0:
            alpha = (t - 15.6) / 0.4
            return ('talk', 'pres', alpha)
        elif t < 20.6:
            return ('pres', 'pres', 0.0)
        elif t < 21.0:
            alpha = (t - 20.6) / 0.4
            return ('pres', 'talk', alpha)
        elif t < 25.2:
            return ('talk', 'talk', 0.0)
        elif t < 25.8:
            alpha = (t - 25.2) / 0.6
            return ('talk', 'rest', alpha)
        else:
            return ('rest', 'rest', 0.0)

    pose_dict = {
        'rest': im_rest,
        'talk': im_talk,
        'pres': im_pres
    }

    # Remap coordinates for mouth openness on talk/pres poses
    grid_y, grid_x = np.mgrid[0:H, 0:W].astype(np.float32)
    m_dx = np.abs(grid_x - 372.0) / 25.0
    m_dy = np.abs(grid_y - 192.0) / 16.0
    mouth_mask = np.clip(1.0 - (m_dx**2 + m_dy**2), 0.0, 1.0) ** 1.5

    print("Rendering frames...")
    for frame_idx in range(total_frames):
        t = frame_idx / fps
        pA_key, pB_key, blend = get_pose_weights(t)

        imA = pose_dict[pA_key]
        imB = pose_dict[pB_key]

        # Smooth ease curve for gesture transition: 3a^2 - 2a^3
        smooth_blend = 3.0 * (blend**2) - 2.0 * (blend**3)

        if blend == 0.0 or pA_key == pB_key:
            current_pose = imA.copy()
        else:
            current_pose = cv2.addWeighted(imA, 1.0 - smooth_blend, imB, smooth_blend, 0)

        # Apply lip sync
        openness = mouth_open[frame_idx]
        if pA_key != 'rest' or (pB_key != 'rest' and blend > 0.5):
            factor = float((1.0 - openness) * 0.52)
            grid_y_remap = (grid_y + (grid_y - 192.0) * mouth_mask * factor).astype(np.float32)
            current_pose = cv2.remap(current_pose, grid_x, grid_y_remap, cv2.INTER_LINEAR)

        # Micro-dynamics: breathing + head speech nod
        y_breath = 1.6 * np.sin(2 * np.pi * t / 3.0)
        x_sway = 1.0 * np.sin(2 * np.pi * t / 4.5)
        y_nod = 1.2 * openness if pA_key != 'rest' else 0.0
        
        dy = int(round(y_breath + y_nod))
        dx = int(round(x_sway))

        if dy != 0 or dx != 0:
            M_trans = np.float32([[1, 0, dx], [0, 1, dy]])
            current_pose = cv2.warpAffine(current_pose, M_trans, (W, H), borderMode=cv2.BORDER_CONSTANT, borderValue=(0,0,0,0))

        # Composite onto background
        frame_rgb = bg_canvas.copy()
        char_bgr = current_pose[:, :, :3]
        char_alpha = (current_pose[:, :, 3:] / 255.0).astype(np.float32)

        composite = (frame_rgb * (1.0 - char_alpha) + char_bgr * char_alpha).astype(np.uint8)
        proc.stdin.write(composite.tobytes())

        if frame_idx % 150 == 0:
            print(f"  Frame {frame_idx}/{total_frames} ({t:.1f}s)")

    proc.stdin.close()
    proc.wait()
    print("Video generation finished successfully!")
    print(f"Output saved to: {out_video}")

if __name__ == '__main__':
    main()
