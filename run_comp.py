
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
