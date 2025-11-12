"""ages = [22, 35, 27, 21, 20]
odds = [age for age in ages if age % 2 == 1]
print(odds)"""

friends = ["Rolf","ruth", "charlie", "michael"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = set([f.lower() for f in friends])
#guests_lower  = set([g.lower() for g in guests])

present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
]

print(present_friends)


#___________________________________________

riends = ["Rolf","ruth", "charlie", "michael"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

present_friends = [
    name.title()
    for name in guests 
    if name.lower() in [f.lower()for f in friends]
]
print(present_friends)


