import shutil

src = r"C:\Users\hp\.gemini\antigravity\brain\0ee541b7-eb92-4360-a00f-81a4f6ff7437\ford_mustang_1968_1785955922529.jpg"
dst = r"C:\Users\hp\.gemini\antigravity\scratch\graphic-design-portfolio\assets\user_projects\ford_mustang_1968.jpg"

shutil.copy(src, dst)
print("Successfully copied Ford Mustang 1968 project cover image!")
