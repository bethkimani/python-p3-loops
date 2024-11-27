#!/usr/bin/env python3

# Function for Happy New Year Countdown
def happy_new_year():
    count = 10
    while count > 0:  # Start from 10 and go down to 1
        print(count)
        count -= 1  # Decrement the count
    print("Happy New Year!")  # After loop, print celebration message

# Function to square integers in a list
def square_integers(int_list):
    return [num ** 2 for num in int_list]  # Use list comprehension to square each element

# Function for FizzBuzz
def fizzbuzz():
    for num in range(1, 101):  # Loop from 1 to 100
        if num % 3 == 0 and num % 5 == 0:  # Multiple of both 3 and 5
            print("FizzBuzz")
        elif num % 3 == 0:  # Multiple of 3
            print("Fizz")
        elif num % 5 == 0:  # Multiple of 5
            print("Buzz")
        else:  # Not a multiple of 3 or 5
            print(num)

# Test the functions
if __name__ == "__main__":
    print("Happy New Year Countdown:")
    happy_new_year()

    print("\nSquare Integers:")
    squared_list = square_integers([1, 2, 3, 4, 5])
    print(squared_list)  # Expected Output: [1, 4, 9, 16, 25]

    print("\nFizzBuzz:")
    fizzbuzz()
