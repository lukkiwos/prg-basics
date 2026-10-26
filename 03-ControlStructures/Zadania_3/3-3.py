###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print("Eligible for discount")
else:
    print("Not eligible for discount")
print()


def f(wiek):
    if wiek >= 65 or wiek < 18:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f(17))
    print(f(18))
    print(f(65))
    