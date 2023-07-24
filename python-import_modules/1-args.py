import sys

if __name__ == "__main__":
    # get the number of arguments
    num_args = len(sys.argv) - 1  # the first argument is the script name

    # print the number of arguments
    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args), end="")

    # print the list of arguments if there are any
    if num_args > 0:
        print(":", end="\n")
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}: {}".format(i, arg))
    else:
        print(".")
