value = eval(input("Enter a value: "))

if isinstance(value, (int, float, set)) and len(str(value)) == 1:

     print("The entered input is a single value.")
else:
     print("The entered input is not a single value.")     