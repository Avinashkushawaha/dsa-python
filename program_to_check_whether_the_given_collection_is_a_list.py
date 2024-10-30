collection = eval(input("Enter a collection (e.g.,[1, 2, 3]):"))

if isinstance(collection, list):
    print("The entered collection is a list")
else:
    print("The entered collection is not a list")