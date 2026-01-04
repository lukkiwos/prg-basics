def f(text, letter):
    count = 0

    for x in text:
        if x == letter:
            count += 1
    
    return f"The number of letter {letter} is: {count}"




def f1(letter):
    text = "You never get a second chance to make a first impression"
    count = 0

    for x in text:
        if x == letter:
            count += 1

    return f"Liczba liter {letter} to: {count}"






if __name__ == "__main__":
    print(f("You never get a second chance to make a first impression", "e"))
    print()
    print(f1("e"))