arr = [5, 8, 9, 6, 10, 15, 20]
# arr.sort()
# print(arr)

largest= arr [0]
sec_largest=arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest=arr[i]
        
    
for i in range(len(arr)):
    if arr[i]>sec_largest and arr[i]!=largest:
        sec_largest=arr[i]
        
print(sec_largest)        
              