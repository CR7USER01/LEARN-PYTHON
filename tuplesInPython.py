"""short_tuple ="rolf","bob"
a_bit_clearer = ("rolf","bob")
tuple_in_list = [("rolf","bob")]
not_a_tuple = "rolf","""

friends = ("rolf","bob","Anne")
#friends.append("jen")#you cant insert an element inside a tupple 
friends = friends + ("jen",)
print(friends)

#in list you can add or insert element but in tupple you cant 
#tupples are useful when you wanna keep them unchanged 