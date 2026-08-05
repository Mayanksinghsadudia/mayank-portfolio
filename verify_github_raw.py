import urllib.request

raw_url = "https://raw.githubusercontent.com/Mayanksinghsadudia/mayank-portfolio/main/index.html"

with urllib.request.urlopen(raw_url) as resp:
    html = resp.read().decode('utf-8')
    if 'id="phone"' in html or 'name="phone"' in html:
        print("CONFIRMED! Phone field is present in index.html on GitHub main branch!")
    else:
        print("Phone field not found in GitHub raw index.html")
