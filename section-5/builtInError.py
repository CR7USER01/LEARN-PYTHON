 #  INDEX ERROR
#IndexError = you are trying to access an item outside the available range.

"""a = [10, 20, 30]
print(a[5])

List has items only at positions: 0, 1, 2
You are trying to access position 5 (which does not exist)"""

#---------------------------------------------------

# KEY ERROR
#KeyError = You asked the dictionary for a key that it doesn’t have.

"""data = {"name": "Jitu", "age": 20}
print(data["city"])

There is no key named "city" in the dictionary."""

#-------------------------------------------------

#NAME ERROR
#NameError = The name you are trying to use has not been created.

"""print(x)
❌ Error because x was never created.

pgsql
Copy code
NameError: name 'x' is not defined

Variable defined later
print(a)
a = 10

"""

#-------------------------------------------------
#ATTRIBUTE ERROR
#AttributeError happens when you try to use a function / method / attribute
# that does NOT exist for that object.

"""Wrong method on a string
name = "Jitu"
name.push()   # ❌ strings do NOT have push()
Error:

Wrong method on a list
numbers = [1, 2, 3]
numbers.upper()  # ❌ lists do NOT have upper()"""

#________________________________________________________

#NOT IMPLEMENTED ERROR

#NotImplementedError is an error you raise in a parent class to force the child class to implement a method.
"""Think like this:

You have a parent class called Animal.
Every animal must have a sound().
But the parent class does not know what sound a Dog or Cat makes.

So the parent class says:

👉 “I don’t know the sound.
👉 Children (Dog, Cat, Cow) must write their own sound.”

To make sure children write their own sound, Python gives you:

⭐ NotImplementedError

It means:

👉 “This function is not written here.

👉 You MUST write it in the child class.”"""



#_________________________________________________________________

 
#RUNTINE ERROR

"""A runtime error is an error that happens while your program is running.

Your code is correct in writing (no syntax error),
but when Python tries to run it, something goes wrong.


a = 10
b = 0
print(a / b)

Code is written correctly
👉 BUT you can’t divide by 0, so Python stops while running"""


#_________________________________________________________________

#SYNTAX ERROR

 #A syntax error happens when you write Python code in the wrong format, so Python cannot even start the program.

 #_____________________________________________________________

# IDENTATION ERROR

"""An Indentation Error happens when your code is not properly aligned.

Super Easy Example (Wrong indentation)
def hello():
print("Hello")


Correct version
def hello():
    print("Hello")"""

#___________________________________________________________

#TAB ERROR

"""What is a Tab Error?

A TabError happens when you mix:

Tabs (⇥ key)
Spaces (space bar)
in the same block of code while indenting.
Python wants either only spaces OR only tabs, not both.

Example of TabError
def hello():
    print("Hello")   # 4 spaces
	print("Hi")      # tab"""

#__________________________________________________________

#VALUE ERROR

"""A ValueError happens when:

The data type is correct
But the value is not acceptable

Example:
You ask Python to convert "abc" into a number — it cannot.

Example 1 — Converting wrong string to int
int("hello")

Example 2 — Wrong value for math operations
import math
math.sqrt(-1)

Example 3 — Wrong value for list remove()
nums = [1, 2, 3]
nums.remove(5)"""

#___________________________________________________________

#TYPE ERROR

#A TypeError happens when you use a value with the wrong data type for an operation.

#____________________________________________________________________

#IMPORT ERROR

"""IMPORT ERROR (ImportError) — Easy Explanation

ImportError occurs when Python cannot find the module or object you are trying to import.

Module is not installed
import numpy  # if numpy is not installed → ImportError

2. Module name is spelled incorrectly
import numppy  # wrong spelling → ImportError

3. File path or package structure is wrong
from mypackage import tools  # if tools.py doesn’t exist → ImportError

4. Importing a function/class that does not exist
from math import squareroot  # no function named squareroot."""

#_________________________________________________________________-

#DEPRECATION WARNING

"""DEPRECATION WARNING — Easy Explanation

A DeprecationWarning means:

👉 “This feature still works now, but it will be removed or changed in the future.”
👉 Python is warning you to update your code before it stops working."""


