###
# Calculates the number of days in a month
#
month = int(input('Enter month number (1 - 12): '))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    days = 31               ## months with 31 days
elif month == 4 or month == 6 or month == 9 or month == 11:
    days = 30               ## months with 30 days
else:
    days = 28               ## February 28 days 

print(f'Month {month} has {days} days')
print()



def f(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        days = 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        days = 30
    else:
        days = 28
    return f"Miesiąc {month} ma {days} dni"
    

if __name__ == "__main__":
    print(f(1))
    print(f(2))
    print(f(4))