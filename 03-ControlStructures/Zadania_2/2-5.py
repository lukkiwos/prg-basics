###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10 and month <= 12:
    quarter = 4
elif month >= 7 and month <= 9:
    quarter = 3
elif month >= 4 and month <= 6:
    quarter = 2
elif month >= 1 and month <= 3:
    quarter = 1
else:
    print("Incorrect number")

print(f'Month {month} is in quarter {quarter}')
print()


def f(miesiac):

    if miesiac >= 10 and miesiac <= 12:
        kwartal = 4
    elif miesiac >= 7 and miesiac <= 9:
        kwartal = 3
    elif miesiac >= 4 and month <= 6:
        kwartal = 2
    elif miesiac >= 1 and month <= 3:
        kwartal = 1
    else:
        return "Niepoprawna liczba"

    return f"Miesiąc {miesiac} jest w {kwartal} kwartale"


if __name__ == "__main__":
    print(f(2))
    print(f(5))
    print(f(8))
    print(f(11))