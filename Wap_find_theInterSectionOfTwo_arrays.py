array1 = [1, 3, 4, 5, 7]
array2 = [2, 3, 5, 6]

set_array2 = set(array2)


intersection = []


for element in array1:
       
    if element in set_array2:
        intersection.append(element)

# Print the intersection of the two arrays
print("Intersection of the two arrays:", intersection)
