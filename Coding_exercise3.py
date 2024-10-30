
    
name1 = input("What is your name? ")
name2 = input("What is his/her name? ")

# Combine the names and convert to lowercase
combine_string = name1 + name2
lower_case_string = combine_string.lower()

# Count occurrences of letters in the word "TRUE"
t = lower_case_string.count('t')
r = lower_case_string.count('r')
u = lower_case_string.count('u')
e = lower_case_string.count('e')

true_score = t + r + u + e

# Count occurrences of letters in the word "LOVE"
l = lower_case_string.count('l')
o = lower_case_string.count('o')
v = lower_case_string.count('v')
e = lower_case_string.count('e')
love_score = l + o + v + e

# Combine the two scores
love_score_total = int(str(true_score) + str(love_score))

# Determine the result based on the love score
if love_score_total < 10 or love_score_total > 90:
    print(f"Your score is {love_score_total}, and you go together like coke and mentos.")
elif 40 <= love_score_total <= 50:
    print(f"Your score is {love_score_total}, and you are alright together.")
else:
    print(f"Your score is {love_score_total}.")


