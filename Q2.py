# Menu Driven Array Operations System

arr = []

while True:
    print("\n----- Array Operations -----")
    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Find Maximum")
    print("6. Find Minimum")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element to insert: "))
        arr.append(element)
        print("Element inserted successfully!")

    elif choice == 2:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array:", arr)

    elif choice == 3:
        element = int(input("Enter element to search: "))
        if element in arr:
            print("Element found at index", arr.index(element))
        else:
            print("Element not found.")

    elif choice == 4:
        element = int(input("Enter element to delete: "))
        if element in arr:
            arr.remove(element)
            print("Element deleted successfully!")
        else:
            print("Element not found.")

    elif choice == 5:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Maximum element:", max(arr))

    elif choice == 6:
        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Minimum element:", min(arr))

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")