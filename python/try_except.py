'''
exception handling: - when an error occurs or exeption as well call it, python will normally stop and generate error message.
these exeption can be handle by using try block.

try() :- the try block lets you test a block of code for errors.
except():- the except block lets you handle the error.
else() :- if you execute the code and there is no error occur the else block will be execute.
finally() :- 
'''

try:
    x=10
    print(x)
except :
    print("an execption occur");
# finally:
#     print("try except is executed");
else:
    print("no exeption occur");

# x=-1
# if x < 0:
#     raise Exception("sorry , no number below zero");

x = 'Hello'
if not type(x) is int:
    raise TypeError("only integers are allowed");