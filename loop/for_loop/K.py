#write a progran in python to print factorial of a number accepted from user
n = int(input("Enter any number:"))
fact = 1
for i in range(1, n+1):
    fact = fact * i
print("factorial of", n, "is:", fact)
