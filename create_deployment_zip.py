import os
import zipfile

folder_path = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio'
zip_path = 'C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/Mayank_Portfolio_Deploy.zip'

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.zip') or file.endswith('.py') or file.endswith('.log'):
                continue
            abs_path = os.path.join(root, file)
            rel_path = os.path.relpath(abs_path, folder_path)
            zipf.write(abs_path, rel_path)

print(f"Deployment ZIP package created successfully at: {zip_path}")
