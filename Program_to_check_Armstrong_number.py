# user_input = int(input("Enter a number : "))

# sum = 0
# temp = user_input

# while temp > 0:
#     digit = temp % 10
#     cube = digit ** 3
#     sum = sum + cube
#     temp //= 10

# if sum == user_input:
#     print("it is armstrong Number")
# else:
#     print("it is not armstrong Number")


# *********************

start = int(input("Enter the starting number here: "))
end = int(input("Enter the ending number here: "))
step = int(input("Enter the step value: "))

for num in range(start, end + 1, step):
    
    num_str = str(num)
    num_digit = len(num_str)

    sum_of_power = 0

    for digit in num_str:
        sum_of_power += int(digit) ** num_digit

        if sum_of_power == num:

            print(f"{num} is an armstrong number")    



