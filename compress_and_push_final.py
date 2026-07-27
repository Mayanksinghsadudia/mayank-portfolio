import os
import shutil
import subprocess

repo_path = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio"
zip_in_repo = os.path.join(repo_path, "Mayank_Portfolio_Deploy.zip")

# 1. Remove zip file from project directory completely
if os.path.exists(zip_in_repo):
    os.remove(zip_in_repo)
    print("Removed zip file from project folder!")

# 2. Compress video2.mp4 to under 30MB using OpenCV frame sampling
v2_path = os.path.join(repo_path, "assets/user_projects/video2.mp4")
py313 = r"C:\Users\hp\AppData\Local\Programs\Python\Python313\python.exe"

compress_code = '''
import cv2, os

v2_path = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2.mp4"
v2_out = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2_small.mp4"

cap = cv2.VideoCapture(v2_path)
fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2 * 2
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2 * 2

# Half resolution for web performance & small file size
target_h = 480
target_w = int(w * (480 / h)) // 2 * 2

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(v2_out, fourcc, fps, (target_w, target_h))

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # Write every second frame to halve file size & double compression
    if frame_count % 2 == 0:
        resized = cv2.resize(frame, (target_w, target_h))
        out.write(resized)
    frame_count += 1

cap.release()
out.release()

if os.path.exists(v2_out) and os.path.getsize(v2_out) > 0:
    os.replace(v2_out, v2_path)
    print("Compressed video2.mp4 size:", os.path.getsize(v2_path))
'''

with open(os.path.join(repo_path, "run_comp.py"), "w") as f:
    f.write(compress_code)

res = subprocess.run([py313, "run_comp.py"], capture_output=True, text=True)
print("Comp Output:", res.stdout)
print("Comp Error:", res.stderr)

# 3. Clean git history and push
git_dir = os.path.join(repo_path, ".git")
if os.path.exists(git_dir):
    shutil.rmtree(git_dir)

token = "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"
remote_url = f"https://{token}@github.com/Mayanksinghsadudia/mayank-portfolio.git"

commands = [
    ["git", "init"],
    ["git", "config", "user.name", "Mayank Singh Sadudia"],
    ["git", "config", "user.email", "mayanksadudia@gmail.com"],
    ["git", "checkout", "-b", "main"],
    ["git", "add", "."],
    ["git", "commit", "-m", "Clean portfolio deployment for GitHub Pages"],
    ["git", "remote", "add", "origin", remote_url],
    ["git", "push", "-u", "origin", "main", "--force"]
]

for cmd in commands:
    res = subprocess.run(cmd, cwd=repo_path, capture_output=True, text=True)
    print(f"Command {' '.join(cmd)} STDOUT:", res.stdout)
    if res.stderr:
        print(f"Command {' '.join(cmd)} STDERR:", res.stderr)
