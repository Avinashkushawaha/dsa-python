#write a program to find and print the largest number in a list without using the built-in max() function.
list = [10, 45, 78, 89, 2]
max_num = list[0]
for i in list:
    if i > max_num:

        max_num = i

print(max_num)