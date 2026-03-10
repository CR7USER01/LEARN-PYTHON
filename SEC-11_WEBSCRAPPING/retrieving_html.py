import os
import requests

url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"

r = requests.get(url)
print(r.text)

with open("fiction.html", "w", encoding="utf-8") as f:
    f.write(r.text)
    
   
   