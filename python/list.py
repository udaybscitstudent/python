# what is list:- list is a data type in python which is used to store multiple items in a single variable.
# list is mutable which means we can change the values of list after its creation.
# list is ordered which means the items in the list have a defined order and that order will not change.
# list allows duplicate values which means we can have multiple items with the same value in a list

# how to create a list
mylist = [1, 2, 3, 4, 5]
mylist[2] = 10  # changing the value at index 2
mylist.append(15)  # inserting 15 at the end of the list
mylist.insert(2, 7)  # inserting 7 at index 2
mylist.remove(4)  # removing 4 from the list
print(mylist[0])
print(mylist[:4])
print(mylist)
print(type(mylist))

#list methods
'''
append(): it is used to add on an item to the end of the list.
extend(): it is used to add multiple items to the end of the list.
insert(): it is used to add an item at a specific index in the list.
remove(): it is used to remove the first occurrence of an item from the list.
pop(): it is used to remove and return an item at a specific index in the list.
clear(): it is used to remove all items from the list.
sort(): it is used to sort the items of the list in ascending order.
reverse(): it is used to reverse the order of the items in the list.
count(): it is used to return the number of occurrences of an item in the list.
index(): it is used to return the index of the first occurrence of an item in the list.


'''

