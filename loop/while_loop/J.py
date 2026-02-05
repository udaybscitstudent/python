# write a program in python to check entered number is composite or not
n = int(input("Enter any number: "))
c = 0
i=1;
while i <= n:
    if(n%i==0):
        c = c+1
    i = i + 1

if(c>2):
    print(n,"is a composite number")
else:
    print(n,"is a not composite number")