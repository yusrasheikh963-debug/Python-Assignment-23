def student_marks():     # Function to manage and analyze student marks
    marks = []    # Create an empty list to store marks

    for i in range(5):      # Take marks for 5 subjects from the user
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i+1}: "))  # Accept input from user as a number
                marks.append(mark)   # Add the valid mark to the list
                break

            except ValueError:
                print("Invalid input! Please enter a numeric value.")  # Display message for invalid input

    average = sum(marks) / len(marks)    # Calculate the average marks
    highest = max(marks)   #Find the highest marks
    lowest = min(marks)    #Find the lowest marks

    sorted_marks = sorted(marks, reverse=True)    # Sort the marks in descending order

    # Display the results on the output screen
    print("\n====== Results ======")
    print("Marks Entered:", marks)
    print(f"Average Marks : {average:.2f}")
    print(f"Highest Marks : {highest}")
    print(f"Lowest Marks  : {lowest}")
    print("Marks in Descending Order:", sorted_marks)

student_marks()    # Call the function
               