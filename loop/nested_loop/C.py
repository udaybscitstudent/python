#write a progarm in python to print the series of perfect no up to 1000.

for i in range(1, 1000):
    s=0
    for j in range(1, i):
        if(i%j==0):
            s = s+j;
    if(i==s):
        print(i, end="+")
