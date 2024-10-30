#wap a program print of n number
'''
sum(1) = 1
sum(2) = 1 x 2
sum(3) = 1 x 2 x 3
sum(4) = 1 x 2 x 3 x 4
sum(n) = 1 x 2 x 3 x 4 x 5 +............(n-1) x n
 
'''


# def sum(n):
#     if n == 1:
#         return 1
#     return sum (n-1) + n



# print(sum(5))



# n = int(input("Enter the number:"))
# sum = (n*(n+1)//2)
# print(f"Sum of numbers till {n} is: ", sum)


def factorial(n):
    
    if n==1:
        return n
    elif n==0:
        return 1
    
    return n*factorial(n-1)
print(factorial(-1))

