cars = ["ok", "ok","ok", "faulty", "ok","ok"]

all_successful = True

for status in cars:
    if status == "faulty":
     print("Stopping the production line!")
     all_successful = True
     break
    print(f"This car is {status}.")
    #print("Shippint new car to customer")

    if all_successful:
       print("all cars built successfully. No faulty cars!")
    else:
       print("All cars not built successfully. No faulty cars!")
