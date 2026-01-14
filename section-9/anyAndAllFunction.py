"""any() vs all() (VERY IMPORTANT)

Function	   Meaning
any()	     At least one True
all()	     All must be True"""


marks = [55, 70, 40, 90]

# Did **any** student score above 80?
print("Any above 80:", any(m > 80 for m in marks))

# Did **all** students score above 50?
print("All above 50:", all(m > 50 for m in marks))
