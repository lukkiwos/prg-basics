class Bank():
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: PLN {amount:.2f}")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdrawn: PLN {amount:.2f}")
        else:
            print("Insufficient funds on the account")



    def display_info(self):
        print(f"Bank Account No: {self.account_no}")
        print(f"Balance: PLN {self.balance:.2f}")
        print("-" * 40)


def main():
    my_account = Bank("12 3456 5555 9090 1111 0000 7722")

    my_account.display_info()
    
    my_account.deposit(25.30)
    my_account.display_info()
    
    my_account.withdraw(31.70)
    my_account.display_info()
    
    my_account.withdraw(14)
    my_account.display_info()


if __name__ == "__main__":
    main()