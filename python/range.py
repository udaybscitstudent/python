'''
range():- the built-in range() function in Python is used to generate a sequence of numbers. 
It is commonly used in for loops to iterate over a block of code a specific number of times.

syntax:- range(start, stop, step)
'''

n = range(1,10,2)
for i in n:
    print(i, end=" ")
print()

print(n[2])
print(n[2:7])
print(n[:7])
print(len(n))
