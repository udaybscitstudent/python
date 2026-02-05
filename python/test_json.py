'''
"""JSON (JavaScript Object Notation) <https://json.org/> support.
This module provides an easy way to encode and decode data in JSON format.
It is part of Python's standard library and can be used to work with JSON data.
The json module can convert Python objects into JSON strings and vice versa.
"""
'''
import json

student = {
    "name" : "uday",
    "roll" : 18, 
    "course" : "bscit" ,
    "mobile" :9334612395,
    "email" : "uday@gmail.com"
}

y = json.dumps(student)

print(y)
