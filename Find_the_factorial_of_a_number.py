num = int(input("Enter a number here: "))
fact = 1
if num < 0 :
    print("factorial of 0 does not exist")
if num == 0:
    print("Factorial of 0 is 1")
if num > 0:
        
  for i in range (1, num+1):
        fact = fact * 1
print("the factorials of the given number is",fact)  
    