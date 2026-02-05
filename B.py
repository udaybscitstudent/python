# write a program in python to enter any decimal number and convert it into binary number.

n = int(input("Enter any decimal number: "))
bin = ""   
while n > 0:
    r = n % 2
    bin = str(r) + bin
    n = n // 2  
print("Binary number:", bin)