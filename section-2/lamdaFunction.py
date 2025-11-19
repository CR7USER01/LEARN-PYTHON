"""def divide(x,y):
    return x/y"""


"""divide = lambda x,y: x/y
print(divide(8,9))
print(divide(12,4))"""

#  print((lambda x, y: x / y)(15, 3))#lambda function provide more simlicity to code


average = lambda sequence: sum(sequence) / len(sequence) # type: ignore


students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))


