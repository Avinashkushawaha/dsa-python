char = input("Enter a character: ").lower()

if char in 'aeiou' and len(char) == 1:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is not a vowels.")