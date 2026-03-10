"""friend_ages ={"Rolf":24,"Adam":30,"Alok":60}

friend_ages["bob"] = 20
friend_ages["Rolf"] = 25
print(friend_ages)  # dictionaries do keep the order in which you added keys to them(not add duplicate) 
# in SETS you cant to add duplicate keys in a dicionary


print(friend_ages["Alok"])"""

"""friends = (
    {"name": "Rolf Smith", "Age": 24},
    {"name": "Adam Wool", "Age": 38},
    {"name": "Anne Pun", "Age": 27}
)

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])"""


#convert tupples to dictionary 
friends = [("Rolf",24),("Adam",30),("Anne",27)]
friends_ages = dict(friends)
print(friends_ages)

