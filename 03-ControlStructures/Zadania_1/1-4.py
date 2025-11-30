###
# Credit card payment 
#

account_balance = 500
total_payment = int(input("Podaj kwotę transakcji: "))

if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')

    #140, 499, 500, 501, 720