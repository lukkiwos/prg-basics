###
# Credit card payment 
#

account_balance = 500
total_payment = int(input("Enter amount to pay: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

print()


def f(payment):
    balance = 500
    if balance >= payment:
        return "Payment succesfully completed"
    else:
        return "Go earn some money"
    

if __name__ == "__main__":
    print(f(499))