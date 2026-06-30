# Student Record System using Arrays and Strings

roll_no = []
name = []

while True:
    print("\n----- Student Record System -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r = input("Enter Roll Number: ")
        n = input("Enter Student Name: ")

        roll_no.append(r)
        name.append(n)

        print("Student added successfully!")

    elif choice == 2:
        if len(roll_no) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for i in range(len(roll_no)):
                print("Roll No:", roll_no[i], " Name:", name[i])

    elif choice == 3:
        r = input("Enter Roll Number to search: ")

        if r in roll_no:
            index = roll_no.index(r)
            print("Student Name:", name[index])
        else:
            print("Student not found.")

    elif choice == 4:
        r = input("Enter Roll Number to delete: ")

        if r in roll_no:
            index = roll_no.index(r)
            roll_no.pop(index)
            name.pop(index)
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")