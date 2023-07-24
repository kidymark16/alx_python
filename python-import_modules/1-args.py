import sys

if __name__ == "__main__":
    # get the command-line arguments
    args = sys.argv[1:]

    # print the number of arguments
    num_args = len(args)
    print("Number of argument{}: {}".format("s" if num_args != 1 else "", num_args), end="")

    # print the list of arguments if there are any
    if num_args > 0:
        print(":")
        for i, arg in enumerate(args, start=1):
            print("{}: {}".format(i, arg))
    else:
        print(".")
