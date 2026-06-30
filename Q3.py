# Salary Management System

employees = {}

while True:
    print("\n----- Salary Management System -----")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = float(input("Enter Salary: "))
        employees[emp_id] = {"Name": name, "Salary": salary}
        print("Employee added successfully!")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for emp_id, details in employees.items():
                print("ID:", emp_id,
                      " Name:", details["Name"],
                      " Salary:", details["Salary"])

    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in employees:
            print("Name:", employees[emp_id]["Name"])
            print("Salary:", employees[emp_id]["Salary"])
        else:
            print("Employee not found.")

    elif choice == 4:
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            new_salary = float(input("Enter New Salary: "))
            employees[emp_id]["Salary"] = new_salary
            print("Salary updated successfully!")
        else:
            print("Employee not found.")

    elif choice == 5:
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")