num = input("Enter a number: ")

if len(num) == 1 and num.isdigit():
    print(f"{num} is a single-digit number.")
else:
    print(f"{num} is not a single-digit number.")

