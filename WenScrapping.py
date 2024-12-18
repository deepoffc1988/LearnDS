import requests
from bs4 import BeautifulSoup

# Send a GET request to the website
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract data from the HTML
title = soup.find('h1').text
paragraphs = soup.find_all('p')

# Print the extracted data
print("Title:", title)
for p in paragraphs:
    print(p.text)