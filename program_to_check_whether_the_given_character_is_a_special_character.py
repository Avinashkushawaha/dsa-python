char = input("Enter a character: ")

if not char.isalnum():
    print(f"{char} is a special character.")
else:
    print(f"{char} is not a special character.")    