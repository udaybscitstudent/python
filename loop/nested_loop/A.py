# write a program in python to print the seried of prime number up to hundred.

for i in range(2,100):
    c = 0
    for j in range(2,i):
        if(i%j==0):
            c=1
    if(c==0):
        print(i, end="+");
