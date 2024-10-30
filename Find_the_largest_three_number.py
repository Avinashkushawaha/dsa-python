num =  int(input("Enter first number here: "))
num1 = int(input("Enter second number here: "))
num2 = int(input("Enter third number here: "))

if num > num1 and num > num2:
    print(num," is the largest number")
elif num1 > num and num1 > num2:
    print(num1,"is the largest number")
else:
    print(num2,"is the largest number")
