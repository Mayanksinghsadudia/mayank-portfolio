import urllib.request
import json

# Search GitHub repositories or user repos for mustang
username = "Mayanksinghsadudia"
url = f"https://api.github.com/users/{username}/repos"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp:
        repos = json.loads(resp.read().decode('utf-8'))
        print("Repos:")
        for r in repos:
            print(r['name'], r['html_url'])
except Exception as e:
    print("Error:", e)
