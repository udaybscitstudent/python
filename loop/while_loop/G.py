# Program to reverse a number using while loop
n = int(input("Enter any number:"))
r = 0
while n>0:
    d = n%10
    r = r*10 + d
    n = n//10

print("Reversed number is:",r)