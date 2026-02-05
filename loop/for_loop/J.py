#write a program in python to check entered number is perfect or not
n = int(input("enter any number"))
s = 0
for i in range(1, n):
    if n%i ==0 :
        s += i
if s == n:
    print("perfect number") 
else:
    print("not perfect number")