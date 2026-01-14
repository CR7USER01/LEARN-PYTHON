"""In Python, mutability refers to whether or not an object’s value can be changed after it is created.

Step 1: Think of objects like boxes
Some boxes are changeable: you can put something new inside anytime.
Some boxes are fixed: once you put something inside, you can’t change it—you can only replace the whole box."""

#Python objects are like these boxes
#1. Mutable (changeable box)
"""You can change the content without making a new box.
Example: a list"""

my_list = [1, 2, 3]  # box with 3 numbers
my_list[0] = 10      # change first number
print(my_list)       # Output: [10, 2, 3]

#Immutable (fixed box)
"""You cannot change the content inside.
Example: a string"""

my_str = "hello"
my_str[0] = "H"      # ❌ ERROR: cannot change inside
my_new_str = "Hello" # ✅ You created a new box