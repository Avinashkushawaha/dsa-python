num1 = float(input("Enter first number here : "))
num2 = float(input("Enter another number here : "))

print("press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for division")

choice = int(input("Enter your choice from 1-4: "))

if choice == 1:
    print(num1 + num2)
elif choice == 2:
    print(num1 - num2)
elif choice == 3:
    print(num1 * num2)
elif choice == 4:
    print(num1 / num2)
else:
     print("Invalid output")    
