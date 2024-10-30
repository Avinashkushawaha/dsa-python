nterms = int(input("Enter number of terms here:"))

result = list(map(lambda X : 2 ** X, range(nterms+1)))
# print(result)

for i in range(nterms+1):
    print("the value of 2 raised to power",i,"is",result[i])