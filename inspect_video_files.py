import os, sys

v1_path = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video1.mp4'
v2_path = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2.mp4'

print("Video 1 Size:", os.path.getsize(v1_path) if os.path.exists(v1_path) else "Not found")
print("Video 2 Size:", os.path.getsize(v2_path) if os.path.exists(v2_path) else "Not found")

# Read header atoms of MP4
with open(v1_path, 'rb') as f:
    header1 = f.read(100)
    print("Video 1 Header:", header1[:30])

with open(v2_path, 'rb') as f:
    header2 = f.read(100)
    print("Video 2 Header:", header2[:30])
