import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.deepmind.com/blog"
response = requests.get(URL)

if response.status_code != 200:
    print(f"Failed to fetch page: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Try to find all paragraph tags
paragraphs = soup.find_all("p")

if not paragraphs:
    print("No <p> tags found. This page might be JavaScript-rendered.")
    exit()

text = "\n".join(p.get_text().strip() for p in paragraphs if p.get_text().strip())

# Make sure docs/ exists
os.makedirs("docs", exist_ok=True)

with open("docs/deepmind_blog.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Successfully scraped and saved to docs/deepmind_blog.txt")
