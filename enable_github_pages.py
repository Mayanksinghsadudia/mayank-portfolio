import urllib.request
import urllib.parse
import json

token = "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"
repo_owner = "Mayanksinghsadudia"
repo_name = "mayank-portfolio"

url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pages"

payload = json.dumps({
    "source": {
        "branch": "main",
        "path": "/"
    }
}).encode('utf-8')

req = urllib.request.Request(url, data=payload, method='POST')
req.add_header('Authorization', f'Bearer {token}')
req.add_header('Accept', 'application/vnd.github+json')
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("GitHub Pages Enabled Successfully:", res.get('html_url'))
except Exception as e:
    print("GitHub API Response:", e)
