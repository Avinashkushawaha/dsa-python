
height = int(input("What is your height (in feet)? "))
bill = 0

if height >= 3:
    print("You can ride.")
    
    age = int(input("What is your age? "))
    if age < 12:
        bill = 150
        print("Ticket Price is 150 Rs.")
    elif age <= 18:
        bill = 250
        print("Ticket Price is 250 Rs.")
    else:
        bill = 500
        print("Ticket Price is 500 Rs.")
    
    want_photo = input("Do you want to take a photo (y/n)? ")
    if want_photo == 'y' or want_photo == 'Y': 
        bill += 50  

    print(f"Your total bill is {bill} Rs.")
else:
    print("You can't ride.")
    print("Thank you.. Enjoy the ride !")
