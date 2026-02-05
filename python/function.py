'''
function:- funciton is a small peace of code that is used to perform a specific task.
    It helps to break down a large program into smaller and manageable pieces.
# how to create a function
'''
# simple function 
def fun():
    print("Hello World");

fun()

# function with parameters
def greet(name):
    print("good morning "+name);

greet("uday")

# function with return value
def add(a, b):
    return a + b;
result = add(5, 10)
print("Sum is:", result)

# function with multiple parameters
def add_multi(*args):
    s = 0
    for i in args:
        s += i
    return s
print("Sum of multiple numbers is:", add_multi(1, 2, 3, 4, 5))

# function with default parameters
def greet_default(name="Guest"):
    print("Hello " + name); 
greet_default()
greet_default("Uday")

# function recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print("Factorial is:", factorial(5))