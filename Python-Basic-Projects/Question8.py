class Employee:   # Create Employee class

    def __init__(self, emp_id, name, department, salary):   # Constructor to initialize employee details
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)  # Store department and salary in a tuple

    def show_details(self):    # Method to display employee details
        print("\nEmployee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])

employees = {}   # Create an empty dictionary

for i in range(1, 4):   # Take details for 3 employees
    print(f"\nEnter details of Employee {i}")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, salary)  # Create Employee object
    employees[emp_id] = emp  # Store object in dictionary using employee ID as key

print("\n====== Employee Details ======")   # Display all employee details

for emp_id, emp in employees.items():
    emp.show_details()