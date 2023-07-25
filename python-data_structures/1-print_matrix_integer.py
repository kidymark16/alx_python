def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            # Use str.format() to print each integer with a width of 2 characters
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()
