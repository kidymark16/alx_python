def print_matrix_integer(matrix=None):
    if matrix is None:
        return

    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to print each integer with a width of 2 characters
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                # Print a space after each integer except the last one
                print(" ", end="")
        # Print a newline character after each row
        print()
