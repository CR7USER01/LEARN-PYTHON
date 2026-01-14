#counter 

"""Counter → Counting items
Real life

You count fruits in a bag 🍎🍌🍎🍎

You say:
Apple = 3
Banana = 1
"""
from collections import Counter
fruits = ["apple", "banana", "apple", "apple"]
print(Counter(fruits))
"""Output
{'apple': 3, 'banana': 1}"""
#------------------------------------------
#defaultdict

"""2️⃣ defaultdict → Box that auto-creates itself
Real life

You have boxes 📦 labeled by name.

If box does not exist, normal dictionary says:
❌ “No box found!”

defaultdict says:
✅ “Okay, I’ll make a new empty box for you.”
"""
from collections import defaultdict
d = defaultdict(list)
d["math"].append(90)
print(d)

#Output
#{'math': [90]}

"""Meaning
defaultdict = dictionary that never says “key not found”"""

#-------------------------------------------------------
#OrderedDict
"""3️⃣ OrderedDict → Dictionary with memory
Real life

You write tasks in a notebook 📒 in order:

Wake up
Study
Sleep
Order matters."""

from collections import OrderedDict

tasks = OrderedDict()
tasks["wake"] = 1
tasks["study"] = 2
tasks["sleep"] = 3

print(tasks)

#Meaning

"""👉 OrderedDict = remembers order you added items

(Today, normal dict also does this, so this is less important now.)"""

#----------------------------------------------------------------
#namedtuple

"""4️⃣ namedtuple → Tuple with labels
Normal tuple (confusing)
student = ("JITU", 21)
print(student[0])


❓ What is student[0]? Name or age?

namedtuple (clear)"""

from collections import namedtuple
Student = namedtuple("Student", ["name", "age"])
s = Student("JITU", 21)
print(s.name)
print(s.age)

#Meaning
"""👉 namedtuple = tuple but with names"""

#--------------------------------------------------

"""deque → Queue (line) from both sides
Real life

People standing in a line 🚶🚶🚶
Someone can:

Join from front
Join from back
Leave from front
Leave from back

"""
from collections import deque

line = deque(["A", "B", "C"])
line.append("D")      # join back
line.appendleft("Z") # join front

print(line)

"""Output
['Z', 'A', 'B', 'C', 'D']"""

#Meaning
#👉 deque = super fast queue
