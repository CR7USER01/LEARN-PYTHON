friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

dict(zip(friends, time_since_seen))

   #= [("Rolf", 3), ("Bob", 7), ("Jen" , 15), ("Anne", 11)]

long_timers = list(zip(friends, time_since_seen, [1, 2, 3, 4, 5]))
    
#long_timers = dict(zip(friends, time_since_seen))
print(long_timers)