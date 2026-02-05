# Write a program to print all even factors of a number accepted from user
n = int(input("enter any number:"))
for i in range(1,n+1):
    if n%i==0:
        if i%2 ==0:
            print(i,end=" ")