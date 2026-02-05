# Program to check whether a number is palindrome or not
n = int(input("Enter any number:"))
r = 0
num = n
while n>0:
    d = n%10
    r = r*10 + d
    n = n//10
if(num==r):
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")