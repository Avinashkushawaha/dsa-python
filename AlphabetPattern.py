# char = 'A'
# for row in range(3):
#     for col in range (3):
#         print(char, end=" ")
#     print()
#     char = chr(ord(char) + 1)  


# char = 'A'
# for row in range(3):
#     for col in range (3):
#         print(char, end=" ")
#         char = chr(ord(char) +1)
#         print()




# char = 'A'
# for row in range(3):
#         new = char
#         for col in range(3):
#           print(new, end=' ')
#           new = chr(ord(new) + 1)
#         print()
#         char = chr(ord(char) + 1)


n = 3
char = 'A'
for row in range(n):
    new = char 
    for col in range(n):
       if col <= n//3:
           print(new, end=' ')
           new = chr(ord(new) +1)
       else:
            print(new, end='')
            new = chr(ord(new)-1)
print()
char = chr(ord(char)+1 )


