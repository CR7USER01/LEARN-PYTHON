#Why Do We Need to Pause?

"""Because modern websites are dynamic.

When you open a website:
HTML loads first
Then CSS loads
Then JavaScript runs
Then data loads from server (API calls)
This takes time ⏳  """


#What Happens Without Wait?

"""Example:

driver.get("some website")
driver.find_element(By.ID, "login")

If the login button appears after 3 seconds,

But Selenium tries in 1 second ❌

Result:

NoSuchElementException


    """
    
"""Important Concept

Selenium is fast ⚡
Websites are slower 🐢

So Selenium must wait for website"""    