#A regular expression (regex) in Python is a pattern used to find, match, or replace text inside a string.

"""Simple idea first 
If a normal search is like:
“Find the word cat”
A regular expression is like:
“Find any word that starts with c and ends with t”"""
#-------------------------
"""Why use Regular Expressions?
You use regex to:

🔍 Search text
✂️ Replace text
✅ Validate input (email, phone number, password)
📄 Extract data from text"""
#----------------------------
import re

text = "My age is 25 and my brother is 30"
numbers = re.findall(r"\+", text)

print(numbers)
#----------------------------

#Important Regex Symbols (Very Easy)

""" Symbol         	Meaning	           Example
    \d	          digit (0–9)	         \d
    \w	          letter or number	     \w
    \s	             space	             \s
    .	          any character	         .
    +	          one or more	        \d+
    *	          zero or more	         a*
    ^	          start of string	    ^Hi
    $	          end of string         end$  """

import re

text = "Hello world"

if re.search(r"world$", text):
    print("Ends with world")
else:
    print("Does not end with world")
