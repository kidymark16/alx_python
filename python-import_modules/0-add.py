# importing the add function from add_0.py
from add_0 import add

# assigning values to variables a and b
a = 1
b = 2

# calling the add function with a and b as arguments and storing the result in a variable
result = add(a, b)

# printing the result using string formatting
print("{0} + {1} = {2}".format(a, b, result))
