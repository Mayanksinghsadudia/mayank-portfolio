import urllib.request
import json

username = "Mayanksinghsadudia"
url = f"https://api.github.com/users/{username}/repos?per_page=100"

req = urllib.request.Request(url)
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
        print(f"Found {len(repos)} repositories:")
        for r in repos:
            print(f"- {r['name']}: {r.get('description')} | URL: {r['html_url']}")
except Exception as e:
    print("Error fetching repos:", e)
