num = input("Enter a number: ")

if len(num) == 4 and num.isdigit():
    print(f"{num} is a 4-digit number.")
else:
    print(f"{num} is not a 4-digit number.")    