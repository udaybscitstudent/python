'''
format string:  f-string is allow you to format selected parts of a string.

'''
name = "uday"
city = 'gaya'
pay = 50
print(f"my name is {name} and i am from {city} and you will have to pay {pay:.2f} ruppes")

# perform mathematical operator in f-string
print(f"the price is {50+5}")
print(f"the price is {50-5}")
print(f"the price is {50*5}")
print(f"the price is {50/2:.2f}")
print(f"the price is {50//3}")

# you can also use if alse in f-string
age=18
print(f"you are {'eligible' if age>=18 else 'not eligible'} for votting")

# execute function in f-string
name = 'uday'
print(f"mu name is {name.upper()}")

# use comma as a thousand separator
price = 50000
print(f"the price is {price:,}")