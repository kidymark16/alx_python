# importing the add function from add_0.py
from add_0 import add

# defining the main function
def main():
    # assigning values to variables a and b
    a = 1
    b = 2

    # calling the add function and storing the result in a variable
    result = add(a, b)

    # printing the result using string formatting
    print("{} + {} = {}".format(a, b, result))

# checking if this is the main module
if __name__ == "__main__":
    # calling the main function
    main()
