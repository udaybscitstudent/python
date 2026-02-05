'''
what is module in python:- 
A module in Python is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Modules can define functions, classes, and variables, and can also include runnable code.

'''

def add(*var):
    total = 0
    for i in var:
        total += i
    return total

add()
