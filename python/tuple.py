'''
tuple:- A built-in Python data type that represents an immutable ordered collection of items.
it is used to represent a small bracket ().
tuples are similar to lists, but unlike lists, tuples cannot be modified after their creation (they are immutable).
#tuple methods
count(): it is used to return the number of occurrences of an item in the tuple.
index(): it is used to return the index of the first occurrence of an item in the tuple.
# how to create a tuple
mytuple = (1, 2, 3, 4, 5)
print(mytuple[0])
'''

from itertools import count


color = ("red", "green", "blue", "yellow" ,"green")
print(type(color))
print(color.count("green"))
print(color[1])
print(color.index("blue"))

# color[2] = "black"  # This will raise an error because tuples are immutable
a = list(color)
a[2] = "black"
color = tuple(a)
print(len(color))


print(color)


