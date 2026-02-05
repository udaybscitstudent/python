# write a proram in python to enter any number after that print sum of all digit of that number.
n = int(input("Enter anu number"))
s = 0
while n>0:
    r = n%10
    s += r
    n = n//10
print("Sum of all digit is:",s)