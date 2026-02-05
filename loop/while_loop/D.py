# write a program in python to enter any number after that print average of even digit of that number.
n = int(input("Enter any number:"))
c = 0
s =0
while n>0:
    d = n%10
    if d%2==0:
        s += d
        c += 1
    n = n//10
print("average of even digit:",s//c)