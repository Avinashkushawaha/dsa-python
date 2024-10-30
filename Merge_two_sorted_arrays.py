arr = [1, 2, 3, 4]
arr1 = [5, 6, 7, 8]

merged_array = []

i, j = 0, 0

while i < len(arr) and j < len(arr1):
    if arr[i] < arr1[j]:
        merged_array.append(arr[i])
        i  += 1
    else:
        merged_array.append(arr[j])
        j += 1
        
merged_array.extend(arr[i:])
merged_array.extend(arr1[j:])

print("merged array :" , merged_array)  #
        

        