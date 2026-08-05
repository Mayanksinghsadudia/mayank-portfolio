import urllib.request
import json

url = "https://api.github.com/repos/Mayanksinghsadudia/reva-3d-speaker-website/contents"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp:
        files = json.loads(resp.read().decode('utf-8'))
        print("Repo files:")
        for f in files:
            print(f"- {f['name']}")
except Exception as e:
    print("Error fetching contents:", e)
