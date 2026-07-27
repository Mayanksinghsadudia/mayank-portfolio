import urllib.request
import urllib.parse
import re

url = "http://localhost:8085"

# 1. Fetch index.html to verify contact form structure
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8')

form_match = re.search(r'<form id="contact-form"[^>]*>(.*?)</form>', html, re.DOTALL)

print("=== CONTACT FORM VERIFICATION ===")
if form_match:
    form_html = form_match.group(0)
    print("Form Tag Found!")
    print("Netlify Attribute Present:", 'data-netlify="true"' in form_html)
    print("Form Name:", 'name="contact"' in form_html)
    print("Hidden Form Name Field:", 'name="form-name"' in form_html)
    print("Name Field:", 'name="name"' in form_html)
    print("Email Field:", 'name="email"' in form_html)
    print("Project Type Field:", 'name="project-type"' in form_html)
    print("Message Field:", 'name="message"' in form_html)
else:
    print("ERROR: Contact form not found in index.html")

# 2. Test sending POST request to contact form
data = urllib.parse.urlencode({
    'form-name': 'contact',
    'name': 'Test Client',
    'email': 'testclient@example.com',
    'project-type': 'branding',
    'message': 'Hello Mayank, testing your portfolio contact form.'
}).encode('utf-8')

post_req = urllib.request.Request(url, data=data, method='POST')
post_req.add_header('Content-Type', 'application/x-www-form-urlencoded')

try:
    with urllib.request.urlopen(post_req) as post_resp:
        print("\n=== HTTP POST TEST RESULT ===")
        print("HTTP Status Code:", post_resp.status)
        print("Form Submission Test Passed!")
except Exception as e:
    print("\nHTTP POST Response:", e)
