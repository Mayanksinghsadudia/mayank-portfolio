import urllib.request
import urllib.parse
import json

url = "https://formsubmit.co/ajax/mayanksadudia@gmail.com"

data = urllib.parse.urlencode({
    'name': 'Portfolio Test Visitor',
    'email': 'mayanksadudia@gmail.com',
    'project_type': 'Brand Identity & Visuals',
    'message': 'Testing FormSubmit automatic email delivery to Mayank Singh Sadudia inbox.',
    '_subject': 'New Portfolio Inquiry from Test Visitor'
}).encode('utf-8')

req = urllib.request.Request(url, data=data, method='POST')
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
req.add_header('User-Agent', 'Mozilla/5.0')

try:
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("FormSubmit Response:", res)
except Exception as e:
    print("FormSubmit Error:", e)
