from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "laptop"
file = 0
for i in range(1, 20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=17VBP392IBJPV&sprefix=lapt%2Caps%2C456&ref=nb_sb_noss_2")
    #assert "Amazon" in driver.title
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    #print(elem.get_attribute("outerHTML"))
    print(f"{len(elems)} items found")
    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.txt", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
       # print(elem.text)



    #time.sleep(4)
    driver.close()