"""def greet():
    print("Hello")

hello =  greet

hello()"""


"""def average(seq):
    return sum(seq) / len(seq)

avg = lambda seq: sum(seq) / len(seq)"""

avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

operation = {
    "average": avg,
    "total":total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"student: {name}")
    operations= input("Enter 'average', 'total', or 'top': ")

    """if operation == "average":
        print(avg(grades))
    
    elif operation == "total":
        print(avg(grades))
        
    elif operation == "top":
        print(top(grades))"""
    
    operation_function = operations[operation]
    print(operation_function(grades))