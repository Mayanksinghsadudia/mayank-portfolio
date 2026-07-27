import os
import shutil

src_dir = r'D:\PROJECTS GRAPHIC DESGIN'
dest_dir = r'C:\Users\hp\.gemini\antigravity\scratch\graphic-design-portfolio\assets\user_projects'

os.makedirs(dest_dir, exist_ok=True)

copied_files = []
for file_name in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file_name)
    if os.path.isfile(src_file) and file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.mp4', '.pdf')):
        # Clean file name for web URL
        clean_name = file_name.strip().replace(' ', '_').lower()
        dest_file = os.path.join(dest_dir, clean_name)
        shutil.copy2(src_file, dest_file)
        copied_files.append((file_name, clean_name, os.path.getsize(dest_file)))

print(f"Successfully copied {len(copied_files)} files from {src_dir}:")
for orig, clean, sz in copied_files:
    print(f" - {orig} -> {clean} ({sz} bytes)")
