num = int(input("Enter a number here :"))

if num < 0:

    print ("Enter positive numbers")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(sum)   

