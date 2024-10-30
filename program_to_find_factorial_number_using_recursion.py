def fact(n):
    if n == 1:
        return 1
    
    else:
        return n * fact(n-1)
n = int(input("Enter a number here :"))
if n <= 0:
    print("factorial of number less than 1 does not exits")
else:
    print("Factorial of", n, "is", fact(n))