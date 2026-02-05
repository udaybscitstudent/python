# 1	write a program in c to input any binary number after that convert into decimal number 
#  this operation must be performed multiple times according to requirement.
n = int(input("Enter any binary number"))
dec = 0
i=0
while(n!=0):
    r = n%10
    dec = dec+r*2**i
    n=n//10
    i += 1

print("Decimal number:",dec)
