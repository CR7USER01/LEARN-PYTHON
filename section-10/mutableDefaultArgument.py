"""Mutable default argument (very simple explanation)
A mutable default argument means:
Using a changeable object (like a list or dictionary) as a default value for a function parameter.
This can cause unexpected behavior."""

def add(x, box=[]):
    box.append(x)
    return box

print(add(1))
print(add(2))
print(add(3))
