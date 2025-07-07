import requests
import os

url = f"https://api.github.com/users/b1gn0se/repos?per_page=100&type=all"
repos = requests.get(url).json()

for repo in repos:
    os.system(f"git clone {repo['clone_url']}")
