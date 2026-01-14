"""Logging vs Print (One Line)
print() → talks to user
logging → talks to developer"""

"""import logging

age = -5

if age < 0:
    logging.error("Age cannot be negative")"""


import logging

logging.basicConfig(
    
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logging.info("App started")
logging.error("Something went wrong")


