import math  # Import required modules
import random
from datetime import datetime

history = {}  # Dictionary to store calculation history

def basic_arithmetic():  # Function for basic arithmetic operations
    try:

        num1 = float(input("Enter First Number: "))  # Take two numbers from the user
        num2 = float(input("Enter Second Number: "))

        # Display arithmetic menu
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter Your Choice: ")

        if choice == "1":  # Perform the selected operation
            result = num1 + num2
            operation = "Addition"

        elif choice == "2":
            result = num1 - num2
            operation = "Subtraction"

        elif choice == "3":
            result = num1 * num2
            operation = "Multiplication"

        elif choice == "4":
            result = num1 / num2
            operation = "Division"

        else:
            print("Invalid Choice!")
            return

        print("Result:", result)  # Display the result

        time = str(datetime.now())    # Store the result in the dictionary
        history[time] = f"{operation} = {result}"

    except ZeroDivisionError:  # Handle division by zero
        print("Cannot divide by zero.")

    except ValueError:  # Handle invalid input
        print("Please enter valid numbers.")


# Function for scientific calculations
def scientific_calculation():
    try:
        # Take one number from the user
        num = float(input("Enter a Number: "))

        # Display scientific calculation menu
        print("\n1. Square Root")
        print("2. Square")
        print("3. Factorial")

        choice = input("Enter Your Choice: ")

        # Perform the selected operation
        if choice == "1":
            result = math.sqrt(num)
            operation = "Square Root"

        elif choice == "2":
            result = math.pow(num, 2)
            operation = "Square"

        elif choice == "3":
            result = math.factorial(int(num))
            operation = "Factorial"

        else:
            print("Invalid Choice!")
            return

        # Display the result
        print("Result:", result)

        # Store the result in the history dictionary
        time = str(datetime.now())
        history[time] = f"{operation} = {result}"

    # Handle invalid input
    except ValueError:
        print("Invalid Input.")


# Function to generate a random number
def generate_random():
    try:
        # Take starting and ending values
        start = int(input("Enter Starting Number: "))
        end = int(input("Enter Ending Number: "))

        # Generate a random number
        number = random.randint(start, end)

        # Display the random number
        print("Random Number:", number)

        # Store the result in history
        time = str(datetime.now())
        history[time] = f"Random Number = {number}"

    # Handle invalid input
    except ValueError:
        print("Please enter valid integers.")


# Function to display all stored results
def view_history():

    # Check whether history is empty
    if len(history) == 0:
        print("No History Available.")

    else:
        print("\n====== Calculation History ======")

        for key, value in history.items():  # Display all stored records
            print(key, ":", value)

while True:

    # Display the main menu
    print("\n===== Smart Calculator & Data Manager =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. View History")
    print("5. Exit")

    choice = input("Enter Your Choice: ")   # Take menu choice

    if choice == "1":  # Call the selected function
        basic_arithmetic()

    elif choice == "2":
        scientific_calculation()

    elif choice == "3":
        generate_random()

    elif choice == "4":
        view_history()

    elif choice == "5":
        print("Thank You! Program Ended.")
        break

    else:
        print("Invalid Choice! Please try again.")