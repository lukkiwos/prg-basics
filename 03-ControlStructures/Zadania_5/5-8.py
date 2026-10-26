###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Check PIN")
    print("3. Change PIN")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Exit")

    choice = input("Choose an option (1 - 6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")

    elif choice == "2":
        print(f"Your current PIN is: {pin}")

    elif choice == "3":
        check = input("Enter your old PIN in order to change it: ")
        if check:
            pin = input("Enter new pin: ")
            if pin.isdigit() and len(pin) == 4:
                print(f"Your new pin is: {pin}")
            else:
                print("Wrong PIN. Only for digits")
        else:
            print("Invalid PIN")

    elif choice == '4':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")

    elif choice == '5':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")

    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    else:
        print("Invalid option. Please try again.")
