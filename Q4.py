# Menu Driven String Operations System

string = input("Enter a string: ")

while True:
    print("\n----- String Operations -----")
    print("1. Display String")
    print("2. Find Length")
    print("3. Convert to Uppercase")
    print("4. Convert to Lowercase")
    print("5. Reverse String")
    print("6. Check Palindrome")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("String:", string)

    elif choice == 2:
        print("Length:", len(string))

    elif choice == 3:
        print("Uppercase:", string.upper())

    elif choice == 4:
        print("Lowercase:", string.lower())

    elif choice == 5:
        print("Reversed String:", string[::-1])

    elif choice == 6:
        if string == string[::-1]:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")