list1 = [1, 2, 3, 4, 5, 6, 7, 8, 2, 3, 4]

result = []

for i in list1:
    if i not in result:
        result.append(i)
        
print(result)        