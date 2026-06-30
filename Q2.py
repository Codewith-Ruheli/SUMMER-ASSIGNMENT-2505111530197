# Mini Library System

books = []

while True:
    print("\n----- Mini Library System -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book added successfully!")

    elif choice == 2:
        if len(books) == 0:
            print("Library is empty.")
        else:
            print("\nAvailable Books:")
            for book in books:
                print(book)

    elif choice == 3:
        book = input("Enter Book Name to search: ")
        if book in books:
            print("Book is available.")
        else:
            print("Book not found.")

    elif choice == 4:
        book = input("Enter Book Name to remove: ")
        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found.")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")