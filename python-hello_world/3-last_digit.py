import random

try:
    # Assign a random signed number to the variable number
    number = random.randint(-10000, 10000)

    # Get the last digit of number using modulo operator %
    last_digit = abs(number) % 10

    # Print the last digit of number and additional information based on its value
    if last_digit > 5:
        if number > 0:
            print(f"Last digit of {number} is {last_digit} and is greater than 5")
        else:
            print(f"Last digit of {number} is -{last_digit} and is greater than 5")
    elif last_digit == 0:
        print(f"Last digit of {number} is {last_digit} and is 0")
    else:
        if number > 0:
            print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
        else:
            print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")
except TypeError:
    print("Error: Input must be an integer.")
