square = lambda x: x * x   # Create a lambda function to find the square of a number

try:
    square_list = []  # Create an empty list to store square values

    for i in range(1, 21):   # Generate numbers from 1 to 20
        square_list.append(square(i))  # Store the square of each number in the list

    print("Squares of numbers from 1 to 20:")  # Display all square values
    print(square_list)

    print("\nEven Squares:")   # Print only even squares
    for num in square_list:

        if num % 2 == 0:
            print(num)

except Exception as e:  # Handle unexpected errors
    print("Error:", e)