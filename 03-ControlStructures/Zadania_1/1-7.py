###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus = 0.30 # 15%
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')
print()


def f(czy_bonus):
    wyplata = 10000
    cala_wyplata = 0
    bonusy = 0.30

    if czy_bonus:
        cala_wyplata = wyplata + (wyplata * bonusy)
    else:
        cala_wyplata = wyplata

    return f"Podstawowa wypłata: {wyplata}\nCzy bonus: {czy_bonus}\nCałkowita wypłata: {cala_wyplata:.0f}\n"


if __name__ == "__main__":
    print(f(True))
    print(f(False))