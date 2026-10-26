###
# Credit card payment 
#
account_balance = 500
total_payment = int(input("Enter amount to pay: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')


def f(payment):
    account = 500

    if account >= payment:
        return "payment successful"
    else:
        return "no funds"

if __name__ == "__main__":
    print(f(140))
    print(f(499))
    print(f(500))
    print(f(501))
    print(f(720))