lst = eval(input("Enter a list: "))

if len(lst) % 2 != 0:
    middle_value = lst[len(lst) // 2]
    print(f"The list has a middle value: {middle_value}")
else:
    print("The list has no single middle value.")    