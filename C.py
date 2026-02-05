# write a program in python to find HCF of two numbers.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
small = min(a, b)

while small > 0:
    if a % small == 0 and b % small == 0:
        print("HCF is:", small)
        break
    small -= 1