###
# Calculates and prints the quarter of the year for a given
# month number (1..12)
#
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif month < 10 and month >= 7:
    quarter = 3
elif month < 7 and month >= 4:
    quarter = 2
elif month < 4 and month >= 1:
    quarter = 1


print(f'Month {month} is in quarter {quarter}')
print()



def f(miesiac):
    if miesiac >= 1 and month < 4:
        quarter = 1
    elif miesiac >= 4 and month < 7:
        quarter = 2
    elif miesiac >= 7 and month < 10:
        quarter = 3
    elif miesiac >= 10 and month < 13:
        quarter = 4
    result = f"Month {miesiac} is in quarter {quarter}"
    return result


if __name__ == "__main__":
    print(f(7))