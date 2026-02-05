#write a program in c to enter any no after that print table.
num = int(input("enter any number:"))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")