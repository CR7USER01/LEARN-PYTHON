"""currencies = 0.8, 1.2
usd, eur = currencies"""

friends = [("Rolf", 25),("Anne",37),("Charlie",31),("Bob",22)]

#case 1
for name, age in friends:
    print(f"{name} is {age} years old.")#destructuring in for loop

#case 2
for friend in friends:
    name, age = friend 
    print(f"{name} is {age} years old.")

