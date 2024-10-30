# list1 = [3, 6, 8, 2, "a","j"]
# list2 = [3, 6,"k","f","j"]

# result = list1 + list2
# print(result)

list1 = [3, 6, 8, 2, "a","j"]
list2 = [3, 6,"k","f","j"]

# list3 = [2,5,6,1,2,5,6]
l12 = list(set(list1+list2))
print(l12)