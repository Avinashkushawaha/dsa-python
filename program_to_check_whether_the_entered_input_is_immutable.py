value = eval(input("Enter a value: "))

if isinstance(value,(int, float, str, tuple)):
    print("The entered input is immutable.")
else:
    print("The entered input is mutable.")    