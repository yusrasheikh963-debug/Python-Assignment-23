class Student:    # Create a Student class

    def __init__(self, name, roll_no):   # Constructor to initialize student details
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []

    def add_mark(self, mark):    # Method to add a mark to the list

        if mark >= 0 and mark <= 100:    # Check if the mark is valid
            self.marks_list.append(mark)
        else:
            print("Marks should be between 0 and 100.")

    def get_average(self):    # Method to calculate the average marks

        if len(self.marks_list) == 0:   # Return 0 if no marks are available
            return 0

        return sum(self.marks_list) / len(self.marks_list)   # Calculate and return the average

    def display_info(self):   # Method to display student details
        print("\n----- Student Details -----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)
        print("Marks:", self.marks_list)
        print("Average Marks:", self.get_average())

# Take student detail from the user
name = input("Enter Student Name: ") 
roll_no = input("Enter Roll Number: ")
student = Student(name, roll_no)

print("\nEnter marks for 5 subjects:")

for i in range(5):    # Loop to take marks for 5 subjects
    while True:

        try:
            mark = float(input(f"Subject {i+1}: "))   # Take mark as input
            student.add_mark(mark)   # Add the mark to the student's marks list

            if mark >= 0 and mark <= 100:   # Exit the loop if the mark is valid
                break

        except ValueError:   # Handle invalid non-numeric input
            print("Invalid input! Please enter a number.")

student.display_info()   # Display all student details