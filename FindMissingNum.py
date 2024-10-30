Arr = [1, 2, 3, 5, 6, 7, 8,]

n = len(Arr)+ 1

sum = n * (n + 1) // 2

actual_sum = 0
for num in Arr:
    actual_sum += num
    
missing_number = sum - actual_sum
print(missing_number)

