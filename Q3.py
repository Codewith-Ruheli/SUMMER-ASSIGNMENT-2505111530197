# ATM Simulation

balance = 10000

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposit successful!")
        print("Current Balance:", balance)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Current Balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice! Please try again.")