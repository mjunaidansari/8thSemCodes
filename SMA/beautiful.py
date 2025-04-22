import requests
from bs4 import BeautifulSoup

url = "https://www.reddit.com/r/socialmedia/"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

posts = soup.find_all('a')  # Post titles are often in <h3>
for post in posts:
    print(post.text)
