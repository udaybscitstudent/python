#string is collecion of characters which is inclosed in single or double quotes.



str = "hello uday how are you what are you doing right now";

print(str[6:10])

for i in str[10:20]:
    print(i)

print(len(str))  # to find length of string

#string mehtods

"""
lower(): it converts all characters to lowercase
upper(): it converts all characters to uppercase
capitalize(): it converts first character to uppercase
title(): it converts first character of each word to uppercase
strip(): it removes leading and trailing whitespaces
replace(): it replaces a substring with another substring
split(): it splits the string into a list of substrings based on a delimiter

"""
print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.strip())
print(str.replace("uday", "udaykiran"))
#concating string
str1 = "hello"
str2 = "world"
str3 = str1 + " " + str2
print(str3)
print(str.split(" "))  # splits the string at spaces and returns a list of words


#format string
name = "uday"

print(f"hello {name}, how are you?")