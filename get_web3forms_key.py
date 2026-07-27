import urllib.request
import urllib.parse
import json

# Request a free Web3Forms access key for mayanksadudia@gmail.com
url = "https://api.web3forms.com/submit"
# Web3Forms public key creation endpoint
data = urllib.parse.urlencode({
    'email': 'mayanksadudia@gmail.com'
}).encode('utf-8')

try:
    req = urllib.request.Request("https://api.web3forms.com/create", data=data, method='POST')
    with urllib.request.urlopen(req) as resp:
        res = json.loads(resp.read().decode('utf-8'))
        print("Web3Forms Key Response:", res)
except Exception as e:
    print("Error getting key:", e)
