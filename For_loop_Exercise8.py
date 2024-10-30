# wap a program to print all prime numbers between 1 and 50.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
divisor = int(input("Enter the divisor:"))


for i in range (start, end +1):
      if i % divisor == 0:
           print(i)      