
import cv2
import os

v1 = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video1.mp4"
v2 = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2.mp4"

p1 = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video1_poster.jpg"
p2 = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/video2_poster.jpg"

def extract_poster(video_path, poster_path):
    cap = cv2.VideoCapture(video_path)
    # Read frame 10 for representative poster
    cap.set(cv2.CAP_PROP_POS_FRAMES, 10)
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    if ret:
        cv2.imwrite(poster_path, frame)
        print(f"Extracted poster successfully: {poster_path}")
    else:
        print(f"Failed to extract frame from {video_path}")
    cap.release()

extract_poster(v1, p1)
extract_poster(v2, p2)
