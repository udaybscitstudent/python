# write a program in python to check whether a number is armstrong number or not.
n  = int(input("enter any number:"))
num = n
c = 0
sum = 0
while n>0:
    c=c+1
    n=n//10

n = num
while n>0:
    d = n%10;
    sum = sum + d**c
    n = n//10
if(sum==num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")