# Student Record Management System

students = {}

while True:
    print("\n----- Student Record Management -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students[roll] = name
        print("Student record added successfully!")

    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for roll, name in students.items():
                print("Roll No:", roll, " Name:", name)

    elif choice == 3:
        roll = input("Enter Roll Number to search: ")
        if roll in students:
            print("Student Name:", students[roll])
        else:
            print("Student not found.")

    elif choice == 4:
        roll = input("Enter Roll Number to delete: ")
        if roll in students:
            del students[roll]
            print("Student record deleted.")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")