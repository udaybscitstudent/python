# write a program in python to enter any number and check that number is prime or not
n = int(input("Enter any number:"))
c=0
for i in range(1, n+1):
    if(n%i==0):
        c+=1
if c==2:
    print("prime")
else:
    print("not prime")