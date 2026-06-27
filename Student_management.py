# Dictionary to store all student records
students = {}


def calculate_percentage(marks):
    return sum(marks) / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B+"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    else:
        return "Fail"


def add_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Student with this Roll Number already exists!")
            return

        name = input("Enter Student Name: ")

        marks = []
        print("Enter marks of 5 subjects:")

        for i in range(5):
            mark = float(input(f"Subject {i+1}: "))
            marks.append(mark)

        attendance = float(input("Enter Attendance Percentage: "))

        percentage = calculate_percentage(marks)
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "percentage": percentage,
            "grade": grade
        }

        print("\nRecord Added Successfully!")

    except ValueError:
        print("Invalid Input!")


def view_all():

    if not students:
        print("\nNo Student Records Available.")
        return

    print("\n========== ALL STUDENTS ==========")

    for roll, data in students.items():

        print("\nRoll Number :", roll)
        print("Name        :", data["name"])
        print("Marks       :", data["marks"])
        print("Attendance  :", data["attendance"], "%")
        print("Percentage  : {:.2f}%".format(data["percentage"]))
        print("Grade       :", data["grade"])


def search_student():

    try:
        roll = int(input("Enter Roll Number to Search: "))

        if roll in students:

            data = students[roll]

            print("\nStudent Found!")
            print("Roll Number :", roll)
            print("Name        :", data["name"])
            print("Marks       :", data["marks"])
            print("Attendance  :", data["attendance"], "%")
            print("Percentage  : {:.2f}%".format(data["percentage"]))
            print("Grade       :", data["grade"])

        else:
            print("Student Not Found!")

    except ValueError:
        print("Invalid Roll Number!")


def update_student():

    try:
        roll = int(input("Enter Roll Number to Update: "))

        if roll not in students:
            print("Student Not Found!")
            return

        name = input("Enter New Name: ")

        marks = []
        print("Enter New Marks of 5 Subjects:")

        for i in range(5):
            mark = float(input(f"Subject {i+1}: "))
            marks.append(mark)

        attendance = float(input("Enter New Attendance Percentage: "))

        percentage = calculate_percentage(marks)
        grade = calculate_grade(percentage)

        students[roll] = {
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "percentage": percentage,
            "grade": grade
        }

        print("Record Updated Successfully!")

    except ValueError:
        print("Invalid Input!")


def delete_student():

    try:
        roll = int(input("Enter Roll Number to Delete: "))

        if roll in students:
            del students[roll]
            print("Record Deleted Successfully!")
        else:
            print("Student Not Found!")

    except ValueError:
        print("Invalid Roll Number!")


def total_students():

    print("\nTotal Students =", len(students))


def best_performance():

    if not students:
        print("No Student Records Available.")
        return

    best_roll = max(
        students,
        key=lambda roll: students[roll]["percentage"]
    )

    data = students[best_roll]

    print("\n===== BEST PERFORMANCE STUDENT =====")
    print("Roll Number :", best_roll)
    print("Name        :", data["name"])
    print("Percentage  : {:.2f}%".format(data["percentage"]))
    print("Grade       :", data["grade"])


def internship_eligible():

    if not students:
        print("No Student Records Available.")
        return

    found = False

    print("\n===== ELIGIBLE STUDENTS FOR INTERNSHIP =====")

    for roll, data in students.items():

        if data["percentage"] >= 70 and data["attendance"] >= 75:

            found = True

            print("\nRoll Number :", roll)
            print("Name        :", data["name"])
            print("Percentage  : {:.2f}%".format(data["percentage"]))
            print("Attendance  :", data["attendance"], "%")
            print("Grade       :", data["grade"])

    if not found:
        print("No Student Eligible for Internship.")


def show_menu():

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Total Student Count")
    print("7. Best Performance Student")
    print("8. Internship Eligible Students")
    print("9. Exit")


# Main Program
while True:

    show_menu()

    try:
        choice = int(input("\nEnter Your Choice: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_all()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            total_students()

        elif choice == 7:
            best_performance()

        elif choice == 8:
            internship_eligible()

        elif choice == 9:
            print("\nThank You For Using Student Management System!")
            break

        else:
            print("Please Enter Valid Choice (1-9)")

    except ValueError:
        print("Invalid Input! Enter Numbers Only.")