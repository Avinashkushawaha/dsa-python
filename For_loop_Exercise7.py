# write a program to print the multiplication table of a given number.
number = int(input("Enter a number here: "))

for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")  