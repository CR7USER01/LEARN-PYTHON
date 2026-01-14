"""logging.info() ℹ️
Normal information about program flow
Used when:
Program starts
User logs in
File saved successfully"""

import logging
logging.basicConfig(level=logging.INFO)

logging.info("Program started")



"""logging.debug() 🐞
Very detailed messages for developers
Used when:
You are learning
You are fixing a bug
You want to see every small step"""

import logging
logging.basicConfig(level=logging.DEBUG)

x = 10
logging.debug("Value of x is 10")
