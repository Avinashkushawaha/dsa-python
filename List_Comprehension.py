# a = ['ironman','hulk','vision','thor']
# # for i in a:
# #  print(i.upper())

# new_list = [i.upper() for i in a]
# print(new_list)

# m = [i for i in range(10)]
# print(m)  
k = [1,2,3,4,5,6,7,8,9]
new_list = []
for i in k:
    if i % 2 == 0:
       new_list.append(i)

print(new_list)        