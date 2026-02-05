#write a program in python to enter any number after that print sum of even digit and sum of odd digit of that number.
n = int(input("Enter any number:"))
even_sum = 0
odd_sum = 0
while n>0:
    d = n%10
    if(d%2==0):
        even_sum += d
    else:
        odd_sum += d
    n = n//10
print("Sum of even digit is:",even_sum)
print("Sum of odd digit is:",odd_sum)