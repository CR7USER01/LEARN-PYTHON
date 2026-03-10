# example 
import requests
from bs4 import BeautifulSoup

# 1. Page
url = "https://example.com"
response = requests.get(url)

# 2. Parser
soup = BeautifulSoup(response.text, "html.parser")

# 3. Locator
title = soup.find("h1")

print(title.text)
