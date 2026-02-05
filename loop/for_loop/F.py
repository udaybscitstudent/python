#write a progrm in python to enter any no and print sum of all factor of that no.
n = int(input("enter any number:"))
s = 0
for i in range(1, n+1):
    if n % i == 0:
        s += i
print("sum of all factor is:", s)