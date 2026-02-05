#write a program in python to input any number and print all factor
n = int(input("enter any number:"))
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")