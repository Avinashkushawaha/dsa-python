# divisor = int(input("Enter number here: "))

# for num in range (1, 100, ):
#     if num % divisor == 0:
#         print(num)


# ****************

l = [39, 48, 26, 98, 33, 67, 87]

result = list(filter(lambda X : X % 13 == 0,l))
print('the numbers divisible by 13 are', result)

