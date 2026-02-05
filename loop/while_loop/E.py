#write a program in python to print sum of square of even digit and cube of odd digit of that number.
n = int(input("Enter any number:"))
even_sum = 0
odd_sum = 0
while n>0:
    d = n%10
    if(d%2==0):
        even_sum += d**2
    else:
        odd_sum += d**3
    n = n//10
print("Sum of square of even digit is:",even_sum)
print("Sum of cube of odd digit is:",odd_sum)