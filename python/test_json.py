'''
"""JSON (JavaScript Object Notation) <https://json.org/> support.
This module provides an easy way to encode and decode data in JSON format.
It is part of Python's standard library and can be used to work with JSON data.
The json module can convert Python objects into JSON strings and vice versa.
"""
'''
import json
# convert python object to json string

student = {
    "name" : "uday",
    "roll" : 18, 
    "course" : "bscit" ,
    "mobile" :9334612395,
    "email" : "uday@gmail.com"
}
y = json.dumps(student, indent=4 , separators=(". ", " = "), sort_keys=True)
print(type(y))
print(y)

# convert json string to python object

json_string = '{"name": "uday", "roll": 18, "course": "bscit", "mobile": 9334612395, "email": "uday@gmail.com"}'
student_dict = json.loads(json_string)
print(type(student_dict))
print(student_dict)

# you can convert python object to json string 
print(json.dumps({"name":"uday", "roll" : 18}))
print(json.dumps([1, 2, 3, 4, 5]))
print(json.dumps(("apple", "banana", "cherry")))
print(json.dumps("Hello World"))
print(json.dumps(42))
print(json.dumps(3.14))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

