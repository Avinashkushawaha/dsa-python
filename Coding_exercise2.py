size = input("What size pizza you want (S/M/L)? ")
bill = 0
if size == 'S' or size == 's':
    bill += 100
    print("Small Pizza price is 100 Rs. ")
elif size == 'm' or size == 'm':
    bill += 200
    print("Medium pizza price is 200 Rs.")
else:
    bill += 300
    print("Large pizza price is 300 Rs.")

    add_pepproni = input("Do you want pepperoni(y/n)? ")
    if add_pepproni == 'y' or add_pepproni == 'Y':
        if size == 'S' or size == 's':
            bill += 30
        else:
            bill += 50

extra_cheese = input("Do you want extra cheese(Y/N)? ")
if extra_cheese == 'Y' or extra_cheese == 'Y':
    bill += 20
print(f"Your final bill is {bill}")