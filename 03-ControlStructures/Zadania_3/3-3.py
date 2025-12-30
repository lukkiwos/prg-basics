###
# Checking if discount is available
# The discount is available to children under 18,
# or people 65 or older.
#
age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print(f"Discount for age {age} is available")
else:
    print("Discount is NOT available")
print()


def f(wiek):
    if wiek < 18 or wiek >= 65:
        return f"Znizka dla wieku {wiek} jest dostępna"
    else:
        return "Znizka NIE jest dostępna"
    

if __name__ == "__main__":
    print(f(17))
    print(f(66))
    print(f(54))