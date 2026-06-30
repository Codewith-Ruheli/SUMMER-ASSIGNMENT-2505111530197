# Employee Management System

employees = {}

while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        employees[emp_id] = name
        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for emp_id, name in employees.items():
                print("Employee ID:", emp_id, " Name:", name)

    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in employees:
            print("Employee Name:", employees[emp_id])
        else:
            print("Employee not found.")

    elif choice == 4:
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee record deleted.")
        else:
            print("Employee not found.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")