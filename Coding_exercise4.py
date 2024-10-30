# import random

# names = input("Enter everybody's name separated by comma:")
# names = names.split(",")

# length=len(names)
# random_choice=randint(0,length-1)
# print(names [random_choice])

import random

names = input("Enter everybody's name separated by a comma: ")
names = names.split(",")

length = len(names)
random_choice = random.randint(0, length - 1)
print(names[random_choice])
