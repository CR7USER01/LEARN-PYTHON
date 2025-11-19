
"""def add(x,y):
    total = x + y
    return total

print(add(5,10))
print(add(6,7))
print(add(5,4))"""

#print(1, 2, 3, 4, 5, sep=" - ")

default_y = 3

def add(x, y = default_y):# stores default value at the tme . not change later
        total = x + y
        print(total)

add(2)

default_y = 4  # here the default value is not changed because it declare before in finction(def add)
add(2) # be careful while using list and dictionary 



