"""Argument unpacking in Python (very easy explanation)
Argument unpacking means:
Sending multiple values to a function using a single variable.
Python uses * and ** for this."""

"""def multiply(a, b):
    print(a * b)
nums = [4, 5]
multiply(*nums)
What Python does:
python
Copy code      
multiply(4, 5)
Output:
Copy code
20

Why?
Function needs 2 values
You gave 1 list"""

"""✅ Example 2: Using ** with a dictionary
def student(name, course):
    print(name, course)
data = {"name": "Jitu", "course": "Python"}
student(**data)
What Python does:
student(name="Jitu", course="Python")
Output:
Jitu Python

Why?
Function needs separate values
You passed one dictionary"""

