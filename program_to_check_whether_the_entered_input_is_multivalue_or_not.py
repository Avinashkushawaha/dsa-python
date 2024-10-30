value = eval(input("Enter a value: "))

if isinstance(value, (list, tuple, dict, set)):
    print("The value is a multivalue type.")
else:
    print("The entered input is not multivalue")    