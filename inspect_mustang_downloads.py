import os, shutil

img1 = r"C:\Users\hp\Downloads\mcar.jpg"
img2 = r"C:\Users\hp\Downloads\car 2.jpg"
target = r"C:\Users\hp\.gemini\antigravity\scratch\graphic-design-portfolio\assets\user_projects\ford_mustang_1968.jpg"

if os.path.exists(img1):
    shutil.copy(img1, target)
    print("Copied mcar.jpg to ford_mustang_1968.jpg! Size:", os.path.getsize(target))
elif os.path.exists(img2):
    shutil.copy(img2, target)
    print("Copied car 2.jpg to ford_mustang_1968.jpg! Size:", os.path.getsize(target))
