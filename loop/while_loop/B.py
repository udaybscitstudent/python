#write a program in python to enter any number after that print count of digit of that number.
n = int(input("Enter any number:"))
c=0
while n!=0:
    n=n//10;
    c+=1
print("Count of digit is:",c)