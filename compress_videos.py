import subprocess

py313 = r'C:\Users\hp\AppData\Local\Programs\Python\Python313\python.exe'

script = '''
import cv2
import os

v2_in = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2.mp4"
v2_out = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2_opt.mp4"

cap = cv2.VideoCapture(v2_in)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2 * 2
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2 * 2

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(v2_out, fourcc, fps, (w, h))

count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Resize to max 720p height if larger
    if h > 720:
        new_h = 720
        new_w = int(w * (720 / h)) // 2 * 2
        frame = cv2.resize(frame, (new_w, new_h))
    out.write(frame)
    count += 1

cap.release()
out.release()

if os.path.exists(v2_out) and os.path.getsize(v2_out) > 0:
    os.replace(v2_out, v2_in)
    print("Video 2 successfully compressed! New size:", os.path.getsize(v2_in))
'''

with open('compress_videos_script.py', 'w', encoding='utf-8') as f:
    f.write(script)

res = subprocess.run([py313, 'compress_videos_script.py'], capture_output=True, text=True)
print("Compression Output:", res.stdout)
print("Compression Error:", res.stderr)
