#write a program in python to print sum of all even and odd factors seperately of a number accepted from user
n = int(input("enter any number:"))
even_sum = 0
odd_sum = 0
for i in range(1, n+1):
    if n%i==0:
        if i%2 ==0:
            even_sum += i
        else:
            odd_sum += i
print("sum of even factors is:", even_sum)
print("sum of odd factors is:", odd_sum)