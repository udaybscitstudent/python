
n1 = int(input("enter first number"))
n2 = int(input("Enter secod number"))
c1 = 0
c2 = 0
i=1
while i<=n1:
    if(n1%i==0):
        c1 += 1
    i=i+1
i=1
while i<= n2:
    if(n2%i==0):
        c2 += 1
    i = i+1;
if((c1==2 and c2==2) and (n1-n2==2) or (n2-n1==2)):
    print("twin prime number")
else:
    print("not twin prime number")