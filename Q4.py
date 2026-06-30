# Inventory Management System

inventory = {}

while True:
    print("\n----- Inventory Management System -----")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Delete Product")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_id = input("Enter Product ID: ")
        product_name = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        inventory[product_id] = {"Name": product_name, "Quantity": quantity}
        print("Product added successfully!")

    elif choice == 2:
        if len(inventory) == 0:
            print("No products available.")
        else:
            print("\nInventory:")
            for product_id, details in inventory.items():
                print("ID:", product_id,
                      "Name:", details["Name"],
                      "Quantity:", details["Quantity"])

    elif choice == 3:
        product_id = input("Enter Product ID to search: ")
        if product_id in inventory:
            print("Product Name:", inventory[product_id]["Name"])
            print("Quantity:", inventory[product_id]["Quantity"])
        else:
            print("Product not found.")

    elif choice == 4:
        product_id = input("Enter Product ID: ")
        if product_id in inventory:
            quantity = int(input("Enter New Quantity: "))
            inventory[product_id]["Quantity"] = quantity
            print("Quantity updated successfully!")
        else:
            print("Product not found.")

    elif choice == 5:
        product_id = input("Enter Product ID to delete: ")
        if product_id in inventory:
            del inventory[product_id]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please try again.")