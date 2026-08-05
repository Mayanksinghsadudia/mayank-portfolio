import urllib.request
import json

q = "mustang user:Mayanksinghsadudia"
url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(q)}"

req = urllib.request.Request(url)
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print("Mustang Repos Found:", data.get('total_count'))
        for r in data.get('items', []):
            print(f"- {r['name']}: {r['html_url']}")
except Exception as e:
    print("Error:", e)
