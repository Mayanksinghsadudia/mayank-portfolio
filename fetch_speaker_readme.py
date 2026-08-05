import urllib.request
import json

url = "https://raw.githubusercontent.com/Mayanksinghsadudia/reva-3d-speaker-website/main/README.md"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp:
        print("Speaker Readme:\n", resp.read().decode('utf-8')[:500])
except Exception as e:
    print("Error fetching readme:", e)
