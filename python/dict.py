'''
dictionary:- 
A dictionary in Python is a data structure that stores key-value pairs. It is unordered, mutable, and does not allow duplicate keys.
Keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.
Dictionaries are defined using curly braces {} and each key-value pair is separated by a colon (:).

#dictionary method
clear() - removes all items from the dictionary
copy() - returns a shallow copy of the dictionary
get() - returns the value for a specified key if the key is in the dictionary
items() - returns a view object that displays a list of a dictionary's key-value tuple pairs
keys() - returns a view object that displays a list of all the keys in the dictionary
pop() - removes the item with the specified key and returns its value
popitem() - removes and returns the last inserted key-value pair as a tuple
update() - updates the dictionary with the specified key-value pairs
values() - returns a view object that displays a list of all the values in the dictionary

'''
student = {'name':{'first_name':'uday','last_name':'kumar'},'Roll':18 , 'course':'bscit'}
student['email']="uday@gmail.com"
print(type(student))
print(len(student))
student['name']['first_name']="pawan"
print(student['name']['first_name'])
student.pop('email')
print(student)

for key in student:
    print(key, student[key])

this_student=student.copy()
print(this_student)