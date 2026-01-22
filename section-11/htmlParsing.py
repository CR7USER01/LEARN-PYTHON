"""Where parsing is used?
HTML parsing
JSON parsing
XML parsing
Log file parsing
Command-line argument parsing"""
#----------------------------------------------------------------------
#----------------------------------------------------------------------
"""bs4 (Beautiful Soup) acts as an intermediary (bridge)
between Python and HTML
👉 It does NOT run HTML,
it parses and translates HTML into a
form Python can understand"""

#----------------------------------------------------------------------
#----------------------------------------------------------------------
from bs4 import BeautifulSoup

html = "<h1>Hello</h1><p>Learning BeautifulSoup</p>"

soup = BeautifulSoup(html, "html.parser")

print(soup.h1.text)
print(soup.p.text)


""""""



