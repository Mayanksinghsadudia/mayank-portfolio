"""
Higgsfield Video Integration Script
Integrates Higgsfield-generated 3D character video into Mayank's portfolio.
"""

import os
import sys
import subprocess
import json
import re
import urllib.request
import imageio_ffmpeg

def main():
    print("=== Higgsfield Video Integration Pipeline ===")
    
    input_source = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Candidate search paths (supports Roor.ai, Seedance 2.5, and Higgsfield)
    candidate_paths = [
        r"C:\Users\hp\Documents\Codex\2026-10-07\https-www-instagram-com-p-deixis4avpj\outputs\higgsfield_video.mp4",
        r"C:\Users\hp\Downloads\roor_seedance.mp4",
        r"C:\Users\hp\Downloads\seedance_video.mp4",
        r"C:\Users\hp\Downloads\hf_mult_motion_control.mp4",
        r"assets\mayank_higgsfield_intro.mp4"
    ]
    
    # Auto-detect newest MP4 in Downloads if from Roor.ai or Seedance
    downloads_dir = r"C:\Users\hp\Downloads"
    if os.path.exists(downloads_dir):
        recent_mp4s = [
            os.path.join(downloads_dir, f) for f in os.listdir(downloads_dir)
            if f.lower().endswith(".mp4") and ("roor" in f.lower() or "seedance" in f.lower() or "byteplus" in f.lower() or "higgs" in f.lower())
        ]
        if recent_mp4s:
            recent_mp4s.sort(key=os.path.getmtime, reverse=True)
            candidate_paths.insert(0, recent_mp4s[0])
    
    target_input = None
    if input_source:
        if input_source.startswith("http://") or input_source.startswith("https://"):
            print(f"Downloading video from URL: {input_source}")
            target_input = "assets/downloaded_presenter.mp4"
            urllib.request.urlretrieve(input_source, target_input)
            print("Download completed.")
        elif os.path.exists(input_source):
            target_input = input_source
    else:
        for p in candidate_paths:
            if os.path.exists(p):
                target_input = p
                break
                
    if not target_input:
        print("Status: Waiting for Roor.ai / Seedance 2.5 or Higgsfield video file/URL.")
        print("Usage: python integrate_higgsfield_video.py <video_file_or_url>")
        print("Tip: You can also simply download the generated video from Roor.ai to your Downloads folder and run this script.")
        return False

    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
    out_video = "assets/mayank_higgsfield_intro.mp4"
    audio_src = r"assets\mayank_intro_30s.mp3"
    if not os.path.exists(audio_src):
        audio_src = r"assets\temp_audio.wav"

    # 1. Inspect Input Video streams
    probe_cmd = [ffmpeg, '-i', target_input]
    probe_proc = subprocess.run(probe_cmd, stderr=subprocess.PIPE, text=True)
    probe_out = probe_proc.stderr

    has_audio = "Audio:" in probe_out
    is_landscape = False
    
    # Check resolution
    res_match = re.search(r'Stream.*Video.* (\d{3,4})x(\d{3,4})', probe_out)
    if res_match:
        w, h = int(res_match.group(1)), int(res_match.group(2))
        print(f"Detected video resolution: {w}x{h}")
        if w > h:
            is_landscape = True

    print(f"Input video: has_audio={has_audio}, is_landscape={is_landscape}")

    # 2. Transcode / Mux audio if needed
    if not has_audio and os.path.exists(audio_src):
        print(f"Adding synchronized audio track from {audio_src}...")
        mux_cmd = [
            ffmpeg, '-y',
            '-i', target_input,
            '-i', audio_src,
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-shortest',
            '-movflags', '+faststart',
            out_video
        ]
    else:
        print("Encoding clean web-compatible MP4 with faststart...")
        mux_cmd = [
            ffmpeg, '-y',
            '-i', target_input,
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-movflags', '+faststart',
            out_video
        ]

    proc = subprocess.run(mux_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        print("Error during video processing:", proc.stderr.decode('utf-8', errors='ignore'))
        return False

    print(f"Processed video saved to {out_video} (size: {os.path.getsize(out_video)} bytes)")

    # 3. Update presenter-config.js
    config_path = "presenter-config.js"
    scene_video = is_landscape
    chroma_key = False
    
    config_content = f"""window.MAYANK_PRESENTER = {{
  "videoSrc": "{out_video}",
  "sceneVideo": {str(scene_video).lower()},
  "autoplay": true,
  "chromaKey": {str(chroma_key).lower()},
  "duration": 30,
  "intro": "Hi, I'm Mayank Singh Sadudia, a data analyst and graphic designer based in Indore. I use Python, SQL, Excel, and Power BI to turn data into clear insights. I also create brand identities, packaging, and engaging visuals. My portfolio brings analytical thinking and creative design together. Explore my projects, visit my GitHub, and get in touch. I'd love to collaborate."
}};
"""
    with open(config_path, "w", encoding="utf-8") as f:
        f.write(config_content)
    print("Updated presenter-config.js successfully.")

    # 4. Update index.html cache-buster
    html_path = "index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    new_html = re.sub(r'(\?v=)[^"\'\s>]+', r'\g<1>higgsfield-20261008', html)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated index.html cache busters to higgsfield-20261008.")

    # 5. Git Commit and Push
    print("Committing and pushing to GitHub...")
    subprocess.run(["git", "add", out_video, config_path, html_path], check=True)
    subprocess.run(["git", "commit", "-m", "Integrate Higgsfield AI 3D presenter video into portfolio"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
    print("Pushed changes to GitHub origin/main successfully!")
    return True

if __name__ == "__main__":
    main()
