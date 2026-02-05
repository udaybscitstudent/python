#write a program in python to input any number after that count prime digit

n = int(input("Enter any prime number"))
pd = 0

while n>0:
    r = n%10
    c=0
    for i in range(1, r+1):
        if(r%i==0):
            c=c+1
    if(c==2):
        pd = pd+1

    n=n//10
print("prime digit=",pd);