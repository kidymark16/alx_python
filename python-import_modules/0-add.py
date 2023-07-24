# importing the add function from add_0.py
from add_0 import add

if __name__ == "__main__":
    # assigning values to variables a and b
    a = 1
    b = 2

    # calling the add function and storing the result in a variable
    result = add(a, b)

    # printing the result using string formatting
    print("{} + {} = {}".format(a, b, result))
