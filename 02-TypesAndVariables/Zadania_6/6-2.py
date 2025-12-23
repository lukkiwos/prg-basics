###
# A program that prints your initials
#
name = 'Łukasz'
surname = 'Woś'
print(name[0])
print(surname[0])
print()


def f(imie, nazwisko):
    array = imie[0], nazwisko[0]
    return "".join(array)

if __name__ == "__main__":
    result = f("Łukasz", "Woś")
    print(result)