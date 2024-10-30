
       

# for i in range (1, 100):
#     if i % 3 == 0 :
#        print(i)
   



start = int(input("Enter the start of the range: "))  
end = int(input("Enter the end of the range: "))      
divisor = int(input("Enter the divisor: "))           


for i in range(start, end +1):  
    if i % divisor == 0:
        print(i)
