num = int(input("Enter an integer: "))

if num % 2 == 0 and num % 5== 0:
    print(f"{num} is even and a multiple of 5.")
else:
    print(f"{num} is not even or not a multiple of 5.")
