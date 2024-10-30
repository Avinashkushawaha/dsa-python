arr = [30, 20, 23, 40, 50]
#finding max element
max=arr[0]

n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)      
    
#finding min element   
arr = [30, 20, 23, 40, 50]

min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)        
