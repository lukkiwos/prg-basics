###
# A program for printing detailed information.
#

employee = "Mr. John May, born on 1998-02-16"

print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-10:]}')
print(f'Initials: {employee[4], employee[9]}')
print()


def f(dane):
    imie = dane[4:8]
    nazwisko = dane[9:12]
    rok = dane[-10:]
    inicjaly = dane[4] + dane[9]
    result = imie, nazwisko, rok, inicjaly
    return " ".join(result)


if __name__ == "__main__":
    result = "Mr. John May, born on 1998-02-16"
    print(f(result))