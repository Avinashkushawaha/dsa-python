char = input("Enter a character: ")

if char.isupper() and char.isalpha():
    print(f"{char} is an uppercase alphabet.")
else:
    print(f"{char} is not an uppercase alphabet.")