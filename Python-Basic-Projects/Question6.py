import random   # Import required modules
import math

numbers = set()   # Create an empty set to store unique numbers
print("Enter 10 numbers:")

for i in range(10):    # Take 10 numbers as input
    while True:
        try:
            num = int(input(f"Number {i+1}: "))   # Take number from the user
            numbers.add(num)   # Add number to the set
            break

        except ValueError:    # Handle invalid input
            print("Invalid input! Please enter a number.")

numbers_tuple = tuple(numbers)   # Convert the set into a tuple

print("\nUnique Numbers (Set):", numbers)   # Display the set and tuple
print("Tuple:", numbers_tuple)

try:
    if len(numbers_tuple) < 3:    # Check if there are at least 3 unique numbers
        raise ValueError("At least 3 unique numbers are required.")

    random_numbers = random.sample(numbers_tuple, 3)   # Select 3 random numbers from the tuple
    print("3 Random Numbers:", random_numbers)

    total = sum(numbers_tuple)    # Calculate the sum of tuple elements
    print("Square Root of Sum:", math.sqrt(total))   # Print the square root of the sum

except ValueError as e:   # Handle possible exceptions
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)