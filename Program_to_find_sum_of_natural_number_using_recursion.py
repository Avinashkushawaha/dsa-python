def  NNS (n):
    if n <= 1:
        return n
    else:
        return(n)+NNS(n-1)

n = int(input("Enter a number here: ")) 
if n <=0:
    print ("Enter a positive number: ")
else:
  print(f"The sum of natural number upto given number is", NNS(n))  
