#write a program that count the number of vowels in a given strong using a for loop.
string = input("Enter a string : ")

vowel_count = 0

vowels = "aeiouAETOU"

for char in string:
    if char  in vowels:
        vowel_count += 1
print("Numbers of vowels in the given string:", vowel_count)