import os

search_terms = ['project', 'graphic', 'design']

found_dirs = []

for root_dir in ['C:\\Users\\hp', 'C:\\']:
    try:
        for root, dirs, files in os.walk(root_dir):
            # Don't recurse into system / temp / AppData / node_modules
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['AppData', 'Windows', 'Program Files', 'Program Files (x86)', 'node_modules', '$Recycle.Bin']]
            
            root_lower = root.lower()
            if 'projects graphic design' in root_lower or ('graphic' in root_lower and 'design' in root_lower) or 'projects' in root_lower:
                found_dirs.append(root)
                print("FOUND:", root)
                if len(files) > 0:
                    print("  Files:", files[:5])
    except Exception as e:
        pass

print("\n--- Search Summary ---")
for d in found_dirs[:20]:
    print(d)
