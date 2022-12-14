"""
Written by Benjamin Jack Cullen aka Holographic_Sol
"""
import os
import time
import requests
import subprocess
from bs4 import BeautifulSoup

# configure BeautifulSoup
url = ('http://library.lol/main/D4A63DD965AF51889F9954F8EFD9B24C')
print('-source:', url)
rHead = requests.get(url)
data = rHead.text
soup = BeautifulSoup(data, "html.parser")

# Example: Get Links
print('-- crawling for links')
for link in soup.find_all('a'):
    href = (link.get('href'))
    print(href)

# Example: Get Text
print('-- crawling for text')
for row in soup.find_all('p'):
    text = row.get_text()
    # text = re.sub(r'\[.*?\]', '', text)
    print(text)
