###
# ATM (cash machine) simulator
#
balance = 1000  # Initial balance
pin = '1111' # initial 4-digit PIN code

while True:
    print()
    print("ATM Menu: ")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    print()
    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print(f"Your current balance is: €{balance}")
    
    elif choice == '2':
        amount = float(input("Enter the amount to deposit: "))
        balance += amount
        print(f"€{amount} has been deposited. New balance: €{balance}")
    
    elif choice == '3':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"€{amount} has been withdrawn. New balance: €{balance}")
        else:
            print("Insufficient balance.")
    
    elif choice == "4":
        print(f"Your PIN is: {pin}")
    
    elif choice == "5":
        pin = (input("Enter new PIN: "))
        if pin.isdigit() and len(pin) == 4:
            print(f"You've changed PIN. Your new PIN is: {pin}")
        else:
            print("Error incorrect PIN")
    
    elif choice == '6':
        print("Exiting... Thank you for using the ATM!")
        break  # Exit the loop
    
    else:
        print("Invalid option. Please try again.")






def f():
    balance = 5000
    pin = '2137'

    while True:
        print()
        print("ATM Menu: ")
        print("1. Sprawdź stan konta")
        print("2. Wpłata środków")
        print("3. Wypłata środków")
        print("4. Sprawdź PIN")
        print("5. Zmień PIN")
        print("6. Wyjdź")

        print()
        choice = input("Wybierz opcję (1-6): ")
        print()

        
        if choice == '1':
            print(f"Twoje saldo konta to: {balance} zł")
        
        elif choice == '2':
            amount = float(input("Wprowadź ilość środków do zdeponowania: "))
            balance += amount
            print(f"{amount} zł zostało zdeponowane do twojego konta. Twoje nowe saldo konta to: {balance} zł")

        elif choice == '3':
            amount = float(input("Wprowadź ilość środków do wypłaty: "))
            if amount <= balance:
                balance -= amount
                print(f"Wypłacono {amount} zł. Nowe saldo konta to: {balance} zł")
            else:
                print("Błąd!")
            
        elif choice == '4':
            print(f"Twój numer PIN to: {pin}")

        elif choice == '5':
            pin = input("Wprowadź nowy numer PIN: ")
            if pin.isdigit() and len(pin) == 4:
                print(f"Zmieniłeś numer PIN. Twój nowy numer PIN to: {pin}")
            else:
                print("Błąd")

        elif choice == '6':
            print("Wychodzenie... Siema!")
            break
        
        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")
    return "Koniec programu"


if __name__ == "__main__":
    print(f())