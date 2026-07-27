import os
import shutil
import subprocess

repo_path = r"C:/Users/hp/.gemini/antigravity/scratch/graphic-design-portfolio"
git_dir = os.path.join(repo_path, ".git")

# Delete old .git directory to strip all history
if os.path.exists(git_dir):
    try:
        shutil.rmtree(git_dir)
        print("Successfully removed old .git directory!")
    except Exception as e:
        print("Error removing .git:", e)

token = "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"
remote_url = f"https://{token}@github.com/Mayanksinghsadudia/mayank-portfolio.git"

commands = [
    ["git", "init"],
    ["git", "config", "user.name", "Mayank Singh Sadudia"],
    ["git", "config", "user.email", "mayanksadudia@gmail.com"],
    ["git", "checkout", "-b", "main"],
    ["git", "add", "."],
    ["git", "commit", "-m", "Initial commit of Mayank Singh Sadudia Portfolio"],
    ["git", "remote", "add", "origin", remote_url],
    ["git", "push", "-u", "origin", "main", "--force"]
]

for cmd in commands:
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, cwd=repo_path, capture_output=True, text=True)
    print("STDOUT:", res.stdout)
    if res.stderr:
        print("STDERR:", res.stderr)
    if res.returncode != 0 and "push" in cmd:
        print("Push Failed!")
