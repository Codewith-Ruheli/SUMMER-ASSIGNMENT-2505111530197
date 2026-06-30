# Mini Employee Management System

emp_id = []
emp_name = []

while True:
    print("\n----- Mini Employee Management System -----")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        emp_id.append(eid)
        emp_name.append(name)

        print("Employee added successfully!")

    elif choice == 2:
        if len(emp_id) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            for i in range(len(emp_id)):
                print("Employee ID:", emp_id[i], " Name:", emp_name[i])

    elif choice == 3:
        eid = input("Enter Employee ID to search: ")

        if eid in emp_id:
            index = emp_id.index(eid)
            print("Employee Name:", emp_name[index])
        else:
            print("Employee not found.")

    elif choice == 4:
        eid = input("Enter Employee ID to delete: ")

        if eid in emp_id:
            index = emp_id.index(eid)
            emp_id.pop(index)
            emp_name.pop(index)
            print("Employee deleted successfully!")
        else:
            print("Employee not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")