import os
import string

def get_drives():
    drives = []
    for letter in string.ascii_uppercase:
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives

print("Available drives:", get_drives())

found_folders = []

for drive in get_drives():
    print(f"Scanning {drive}...")
    try:
        for root, dirs, files in os.walk(drive):
            # Exclude system folders
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['Windows', 'Program Files', 'Program Files (x86)', 'AppData', '$Recycle.Bin', 'System Volume Information']]
            
            root_lower = root.lower()
            if 'graphic' in root_lower or 'project' in root_lower or 'design' in root_lower:
                image_files = [f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png', '.pdf', '.psd', '.ai', '.cdr', '.eps'))]
                if len(image_files) > 0:
                    found_folders.append((root, image_files))
                    print(f"Found match: {root} ({len(image_files)} image/design files)")
                    for f in image_files[:10]:
                        print(f"   - {f}")
    except Exception as e:
        print(f"Error scanning {drive}: {e}")

print("\n=== SUMMARY OF DESIGN FOLDERS FOUND ===")
for folder, files in found_folders:
    print(f"\nFolder: {folder}")
    for f in files:
        print(f"  * {f}")
