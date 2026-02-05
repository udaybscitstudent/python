'''
Array:- it is a linear data structure that stores multiple items in a single variable. it can be accessed by using an index.

# array methods
append() - adds an element to the end of the array
pop() - removes the last element from the array 
insert() - adds an element at a specific index
remove() - removes the first occurrence of a specific element
sort() - sorts the elements of the array in ascending order
reverse() - reverses the order of elements in the array
len() - returns the number of elements in the array
index() - returns the index of the first occurrence of a specific element
extend() - adds multiple elements to the end of the array
clear() - removes all elements from the array
example:-

'''

arr = [10,20,30,40,50]
print(arr[0])          # Accessing first element
print(arr[1])          # Accessing second element

arr.append(60)         # Adding an element to the end
print(arr)
arr.pop()              # Removing the last element
arr.remove(30)
arr.insert(2, 25)

print(len(arr))          # Finding the length of the array
n = int(input("How many items you want to insert in it"))
print("Enter " ,n ," numbers");
for i in range(n):
    arr[i] = int(input());

print(arr);

