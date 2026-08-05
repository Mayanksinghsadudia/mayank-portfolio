import os

search_dirs = [
    r"D:\PROJECTS GRAPHIC DESGIN",
    r"C:\Users\hp\Downloads",
    r"C:\Users\hp\Desktop",
    r"C:\Users\hp\Pictures"
]

for d in search_dirs:
    if os.path.exists(d):
        print(f"Searching in {d}...")
        for root, dirs, files in os.walk(d):
            for f in files:
                if any(k in f.lower() for k in ["mustang", "ford", "1968", "fastback", "car"]):
                    print(f"Found: {os.path.join(root, f)}")
