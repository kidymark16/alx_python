import sys

# check if add_0 module has already been imported
if "add_0" in sys.modules:
    # if add_0 has already been imported, get the reference to the module
    add_module = sys.modules["add_0"]
else:
    # if add_0 has not been imported, import the module
    import add_0
    add_module = add_0

# get the reference to the add function
add = add_module.add

# define the main function
def main():
    # assign values to variables a and b
    a = 1
    b = 2

    # call the add function and store the result in a variable
    result = add(a, b)

    # print the result using string formatting
    print("{} + {} = {}".format(a, b, result))

# check if this is the main module
if __name__ == "__main__":
    # call the main function
    main()
