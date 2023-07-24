def perform_addition():
    # import the add function from add_0.py
    from add_0 import add

    # assign values to variables a and b
    a = 1
    b = 2

    # call the add function and store the result in a variable
    result = add(a, b)

    # print the result using string formatting
    print("{} + {} = {}".format(a, b, result))

# check if this is the main module
if __name__ == "__main__":
    # call the perform_addition function
    perform_addition()
