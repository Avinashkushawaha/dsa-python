a = 0
b = 1

num = int(input("Enter a number to obtain fibonacci sequence :"))
if num == 1:
    print(a)
else:    
    print(a)
    print(b)
    for i in range (2, num ):
        c = a + b
        a = b
        b = c
        print(c)



# a = 0
# b = 1

# num = int(input("Enter a number to obtain Fibonacci sequence: "))
# if num == 1:
#     print(a)
# else:
#     print(a)  # Print first number
#     print(b)  # Print second number
#     for i in range(2, num):  # Loop starting from 2 because first two numbers are already printed
#         c = a + b
#         print(c)  # Print the current Fibonacci number
#         a = b  # Update a to the previous b
#         b = c  # Update b to the current Fibonacci number

