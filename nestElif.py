
height = int(input("What is your height (in feet)? "))

if height >= 3:
    print("You can ride.")
    
    # Get the age from the user and determine the ticket price
    age = int(input("What is your age? "))
    
    if age < 12:
        print("Please pay 150 Rs.")
    elif age <= 18:
        print("Please pay 250 Rs.")
    else:
        print("Please pay 500 Rs.")
else:
    print("You can't ride.")
    print("Bye.")
