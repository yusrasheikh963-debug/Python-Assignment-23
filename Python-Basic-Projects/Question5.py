def student_database():  # Function to manage the student database

    students = {}   # Dictionary to store student records

    while True:
        print("\n====== Student Database Menu ======")  # Display menu options
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        choice = input("Enter your choice: ")   # Take user's choice

        if choice == "1":    # Add a new student
            try:
                roll_no = int(input("Enter Roll Number: "))   # Take student details
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                students.update({    # Add student record using update()
                    roll_no: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student added successfully!")

            except ValueError:
                print("Invalid input! Roll number and age must be numbers.")

        elif choice == "2":    # Search student by roll number
            try:
                roll_no = int(input("Enter Roll Number to search: "))
                student = students.get(roll_no)  # Search using get()

                if student:
                    print("\nStudent Found")
                    print("Name :", student["Name"])
                    print("Age  :", student["Age"])
                    print("City :", student["City"])
                else:
                    print("Student not found.")

            except ValueError:
                print("Please enter a valid roll number.")

        elif choice == "3":  # Display all students

            if len(students) == 0:
                print("No student records found.")
            else:
                print("\n====== Student Records ======")

                for roll_no, details in students.items():
                    print("\nRoll Number:", roll_no)
                    print("Name :", details["Name"])
                    print("Age  :", details["Age"])
                    print("City :", details["City"])

        elif choice == "4":   # Exit the program
            print("Exiting Student Database...")
            break

        else:    # Handle invalid menu choice
            print("Invalid choice! Please select from 1 to 4.")

student_database()  # Call the function