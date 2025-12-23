###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Lukasz'   # replace Anna with your name
surname = 'Wos' # replace May with your surname
characters_in_name = len(name)

print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {(len(name) + len(" ") + len(surname))}') # with a space between name and surname
print()


def f(imie, nazwisko):
    characters1 = len(imie)
    characters2 = len(nazwisko)
    characters3 = characters1 + len(" ") + characters2
    array = [str(characters1), str(characters2), str(characters3)]
    return " ".join(array)

def f1(imie, nazwisko):
    characters1 = len(imie)
    characters2 = len(nazwisko)
    characters3 = characters1 + len(" ") + characters2
    array = [characters1, characters2, characters3]
    array2 = []
    for x in array:
        array2.append(str(x))
    return " ".join(array2)
    
def f2(imie, nazwisko):
    characters1 = len(imie)
    characters2 = len(nazwisko)
    characters3 = characters1 + len(" ") + characters2
    array = [characters1, characters2, characters3]
    result = list(map(lambda x: str(x), array))
    return " ".join(result)



if __name__ == "__main__":
    print("Liczba liter w imieniu, nazwisku i łącznie(ze spacją): ")
    result = f2("Łukasz", "Woś")
    print(result)
    # array = ["abc", "a", "ab"]
    # result = list(map(lambda x: len(x), array))
    # print(result)