import urllib.request

img_url = "https://raw.githubusercontent.com/Mayanksinghsadudia/reva-3d-speaker-website/main/reva_cinematic_speaker.jpg"
target = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio/assets/user_projects/reva_speaker.jpg"

req = urllib.request.Request(img_url)
req.add_header('User-Agent', 'Antigravity-Agent')

try:
    with urllib.request.urlopen(req) as resp, open(target, 'wb') as f:
        f.write(resp.read())
        print("Successfully downloaded reva_cinematic_speaker.jpg!")
except Exception as e:
    print("Error downloading image:", e)
